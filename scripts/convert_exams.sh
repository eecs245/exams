#!/usr/bin/env bash
# Generate web-view pages for all exams with LaTeX sources.
# Usage: scripts/convert_exams.sh <exam-sources-root>
# Expects: <exam-sources-root>/<name>/<name>.tex  (eecs245.sty at sources root)
# Outputs: <repo>/exams/<name>/index.md (+ copied image assets)
# PDF buttons link to the repo's existing resources/exams/<name>[-solutions].pdf
set -euo pipefail

SRC_ROOT="$(cd "${1:?usage: convert_exams.sh <exam-sources-root>}" && pwd)"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"

fail=0
for tex in "$SRC_ROOT"/*/*.tex; do
  name="$(basename "$tex" .tex)"
  args=(--include-solutions --exam --layout minimal
        --pdf-link "/resources/exams/${name}.pdf")
  if [ -f "$REPO_ROOT/resources/exams/${name}-solutions.pdf" ]; then
    args+=(--solutions-pdf-link "/resources/exams/${name}-solutions.pdf")
  fi
  # Walkthrough videos: looked up from scripts/exam_videos.conf (name=url lines).
  videos_url="$(grep -E "^${name}=" "$SCRIPT_DIR/exam_videos.conf" 2>/dev/null | head -1 | cut -d= -f2- || true)"
  if [ -n "$videos_url" ]; then
    args+=(--videos-link "$videos_url")
  fi
  if python3 "$SCRIPT_DIR/generate_exam_markdown.py" \
      "$tex" "$REPO_ROOT/exams/${name}/index.md" "${args[@]}"; then
    # Keep the LaTeX source of truth alongside its generated page.
    cp "$tex" "$REPO_ROOT/exams/${name}/${name}.tex"
    echo "PASS  $name"
  else
    echo "FAIL  $name"; fail=1
  fi
done
exit "$fail"
