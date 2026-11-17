"""Regression checks for exam-specific metadata and math conversion."""
import unittest

import generate_exam_markdown as converter


class ExamConversionTests(unittest.TestCase):
    def test_exam_without_due_date(self):
        source = (r"\newcommand{\assignment}{Midterm 1}"
                  r"\newcommand{\submissioninstructions}{Instructions}")
        self.assertEqual(converter.extract_metadata(source, exam=True).due_date, "")
        with self.assertRaises(ValueError):
            converter.extract_metadata(source)
        dated = source + r"\newcommand{\duedate}{October 7}"
        self.assertEqual(converter.extract_metadata(dated, exam=True).due_date, "October 7")

    def test_set_brace_does_not_merge_with_variable(self):
        rendered = converter.escape_inline_math_content(r"A=\{y_1,y_2\}")
        self.assertIn(r"\lbrace y", rendered)
        self.assertNotIn(r"\lbracey", rendered)

    def test_alignment_already_in_display_math(self):
        aligned = "\\begin{aligned}\nx+y&=0\\\\\nx-y&=0\n\\end{aligned}"
        for opening, closing in [(r"\[", r"\]"), ("$$", "$$")]:
            source = f"{opening}\n{aligned}\n{closing}"
            self.assertEqual(converter.wrap_bare_alignment_environments(source), source)
        self.assertIn("$$", converter.wrap_bare_alignment_environments(aligned))

    def test_filled_example_and_hidden_answer_are_distinct(self):
        rendered = converter.replace_choice_markers(
            r"\filledbubble{example}\correctbubble{answer}\bubble{other}")
        self.assertEqual(rendered.count(r"\eecsfilledcircle"), 1)
        self.assertEqual(rendered.count(r"\bigcirc"), 2)

    def test_hash_in_math_text(self):
        rendered = converter.fix_latex_for_mathjax(r"$$\text{\# of points}$$")
        self.assertIn(r"\text{# of points}", rendered)
        self.assertNotIn(r"\#", rendered)

    def test_solution_copies_all_choices_across_print_rows(self):
        source = (
            r"\bubble{incorrect choice}\\[0.2em]"
            "\n"
            r"\correctbubble{$\begin{bmatrix}6\\-7\\4\end{bmatrix}$}"
            "\n"
            r"\bubble{$\begin{bmatrix}6\\-7\\3\end{bmatrix}$}"
        )
        summary = converter.solution_choice_summary(source, None)
        self.assertEqual(summary.count(r"\solutionbubble"), 2)
        self.assertIn(r"\solutioncorrectbubble{$\begin{bmatrix}6\\-7\\4\end{bmatrix}$}", summary)

    def test_shared_solution_copies_and_labels_each_answer_set(self):
        source = r"""
\begin{subprob}
\begin{enumerate}[label=(\roman*)]
\item \correctbubble{True} \bubble{False}
\item Explain.
\item \bubble{True} \correctbubble{False}
\end{enumerate}
"""
        summary = converter.solution_choice_summary(source, "parts (i)-(iii)")
        self.assertIn("\\textbf{(i)}\n\n\\solutioncorrectbubble{True}", summary)
        self.assertIn("\\textbf{(iii)}\n\n\\solutionbubble{True}\n\\solutioncorrectbubble{False}", summary)
        self.assertNotIn(r"\textbf{(ii)}", summary)

    def test_shared_solution_sits_after_the_whole_list(self):
        source = "1. First\n2. Second\n\n" + converter.replace_solution_markers(
            "\\begin{solution}[both parts]\nExplanation\n\\end{solution}",
            include_solutions=True,
        )
        rendered = converter.ordered_lists_as_html(source)
        self.assertIn('</ol>\n\n<details class="group-solution"', rendered)
        self.assertIn("<summary>Solution for both parts</summary>", rendered)

    def test_unmarked_choices_are_not_copied_into_solutions(self):
        self.assertEqual(converter.solution_choice_summary(r"\squarebubble{First} \squarebubble{Second}", None), "")


if __name__ == "__main__":
    unittest.main()
