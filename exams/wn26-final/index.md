---
layout: minimal
title: "Winter 2026 Final Exam"
description: "Final Exam problems."
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

# Winter 2026 Final Exam

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/exams/wn26-final.pdf" target="_blank">View as PDF ✏️</a>
<a class="btn btn-info assignment-pdf-button" href="/resources/exams/wn26-final-solutions.pdf" target="_blank">Solutions PDF ✅</a>
</div>

{: .yellow }
<div markdown="1">
**Instructions**

-   This exam consists of 13 problems, worth a total of 130 points, spread across 14 pages (7 sheets of paper). **All problems count towards your Final Exam score; certain problems also count towards your Midterm 1 or Midterm 2 redemption scores.**

-   You have 120 minutes to complete this exam, unless you have extended-time accommodations through SSD.

-   Write your uniqname in the top right corner of every page in the space provided.

-   For free response problems, you must show all of your work (unless otherwise specified), and <span class="math-inline">\\(\boxed{\text{circle}}\\)</span> your final answer. We will not grade work that appears elsewhere, and you may lose points if your work is not shown.

-   For multiple choice problems, completely fill in bubbles and square boxes; if we cannot tell which option(s) you selected, you may lose points.



-   You may refer to **3** two-sided handwritten notes sheets. Other than that, you may not refer to any other resources or technology during the exam (no phones, watches, or calculators).
</div>

---

## Problems

- [Problem 1: (12 pts) $\boxed{\text{Counts towards Midterm 1 redemption score}}$](#problem-1-12-pts-boxedtextcounts-towards-midterm-1-redemption-score)
- [Problem 2: (13 pts) $\boxed{\text{Counts towards Midterm 1 redemption score}}$](#problem-2-13-pts-boxedtextcounts-towards-midterm-1-redemption-score)
- [Problem 3: (9 pts) $\boxed{\text{Counts towards Midterm 1 redemption score}}$](#problem-3-9-pts-boxedtextcounts-towards-midterm-1-redemption-score)
- [Problem 4: (4 pts) $\boxed{\text{Counts towards Midterm 1 redemption score}}$](#problem-4-4-pts-boxedtextcounts-towards-midterm-1-redemption-score)
- [Problem 5: (11 pts) $\boxed{\text{Counts towards Midterm 2 redemption score}}$](#problem-5-11-pts-boxedtextcounts-towards-midterm-2-redemption-score)
- [Problem 6: (12 pts) $\boxed{\text{Counts towards Midterm 2 redemption score}}$](#problem-6-12-pts-boxedtextcounts-towards-midterm-2-redemption-score)
- [Problem 7: (8 pts) $\boxed{\text{Counts towards Midterm 2 redemption score}}$](#problem-7-8-pts-boxedtextcounts-towards-midterm-2-redemption-score)
- [Problem 8: (9 pts) $\boxed{\text{Counts towards Midterm 2 redemption score}}$](#problem-8-9-pts-boxedtextcounts-towards-midterm-2-redemption-score)
- [Problem 9](#problem-9-12-pts)
- [Problem 10](#problem-10-14-pts)
- [Problem 11](#problem-11-10-pts)
- [Problem 12](#problem-12-12-pts)
- [Problem 13](#problem-13-4-pts)

---

## Problem 1: (12 pts) <span class="math-inline">\\(\boxed{\text{Counts towards Midterm 1 redemption score}}\\)</span>

Suppose we'd like to find the optimal constant prediction, <span class="math-inline">\\(w^{\ast}\\)</span>, for the constant model <span class="math-inline">\\(h(x&#95;i) = w\\)</span>, given the following dataset of <span class="math-inline">\\(n = 4\\)</span> values.

<div class="math-display">
$$
y_1 = 3, \quad y_2 = 6, \quad y_3 = 6, \quad y_4 = 13
$$
</div>

 In each part, choose from the options below.

<div class="math-display">
$$
\begin{array}{l@{\hspace{1.75cm}}l}
A = 3 & E = 7 \\\\[1.5ex]
B = \dfrac{4}{\frac{1}{3} + \frac{1}{6} + \frac{1}{6} + \frac{1}{13}} \approx 5.37 & F = \sqrt{\dfrac{3^2 + 6^2 + 6^2 + 13^2}{4}} \approx 7.90 \\\\[3ex]
C = 6 & G = 8 \\\\[1.5ex]
D = \left( 3 \cdot 6 \cdot 6 \cdot 13 \right)^{1/4} \approx 6.12 & H = 13 \\\\
\end{array}
$$
</div>

1.  (3 pts) What value of <span class="math-inline">\\(w^{\ast}\\)</span> minimizes <span class="math-inline">\\(R(w) = \displaystyle \frac{1}{4} \sum&#95;{i=1}^4 (y&#95;i - w)^2\\)</span>?

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(A\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(B\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(C\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(D\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(E\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(F\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(G\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(H\\)</span></span></div>

    <details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(A\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(B\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(C\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(D\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(E\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(F\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(G\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(H\\)</span></span></div>

```python
For (i), the minimizer of mean squared error is the mean, so
```
<div class="math-display">
$$
w^* = \frac{3+6+6+13}{4} = \boxed{7}
$$
</div>

    </details>

**(ii)** (3 pts) What value of <span class="math-inline">\\(w^{\ast}\\)</span> minimizes <span class="math-inline">\\(R(w) = \displaystyle \lim&#95;{p \to \infty} \displaystyle \frac{1}{4} \sum&#95;{i=1}^4 |y&#95;i - w|^p\\)</span>?

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(A\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(B\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(C\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(D\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(E\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(F\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(G\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(H\\)</span></span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(A\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(B\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(C\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(D\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(E\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(F\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(G\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(H\\)</span></span></div>

```python
For (ii), as <span class="math-inline">\\(p \to \infty\\)</span>, the largest value of <span class="math-inline">\\(|y&#95;i-w|\\)</span> dominates. So we should put <span class="math-inline">\\(w\\)</span> halfway between the smallest and largest data values, as discussed in [Chapter 1.4](https://notes.eecs245.org/introduction-to-supervised-learning/comparing-loss-functions/#beyond-absolute-and-squared-loss).
```
<div class="math-display">
$$
w^* = \frac{3+13}{2} = \boxed{8}
$$
</div>

</details>

**(iii)** (3 pts) What value of <span class="math-inline">\\(w^{\ast}\\)</span> minimizes <span class="math-inline">\\(R(w) = \displaystyle \frac{1}{4} \sum&#95;{i=1}^4 (\log(y&#95;i) - \log(w))^2\\)</span>?

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(A\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(B\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(C\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(D\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(E\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(F\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(G\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(H\\)</span></span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(A\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(B\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(C\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(D\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(E\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(F\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(G\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(H\\)</span></span></div>

```python
For (iii), let <span class="math-inline">\\(u=\log(w)\\)</span>. The problem is now asking for the best constant prediction for the transformed values <span class="math-inline">\\(\log(y&#95;i)\\)</span>, so
```
<div class="math-display">
$$
u^* = \frac{\log(3)+\log(6)+\log(6)+\log(13) = \log(3 \cdot 6 \cdot 6 \cdot 13)}{4}
$$
</div>

 Exponentiating gives

<div class="math-display">
$$
w^* = e^{u^*} = \boxed{(3 \cdot 6 \cdot 6 \cdot 13)^{1/4}}
$$
</div>

 This was also a homework problem.

</details>

**(iv)** (3 pts) The slope of the graph of <span class="math-inline">\\(R(w) = \displaystyle\frac{1}{4} \sum&#95;{i = 1}^4 |y&#95;i - w|\\)</span> at <span class="math-inline">\\(w = \alpha\\)</span> is <span class="math-inline">\\(-1/2\\)</span>. Among the options above, which could be <span class="math-inline">\\(\alpha\\)</span>?

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(A\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(B\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(C\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(D\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(E\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(F\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(G\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(H\\)</span></span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(A\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(B\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(C\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(D\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(E\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(F\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(G\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(H\\)</span></span></div>

```python
For (iv), the slope of mean absolute error at any <span class="math-inline">\\(w\\)</span> that is not a data point is
```
<div class="math-display">
$$
\frac{\text{\# left of } w - \text{\# right of } w}{n}
$$
</div>

Here, in order to achieve a slope of <span class="math-inline">\\(-1/2\\)</span>, we need to have 1 data point to the left of <span class="math-inline">\\(w\\)</span> and 3 to the right, since <span class="math-inline">\\(\frac{1-3}{4} = -1/2\\)</span>. This means we need <span class="math-inline">\\(w\\)</span> to be between <span class="math-inline">\\(3\\)</span> and <span class="math-inline">\\(6\\)</span>, **exclusive**. The only value in this interval is <span class="math-inline">\\(B\\)</span>,

<div class="math-display">
$$
\boxed{\dfrac{4}{\frac{1}{3}+\frac{1}{6}+\frac{1}{6}+\frac{1}{13}} \approx 5.37}
$$
</div>

</details>

---

## Problem 2: (13 pts) <span class="math-inline">\\(\boxed{\text{Counts towards Midterm 1 redemption score}}\\)</span>

Suppose a dataset of <span class="math-inline">\\(n\\)</span> points, <span class="math-inline">\\((x&#95;1, y&#95;1), (x&#95;2, y&#95;2), \ldots, (x&#95;n, y&#95;n)\\)</span>, has the following properties:

<div class="math-display">
$$
\text{mean of y-values} = \bar y = 11,
\qquad
\text{standard deviation of x-values} = \sigma_x = 2,
\qquad
\sigma_y = 6
$$
</div>

 The simple linear regression line that minimizes mean squared error for predicting <span class="math-inline">\\(y&#95;i\\)</span> from <span class="math-inline">\\(x&#95;i\\)</span> is

<div class="math-display">
$$
h(x_i) = 15 - x_i
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> What is <span class="math-inline">\\(\bar x\\)</span>, the mean of the <span class="math-inline">\\(x\\)</span>-values? Give your answer as a number with no variables.

<span class="math-inline">\\(\bar x = \boxed{\textbf{4}}\\)</span>

<details markdown="1"><summary>Solution</summary>

The regression line must pass through <span class="math-inline">\\((\bar x, \bar y)\\)</span>, so

<div class="math-display">
$$
11 = 15 - \bar x
$$
</div>

 This gives

<div class="math-display">
$$
\bar x = \boxed{4}
$$
</div>

</details>

Now, consider a new dataset, <span class="math-inline">\\((t&#95;1, z&#95;1), (t&#95;2, z&#95;2), \ldots, (t&#95;n, z&#95;n)\\)</span>, defined by <span class="math-inline">\\(t&#95;i = 5 - x&#95;i\\)</span> and <span class="math-inline">\\(z&#95;i = 2y&#95;i - 1\\)</span>.

Let <span class="math-inline">\\(g(t&#95;i) = \beta&#95;0^{\ast} + \beta&#95;1^{\ast} t&#95;i\\)</span> be the best simple linear regression line for predicting <span class="math-inline">\\(z&#95;i\\)</span> from <span class="math-inline">\\(t&#95;i\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Find <span class="math-inline">\\(\beta&#95;0^{\ast}\\)</span>, the intercept of the best simple linear regression line for predicting <span class="math-inline">\\(z&#95;i\\)</span> from <span class="math-inline">\\(t&#95;i\\)</span>. Show your work, and write your final answer in the box provided. Your answer should be a number with no variables.

<div class="math-display">
$$
\beta_0^* = \boxed{\textbf{19}}
$$
</div>

<details markdown="1"><summary>Solution</summary>

First, use the original regression line to find the original correlation, which we'll call <span class="math-inline">\\(r&#95;{xy}\\)</span>. The slope is <span class="math-inline">\\(-1\\)</span>, so

<div class="math-display">
$$
-1 = r_{xy} \cdot \frac{\sigma_y}{\sigma_x}
= r \cdot \frac{6}{2}
= 3r_{xy}
$$
</div>

 This gives

<div class="math-display">
$$
r_{xy} = -\frac{1}{3}
$$
</div>

Now, what is <span class="math-inline">\\(r&#95;{tz}\\)</span>? Replacing <span class="math-inline">\\(x&#95;i\\)</span> with <span class="math-inline">\\(t&#95;i=5-x&#95;i\\)</span> flips the sign of the correlation, while replacing <span class="math-inline">\\(y&#95;i\\)</span> with <span class="math-inline">\\(z&#95;i=2y&#95;i-1\\)</span> keeps the sign the same. So the correlation between <span class="math-inline">\\(t&#95;i\\)</span> and <span class="math-inline">\\(z&#95;i\\)</span> is

<div class="math-display">
$$
r_{tz} = \frac{1}{3}
$$
</div>

Also,

<div class="math-display">
$$
\bar t = 5-\bar x = 5 - 4 = 1,
\qquad
\bar z = 2\bar y - 1 = 2 \cdot 11 - 1 = 21
$$
</div>



<div class="math-display">
$$
\sigma_t = \sigma_x = 2,
\qquad
\sigma_z = |2| \sigma_y = 2 \cdot 6 = 12
$$
</div>

Where did these facts come from? In general, if <span class="math-inline">\\(x&#95;1, x&#95;2, ..., x&#95;n\\)</span> have a mean of <span class="math-inline">\\(\bar x\\)</span> and a standard deviation of <span class="math-inline">\\(\sigma&#95;x\\)</span>, then <span class="math-inline">\\(a x&#95;1 + b, a x&#95;2 + b, ..., a x&#95;n + b\\)</span> have a mean of <span class="math-inline">\\(a \bar x + b\\)</span> and a standard deviation of <span class="math-inline">\\(|a| \sigma&#95;x\\)</span>. This was discussed in an early homework problem.

The new slope is, then

<div class="math-display">
$$
\beta_1^* = r_{tz} \cdot \frac{\sigma_z}{\sigma_t} = r_{tz} \cdot \frac{12}{2} = 6 r_{tz} = 6 \cdot \frac{1}{3} = 2
$$
</div>

 Since the new regression line passes through <span class="math-inline">\\((\bar t,\bar z) = (1, 21)\\)</span>, we have

<div class="math-display">
$$
\bar z = \beta_0^* + \beta_1^* \bar t \implies 21 = \beta_0^* + 2 \cdot 1 \implies \beta_0^* = 19
$$
</div>

Thus, <span class="math-inline">\\(\boxed{\beta&#95;0^{\ast} = 19}\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Let <span class="math-inline">\\(M\\)</span> be the mean squared error of the model <span class="math-inline">\\(h(x&#95;i) = 15 - x&#95;i\\)</span>'s predictions on the dataset <span class="math-inline">\\((x&#95;1, y&#95;1), (x&#95;2, y&#95;2), \ldots, (x&#95;n, y&#95;n)\\)</span>, and <span class="math-inline">\\(M'\\)</span> be the mean squared error of the model <span class="math-inline">\\(g(t&#95;i) = \beta&#95;0^{\ast} + \beta&#95;1^{\ast} t&#95;i\\)</span>'s predictions on the dataset <span class="math-inline">\\((t&#95;1, z&#95;1), (t&#95;2, z&#95;2), \ldots, (t&#95;n, z&#95;n)\\)</span>.

What is the value of the fraction <span class="math-inline">\\(\frac{M}{M'}\\)</span>? *If it's not clear, <span class="math-inline">\\(M'\\)</span> is on the denominator.*

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1/5\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1/4\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1/2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(4\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(5\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Impossible to tell</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1/5\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1/4\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1/2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(4\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(5\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Impossible to tell</span></div>

The intuitive answer is that since we've stretched out the <span class="math-inline">\\(y\\)</span>-values by a factor of <span class="math-inline">\\(2\\)</span>, the mean squared error is multiplied by a factor of <span class="math-inline">\\(4\\)</span>, so the fraction <span class="math-inline">\\(\frac{M}{M'}\\)</span> is <span class="math-inline">\\(\frac{1}{4}\\)</span>.

Let's show this a bit more formally. First, note that

<div class="math-display">
$$
M = \frac{1}{n} \sum_{i=1}^n (y_i - (15 - x_i))^2
$$
</div>

Can we write <span class="math-inline">\\(M'\\)</span> in terms of <span class="math-inline">\\(M\\)</span>? Yes, we can.

<div class="math-display">
$$
M' = \frac{1}{n} \sum_{i=1}^n (z_i - (\beta_0^* + \beta_1^* t_i))^2
$$
</div>

Using the fact that <span class="math-inline">\\(z&#95;i = 2y&#95;i - 1\\)</span>, <span class="math-inline">\\(t&#95;i = 5 - x&#95;i\\)</span>, <span class="math-inline">\\(\beta&#95;0^{\ast} = 19\\)</span>, and <span class="math-inline">\\(\beta&#95;1^{\ast} = 2\\)</span> gives

<div class="math-display">
$$
\begin{align*}
M' &= \frac{1}{n} \sum_{i=1}^n \big(z_i - (\beta_0^* + \beta_1^* t_i)\big)^2 \\\\
&= \frac{1}{n} \sum_{i=1}^n \big((2y_i - 1) - (19 + 2 (5 - x_i))\big)^2 \\\\
&= \frac{1}{n} \sum_{i=1}^n \big((2y_i - 1) - (19 + 10 - 2x_i)\big)^2 \\\\
&= \frac{1}{n} \sum_{i=1}^n \big(2y_i - 30 + 2x_i\big)^2 \\\\
&= \frac{1}{n} \sum_{i=1}^n \big(2(y_i - 15 + x_i)\big)^2 \\\\
&= 4 \cdot \frac{1}{n} \sum_{i=1}^n (y_i - (15 - x_i))^2 \\\\
&= 4M
\end{align*}
$$
</div>

So, since <span class="math-inline">\\(M' = 4M\\)</span>,

<div class="math-display">
$$
\frac{M}{M'} = \frac{M}{4M} = \boxed{\frac{1}{4}}
$$
</div>

</details>

</div>
</div>

</div>

---

## Problem 3: (9 pts) <span class="math-inline">\\(\boxed{\text{Counts towards Midterm 1 redemption score}}\\)</span>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">5 pts</span> Suppose <span class="math-inline">\\(\vec a = \begin{bmatrix} 0 \\\\ 3 \\\\ 6 \end{bmatrix}\\)</span> and that <span class="math-inline">\\(\vec b\\)</span> is another vector in <span class="math-inline">\\(\mathbb{R}^3\\)</span> such that:

-   <span class="math-inline">\\(\vec a\\)</span> and <span class="math-inline">\\(\vec b\\)</span> are orthogonal, and

-   the plane spanned by <span class="math-inline">\\(\vec a\\)</span> and <span class="math-inline">\\(\vec b\\)</span> is

<div class="math-display">
$$
4x - 2y + z = 0
$$
</div>

There are infinitely many possible vectors <span class="math-inline">\\(\vec b\\)</span> that satisfy the given conditions. State **one** of them. Show your work, and write your final answer in the box provided. Your answer should be a vector with no variables.

<div class="math-display">
$$
\text{one possible \vec b} = \boxed{\textbf{}}
$$
</div>

<details markdown="1"><summary>Solution</summary>

Let <span class="math-inline">\\(\vec b = \begin{bmatrix} x \\\\ y \\\\ z \end{bmatrix}\\)</span>.

Since <span class="math-inline">\\(\vec b\\)</span> lies in the given plane,

<div class="math-display">
$$
4x-2y+z=0
$$
</div>

 Since <span class="math-inline">\\(\vec a\\)</span> and <span class="math-inline">\\(\vec b\\)</span> are orthogonal,

<div class="math-display">
$$
\vec a \cdot \vec b = 3y+6z=0
$$
</div>

 The second equation gives <span class="math-inline">\\(y=-2z\\)</span>. Plugging this into the first equation gives

<div class="math-display">
$$
4x+4z+z=0
\implies
x=-\frac{5}{4}z
$$
</div>

 There are infinitely many solutions for <span class="math-inline">\\(x\\)</span>, <span class="math-inline">\\(y\\)</span>, and <span class="math-inline">\\(z\\)</span>; they all lie on a line. To state one, let's just fix a value of <span class="math-inline">\\(z\\)</span>. Arbitrarily choosing <span class="math-inline">\\(z = 4\\)</span> gives

<div class="math-display">
$$
\vec b = \boxed{\begin{bmatrix}-5\\\\-8\\\\4\end{bmatrix}}
$$
</div>

Here's another solution: really, the question is asking for a vector that is orthogonal to both <span class="math-inline">\\(\vec a\\)</span> and <span class="math-inline">\\(\begin{bmatrix} 4 \\\\ -2 \\\\ 1 \end{bmatrix}\\)</span>. Such a vector would be orthogonal to <span class="math-inline">\\(\vec a\\)</span> and would lie in the plane <span class="math-inline">\\(4x-2y+z=0\\)</span>. So, all we need to do is take the cross product of <span class="math-inline">\\(\vec a\\)</span> and <span class="math-inline">\\(\begin{bmatrix} 4 \\\\ -2 \\\\ 1 \end{bmatrix}\\)</span>.

<div class="math-display">
$$
\underbrace{\begin{bmatrix} 0 \\\\ 3 \\\\ 6 \end{bmatrix}}_{\vec a} \times \begin{bmatrix} 4 \\\\ -2 \\\\ 1 \end{bmatrix} = \begin{bmatrix} 3 \cdot 1 - 6 \cdot (-2) \\\\ 6 \cdot 4 - 0 \cdot 1 \\\\ 0 \cdot (-2) - 3 \cdot 4 \end{bmatrix} = \boxed{\begin{bmatrix} 15 \\\\ 24 \\\\ -12 \end{bmatrix}}
$$
</div>

Note that this is just <span class="math-inline">\\(-3\\)</span> times the vector we found above. Indeed, any scalar multiple of <span class="math-inline">\\(\begin{bmatrix} -5 \\\\ -8 \\\\ 4 \end{bmatrix}\\)</span> is also a solution.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> This part is unrelated to the previous part. Suppose <span class="math-inline">\\(\vec u, \vec v \in \mathbb{R}^n\\)</span>, and that:

-   <span class="math-inline">\\(\vec u\\)</span> is a unit vector,

-   <span class="math-inline">\\(\cos(\theta) = 2/3\\)</span>, where <span class="math-inline">\\(\theta\\)</span> is the angle between <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span>,

-   the projection of <span class="math-inline">\\(\vec v\\)</span> onto <span class="math-inline">\\(\vec u\\)</span> is <span class="math-inline">\\(6 \vec u\\)</span>.

What is the value of <span class="math-inline">\\(\lVert \vec v \rVert\\)</span>?

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(3\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(4\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(6\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(9\\)</span></span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(3\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(4\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(6\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(9\\)</span></span></div>

Since <span class="math-inline">\\(\vec u\\)</span> is a unit vector,

<div class="math-display">
$$
\vec p
= \frac{\vec v \cdot \vec u}{\vec u \cdot \vec u} \vec u
=
(\vec v \cdot \vec u)\vec u
$$
</div>

But this projection is also <span class="math-inline">\\(6 \vec u\\)</span>, so

<div class="math-display">
$$
\vec u \cdot \vec v = 6
$$
</div>

Now, let's use the fact that <span class="math-inline">\\(\cos(\theta) = 2/3\\)</span>, where <span class="math-inline">\\(\theta\\)</span> is the angle between <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span>, and plug in the values we know.

<div class="math-display">
$$
\begin{align*}
\cos \theta &= \frac{\vec u \cdot \vec v}{\lVert \vec u \rVert \lVert \vec v \rVert} \\\\
\frac{2}{3} &= \frac{6}{1 \cdot \lVert \vec v \rVert} \\\\
\lVert \vec v \rVert &= 9
\end{align*}
$$
</div>

So, <span class="math-inline">\\(\boxed{\lVert \vec v \rVert = 9}\\)</span>.
</details>

</div>
</div>

</div>

---

## Problem 4: (4 pts) <span class="math-inline">\\(\boxed{\text{Counts towards Midterm 1 redemption score}}\\)</span>

Let

<div class="math-display">
$$
S =
\left\{
\begin{bmatrix}
x_1\\\\x_2\\\\x_3\\\\x_4\\\\x_5\\\\x_6
\end{bmatrix}
\in \mathbb{R}^6
:
x_1+x_2+x_3=0
\text{ and }
x_4=x_5
\right\}
$$
</div>

Find <span class="math-inline">\\(\dim(S)\\)</span>. Give your answer as an integer with no variables.

<span class="math-inline">\\(\dim(S)=\boxed{\textbf{4}}\\)</span>

<details markdown="1"><summary>Solution</summary>

There are <span class="math-inline">\\(6\\)</span> variables total. The condition

<div class="math-display">
$$
x_1+x_2+x_3=0
$$
</div>

 removes one degree of flexibility, and the condition

<div class="math-display">
$$
x_4=x_5
$$
</div>

 removes one flexibility. So

<div class="math-display">
$$
\dim(S) = 6-2 = \boxed{4}
$$
</div>

Another way to think about it is to think of what a basis for <span class="math-inline">\\(S\\)</span> looks like. Every vector in <span class="math-inline">\\(S\\)</span> is of the form

<div class="math-display">
$$
\begin{bmatrix} a \\\\ b \\\\ -a-b \\\\ c \\\\ c \\\\ d \end{bmatrix}
$$
</div>

where <span class="math-inline">\\(a, b, c, d\\)</span> are real numbers. <span class="math-inline">\\(a\\)</span> and <span class="math-inline">\\(b\\)</span> (components 1 and 2) can both be anything, but component 3 is automatically determined once <span class="math-inline">\\(a\\)</span> and <span class="math-inline">\\(b\\)</span> are chosen. Similarly, <span class="math-inline">\\(c\\)</span> and <span class="math-inline">\\(d\\)</span> (components 4 and 6) can both be anything, but once component 4 is chosen, component 5 is automatically determined.

<span class="math-inline">\\(S\\)</span> is the set of all vectors that fit the template above. But

<div class="math-display">
$$
\begin{bmatrix} a \\\\ b \\\\ -a-b \\\\ c \\\\ c \\\\ d \end{bmatrix} = a \begin{bmatrix} 1 \\\\ 0 \\\\ -1 \\\\ 0 \\\\ 0 \\\\ 0 \end{bmatrix} + b \begin{bmatrix} 0 \\\\ 1 \\\\ -1 \\\\ 0 \\\\ 0 \\\\ 0 \end{bmatrix} + c \begin{bmatrix} 0 \\\\ 0 \\\\ 0 \\\\ 1 \\\\ 1 \\\\ 0 \end{bmatrix} + d \begin{bmatrix} 0 \\\\ 0 \\\\ 0 \\\\ 0 \\\\ 0 \\\\ 1 \end{bmatrix}
$$
</div>

So, <span class="math-inline">\\(S = \text{span}\left(\left\lbrace \begin{bmatrix} 1 \\\\ 0 \\\\ -1 \\\\ 0 \\\\ 0 \\\\ 0 \end{bmatrix}, \begin{bmatrix} 0 \\\\ 1 \\\\ -1 \\\\ 0 \\\\ 0 \\\\ 0 \end{bmatrix}, \begin{bmatrix} 0 \\\\ 0 \\\\ 0 \\\\ 1 \\\\ 1 \\\\ 0 \end{bmatrix}, \begin{bmatrix} 0 \\\\ 0 \\\\ 0 \\\\ 0 \\\\ 0 \\\\ 1 \end{bmatrix} \right\rbrace\right)\\)</span>. This is a 4-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^6\\)</span>, so <span class="math-inline">\\(\dim(S) = 4\\)</span>.
</details>

---

## Problem 5: (11 pts) <span class="math-inline">\\(\boxed{\text{Counts towards Midterm 2 redemption score}}\\)</span>

Suppose <span class="math-inline">\\(A\\)</span> is a <span class="math-inline">\\(6 \times 5\\)</span> matrix such that

<div class="math-display">
$$
\text{nullsp}(A)
=
\text{span}\left(
\left\{
\begin{bmatrix}1\\\\0\\\\1\\\\0\\\\0\end{bmatrix},
\begin{bmatrix}0\\\\1\\\\1\\\\0\\\\0\end{bmatrix},
\begin{bmatrix}0\\\\0\\\\0\\\\1\\\\1\end{bmatrix}
\right\}
\right)
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Find <span class="math-inline">\\(\text{rank}(A)\\)</span> and <span class="math-inline">\\(\dim(\text{nullsp}(A^T))\\)</span>. Give your answers as integers with no variables.

<span class="math-inline">\\(\text{rank}(A) = \boxed{\textbf{2}}  \dim(\text{nullsp}(A^T)) = \boxed{\textbf{4}}\\)</span>

<details markdown="1"><summary>Solution</summary>

Recall, the rank-nullity theorem states that for any matrix <span class="math-inline">\\(A\\)</span>,

<div class="math-display">
$$
\text{rank}(A) + \dim(\text{nullsp}(A)) = \text{number of columns of } A
$$
</div>

The null space has dimension <span class="math-inline">\\(3\\)</span>, since the given basis has <span class="math-inline">\\(3\\)</span> vectors. Because <span class="math-inline">\\(A\\)</span> has <span class="math-inline">\\(5\\)</span> columns, rank-nullity gives

<div class="math-display">
$$
\text{rank}(A) + 3 = 5
\implies \text{rank}(A) = \boxed{2}
$$
</div>

 Also, <span class="math-inline">\\(A^T\\)</span> has <span class="math-inline">\\(6\\)</span> columns and <span class="math-inline">\\(\text{rank}(A^T)=\text{rank}(A)=2\\)</span>, so rank-nullity gives

<div class="math-display">
$$
\dim(\text{nullsp}(A^T)) = 6-2 = \boxed{4}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> Which of the following **could NOT** be the first row of <span class="math-inline">\\(A\\)</span>?

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} 2 &amp; 2 &amp; -2 &amp; 3 &amp; -3 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} 1 &amp; 1 &amp; -1 &amp; 4 &amp; -4 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} 2 &amp; 0 &amp; -2 &amp; 5 &amp; -5 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} 3 &amp; 3 &amp; -3 &amp; -2 &amp; 2 \end{bmatrix}\\)</span></span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} 2 &amp; 2 &amp; -2 &amp; 3 &amp; -3 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} 1 &amp; 1 &amp; -1 &amp; 4 &amp; -4 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} 2 &amp; 0 &amp; -2 &amp; 5 &amp; -5 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} 3 &amp; 3 &amp; -3 &amp; -2 &amp; 2 \end{bmatrix}\\)</span></span></div>

A key fact is that the row space and null space of a matrix are orthogonal complements, as discussed in [Chapter 5.4](https://notes.eecs245.org/matrices/null-space-rank-nullity/#example-orthogonal-complements) (and the linked video). What this means is that every row of <span class="math-inline">\\(A\\)</span> is orthogonal to every vector in <span class="math-inline">\\(\text{nullsp}(A)\\)</span>.

So a row

<div class="math-display">
$$
\begin{bmatrix} a & b & c & d & e \end{bmatrix}
$$
</div>

 must satisfy

<div class="math-display">
$$
a+c = 0,
\qquad
b+c = 0,
\qquad
d+e = 0
$$
</div>

Equivalently, every row of <span class="math-inline">\\(A\\)</span> must have the form

<div class="math-display">
$$
\begin{bmatrix} a & a & -a & d & -d \end{bmatrix}
$$
</div>

The first, second, and fourth options all have this form. The third option,

<div class="math-display">
$$
\begin{bmatrix} 2 & 0 & -2 & 5 & -5 \end{bmatrix}
$$
</div>

 does not. For instance, it is not orthogonal to

<div class="math-display">
$$
\begin{bmatrix}0\\\\1\\\\1\\\\0\\\\0\end{bmatrix}
\in \text{nullsp}(A)
$$
</div>

 since

<div class="math-display">
$$
\begin{bmatrix} 2 & 0 & -2 & 5 & -5 \end{bmatrix}
\begin{bmatrix}0\\\\1\\\\1\\\\0\\\\0\end{bmatrix}
= -2 \neq 0
$$
</div>

So the correct answer is the **third** option, <span class="math-inline">\\(\boxed{\begin{bmatrix} 2 &amp; 0 &amp; -2 &amp; 5 &amp; -5 \end{bmatrix}}\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Let <span class="math-inline">\\(\vec a^{(1)}, \vec a^{(2)}, \vec a^{(3)}, \vec a^{(4)}, \vec a^{(5)} \in \mathbb{R}^6\\)</span> be the columns of <span class="math-inline">\\(A\\)</span>.

Below, select **one possible set** of columns of <span class="math-inline">\\(A\\)</span> that form a basis for <span class="math-inline">\\(\text{colsp}(A)\\)</span>. You should select the fewest possible number of columns needed to span <span class="math-inline">\\(\text{colsp}(A)\\)</span>.

<div class="math-display">
$$
\begin{array}{c|c}
\text{Column} & \text{Include in your basis?} \\\\ \hline
\vec a^{(1)} & $\square$  \quad  \\\\
\vec a^{(2)} & $\square$  \quad  \\\\
\vec a^{(3)} & $\square$  \quad  \\\\
\vec a^{(4)} & $\square$  \quad  \\\\
\vec a^{(5)} & $\square$  \quad
\end{array}
$$
</div>

<details markdown="1"><summary>Solution</summary>

<span class="mc-square" aria-hidden="true"></span>

The vector

<div class="math-display">
$$
\begin{bmatrix}1\\\\0\\\\1\\\\0\\\\0\end{bmatrix}
\in \text{nullsp}(A)
$$
</div>

 tells us

<div class="math-display">
$$
\vec a^{(1)}+\vec a^{(3)}=\vec 0 \implies \vec a^{(3)} = -\vec a^{(1)}
$$
</div>

 and the vector

<div class="math-display">
$$
\begin{bmatrix}0\\\\1\\\\1\\\\0\\\\0\end{bmatrix}
\in \text{nullsp}(A)
$$
</div>

 tells us

<div class="math-display">
$$
\vec a^{(2)}+\vec a^{(3)}=\vec 0 \implies \vec a^{(3)} = -\vec a^{(2)}
$$
</div>

 So <span class="math-inline">\\(\vec a^{(1)}\\)</span>, <span class="math-inline">\\(\vec a^{(2)}\\)</span>, and <span class="math-inline">\\(\vec a^{(3)}\\)</span> all lie on the same line and are scalar multiples of each other. Similarly,

<div class="math-display">
$$
\begin{bmatrix}0\\\\0\\\\0\\\\1\\\\1\end{bmatrix}
\in \text{nullsp}(A)
$$
</div>

 tells us

<div class="math-display">
$$
\vec a^{(4)}+\vec a^{(5)}=\vec 0 \implies \vec a^{(5)} = -\vec a^{(4)}
$$
</div>

 Since <span class="math-inline">\\(\text{rank}(A)=2\\)</span>, the column space is 2-dimensional. A basis for the column space comes from picking one of <span class="math-inline">\\(\lbrace \vec a^{(1)}, \vec a^{(2)}, \vec a^{(3)} \rbrace\\)</span> and one of <span class="math-inline">\\(\lbrace \vec a^{(4)}, \vec a^{(5)} \rbrace\\)</span>. There are therefore 6 possible options; one of them is

<div class="math-display">
$$
\boxed{\{\vec a^{(1)}, \vec a^{(4)}\}}
$$
</div>

</details>

</div>
</div>

</div>

---

## Problem 6: (12 pts) <span class="math-inline">\\(\boxed{\text{Counts towards Midterm 2 redemption score}}\\)</span>

Suppose <span class="math-inline">\\(X\\)</span> is an <span class="math-inline">\\(n \times 3\\)</span> matrix, where <span class="math-inline">\\(n &gt; 2\\)</span>, with columns <span class="math-inline">\\(\vec x^{(1)}\\)</span>, <span class="math-inline">\\(\vec x^{(2)}\\)</span>, and <span class="math-inline">\\(\vec x^{(3)}\\)</span>. Furthermore, suppose that <span class="math-inline">\\(X = QR\\)</span>, where

<div class="math-display">
$$
Q =
\begin{bmatrix}
\vert & \vert \\\\
\vec q^{(1)} & \vec q^{(2)} \\\\
\vert & \vert
\end{bmatrix}
$$
</div>

 is an <span class="math-inline">\\(n \times 2\\)</span> matrix with orthonormal columns, and

<div class="math-display">
$$
R =
\begin{bmatrix}
2 & 0 & 2\\\\
0 & 1 & -1
\end{bmatrix}
$$
</div>

Lastly, suppose <span class="math-inline">\\(\vec y \in \mathbb{R}^n\\)</span> and <span class="math-inline">\\(Q^T \vec y = \begin{bmatrix} -2 \\\\ 10 \end{bmatrix}\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Let <span class="math-inline">\\(\vec p\\)</span> be the projection of <span class="math-inline">\\(\vec y\\)</span> onto <span class="math-inline">\\(\text{colsp}(X)\\)</span>. Write <span class="math-inline">\\(\vec p\\)</span> as a linear combination of the columns of <span class="math-inline">\\(X\\)</span>. Fill in each box with a number with no variables. If there are multiple correct answers, you only need to provide one.

<span class="math-inline">\\(\vec p = \boxed{\textbf{-1}}  \vec x^{(1)} + \boxed{\textbf{10}}  \vec x^{(2)} + \boxed{\textbf{0}}  \vec x^{(3)}\\)</span>

<details markdown="1"><summary>Solution</summary>

The columns of <span class="math-inline">\\(Q\\)</span> are a basis for <span class="math-inline">\\(\text{colsp}(X)\\)</span> (since <span class="math-inline">\\(X = QR\\)</span> writes every column of <span class="math-inline">\\(X\\)</span> as a linear combination of the columns of <span class="math-inline">\\(Q\\)</span>). So, the general strategy is to first write <span class="math-inline">\\(\vec p\\)</span> as a linear combination of the columns of <span class="math-inline">\\(Q\\)</span>, and then use the information in <span class="math-inline">\\(R\\)</span> to write that as a linear combination of the columns of <span class="math-inline">\\(X\\)</span>.

If <span class="math-inline">\\(X\\)</span> is a full rank matrix, then the projection of <span class="math-inline">\\(\vec y\\)</span> onto <span class="math-inline">\\(\text{colsp}(X)\\)</span> is

<div class="math-display">
$$
X (X^TX)^{-1}X^T \vec y
$$
</div>

<span class="math-inline">\\(X\\)</span> isn't full rank here, but <span class="math-inline">\\(Q\\)</span> is, and that is the matrix whose columns we're writing <span class="math-inline">\\(\vec p\\)</span> as a linear combination of to begin with. So, we have

<div class="math-display">
$$
\vec p = Q (Q^TQ)^{-1}Q^T \vec y
$$
</div>

But, since <span class="math-inline">\\(Q\\)</span>'s columns are orthonormal, <span class="math-inline">\\(Q^TQ = I\\)</span>, so

<div class="math-display">
$$
\vec p = Q (Q^TQ)^{-1} Q^T \vec y = Q I Q^T \vec y = Q Q^T \vec y = Q \begin{bmatrix} -2 \\\\ 10 \end{bmatrix} = -2 \vec q^{(1)}+10 \vec q^{(2)}
$$
</div>

Good, so now we have <span class="math-inline">\\(\vec p\\)</span> as a linear combination of the columns of <span class="math-inline">\\(Q\\)</span>. How do the columns of <span class="math-inline">\\(X\\)</span> relate to the columns of <span class="math-inline">\\(Q\\)</span>? <span class="math-inline">\\(R = \begin{bmatrix} 2 &amp; 0 &amp; 2\\\\0 &amp; 1 &amp; -1 \end{bmatrix}\\)</span> tells us that

<div class="math-display">
$$
\vec x^{(1)} = 2\vec q^{(1)},
\qquad
\vec x^{(2)} = \vec q^{(2)},
\qquad
\vec x^{(3)} = 2\vec q^{(1)}-\vec q^{(2)}
$$
</div>

 So, one possible answer comes from

<div class="math-display">
$$
\vec p = \boxed{-\vec x^{(1)}+10\vec x^{(2)}+0\vec x^{(3)}}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Let <span class="math-inline">\\(\vec w^{\ast}\\)</span> be a minimizer of

<div class="math-display">
$$
R_\text{sq}(w) = \frac{1}{n}\lVert \vec y - X \vec w \rVert^2
$$
</div>

 Fill in the blanks to describe the set of all possible values of <span class="math-inline">\\(\vec w^{\ast}\\)</span>. Each blank should contain a vector with no variables.

<span class="math-inline">\\(\text{set of all possible } \vec w^{\ast} = \left\lbrace \boxed{\textbf{\begin{bmatrix}-1\\\\10\\\\0\end{bmatrix}}} + t  \boxed{\textbf{\begin{bmatrix}-1\\\\1\\\\1\end{bmatrix}}} : t \in \mathbb{R} \right\rbrace\\)</span>.

<details markdown="1"><summary>Solution</summary>

From the previous part, we know one possible minimizer is

<div class="math-display">
$$
\vec w^* = \begin{bmatrix}-1\\\\10\\\\0\end{bmatrix}
$$
</div>

As discussed in [Chapter 6.4](https://notes.eecs245.org/linear-transformations-and-projections/complete-solution/#finding-all-solutions), the full sete of minimizers results from taking one particular solution and adding any vector in <span class="math-inline">\\(\text{nullsp}(X)\\)</span>. So, all we need to do is find a basis for <span class="math-inline">\\(\text{nullsp}(X)\\)</span>.

Note that <span class="math-inline">\\(X\\)</span> has two linearly independent columns (<span class="math-inline">\\(\vec x^{(1)}\\)</span> and <span class="math-inline">\\(\vec x^{(2)}\\)</span>), with a third column defined by

<div class="math-display">
$$
\vec x^{(3)} = 2 \vec q^{(1)}-\vec q^{(2)} = \vec x^{(1)} - \vec x^{(2)}
$$
</div>

**Before continuing to read these solutions, make sure you understand why the statement above is true!**

Rearranging the above equation gives

<div class="math-display">
$$
\vec x^{(1)} - \vec x^{(2)} - \vec x^{(3)} = \vec 0
$$
</div>

The coefficients on the three vectors in the linear combination above are <span class="math-inline">\\(1\\)</span>, <span class="math-inline">\\(-1\\)</span>, and <span class="math-inline">\\(-1\\)</span>. So, <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ -1 \\\\ -1 \end{bmatrix}\\)</span> is in <span class="math-inline">\\(\text{nullsp}(X)\\)</span>. Not only that, but it's a basis for <span class="math-inline">\\(\text{nullsp}(X)\\)</span>, since <span class="math-inline">\\(\text{rank}(X) = 2\\)</span> and thus <span class="math-inline">\\(\text{dim}(\text{nullsp}(X)) = 3-2 = 1\\)</span> (meaning any one vector in <span class="math-inline">\\(\text{nullsp}(X)\\)</span> is a basis for it). Another commonly chosen basis for <span class="math-inline">\\(\text{nullsp}(X)\\)</span> was <span class="math-inline">\\(\begin{bmatrix} -1 \\\\ 1 \\\\ 1 \end{bmatrix}\\)</span>.

So, the full set of minimizers is

<div class="math-display">
$$
\boxed{\left\{ \begin{bmatrix}-1\\\\10\\\\0\end{bmatrix} + t \begin{bmatrix}1\\\\-1\\\\-1\end{bmatrix} : t \in \mathbb{R} \right\}}
$$
</div>

</details>

</div>
</div>

</div>

---

## Problem 7: (8 pts) <span class="math-inline">\\(\boxed{\text{Counts towards Midterm 2 redemption score}}\\)</span>

Suppose we'd like to fit a multiple linear regression model **without an intercept term** to predict an apartment's monthly rent (in hundreds of dollars) using various features.

For apartment <span class="math-inline">\\(i\\)</span>, the corresponding feature vector is <span class="math-inline">\\(\vec x&#95;i = \begin{bmatrix} \text{bedrooms}&#95;i &amp; K&#95;i &amp; C&#95;i &amp; N&#95;i \end{bmatrix}^T\\)</span>, where <span class="math-inline">\\(\text{bedrooms}&#95;i\\)</span> is the number of bedrooms in apartment <span class="math-inline">\\(i\\)</span>, and <span class="math-inline">\\(K&#95;i\\)</span>, <span class="math-inline">\\(C&#95;i\\)</span>, and <span class="math-inline">\\(N&#95;i\\)</span> are one hot encoded features for the Kerrytown, Central Campus, and North Campus neighborhoods, respectively.

The model is fit by minimizing mean squared error. **All rows of the dataset are shown to the right.** The model's predictions, <span class="math-inline">\\(h(x&#95;i)\\)</span>, are shown, along with the true rents, <span class="math-inline">\\(y&#95;i\\)</span>. Several values are missing.

<div class="math-display">
$$
\boxed{\renewcommand{\arraystretch}{1.3}
\begin{array}{c|c|c|c}
\text{bedrooms}_i & \text{neighborhood}_i & y_i & h(x_i) \\\\
\hline
4 & \text{K} & 17 & \boxed{(i)} \\\\
1 & \text{C} & \boxed{(ii)} & 9 \\\\
3 & \text{C} & 15 & 13 \\\\
2 & \text{C} & 10 & 11 \\\\
1 & \text{N} & 9 & \boxed{(iii)} \\\\
4 & \text{N} & 13 & \boxed{(iv)}
\end{array}
\renewcommand{\arraystretch}{1}}
$$
</div>

For instance, the first row of the design matrix

is <span class="math-inline">\\(\begin{bmatrix} 4 &amp; 1 &amp; 0 &amp; 0 \end{bmatrix}\\)</span>.

Find all four missing values in the table. Show your work, and write your final answers in the boxes provided. Your answers should be integers with no variables. <em>Hint: Think about orthogonality.</em>

<details markdown="1"><summary>Solution</summary>

For clarity, let's start by writing out the full design matrix <span class="math-inline">\\(X\\)</span>.

<div class="math-display">
$$
X = \begin{bmatrix}
  4 & 1 & 0 & 0 \\\\
  1 & 0 & 1 & 0 \\\\
  3 & 0 & 1 & 0 \\\\
  2 & 0 & 1 & 0 \\\\
  1 & 0 & 0 & 1 \\\\
  4 & 0 & 0 & 1 \end{bmatrix}
$$
</div>

Let <span class="math-inline">\\(e&#95;i = y&#95;i-h(x&#95;i)\\)</span> refer to the error for apartment <span class="math-inline">\\(i\\)</span>. Since the model is fit by minimizing mean squared error, the vector

<div class="math-display">
$$
\vec e = \begin{bmatrix} e_1 \\\\ e_2 \\\\ e_3 \\\\ e_4 \\\\ e_5 \\\\ e_6 \end{bmatrix} = \begin{bmatrix} y_1 - h(x_1) \\\\ y_2 - h(x_2) \\\\ y_3 - h(x_3) \\\\ y_4 - h(x_4) \\\\ y_5 - h(x_5) \\\\ y_6 - h(x_6) \end{bmatrix} = \begin{bmatrix} 17 - (i) \\\\ (ii) - 9 \\\\ 15 - 13 \\\\ 10 - 11 \\\\ 9 - (iii) \\\\ 13 - (iv) \end{bmatrix}
$$
</div>

 is orthogonal to every column of <span class="math-inline">\\(X\\)</span>.

-   First, let's take the dot product of the error vector with the second column of <span class="math-inline">\\(X\\)</span>, the one hot encoded column for Kerrytown. We know this dot product must be <span class="math-inline">\\(0\\)</span>.

<div class="math-display">
$$
\begin{bmatrix} 1 \\\\ 0 \\\\ 0 \\\\ 0 \\\\ 0 \\\\ 0 \end{bmatrix} \cdot \begin{bmatrix} 17 - (i) \\\\ (ii) - 9 \\\\ 15 - 13 \\\\ 10 - 11 \\\\ 9 - (iii) \\\\ 13 - (iv) \end{bmatrix} = 0 \implies 17 - (i) = 0 \implies \boxed{(i) = 17}
$$
</div>

 Intuitively, this says that the errors for Kerrytown apartments must sum to <span class="math-inline">\\(0\\)</span>. Since there is only one Kerrytown apartment, this means that its prediction must be correct.

-   Similarly, if we take the dot product of the error vector with the third column of <span class="math-inline">\\(X\\)</span>, this tells us that the errors for the Central Campus apartments must sum to <span class="math-inline">\\(0\\)</span>.

<div class="math-display">
$$
((ii) - 9) + (15 - 13) + (10 - 11) = 0 \implies (ii) - 9 + 2 - 1 = 0 \implies \boxed{(ii) = 8}
$$
</div>

-   Things are a little more complicated for (iii) and (iv): it's true that

<div class="math-display">
$$
(9 - (iii)) + (13 - (iv)) = 0 \implies (iii) + (iv) = 22
$$
</div>

 but this is not enough information to determine the values of (iii) and (iv). To get another equation, we can set the dot product of the error vector with the first column of <span class="math-inline">\\(X\\)</span> to <span class="math-inline">\\(0\\)</span>.



<div class="math-display">
$$
\begin{align*}
    \begin{bmatrix} 4 \\\\ 1 \\\\ 3 \\\\ 2 \\\\ 1 \\\\ 4 \end{bmatrix} \cdot \begin{bmatrix} 17 - \mathbf{17} \\\\ \mathbf{8} - 9 \\\\ 15 - 13 \\\\ 10 - 11 \\\\ 9 - (iii) \\\\ 13 - (iv) \end{bmatrix} &= 0 \\\\
    -1 + 3 \cdot 2 + 2 \cdot (-1) + 1 \cdot (9 - (iii)) + 4 \cdot (13 - (iv)) &= 0 \\\\
    (iii) + 4(iv) &= 64
    \end{align*}
$$
</div>

   So,

<div class="math-display">
$$
\left( (iii) + 4(iv) \right) - \left( (iii) + (iv) \right) = 64 - 22 \implies 3(iv) = 42 \implies \boxed{(iv) = 14}
$$
</div>

 and thus

<div class="math-display">
$$
(iii) + 14 = 22 \implies \boxed{(iii) = 8}
$$
</div>

To summarize,

<div class="math-display">
$$
\boxed{(i)=17,\qquad (ii)=8,\qquad (iii)=8,\qquad (iv)=14}
$$
</div>

</details>

---

## Problem 8: (9 pts) <span class="math-inline">\\(\boxed{\text{Counts towards Midterm 2 redemption score}}\\)</span>

Consider the function <span class="math-inline">\\(g: \mathbb{R}^3 \to \mathbb{R}\\)</span>. We'd like to minimize <span class="math-inline">\\(g\\)</span> using gradient descent.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(6 pts) Suppose two separate runs of gradient descent are started from **the same initial guess** <span class="math-inline">\\(\vec x^{(0)}\\)</span>, but with different learning rates (step sizes), <span class="math-inline">\\(\alpha\\)</span>.

If <span class="math-inline">\\(\alpha = 1/2\\)</span>, then <span class="math-inline">\\(\vec x^{(1)} = \begin{bmatrix} 1 \\\\ 1 \\\\ 1 \end{bmatrix}\\)</span>, and if <span class="math-inline">\\(\alpha = 1/4\\)</span>, then <span class="math-inline">\\(\vec x^{(1)} = \begin{bmatrix} 2 \\\\ 3 \\\\ 2 \end{bmatrix}\\)</span>.

Find <span class="math-inline">\\(\nabla g(\vec x^{(0)})\\)</span>, the gradient of <span class="math-inline">\\(g\\)</span> at <span class="math-inline">\\(\vec x^{(0)}\\)</span>. Show your work, and write your final answer in the box provided. Your answer should be a vector with no variables.

<div class="math-display">
$$
\nabla g(\vec x^{(0)}) = \boxed{\textbf{}}
$$
</div>

<details markdown="1"><summary>Solution</summary>

Let <span class="math-inline">\\(\vec d = \nabla g(\vec x^{(0)})\\)</span>. The gradient descent update rule is

<div class="math-display">
$$
\vec x^{(1)} = \vec x^{(0)} - \alpha \nabla g(\vec x^{(0)})
$$
</div>

 The two runs give

<div class="math-display">
$$
\begin{bmatrix}
1\\\\
1\\\\
1
\end{bmatrix}
=
\vec x^{(0)} - \frac{1}{2}\nabla g(\vec x^{(0)})
$$
</div>

 and

<div class="math-display">
$$
\begin{bmatrix}
2\\\\
3\\\\
2
\end{bmatrix}
=
\vec x^{(0)} - \frac{1}{4}\nabla g(\vec x^{(0)})
$$
</div>

 Subtracting the second equation from the first eliminates <span class="math-inline">\\(\vec x^{(0)}\\)</span>:

<div class="math-display">
$$
\begin{bmatrix}
-1\\\\
-2\\\\
-1
\end{bmatrix}
=
-\frac{1}{4}\nabla g(\vec x^{(0)})
$$
</div>

 So

<div class="math-display">
$$
\nabla g(\vec x^{(0)}) =
\boxed{
\begin{bmatrix}
4\\\\
8\\\\
4
\end{bmatrix}}
$$
</div>

</details>

Now let <span class="math-inline">\\(\vec x = \begin{bmatrix} x&#95;1 \\\\ x&#95;2 \end{bmatrix}\\)</span>, and consider the function <span class="math-inline">\\(f: \mathbb{R}^2 \to \mathbb{R}\\)</span> defined by

<div class="math-display">
$$
f(\vec x) = (x_1 + 2x_2 - 6)^2 + \lVert \vec x \rVert^2
$$
</div>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> Suppose

<div class="math-display">
$$
\nabla f(\vec x)
=
M
\begin{bmatrix}
x_1\\\\
x_2\\\\
1
\end{bmatrix}
$$
</div>

for some <span class="math-inline">\\(2 \times 3\\)</span> matrix <span class="math-inline">\\(M\\)</span>. Which of the following matrices is <span class="math-inline">\\(M\\)</span>?

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} 2 &amp; 2 &amp; -6 \\\\ 2 &amp; 5 &amp; -12 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} 4 &amp; 2 &amp; -12 \\\\ 2 &amp; 10 &amp; -24 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} 4 &amp; 4 &amp; -12 \\\\ 4 &amp; 10 &amp; -24 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} 4 &amp; 4 &amp; 12 \\\\ 4 &amp; 10 &amp; 24 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} 4 &amp; 4 &amp; -12 \\\\ 2 &amp; 6 &amp; -12 \end{bmatrix}\\)</span></span></div>

<details markdown="1"><summary>Solution</summary>

<span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} 4 &amp; 4 &amp; -12 \\\\ 2 &amp; 6 &amp; -12 \end{bmatrix}\\)</span>

We have

<div class="math-display">
$$
f(\vec x) = (x_1 + 2x_2 - 6)^2 + \lVert \vec x \rVert^2
$$
</div>

Using the chain rule,

<div class="math-display">
$$
\nabla f(\vec x)
=
2(x_1+2x_2-6)
\begin{bmatrix}
1\\\\
2
\end{bmatrix}
+
2\vec x
$$
</div>

We applied the chain rule above by writing <span class="math-inline">\\(\left( x&#95;1 + 2x&#95;2 - 6 \right)^2 = (\begin{bmatrix} 1 \\\\ 2 \end{bmatrix} \cdot \vec x - 6)^2\\)</span>. If this feels foreign, we can instead take partial derivatives with respect to <span class="math-inline">\\(x&#95;1\\)</span> and <span class="math-inline">\\(x&#95;2\\)</span> separately.

<div class="math-display">
$$
\frac{\partial f}{\partial x_1} = 2(x_1 + 2x_2 - 6) \cdot 1 + 2x_1 = 4x_1 + 4x_2 - 12
$$
</div>



<div class="math-display">
$$
\frac{\partial f}{\partial x_2} = 2(x_1 + 2x_2 - 6) \cdot 2 + 2x_2 = 4x_1 + 10x_2 - 24
$$
</div>

Either way, <span class="math-inline">\\(\nabla f(\vec x)\\)</span> simplifies to

<div class="math-display">
$$
\nabla f(\vec x)
=
\begin{bmatrix}
2(x_1+2x_2-6)+2x_1\\\\
4(x_1+2x_2-6)+2x_2
\end{bmatrix}
=
\begin{bmatrix}
4x_1+4x_2-12\\\\
4x_1+10x_2-24
\end{bmatrix}
=
\begin{bmatrix}
4 & 4 & -12\\\\
4 & 10 & -24
\end{bmatrix}
\begin{bmatrix}
x_1 \\\\ x_2 \\\\ 1
\end{bmatrix}
$$
</div>

 So,

<div class="math-display">
$$
M =
\boxed{
\begin{bmatrix}
4 & 4 & -12\\\\
4 & 10 & -24
\end{bmatrix}}
$$
</div>

</details>

</div>
</div>

</div>

---

## Problem 9 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>

Consider the matrix <span class="math-inline">\\(A = \begin{bmatrix} 2 &amp; 3 \\\\ -4 &amp; k \end{bmatrix}\\)</span> where <span class="math-inline">\\(k \in \mathbb{R}\\)</span> is some unknown constant.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> Suppose <span class="math-inline">\\(\lambda&#95;1 = 0\\)</span> is an eigenvalue of <span class="math-inline">\\(A\\)</span>. Find the value of <span class="math-inline">\\(k\\)</span>. Give your answer as a number with no variables.

<span class="math-inline">\\(k = \boxed{\textbf{-6}}\\)</span>

<details markdown="1"><summary>Solution</summary>

If <span class="math-inline">\\(0\\)</span> is an eigenvalue, then <span class="math-inline">\\(\det(A)=0\\)</span>. So

<div class="math-display">
$$
\det(A)=2k-3(-4)=2k+12=0
$$
</div>

 This gives

<div class="math-display">
$$
k=\boxed{-6}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Suppose <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ 1 \end{bmatrix}\\)</span> is an eigenvector of <span class="math-inline">\\(A\\)</span>. Find the value of <span class="math-inline">\\(k\\)</span>. Give your answer as a number with no variables.

<div class="math-display">
$$
k = \boxed{\textbf{9}}
$$
</div>

<details markdown="1"><summary>Solution</summary>

If <span class="math-inline">\\(\begin{bmatrix}1\\\\1\end{bmatrix}\\)</span> is an eigenvector, then

<div class="math-display">
$$
A\begin{bmatrix}1\\\\1\end{bmatrix}
=
\begin{bmatrix}5\\\\k-4\end{bmatrix}
$$
</div>

 must be a scalar multiple of <span class="math-inline">\\(\begin{bmatrix}1\\\\1\end{bmatrix}\\)</span>. Therefore,

<div class="math-display">
$$
k-4=5
$$
</div>

 so

<div class="math-display">
$$
k=\boxed{9}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">5 pts</span> Suppose <span class="math-inline">\\(\lambda&#95;1 = 3\\)</span> is an eigenvalue of <span class="math-inline">\\(A\\)</span>. Find <span class="math-inline">\\(\lambda&#95;2\\)</span>, the **other eigenvalue** of <span class="math-inline">\\(A\\)</span>. Show your work, and write your final answer in the box provided. Give your answer as a number with no variables.

<div class="math-display">
$$
\lambda_2 = \boxed{\textbf{14}}
$$
</div>

<details markdown="1"><summary>Solution</summary>

If <span class="math-inline">\\(3\\)</span> is an eigenvalue, then

<div class="math-display">
$$
\det(A-3I)=0
$$
</div>

 So

<div class="math-display">
$$
\det\left(
\begin{bmatrix}
-1 & 3\\\\
-4 & k-3
\end{bmatrix}
\right)
=
-(k-3)+12
=
15-k
=0
$$
</div>

 This gives <span class="math-inline">\\(k=15\\)</span>. The trace of <span class="math-inline">\\(A\\)</span> is then <span class="math-inline">\\(2+15=17\\)</span>, so the two eigenvalues sum to <span class="math-inline">\\(17\\)</span>. Thus,

<div class="math-display">
$$
\lambda_2 = 17-3 = \boxed{14}
$$
</div>

</details>

</div>
</div>

</div>

---

## Problem 10 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">14 pts</span>

The state diagram below describes a Markov chain with four states.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Find the adjacency matrix <span class="math-inline">\\(A\\)</span> for this Markov chain.

<span class="math-inline">\\(A =\\)</span>

<details markdown="1"><summary>Solution</summary>

Column <span class="math-inline">\\(j\\)</span> contains the probabilities of transitioning from state <span class="math-inline">\\(j\\)</span> to all other states; columns must sum to <span class="math-inline">\\(1\\)</span>. Reading from the diagram, the first two columns come from the left "connected component" (made up of states <span class="math-inline">\\(1\\)</span> and <span class="math-inline">\\(2\\)</span>), and the last two columns come from the right connected component. So

<div class="math-display">
$$
\boxed{
A =
\begin{bmatrix}
1/4 & 1/2 & 0 & 0\\\\
3/4 & 1/2 & 0 & 0\\\\
0 & 0 & 2/3 & 1/5\\\\
0 & 0 & 1/3 & 4/5
\end{bmatrix}}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Suppose the chain starts in **state <span class="math-inline">\\(\mathbf{1}\\)</span>**. Fill each box with the **long-run fraction** of time spent in each state. Your answers should be numbers with no variables, and should sum to <span class="math-inline">\\(1\\)</span>.

State 1: State 2: State 3: State 4:

<details markdown="1"><summary>Solution</summary>

As we know from [Chapter 9.3](https://notes.eecs245.org/eigenvalues-and-eigenvectors/markov-chains-adjacency-matrices/), the long-run fraction of time spent in each state is described by the eigenvector of the adjacency matrix corresponding to eigenvalue <span class="math-inline">\\(1\\)</span> (and whose components sum to <span class="math-inline">\\(1\\)</span>).

What is tricky about this particular adjacency matrix is that it has **two linearly independent eigenvectors, both for the eigenvalue <span class="math-inline">\\(1\\)</span>.** Why? Note that the Markov chain has two isolated islands, and its impossible to transition between them. So if we ever start in states <span class="math-inline">\\(1\\)</span> or <span class="math-inline">\\(2\\)</span>, in the long run, we will only spend time in states <span class="math-inline">\\(1\\)</span> and <span class="math-inline">\\(2\\)</span>. Similarly, if we start in states <span class="math-inline">\\(3\\)</span> or <span class="math-inline">\\(4\\)</span>, in the long run, we will only spend time in states <span class="math-inline">\\(3\\)</span> and <span class="math-inline">\\(4\\)</span>.

This means that we can simplify the problem by just looking at the <span class="math-inline">\\(2 \times 2\\)</span> matrix in the top right of <span class="math-inline">\\(A\\)</span> corresponding to the left island (states <span class="math-inline">\\(1\\)</span> and <span class="math-inline">\\(2\\)</span>). This matrix is

<div class="math-display">
$$
A_{\text{left}} = \begin{bmatrix}
1/4 & 1/2 \\\\
3/4 & 1/2
\end{bmatrix}
$$
</div>

All we need to do now is find the eigenvector of <span class="math-inline">\\(A&#95;{\text{left}}\\)</span> corresponding to eigenvalue <span class="math-inline">\\(1\\)</span>. If such an eigenvector is of the form <span class="math-inline">\\(\begin{bmatrix} a \\\\ b \end{bmatrix}\\)</span>, then

<div class="math-display">
$$
\begin{bmatrix} 1/4 & 1/2 \\\\ 3/4 & 1/2 \end{bmatrix} \begin{bmatrix} a \\\\ b \end{bmatrix} = 1 \begin{bmatrix} a \\\\ b \end{bmatrix}
$$
</div>

The first row gives us

<div class="math-display">
$$
\frac{1}{4}a + \frac{1}{2} b = a \implies \frac{1}{2} b = \frac{3}{4}a \implies b = \frac{3}{2}a
$$
</div>

So, if <span class="math-inline">\\(a = 2\\)</span>, then <span class="math-inline">\\(b = 3\\)</span>. But, the steady-state distribution must have components that sum to <span class="math-inline">\\(1\\)</span>, so as probabilities, we're looking at <span class="math-inline">\\(2/5\\)</span> and <span class="math-inline">\\(3/5\\)</span>.

Not only is <span class="math-inline">\\(\begin{bmatrix} 2/5 \\\\ 3/5 \end{bmatrix}\\)</span> an eigenvector of <span class="math-inline">\\(A&#95;{\text{left}}\\)</span> corresponding to eigenvalue <span class="math-inline">\\(1\\)</span>, but

<div class="math-display">
$$
\begin{bmatrix} 2/5 \\\\ 3/5 \\\\ 0 \\\\ 0 \end{bmatrix}
$$
</div>

is an eigenvector of the full matrix <span class="math-inline">\\(A\\)</span> corresponding to eigenvalue <span class="math-inline">\\(1\\)</span>! The 0's in the latter two components effectively "ignore" states <span class="math-inline">\\(3\\)</span> and <span class="math-inline">\\(4\\)</span>, representing the assumption that we start in state <span class="math-inline">\\(1\\)</span>.

So, if we start in state <span class="math-inline">\\(1\\)</span>,

<div class="math-display">
$$
\boxed{\text{State 1: } \frac{2}{5},\quad \text{State 2: } \frac{3}{5},\quad \text{State 3: } 0,\quad \text{State 4: } 0}
$$
</div>

In case you're curious, the other linearly independent eigenvector of <span class="math-inline">\\(A\\)</span> corresponding to eigenvalue <span class="math-inline">\\(1\\)</span> is

<div class="math-display">
$$
\begin{bmatrix} 0 \\\\ 0 \\\\ 3/8 \\\\ 5/8 \end{bmatrix}
$$
</div>

There's a section in [Chapter 9.4](https://notes.eecs245.org/eigenvalues-and-eigenvectors/multiplicities-diagonalization/#example-another-diagonalizable-matrix) about block diagonal matrices that is relevant here.
</details>

Now, consider a **modified** version of the Markov chain. Changes have been emphasized in **bold**.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Consider the statement: "'If we start in \_\_\_\_, the long-run fraction of time spent in each state is the same as in the original chain.''

Which of the following could be placed in the blank to make the statement true? **Select all** that apply.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> state 1</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> state 2</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> state 3</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> state 4</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> none of these are valid</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> state 1</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> state 2</span><span class="mc-option"><span class="mc-square mc-correct" aria-hidden="true"></span> state 3</span><span class="mc-option"><span class="mc-square mc-correct" aria-hidden="true"></span> state 4</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> none of these are valid</span></div>

In the modified chain, starting in state <span class="math-inline">\\(1\\)</span> or state <span class="math-inline">\\(2\\)</span> eventually leads to the right connected component, because there is now a positive-probability path from state <span class="math-inline">\\(2\\)</span> to state <span class="math-inline">\\(3\\)</span>. This changes the long-run fractions compared to the original chain. The long-run fraction of time spent in states <span class="math-inline">\\(1\\)</span> and <span class="math-inline">\\(2\\)</span> now will be <span class="math-inline">\\(0\\)</span>.

Starting in state <span class="math-inline">\\(3\\)</span> or state <span class="math-inline">\\(4\\)</span>, the chain stays in the right connected component, and that component has not changed. There is no way to go from state <span class="math-inline">\\(3\\)</span> to <span class="math-inline">\\(2\\)</span> or <span class="math-inline">\\(1\\)</span>. So, the long-run fractions are the same as in the original chain; <span class="math-inline">\\(3/8\\)</span> for state <span class="math-inline">\\(3\\)</span> and <span class="math-inline">\\(5/8\\)</span> for state <span class="math-inline">\\(4\\)</span>, and <span class="math-inline">\\(0\\)</span> for states <span class="math-inline">\\(1\\)</span> and <span class="math-inline">\\(2\\)</span>.

The correct choices are

<div class="math-display">
$$
\boxed{\text{state 3 and state 4}}
$$
</div>

</details>

</div>
</div>

</div>

---

## Problem 11 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">10 pts</span>

Let <span class="math-inline">\\(S\\)</span> be a <span class="math-inline">\\(3 \times 3\\)</span> **symmetric** matrix with eigenvectors <span class="math-inline">\\(\vec v&#95;1\\)</span>, <span class="math-inline">\\(\vec v&#95;2\\)</span>, and <span class="math-inline">\\(\vec v&#95;3\\)</span> corresponding to eigenvalues <span class="math-inline">\\(5\\)</span>, <span class="math-inline">\\(2\\)</span>, and <span class="math-inline">\\(-1\\)</span>, respectively. Assume that each <span class="math-inline">\\(\vec v&#95;i\\)</span> is a unit vector.

Suppose <span class="math-inline">\\(\vec x \in \mathbb{R}^3\\)</span> and that

<div class="math-display">
$$
\vec x = 3\vec v_1 - 4\vec v_2 + \vec v_3
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Write <span class="math-inline">\\(S^2 \vec x\\)</span> as a linear combination of <span class="math-inline">\\(\vec v&#95;1\\)</span>, <span class="math-inline">\\(\vec v&#95;2\\)</span>, and <span class="math-inline">\\(\vec v&#95;3\\)</span>. Fill in each box with a number with no variables.

<span class="math-inline">\\(S^2 \vec x = \boxed{\textbf{75}}  \vec v&#95;1 + \boxed{\textbf{-16}}  \vec v&#95;2 + \boxed{\textbf{1}}  \vec v&#95;3\\)</span>

<details markdown="1"><summary>Solution</summary>

Applying <span class="math-inline">\\(S^2\\)</span> multiplies each eigenvector by the square of its eigenvalue, so

<div class="math-display">
$$
S^2\vec x
=
3(5^2)\vec v_1 - 4(2^2)\vec v_2 + ((-1)^2)\vec v_3
=
\boxed{75\vec v_1 - 16\vec v_2 + \vec v_3}
$$
</div>

 This result doesn't rely on the fact that <span class="math-inline">\\(\vec v&#95;1\\)</span>, <span class="math-inline">\\(\vec v&#95;2\\)</span>, and <span class="math-inline">\\(\vec v&#95;3\\)</span> are unit vectors or orthogonal; we'll use these assumptions in the next part.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> What is the value of <span class="math-inline">\\(\lVert S\vec x \rVert^2\\)</span>?

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(24\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(26\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(218\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(290\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(5882\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Not enough information</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(24\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(26\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(218\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(290\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(5882\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Not enough information</span></div>

Applying <span class="math-inline">\\(S\\)</span> once gives

<div class="math-display">
$$
S\vec x = 15\vec v_1 - 8\vec v_2 - \vec v_3
$$
</div>

 Since <span class="math-inline">\\(S\\)</span> is symmetric, eigenvectors corresponding to distinct eigenvalues are orthogonal. The vectors <span class="math-inline">\\(\vec v&#95;1\\)</span>, <span class="math-inline">\\(\vec v&#95;2\\)</span>, and <span class="math-inline">\\(\vec v&#95;3\\)</span> are also unit vectors, so

<div class="math-display">
$$
\begin{align*}
\lVert S\vec x \rVert^2 &= \lVert 15\vec v_1 - 8\vec v_2 - \vec v_3 \rVert^2 \\\\
&= (15 \vec v_1 - 8\vec v_2 - \vec v_3) \cdot (15\vec v_1 - 8\vec v_2 - \vec v_3) \\\\
&= 15^2 \underbrace{(\vec v_1 \cdot \vec v_1)}_{1} - 8 \cdot 15 \underbrace{(\vec v_1 \cdot \vec v_2)}_{0} - 15 (\vec v_1 \cdot \vec v_3) \\\\
& \quad - 8 \cdot 15 (\vec v_2 \cdot \vec v_1) + 8^2 (\vec v_2 \cdot \vec v_2) + 8 (\vec v_2 \cdot \vec v_3) \\\\
& \quad - (\vec v_3 \cdot \vec v_1) - 8 (\vec v_3 \cdot \vec v_2) + (-1)^2(\vec v_3 \cdot \vec v_3) \\\\
&= 15^2 + 8^2 + 1^2 \\\\
&= 290
\end{align*}
$$
</div>

Yet another way to look at this is to see that <span class="math-inline">\\(S = Q \Lambda Q^T\\)</span>, where the columns of <span class="math-inline">\\(Q\\)</span> are the vectors <span class="math-inline">\\(\vec v&#95;i\\)</span> and the diagonal entries of <span class="math-inline">\\(\Lambda\\)</span> are <span class="math-inline">\\(5\\)</span>, <span class="math-inline">\\(2\\)</span>, and <span class="math-inline">\\(-1\\)</span>. So,

<div class="math-display">
$$
\begin{align*}
\lVert S\vec x \rVert^2
&= \vec x^T S^T S \vec x \\\\
&= \vec x^T S^2 \vec x \\\\
&= \vec x^T (Q \Lambda Q^T)^2 \vec x \\\\
&= \vec x^T Q \Lambda^2 Q^T \vec x \\\\
&= \vec x^T Q
\begin{bmatrix}
25 & 0 & 0 \\\\
0 & 4 & 0 \\\\
0 & 0 & 1
\end{bmatrix}
Q^T \vec x \\\\
&= \begin{bmatrix} 3 & -4 & 1 \end{bmatrix}
\begin{bmatrix}
25 & 0 & 0 \\\\
0 & 4 & 0 \\\\
0 & 0 & 1
\end{bmatrix}
\begin{bmatrix} 3 \\\\ -4 \\\\ 1 \end{bmatrix} \\\\
&= \boxed{290}
\end{align*}
$$
</div>

In this solution, we used the fact that <span class="math-inline">\\(\vec x = 3 \vec v&#95;1 - 4 \vec v&#95;2 + \vec v&#95;3 = Q \begin{bmatrix} 3 \\\\ -4 \\\\ 1 \end{bmatrix}\\)</span>, and since <span class="math-inline">\\(Q^T Q = I\\)</span> (if <span class="math-inline">\\(Q\\)</span>'s columns are the orthonormal <span class="math-inline">\\(\vec v&#95;i\\)</span>'s), then <span class="math-inline">\\(Q^T \vec x = Q^TQ \begin{bmatrix} 3 \\\\ -4 \\\\ 1 \end{bmatrix} = \begin{bmatrix} 3 \\\\ -4 \\\\ 1 \end{bmatrix}\\)</span>.
</details>

</div>
</div>

</div>

---

## Problem 12 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>

Suppose <span class="math-inline">\\(\tilde X\\)</span> is an <span class="math-inline">\\(n \times 2\\)</span> matrix whose columns are mean-centered (i.e. have a mean of 0). Furthermore, suppose

<div class="math-display">
$$
\tilde X^T \tilde X = \begin{bmatrix} 3 & 2 \\\\ 2 & 6 \end{bmatrix}
$$
</div>

 Note that <span class="math-inline">\\(\tilde X^T \tilde X\\)</span> has eigenvalues of <span class="math-inline">\\(7\\)</span> and <span class="math-inline">\\(2\\)</span>. Let <span class="math-inline">\\(\tilde X = U \Sigma V^T\\)</span> be the singular value decomposition of <span class="math-inline">\\(\tilde X\\)</span>, and let <span class="math-inline">\\(\vec v&#95;1\\)</span> be the first column of <span class="math-inline">\\(V\\)</span> (not <span class="math-inline">\\(V^T\\)</span>).

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> What is <span class="math-inline">\\(\vec v&#95;1\\)</span>? Give your answer as a vector with no variables. If there are multiple correct answers, you only need to provide one.

<span class="math-inline">\\(\vec v&#95;1 = \boxed{\textbf{\frac{1}{\sqrt 5}\begin{bmatrix}1\\\\2\end{bmatrix}}}\\)</span>

<details markdown="1"><summary>Solution</summary>

The first right singular vector, <span class="math-inline">\\(\vec v&#95;1\\)</span>, is an eigenvector of <span class="math-inline">\\(\tilde X^T\tilde X\\)</span> corresponding to the largest eigenvalue, <span class="math-inline">\\(7\\)</span>. So we solve

<div class="math-display">
$$
\begin{bmatrix}
3 & 2\\\\
2 & 6
\end{bmatrix}
\begin{bmatrix}
a\\\\b
\end{bmatrix}
=
7
\begin{bmatrix}
a\\\\b
\end{bmatrix}
$$
</div>

 The first row gives

<div class="math-display">
$$
3a+2b=7a
\implies
b=2a
$$
</div>

 One unit vector in this direction is

<div class="math-display">
$$
\vec v_1 = \boxed{\frac{1}{\sqrt 5}\begin{bmatrix}1\\\\2\end{bmatrix}}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> Suppose the variance of the **second** principal component is <span class="math-inline">\\(1/15\\)</span>. What is <span class="math-inline">\\(n\\)</span>, the number of rows in <span class="math-inline">\\(\tilde X\\)</span>? Give your answer as a number with no variables.

<span class="math-inline">\\(n = \boxed{\textbf{30}}\\)</span>

<details markdown="1"><summary>Solution</summary>

The variance of the second principal component is

<div class="math-display">
$$
\frac{\sigma_2^2}{n}
$$
</div>

 Since <span class="math-inline">\\(\sigma&#95;2^2\\)</span> is the second-largest eigenvalue of <span class="math-inline">\\(\tilde X^T\tilde X\\)</span>, we have <span class="math-inline">\\(\sigma&#95;2^2=2\\)</span>. So

<div class="math-display">
$$
\frac{2}{n}=\frac{1}{15}
$$
</div>

 This gives

<div class="math-display">
$$
n=\boxed{30}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">5 pts</span> Suppose that <span class="math-inline">\\(\vec u&#95;2\\)</span> is the second column of <span class="math-inline">\\(U\\)</span>, corresponding to the singular value <span class="math-inline">\\(\sigma&#95;2\\)</span>, in the singular value decomposition of <span class="math-inline">\\(\tilde X\\)</span>.

Prove that <span class="math-inline">\\(\tilde X \vec v&#95;1\\)</span> and <span class="math-inline">\\(\sigma&#95;2 \vec u&#95;2\\)</span> are orthogonal. You do not need to re-prove any facts about the singular value decomposition, but you should state any facts you use.

<details markdown="1"><summary>Solution</summary>

Using the SVD relationship,

<div class="math-display">
$$
\tilde X\vec v_1 = \sigma_1\vec u_1
$$
</div>

 So

<div class="math-display">
$$
(\tilde X\vec v_1)^T(\sigma_2\vec u_2)
=
(\sigma_1\vec u_1)^T(\sigma_2\vec u_2)
=
\sigma_1\sigma_2 \vec u_1^T\vec u_2
$$
</div>

 The columns of <span class="math-inline">\\(U\\)</span> are orthonormal, so <span class="math-inline">\\(\vec u&#95;1^T\vec u&#95;2=0\\)</span>. Therefore,

<div class="math-display">
$$
(\tilde X\vec v_1)^T(\sigma_2\vec u_2)=0
$$
</div>

 This proves that <span class="math-inline">\\(\tilde X\vec v&#95;1\\)</span> and <span class="math-inline">\\(\sigma&#95;2\vec u&#95;2\\)</span> are orthogonal.
</details>

</div>
</div>

</div>

---

## Problem 13 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span>

What is one topic you studied a lot for that wasn't on the Final Exam? **Blank answers will receive no credit!**

<details markdown="1"><summary>Solution</summary>

One topic that didn't appear was convexity --- there was originally going to be a question about convexity but we cut it to prevent the exam from being too long.
</details>

Congrats on completing the Final Exam for EECS 245! We'll really miss you; please stay in touch.

Feel free to draw us a picture about EECS 245 in the box below.

Did you notice any violations of the Honor Code during the exam? If so, share details with us here. We will keep your identity anonymous when investigating any cases.

{% endraw %}
