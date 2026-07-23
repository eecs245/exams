---
layout: minimal
title: "Fall 2025 Final Exam"
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

# Fall 2025 Final Exam

**administered**

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/exams/fa25-final.pdf" target="_blank">View as PDF ✏️</a>
<a class="btn btn-info assignment-pdf-button" href="/resources/exams/fa25-final-solutions.pdf" target="_blank">Solutions PDF ✅</a>
</div>

{: .yellow }
<div markdown="1">
**Instructions**

-   This exam consists of 13 problems, worth a total of 130 points, spread across 14 pages (7 sheets of paper). **All problems count towards your Final Exam score; certain problems also count towards your Midterm 1 or Midterm 2 redemption scores.**

-   You have 120 minutes to complete this exam, unless you have extended-time accommodations through SSD.

-   Write your uniqname in the top right corner of every page in the space provided.

-   For free response problems, you must show all of your work (unless otherwise specified), and <span class="math-inline">\\(\boxed{\text{circle}}\\)</span> your final answer. We will not grade work that appears elsewhere, and you may lose points if your work is not shown.

-   For multiple choice problems, completely fill in bubbles and square boxes; if we cannot tell which option(s) you selected, you may lose points.



-   You may refer to **3** two-sided handwritten notes sheet. Other than that, you may not refer to any other resources or technology during the exam (no phones, watches, or calculators).
</div>

---

## Problems

- [Problem 1: (10 pts) $\boxed{\text{Counts towards Midterm 1 redemption score}}$](#problem-1-10-pts-boxedtextcounts-towards-midterm-1-redemption-score)
- [Problem 2: (10 pts) $\boxed{\text{Counts towards Midterm 1 redemption score}}$](#problem-2-10-pts-boxedtextcounts-towards-midterm-1-redemption-score)
- [Problem 3: (16 pts) $\boxed{\text{Counts towards Midterm 1 redemption score}}$](#problem-3-16-pts-boxedtextcounts-towards-midterm-1-redemption-score)
- [Problem 4: (8 pts) $\boxed{\text{Counts towards Midterm 2 redemption score}}$](#problem-4-8-pts-boxedtextcounts-towards-midterm-2-redemption-score)
- [Problem 5: (12 pts) $\boxed{\text{Counts towards Midterm 2 redemption score}}$](#problem-5-12-pts-boxedtextcounts-towards-midterm-2-redemption-score)
- [Problem 6: (4 pts) $\boxed{\text{Counts towards Midterm 2 redemption score}}$](#problem-6-4-pts-boxedtextcounts-towards-midterm-2-redemption-score)
- [Problem 7: (6 pts) $\boxed{\text{Counts towards Midterm 2 redemption score}}$](#problem-7-6-pts-boxedtextcounts-towards-midterm-2-redemption-score)
- [Problem 8: (6 pts) $\boxed{\text{Counts towards Midterm 2 redemption score}}$](#problem-8-6-pts-boxedtextcounts-towards-midterm-2-redemption-score)
- [Problem 9](#problem-9-18-pts)
- [Problem 10](#problem-10-12-pts)
- [Problem 11](#problem-11-12-pts)
- [Problem 12](#problem-12-12-pts)
- [Problem 13](#problem-13-4-pts)

---

## Problem 1: (10 pts) <span class="math-inline">\\(\boxed{\text{Counts towards Midterm 1 redemption score}}\\)</span>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Suppose we'd like to find the optimal constant prediction, <span class="math-inline">\\(w^{\ast}\\)</span>, for the constant model <span class="math-inline">\\(h(x&#95;i) = w\\)</span>, given a dataset of <span class="math-inline">\\(n\\)</span> values <span class="math-inline">\\(y&#95;1, y&#95;2, \ldots, y&#95;n\\)</span>. To do so, we minimize mean Bursley error, defined as

<div class="math-display">
$$
R_{\text{B}}(w) = \frac{1}{n} \sum_{i=1}^n | 2y_i - w |^2
$$
</div>

Suppose the mean of <span class="math-inline">\\(y&#95;1, y&#95;2, \ldots, y&#95;n\\)</span> is 20 and the median of <span class="math-inline">\\(y&#95;1, y&#95;2, \ldots, y&#95;n\\)</span> is 30.

Which value of <span class="math-inline">\\(w^{\ast}\\)</span> minimizes <span class="math-inline">\\(R&#95;{\text{B}}(w)\\)</span> for this dataset? Select one of the answers below, then justify your answer in the box provided.

Hint: Look very closely at the definition of <span class="math-inline">\\(R&#95;{\text{B}}(w)\\)</span>. You do not need to re-prove any results from class; you can fully find and explain your answer without using calculus.

1.  Answer:
<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(10\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(15\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(20\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(30\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(40\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(60\\)</span></span></div>

2.  Justify your answer in the box below.

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(10\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(15\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(20\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(30\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(40\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(60\\)</span></span></div>

First, notice that the use of absolute values is a distraction: since <span class="math-inline">\\(|x|^2 = x^2\\)</span>, we can rewrite <span class="math-inline">\\(R&#95;{\text{B}}(w)\\)</span> as

<div class="math-display">
$$
R_{\text{B}}(w) = \frac{1}{n} \sum_{i=1}^n (2y_i - w)^2
$$
</div>

While it's possible to solve this problem by taking the derivative of <span class="math-inline">\\(R&#95;{\text{B}}(w)\\)</span> with respect to <span class="math-inline">\\(w\\)</span> and setting it equal to 0, it's quicker to leverage what we already know. We know that if there wasn't a coefficient of <span class="math-inline">\\(2\\)</span> in front of <span class="math-inline">\\(y&#95;i\\)</span>, the minimizer would be the mean of the dataset.

One way to reason about the effect of the coefficient of <span class="math-inline">\\(2\\)</span> is to consider a substitution. Let <span class="math-inline">\\(z&#95;i = 2y&#95;i\\)</span>. Then, <span class="math-inline">\\(R&#95;{\text{B}}(w)\\)</span> becomes

<div class="math-display">
$$
R_{\text{B}}(w) = \frac{1}{n} \sum_{i=1}^n (z_i - w)^2
$$
</div>

 which is the same as the mean squared error of the dataset <span class="math-inline">\\(z&#95;1, z&#95;2, \ldots, z&#95;n\\)</span>, and so <span class="math-inline">\\(w^{\ast} = \bar{z}\\)</span>. But <span class="math-inline">\\(\bar{z} = 2 \bar{y}\\)</span>, and so

<div class="math-display">
$$
w^* = 2 \bar{y} = 2 \cdot 20 = \boxed{40}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> This part does not use any of the numbers from part **a)**.

Recall that the mean absolute error, <span class="math-inline">\\(R&#95;{\text{abs}}(w)\\)</span>, of a constant prediction <span class="math-inline">\\(w\\)</span> on a dataset of <span class="math-inline">\\(n\\)</span> values <span class="math-inline">\\(y&#95;1, y&#95;2, \ldots, y&#95;n\\)</span> is given by

<div class="math-display">
$$
R_{\text{abs}}(w) = \frac{1}{n} \sum_{i=1}^n |y_i - w|
$$
</div>

Consider the dataset of 4 values, <span class="math-inline">\\(1, 3, 5, 9\\)</span>. Among all integers **not in this dataset**, which **integer** minimizes <span class="math-inline">\\(R&#95;{\text{abs}}(w)\\)</span> for this dataset?

<span class="math-inline">\\(\text{minimizer} = \minibox{3cm}{4}[1cm]\\)</span>

<details markdown="1"><summary>Solution</summary>

The minimizer of mean absolute error is the median of the dataset. When the number of data points is even, any value between the middle two values, inclusive, minimizes mean absolute error. Here, any value between 3 and 5 inclusive minimizes mean absolute error; the value <span class="math-inline">\\(\boxed{4}\\)</span> is the only integer in this range that isn't in the dataset itself, so it is the minimizer we're looking for.
</details>

</div>
</div>

</div>

---

## Problem 2: (10 pts) <span class="math-inline">\\(\boxed{\text{Counts towards Midterm 1 redemption score}}\\)</span>

Let <span class="math-inline">\\(k\\)</span> be a positive integer and let <span class="math-inline">\\(\alpha\\)</span> be a positive real number. Consider the dataset of <span class="math-inline">\\(n = 2k+1\\)</span> points, <span class="math-inline">\\(\underbrace{(-k, -\alpha), (-k+1, 0), (-k+2, 0), \ldots, (-1, 0)}&#95;{k \text{ points}}, (0, 0), \underbrace{(1, 0), \ldots, (k-2, 0), (k-1, 0), (k, \alpha)}&#95;{k \text{ points}}\\)</span>.

Note that the <span class="math-inline">\\(x\\)</span>-values are equally spaced, starting from <span class="math-inline">\\(-k\\)</span> and ending at <span class="math-inline">\\(k\\)</span>. The <span class="math-inline">\\(y\\)</span>-values are all 0, except for the first and last points, which have <span class="math-inline">\\(y\\)</span>-value <span class="math-inline">\\(-\alpha\\)</span> and <span class="math-inline">\\(\alpha\\)</span>, respectively. For example, if <span class="math-inline">\\(k = 4\\)</span> and <span class="math-inline">\\(\alpha = 2\\)</span>, the dataset looks like

<div style="text-align: center;">
<img src="imgs/outliers.png" alt="image" style="width: 50%; max-width: 100%;">
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Find <span class="math-inline">\\(\bar{x}\\)</span> and <span class="math-inline">\\(\bar{y}\\)</span>, the means of the <span class="math-inline">\\(x\\)</span>- and <span class="math-inline">\\(y\\)</span>-values, respectively. Give your answers as expressions involving <span class="math-inline">\\(k\\)</span>, <span class="math-inline">\\(\alpha\\)</span>, and/or other constants.

<span class="math-inline">\\(\bar{x} = \minibox{3cm}{0}[1cm], \qquad \bar{y} = \minibox{3cm}{0}[1cm]\\)</span>

<details markdown="1"><summary>Solution</summary>

Both sets of values average to 0: <span class="math-inline">\\(\bar{x} = 0\\)</span> and <span class="math-inline">\\(\bar{y} = 0\\)</span>.

-   The <span class="math-inline">\\(x\\)</span>-values are evenly spaced and centered around 0. If you were to add them up, the <span class="math-inline">\\(-k\\)</span> would cancel out with the <span class="math-inline">\\(k\\)</span>, the <span class="math-inline">\\(k-1\\)</span> would cancel out with the <span class="math-inline">\\(-k+1\\)</span>, and so on, making the sum 0, and hence the average 0.

-   The <span class="math-inline">\\(y\\)</span>-values are all 0, except for the first and last points, which have <span class="math-inline">\\(y\\)</span>-value <span class="math-inline">\\(-\alpha\\)</span> and <span class="math-inline">\\(\alpha\\)</span>, respectively. The average of the <span class="math-inline">\\(y\\)</span>-values is therefore <span class="math-inline">\\(\frac{-\alpha + \alpha}{2k+1} = 0\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Suppose we fit a simple linear regression model to the dataset by minimizing mean squared error. <span class="math-inline">\\(w&#95;1^{\ast}\\)</span>, the slope of the regression line, is of the form

<div class="math-display">
$$
w_1^* = \frac{A}{\sum_{i=1}^n (x_i - \bar{x})^2}
$$
</div>

What is the value of <span class="math-inline">\\(A\\)</span>? Select one of the answers below, then justify your answer in the box provided.

1.  Answer:
<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(0\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \alpha\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle 2 \alpha\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle 2 k \alpha\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle 2 k^2 \alpha\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \frac{2 \alpha}{k}\\)</span></span></div>

2.  Justify your answer in the box below.

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(0\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \alpha\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle 2 \alpha\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle 2 k \alpha\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle 2 k^2 \alpha\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \frac{2 \alpha}{k}\\)</span></span></div>

There are several equivalent formulas for the slope of the regression line, <span class="math-inline">\\(w&#95;1^{\ast}\\)</span>, and any of them would allow us to answer the question quickly. Let's start with

<div class="math-display">
$$
w_1^* = \frac{\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^n (x_i - \bar{x})^2}
$$
</div>

The denominator of this formula is the same as the one given to us, so let's focus on the numerator, which is <span class="math-inline">\\(v\\)</span> in the formula provided.

<div class="math-display">
$$
v = \sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})
$$
</div>

From the previous part, we know that <span class="math-inline">\\(\bar{x} = 0\\)</span> and <span class="math-inline">\\(\bar{y} = 0\\)</span>, so we can simplify the expression to

<div class="math-display">
$$
v = \sum_{i=1}^n (x_i - 0)(y_i - 0) = \sum_{i=1}^n x_i y_i
$$
</div>

But, we know that for all data points other than <span class="math-inline">\\(i=1\\)</span> (the point <span class="math-inline">\\((-k, -\alpha)\\)</span>) and <span class="math-inline">\\(i=n\\)</span> (the point <span class="math-inline">\\((k, \alpha)\\)</span>), <span class="math-inline">\\(x&#95;i = 0\\)</span>. Therefore,

<div class="math-display">
$$
v = \sum_{i = 1}^n x_iy_i = -k(-\alpha) + \underbrace{\sum_{i = 2}^{n-1} x_i (0)}_{0} + k(\alpha) = 2k\alpha
$$
</div>

Therefore, <span class="math-inline">\\(v = \boxed{2k\alpha}\\)</span>.
</details>

</div>
</div>

</div>

---

## Problem 3: (16 pts) <span class="math-inline">\\(\boxed{\text{Counts towards Midterm 1 redemption score}}\\)</span>

Consider the vectors <span class="math-inline">\\(\vec u = \begin{bmatrix} 3 \\\\ 3 \\\\ 6 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec v = \begin{bmatrix} 1 \\\\ 0 \\\\ c \end{bmatrix}\\)</span>, where <span class="math-inline">\\(c \in \mathbb{R}\\)</span> is some constant.

In parts **a)** and **b)**, if there are multiple possible values of <span class="math-inline">\\(c\\)</span>, give just one.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> Suppose <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> are orthogonal. Find <span class="math-inline">\\(c\\)</span>. Give your answer as a number with no variables.

$c = \minibox{3cm}{

<div class="math-display">

<div class="math-display">
$$
-1/2
$$
</div>

</div>

}$

<details markdown="1"><summary>Solution</summary>

Since <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> are orthogonal, their dot product is 0.

<div class="math-display">
$$
\begin{bmatrix} 3 \\\\ 3 \\\\ 6 \end{bmatrix} \cdot \begin{bmatrix} 1 \\\\ 0 \\\\ c \end{bmatrix} = 0
$$
</div>



<div class="math-display">
$$
3 + 0 + 6c = 0
$$
</div>



<div class="math-display">
$$
6c = -3
$$
</div>



<div class="math-display">
$$
c = -1/2
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> Suppose <span class="math-inline">\\(\lVert \vec v \rVert = 4\\)</span>. Find <span class="math-inline">\\(c\\)</span>. Give your answer as a number with no variables.

$c = \minibox{3cm}{

<div class="math-display">

<div class="math-display">
$$
\sqrt{15}
$$
</div>

</div>

}$

<details markdown="1"><summary>Solution</summary>

Since <span class="math-inline">\\(\lVert \vec v \rVert = 4\\)</span>, we have

<div class="math-display">
$$
\sqrt{1^2 + 0^2 + c^2} = 4
$$
</div>



<div class="math-display">
$$
1 + c^2 = 16
$$
</div>



<div class="math-display">
$$
c^2 = 15
$$
</div>



<div class="math-display">
$$
c = \sqrt{15}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Suppose the projection of <span class="math-inline">\\(\vec v\\)</span> onto <span class="math-inline">\\(\vec u\\)</span> is <span class="math-inline">\\(\begin{bmatrix} 1.5 \\\\ 1.5 \\\\ 3 \end{bmatrix}\\)</span>. What is the value of <span class="math-inline">\\(c\\)</span>? Select one of the answers below, then justify your answer in the box provided.

1.  Answer:
<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1/2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(3/2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(4\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(6\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(6 + \sqrt{41}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(27\\)</span></span></div>

2.  Justify your answer in the box below.

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1/2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(3/2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(2\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(4\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(6\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(6 + \sqrt{41}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(27\\)</span></span></div>

The projection of <span class="math-inline">\\(\vec v\\)</span> onto <span class="math-inline">\\(\vec u\\)</span> is given by

<div class="math-display">
$$
\vec p = \frac{\vec v \cdot \vec u}{\vec u \cdot \vec u} \vec u
$$
</div>

Since we're told that <span class="math-inline">\\(\vec p = \begin{bmatrix} 1.5 \\\\ 1.5 \\\\ 3 \end{bmatrix}\\)</span>, this means that <span class="math-inline">\\(p = \frac{1}{2} \begin{bmatrix} 3 \\\\ 3 \\\\ 6 \end{bmatrix} = \frac{1}{2} \vec u\\)</span>. So,

<div class="math-display">
$$
\frac{\vec v \cdot \vec u}{\vec u \cdot \vec u} = \frac{1}{2}
$$
</div>

Substituting in <span class="math-inline">\\(\vec v = \begin{bmatrix} 1 \\\\ 0 \\\\ c \end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec u = \begin{bmatrix} 3 \\\\ 3 \\\\ 6 \end{bmatrix}\\)</span> gives us

<div class="math-display">
$$
\frac{1 \cdot 3 + 0 \cdot 3 + c \cdot 6}{3^2 + 3^2 + 6^2} = \frac{1}{2} \implies \frac{3 + 6c}{54} = \frac{1}{2} \implies 3 + 6c = 27 \implies \boxed{c = 4}
$$
</div>

</details>

Recall from the previous page that <span class="math-inline">\\(\vec u = \begin{bmatrix} 3 \\\\ 3 \\\\ 6 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec v = \begin{bmatrix} 1 \\\\ 0 \\\\ c \end{bmatrix}\\)</span>, where <span class="math-inline">\\(c \in \mathbb{R}\\)</span> is some constant.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Suppose <span class="math-inline">\\(\text{span}(\lbrace\vec u, \vec v\rbrace)\\)</span> is the plane <span class="math-inline">\\(2x + 4y - 3z = 0\\)</span>. Find <span class="math-inline">\\(c\\)</span>. Show your work, and <span class="math-inline">\\(\boxed{\text{circle}}\\)</span> your final answer, which should be a number with no variables. <em>Hint: While you could compute the cross product, there is no need to --- there is a much quicker solution.</em>

<details markdown="1"><summary>Solution</summary>

One way to find the equation of the plane <span class="math-inline">\\(ax + by + cz = 0\\)</span> spanned by <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> in <span class="math-inline">\\(\mathbb{R}^3\\)</span> is to take the cross product of the two vectors, and setting <span class="math-inline">\\(a\\)</span> to the first component of the cross product, <span class="math-inline">\\(b\\)</span> to the second component, and <span class="math-inline">\\(c\\)</span> to the third component. We could compute the cross product in terms of <span class="math-inline">\\(c\\)</span>, and solve for where it is equal to <span class="math-inline">\\(\begin{bmatrix} 2 \\\\ 4 \\\\ -3 \end{bmatrix}\\)</span>.

But this is overly complicated, and there's an easier solution: if this plane is spanned by <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span>, then <span class="math-inline">\\(\vec v\\)</span> needs to satisfy the equation of the plane, which is <span class="math-inline">\\(2x + 4y - 3z = 0\\)</span>.

Substituting in <span class="math-inline">\\(\vec v = \begin{bmatrix} 1 \\\\ 0 \\\\ c \end{bmatrix}\\)</span> gives us

<div class="math-display">
$$
2 \cdot 1 + 4 \cdot 0 - 3 \cdot c = 0 \implies 2 - 3c = 0 \implies \boxed{c = 2/3}
$$
</div>

</details>

</div>
</div>

</div>

---

## Problem 4: (8 pts) <span class="math-inline">\\(\boxed{\text{Counts towards Midterm 2 redemption score}}\\)</span>

Let <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> be as in the previous problem.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Suppose that for some value of <span class="math-inline">\\(c\\)</span>, <span class="math-inline">\\(P\\)</span> is the matrix that projects vectors in <span class="math-inline">\\(\mathbb{R}^3\\)</span> onto <span class="math-inline">\\(\text{span}(\lbrace\vec u, \vec v\rbrace)\\)</span>. **Select all** true statements below.

<div class="mc-options"><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(P^2 = P\\)</span></span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(P\\)</span> is invertible</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(P\\)</span> is orthogonal</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(P\\)</span> is symmetric</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-square mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(P^2 = P\\)</span></span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(P\\)</span> is invertible</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(P\\)</span> is orthogonal</span><span class="mc-option"><span class="mc-square mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(P\\)</span> is symmetric</span></div>

If we let <span class="math-inline">\\(X = \begin{bmatrix} | &amp; | \\\\ \vec u &amp; \vec v \\\\ | &amp; | \end{bmatrix}\\)</span>, then no matter what <span class="math-inline">\\(c\\)</span> is, <span class="math-inline">\\(\text{rank}(X) = 2\\)</span>, meaning the <span class="math-inline">\\(2 \times 2\\)</span> matrix <span class="math-inline">\\(X^TX\\)</span> is invertible. Then,

<div class="math-display">
$$
P = X (X^TX)^{-1}X^T
$$
</div>

With this in mind:

-   <span class="math-inline">\\(P^2 = P\\)</span> is **true**. This is the defining property of a projection matrix: once a vector has been projected onto the plane, projecting it again does nothing.

-   Conceptually, <span class="math-inline">\\(P\\)</span> is **not** invertible, because multiple different vectors <span class="math-inline">\\(\vec y\\)</span> can be projected onto the same vector <span class="math-inline">\\(\vec p\\)</span>. The act of multiplying by <span class="math-inline">\\(P\\)</span> is not one-to-one, so <span class="math-inline">\\(P\\)</span> is not invertible.

-   <span class="math-inline">\\(P\\)</span> is **not** an orthogonal matrix. Orthogonal matrices preserve lengths, but projection usually shortens vectors unless they already lie in the plane. Also, orthogonal matrices are invertible, but <span class="math-inline">\\(P\\)</span> is not.

-   <span class="math-inline">\\(P\\)</span> is **symmetric**. This is a standard property of orthogonal projection matrices, and you can also verify it directly from <span class="math-inline">\\(P = X(X^TX)^{-1}X^T\\)</span> by taking the transpose.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Now, suppose <span class="math-inline">\\(\vec y \in \mathbb{R}^3\\)</span>. Let <span class="math-inline">\\(\vec p \\)</span> be the projection of <span class="math-inline">\\(\vec y\\)</span> onto <span class="math-inline">\\(\text{span}(\lbrace\vec u, \vec v\rbrace)\\)</span>, and let <span class="math-inline">\\(\vec e = \vec y - \vec p\\)</span>.

There is no value of <span class="math-inline">\\(c\\)</span> that guarantees that the components of <span class="math-inline">\\(\vec e\\)</span> sum to 0, for every <span class="math-inline">\\(\vec y \in \mathbb{R}^3\\)</span>. That is, it is **not** guaranteed that <span class="math-inline">\\(e&#95;1 + e&#95;2 + e&#95;3 = 0\\)</span> for every <span class="math-inline">\\(\vec y \in \mathbb{R}^3\\)</span>.

Give a 1-2 sentence English explanation for why it is **not** guaranteed that <span class="math-inline">\\(e&#95;1 + e&#95;2 + e&#95;3 = 0\\)</span> for every <span class="math-inline">\\(\vec y \in \mathbb{R}^3\\)</span>. <em>Hint: What <strong>would</strong> have to be true about <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> to make this guarantee for every <span class="math-inline">\\(\vec y\\)</span>?</em>

<details markdown="1"><summary>Solution</summary>

For <span class="math-inline">\\(e&#95;1 + e&#95;2 + e&#95;3\\)</span> to always equal 0, every error vector <span class="math-inline">\\(\vec e\\)</span> would have to be orthogonal to <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ 1 \\\\ 1 \end{bmatrix}\\)</span>. Since every error vector is orthogonal to <span class="math-inline">\\(\text{span}(\lbrace\vec u, \vec v\rbrace)\\)</span>, this would require <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ 1 \\\\ 1 \end{bmatrix}\\)</span> to lie in <span class="math-inline">\\(\text{span}(\lbrace\vec u, \vec v\rbrace)\\)</span>, but no value of <span class="math-inline">\\(c\\)</span> makes that happen.
</details>

</div>
</div>

</div>

---

## Problem 5: (12 pts) <span class="math-inline">\\(\boxed{\text{Counts towards Midterm 2 redemption score}}\\)</span>

Consider the <span class="math-inline">\\(n \times 5\\)</span> matrix <span class="math-inline">\\(A\\)</span>, along with a CR decomposition of it, given below.

<div class="math-display">
$$
A =
\begin{bmatrix}
2 & 2 & 2 & 2 & 2 \\\\
3 & 4 & 5 & 6 & 7 \\\\
4 & 6 & 8 & 10 & 12 \\\\
5 & 8 & 11 & 14 & 17 \\\\
6 & 10 & 14 & 18 & 22 \\\\
\vdots & \vdots & \vdots & \vdots & \vdots \\\\
n+1 & 2n & 3n - 1 & 4n - 2 & 5n - 3 \\\\
\end{bmatrix} = \underbrace{\begin{bmatrix} 2 & ? \\\\ 3 & ? \\\\ 4 & ? \\\\ 5 & ? \\\\ 6 & ? \\\\ \vdots & \vdots \\\\ n + 1 & ? \end{bmatrix}}_{C} \underbrace{\begin{bmatrix} 1 & \boxed{a} & 0 & c & -1 \\\\ 0 & \boxed{b} & 1 & d & 2\end{bmatrix}}_{R}
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">2 pts</span> Find <span class="math-inline">\\(\text{rank}(A)\\)</span>. Give your answer as an integer with no variables.

<span class="math-inline">\\(\text{rank}(A) = \minibox{3cm}{2}[1cm]\\)</span>

<details markdown="1"><summary>Solution</summary>

The CR decomposition writes <span class="math-inline">\\(A = CR\\)</span>, where <span class="math-inline">\\(C\\)</span> contains linearly independent columns of <span class="math-inline">\\(A\\)</span>. Since <span class="math-inline">\\(C\\)</span> has 2 columns, <span class="math-inline">\\(A\\)</span> has 2 linearly independent columns, so

<div class="math-display">
$$
\text{rank}(A) = \boxed{2}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Find <span class="math-inline">\\(a\\)</span> and <span class="math-inline">\\(b\\)</span>. Give your answers as numbers with no variables.

<span class="math-inline">\\(a = \minibox{3cm}{1/2}[1cm], \qquad b = \minibox{3cm}{1/2}[1cm]\\)</span>

<details markdown="1"><summary>Solution</summary>

Because columns 1 and 3 of <span class="math-inline">\\(R\\)</span> are the basis of <span class="math-inline">\\(\text{colsp}(A)\\)</span> that we're using to construct all 5 columns of <span class="math-inline">\\(A\\)</span>, column 2 of <span class="math-inline">\\(A\\)</span> must be

<div class="math-display">
$$
\text{col}_2(A) = a\,\text{col}_1(A) + b\,\text{col}_3(A)
$$
</div>

The "quick" way to spot what <span class="math-inline">\\(a\\)</span> and <span class="math-inline">\\(b\\)</span> must be is that column 2 is the average of columns 1 and 3: 2 is the average of 2 and 2, 4 is the average of 3 and 5, 6 is the average of 4 and 8, and so on. This alone tells you that <span class="math-inline">\\(a = b = \frac{1}{2}\\)</span>.

Another way to find <span class="math-inline">\\(a\\)</span> and <span class="math-inline">\\(b\\)</span> more systematically is to set up a system of equations. We have two unknowns --- <span class="math-inline">\\(a\\)</span> and <span class="math-inline">\\(b\\)</span> --- so we must need two equations, which we can get from looking at the first two rows of <span class="math-inline">\\(A\\)</span>.

<div class="math-display">
$$
\begin{align*}
2 &= 2a + 2b \\\\
4 &= 3a + 5b
\end{align*}
$$
</div>

The first equation says <span class="math-inline">\\(a+b=1\\)</span>, so <span class="math-inline">\\(a=1-b\\)</span>. Substitute into the second:

<div class="math-display">
$$
4 = 3(1-b) + 5b = 3 + 2b \implies b = \frac{1}{2}
$$
</div>

 Then <span class="math-inline">\\(a = \frac{1}{2}\\)</span> as well. Therefore,

<div class="math-display">
$$
\boxed{a = \frac{1}{2}, \qquad b = \frac{1}{2}}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> State **one** vector in <span class="math-inline">\\(\text{nullsp}(A)\\)</span>. Give your answer as a vector with no variables. <em>Hint: It is possible to find a vector in <span class="math-inline">\\(\text{nullsp}(A)\\)</span> without using your answer from part <strong>b)</strong>. Try not to rely heavily on your answer from part <strong>b)</strong> in case it's incorrect.</em>

<span class="math-inline">\\(\text{One vector in } \text{nullsp}(A) \text{ is:   } \minibox{3cm}{\\)</span>\begin{bmatrix} 1 \\ -2 \\ 1 \\ 0 \\ 0 \end{bmatrix}<span class="math-inline">\\(}[4cm]\\)</span>

<details markdown="1"><summary>Solution</summary>

To find a vector in <span class="math-inline">\\(\text{nullsp}(A)\\)</span>, we need to find a linear combination of <span class="math-inline">\\(A\\)</span>'s columns that equals <span class="math-inline">\\(\vec 0\\)</span>. One such linear combination can be found from rearranging the linear dependence relationship from the last part:

<div class="math-display">
$$
\begin{align*}
\text{col}_2(A) &= \frac{1}{2}\,\text{col}_1(A) + \frac{1}{2}\,\text{col}_3(A) \\\\
\vec 0 &= \frac{1}{2}\,\text{col}_1(A) - \text{col}_2(A) + \frac{1}{2}\,\text{col}_3(A)
\end{align*}
$$
</div>

The coefficients on columns 1 through 3 are <span class="math-inline">\\(\frac{1}{2}\\)</span>, <span class="math-inline">\\(-1\\)</span>, and <span class="math-inline">\\(\frac{1}{2}\\)</span>; this linear combination doesn't use columns 4 and 5. So, this tells us that <span class="math-inline">\\(\begin{bmatrix} 1/2 \\\\ -1 \\\\ 1/2 \\\\ 0 \\\\ 0 \end{bmatrix}\\)</span> is in <span class="math-inline">\\(\text{nullsp}(A)\\)</span>. If we'd like to get rid of the fraction, then we could also say <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ -2 \\\\ 1 \\\\ 0 \\\\ 0 \end{bmatrix}\\)</span> is in <span class="math-inline">\\(\text{nullsp}(A)\\)</span> too.

There are plenty of other answers. For instance, the fact that

<div class="math-display">
$$
\text{col}_3(A) = \frac{1}{2}\,\text{col}_1(A) + \frac{1}{2}\,\text{col}_5(A)
$$
</div>

tells us that <span class="math-inline">\\(\begin{bmatrix} 1/2 \\\\ 0 \\\\ -1 \\\\ 0 \\\\ 1/2 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ 0 \\\\ -2 \\\\ 0 \\\\ 1 \end{bmatrix}\\)</span> are also in <span class="math-inline">\\(\text{nullsp}(A)\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> Fill in the blanks: <span class="math-inline">\\(\text{nullsp}(A^T)\\)</span> is a \_\_(i)\_\_-dimensional subspace of \_\_(ii)\_\_.

| <span class="math-inline">\\(i\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(2\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(3\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(4\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(5\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(n-2\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(n-1\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(n\\)</span> |  |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
|  |  |  |  |  |  |  |  |  |
| <span class="math-inline">\\(ii\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\mathbb{R}^2\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\mathbb{R}^3\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\mathbb{R}^4\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\mathbb{R}^5\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\mathbb{R}^{n-2}\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\mathbb{R}^{n-1}\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\mathbb{R}^n\\)</span> |  |

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\mathbb{R}^2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\mathbb{R}^3\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\mathbb{R}^4\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\mathbb{R}^5\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\mathbb{R}^{n-2}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\mathbb{R}^{n-1}\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(\mathbb{R}^n\\)</span></span></div>

Since <span class="math-inline">\\(\text{rank}(A)=2\\)</span> and <span class="math-inline">\\(\text{rank}(A) = \text{rank}(A^T)\\)</span>, we also have <span class="math-inline">\\(\text{rank}(A^T)=2\\)</span>. The matrix <span class="math-inline">\\(A^T\\)</span> has <span class="math-inline">\\(n\\)</span> columns, so rank-nullity gives

<div class="math-display">
$$
\dim(\text{nullsp}(A^T)) = \text{\# columns in A^T} - \text{rank}(A^T) = n - 2
$$
</div>

 Also, <span class="math-inline">\\(\text{nullsp}(A^T)\\)</span> is a subspace of <span class="math-inline">\\(\mathbb{R}^n\\)</span>, because vectors in <span class="math-inline">\\(\text{nullsp}(A^T)\\)</span> must have one entry for each column of <span class="math-inline">\\(A^T\\)</span> (row of <span class="math-inline">\\(A\\)</span>).
</details>

</div>
</div>

</div>

---

## Problem 6: (4 pts) <span class="math-inline">\\(\boxed{\text{Counts towards Midterm 2 redemption score}}\\)</span>

Suppose <span class="math-inline">\\(A\\)</span> and <span class="math-inline">\\(B\\)</span> are both (not necessarily symmetric!) <span class="math-inline">\\(n \times n\\)</span> matrices. Which of the following is <span class="math-inline">\\(\nabla f(\vec x)\\)</span>, the gradient of

<div class="math-display">
$$
f(\vec x) = (A \vec x)^T (B \vec x)
$$
</div>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(2AB \vec x\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(A^TB \vec x\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(2A^TB \vec x\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(2B^TA \vec x\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\((A^TB + B^TA) \vec x\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\((A^TB - B^TA) \vec x\\)</span></span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(2AB \vec x\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(A^TB \vec x\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(2A^TB \vec x\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(2B^TA \vec x\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\((A^TB + B^TA) \vec x\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\((A^TB - B^TA) \vec x\\)</span></span></div>

We can rewrite the function as

<div class="math-display">
$$
f(\vec x) = (A\vec x)^T(B\vec x) = \vec x^T A^T B \vec x
$$
</div>

 If <span class="math-inline">\\(M\\)</span> is any matrix, then

<div class="math-display">
$$
\nabla(\vec x^T M \vec x) = (M + M^T)\vec x
$$
</div>

 Here, <span class="math-inline">\\(M = A^TB\\)</span>, so

<div class="math-display">
$$
\nabla f(\vec x) = \left(A^TB + (A^TB)^T\right)\vec x = \boxed{(A^TB + B^TA)\vec x}
$$
</div>

</details>

---

## Problem 7: (6 pts) <span class="math-inline">\\(\boxed{\text{Counts towards Midterm 2 redemption score}}\\)</span>

Consider the function <span class="math-inline">\\(f: \mathbb{R} \to \mathbb{R}\\)</span> graphed below.

<div style="text-align: center;">
<img src="imgs/convexity-scale.png" alt="image" style="width: 60%; max-width: 100%;">
</div>

Note that <span class="math-inline">\\(f\\)</span> is a piecewise linear function, with slopes of <span class="math-inline">\\(0\\)</span>, <span class="math-inline">\\(4\\)</span>, and <span class="math-inline">\\(-4\\)</span>. The slope changes at the following values of <span class="math-inline">\\(x\\)</span>: <span class="math-inline">\\(-6, -5, -2, -1, 1, 2, 5, 6\\)</span>.

Suppose we want to minimize <span class="math-inline">\\(f(x)\\)</span> using gradient descent. There are several values of <span class="math-inline">\\(x\\)</span> such that <span class="math-inline">\\(f\\)</span> is not differentiable at <span class="math-inline">\\(x\\)</span>; if any of our guesses <span class="math-inline">\\(x^{(0)}, x^{(1)}, x^{(2)}, \ldots\\)</span> ever evaluate to one of these values, we say that gradient descent **crashes**.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">2 pts</span> True or False: <span class="math-inline">\\(f(x)\\)</span> is convex on the domain <span class="math-inline">\\(x \in [-9, 9]\\)</span>.

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> False</span></div>

This is false. In order for a function to be convex, it must be the case that we can draw a line segment between any two points on the function and the line segment never passes below the function, but this is not the case for this <span class="math-inline">\\(f\\)</span>. For example, connect <span class="math-inline">\\((-3, 1)\\)</span> to <span class="math-inline">\\((-1, -3)\\)</span>; the line segment is entirely beneath the function.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Suppose we choose a learning rate/step size of <span class="math-inline">\\(\alpha = 0.1\\)</span>.

Among the options below, which value of <span class="math-inline">\\(x^{(0)}\\)</span> will allow gradient descent to **converge to the global minimum** of <span class="math-inline">\\(f(x)\\)</span> **without crashing**?

If multiple values of <span class="math-inline">\\(x^{(0)}\\)</span> are possible, **select the value that converges the quickest** (i.e. in the fewest number of iterations).

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1.4\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1.6\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1.8\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1.9\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(2.0\\)</span></span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1.4\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(1.6\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1.8\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1.9\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(2.0\\)</span></span></div>

When <span class="math-inline">\\(x\\)</span> is between <span class="math-inline">\\(1\\)</span> and <span class="math-inline">\\(2\\)</span>, the slope is 4, so with learning rate <span class="math-inline">\\(\alpha = 0.1\\)</span>, gradient descent updates by

<div class="math-display">
$$
x^{(t+1)} = x^{(t)} - 0.1(4) = x^{(t)} - 0.4
$$
</div>

 Now, let's check the options:

-   <span class="math-inline">\\(1.4 \to 1.0\\)</span>, so gradient descent crashes at the nondifferentiable point <span class="math-inline">\\(x=1\\)</span>.

-   <span class="math-inline">\\(1.6 \to 1.2 \to 0.8\\)</span>, so it reaches the flat global-minimum region without crashing.

-   <span class="math-inline">\\(1.8 \to 1.4 \to 1.0\\)</span>, so it crashes.

-   <span class="math-inline">\\(1.9 \to 1.5 \to 1.1 \to 0.7\\)</span>, so it also works, but it takes more iterations than starting at 1.6.

-   Starting at <span class="math-inline">\\(2.0\\)</span> crashes immediately, because <span class="math-inline">\\(f\\)</span> is not differentiable there.

Therefore, the correct choice is <span class="math-inline">\\(\boxed{1.6}\\)</span>.
</details>

</div>
</div>

</div>

---

## Problem 8: (6 pts) <span class="math-inline">\\(\boxed{\text{Counts towards Midterm 2 redemption score}}\\)</span>

Suppose we fit a multiple linear regression model **with** an intercept term that predicts the `height` of a wolverine given its `weight` and `color`. The model is fit by minimizing mean squared error.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">2 pts</span> If we one hot encode the color feature **without** dropping any categories, the design matrix <span class="math-inline">\\(X\\)</span> has 6 columns.

How many unique `color`s are there? Give your answer as an integer with no variables.

There are <span class="math-inline">\\(\minibox{3cm}{4}[1cm]\\)</span> unique `color`s.

<details markdown="1"><summary>Solution</summary>

The 6 columns are:

-   1 intercept column

-   1 `weight` column

-   1 column for each color after one hot encoding without dropping any categories

So the number of unique colors is

<div class="math-display">
$$
6 - 2 = \boxed{4}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Assume that not all wolverines in the dataset have the same `weight`, and that there is at least one wolverine with each color.

What impact would dropping one of the color categories' columns from the design matrix <span class="math-inline">\\(X\\)</span> have? **Select all that apply.**

<span class="mc-square" aria-hidden="true"></span> It would decrease the rank of <span class="math-inline">\\(X\\)</span>.

<span class="mc-square" aria-hidden="true"></span> It would guarantee that <span class="math-inline">\\(X\\)</span> invertible.

<span class="mc-square" aria-hidden="true"></span> It would guarantee that <span class="math-inline">\\(X^TX\\)</span> invertible.

<span class="mc-square" aria-hidden="true"></span> It would guarantee the existence of a unique optimal parameter vector <span class="math-inline">\\(\vec w^{\ast}\\)</span>.

<span class="mc-square" aria-hidden="true"></span> It would change <span class="math-inline">\\(\text{nullsp}(X)\\)</span>.

<span class="mc-square" aria-hidden="true"></span> It would change <span class="math-inline">\\(\text{colsp}(X)\\)</span>.

<details markdown="1"><summary>Solution</summary>

<span class="mc-square" aria-hidden="true"></span> It would change <span class="math-inline">\\(\text{colsp}(X)\\)</span>.

By dropping one of the color categories' columns from the design matrix <span class="math-inline">\\(X\\)</span>, we guarantee that the columns of <span class="math-inline">\\(X\\)</span> are linearly independent. As discussed in the course notes, when one hot encoding, the sum of all 4 color columns is equal to the intercept column (of all ones); by dropping one of the 4 color columns, we don't lose any information but remove the linear dependence. (The other assumptions in the problem help guarantee this, too --- for instance, if all of the wolverines in the dataset have the same `weight`, then the `weight` column is a scalar multiple of the intercept column.)

With that in mind, let's look at the options:

-   It would decrease the rank of <span class="math-inline">\\(X\\)</span>. **False**: <span class="math-inline">\\(\text{colsp}(X)\\)</span> doesn't change, so <span class="math-inline">\\(\text{rank}(X)\\)</span> doesn't change.

-   It would guarantee that <span class="math-inline">\\(X\\)</span> is invertible. **False**: <span class="math-inline">\\(X\\)</span> is not necessarily square!

-   It would guarantee that <span class="math-inline">\\(X^TX\\)</span> is invertible. **True**: If <span class="math-inline">\\(X\\)</span>'s columns are linearly independent, then <span class="math-inline">\\(X^TX\\)</span> is invertible, since <span class="math-inline">\\(\text{rank}(X) = \text{rank}(X^TX) = \text{\# columns in } X^TX\\)</span>.

-   It would gaurantee the existence of a unique optimal parameter vector <span class="math-inline">\\(\vec w^{\ast}\\)</span>. **True**: If <span class="math-inline">\\(X\\)</span>'s columns are linearly independent, there is a unique <span class="math-inline">\\(\vec w^{\ast}\\)</span>.

-   It would change <span class="math-inline">\\(\text{nullsp}(X)\\)</span>: **True**. With the redundant column, <span class="math-inline">\\(X\\)</span> has a non-trivial null space, but without it, <span class="math-inline">\\(X\\)</span>'s null space is <span class="math-inline">\\(\lbrace \vec 0 \rbrace\\)</span>.

-   It would change <span class="math-inline">\\(\text{colsp}(X)\\)</span>: **False**, as discussed above.
</details>

</div>
</div>

</div>

---

## Problem 9 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">18 pts</span>

Consider the matrix <span class="math-inline">\\(A = \begin{bmatrix} 2 &amp; 1 \\\\ c &amp; 6 \end{bmatrix}\\)</span>, where <span class="math-inline">\\(c \in \mathbb{R}\\)</span> is some constant.

Each part asks you to find the values of <span class="math-inline">\\(c\\)</span>, <span class="math-inline">\\(\lambda&#95;1\\)</span> (<span class="math-inline">\\(A\\)</span>'s **larger eigenvalue**) and <span class="math-inline">\\(\lambda&#95;2\\)</span> (<span class="math-inline">\\(A\\)</span>'s **smaller eigenvalue**) given the information provided. Your answers should be **numbers with no variables**.

If <span class="math-inline">\\(A\\)</span> only has one unique eigenvalue, put the same number for both <span class="math-inline">\\(\lambda&#95;1\\)</span> and <span class="math-inline">\\(\lambda&#95;2\\)</span>.

<em>Hint: Remember the relationship between the eigenvalues of a matrix and its determinant and trace.</em>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span>
<span class="math-inline">\\(A\\)</span> is **not** invertible.

<span class="math-inline">\\(c = \minibox{3cm}{12}, \qquad \lambda&#95;1 = \minibox{3cm}{8}, \qquad \lambda&#95;2 = \minibox{3cm}{0}\\)</span>

<details markdown="1"><summary>Solution</summary>

If <span class="math-inline">\\(A\\)</span> is not invertible, then <span class="math-inline">\\(\det(A)=0\\)</span>. Here,

<div class="math-display">
$$
\det(A) = (2)(6) - (1)(c) = 12 - c
$$
</div>

 so

<div class="math-display">
$$
12 - c = 0 \implies \boxed{c = 12}
$$
</div>

The trace is

<div class="math-display">
$$
\text{tr}(A)=2+6=8
$$
</div>

 so the eigenvalues must add to 8. Since the determinant is 0, the eigenvalues must multiply to 0, so one eigenvalue is 0 and the other is 8. Therefore,

<div class="math-display">
$$
\boxed{\lambda_1 = 8, \qquad \lambda_2 = 0}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span>
<span class="math-inline">\\(A\\)</span>'s characteristic polynomial is <span class="math-inline">\\(p(\lambda) = \lambda^2 - 8\lambda + 7\\)</span>.

<span class="math-inline">\\(c = \minibox{3cm}{5}, \qquad \lambda&#95;1 = \minibox{3cm}{7}, \qquad \lambda&#95;2 = \minibox{3cm}{1}\\)</span>

<details markdown="1"><summary>Solution</summary>

For a <span class="math-inline">\\(2 \times 2\\)</span> matrix,

<div class="math-display">
$$
p(\lambda) = \lambda^2 - (\text{trace})\lambda + \det(A)
$$
</div>

 Here, the trace is 8, as both <span class="math-inline">\\(A\\)</span> and the characteristic polynomial tell us. This must mean

<div class="math-display">
$$
\det(A) = 7
$$
</div>

 Since <span class="math-inline">\\(\det(A)=12-c\\)</span>, we get

<div class="math-display">
$$
12 - c = 7 \implies \boxed{c = 5}
$$
</div>

 Now, let's factor the characteristic polynomial:

<div class="math-display">
$$
\lambda^2 - 8\lambda + 7 = (\lambda-7)(\lambda-1)
$$
</div>

 so the eigenvalues are 7 and 1. Thus,

<div class="math-display">
$$
\boxed{\lambda_1 = 7, \qquad \lambda_2 = 1}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span>
<span class="math-inline">\\(A\\)</span> is **not** diagonalizable.

<span class="math-inline">\\(c = \minibox{3cm}{-4}, \qquad \lambda&#95;1 = \minibox{3cm}{4}, \qquad \lambda&#95;2 = \minibox{3cm}{4}\\)</span>

<details markdown="1"><summary>Solution</summary>

A <span class="math-inline">\\(2 \times 2\\)</span> matrix is not diagonalizable only if it has an eigenvalue <span class="math-inline">\\(\lambda\\)</span> with algebraic multiplicity 2 but geometric multiplicity 1, i.e. a repeated eigenvalue but only one linearly independent eigenvector. Since the two eigenvalues must add to 8, they must both be

<div class="math-display">
$$
\lambda = \frac{8}{2} = 4
$$
</div>



<div class="math-display">
$$
\boxed{\lambda_1 = 4, \qquad \lambda_2 = 4}
$$
</div>

 That means the determinant must be

<div class="math-display">
$$
4 \cdot 4 = 16
$$
</div>

 So,

<div class="math-display">
$$
12 - c = 16 \implies \boxed{c = -4}
$$
</div>

</details>

</div>
</div>

</div>

---

{: .yellow }
> **Make sure to place the larger eigenvalue in <span class="math-inline">\\(\lambda&#95;1\\)</span> and the smaller eigenvalue in <span class="math-inline">\\(\lambda&#95;2\\)</span>!**

## Problem 10 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>

Consider the adjacency matrix <span class="math-inline">\\(A = \begin{bmatrix} 0.4 &amp; 0 &amp; 0.5 \\\\ 0.4 &amp; 0 &amp; 0.5 \\\\ a &amp; b &amp; c \end{bmatrix}\\)</span> for a Markov chain with three states, where <span class="math-inline">\\(a, b, c \in \mathbb{R}\\)</span> are some constants.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Find <span class="math-inline">\\(a\\)</span>, <span class="math-inline">\\(b\\)</span>, and <span class="math-inline">\\(c\\)</span> such that <span class="math-inline">\\(A\\)</span> is a valid adjacency matrix. Give your answers as numbers with no variables.

<span class="math-inline">\\(a = \minibox{3cm}{0.2}[1cm], \qquad b = \minibox{3cm}{1}[1cm], \qquad c = \minibox{3cm}{0}[1cm]\\)</span>

<details markdown="1"><summary>Solution</summary>

For a valid adjacency matrix, each column must sum to 1, since the columns describe the transition probabilities **out of** a given state. So,

<div class="math-display">
$$
\begin{align*}
0.4 + 0.4 + a &= 1 \implies a = 0.2 \\\\
0 + 0 + b &= 1 \implies b = 1 \\\\
0.5 + 0.5 + c &= 1 \implies c = 0
\end{align*}
$$
</div>

Therefore,

<div class="math-display">
$$
\boxed{a = 0.2, \qquad b = 1, \qquad c = 0}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Suppose <span class="math-inline">\\(\vec x^{\ast} \in \mathbb{R}^3\\)</span> is a vector containing the long-run fraction of time spent in each state. Which of the following vectors is <span class="math-inline">\\(\vec x^{\ast}\\)</span> and why?

1.  <span class="math-inline">\\(\vec x^{\ast}\\)</span> is
<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \begin{bmatrix} 1/3 \\\\ 1/3 \\\\ 1/3 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \begin{bmatrix} 4/9 \\\\ 0 \\\\ 5/9 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \begin{bmatrix} 5/16 \\\\ 5/16 \\\\ 6/16 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \begin{bmatrix} 5/16 \\\\ 6/16 \\\\ 5/16 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \begin{bmatrix} 3/16 \\\\ 3/16 \\\\ 10/16 \end{bmatrix}\\)</span></span></div>

2.  because <span class="math-inline">\\(\vec x^{\ast}\\)</span> is the eigenvector of <span class="math-inline">\\(A\\)</span> corresponding to the eigenvalue



<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(-1\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(0\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(0.4\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1.8\\)</span></span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(-1\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(0\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(0.4\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(1\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1.8\\)</span></span></div>

The long-run fraction of time spent in each state is the stationary distribution, so it must satisfy

<div class="math-display">
$$
A\vec x^* = \vec x^*
$$
</div>

 That means <span class="math-inline">\\(\vec x^{\ast}\\)</span> is an eigenvector corresponding to eigenvalue 1.

Using the matrix from part **a)**,

<div class="math-display">
$$
A = \begin{bmatrix} 0.4 & 0 & 0.5 \\\\ 0.4 & 0 & 0.5 \\\\ 0.2 & 1 & 0 \end{bmatrix}
$$
</div>

 we can check that

<div class="math-display">
$$
A\begin{bmatrix} 5/16 \\\\ 5/16 \\\\ 6/16 \end{bmatrix}
=
\begin{bmatrix} 5/16 \\\\ 5/16 \\\\ 6/16 \end{bmatrix}
$$
</div>

 So the correct choices are

<div class="math-display">
$$
\boxed{\begin{bmatrix} 5/16 \\\\ 5/16 \\\\ 6/16 \end{bmatrix}}
\qquad \text{and} \qquad
\boxed{1}
$$
</div>

</details>

</div>
</div>

</div>

---

## Problem 11 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>

Let <span class="math-inline">\\(A\\)</span> be a <span class="math-inline">\\(4 \times 4\\)</span> **symmetric** matrix with eigenvalue decomposition <span class="math-inline">\\(A = V \Lambda V^{-1}\\)</span>. Suppose the columns of <span class="math-inline">\\(V\\)</span> are <span class="math-inline">\\(\vec v&#95;1\\)</span>, <span class="math-inline">\\(\vec v&#95;2\\)</span>, <span class="math-inline">\\(\vec v&#95;3\\)</span>, and <span class="math-inline">\\(\vec v&#95;4\\)</span>, in that order, and that the columns of <span class="math-inline">\\(V\\)</span> are unit vectors.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">2 pts</span> Suppose <span class="math-inline">\\(\Lambda = \begin{bmatrix} 4 &amp; 0 &amp; 0 &amp; 0 \\\\ 0 &amp; 3 &amp; 0 &amp; 0 \\\\ 0 &amp; 0 &amp; 2 &amp; 0 \\\\ 0 &amp; 0 &amp; 0 &amp; 1 \end{bmatrix}\\)</span>.

True or False: <span class="math-inline">\\(V\\)</span> is guaranteed to be an orthogonal matrix.

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

This is true. Since <span class="math-inline">\\(A\\)</span> is symmetric, the spectral theorem states that eigenvectors corresponding to different eigenvalues are automatically orthogonal. Additionally, <span class="math-inline">\\(A\\)</span> has four unique eigenvalues. This means that the columns of <span class="math-inline">\\(V\\)</span> are guaranteed to be orthogonal. Since we're told that the columns of <span class="math-inline">\\(V\\)</span> are unit vectors, they are orthonormal, so <span class="math-inline">\\(V\\)</span> is orthogonal.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">2 pts</span> Suppose <span class="math-inline">\\(\Lambda = \begin{bmatrix} 4 &amp; 0 &amp; 0 &amp; 0 \\\\ 0 &amp; 2 &amp; 0 &amp; 0 \\\\ 0 &amp; 0 &amp; 2 &amp; 0 \\\\ 0 &amp; 0 &amp; 0 &amp; 1 \end{bmatrix}\\)</span>.

True or False: <span class="math-inline">\\(V\\)</span> is guaranteed to be an orthogonal matrix.

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> False</span></div>

This is false. A symmetric matrix always has an orthonormal eigenbasis, but when an eigenvalue is repeated, the problem does not guarantee that the particular unit eigenvectors in <span class="math-inline">\\(V\\)</span> were chosen to be orthogonal within that eigenspace. The two eigenvectors corresponding to <span class="math-inline">\\(\lambda = 2\\)</span> are guaranteed to be orthogonal to the eigenvectors for <span class="math-inline">\\(\lambda = 1\\)</span> and <span class="math-inline">\\(\lambda = 4\\)</span>, but not necessarily orthogonal to each other.
</details>

The rest of this problem does not use any of the information from parts **a)** and **b)**. Suppose <span class="math-inline">\\(k\\)</span> is some positive integer greater than 1, and that

<div class="math-display">
$$
\vec x = 5 \vec v_1 - 3 \vec v_2 - 5 \vec v_3 + \vec v_4
$$
</div>

 and

<div class="math-display">
$$
A^k \vec x = 40 \vec v_1 - 81 \vec v_2 + 64 \vec v_4
$$
</div>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> What is the value of <span class="math-inline">\\(k\\)</span>? Select one of the answers below, then justify your answer in the box provided. <em>Hint: If <span class="math-inline">\\(A = V \Lambda V^{-1}\\)</span>, what is <span class="math-inline">\\(A^k\\)</span>?</em>

1.  Answer:
<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(3\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(4\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(5\\)</span></span></div>

2.  Justify your answer in the box below.

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(2\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(3\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(4\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(5\\)</span></span></div>

If <span class="math-inline">\\(A = V\Lambda V^{-1}\\)</span>, then

<div class="math-display">
$$
A^k \vec x = 5\lambda_1^k \vec v_1 - 3\lambda_2^k \vec v_2 - 5\lambda_3^k \vec v_3 + \lambda_4^k \vec v_4.
$$
</div>

 Matching this with

<div class="math-display">
$$
A^k \vec x = 40 \vec v_1 - 81 \vec v_2 + 64 \vec v_4
$$
</div>

 gives

<div class="math-display">
$$
\lambda_1^k = 8 \qquad \lambda_2^k = 27 \qquad \lambda_4^k = 64
$$
</div>

 Among the answer choices, the only value of <span class="math-inline">\\(k\\)</span> for which all three numbers are perfect <span class="math-inline">\\(k\\)</span>th powers is <span class="math-inline">\\(k=3\\)</span>:

<div class="math-display">
$$
8 = 2^3 \qquad 27 = 3^3 \qquad 64 = 4^3
$$
</div>

 Therefore, <span class="math-inline">\\(\boxed{k = 3}\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">2 pts</span> Fill in the blank: as <span class="math-inline">\\(k \to \infty\\)</span>, the direction of <span class="math-inline">\\(A^k \vec x\\)</span> approaches the direction of\...

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\vec v&#95;1\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\vec v&#95;2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\vec v&#95;3\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\vec v&#95;4\\)</span></span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\vec v&#95;1\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\vec v&#95;2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\vec v&#95;3\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(\vec v&#95;4\\)</span></span></div>

From part **c)**, the relevant eigenvalues have magnitudes 2, 3, 0, and 4. As <span class="math-inline">\\(k \to \infty\\)</span>, the component corresponding to the largest eigenvalue magnitude dominates, so the direction of <span class="math-inline">\\(A^k \vec x\\)</span> approaches the direction of <span class="math-inline">\\(\boxed{\vec v&#95;4}\\)</span>.
</details>

</div>
</div>

</div>

---

## Problem 12 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>

Suppose <span class="math-inline">\\(\tilde X\\)</span> is a <span class="math-inline">\\(24 \times 3\\)</span> matrix whose columns are mean-centered (i.e. have a mean of 0). Let <span class="math-inline">\\(\tilde X = U \Sigma V^T\\)</span> be the singular value decomposition of <span class="math-inline">\\(\tilde X\\)</span>, where

<div class="math-display">
$$
\tilde X = U \underbrace{\begin{bmatrix} 12 & 0 & 0 \\\\ 0 & 2 & 0 \\\\ 0 & 0 & 0 \\\\\vdots & \vdots & \vdots \end{bmatrix}}_{\Sigma} \underbrace{\begin{bmatrix} 1/\sqrt{10} & 3/\sqrt{10} & 0 \\\\ \cdots & \vec v_2^T & \cdots \\\\ 0 & 0 & 1 \end{bmatrix}}_{V^T}
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">2 pts</span> Find <span class="math-inline">\\(\text{rank}(\tilde X)\\)</span>. Give your answer as an integer with no variables.

<span class="math-inline">\\(\text{rank}(\tilde X) = \minibox{3cm}{2}\\)</span>

<details markdown="1"><summary>Solution</summary>

The rank of a matrix is equal to its number of non-zero singular values. Here, the singular values are 12, 2, and 0, so

<div class="math-display">
$$
\text{rank}(\tilde X) = \boxed{2}.
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> It is possible to find <span class="math-inline">\\(\vec v&#95;2^T\\)</span>, the second row of <span class="math-inline">\\(V^T\\)</span>, solely using the information provided (without knowing any of the values in <span class="math-inline">\\(\tilde X\\)</span>). In one English sentence, **explain how** to find it.

<details markdown="1"><summary>Solution</summary>

Since <span class="math-inline">\\(V\\)</span> is orthogonal, the rows of <span class="math-inline">\\(V^T\\)</span> must be orthonormal, so <span class="math-inline">\\(\vec v&#95;2^T\\)</span> is the unit vector orthogonal to both <span class="math-inline">\\(\begin{bmatrix} 1/\sqrt{10} \\\\ 3/\sqrt{10} \\\\ 0 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\begin{bmatrix} 0 \\\\ 0 \\\\ 1 \end{bmatrix}\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">2 pts</span> True or False: There exists some vector <span class="math-inline">\\(\vec z \in \mathbb{R}^{24}\\)</span> such that <span class="math-inline">\\(\tilde X \tilde X^T \vec z = 2 \vec z\\)</span>.

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Impossible to tell</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> False</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Impossible to tell</span></div>

This is **False**. The eigenvalues of <span class="math-inline">\\(\tilde X \tilde X^T\\)</span> are the squares of the singular values of <span class="math-inline">\\(\tilde X\\)</span>, so they are <span class="math-inline">\\(144\\)</span>, <span class="math-inline">\\(4\\)</span>, and <span class="math-inline">\\(0\\)</span>. Since 2 is not an eigenvalue of <span class="math-inline">\\(\tilde X \tilde X^T\\)</span>, no such vector <span class="math-inline">\\(\vec z\\)</span> exists.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">5 pts</span> What is the largest possible variance of the components of <span class="math-inline">\\(\tilde X \vec w\\)</span>, where <span class="math-inline">\\(\vec w \in \mathbb{R}^3\\)</span> is a unit vector? Select one of the answers below, then justify your answer in the box provided.

1.  Answer:
<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(6\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(12\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(24\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(144\\)</span></span></div>

2.  Justify your answer in the box below.

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(2\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(6\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(12\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(24\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(144\\)</span></span></div>

Because the columns of <span class="math-inline">\\(\tilde X\\)</span> are mean-centered, the variance of the components of <span class="math-inline">\\(\tilde X\vec w\\)</span> is

<div class="math-display">
$$
\frac{1}{n}\|\tilde X\vec w\|^2 = \frac{1}{24}\|\tilde X\vec w\|^2
$$
</div>

 This is maximized when <span class="math-inline">\\(\vec w\\)</span> is the first right singular vector (<span class="math-inline">\\(\vec v&#95;1\\)</span>), and the maximum value is

<div class="math-display">
$$
\frac{\sigma_1^2}{24} = \frac{12^2}{24} = \frac{144}{24} = 6
$$
</div>

 So the largest possible variance is <span class="math-inline">\\(\boxed{6}\\)</span>.
</details>

</div>
</div>

</div>

---

## Problem 13 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span>

What is one topic you studied a lot for that wasn't on the Final Exam? **Blank answers will receive no credit!**

<details markdown="1"><summary>Solution</summary>

</details>

Congrats on completing the Final Exam for EECS 245! We'll really miss you; please stay in touch.

Feel free to draw us a picture about EECS 245 in the box below.

{% endraw %}
