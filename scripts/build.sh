#!/usr/bin/env bash
# Build the site's content: extract questions from any exam source that
# changed, then compose every exam page and topic worksheet.
#
#   scripts/build.sh                 extract what changed (needs pandoc), compose all
#   scripts/build.sh fa26-mt1        force one exam to re-extract, compose all
#   scripts/build.sh --all           force every exam to re-extract, compose all
#   scripts/build.sh --compose-only  never extract; compose from committed questions
#
# Normally nobody runs this by hand: `jekyll serve` and `jekyll build` invoke
# it from _plugins/build_content.rb before Jekyll reads files, and CI runs it
# as an explicit step. Adding an exam is: add its entry to _data/exams.yml,
# drop its folder into _sources/exams/, then preview.
#
#   _sources/exams/<id>/<id>.tex                  source you drop in
#   exams/<id>/{q*.md,imgs/,.extracted}           extracted from it; hand-editable headers
#   exams/<id>/index.md, worksheets/chapter-*/    composed from the questions
#   _data/exams.yml                               registry: title, PDFs, playlist
#
# "Changed" means the content hash of the source folder plus these scripts
# differs from exams/<id>/.extracted -- not mtimes, which git does not keep.
#
# Extraction needs pandoc (and pdflatex + pdftocairo only for a TikZ figure not
# already rendered). Without pandoc, a stale exam is reported and its committed
# questions are used; an exam with NO committed questions is an error. CI passes
# --compose-only: it must never re-extract, because question headers carry
# hand-typed data (video links) that a fresh extraction would not know about.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
SRC_ROOT="${EXAM_SOURCES:-$REPO_ROOT/_sources/exams}"

mode=changed   # changed | all | none
only=""
case "${1:-}" in
  --all)          mode=all ;;
  --compose-only) mode=none ;;
  "")             ;;
  -*)             echo "usage: $0 [--all | --compose-only | <exam-id>]" >&2; exit 2 ;;
  *)              only="$1"; mode=all ;;
esac

fail=0
if [ "$mode" != none ]; then
  [ -d "$SRC_ROOT" ] || { echo "No exam sources at $SRC_ROOT" >&2; exit 1; }
  have_pandoc=1; command -v pandoc >/dev/null 2>&1 || have_pandoc=0
  matched=0

  for tex in "$SRC_ROOT"/*/*.tex; do
    name="$(basename "$tex" .tex)"
    [ -n "$only" ] && [ "$name" != "$only" ] && continue
    matched=1
    questions_dir="$REPO_ROOT/exams/${name}"

    if [ "$mode" = changed ] && \
       python3 "$SCRIPT_DIR/generate_exam_markdown.py" --check-extracted "$tex" "$questions_dir"; then
      echo "SKIP  $name (questions match source)"
      continue
    fi

    if [ "$have_pandoc" -eq 0 ]; then
      if [ -f "$questions_dir/.extracted" ]; then
        echo "STALE $name: source changed but pandoc is not installed; using committed questions"
      else
        echo "ERROR $name: has no extracted questions and pandoc is not installed" >&2
        fail=1
      fi
      continue
    fi

    if python3 "$SCRIPT_DIR/generate_exam_markdown.py" \
        "$tex" "$questions_dir" --include-solutions --exam; then
      echo "PASS  $name"
    else
      echo "FAIL  $name"; fail=1
    fi
  done

  if [ -n "$only" ] && [ "$matched" -eq 0 ]; then
    echo "No exam named '$only' in $SRC_ROOT" >&2
    exit 1
  fi
  if [ "$fail" -ne 0 ]; then
    echo "Extraction failed; not composing pages." >&2
    exit 1
  fi
fi

# Both page trees are pure output of the questions, recomposed in full every
# run: it takes well under a second, and it keeps a partial extraction from
# leaving the site half-updated. Every write is compare-first, so an unchanged
# page is not touched and `jekyll serve --watch` does not rebuild in a loop.
python3 "$SCRIPT_DIR/build_exam_pages.py"
python3 "$SCRIPT_DIR/build_worksheets.py"
