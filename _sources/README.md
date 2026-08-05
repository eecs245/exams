# EECS 245 exam sources

This archive contains the LaTeX sources and required image assets for the Fall
2025, Winter 2026, and Spring 2026 EECS 245 exams.

## macOS setup and previewing

1. Install [MacTeX](https://www.tug.org/mactex/).
2. Install [Visual Studio Code](https://code.visualstudio.com/) or Cursor.
3. In VS Code or Cursor, install the **LaTeX Workshop** extension.
4. Open this extracted archive as a folder. Keep `eecs245.sty` at the archive
   root; the exam sources load it using their existing relative paths.
5. Open an exam's `.tex` file and press **Command + Option + V**. This is the
   easiest way to build and preview its PDF with LaTeX Workshop, so you do not
   need to run a build command in Terminal.

Your job is not to edit anything in the rendered PDF. Previewing is only useful
for rendering a PDF from source in case you need to see what an exam looks like.

The image folders must remain beside their corresponding exam sources. They are
already included in this archive.

## Included helper

`generate_homework_markdown.py` is the Spring 2026 helper used to generate the
website Markdown/HTML view of a homework from its LaTeX source. It is included
at the archive root for reference; it is not needed to compile these exams.
