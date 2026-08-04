#!/usr/bin/env python3
"""One-time bootstrap: derive _data/worksheet_topics.yml from the homepage's
existing topic-browser data (the examTopics JS array in index.md).

The YAML follows the agreed shape -- a list of chapters, each with a
problems list. Problem entries are either:
  - a bare ID string like sp26/mt1/q2 (embedded from the exam web view), or
  - a mapping {id: mock/mt1/q1, pdf: resources/...pdf#page=N} for exams with
    no web view, rendered as PDF links.

Re-runnable, but intended to run once; afterwards the YAML is the source of
truth and is edited by hand (append new problems under their topics).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
INDEX_MD = REPO_ROOT / "index.md"
OUTPUT_YML = REPO_ROOT / "_data" / "worksheet_topics.yml"

# "SP26 MT1 Problem 1" -> ("sp26", "mt1", 1); "FA25 Final Problem 3" -> ("fa25", "final", 3)
LABEL_PATTERN = re.compile(r"^(\w+)\s+(MT1|MT2|Final)\s+Problem\s+(\d+)$", re.I)


def label_to_id(label: str) -> str | None:
    match = LABEL_PATTERN.match(label.strip())
    if not match:
        return None
    term, exam, num = match.groups()
    return f"{term.lower()}/{exam.lower()}/q{num}"


def main() -> int:
    text = INDEX_MD.read_text()
    js = re.search(r"const examTopics = \[(.*?)\n\];", text, re.S)
    if not js:
        raise SystemExit("Could not find examTopics array in index.md")

    chapters = []
    for block in re.finditer(
        r"\{\s*title:\s*\"([^\"]+)\",\s*summary:\s*\"([^\"]*)\",\s*links:\s*\[(.*?)\]\s*\}",
        js.group(1),
        re.S,
    ):
        title, summary, links_src = block.groups()
        chap_match = re.match(r"(\d+)\.\s*(.+)", title)
        if not chap_match:
            raise SystemExit(f"Unparseable chapter title: {title!r}")
        number, name = int(chap_match.group(1)), chap_match.group(2).strip()
        problems = []
        for label, url in re.findall(r"\[\"([^\"]+)\",\s*\"([^\"]+)\"\]", links_src):
            pid = label_to_id(label)
            if pid is None:
                print(f"  WARNING: skipping unparseable label {label!r}", file=sys.stderr)
                continue
            if pid.startswith("mock/"):
                problems.append({"id": pid, "pdf": url})
            else:
                problems.append(pid)
        chapters.append(
            {"chapter": number, "name": name, "summary": summary, "problems": problems}
        )

    lines = [
        "# Topic-specific worksheet definitions.",
        "# Each chapter lists the exam problems belonging to it. Problem IDs are",
        "#   <term>/<exam>/q<number>   e.g. sp26/mt1/q2  ->  exams/sp26-mt1, Problem 2.",
        "# Exams without a web view (mocks) use {id, pdf} and render as PDF links.",
        "# To add a new exam: append its problem IDs under the matching chapters,",
        "# then run scripts/build_worksheets.py (or push -- CI rebuilds automatically).",
        "",
    ]
    for chap in chapters:
        lines.append(f"- chapter: {chap['chapter']}")
        lines.append(f'  name: "{chap["name"]}"')
        lines.append(f'  summary: "{chap["summary"]}"')
        lines.append("  problems:")
        for prob in chap["problems"]:
            if isinstance(prob, str):
                lines.append(f"    - {prob}")
            else:
                lines.append(f'    - id: {prob["id"]}')
                lines.append(f'      pdf: "{prob["pdf"]}"')
    OUTPUT_YML.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_YML.write_text("\n".join(lines) + "\n")
    total = sum(len(c["problems"]) for c in chapters)
    print(f"Wrote {OUTPUT_YML.relative_to(REPO_ROOT)}: {len(chapters)} chapters, {total} problems")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
