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
only, written to .build/ and published by _plugins/composed_pages.rb. src/ is excluded from the Jekyll build in _config.yml. Both YAML files are
read with scripts/miniyaml.py, since CI has no PyYAML.
"""
from __future__ import annotations

import hashlib
import html
import re
import shutil
import sys
from dataclasses import dataclass, field
from decimal import Decimal, InvalidOperation
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import miniyaml  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[1]
QUESTIONS_DIR = REPO_ROOT / "src"      # the only content tree
# Everything composed lands here, never in the source tree: it is rebuilt on
# every build, so a copy at the repo root would only invite edits that get
# overwritten. _plugins/composed_pages.rb publishes it; the pages exist only
# in _site. Gitignored, and excluded in _config.yml so Jekyll neither reads
# nor watches it.
BUILD_DIR = REPO_ROOT / ".build"
EXAMS_DIR = BUILD_DIR / "exams"            # composed exam pages
WORKSHEETS_DIR = BUILD_DIR / "worksheets"  # composed topic worksheets
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
POINTS_NUMBER = r"\d+(?:\.\d+)?"
POINTS_MARKUP = (
    rf'(?P<points_markup><span class="badge badge-points">(?P<badge>{POINTS_NUMBER}) pts?</span>'
    rf'|\((?P<plain>{POINTS_NUMBER}) pts?\))'
)
LETTERED_PART = re.compile(
    r'^<div class="assignment-part-label">(?P<part>[a-z])\)</div>\n'
    r'<div class="assignment-part-content" markdown="1">\n[ \t]*'
    + POINTS_MARKUP, re.M
)
ROMAN_LIST = re.compile(r'^<ol class="roman">\n.*?^</ol>', re.M | re.S)
ROMAN_ITEM = re.compile(r'^<li markdown="1">\n[ \t]*(?:' + POINTS_MARKUP + r')?', re.M)
ROMAN_LABELS = ("i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x")


@dataclass(frozen=True)
class Part:
    label: str
    points: str
    start: int
    end: int


def graded_parts(body: str, points: str) -> list[Part]:
    """Locate scored lettered parts, or a scored Roman list in an unlettered problem."""
    def part_at(label: str, match: re.Match[str]) -> Part:
        return Part(label, match["badge"] or match["plain"], *match.span("points_markup"))

    lettered = [part_at(match["part"], match) for match in LETTERED_PART.finditer(body)]
    if lettered:
        return lettered

    for group in ROMAN_LIST.finditer(body):
        items = list(ROMAN_ITEM.finditer(body, group.start(), group.end()))
        if not items or len(items) > len(ROMAN_LABELS) or not all(m["points_markup"] for m in items):
            continue
        parts = [part_at(label, match) for label, match in zip(ROMAN_LABELS, items)]
        if re.fullmatch(POINTS_NUMBER, points) and sum(Decimal(p.points) for p in parts) == Decimal(points):
            return parts
    return []


def points_badge(points: str, average_controls: str = "") -> str:
    unit = "pt" if points == "1" else "pts"
    value = f"<strong>{points}</strong> {unit}"
    if average_controls:
        return (
            f'<span class="badge badge-points badge-with-average">'
            f'<span class="points-value">{value}</span>{average_controls}</span>'
        )
    return f'<span class="badge badge-points">{value}</span>'


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
    average_points: Decimal | None = None
    parts: list[Part] = field(default_factory=list)
    part_averages: dict[str, Decimal] = field(default_factory=dict)

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
    def title_suffix(self) -> str:
        return f": {escape_title(self.title)}" if self.title else ""

    @property
    def flag_badges(self) -> str:
        return "".join(
            f' <span class="badge badge-flag" data-flag="{flag}">{flag_label(flag)}</span>'
            for flag in self.flags
        )


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


def checked_average(value: object, points: str, location: str) -> Decimal:
    try:
        average = Decimal(str(value))
        maximum = Decimal(points)
        if average.is_finite() and maximum.is_finite() and maximum > 0 and 0 <= average <= maximum:
            return average
    except InvalidOperation:
        pass
    raise SystemExit(f"{location}: expected an average between zero and the available points")


def read_question(question_id: str) -> Question:
    exam, number = question_id_parts(question_id)
    folder = QUESTIONS_DIR / exam / question_filename(number)
    body_path = folder / BODY_FILE
    if not body_path.exists():
        raise SystemExit(
            f"No question at {body_path.relative_to(REPO_ROOT)} "
            "(run scripts/build.sh first)"
        )
    config_path = folder / CONFIG_FILE
    config = read_config(config_path)
    flags = config.get("flags") or []
    if not isinstance(flags, list):
        raise SystemExit(f"{(folder / CONFIG_FILE).relative_to(REPO_ROOT)}: flags must be a list")
    preamble_path = folder / PREAMBLE_FILE
    raw_points = config.get("points")
    points = "" if raw_points in (None, "") else str(raw_points)
    body = body_path.read_text().rstrip()
    parts = graded_parts(body, points)
    points_by_part = {part.label: part.points for part in parts}
    raw_part_averages = config.get("part_averages")
    location = config_path.relative_to(REPO_ROOT)
    part_averages = {}
    if raw_part_averages is not None:
        if not isinstance(raw_part_averages, dict):
            raise SystemExit(f"{location}: part_averages must map part labels to average points")
        for label, value in raw_part_averages.items():
            if label not in points_by_part:
                raise SystemExit(f"{location}: no scored part ({label}) for part_averages")
            part_averages[label] = checked_average(
                value, points_by_part[label], f"{location}: part_averages.{label}"
            )
    average = config.get("average_points")
    average_points = (
        checked_average(average, points, f"{location}: average_points")
        if average is not None and not parts else None
    )
    return Question(
        exam=exam,
        number=number,
        body=body,
        preamble=preamble_path.read_text().strip() if preamble_path.exists() else "",
        title=str(config.get("title") or ""),
        points=points,
        flags=[str(flag) for flag in flags],
        videos=videos_from_config(config),
        average_points=average_points,
        parts=parts,
        part_averages=part_averages,
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
        for key in ("pdf", "solutions"):
            # A path that does not exist still renders a button -- one that 404s,
            # which nobody notices until a student clicks it.
            target = str(entry.get(key) or "")
            if target and not target.startswith(("http://", "https://")):
                if not (REPO_ROOT / target.lstrip("/")).is_file():
                    raise SystemExit(
                        f"{REGISTRY_PATH.name}: {exam_id!r} has {key}: {target} but that file does "
                        f"not exist. Paths are relative to the repo root, e.g. resources/exams/{exam_id}.pdf"
                    )
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


def average_score_controls(average: Decimal, points: str, score_id: str, label: str) -> str:
    percentage = 100 * average / Decimal(points)
    button = (
        f'<button class="score-toggle" type="button" aria-label="Class average for {label}"'
        f' aria-expanded="false" aria-controls="{score_id}" title="Class average">'
        '<svg class="score-icon" viewBox="0 0 16 16" width="14" height="14" '
        'fill="none" stroke="currentColor" stroke-width="3" aria-hidden="true">'
        '<path d="M3 15v-5m5 5V6m5 9V2"/></svg>'
        '</button>'
    )
    unit = "pt" if points == "1" else "pts"
    score = (
        f'<span class="score-value" id="{score_id}" hidden>'
        f'Class average <strong>{average:.2f} / {points} {unit} ({percentage:.0f}%)</strong></span>'
    )
    return button + score


def render_heading(question: Question, label: str) -> tuple[str, str]:
    """(html, anchor) for a question heading.

    `label` is the page's name for the question ("Problem 4" on its exam page,
    "FA25 MT1 · Problem 4" on a worksheet). The anchor is computed with plain
    points and flag badges before rendering the video and average controls.
    """
    title = f"{label}{question.title_suffix}"
    points = f" {points_badge(question.points)}" if question.points else ""
    flags = question.flag_badges
    anchor = heading_anchor(f"{title}{points}{flags}")
    if question.average_points is not None:
        controls = average_score_controls(
            question.average_points, question.points, f"{anchor}-average-score",
            f"Problem {question.number}"
        )
        points = f" {points_badge(question.points, controls)}"
    # markdown="span": Kramdown still renders the heading's inner text as inline
    # Markdown (pandoc's "\..." escapes, "\\(" math delimiters), exactly as it
    # did when the heading was "## ...", while the id attribute is ours.
    return f'<h2 id="{anchor}" markdown="span">{title}{points}{flags}{video_badges(question)}</h2>', anchor


# ===> Rendering into a page <=== #

def render_part_scores(question: Question) -> str:
    body = question.body
    for part in reversed(question.parts):
        controls = ""
        if part.label in question.part_averages:
            controls = average_score_controls(
                question.part_averages[part.label], part.points,
                f"{question.slug}-part-{part.label}-average-score",
                f"Problem {question.number}, part ({part.label})"
            )
        badge = points_badge(part.points, controls)
        body = body[:part.start] + badge + body[part.end:]

    def style_roman_points(group: re.Match[str]) -> str:
        def replace(match: re.Match[str]) -> str:
            points = match["badge"] or match["plain"]
            if not points:
                return match[0]
            prefix = match[0][:match.start("points_markup") - match.start()]
            return prefix + points_badge(points)

        # Keep the printed point values on nested Roman items in the same
        # style. Their average, when available, is already on the parent part.
        return ROMAN_ITEM.sub(replace, group[0])

    return ROMAN_LIST.sub(style_roman_points, body)


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
    body = render_part_scores(question)
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
