# EECS 245 Exams

Source for [exams.eecs245.org](https://exams.eecs245.org): past exams with
solutions, and worksheets of the same problems grouped by course-notes chapter.
Every page is generated from the exams' LaTeX. You add a `.tex`, and edit a few
small YAML files; you never edit a page.

## How it fits together

```
_sources/exams/fa25-mt1/fa25-mt1.tex     the exam as written            (you add this)
        │  conversion: LaTeX → one folder per question            needs pandoc
        ▼
src/fa25-mt1/q03/src.md                  the question body              generated
src/fa25-mt1/q03/config.yml              title, points, flags, videos   generated ONCE, then yours
src/fa25-mt1/q03/imgs/                   its figures                    generated
        │  composition: questions → pages                          Python only
        ▼
.build/exams/fa25-mt1/index.md           local, gitignored, overwritten every build
.build/worksheets/chapter-2/index.md
        │  Jekyll + _plugins/composed_pages.rb
        ▼
_site/                                   the published site
```

**The folder name is the exam's id.** `fa25-mt1` is the source folder, the `src/`
folder, the `id` in the registry, the PDF's filename, the prefix of its worksheet
ids (`fa25-mt1/q03`), and its URL (`/exams/fa25-mt1/`). Choose it once, as
`<term>-<exam>`: `fa26-mt1`, `fa26-mt2`, `fa26-final`.

| Path | What it is | Who writes it |
|---|---|---|
| `_sources/exams/<id>/` | LaTeX and its figures; `_sources/eecs245.sty` | you |
| `resources/exams/<id>.pdf`, `<id>-solutions.pdf` | the PDFs the buttons link to | you |
| `_data/exams.yml` | the registry: one entry per exam | you |
| `_data/worksheet_topics.yml` | which questions go on which worksheet | you |
| `src/<id>/qNN/config.yml` | a question's title, points, flags, video links | conversion, once — then you |
| `src/<id>/qNN/src.md`, `imgs/`, `preamble.md` | the question itself | conversion, every time |
| `src/<id>/.extracted` | fingerprint of what the questions were converted from | conversion |
| `.build/`, `_site/` | composed pages, built site | the build; both gitignored |

Exam pages and worksheets are not in the repository. They are rebuilt on every
build, so a copy here would only invite edits that get overwritten.

## Setup

- Ruby with Bundler, then `bundle install`.
- Python 3.9 or newer. No packages.
- [pandoc](https://pandoc.org), only to convert LaTeX. Previewing the site does
  not need it.
- `pdflatex` and `pdftocairo` (MacTeX/BasicTeX, poppler), only when an exam has a
  TikZ figure that is new or has changed. Rendered figures are committed.

## Preview

```bash
bundle exec jekyll serve
```

Open <http://localhost:4001>. This one command converts any exam whose LaTeX
changed, composes every page, and rebuilds when you save a file. There is no
separate script to remember.

## Adding an exam

Using `fa26-mt1` as the example.

1. **LaTeX.** Create `_sources/exams/fa26-mt1/` containing `fa26-mt1.tex` (named
   after the folder) and a subfolder with its figures. The subfolder can be
   called anything; figures are found by filename. Leave
   `\usepackage{../../eecs245}` as it is.
2. **PDFs.** Add `resources/exams/fa26-mt1.pdf` and, if there is one,
   `resources/exams/fa26-mt1-solutions.pdf`.
3. **Registry.** Add an entry to `_data/exams.yml`. Its position in the file is
   its position on the front page, so new exams go at the top.

   ```yaml
   - id: fa26-mt1
     term: Fall 2026
     exam: Midterm 1
     pdf: resources/exams/fa26-mt1.pdf
     solutions: resources/exams/fa26-mt1-solutions.pdf
   ```

4. **Build.** Run `bundle exec jekyll serve`. Only the new exam converts; the rest
   print `SKIP`. Read the output for:
   - `PASS fa26-mt1` — converted.
   - `SYNTHESIZED solution for Problem 1a (...)` — that part marks an answer (a
     correct bubble, or a blank with the answer typed in) but has no written
     solution, so one was generated: every choice with the right one filled, and
     blanks showing the boxed answer. Check that it is right.
   - `WARNING:` — see [Messages](#messages).
5. **Worksheets.** In `_data/worksheet_topics.yml`, list each problem under the
   chapter it belongs to, as `fa26-mt1/q01`. This is the one step that needs your
   judgment. A problem may appear under more than one chapter, or none.
6. **Check, commit, push.** Look at `/exams/fa26-mt1/`, click both PDF buttons,
   open a worksheet you added to. Commit `_sources/exams/fa26-mt1/`,
   `src/fa26-mt1/`, the PDFs and the two `_data/` files. Pushing deploys.

Building before step 3 is harmless: conversion succeeds and the build then stops,
telling you to add the registry entry.

## Everyday edits

**Add a walkthrough video.** In the question's `config.yml`:

```yaml
video: https://youtu.be/7E1WH2p-MoU        # the whole problem
video_c: https://youtu.be/4qk_4dNKtD4      # part (c) only
```

A badge appears beside the points, on the exam page and on every worksheet that
includes the question. Pushing that one-line change is enough to update the site.

**Change a title, points, or flags.** Edit `config.yml`; the heading is rendered
from it. Note that a problem's link includes its title and points
(`#problem-3-spreading-your-wings-12-pts`), so changing either changes the link.
Videos never do.

**Fix something in an exam.** Edit the `.tex`. With `serve` running it re-converts
on save. `src.md` is regenerated; `config.yml` is never overwritten. If the LaTeX
now disagrees with it — say the points changed — you get a warning naming the
question and both values, and you decide which is right.

**Do not edit** `src.md`, or anything under `.build/` or `_site/`. The next build
replaces them.

**Move a problem between worksheets.** Edit `_data/worksheet_topics.yml`.

**Front page.** `index.md`. The exams table is generated from `_data/exams.yml`.

## Reference

### `_data/exams.yml`

| Key | | |
|---|---|---|
| `id` | required | the exam's folder name |
| `term`, `exam` | required | the page title is `<term> <exam>` |
| `label` | optional | front-page link text, when shorter than `exam` (`Final`) |
| `pdf` | required | path from the repo root, or a URL |
| `solutions` | optional | same |
| `playlist` | optional | adds a "Video Walkthroughs" button to the exam page |

Every entry needs a `src/<id>/` folder, every `src/` folder needs an entry, and
`pdf`/`solutions` must point at files that exist. The build stops otherwise.

### `src/<id>/qNN/config.yml`

`title`, `points`, `flags` (a list of ids), `video`, `video_<part>`. It is created
the first time the question is converted and never written again. The one flag
the LaTeX produces today is `mtN-redemption`, from a title annotated "Counts
towards Midterm N redemption score".

### `scripts/build.sh`

`jekyll serve` and `jekyll build` run this for you. By hand:

```bash
scripts/build.sh                  # convert what changed, compose everything
scripts/build.sh fa26-mt1         # force one exam to re-convert
scripts/build.sh --all            # force all of them
scripts/build.sh --compose-only   # never convert; compose from src/ as committed
```

"Changed" means the content of the exam's source folder, or of the scripts, no
longer matches `src/<id>/.extracted`. So improving the converter re-converts
every exam, which is intended. File timestamps are not used; git does not keep
them.

| Script | |
|---|---|
| `generate_exam_markdown.py` | LaTeX → question folders. Most of the code is here |
| `compose.py` | reads questions and the registry; renders headings; shared by both builders |
| `build_exam_pages.py`, `build_worksheets.py` | questions → pages |
| `miniyaml.py` | reads the two `_data` files and `config.yml`, so nothing needs PyYAML |

## Deployment

Pushing to `main` runs `.github/workflows/build-site.yml`: it composes the pages
(`build.sh --compose-only`), builds with Jekyll, and deploys to GitHub Pages. CI
never converts LaTeX — it has no pandoc — so **`src/` must be committed**.
Nothing generated is ever committed back.

The site uses a custom Jekyll plugin, which works because this workflow runs
Jekyll itself. GitHub Pages' built-in builder would ignore `_plugins/`.

## Messages

| You see | It means |
|---|---|
| `src/ has folders with no entry in _data/exams.yml: X` | add X to the registry |
| `exams.yml lists 'X' but src/X/ does not exist` | the source has not been converted, or the id is misspelled |
| `'X' has pdf: ... but that file does not exist` | fix the path or add the PDF |
| `No question at src/X/q99/src.md` | a bad id in `worksheet_topics.yml` |
| `config.yml says points: '12' but the LaTeX now says '14'` | they disagree; edit `config.yml` if the LaTeX is right |
| `src/X/q09 has no matching problem in the LaTeX any more` | the exam lost a problem; its `src.md` was removed and `config.yml` kept. Delete the folder if that is right |
| `X.tex sets \duedate ...` | left over from the homework template; exams ignore it. Clear it to silence this |
| `_data/exams.yml titles X '...' but its source says '...'` | the registry and the `.tex`'s `\term`/`\assignment` disagree |
| `STALE X: source changed but pandoc is not installed` | preview uses the committed questions; install pandoc to convert |
| `TikZ figure ... needs rendering, but pdflatex/pdftocairo were not found` | a figure is new or changed; install TeX and poppler |
| `.build/ is missing` | `SKIP_CONTENT_BUILD` is set but nothing was composed; run `scripts/build.sh` |

## Things that look wrong but are not

- **`src/*` is excluded in `_config.yml` by glob, not as `src`.** Jekyll stops
  *watching* any excluded path that exists, so the literal form would mean editing
  a `config.yml` under `serve` rebuilt nothing. The glob keeps `src/` unread,
  unpublished, and watched. `_sources` is left out of `exclude` for the same
  reason; Jekyll never reads `_`-prefixed folders anyway.
- **Questions with no "Solution" in the LaTeX still show one.** See
  `SYNTHESIZED` above.
- **Files like `q01 2.md` appear.** If the repository lives in an iCloud-synced
  folder (`~/Documents`), iCloud makes conflict copies whenever many files are
  rewritten at once. They are gitignored and never published. Delete them with
  `find . -name '* [0-9].*' -delete`, or keep the repository outside iCloud.
