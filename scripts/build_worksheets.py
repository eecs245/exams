#!/usr/bin/env python3
"""Build topic-specific worksheet pages from the question tree.

Reads _data/worksheet_topics.yml and, for each chapter, assembles
worksheets/chapter-<n>/index.md from the questions it lists. Questions come
straight out of exams/ via scripts/compose.py -- the same route
scripts/build_exam_pages.py takes -- so a worksheet and an exam page render an
identical question identically, and no generated page is ever parsed to recover
its contents.

Problem IDs are <term>-<exam>/q<NN>, e.g. sp26-mt1/q02, which is also that
question's path: exams/sp26-mt1/q02.md. Entries may instead be mappings
{id, pdf} for exams that have no web view (mocks); those render as PDF links in
a trailing section.

No third-party dependencies: the YAML subset used by worksheet_topics.yml
is parsed directly, so CI needs nothing but Python.
"""
from __future__ import annotations

import html
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import compose  # noqa: E402
from generate_exam_markdown import (  # noqa: E402
    EXAM_NAV_SNIPPET,
    HOMEWORK_STYLE_SNIPPET,
    MATHJAX_SNIPPET,
    replace_inline_math_spans_with_dollars,
)

TOPICS_YML = REPO_ROOT / "_data" / "worksheet_topics.yml"
WORKSHEETS_DIR = REPO_ROOT / "worksheets"


# ===> Minimal YAML parsing (only the shape worksheet_topics.yml uses) <=== #

def parse_topics_yaml(text: str) -> list[dict]:
    chapters: list[dict] = []
    current: dict | None = None
    pending_mapping: dict | None = None
    for raw in text.splitlines():
        line = raw.rstrip()
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if match := re.match(r"^- chapter:\s*(\d+)$", line):
            current = {"chapter": int(match.group(1)), "name": "", "summary": "", "problems": []}
            chapters.append(current)
            pending_mapping = None
        elif current is None:
            raise SystemExit(f"worksheet_topics.yml: entry before first chapter: {line!r}")
        elif match := re.match(r'^\s+name:\s*"(.*)"$', line):
            current["name"] = match.group(1)
        elif match := re.match(r'^\s+summary:\s*"(.*)"$', line):
            current["summary"] = match.group(1)
        elif re.match(r"^\s+problems:\s*$", line):
            pass
        elif match := re.match(r"^\s+- id:\s*(\S+)$", line):
            pending_mapping = {"id": match.group(1)}
            current["problems"].append(pending_mapping)
        elif match := re.match(r'^\s+pdf:\s*"(.*)"$', line):
            if pending_mapping is None:
                raise SystemExit(f"worksheet_topics.yml: pdf without id: {line!r}")
            pending_mapping["pdf"] = match.group(1)
            pending_mapping = None
        elif match := re.match(r"^\s+-\s*(\S+)$", line):
            current["problems"].append(match.group(1))
            pending_mapping = None
        else:
            raise SystemExit(f"worksheet_topics.yml: unrecognized line: {line!r}")
    return chapters


# ===> Labels <=== #

def exam_label_for(exam_dir: str) -> str:
    term, _, exam = exam_dir.partition("-")
    exam_display = {"mt1": "MT1", "mt2": "MT2", "final": "Final"}.get(exam, exam.upper())
    return f"{term.upper()} {exam_display}"


# ===> Page assembly <=== #

def heading_anchor(heading_text: str) -> str:
    """Kramdown-compatible ID for a rendered heading line.

    Kramdown maps each whitespace character to a dash WITHOUT collapsing
    runs, so "FA25 MT1 · Problem 4" (middle dot removed, leaving two
    spaces) becomes fa25-mt1--problem-4 with a double dash.
    """
    text = replace_inline_math_spans_with_dollars(heading_text)
    text = re.sub(r"<[^>]+>", "", text)
    text = html.unescape(text)
    anchor = re.sub(r"[^\w\s-]", "", text.lower())
    return re.sub(r"\s", "-", anchor.strip())


def build_chapter_page(chapter: dict) -> str:
    title = f"Chapter {chapter['chapter']}: {chapter['name']}"
    sections: list[str] = []
    toc_lines: list[str] = ["## Problems", ""]
    pdf_only: list[dict] = []
    page_dir = WORKSHEETS_DIR / f"chapter-{chapter['chapter']}"
    compose.clear_generated_images(page_dir)

    for entry in chapter["problems"]:
        if isinstance(entry, dict):
            pdf_only.append(entry)
            continue
        question = compose.read_question(entry)
        label = exam_label_for(question.exam)
        number = question.number
        heading_line = f"## {label} · Problem {number}{question.heading_suffix}"
        anchor = heading_anchor(heading_line[3:])
        toc_lines.append(f"- [{label} · Problem {number}](#{anchor})")
        source_note = (
            f'<p class="worksheet-source">From '
            f'<a href="/exams/{question.exam}/">{label}</a></p>'
        )
        rendered = compose.emit_question(question, page_dir, heading_line, note=source_note)
        sections.append(f"{rendered.rstrip()}\n\n---\n")

    parts = [
        "---",
        "layout: minimal",
        f'title: "{title}"',
        f'description: "Practice problems for {title}."',
        "nav_exclude: true",
        "hide_footer_hr: true",
        "---",
        "",
        "{% raw %}",
        "",
        MATHJAX_SNIPPET,
        "",
        HOMEWORK_STYLE_SNIPPET,
        "",
        WORKSHEET_STYLE_SNIPPET,
        "",
        EXAM_NAV_SNIPPET,
        "",
        f"# {title}",
        "",
    ]
    if chapter["summary"]:
        parts.extend([f"*Topics: {chapter['summary']}*", ""])
    parts.extend(
        [
            "*Problems below are collected from past exams; each links back to its "
            "full exam. Solutions are in the dropdowns.*",
            "",
            "\n".join(toc_lines),
            "",
            "---",
            "",
        ]
    )
    parts.extend(sections)
    if pdf_only:
        parts.append("## More practice (PDF only)\n")
        for entry in pdf_only:
            exam, number = compose.question_id_parts(entry["id"])
            label = exam_label_for(exam)
            parts.append(f"- [{label} Problem {number}](/{entry['pdf']})")
        parts.append("")
    parts.extend(["{% endraw %}", ""])
    return "\n".join(parts)


WORKSHEET_STYLE_SNIPPET = """<style>
.worksheet-source { font-size: 0.8rem; color: #57606a; margin: -0.4rem 0 0.8rem; }
.worksheet-source a { color: #0066cc; }
</style>"""


def build_index_page(chapters: list[dict]) -> str:
    lines = [
        "---",
        "layout: minimal",
        'title: "Problems by Topic"',
        'description: "Topic-specific worksheets of past exam problems."',
        "nav_exclude: true",
        "hide_footer_hr: true",
        "---",
        "",
        EXAM_NAV_SNIPPET,
        "",
        "# Problems by Topic",
        "",
        "Worksheets of past exam problems, organized by chapter of the "
        "[course notes](https://notes.eecs245.org). Solutions included as dropdowns.",
        "",
    ]
    for chapter in chapters:
        count = len(chapter["problems"])
        lines.append(
            f"- **[Chapter {chapter['chapter']}: {chapter['name']}]"
            f"(/worksheets/chapter-{chapter['chapter']}/)** — "
            f"{count} problem{'s' if count != 1 else ''}. *{chapter['summary']}*"
        )
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    chapters = parse_topics_yaml(TOPICS_YML.read_text())
    if not chapters:
        raise SystemExit("worksheet_topics.yml defines no chapters")
    for chapter in chapters:
        out = WORKSHEETS_DIR / f"chapter-{chapter['chapter']}" / "index.md"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(build_chapter_page(chapter))
        embedded = sum(1 for p in chapter["problems"] if isinstance(p, str))
        pdf = len(chapter["problems"]) - embedded
        print(f"chapter-{chapter['chapter']}: {embedded} embedded, {pdf} pdf-only")
    (WORKSHEETS_DIR / "index.md").write_text(build_index_page(chapters))
    print(f"Wrote {len(chapters)} worksheets + index to {WORKSHEETS_DIR.relative_to(REPO_ROOT)}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
