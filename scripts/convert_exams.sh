#!/usr/bin/env bash
# Convert exam LaTeX sources into the question tree, then compose every page.
#
#   scripts/convert_exams.sh              convert whatever changed, rebuild pages
#   scripts/convert_exams.sh fa26-mt1     force one exam, rebuild pages
#   scripts/convert_exams.sh --all        force every exam, rebuild pages
#
# Adding an exam is: drop its folder into _sources/exams/ (the .tex plus its
# image directory, whatever that directory is called) and run this. Nothing
# else needs editing -- the term/exam split, the question ids and the image
# paths are all derived from the folder name and the source itself.
#
#   _sources/exams/<term>-<exam>/<term>-<exam>.tex   source you drop in
#   exams/<term>-<exam>/{q*.md,imgs/,.extracted}     the only content tree
#   _data/exams.yml                                  registry: title, PDFs, videos
#   exams/<term>-<exam>/index.md                     composed from it
#   worksheets/chapter-*/index.md                    composed from it
#
# PDF and video links come from _data/exams.yml.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
SRC_ROOT="${EXAM_SOURCES:-$REPO_ROOT/_sources/exams}"

[ -d "$SRC_ROOT" ] || { echo "No exam sources at $SRC_ROOT" >&2; exit 1; }

only=""
force=0
case "${1:-}" in
  --all) force=1 ;;
  "") ;;
  *) only="$1"; force=1 ;;
esac

fail=0
converted=0
for tex in "$SRC_ROOT"/*/*.tex; do
  name="$(basename "$tex" .tex)"
  [ -n "$only" ] && [ "$name" != "$only" ] && continue

  # The folder name is the exam id: the key in _data/exams.yml and the prefix
  # of every problem id in _data/worksheet_topics.yml.
  questions_dir="$REPO_ROOT/exams/${name}"
  stamp="$questions_dir/.extracted"

  # Incremental: skip an exam whose source (and the scripts that convert it) are
  # all older than its questions. Touch the source, or pass --all, to force.
  if [ "$force" -eq 0 ] && [ -f "$stamp" ]; then
    newest="$(find "$(dirname "$tex")" "$SCRIPT_DIR" -type f -newer "$stamp" -print -quit)"
    if [ -z "$newest" ]; then
      echo "SKIP  $name (up to date)"
      continue
    fi
  fi

  # Page metadata (PDF links, playlist) comes from _data/exams.yml at compose
  # time; extraction needs nothing but the source.
  if python3 "$SCRIPT_DIR/generate_exam_markdown.py" \
      "$tex" "$questions_dir" --include-solutions --exam; then
    echo "PASS  $name"
    converted=$((converted + 1))
  else
    echo "FAIL  $name"; fail=1
  fi
done

if [ -n "$only" ] && [ "$converted" -eq 0 ] && [ "$fail" -eq 0 ]; then
  echo "No exam named '$only' in $SRC_ROOT" >&2
  exit 1
fi

if [ "$fail" -ne 0 ]; then
  echo "Conversion failed; not composing pages." >&2
  exit "$fail"
fi

# Both page trees are pure output of the question tree above, so they are
# recomposed in full every run -- cheap, and it keeps a partial conversion from
# leaving the site half-updated.
python3 "$SCRIPT_DIR/build_exam_pages.py"
python3 "$SCRIPT_DIR/build_worksheets.py"
