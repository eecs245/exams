#!/usr/bin/env python3
"""Read questions from src/ and render them into composed pages.

One question is one folder, and the folder separates what conversion owns from
what people own:

    src/<term>-<exam>/q<NN>/src.md        the question body. GENERATED from the
                                          LaTeX; rewritten on every conversion.
    src/<term>-<exam>/q<NN>/config.yml    title, points, flags, video links.
                                          Written ONCE, when the question is
                                          first converted, then never touched
                                          again -- it is yours to edit. If the
                                          LaTeX later disagrees, conversion
                                          warns; it does not overwrite.
    src/<term>-<exam>/q<NN>/preamble.md   optional note rendered above the heading
    src/<term>-<exam>/q<NN>/imgs/*        the question's images
    src/<term>-<exam>/.extracted          fingerprint of the source extracted

Nothing about a question is stored twice. Its heading -- title, points badge,
flag badges, video badges -- is rendered from config.yml every time; its image
list is whatever is in imgs/.

Exam-level metadata (title, PDFs, playlist) is one entry in _data/exams.yml,
the registry, keyed by the folder name. Jekyll reads that file too, so the front
page and the composed pages agree by construction. See load_registry.

Both consumers -- scripts/build_exam_pages.py and scripts/build_worksheets.py --
go through this module, so an exam page and a topic worksheet render the same
question identically. Nothing here parses a generated page; pages are output
only. src/ is excluded from the Jekyll build in _config.yml. Both YAML files are
read with scripts/miniyaml.py, since CI has no PyYAML.
"""
from __future__ import annotations

import hashlib
import html
import re
import shutil
import sys
from dataclasses import dataclass, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import miniyaml  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[1]
QUESTIONS_DIR = REPO_ROOT / "src"      # the only content tree
EXAMS_DIR = REPO_ROOT / "exams"        # composed exam pages (output)
SOURCES_DIR = REPO_ROOT / "_sources" / "exams"
SCRIPTS_DIR = REPO_ROOT / "scripts"
REGISTRY_PATH = REPO_ROOT / "_data" / "exams.yml"

# Per-exam record of what the questions were extracted from; see
# source_fingerprint. A dotfile so Jekyll never serves it.
EXTRACTED_STAMP = ".extracted"

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


# ===> Questions <=== #

CONFIG_FILE = "config.yml"
BODY_FILE = "src.md"
PREAMBLE_FILE = "preamble.md"
QUESTION_DIR_PATTERN = re.compile(r"^q(\d+)$")


@dataclass
class Question:
    exam: str
    number: int
    body: str
    preamble: str = ""
    title: str = ""                    # plain text, as typed in config.yml
    points: str = ""
    flags: list[str] = field(default_factory=list)
    videos: list[tuple[str, str]] = field(default_factory=list)  # (part, url)

    @property
    def id(self) -> str:
        return f"{self.exam}/{question_filename(self.number)}"

    @property
    def slug(self) -> str:
        """Filesystem-safe form of the id, used to namespace copied images."""
        return f"{self.exam}-{question_filename(self.number)}"

    @property
    def directory(self) -> Path:
        return QUESTIONS_DIR / self.exam / question_filename(self.number)

    @property
    def images(self) -> list[str]:
        folder = self.directory / "imgs"
        return sorted(p.name for p in folder.iterdir() if p.is_file()) if folder.is_dir() else []

    @property
    def heading_suffix(self) -> str:
        """': Title <points badge> <flag badges>' -- rendered, never stored."""
        suffix = f": {escape_title(self.title)}" if self.title else ""
        if self.points:
            unit = "pt" if str(self.points) == "1" else "pts"
            suffix += f' <span class="badge badge-points">{self.points} {unit}</span>'
        for flag in self.flags:
            suffix += f' <span class="badge badge-flag" data-flag="{flag}">{flag_label(flag)}</span>'
        return suffix


def escape_title(title: str) -> str:
    """Markdown-escape a plain title for a heading rendered with markdown="span".

    Without this Kramdown would turn "..." into an ellipsis character and read
    * or _ as emphasis. unescape_title is the inverse, used when a title is
    first seeded from pandoc's already-escaped output.
    """
    title = re.sub(r"([\\*_`])", r"\\\1", title)
    return title.replace("...", "\\...")


def unescape_title(markdown_title: str) -> str:
    return re.sub(r"\\([\\.*_`!#\[\]~-])", r"\1", markdown_title)


def flag_label(flag_id: str) -> str:
    """Badge text for a flag id: mt1-redemption -> 'MT1 Redemption'."""
    match = re.fullmatch(r"mt(\d+)-redemption", flag_id)
    if match:
        return f"MT{match.group(1)} Redemption"
    return flag_id.replace("-", " ").title()


def question_id_parts(question_id: str) -> tuple[str, int]:
    match = re.fullmatch(r"([\w-]+)/q(\d+)", question_id)
    if not match:
        raise SystemExit(
            f"Bad question id {question_id!r} (expected <term>-<exam>/qNN)"
        )
    exam, number = match.groups()
    return exam, int(number)


def read_config(path: Path) -> dict:
    config = miniyaml.load_file(path) if path.exists() else None
    if config is None:
        return {}
    if not isinstance(config, dict):
        raise SystemExit(f"{path.relative_to(REPO_ROOT)}: expected key: value pairs")
    return config


def videos_from_config(config: dict) -> list[tuple[str, str]]:
    """(part, url) pairs from video / video_<part> keys; part is "" for whole-problem."""
    videos: list[tuple[str, str]] = []
    for key, value in config.items():
        if not value:
            continue
        if key == "video":
            videos.append(("", str(value).strip()))
        elif key.startswith("video_") and key[len("video_"):]:
            videos.append((key[len("video_"):], str(value).strip()))
    return videos


def read_question(question_id: str) -> Question:
    exam, number = question_id_parts(question_id)
    folder = QUESTIONS_DIR / exam / question_filename(number)
    body_path = folder / BODY_FILE
    if not body_path.exists():
        raise SystemExit(
            f"No question at {body_path.relative_to(REPO_ROOT)} "
            "(run scripts/build.sh first)"
        )
    config = read_config(folder / CONFIG_FILE)
    flags = config.get("flags") or []
    if not isinstance(flags, list):
        raise SystemExit(f"{(folder / CONFIG_FILE).relative_to(REPO_ROOT)}: flags must be a list")
    preamble_path = folder / PREAMBLE_FILE
    points = config.get("points")
    return Question(
        exam=exam,
        number=number,
        body=body_path.read_text().rstrip(),
        preamble=preamble_path.read_text().strip() if preamble_path.exists() else "",
        title=str(config.get("title") or ""),
        points="" if points in (None, "") else str(points),
        flags=[str(flag) for flag in flags],
        videos=videos_from_config(config),
    )


def read_exam_questions(exam: str) -> list[Question]:
    numbers = sorted(
        int(match.group(1))
        for path in (QUESTIONS_DIR / exam).iterdir()
        if path.is_dir() and (match := QUESTION_DIR_PATTERN.match(path.name))
        and (path / BODY_FILE).exists()
    )
    return [read_question(f"{exam}/{question_filename(n)}") for n in numbers]


# config.yml is written exactly once per question. After that, conversion only
# ever compares against it.
CONFIG_COMMENT = (
    "# Hand-editable; conversion never overwrites this file.\n"
    "# Keys: title, points, flags (list), video (whole problem), video_<part> (e.g. video_c).\n"
)


def yaml_scalar(value: str) -> str:
    if value == "":
        return ""
    if '"' not in value:
        return f'"{value}"'
    return f"'{value}'"


def seed_config(path: Path, title: str, points: str, flags: list[str]) -> None:
    lines = [CONFIG_COMMENT.rstrip("\n"), f"title: {yaml_scalar(title)}".rstrip(), f"points: {points}".rstrip()]
    if flags:
        lines.append("flags:")
        lines.extend(f"  - {flag}" for flag in flags)
    else:
        lines.append("flags:")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n")


def config_drift(path: Path, title: str, points: str, flags: list[str]) -> list[str]:
    """Human-readable differences between config.yml and what the LaTeX now says."""
    config = read_config(path)
    have = {"title": str(config.get("title") or ""),
            "points": "" if config.get("points") in (None, "") else str(config.get("points")),
            "flags": [str(f) for f in (config.get("flags") or [])]}
    want = {"title": title, "points": points, "flags": flags}
    return [f"{key}: {have[key]!r} but the LaTeX now says {want[key]!r}" for key in want if have[key] != want[key]]


# ===> The exam registry: _data/exams.yml <=== #
# The one hand-maintained list of exams. Jekyll reads it too (site.data.exams
# drives the front page), so the same entry names an exam everywhere.

REQUIRED_REGISTRY_KEYS = ("id", "term", "exam", "pdf")


def load_registry() -> list[dict]:
    """Every exam, in front-page order, checked against src/ both ways.

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
        if not (QUESTIONS_DIR / exam_id).is_dir():
            raise SystemExit(
                f"{REGISTRY_PATH.name} lists {exam_id!r} but src/{exam_id}/ does not exist "
                f"(drop the source into _sources/exams/{exam_id}/ and run the build)"
            )

    unregistered = sorted(
        path.name for path in QUESTIONS_DIR.iterdir() if path.is_dir() and path.name not in seen
    )
    if unregistered:
        raise SystemExit(
            "src/ has folders with no entry in _data/exams.yml: "
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
    stamp = QUESTIONS_DIR / exam / EXTRACTED_STAMP
    return stamp.read_text().strip() if stamp.exists() else None


# ===> Headings <=== #

def heading_anchor(heading_html: str) -> str:
    """The id Kramdown would have generated for this heading's text.

    Headings are emitted as HTML (so a video badge can sit in them without
    changing their anchor), which means Kramdown no longer assigns ids -- so
    this reproduces its algorithm exactly: take the text content, drop
    leading non-letters, keep only ASCII letters, digits, spaces and hyphens,
    turn each space into a hyphen WITHOUT collapsing runs (which is why a
    removed middle dot leaves a double hyphen), lowercase.
    """
    text = html.unescape(re.sub(r"<[^>]+>", "", heading_html))
    text = re.sub(r"^[^A-Za-z]+", "", text)
    text = re.sub(r"[^A-Za-z0-9 -]", "", text)
    return text.replace(" ", "-").lower()


def video_badges(question: Question) -> str:
    return "".join(
        f' <a class="badge badge-video" href="{url}" target="_blank" rel="noopener">'
        f'🎥 {("Part " + part) if part else "Walkthrough"}</a>'
        for part, url in question.videos
    )


def render_heading(question: Question, label: str) -> tuple[str, str]:
    """(html, anchor) for a question heading.

    `label` is the page's name for the question ("Problem 4" on its exam page,
    "FA25 MT1 · Problem 4" on a worksheet); heading_suffix is the title, points
    and flag badges rendered from config.yml. The anchor is computed BEFORE the video badge is appended, so
    adding or removing a video never changes a link into the page.
    """
    core = f"{label}{question.heading_suffix}"
    anchor = heading_anchor(core)
    # markdown="span": Kramdown still renders the heading's inner text as inline
    # Markdown (pandoc's "\..." escapes, "\\(" math delimiters), exactly as it
    # did when the heading was "## ...", while the id attribute is ours.
    return f'<h2 id="{anchor}" markdown="span">{core}{video_badges(question)}</h2>', anchor


# ===> Rendering into a page <=== #

def emit_question(
    question: Question,
    page_dir: Path,
    heading: str,
    note: str = "",
    copied_to: set[Path] | None = None,
    namespace_images: bool = True,
) -> str:
    """Render one question for a page, copying the images it needs.

    `note` is page-specific text placed directly under the heading (the
    worksheets use it to credit the exam a question came from). `copied_to`,
    if given, collects the image paths written under page_dir so the caller
    can prune whatever else is left there (see prune_images).

    With namespace_images (worksheets) images go to <page_dir>/imgs/<slug>/: a
    chapter gathers questions from several exams, and two terms reusing a
    figure name would otherwise overwrite each other. An exam page holds one
    exam's questions, whose figure names are already unique, so it copies flat
    into <page_dir>/imgs/ and its references need no rewriting.
    """
    body = question.body
    preamble = question.preamble
    if question.images:
        destination = page_dir / "imgs" / question.slug if namespace_images else page_dir / "imgs"
        for image in question.images:
            source = question.directory / "imgs" / image
            copy_if_changed(source, destination / image)
            if copied_to is not None:
                copied_to.add((destination / image).resolve())
        if namespace_images:
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
    would rebuild on. Composed pages only -- never the question tree, whose
    imgs/ folders are the originals.
    """
    if QUESTIONS_DIR in page_dir.resolve().parents or page_dir.resolve() == QUESTIONS_DIR:
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
