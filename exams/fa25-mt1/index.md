---
layout: minimal
title: "Fall 2025 Midterm 1"
description: "Midterm 1 problems."
nav_exclude: true
hide_footer_hr: true
---

{% raw %}

<script>
window.MathJax = {
  tex: {inlineMath: [['$', '$'], ['\\(', '\\)']]}
};
</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js" async></script>

<style>
.main-content p {
  margin-bottom: 1.15em;
}
.assignment-pdf-button {
  font-size: 0.95rem;
  padding: 0.35rem 0.65rem;
}
.assignment-actions {
  align-items: center;
  display: flex;
  flex-wrap: wrap;
  gap: 0.55rem;
  margin: 0 0 1rem;
}
.math-display,
mjx-container[jax="CHTML"][display="true"] {
  max-width: 100%;
  overflow-x: auto;
  overflow-y: hidden;
}
.math-display {
  padding-bottom: 0.2rem;
}
.math-display mjx-container[jax="CHTML"][display="true"] {
  padding-bottom: 0.2rem;
}
.answer-blank {
  border-bottom: 1px solid currentColor;
  display: inline-block;
  min-width: 8rem;
  height: 1em;
  vertical-align: baseline;
}
.assignment-parts {
  margin: 1rem 0;
}
.assignment-part {
  column-gap: 0.55rem;
  display: grid;
  grid-template-columns: 1.4rem minmax(0, 1fr);
  margin-bottom: 1.05rem;
}
.assignment-part-label {
  font-weight: 600;
  text-align: right;
}
.assignment-part-content > :first-child {
  margin-top: 0;
}
.mc-options {
  display: flex;
  flex-wrap: wrap;
  gap: 0.9rem 1.6rem;
  margin: 0.9rem 0 1.1rem;
}
.mc-option {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  white-space: nowrap;
}
.mc-bubble,
.mc-square {
  display: inline-block;
  flex: 0 0 auto;
  height: 0.95em;
  width: 0.95em;
  vertical-align: -0.12em;
}
.mc-bubble {
  border: 1.5px solid currentColor;
  border-radius: 50%;
}
.mc-square {
  border: 1.5px solid currentColor;
}
.mc-correct {
  background: currentColor;
}
.main-content table {
  font-size: 0.9rem;
  width: auto;
  max-width: 100%;
}
.main-content table th,
.main-content table td {
  padding: 0.35rem 0.5rem;
  white-space: nowrap;
}
</style>

# Fall 2025 Midterm 1

**administered** by 3:50PM on Friday, September 27th, 2025

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/exams/fa25-mt1.pdf" target="_blank">View as PDF ✏️</a>
<a class="btn btn-info assignment-pdf-button" href="/resources/exams/fa25-mt1-solutions.pdf" target="_blank">Solutions PDF ✅</a>
</div>

{: .yellow }
<div markdown="1">
**Instructions**

-   This exam consists of 8 problems, worth a total of 100 points, spread across 12 pages (6 sheets of paper).

-   You have 80 minutes to complete this exam, unless you have extended-time accommodations through SSD.

-   Write your uniqname in the top right corner of each page.

-   For free response problems, you must show all of your work (unless otherwise specified), and <span class="math-inline">\\(\boxed{\text{circle}}\\)</span> your final answer. We will not grade work that appears elsewhere, and you may lose points if your work is not shown.

-   For multiple choice problems, completely fill in bubbles and square boxes; if we cannot tell which option(s) you selected, you may lose points.



-   You may refer to a single two-sided handwritten notes sheet. Other than that, you may not refer to any other resources or technology during the exam (no phones, watches, or calculators).
</div>

---

## Problems

- [Problem 1: Consider the Following\...](#problem-1-consider-the-following-15-pts)
- [Problem 2: Absolute Madness](#problem-2-absolute-madness-17-pts)
- [Problem 3: Spreading Your Wings](#problem-3-spreading-your-wings-12-pts)
- [Problem 4: Mission Impossible](#problem-4-mission-impossible-12-pts)
- [Problem 5: Back to Normal](#problem-5-back-to-normal-12-pts)
- [Problem 6: Needed Me](#problem-6-needed-me-11-pts)
- [Problem 7: High Definition](#problem-7-high-definition-12-pts)
- [Problem 8: Worst-Case Scenario](#problem-8-worst-case-scenario-8-pts)

---

## Problem 1: Consider the Following\... <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">15 pts</span>

Consider the following dataset of <span class="math-inline">\\(n = 9\\)</span> values.

| <span class="math-inline">\\(y&#95;1\\)</span> | <span class="math-inline">\\(y&#95;2\\)</span> | <span class="math-inline">\\(y&#95;3\\)</span> | <span class="math-inline">\\(y&#95;4\\)</span> | <span class="math-inline">\\(y&#95;5\\)</span> | <span class="math-inline">\\(y&#95;6\\)</span> | <span class="math-inline">\\(y&#95;7\\)</span> | <span class="math-inline">\\(y&#95;8\\)</span> | <span class="math-inline">\\(y&#95;9\\)</span> |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|  <span class="math-inline">\\(7\\)</span>  |  <span class="math-inline">\\(8\\)</span>  | <span class="math-inline">\\(10\\)</span>  | <span class="math-inline">\\(10\\)</span>  | <span class="math-inline">\\(11\\)</span>  | <span class="math-inline">\\(13\\)</span>  | <span class="math-inline">\\(14\\)</span>  | <span class="math-inline">\\(17\\)</span>  | <span class="math-inline">\\(27\\)</span>  |

Suppose we'd like to find the optimal parameter, <span class="math-inline">\\(w^{\ast}\\)</span>, for the constant model <span class="math-inline">\\(h(x&#95;i) = w\\)</span>, given this dataset of 9 values.

In parts **a)** through **f)**, choose the empirical risk function <span class="math-inline">\\(R(w)\\)</span> that the given value of <span class="math-inline">\\(w^{\ast}\\)</span> is the minimizer of, for this particular dataset. If you believe the given value of <span class="math-inline">\\(w^{\ast}\\)</span> does not minimize any of the five options, select N/A.

-   **Option 1**: <span class="math-inline">\\(\displaystyle R(w) = \frac{1}{n} \sum&#95;{i = 1}^n (y&#95;i - w)^2\\)</span>

-   **Option 2**: <span class="math-inline">\\(\displaystyle R(w) = \frac{1}{n} \sum&#95;{i = 1}^n (27y&#95;i - 13w)^2\\)</span>

-   **Option 3**: <span class="math-inline">\\(\displaystyle R(w) = \frac{1}{n} \sum&#95;{i = 1}^n 13|y&#95;i - w|\\)</span>

-   **Option 4**: <span class="math-inline">\\(\displaystyle R(w) = \frac{1}{n} \sum&#95;{i = 1}^n \begin{cases} 13 &amp; \text{if } y&#95;i = w \\\\ 27 &amp; \text{if } y&#95;i \neq w \end{cases}\\)</span>

-   **Option 5**: <span class="math-inline">\\(\displaystyle R(w) = \lim&#95;{p \rightarrow \infty} \frac{1}{n} \sum&#95;{i = 1}^n |y&#95;i - w|^p\\)</span>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(2.5 pts) **10** is the value of <span class="math-inline">\\(w\\)</span> that minimizes\...

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 1</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 2</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 3</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 4</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 5</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> N/A</span></div>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(2.5 pts) **11** is the value of <span class="math-inline">\\(w\\)</span> that minimizes\...

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 1</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 2</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 3</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 4</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 5</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> N/A</span></div>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(2.5 pts) **12** is the value of <span class="math-inline">\\(w\\)</span> that minimizes\...

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 1</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 2</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 3</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 4</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 5</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> N/A</span></div>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
(2.5 pts) **13** is the value of <span class="math-inline">\\(w\\)</span> that minimizes\...

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 1</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 2</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 3</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 4</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 5</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> N/A</span></div>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">e)</div>
<div class="assignment-part-content" markdown="1">
(2.5 pts) **17** is the value of <span class="math-inline">\\(w\\)</span> that minimizes\...

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 1</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 2</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 3</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 4</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 5</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> N/A</span></div>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">f)</div>
<div class="assignment-part-content" markdown="1">
(2.5 pts) **27** is the value of <span class="math-inline">\\(w\\)</span> that minimizes\...

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 1</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 2</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 3</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 4</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 5</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> N/A</span></div>

</div>
</div>

</div>

---

## Problem 2: Absolute Madness <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">17 pts</span>

Consider a dataset of <span class="math-inline">\\(n = 8\\)</span> values, where

<div class="math-display">
$$
y_1 = 1,\quad y_2 = y_3 = 4, \quad y_4 = y_5 = y_6 = \alpha,\quad y_7 = y_8 = 20
$$
</div>

and <span class="math-inline">\\(4 &lt; \alpha &lt; 20\\)</span>.

As usual, let <span class="math-inline">\\(R&#95;\text{abs}(w)\\)</span> represent the mean absolute error of a constant prediction <span class="math-inline">\\(w\\)</span> on this dataset of 8 values.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> Is the value of <span class="math-inline">\\(w^{\ast}\\)</span>, the minimizer of <span class="math-inline">\\(R&#95;\text{abs}(w)\\)</span>, unique? Select and fill out one option below.

<span class="mc-bubble" aria-hidden="true"></span> The value of <span class="math-inline">\\(w^{\ast}\\)</span> is unique, and is equal to .

<span class="mc-bubble" aria-hidden="true"></span> The value of <span class="math-inline">\\(w^{\ast}\\)</span> is not unique; any value between and is a minimizer.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Find the value of <span class="math-inline">\\(R&#95;\text{abs}(\alpha)\\)</span>, for any valid choice of <span class="math-inline">\\(\alpha\\)</span>. Show your work, and <span class="math-inline">\\(\boxed{\text{circle}}\\)</span> your final answer, which should be an expression involving <span class="math-inline">\\(\alpha\\)</span> and other constants, but no other variables, and no summation notation.

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(R&#95;\text{abs}(\alpha) = \frac{\alpha + 31}{8}\\)</span>.

Let's start with the definition of <span class="math-inline">\\(R&#95;\text{abs}(w)\\)</span> and plug in <span class="math-inline">\\(w = \alpha\\)</span>.

<div class="math-display">
$$
\begin{align*}
R_\text{abs}(\alpha) &= \frac{1}{8} \sum_{i=1}^8 |y_i - \alpha| \\\\
&= \frac{|1 - \alpha| + |4 - \alpha| + |4 - \alpha| + |\alpha - \alpha| + |\alpha - \alpha| + |\alpha - \alpha| + |20 - \alpha| + |20 - \alpha|}{8} \\\\
&= \frac{|1 - \alpha| + 2|4 - \alpha| + 2|20 - \alpha|}{8}
\end{align*}
$$
</div>

Since <span class="math-inline">\\(\alpha &gt; 1\\)</span> and <span class="math-inline">\\(\alpha &gt; 4\\)</span>, we know that <span class="math-inline">\\(|1 - \alpha| = \alpha - 1\\)</span> and <span class="math-inline">\\(|4 - \alpha| = \alpha - 4\\)</span>. Similarly, since <span class="math-inline">\\(\alpha &lt; 20\\)</span>, we have <span class="math-inline">\\(|20 - \alpha| = 20 - \alpha\\)</span>.

<div class="math-display">
$$
\begin{align*}
R_\text{abs}(\alpha) &= \frac{|1 - \alpha| + 2|4 - \alpha| + 2|20 - \alpha|}{8} \\\\
&= \frac{\alpha - 1 + 2(\alpha - 4) + 2(20 - \alpha)}{8} \\\\
&= \frac{\alpha - 1 + 2\alpha - 8 + 40 - 2\alpha}{8} \\\\
&= \frac{\alpha + 31}{8}
\end{align*}
$$
</div>

</details>

Recall,

<div class="math-display">
$$
y_1 = 1,\quad y_2 = y_3 = 4, \quad y_4 = y_5 = y_6 = \alpha,\quad y_7 = y_8 = 20
$$
</div>

where <span class="math-inline">\\(4 &lt; \alpha &lt; 20\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">8 pts</span> Let the minimum possible value of <span class="math-inline">\\(R&#95;\text{abs}(w)\\)</span> be <span class="math-inline">\\(M\\)</span>. Given that

<div class="math-display">
$$
R_\text{abs}(20) - M = \frac{9}{2}
$$
</div>

find the value of <span class="math-inline">\\(\alpha\\)</span>. Show your work, and <span class="math-inline">\\(\boxed{\text{circle}}\\)</span> your final answer, which should be a number with no variables.

<em>Hint: It's possible to answer this without using your answer from the previous part.</em>

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(\alpha = 11\\)</span>.

Since <span class="math-inline">\\(\alpha\\)</span> minimizes <span class="math-inline">\\(R&#95;\text{abs}(w)\\)</span>, we know that <span class="math-inline">\\(R&#95;\text{abs}(\alpha) = M\\)</span>. In the previous part, we found an expression for <span class="math-inline">\\(R&#95;\text{abs}(\alpha)\\)</span>. One common solution was to find another expression for <span class="math-inline">\\(R&#95;\text{abs}(20)\\)</span> (which is also a function of <span class="math-inline">\\(\alpha\\)</span>), and then to solve for the <span class="math-inline">\\(\alpha\\)</span> such that

<div class="math-display">
$$
R_\text{abs}(20) - R_\text{abs}(\alpha) = \frac{9}{2}
$$
</div>

Here's another solution. Since <span class="math-inline">\\((\alpha, M)\\)</span> is the vertex of <span class="math-inline">\\(R&#95;\text{abs}(w)\\)</span>, we know that the slope to the left of it is negative and the slope to the right of it is positive.

The slope on the line segment between <span class="math-inline">\\((\alpha, M)\\)</span> and <span class="math-inline">\\((20, M + \frac{9}{2})\\)</span> is

<div class="math-display">
$$
\text{slope} = \frac{\# \text{left} - \# \text{right}}{n} = \frac{6 - 2}{8} = \frac{1}{2}
$$
</div>

So, now we know that on the line segment between <span class="math-inline">\\((\alpha, M)\\)</span> and <span class="math-inline">\\((20, M + \frac{9}{2})\\)</span>, the slope is <span class="math-inline">\\(\frac{1}{2}\\)</span>. This is all we need to solve for <span class="math-inline">\\(\alpha\\)</span>. Since the slope of a line segment is its change in <span class="math-inline">\\(y\\)</span> over its change in <span class="math-inline">\\(x\\)</span>, we have:

<div class="math-display">
$$
\frac{M + \frac{9}{2} - M}{20 - \alpha} = \frac{1}{2}
$$
</div>

Solving for <span class="math-inline">\\(\alpha\\)</span>, we get:

<div class="math-display">
$$
\alpha = 11
$$
</div>

</details>

</div>
</div>

</div>

---

## Problem 3: Spreading Your Wings <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>

Consider a dataset of <span class="math-inline">\\(n\\)</span> points, <span class="math-inline">\\((x&#95;1, y&#95;1), (x&#95;2, y&#95;2), \ldots, (x&#95;n, y&#95;n)\\)</span>, where

-   the means of <span class="math-inline">\\(x&#95;1, x&#95;2, \ldots, x&#95;n\\)</span> and <span class="math-inline">\\(y&#95;1, y&#95;2, \ldots, y&#95;n\\)</span> are 15 and 5, respectively

-   the variances of <span class="math-inline">\\(x&#95;1, x&#95;2, \ldots, x&#95;n\\)</span> and <span class="math-inline">\\(y&#95;1, y&#95;2, \ldots, y&#95;n\\)</span> are <span class="math-inline">\\(\sigma&#95;x^2\\)</span> and <span class="math-inline">\\(\sigma&#95;y^2\\)</span>, respectively

-   the correlation coefficient between <span class="math-inline">\\(x&#95;1, x&#95;2, \ldots, x&#95;n\\)</span> and <span class="math-inline">\\(y&#95;1, y&#95;2, \ldots, y&#95;n\\)</span> is <span class="math-inline">\\(r\\)</span>

We define a new set of values, <span class="math-inline">\\(z&#95;1, z&#95;2, \ldots, z&#95;n\\)</span>, as follows:

<div class="math-display">
$$
z_i = 3x_i - y_i, \quad i = 1, 2, \ldots, n
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Suppose we fit a simple linear regression line to the dataset <span class="math-inline">\\((x&#95;1, z&#95;1), (x&#95;2, z&#95;2), \ldots, (x&#95;n, z&#95;n)\\)</span> by minimizing mean squared error. Note that <span class="math-inline">\\(z\\)</span> is the variable being predicted, not <span class="math-inline">\\(y\\)</span>. Let <span class="math-inline">\\(h(x&#95;i)\\)</span> represent the corresponding line.

What is the value of <span class="math-inline">\\(h(15)\\)</span>? Your answer should be a number with no variables.

<span class="math-inline">\\(h(15) =\\)</span>

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(h(15) = 40\\)</span>.

The key fact being assessed here is that the line that minimizes mean squared error always passes through

<div class="math-display">
$$
(\text{mean of input variable}, \text{mean of output variable})
$$
</div>

Normally this is stated as the line passing through the point <span class="math-inline">\\((\bar{x}, \bar{y})\\)</span>, but here the output variable is <span class="math-inline">\\(z\\)</span>, not <span class="math-inline">\\(y\\)</span>.

The mean of <span class="math-inline">\\(z\\)</span> is <span class="math-inline">\\(3 \bar{x} - \bar{y}\\)</span>, as we explored in a homework problem, and this is

<div class="math-display">
$$
3 \bar{x} - \bar{y} = 3(15) - 5 = 40
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">8 pts</span>
<span class="math-inline">\\(\sigma&#95;z^2\\)</span>, the variance of <span class="math-inline">\\(z&#95;1, z&#95;2, \ldots, z&#95;n\\)</span>, can be written in the form <span class="math-inline">\\(\sigma&#95;z^2 = 9 \sigma&#95;x^2 + \sigma&#95;y^2 + C\\)</span>.

1.  What is the value of <span class="math-inline">\\(C\\)</span>?

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(-6 \sigma&#95;x \sigma&#95;y\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(6 \sigma&#95;x \sigma&#95;y\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(-6r \sigma&#95;x \sigma&#95;y\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(6r \sigma&#95;x \sigma&#95;y\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(-6nr \sigma&#95;x \sigma&#95;y\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(6nr \sigma&#95;x \sigma&#95;y\\)</span></span></div>

2.  Show your work in the box below. English explanations are not enough.

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(-6 \sigma&#95;x \sigma&#95;y\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(6 \sigma&#95;x \sigma&#95;y\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(-6r \sigma&#95;x \sigma&#95;y\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(6r \sigma&#95;x \sigma&#95;y\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(-6nr \sigma&#95;x \sigma&#95;y\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(6nr \sigma&#95;x \sigma&#95;y\\)</span></span></div>

We'll find the answer by expanding out the definition of <span class="math-inline">\\(\sigma&#95;z^2\\)</span> and simplifying.

<div class="math-display">
$$
\begin{align*}
\sigma_z^2 &= \frac{1}{n} \sum_{i=1}^n (z_i - \bar{z})^2 \\\\
&= \frac{1}{n} \sum_{i=1}^n (3x_i - y_i - (3\bar{x} - \bar{y}))^2 \\\\
&= \underbrace{\frac{1}{n} \sum_{i=1}^n (3x_i - 3\bar{x} - y_i + \bar{y})^2}_\text{distributed the negative sign and rearranged} \\\\
&= \frac{1}{n} \sum_{i=1}^n \underbrace{(3(x_i - \bar{x}) - (y_i - \bar{y}))^2}_\text{treat this as (a - b)^2} \\\\
&= \frac{1}{n} \sum_{i=1}^n \left( 9(x_i - \bar{x})^2 - 6(x_i - \bar{x})(y_i - \bar{y}) + (y_i - \bar{y})^2 \right) \\\\
&= 9 \left(\frac{1}{n} \sum_{i=1}^n (x_i - \bar{x})^2 \right) - 6 \left(\frac{1}{n} \sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})\right) + \left(\frac{1}{n} \sum_{i=1}^n (y_i - \bar{y})^2 \right) \\\\
&= 9 \sigma_x^2 + \sigma_y^2 - 6 \left(\frac{1}{n} \sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})\right) \\\\
\end{align*}
$$
</div>

So,

<div class="math-display">
$$
C = -6 \left(\frac{1}{n} \sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})\right)
$$
</div>

But, recall that

<div class="math-display">
$$
r = \frac{1}{n} \sum_{i=1}^n \left( \frac{x_i - \bar{x}}{\sigma_x} \right) \left( \frac{y_i - \bar{y}}{\sigma_y} \right)
$$
</div>

which means that

<div class="math-display">
$$
r \sigma_x \sigma_y = \frac{1}{n} \sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})
$$
</div>

So,

<div class="math-display">
$$
C = -6 \left(\frac{1}{n} \sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})\right) = -6r \sigma_x \sigma_y
$$
</div>

</details>

</div>
</div>

</div>

---

## Problem 4: Mission Impossible <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Suppose <span class="math-inline">\\(\vec u, \vec v \in \mathbb{R}^n\\)</span> are **non-zero** vectors, and suppose that

<div class="math-display">
$$
| \vec u \cdot \vec v | = \lVert \vec u \rVert \lVert \vec v \rVert
$$
</div>

For each statement below, determine whether it is impossible, possible, or guaranteed to be true, given the above assumptions. **Select exactly one option from each row**. The first statement has been done for you as an example.

|  | **statement** | **impossible?** | **possible?** | **guaranteed?** |
|:--:|:---|:--:|:--:|:--:|
| <span class="math-inline">\\(i\\)</span> | <span class="math-inline">\\(\lVert \vec u \rVert = 5\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> |
| <span class="math-inline">\\(ii\\)</span> | <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> are orthogonal | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> |
| <span class="math-inline">\\(iii\\)</span> | <span class="math-inline">\\(\lVert \vec u - \vec v \rVert = 0\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> |
| <span class="math-inline">\\(iv\\)</span> | <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> span a 1-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^n\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> |
| <span class="math-inline">\\(v\\)</span> | <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> span a 2-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^n\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> |
| <span class="math-inline">\\(vi\\)</span> | <span class="math-inline">\\(\lVert \vec u + \vec v \rVert = \lVert \vec u \rVert + \lVert \vec v \rVert\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> |

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"></div>

Remember that for **any** two vectors <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span>,

<div class="math-display">
$$
\vec u \cdot \vec v = \lVert \vec u \rVert \lVert \vec v \rVert \cos \theta
$$
</div>

The fact that we're told that

<div class="math-display">
$$
| \vec u \cdot \vec v | = \lVert \vec u \rVert \lVert \vec v \rVert
$$
</div>

tells us that <span class="math-inline">\\(\cos \theta = 1\\)</span> or <span class="math-inline">\\(\cos \theta = -1\\)</span>, which means that the angle between <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> is <span class="math-inline">\\(0^\circ\\)</span> or <span class="math-inline">\\(180^\circ\\)</span>, which means that <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> are scalar multiples of each other. (They may point in the same or opposite directions.) This is the key insight to assessing each of the statements.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Suppose <span class="math-inline">\\(\vec w, \vec z \in \mathbb{R}^n\\)</span>. Given that <span class="math-inline">\\(\lVert \vec w \rVert = \lVert \vec z \rVert = \lVert \vec w - \vec z \rVert = 1\\)</span>, find <span class="math-inline">\\(\lVert \vec w + \vec z \rVert\\)</span>. Show your work, and <span class="math-inline">\\(\boxed{\text{circle}}\\)</span> your final answer, which should be a number with no variables.

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(\lVert \vec w + \vec z \rVert = \sqrt{3}\\)</span>.

We're asked to find <span class="math-inline">\\(\lVert \vec w + \vec z \rVert\\)</span>. To do so, let's expand out <span class="math-inline">\\(\lVert \vec w + \vec z \rVert^2\\)</span> as we've done in the past, and see how to utilize what we were given.

<div class="math-display">
$$
\begin{align*}
\lVert \vec w + \vec z \rVert^2 &= (\vec w + \vec z) \cdot (\vec w + \vec z) \\\\
&= \vec w \cdot \vec w + 2 \vec w \cdot \vec z + \vec z \cdot \vec z \\\\
&= \lVert \vec w \rVert^2 + 2 \vec w \cdot \vec z + \lVert \vec z \rVert^2 \\\\
&= 1 + 2 \vec w \cdot \vec z + 1 \\\\
&= 2 + 2 \vec w \cdot \vec z
\end{align*}
$$
</div>

Above, we've plugged in <span class="math-inline">\\(\lVert \vec w \rVert^2 = 1\\)</span> and <span class="math-inline">\\(\lVert \vec z \rVert^2 = 1\\)</span>. We need to know <span class="math-inline">\\(\vec w \cdot \vec z\\)</span>, which we don't yet know.

But, we have enough information to find it, if we expand out <span class="math-inline">\\(\lVert \vec w - \vec z \rVert^2\\)</span>, which we were told is equal to 1.

<div class="math-display">
$$
\begin{align*}
\lVert \vec w - \vec z \rVert^2 &= (\vec w - \vec z) \cdot (\vec w - \vec z) \\\\
1 &= \vec w \cdot \vec w - 2 \vec w \cdot \vec z + \vec z \cdot \vec z \\\\
1 &= \lVert \vec w \rVert^2 - 2 \vec w \cdot \vec z + \lVert \vec z \rVert^2 \\\\
1 &= 1 - 2 \vec w \cdot \vec z + 1 \\\\
1 &= 2 - 2 \vec w \cdot \vec z
\end{align*}
$$
</div>

Solving the above gives us <span class="math-inline">\\(\vec w \cdot \vec z = \frac{1}{2}\\)</span>. This gives

<div class="math-display">
$$
\lVert \vec w + \vec z \rVert^2 = 2 + 2 \vec w \cdot \vec z = 2 + 2 \cdot \frac{1}{2} = 3
$$
</div>

And so,

<div class="math-display">
$$
\lVert \vec w + \vec z \rVert = \sqrt{3}
$$
</div>

</details>

</div>
</div>

</div>

---

## Problem 5: Back to Normal <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>

Consider the orthogonal vectors <span class="math-inline">\\(\vec u&#95;1 = \begin{bmatrix} 13 \\\\ -3 \\\\ 2 \end{bmatrix}\\)</span>, <span class="math-inline">\\(\vec u&#95;2 = \begin{bmatrix} 0 \\\\ 4 \\\\ 6 \end{bmatrix}\\)</span>, and <span class="math-inline">\\(\vec u&#95;3 = \begin{bmatrix} 1 \\\\ 3 \\\\ -2 \end{bmatrix}\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Find the equation of the plane spanned by <span class="math-inline">\\(\vec u&#95;2\\)</span> and <span class="math-inline">\\(\vec u&#95;3\\)</span> in standard form, i.e. <span class="math-inline">\\(ax + by + cz + d = 0\\)</span>. <span class="math-inline">\\(\boxed{\text{Circle}}\\)</span> your final answer.

<details markdown="1"><summary>Solution</summary>

Plane: <span class="math-inline">\\(13x - 3y + 2z = 0\\)</span> (or any scalar multiple of this equation).

Most students took the cross product of <span class="math-inline">\\(\vec u&#95;2\\)</span> and <span class="math-inline">\\(\vec u&#95;3\\)</span> to find a vector that is orthogonal to the plane spanned by <span class="math-inline">\\(\vec u&#95;2\\)</span> and <span class="math-inline">\\(\vec u&#95;3\\)</span>, and then used that vector to define the plane.

But, we were already told that all three vectors are orthogonal to each other, which means that the vector orthogonal to the plane spanned by <span class="math-inline">\\(\vec u&#95;2\\)</span> and <span class="math-inline">\\(\vec u&#95;3\\)</span> is <span class="math-inline">\\(\vec u&#95;1\\)</span>. So, we can use <span class="math-inline">\\(\vec u&#95;1\\)</span> to define the plane.

<div class="math-display">
$$
\vec u_1 \cdot (x, y, z) = 0 \implies 13x - 3y + 2z = 0
$$
</div>

So, the equation of the plane spanned by <span class="math-inline">\\(\vec u&#95;2\\)</span> and <span class="math-inline">\\(\vec u&#95;3\\)</span> is <span class="math-inline">\\(13x - 3y + 2z = 0\\)</span> (or any scalar multiple of this equation).
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">8 pts</span> There is one value of <span class="math-inline">\\(k\\)</span> such that the projection of <span class="math-inline">\\(\vec x = \begin{bmatrix} 7 \\\\ 3 \\\\ 1 \end{bmatrix}\\)</span> onto <span class="math-inline">\\(\vec u&#95;k\\)</span> is just <span class="math-inline">\\(\vec u&#95;k\\)</span> itself.

1.  What is the value of <span class="math-inline">\\(k\\)</span>?
<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 1</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 2</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 3</span></div>

2.  Show your work in the box below. English explanations are not enough.

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 1</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 2</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> 3</span></div>

We're told that for one of the three provided vectors --- <span class="math-inline">\\(\vec u&#95;1\\)</span>, <span class="math-inline">\\(\vec u&#95;2\\)</span>, or <span class="math-inline">\\(\vec u&#95;3\\)</span> --- the projection of <span class="math-inline">\\(\vec x\\)</span> onto that vector is just that vector itself.

Remember that the projection of <span class="math-inline">\\(\vec x\\)</span> onto <span class="math-inline">\\(\vec u&#95;k\\)</span> is given by

<div class="math-display">
$$
\text{proj}_{\vec u_k} \vec x = \frac{\vec x \cdot \vec u_k}{\vec u_k \cdot \vec u_k} \vec u_k
$$
</div>

So, we need to find the vector <span class="math-inline">\\(\vec u&#95;k\\)</span> such that the scalar <span class="math-inline">\\(\frac{\vec x \cdot \vec u&#95;k}{\vec u&#95;k \cdot \vec u&#95;k}\\)</span> is equal to 1, or equivalently, <span class="math-inline">\\(\vec x \cdot \vec u&#95;k = \vec u&#95;k \cdot \vec u&#95;k\\)</span>. We can check this equality for each of the three provided vectors.

**(i)** <span class="math-inline">\\(x \cdot \vec u&#95;1 = \begin{bmatrix} 7 \\\\ 3 \\\\ 1 \end{bmatrix} \cdot \begin{bmatrix} 13 \\\\ -3 \\\\ 2 \end{bmatrix} = 7 \cdot 13 + 3 \cdot (-3) + 1 \cdot 2 = 84\\)</span>

<span class="math-inline">\\(\vec u&#95;1 \cdot \vec u&#95;1 = 13^2 + (-3)^2 + 2^2 = 180\\)</span>

<span class="math-inline">\\(84 \neq 180\\)</span>, so <span class="math-inline">\\(\vec u&#95;1\\)</span> is not the vector we're looking for.

**(ii)** <span class="math-inline">\\(x \cdot \vec u&#95;2 = \begin{bmatrix} 7 \\\\ 3 \\\\ 1 \end{bmatrix} \cdot \begin{bmatrix} 0 \\\\ 4 \\\\ 6 \end{bmatrix} = 7 \cdot 0 + 3 \cdot 4 + 1 \cdot 6 = 18\\)</span>

<span class="math-inline">\\(\vec u&#95;2 \cdot \vec u&#95;2 = 0^2 + 4^2 + 6^2 = 52\\)</span>

<span class="math-inline">\\(18 \neq 52\\)</span>, so <span class="math-inline">\\(\vec u&#95;2\\)</span> is not the vector we're looking for.

**(iii)** <span class="math-inline">\\(x \cdot \vec u&#95;3 = \begin{bmatrix} 7 \\\\ 3 \\\\ 1 \end{bmatrix} \cdot \begin{bmatrix} 1 \\\\ 3 \\\\ -2 \end{bmatrix} = 7 \cdot 1 + 3 \cdot 3 + 1 \cdot (-2) = 14\\)</span>

<span class="math-inline">\\(\vec u&#95;3 \cdot \vec u&#95;3 = 1^2 + 3^2 + (-2)^2 = 14\\)</span>

<span class="math-inline">\\(14 = 14\\)</span>, so <span class="math-inline">\\(\vec u&#95;3\\)</span> **is** the vector we're looking for.
</details>

</div>
</div>

</div>

---

## Problem 6: Needed Me <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">11 pts</span>

Suppose <span class="math-inline">\\(\vec x = \begin{bmatrix} c \\\\ 1 \\\\ 0 \end{bmatrix}\\)</span>, <span class="math-inline">\\(\vec y = \begin{bmatrix} 1 \\\\ c \\\\ 1 \end{bmatrix}\\)</span>, and <span class="math-inline">\\(\vec z = \begin{bmatrix} 0 \\\\ 1 \\\\ c \end{bmatrix}\\)</span>, where <span class="math-inline">\\(c \in \mathbb{R}\\)</span> is a constant.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">8 pts</span> Find a **positive value** of <span class="math-inline">\\(c\\)</span> such that <span class="math-inline">\\(\vec x\\)</span>, <span class="math-inline">\\(\vec y\\)</span>, and <span class="math-inline">\\(\vec z\\)</span> are linearly **dependent**. Show your work, and <span class="math-inline">\\(\boxed{\text{circle}}\\)</span> your final answer, which should be a positive number with no variables.

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(c = \sqrt{2}\\)</span>.

For <span class="math-inline">\\(\vec x\\)</span>, <span class="math-inline">\\(\vec y\\)</span>, and <span class="math-inline">\\(\vec z\\)</span> to be linearly dependent, there must exist scalars <span class="math-inline">\\(a\\)</span>, <span class="math-inline">\\(b\\)</span>, and <span class="math-inline">\\(c\\)</span> such that

<div class="math-display">
$$
a \vec x + b \vec y + \vec z
$$
</div>

(or equivalently, <span class="math-inline">\\(a \vec x + b \vec y + d\vec z = \vec 0\\)</span>, but the former approach involves one fewer variable to solve for).

Substituting in the given vectors, we have

<div class="math-display">
$$
a \begin{bmatrix} c \\\\ 1 \\\\ 0 \end{bmatrix} + b \begin{bmatrix} 1 \\\\ c \\\\ 1 \end{bmatrix} = \begin{bmatrix} 0 \\\\ 1 \\\\ c \end{bmatrix}
$$
</div>

As a system of equations, we have

<div class="math-display">
$$
\begin{align*}
c a + b &= 0 \\\\
a + c b &= 1 \\\\
b &= c
\end{align*}
$$
</div>

The third equation gives us <span class="math-inline">\\(b = c\\)</span>, and the second gives us <span class="math-inline">\\(a = 1 - cb = 1 - c^2\\)</span>. Substituting these into the first equation gives us

<div class="math-display">
$$
c(1 - c^2) + c = 0 \implies c - c^3 + c = 0 \implies c(2 - c^2) = 0
$$
</div>

This equation has three solutions for <span class="math-inline">\\(c\\)</span>: <span class="math-inline">\\(c = 0\\)</span>, <span class="math-inline">\\(c = \sqrt{2}\\)</span>, and <span class="math-inline">\\(c = -\sqrt{2}\\)</span>. We're asked to find a **positive** value of <span class="math-inline">\\(c\\)</span>, so <span class="math-inline">\\(c = \sqrt{2}\\)</span> for this part, and either <span class="math-inline">\\(0\\)</span> or <span class="math-inline">\\(-\sqrt{2}\\)</span> for the next part.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> Provide one **other** value of <span class="math-inline">\\(c\\)</span> (that is, not your answer from the previous part) such that <span class="math-inline">\\(\vec x\\)</span>, <span class="math-inline">\\(\vec y\\)</span>, and <span class="math-inline">\\(\vec z\\)</span> are linearly **dependent**. Your answer should be a number with no variables.

other value of <span class="math-inline">\\(c =\\)</span>

</div>
</div>

</div>

---

## Problem 7: High Definition <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>

Suppose <span class="math-inline">\\(\vec x&#95;1, \vec x&#95;2, \ldots \vec x&#95;{12}\\)</span> are 12 non-zero vectors in <span class="math-inline">\\(\mathbb{R}^{7}\\)</span>. Furthermore, suppose:

-   <span class="math-inline">\\(\vec x&#95;1\\)</span>, <span class="math-inline">\\(\vec x&#95;2\\)</span>, and <span class="math-inline">\\(\vec x&#95;3\\)</span> span a 2-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^{7}\\)</span>.

-   <span class="math-inline">\\(\vec x&#95;4\\)</span>, <span class="math-inline">\\(\vec x&#95;5\\)</span>, and <span class="math-inline">\\(\vec x&#95;6\\)</span> span **the same** 2-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^{7}\\)</span> as <span class="math-inline">\\(\vec x&#95;1\\)</span>, <span class="math-inline">\\(\vec x&#95;2\\)</span>, and <span class="math-inline">\\(\vec x&#95;3\\)</span>, i.e.

<div class="math-display">
$$
\text{span}(\{\vec x_4, \vec x_5, \vec x_6\}) = \text{span}(\{\vec x_1, \vec x_2, \vec x_3\})
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Let <span class="math-inline">\\(r\\)</span> be the dimension of the subspace of <span class="math-inline">\\(\mathbb{R}^{7}\\)</span> spanned by <span class="math-inline">\\(\vec x&#95;1, \vec x&#95;2, \ldots \vec x&#95;{12}\\)</span>. What are the smallest and largest possible values of <span class="math-inline">\\(r\\)</span>? Your answers should be integers with no variables.

smallest possible value of <span class="math-inline">\\(r =\\)</span> largest possible value of <span class="math-inline">\\(r =\\)</span>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Which of the following **could** form a basis for <span class="math-inline">\\(\mathbb{R}^{7}\\)</span>? Select all that apply. Blank answers will receive no credit.

<details markdown="1"><summary>Solution</summary>

The first choice only includes 6 vectors, but since the span of <span class="math-inline">\\(\vec x&#95;1, \vec x&#95;2, \ldots \vec x&#95;{12}\\)</span> is 7-dimensional, it must include at least 7 vectors. So, the first choice is not a valid basis.

The fourth choice includes 7 vectors, but we know that <span class="math-inline">\\(\vec x&#95;1, \vec x&#95;2, \vec x&#95;5\\)</span> are a linearly **dependent** set since they all lie on the same 2-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^7\\)</span> (and you only need 2 vectors to uniquely define a 2-dimensional subspace), so the fourth choice is not a valid basis.

The other options all include 7 vectors that *could* be linearly independent, and so they could form a basis for <span class="math-inline">\\(\mathbb{R}^7\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Suppose the intersection of <span class="math-inline">\\(\text{span}(\lbrace\vec x&#95;1, \vec x&#95;2\rbrace)\\)</span> and <span class="math-inline">\\(\text{span}(\lbrace \vec x&#95;4, \vec x&#95;5 \rbrace)\\)</span> is a line (i.e. a 1-dimensional subspace) in <span class="math-inline">\\(\mathbb{R}^{7}\\)</span>. Which of the following **must** be true? Select all that apply. Blank answers will receive no credit.

<em>Hint: Don't forget the assumptions introduced at the start of the problem.</em>

<span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\vec x&#95;2\\)</span>, <span class="math-inline">\\(\vec x&#95;4\\)</span>, and <span class="math-inline">\\(\vec x&#95;5\\)</span> can all be written as scalar multiples of <span class="math-inline">\\(\vec x&#95;1\\)</span>.

<span class="mc-square" aria-hidden="true"></span> The set <span class="math-inline">\\(\lbrace \vec x&#95;2, \vec x&#95;4 \rbrace\\)</span> is linearly independent.

<span class="mc-square" aria-hidden="true"></span> The set <span class="math-inline">\\(\lbrace \vec x&#95;3, \vec x&#95;4 \rbrace\\)</span> is linearly independent.

<span class="mc-square" aria-hidden="true"></span> The set <span class="math-inline">\\(\lbrace \vec x&#95;3, \vec x&#95;6 \rbrace\\)</span> is linearly independent.

<span class="mc-square" aria-hidden="true"></span> None of the above.

<details markdown="1"><summary>Solution</summary>

<span class="mc-square" aria-hidden="true"></span> None of the above.

The intended answer to the problem was options 1 and 3. The scenario we had in mind was that <span class="math-inline">\\(\operatorname{span}(\lbrace\vec x&#95;1, \vec x&#95;2\rbrace) = \operatorname{span}(\lbrace\vec x&#95;4, \vec x&#95;5\rbrace) = \text{the same line}\\)</span>. The two spans can't both be different planes that happen to intersect in a line, since we're told that <span class="math-inline">\\(\vec x&#95;1, \vec x&#95;2, \vec x&#95;3\\)</span> span a 2-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^7\\)</span> and <span class="math-inline">\\(\vec x&#95;4, \vec x&#95;5, \vec x&#95;6\\)</span> span the same 2-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^7\\)</span>. So, if the two spans are planes, they're the same plane, and they would intersect at a plane. Since the two spans intersect at a line, **we thought** they'd both have to be lines. If that was the case, then <span class="math-inline">\\(\vec x&#95;2\\)</span>, <span class="math-inline">\\(\vec x&#95;4\\)</span>, and <span class="math-inline">\\(\vec x&#95;5\\)</span> would all be scalar multiples of <span class="math-inline">\\(\vec x&#95;1\\)</span>, and so <span class="math-inline">\\(\vec x&#95;3\\)</span> would have to not be on that line (for <span class="math-inline">\\(\vec x&#95;1, \vec x&#95;2, \vec x&#95;3\\)</span> to span a 2-dimensional subspace), which is why Options 1 and 3 were our originally intended answers.

But after releasing exam scores, a student brought up a possibility we hadn't considered: it's possible that <span class="math-inline">\\(\operatorname{span}(\lbrace\vec x&#95;1, \vec x&#95;2\rbrace)\\)</span> is a plane, and <span class="math-inline">\\(\operatorname{span}(\lbrace\vec x&#95;4, \vec x&#95;5\rbrace)\\)</span> is a line that is contained on that plane. That setup would satisfy all of the assumptions provided in the problem statement, but it would imply that none of the options are true.

So, retroactively, we gave full credit to everyone for this part.
</details>

</div>
</div>

</div>

---

## Problem 8: Worst-Case Scenario <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">8 pts</span>

Suppose <span class="math-inline">\\(a, b, c, d, e\\)</span> are positive real numbers. Find the **largest** real number <span class="math-inline">\\(T\\)</span> such that it's guaranteed that

<div class="math-display">
$$
(a + b + c + d + e) \left( \frac{1}{a} + \frac{1}{b} + \frac{1}{c} + \frac{1}{d} + \frac{1}{e} \right) \geq T
$$
</div>

Think of <span class="math-inline">\\(T\\)</span> as the "best possible lower bound". For instance, we know that the expression on the left-hand side above must be greater than or equal to 0, since <span class="math-inline">\\(a, b, c, d, e\\)</span> are all positive, but <span class="math-inline">\\(T = 0\\)</span> is not the answer, since there's a larger value of <span class="math-inline">\\(T\\)</span> that also guarantees the inequality holds.

Show your work, and <span class="math-inline">\\(\boxed{\text{circle}}\\)</span> your final answer, which should be a number with no variables.

<em>Hint: Use the Cauchy-Schwarz inequality.</em>

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(T = 25\\)</span>.

Recall, the Cauchy-Schwarz inequality states that for any two vectors <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span>,

<div class="math-display">
$$
|\vec u \cdot \vec v| \leq \lVert \vec u \rVert \lVert \vec v \rVert
$$
</div>

Let's define two vectors <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> and then apply the Cauchy-Schwarz inequality to them.

<div class="math-display">
$$
\vec u = \begin{bmatrix} \sqrt{a} \\\\ \sqrt{b} \\\\ \sqrt{c} \\\\ \sqrt{d} \\\\ \sqrt{e} \end{bmatrix}, \quad \vec v = \begin{bmatrix} \frac{1}{\sqrt{a}} \\\\ \frac{1}{\sqrt{b}} \\\\ \frac{1}{\sqrt{c}} \\\\ \frac{1}{\sqrt{d}} \\\\ \frac{1}{\sqrt{e}} \end{bmatrix}
$$
</div>

Let's compute the three quantities involved in the inequality.

-   <span class="math-inline">\\(\lVert \vec u \rVert = \sqrt{a + b + c + d + e}\\)</span>

-   <span class="math-inline">\\(\lVert \vec v \rVert = \sqrt{\frac{1}{a} + \frac{1}{b} + \frac{1}{c} + \frac{1}{d} + \frac{1}{e}}\\)</span>

-   <span class="math-inline">\\(|\vec u \cdot \vec v| = |\sqrt{a} \cdot \frac{1}{\sqrt{a}} + \sqrt{b} \cdot \frac{1}{\sqrt{b}} + \sqrt{c} \cdot \frac{1}{\sqrt{c}} + \sqrt{d} \cdot \frac{1}{\sqrt{d}} + \sqrt{e} \cdot \frac{1}{\sqrt{e}}| = 5\\)</span>

So, we have that

<div class="math-display">
$$
5 \leq \sqrt{a + b + c + d + e} \cdot \sqrt{\frac{1}{a} + \frac{1}{b} + \frac{1}{c} + \frac{1}{d} + \frac{1}{e}}
$$
</div>

Squaring both sides of the inequality gives us

<div class="math-display">
$$
25 \leq (a + b + c + d + e) \left( \frac{1}{a} + \frac{1}{b} + \frac{1}{c} + \frac{1}{d} + \frac{1}{e} \right)
$$
</div>

This means that for any positive values of <span class="math-inline">\\(a, b, c, d, e\\)</span>, it's impossible for <span class="math-inline">\\((a + b + c + d + e) \left( \frac{1}{a} + \frac{1}{b} + \frac{1}{c} + \frac{1}{d} + \frac{1}{e} \right)\\)</span> to be less than 25. Finding a value equal to 25 is doable if we set <span class="math-inline">\\(a = b = c = d = e = 1\\)</span>. So, <span class="math-inline">\\(T = 25\\)</span> is the largest possible value of <span class="math-inline">\\(T\\)</span> that guarantees the inequality holds.
</details>

(1 pt) Congrats on finishing Midterm 1! Here's a free point.

Feel free to draw us a picture about EECS 245 in the box below.

{% endraw %}
