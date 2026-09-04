#!/usr/bin/env python3
"""Read questions from exams/ and render them into composed pages.

One exam is one folder. It holds that exam's questions, their images, its
metadata, and -- once composed -- its own generated page:

    exams/<term>-<exam>/q<NN>.md            question: metadata header + body
    exams/<term>-<exam>/q<NN>-preamble.md   optional note above that heading
    exams/<term>-<exam>/imgs/*              images the questions reference
    exams/<term>-<exam>/.extracted          fingerprint of the source extracted
    exams/<term>-<exam>/index.md            GENERATED -- never hand-edited

Exam-level metadata (title, PDFs, playlist) is not in the folder at all: it is
one entry in _data/exams.yml, the registry, keyed by the folder name. Jekyll
reads that file too, so the front page and the composed pages agree by
construction. See load_registry.

Both consumers -- scripts/build_exam_pages.py and scripts/build_worksheets.py --
go through this module, so an exam page and a topic worksheet render the same
question identically. Nothing here parses a generated page; pages are output
only.

Question sources sit in a published directory but are not themselves served:
_config.yml excludes exams/*/q*.md from the Jekyll build. That exclusion is
load-bearing -- the question header below is NOT valid YAML (values are taken
verbatim from the first ": " onward so heading_suffix can hold raw badge HTML
full of colons and quotes), so Jekyll would fail parsing it as front matter.
The registry, by contrast, is real YAML: Jekyll parses it with a full parser
and this module with scripts/miniyaml.py, since CI has no PyYAML.
"""
from __future__ import annotations

import hashlib
import re
import shutil
import sys
from dataclasses import dataclass, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import miniyaml  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[1]
EXAMS_DIR = REPO_ROOT / "exams"
SOURCES_DIR = REPO_ROOT / "_sources" / "exams"
SCRIPTS_DIR = REPO_ROOT / "scripts"
REGISTRY_PATH = REPO_ROOT / "_data" / "exams.yml"

# Per-exam record of what the questions were extracted from; see
# source_fingerprint. A dotfile so Jekyll never serves it.
EXTRACTED_STAMP = ".extracted"

HEADER_DELIMITER = "---"


def question_filename(number: int) -> str:
    """q1 -> q01. Zero-padded so a directory listing sorts in exam order."""
    return f"q{number:02d}"


def write_if_changed(path: Path, text: str) -> bool:
    """Write only when the content differs. Returns True if it wrote.

    Every generated file lands inside the Jekyll source tree, so an
    unconditional write would bump its mtime, `jekyll serve --watch` would see
    a change, rebuild, run the hook, write again... Comparing first is what
    keeps that loop from running forever, and it keeps `git status` quiet
    after a no-op build.
    """
    if path.exists() and path.read_text() == text:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)
    return True


def copy_if_changed(source: Path, destination: Path) -> bool:
    """copy2 that leaves an identical destination untouched. See write_if_changed."""
    if destination.exists() and destination.read_bytes() == source.read_bytes():
        return False
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)
    return True


# ===> Header format <=== #

def format_header(fields: dict[str, object]) -> str:
    lines = [HEADER_DELIMITER]
    for key, value in fields.items():
        if isinstance(value, (list, tuple)):
            rendered = "[" + ", ".join(str(item) for item in value) + "]"
        elif isinstance(value, bool):
            rendered = "true" if value else "false"
        else:
            rendered = str(value)
        lines.append(f"{key}: {rendered}")
    lines.append(HEADER_DELIMITER)
    return "\n".join(lines)


def read_header(text: str, source: Path) -> tuple[dict[str, str], str]:
    """Split a question/exam file into its header fields and its body."""
    if not text.startswith(HEADER_DELIMITER + "\n"):
        raise SystemExit(f"{source}: missing header block")
    end = text.find(f"\n{HEADER_DELIMITER}\n", len(HEADER_DELIMITER))
    if end == -1:
        raise SystemExit(f"{source}: unterminated header block")

    fields: dict[str, str] = {}
    for line in text[len(HEADER_DELIMITER) + 1 : end].splitlines():
        if not line.strip():
            continue
        key, separator, value = line.partition(":")
        if not separator:
            raise SystemExit(f"{source}: unrecognized header line: {line!r}")
        # Only the first colon separates key from value; everything after it is
        # verbatim, which is what lets heading_suffix carry raw badge HTML.
        fields[key.strip()] = value[1:] if value.startswith(" ") else value

    return fields, text[end + len(HEADER_DELIMITER) + 2 :].lstrip("\n")


def parse_list(value: str) -> list[str]:
    inner = value.strip().removeprefix("[").removesuffix("]").strip()
    return [item.strip() for item in inner.split(",") if item.strip()]


# ===> Questions <=== #

@dataclass
class Question:
    exam: str
    number: int
    heading_suffix: str
    body: str
    preamble: str = ""
    title: str = ""
    points: str = ""
    flags: list[str] = field(default_factory=list)
    images: list[str] = field(default_factory=list)

    @property
    def id(self) -> str:
        return f"{self.exam}/{question_filename(self.number)}"

    @property
    def slug(self) -> str:
        """Filesystem-safe form of the id, used to namespace copied images."""
        return f"{self.exam}-{question_filename(self.number)}"

    @property
    def directory(self) -> Path:
        return EXAMS_DIR / self.exam


def question_id_parts(question_id: str) -> tuple[str, int]:
    match = re.fullmatch(r"([\w-]+)/q(\d+)", question_id)
    if not match:
        raise SystemExit(
            f"Bad question id {question_id!r} (expected <term>-<exam>/qNN)"
        )
    exam, number = match.groups()
    return exam, int(number)


def read_question(question_id: str) -> Question:
    exam, number = question_id_parts(question_id)
    path = EXAMS_DIR / exam / f"{question_filename(number)}.md"
    if not path.exists():
        raise SystemExit(
            f"No question at {path.relative_to(REPO_ROOT)} "
            "(run scripts/build.sh first)"
        )
    fields, body = read_header(path.read_text(), path)
    preamble_path = path.with_name(f"{path.stem}-preamble.md")
    return Question(
        exam=exam,
        number=number,
        heading_suffix=fields.get("heading_suffix", ""),
        body=body.rstrip(),
        preamble=preamble_path.read_text().strip() if preamble_path.exists() else "",
        title=fields.get("title", ""),
        points=fields.get("points", ""),
        flags=parse_list(fields.get("flags", "[]")),
        images=parse_list(fields.get("images", "[]")),
    )


QUESTION_FILE_PATTERN = re.compile(r"^q(\d+)\.md$")


def read_exam_questions(exam: str) -> list[Question]:
    numbers = sorted(
        int(match.group(1))
        for path in (EXAMS_DIR / exam).glob("q*.md")
        if (match := QUESTION_FILE_PATTERN.match(path.name))
    )
    return [read_question(f"{exam}/{question_filename(n)}") for n in numbers]


# ===> The exam registry: _data/exams.yml <=== #
# The one hand-maintained list of exams. Jekyll reads it too (site.data.exams
# drives the front page), so the same entry names an exam everywhere.

REQUIRED_REGISTRY_KEYS = ("id", "term", "exam", "pdf")


def load_registry() -> list[dict]:
    """Every exam, in front-page order, checked against exams/ both ways.

    An exam folder with no entry, or an entry with no folder, is an error: the
    first would silently drop an exam from the site, the second would promise a
    page that never composes.
    """
    if not REGISTRY_PATH.exists():
        raise SystemExit(f"Missing exam registry {REGISTRY_PATH.relative_to(REPO_ROOT)}")
    entries = miniyaml.load_file(REGISTRY_PATH)
    if not isinstance(entries, list):
        raise SystemExit(f"{REGISTRY_PATH.name}: expected a list of exams")

    seen: set[str] = set()
    for entry in entries:
        if not isinstance(entry, dict):
            raise SystemExit(f"{REGISTRY_PATH.name}: every entry must be a mapping, got {entry!r}")
        missing = [key for key in REQUIRED_REGISTRY_KEYS if not entry.get(key)]
        if missing:
            raise SystemExit(
                f"{REGISTRY_PATH.name}: entry {entry.get('id', '?')!r} is missing {', '.join(missing)}"
            )
        exam_id = str(entry["id"])
        if exam_id in seen:
            raise SystemExit(f"{REGISTRY_PATH.name}: duplicate id {exam_id!r}")
        seen.add(exam_id)
        if not (EXAMS_DIR / exam_id).is_dir():
            raise SystemExit(
                f"{REGISTRY_PATH.name} lists {exam_id!r} but exams/{exam_id}/ does not exist "
                f"(drop the source into _sources/exams/{exam_id}/ and run the build)"
            )

    unregistered = sorted(
        path.name for path in EXAMS_DIR.iterdir() if path.is_dir() and path.name not in seen
    )
    if unregistered:
        raise SystemExit(
            "exams/ has folders with no entry in _data/exams.yml: "
            + ", ".join(unregistered)
            + " -- add each one to the registry (id, term, exam, pdf)."
        )
    return entries


def registry_entry(exam: str) -> dict:
    for entry in load_registry():
        if entry["id"] == exam:
            return entry
    raise SystemExit(f"{exam!r} is not in {REGISTRY_PATH.relative_to(REPO_ROOT)}")


def exam_title(entry: dict) -> str:
    return f"{entry['term']} {entry['exam']}"


def iter_exams() -> list[str]:
    return [entry["id"] for entry in load_registry()]


# ===> Extraction state <=== #

def source_fingerprint(source_dir: Path, scripts_dir: Path = SCRIPTS_DIR) -> str:
    """Content hash of an exam's source plus the code that converts it.

    Timestamps cannot answer "has this changed?" here: git does not preserve
    mtimes, so a fresh clone stamps every file with the checkout time and any
    -newer comparison becomes a coin flip. Hashing content is deterministic and
    survives cloning. The conversion scripts are included so that improving the
    pipeline re-extracts, which is what an mtime check was reaching for.
    """
    digest = hashlib.sha256()
    for path in sorted(p for p in source_dir.rglob("*") if p.is_file()):
        digest.update(path.relative_to(source_dir).as_posix().encode())
        digest.update(path.read_bytes())
    for path in sorted(scripts_dir.glob("*.py")) + sorted(scripts_dir.glob("*.sh")):
        digest.update(path.name.encode())
        digest.update(path.read_bytes())
    return digest.hexdigest()[:16]


def read_extracted_fingerprint(exam: str) -> str | None:
    stamp = EXAMS_DIR / exam / EXTRACTED_STAMP
    return stamp.read_text().strip() if stamp.exists() else None


# ===> Rendering into a page <=== #

def emit_question(
    question: Question,
    page_dir: Path,
    heading: str,
    note: str = "",
    copied_to: set[Path] | None = None,
) -> str:
    """Render one question for a page, copying the images it needs.

    `note` is page-specific text placed directly under the heading (the
    worksheets use it to credit the exam a question came from). `copied_to`,
    if given, collects the image paths written under page_dir so the caller
    can prune whatever else is left there (see prune_images).

    Images are copied into <page_dir>/imgs/<slug>/ rather than a flat imgs/.
    Within a single exam a flat directory would be safe -- those images already
    share one today -- but a worksheet chapter gathers questions from several
    exams, and two terms reusing a figure name would otherwise overwrite each
    other.
    """
    body = question.body
    preamble = question.preamble
    # An exam page is composed into the very folder its questions live in, so
    # its imgs/ references already resolve -- only a page somewhere else (a
    # worksheet) needs its own copy.
    if question.images and page_dir.resolve() != question.directory.resolve():
        destination = page_dir / "imgs" / question.slug
        for image in question.images:
            source = question.directory / "imgs" / image
            if not source.exists():
                raise SystemExit(f"{question.id}: missing image {source}")
            copy_if_changed(source, destination / image)
            if copied_to is not None:
                copied_to.add((destination / image).resolve())
        body = rewrite_image_paths(body, question.slug)
        preamble = rewrite_image_paths(preamble, question.slug)

    blocks = []
    if preamble:
        blocks.append(preamble)
    blocks.append(heading)
    # The note is raw block-level HTML, so it needs a blank line before the body
    # resumes or Kramdown swallows the following markdown as HTML content.
    blocks.append(f"{note}\n\n{body}" if note else body)
    return "\n\n".join(blocks) + "\n"


def rewrite_image_paths(body: str, slug: str) -> str:
    """Point a question's imgs/ references at its namespaced copy on the page."""
    body = re.sub(
        r'\b(src|href)=(["\'])imgs/(?!.*/)',
        rf"\1=\2imgs/{slug}/",
        body,
    )
    return re.sub(r"\]\(imgs/(?![^)]*/)", f"](imgs/{slug}/", body)


def prune_images(page_dir: Path, keep: set[Path]) -> None:
    """Remove copied images under page_dir/imgs that this build did not write.

    Replaces wiping imgs/ before every build: a wipe-and-recopy rewrites every
    image each run, which is exactly the kind of write `jekyll serve --watch`
    would rebuild on. Only for pages that own copies (worksheets); an exam
    folder's imgs/ holds the source images, never copies, so refuse it.
    """
    if EXAMS_DIR in page_dir.resolve().parents or page_dir.resolve() == EXAMS_DIR:
        raise SystemExit(f"Refusing to prune source images in {page_dir}")
    images = page_dir / "imgs"
    if not images.exists():
        return
    for path in sorted(images.rglob("*"), reverse=True):
        if path.is_file() and path.resolve() not in keep:
            path.unlink()
        elif path.is_dir() and not any(path.iterdir()):
            path.rmdir()
    if not any(images.iterdir()):
        images.rmdir()
