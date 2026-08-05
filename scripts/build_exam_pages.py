#!/usr/bin/env python3
"""Compose exam web views from the question tree.

Reads _questions/<term>/<exam>/ and writes exams/<term>/<exam>/index.md. The
page is nothing but its questions plus chrome -- it is never the source of
anything, and nothing reads it back. scripts/build_worksheets.py assembles the
topic worksheets from the same questions by the same route.

Page chrome (MathJax, styles, breadcrumb, disclaimer, table of contents) is
imported from generate_exam_markdown so the LaTeX->HTML pipeline stays the
single definition of how an exam looks.
"""
from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import compose  # noqa: E402
from generate_exam_markdown import (  # noqa: E402
    EXAM_DISCLAIMER,
    EXAM_NAV_SNIPPET,
    HOMEWORK_STYLE_SNIPPET,
    MATHJAX_SNIPPET,
    SECTION_SEPARATOR,
    escape_frontmatter,
    generate_toc,
)

EXAMS_DIR = REPO_ROOT / "exams"


def action_buttons(meta: dict[str, str]) -> str:
    buttons = [
        (meta.get("pdf"), "View as PDF ✏️"),
        (meta.get("solutions_pdf"), "Solutions PDF ✅"),
        (meta.get("videos"), "Video Walkthroughs 🎥"),
    ]
    rendered = [
        f'<a class="btn btn-info assignment-pdf-button" href="{link}" target="_blank">{label}</a>'
        for link, label in buttons
        if link
    ]
    if not rendered:
        return ""
    return '<div class="assignment-actions">\n' + "\n".join(rendered) + "\n</div>"


def build_exam_page(term: str, exam: str) -> tuple[str, int]:
    meta = compose.read_exam_meta(term, exam)
    questions = compose.read_exam_questions(term, exam)
    if not questions:
        raise SystemExit(f"_questions/{term}/{exam} contains no questions")

    page_dir = EXAMS_DIR / term / exam
    compose.clear_generated_images(page_dir)

    body = f"\n\n{SECTION_SEPARATOR}\n\n".join(
        compose.emit_question(
            question,
            page_dir,
            f"## Problem {question.number}{question.heading_suffix}",
        ).rstrip()
        for question in questions
    )

    title = meta.get("title", f"{term.upper()} {exam.upper()}")
    parts = [
        "---",
        f"layout: {meta.get('layout') or 'minimal'}",
        f'title: "{escape_frontmatter(title)}"',
        f'description: "{escape_frontmatter(title)} problems."',
        "nav_exclude: true",
        "hide_footer_hr: true",
    ]
    if meta.get("legacy_path"):
        # Exams used to be published at /exams/<term>-<exam>/; keep those URLs
        # alive for anything already linking to them.
        parts.append(f"redirect_from: /exams/{meta['legacy_path']}/")
    parts.extend(
        [
            "---",
            "",
            "{% raw %}",
            "",
            MATHJAX_SNIPPET,
            "",
            HOMEWORK_STYLE_SNIPPET,
            "",
            EXAM_NAV_SNIPPET,
            "",
            f"# {title}",
            "",
        ]
    )
    if meta.get("administered", "").strip():
        parts.extend([f"**administered** {meta['administered']}", ""])
    buttons = action_buttons(meta)
    if buttons:
        parts.extend([buttons, ""])
    parts.extend(
        [
            EXAM_DISCLAIMER,
            "",
            SECTION_SEPARATOR,
            "",
            generate_toc(body, toc_title="Problems"),
            "",
            SECTION_SEPARATOR,
            "",
            body,
            "",
            "{% endraw %}",
            "",
        ]
    )
    page = "\n".join(parts)
    return "\n".join(line.rstrip() for line in page.splitlines()) + "\n", len(questions)


def main() -> int:
    exams = compose.iter_exams()
    if not exams:
        raise SystemExit(f"No exams found under {compose.QUESTIONS_DIR.name}/")
    for term, exam in exams:
        page, count = build_exam_page(term, exam)
        out = EXAMS_DIR / term / exam / "index.md"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page)
        print(f"{term}/{exam}: {count} problems")
    print(f"Wrote {len(exams)} exam pages to {EXAMS_DIR.relative_to(REPO_ROOT)}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
