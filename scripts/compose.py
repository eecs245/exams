#!/usr/bin/env python3
"""Read questions from exams/ and render them into composed pages.

One exam is one folder. It holds that exam's questions, their images, its
metadata, and -- once composed -- its own generated page:

    exams/<term>-<exam>/q<NN>.md            question: metadata header + body
    exams/<term>-<exam>/q<NN>-preamble.md   optional note above that heading
    exams/<term>-<exam>/imgs/*              images the questions reference
    exams/<term>-<exam>/exam.yml            exam-level metadata
    exams/<term>-<exam>/index.md            GENERATED -- never hand-edited

Both consumers -- scripts/build_exam_pages.py and scripts/build_worksheets.py --
go through this module, so an exam page and a topic worksheet render the same
question identically. Nothing here parses a generated page; pages are output
only.

Question sources sit in a published directory but are not themselves served:
_config.yml excludes exams/*/q*.md and exams/*/exam.yml from the Jekyll build.
That exclusion is load-bearing -- the header below is NOT valid YAML (values are
taken verbatim from the first ": " onward so heading_suffix can hold raw badge
HTML full of colons and quotes), so Jekyll would fail parsing it as front
matter. CI also runs bare Python with no PyYAML, hence the hand-rolled parser.
"""
from __future__ import annotations

import re
import shutil
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
EXAMS_DIR = REPO_ROOT / "exams"

HEADER_DELIMITER = "---"


def question_filename(number: int) -> str:
    """q1 -> q01. Zero-padded so a directory listing sorts in exam order."""
    return f"q{number:02d}"


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
            "(run scripts/convert_exams.sh first)"
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


def read_exam_meta(exam: str) -> dict[str, str]:
    path = EXAMS_DIR / exam / "exam.yml"
    if not path.exists():
        raise SystemExit(f"No exam metadata at {path.relative_to(REPO_ROOT)}")
    fields, _ = read_header(path.read_text(), path)
    return fields


def iter_exams() -> list[str]:
    return [path.parent.name for path in sorted(EXAMS_DIR.glob("*/exam.yml"))]


# ===> Rendering into a page <=== #

def emit_question(question: Question, page_dir: Path, heading: str, note: str = "") -> str:
    """Render one question for a page, copying the images it needs.

    `note` is page-specific text placed directly under the heading (the
    worksheets use it to credit the exam a question came from).

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
        destination.mkdir(parents=True, exist_ok=True)
        for image in question.images:
            source = question.directory / "imgs" / image
            if not source.exists():
                raise SystemExit(f"{question.id}: missing image {source}")
            shutil.copy2(source, destination / image)
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


def clear_generated_images(page_dir: Path) -> None:
    """Drop a composed page's imgs/ so dropped questions leave no orphans.

    Only for pages that own copies (worksheets). Never call this on an exam
    folder -- that imgs/ holds the source images, not copies of them.
    """
    if (page_dir / "exam.yml").exists():
        raise SystemExit(f"Refusing to clear source images in {page_dir}")
    images = page_dir / "imgs"
    if images.exists():
        shutil.rmtree(images)
