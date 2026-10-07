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


if __name__ == "__main__":
    unittest.main()
