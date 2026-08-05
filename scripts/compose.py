#!/usr/bin/env python3
"""Read questions from _questions/ and render them into composed pages.

_questions/ is the only content tree in this repo. One question is one folder:

    _questions/<term>/<exam>/q<N>/index.md    metadata header + body
    _questions/<term>/<exam>/q<N>/imgs/*      images that question references
    _questions/<term>/<exam>/exam.yml         exam-level metadata

Both consumers -- scripts/build_exam_pages.py and scripts/build_worksheets.py --
go through this module, so an exam page and a topic worksheet render the same
question identically. Nothing here parses a generated page; pages are output
only.

Neither Jekyll nor any third-party library reads these files: _questions/ is
underscore-prefixed so Jekyll skips it, and CI runs bare Python with no PyYAML.
The header is therefore a deliberately small key/value format, parsed by
read_header() below -- values are taken verbatim from the first ": " onward, so
heading_suffix can hold raw badge HTML (full of colons and quotes) without any
escaping.
"""
from __future__ import annotations

import re
import shutil
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
QUESTIONS_DIR = REPO_ROOT / "_questions"

HEADER_DELIMITER = "---"

# Optional per-question file holding an interstitial note that renders above the
# question's heading (see split_body_into_questions in generate_exam_markdown).
PREAMBLE_FILE = "preamble.md"


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
    term: str
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
        return f"{self.term}/{self.exam}/q{self.number}"

    @property
    def slug(self) -> str:
        """Directory-safe form of the id, used to namespace copied images."""
        return f"{self.term}-{self.exam}-q{self.number}"

    @property
    def directory(self) -> Path:
        return QUESTIONS_DIR / self.term / self.exam / f"q{self.number}"


def question_id_parts(question_id: str) -> tuple[str, str, int]:
    match = re.fullmatch(r"(\w+)/(\w+)/q(\d+)", question_id)
    if not match:
        raise SystemExit(f"Bad question id {question_id!r} (expected term/exam/qN)")
    term, exam, number = match.groups()
    return term, exam, int(number)


def read_question(question_id: str) -> Question:
    term, exam, number = question_id_parts(question_id)
    path = QUESTIONS_DIR / term / exam / f"q{number}" / "index.md"
    if not path.exists():
        raise SystemExit(
            f"No question at {path.relative_to(REPO_ROOT)} "
            "(run scripts/convert_exams.sh first)"
        )
    fields, body = read_header(path.read_text(), path)
    preamble_path = path.parent / PREAMBLE_FILE
    return Question(
        term=term,
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


def read_exam_questions(term: str, exam: str) -> list[Question]:
    exam_dir = QUESTIONS_DIR / term / exam
    numbers = sorted(
        int(path.name[1:])
        for path in exam_dir.glob("q*")
        if path.is_dir() and path.name[1:].isdigit()
    )
    return [read_question(f"{term}/{exam}/q{number}") for number in numbers]


def read_exam_meta(term: str, exam: str) -> dict[str, str]:
    path = QUESTIONS_DIR / term / exam / "exam.yml"
    if not path.exists():
        raise SystemExit(f"No exam metadata at {path.relative_to(REPO_ROOT)}")
    fields, _ = read_header(path.read_text(), path)
    return fields


def iter_exams() -> list[tuple[str, str]]:
    exams: list[tuple[str, str]] = []
    for meta_path in sorted(QUESTIONS_DIR.glob("*/*/exam.yml")):
        exams.append((meta_path.parent.parent.name, meta_path.parent.name))
    return exams


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
    if question.images:
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
    """Drop a page's imgs/ so removed questions do not leave orphans behind."""
    images = page_dir / "imgs"
    if images.exists():
        shutil.rmtree(images)
