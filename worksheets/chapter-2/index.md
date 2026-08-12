---
layout: minimal
title: "Chapter 2: Simple Linear Regression"
description: "Practice problems for Chapter 2: Simple Linear Regression."
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

<style>
.worksheet-source { font-size: 0.8rem; color: #57606a; margin: -0.4rem 0 0.8rem; }
.worksheet-source a { color: #0066cc; }
</style>

<style>
#main-header,
.site-header,
.aux-nav,
.main-header,
.side-bar {
  display: none !important;
}
body { padding-top: 0 !important; }
.main-content-wrap { margin-top: 0 !important; }
.exam-breadcrumb { font-size: 0.85rem; margin-bottom: 0.75rem; }
.exam-breadcrumb a { color: #0066cc; text-decoration: none; }
.exam-breadcrumb a:hover { text-decoration: underline; }
.exam-breadcrumb .crumb-sep { color: #57606a; margin: 0 0.35rem; }
</style>
<nav class="exam-breadcrumb" aria-label="Breadcrumb">
<a href="/">← Back</a><span class="crumb-sep">·</span><a href="https://eecs245.org">Course home</a>
</nav>

# Chapter 2: Simple Linear Regression

*Topics: partial derivatives, finding optimal parameters, correlation*

*Problems below are collected from past exams; each links back to its full exam. Solutions are in the dropdowns.*

## Problems

- [FA25 MT1 · Problem 3](#fa25-mt1--problem-3-spreading-your-wings-12-pts)
- [FA25 Final · Problem 2](#fa25-final--problem-2-10-pts-mt1-redemption)
- [WN26 MT1 · Problem 2](#wn26-mt1--problem-2-14-pts)
- [WN26 Final · Problem 2](#wn26-final--problem-2-13-pts-mt1-redemption)
- [SP26 MT1 · Problem 3](#sp26-mt1--problem-3-14-pts)
- [SP26 Final · Problem 2](#sp26-final--problem-2-9-pts-mt1-redemption)

---

## FA25 MT1 · Problem 3: Spreading Your Wings <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>

<p class="worksheet-source">From <a href="/exams/fa25-mt1/">FA25 MT1</a></p>

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

<span class="math-inline">\\(h(15) =\\)</span> \_\_\_\_\_\_

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

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(-6 \sigma&#95;x \sigma&#95;y\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(6 \sigma&#95;x \sigma&#95;y\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(-6r \sigma&#95;x \sigma&#95;y\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(6r \sigma&#95;x \sigma&#95;y\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(-6nr \sigma&#95;x \sigma&#95;y\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(6nr \sigma&#95;x \sigma&#95;y\\)</span></span></div>

2.  Show your work in the box below. English explanations are not enough.

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(-6 \sigma&#95;x \sigma&#95;y\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(6 \sigma&#95;x \sigma&#95;y\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(-6r \sigma&#95;x \sigma&#95;y\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(6r \sigma&#95;x \sigma&#95;y\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(-6nr \sigma&#95;x \sigma&#95;y\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(6nr \sigma&#95;x \sigma&#95;y\\)</span></span></div>

We'll find the answer by expanding out the definition of <span class="math-inline">\\(\sigma&#95;z^2\\)</span> and simplifying.

<div class="math-display">
$$
\begin{align*}
\sigma_z^2 &= \frac{1}{n} \sum_{i=1}^n (z_i - \bar{z})^2 \\\\
&= \frac{1}{n} \sum_{i=1}^n (3x_i - y_i - (3\bar{x} - \bar{y}))^2 \\\\
&= \underbrace{\frac{1}{n} \sum_{i=1}^n (3x_i - 3\bar{x} - y_i + \bar{y})^2}_\text{distributed the negative sign and rearranged} \\\\
&= \frac{1}{n} \sum_{i=1}^n \underbrace{(3(x_i - \bar{x}) - (y_i - \bar{y}))^2}_\text{treat this as }(a - b)^2 \\\\
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

## FA25 Final · Problem 2 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">10 pts</span> <span class="badge" data-flag="mt1-redemption" style="background-color: #9A3324; color: #FFFFFF; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">MT1 Redemption</span>

<p class="worksheet-source">From <a href="/exams/fa25-final/">FA25 Final</a></p>

Let <span class="math-inline">\\(k\\)</span> be a positive integer and let <span class="math-inline">\\(\alpha\\)</span> be a positive real number. Consider the dataset of <span class="math-inline">\\(n = 2k+1\\)</span> points, <span class="math-inline">\\(\underbrace{(-k, -\alpha), (-k+1, 0), (-k+2, 0), \ldots, (-1, 0)}&#95;{k \text{ points}}, (0, 0), \underbrace{(1, 0), \ldots, (k-2, 0), (k-1, 0), (k, \alpha)}&#95;{k \text{ points}}\\)</span>.

Note that the <span class="math-inline">\\(x\\)</span>-values are equally spaced, starting from <span class="math-inline">\\(-k\\)</span> and ending at <span class="math-inline">\\(k\\)</span>. The <span class="math-inline">\\(y\\)</span>-values are all 0, except for the first and last points, which have <span class="math-inline">\\(y\\)</span>-value <span class="math-inline">\\(-\alpha\\)</span> and <span class="math-inline">\\(\alpha\\)</span>, respectively. For example, if <span class="math-inline">\\(k = 4\\)</span> and <span class="math-inline">\\(\alpha = 2\\)</span>, the dataset looks like

<div style="text-align: center;">
<img src="imgs/fa25-final-q02/outliers.png" alt="image" style="width: 50%; max-width: 100%;">
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Find <span class="math-inline">\\(\bar{x}\\)</span> and <span class="math-inline">\\(\bar{y}\\)</span>, the means of the <span class="math-inline">\\(x\\)</span>- and <span class="math-inline">\\(y\\)</span>-values, respectively. Give your answers as expressions involving <span class="math-inline">\\(k\\)</span>, <span class="math-inline">\\(\alpha\\)</span>, and/or other constants.

<span class="math-inline">\\(\bar{x} = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;, \qquad \bar{y} = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>

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
<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(0\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \alpha\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle 2 \alpha\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle 2 k \alpha\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle 2 k^2 \alpha\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \frac{2 \alpha}{k}\\)</span></span></div>

2.  Justify your answer in the box below.

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(0\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \alpha\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle 2 \alpha\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle 2 k \alpha\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle 2 k^2 \alpha\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \frac{2 \alpha}{k}\\)</span></span></div>

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

## WN26 MT1 · Problem 2 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">14 pts</span>

<p class="worksheet-source">From <a href="/exams/wn26-mt1/">WN26 MT1</a></p>

Suppose we'd like to fit a simple linear regression model to a dataset of <span class="math-inline">\\(n\\)</span> points,

<span class="math-inline">\\((x&#95;1, y&#95;1), (x&#95;2, y&#95;2), \ldots, (x&#95;n, y&#95;n)\\)</span>, by minimizing mean squared error.

Suppose <span class="math-inline">\\(w&#95;0^{\ast}\\)</span> and <span class="math-inline">\\(w&#95;1^{\ast}\\)</span> are the optimal intercept and slope parameters, respectively, and let

<div class="math-display">
$$
M = \frac{1}{n} \sum_{i=1}^n (y_i - (w_0^* + w_1^* x_i))^2
$$
</div>

 Finally, let <span class="math-inline">\\(\sigma&#95;x\\)</span> and <span class="math-inline">\\(\sigma&#95;y\\)</span> be the standard deviations of the <span class="math-inline">\\(x\\)</span>-values and <span class="math-inline">\\(y\\)</span>-values in the dataset, respectively. Assume that <span class="math-inline">\\(\sigma&#95;x &gt; 0\\)</span> and <span class="math-inline">\\(\sigma&#95;y &gt; 0\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">5 pts</span> Which of the following is the relationship between <span class="math-inline">\\(M\\)</span> and <span class="math-inline">\\(\sigma&#95;y^2\\)</span>? Select an answer and provide a brief explanation in the box provided.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(M \leq \sigma&#95;y^2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(M = \sigma&#95;y^2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(M \geq \sigma&#95;y^2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Impossible to tell</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(M \leq \sigma&#95;y^2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(M = \sigma&#95;y^2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(M \geq \sigma&#95;y^2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Impossible to tell</span></div>

<span class="math-inline">\\(M\\)</span> is the mean squared error of the best simple linear regression model for the dataset; it minimizes the mean squared error among all models of the form

<div class="math-display">
$$
h(x_i) = w_0 + w_1 x_i
$$
</div>

The constant model, <span class="math-inline">\\(h(x&#95;i) = w\\)</span>, can be thought of as a more restrictive version of the simple linear regression model, in that it has an intercept <span class="math-inline">\\(w\\)</span> and slope of <span class="math-inline">\\(0\\)</span>. So, the best simple linear regression model is at least as good as the best constant model, when both are measured by mean squared error. If the <span class="math-inline">\\(x\\)</span> and <span class="math-inline">\\(y\\)</span> values in the dataset have no linear association, meaning the correlation coefficient <span class="math-inline">\\(r\\)</span> is 0, then the best simple linear regression model is the same as the best constant model; otherwise, the best simple linear regression model is better, since it has all of the flexibility of the constant model, and more. The first section of [Chapter 2.5](https://notes.eecs245.org/simple-linear-regression/least-squares/) discusses this idea further.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">5 pts</span> Suppose that <span class="math-inline">\\(M = 0\\)</span>. What is the value of <span class="math-inline">\\(r\\)</span>, the correlation coefficient between the <span class="math-inline">\\(x\\)</span>-values and <span class="math-inline">\\(y\\)</span>-values in the dataset? <span class="math-inline">\\(\boxed{\text{Circle}}\\)</span> your final answer and provide a brief explanation. If there are multiple possible values, state them all.

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(r = 1\\)</span> or <span class="math-inline">\\(r = -1\\)</span>.

The only case in which <span class="math-inline">\\(M = 0\\)</span> is when the best simple linear regression model makes 0 errors, i.e. it passes through every point in the dataset. This happens when the <span class="math-inline">\\(x\\)</span> and <span class="math-inline">\\(y\\)</span> values in the dataset have a perfect linear association, meaning <span class="math-inline">\\(r = 1\\)</span> (positive linear association) or <span class="math-inline">\\(r = -1\\)</span> (negative linear association).
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">2 pts</span> True or False: It is possible for there to be multiple pairs of <span class="math-inline">\\((\text{intercept}, \text{slope})\\)</span> with a mean squared error of <span class="math-inline">\\(M\\)</span>.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> False</span></div>

The values of <span class="math-inline">\\(w&#95;0^{\ast}\\)</span> and <span class="math-inline">\\(w&#95;1^{\ast}\\)</span> are unique. We've seen several formulas for them in the notes; they are the unique minimizers of

<div class="math-display">
$$
R_\text{sq}(w_0, w_1) = \frac{1}{n} \sum_{i=1}^n (y_i - (w_0 + w_1 x_i))^2
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">2 pts</span> True or False: It is possible for there to be multiple pairs of <span class="math-inline">\\((\text{intercept}, \text{slope})\\)</span> with a mean squared error of <span class="math-inline">\\(M + 1\\)</span>.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

The values of <span class="math-inline">\\(w&#95;0\\)</span> and <span class="math-inline">\\(w&#95;1\\)</span> that minimize <span class="math-inline">\\(R&#95;\text{sq}(w&#95;0, w&#95;1)\\)</span> are unique, but we're not discussing the minimizers here, so that fact is irrelevant.

Instead, it's asking whether it's possible for there to be multiple pairs of <span class="math-inline">\\((w&#95;0, w&#95;1)\\)</span> with a mean squared error of something bigger than <span class="math-inline">\\(M\\)</span>. The <span class="math-inline">\\(+1\\)</span> is not important; we could have stated <span class="math-inline">\\(+17\\)</span> or <span class="math-inline">\\(+3\pi^2\\)</span> and the question would be the same.

Recall from [Chapter 2.3](https://notes.eecs245.org/simple-linear-regression/finding-optimal-parameters/) that the graph of <span class="math-inline">\\(R&#95;\text{sq}(w&#95;0, w&#95;1)\\)</span> looks like a bowl in <span class="math-inline">\\(\mathbb{R}^3\\)</span>. While there's only one point at which the bowl is minimized, for any height (<span class="math-inline">\\(z\\)</span>-value) greater than <span class="math-inline">\\(M\\)</span>, there are infinitely many pairs of <span class="math-inline">\\((w&#95;0, w&#95;1)\\)</span> that give that height. To see this, imagine slicing the bowl with the plane <span class="math-inline">\\(z = M + 1\\)</span>. This slice is an ellipse (stretched circle), upon which infinitely many combinations of <span class="math-inline">\\((w&#95;0, w&#95;1)\\)</span> lie.

So, yes, it is possible for there to be multiple pairs of <span class="math-inline">\\((w&#95;0, w&#95;1)\\)</span> with a mean squared error of <span class="math-inline">\\(M + 1\\)</span> --- in fact, that's guaranteed.
</details>

</div>
</div>

</div>

---

## WN26 Final · Problem 2 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">13 pts</span> <span class="badge" data-flag="mt1-redemption" style="background-color: #9A3324; color: #FFFFFF; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">MT1 Redemption</span>

<p class="worksheet-source">From <a href="/exams/wn26-final/">WN26 Final</a></p>

Suppose a dataset of <span class="math-inline">\\(n\\)</span> points, <span class="math-inline">\\((x&#95;1, y&#95;1), (x&#95;2, y&#95;2), \ldots, (x&#95;n, y&#95;n)\\)</span>, has the following properties:

<div class="math-display">
$$
\text{mean of }y\text{-values} = \bar y = 11,
\qquad
\text{standard deviation of }x\text{-values} = \sigma_x = 2,
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

<span class="math-inline">\\(\bar x = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>

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
\beta_0^* = \_\_\_\_\_\_
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

## SP26 MT1 · Problem 3 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">14 pts</span>

<p class="worksheet-source">From <a href="/exams/sp26-mt1/">SP26 MT1</a></p>

Suppose we fit a simple linear regression model **with** an intercept term, <span class="math-inline">\\(h(x&#95;i)=w&#95;0+w&#95;1x&#95;i\\)</span>, to a dataset of <span class="math-inline">\\(n\\)</span> points <span class="math-inline">\\((x&#95;1, y&#95;1), (x&#95;2, y&#95;2), \ldots, (x&#95;n, y&#95;n)\\)</span> by minimizing mean squared error. You are given the following information:

-   The fit model satisfies <span class="math-inline">\\(h(-4) = 5\\)</span> and <span class="math-inline">\\(h(8) = 14\\)</span>.

-   The mean of <span class="math-inline">\\(y&#95;1, y&#95;2, \ldots, y&#95;n\\)</span> is <span class="math-inline">\\(\bar y = 2\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Find <span class="math-inline">\\(\bar x\\)</span>, the mean of <span class="math-inline">\\(x&#95;1, x&#95;2, \ldots, x&#95;n\\)</span>. Show your work, and write your final answer in the box provided. Your answer should be a number with no variables. <em>Hint: What property does the line <span class="math-inline">\\(h(x&#95;i)\\)</span> satisfy?</em>

<div class="math-display">
$$
\bar x = \_\_\_\_\_\_
$$
</div>

<details markdown="1"><summary>Solution</summary>

The line through <span class="math-inline">\\((-4,5)\\)</span> and <span class="math-inline">\\((8,14)\\)</span> has slope

<div class="math-display">
$$
w_1^*=\frac{14-5}{8-(-4)}=\frac{9}{12}=\frac34
$$
</div>

 Using <span class="math-inline">\\(h(-4)=5\\)</span>,

<div class="math-display">
$$
5=w_0^*+\frac34(-4)=w_0^*-3
$$
</div>

 so <span class="math-inline">\\(w&#95;0^{\ast}=8\\)</span>, and the fit model is <span class="math-inline">\\(h(x&#95;i) = 8 + \frac{3}{4}x&#95;i\\)</span>.

For simple linear regression with an intercept, the fit line passes through <span class="math-inline">\\((\bar x,\bar y)\\)</span>. Since <span class="math-inline">\\(\bar y=2\\)</span>,

<div class="math-display">
$$
2=8+\frac34\bar x \implies \bar x = -8
$$
</div>

 which gives <span class="math-inline">\\(\boxed{\bar x=-8}\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Suppose the correlation coefficient between the <span class="math-inline">\\(x\\)</span>-values and <span class="math-inline">\\(y\\)</span>-values is <span class="math-inline">\\(r = 1/3\\)</span>.

The standard deviation of <span class="math-inline">\\(y\\)</span>, <span class="math-inline">\\(\sigma&#95;y\\)</span>, is <span class="math-inline">\\(c\\)</span> times the standard deviation of <span class="math-inline">\\(x\\)</span>, <span class="math-inline">\\(\sigma&#95;x\\)</span>. In other words,

<div class="math-display">
$$
\sigma_y = c \sigma_x
$$
</div>

 What is the value of <span class="math-inline">\\(c\\)</span>?

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1/4\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(4/9\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(3/4\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(9/4\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(3\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(4\\)</span></span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1/4\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(4/9\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(3/4\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(9/4\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(3\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(4\\)</span></span></div>

For simple linear regression, one (of the many equivalent) formula for the slope <span class="math-inline">\\(w&#95;1^{\ast}\\)</span> is

<div class="math-display">
$$
w_1^*=r\frac{\sigma_y}{\sigma_x}
$$
</div>

 From part **a)**, <span class="math-inline">\\(w&#95;1^{\ast}=\frac34\\)</span>. Since <span class="math-inline">\\(r=\frac13\\)</span> and <span class="math-inline">\\(\sigma&#95;y=c\sigma&#95;x\\)</span>,

<div class="math-display">
$$
\frac34=\frac13c
$$
</div>

 so <span class="math-inline">\\(\boxed{c=\frac94}\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Let <span class="math-inline">\\(e&#95;i=y&#95;i-h(x&#95;i)\\)</span> be the fit model's error for the <span class="math-inline">\\(i\\)</span>th point. Note that <span class="math-inline">\\(e&#95;i\\)</span> may either be positive or negative. Which of the following statements are **guaranteed** to be true? **Select all** that apply.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle\sum&#95;{i=1}^n e&#95;i=0\\)</span></span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle\sum&#95;{i=1}^n x&#95;i e&#95;i=0\\)</span></span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle\sum&#95;{i=1}^n y&#95;i e&#95;i=0\\)</span></span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle\sum&#95;{i=1}^n e&#95;i (x&#95;i - \bar x)=0\\)</span></span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-square mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle\sum&#95;{i=1}^n e&#95;i=0\\)</span></span><span class="mc-option"><span class="mc-square mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle\sum&#95;{i=1}^n x&#95;i e&#95;i=0\\)</span></span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle\sum&#95;{i=1}^n y&#95;i e&#95;i=0\\)</span></span><span class="mc-option"><span class="mc-square mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle\sum&#95;{i=1}^n e&#95;i (x&#95;i - \bar x)=0\\)</span></span></div>

How did we find <span class="math-inline">\\(w&#95;0^{\ast}\\)</span> and <span class="math-inline">\\(w&#95;1^{\ast}\\)</span>? By minimizing mean squared error:

<div class="math-display">
$$
R_\text{sq}(w_0, w_1) = \frac{1}{n} \sum_{i=1}^n (y_i - (w_0 + w_1 x_i))^2
$$
</div>

To do so, we took the partial derivatives with respect to <span class="math-inline">\\(w&#95;0\\)</span> and <span class="math-inline">\\(w&#95;1\\)</span> and set them equal to 0:

<div class="math-display">
$$
\frac{\partial R_\text{sq}}{\partial w_0} = \frac{1}{n} \sum_{i=1}^n -2(y_i - (w_0 + w_1 x_i)) = 0
$$
</div>



<div class="math-display">
$$
\frac{\partial R_\text{sq}}{\partial w_1} = \frac{1}{n} \sum_{i=1}^n -2x_i(y_i - (w_0 + w_1 x_i)) = 0
$$
</div>

Solving these equations gave us <span class="math-inline">\\(w&#95;0^{\ast}\\)</span> and <span class="math-inline">\\(w&#95;1^{\ast}\\)</span>. But if we take a closer look, these equations are telling us properties about the errors, <span class="math-inline">\\(e&#95;i = y&#95;i - h(x&#95;i) = y&#95;i - (w&#95;0 + w&#95;1 x&#95;i)\\)</span>. Above, I'll substitute in <span class="math-inline">\\(e&#95;i\\)</span> every time I see a <span class="math-inline">\\(y&#95;i - (w&#95;0 + w&#95;1 x&#95;i)\\)</span>.

The first equation becomes

<div class="math-display">
$$
\frac{1}{n} \sum_{i=1}^n -2e_i = 0 \implies \sum_{i=1}^n e_i = 0
$$
</div>

and the second equation becomes

<div class="math-display">
$$
\frac{1}{n} \sum_{i=1}^n -2x_i e_i = 0 \implies \sum_{i=1}^n x_i e_i = 0
$$
</div>

So, hidden in plain sight were these properties about the errors! Recall, the four options in this question are:

-   <span class="math-inline">\\(\displaystyle\sum&#95;{i=1}^n e&#95;i=0\\)</span>

-   <span class="math-inline">\\(\displaystyle\sum&#95;{i=1}^n x&#95;i e&#95;i=0\\)</span>

-   <span class="math-inline">\\(\displaystyle\sum&#95;{i=1}^n y&#95;i e&#95;i=0\\)</span>

-   <span class="math-inline">\\(\displaystyle\sum&#95;{i=1}^n e&#95;i(x&#95;i-\bar x)=0\\)</span>

So, we know the first two are true.

What about the third option, <span class="math-inline">\\(\displaystyle\sum&#95;{i=1}^n y&#95;i e&#95;i=0\\)</span>? The short answer is that there's no reason to believe this is true; if it were, it would have emerged from our analysis above. To be sure that it's not true, let's find a counterexample.

We know that <span class="math-inline">\\(y&#95;i = h(x&#95;i) + e&#95;i\\)</span>, so

<div class="math-display">
$$
\sum_{i=1}^n y_i e_i = \sum_{i=1}^n (h(x_i) + e_i) e_i = \sum_{i=1}^n h(x_i) e_i + \sum_{i=1}^n e_i^2
$$
</div>

This is only <span class="math-inline">\\(0\\)</span> when the fit line has zero error on every point. So, the third option is not guaranteed to be true.

Finally, let's look at the fourth option, <span class="math-inline">\\(\sum&#95;{i=1}^n e&#95;i(x&#95;i-\bar x)=0\\)</span>. This is true, because the first two options are true:

<div class="math-display">
$$
\sum_{i=1}^n e_i(x_i-\bar x)=\sum_{i=1}^n e_i x_i -\sum_{i=1}^n e_i \bar x = 0 - \bar x \sum_{i=1}^n e_i = 0
$$
</div>

 The statement <span class="math-inline">\\(\sum&#95;{i=1}^n y&#95;i e&#95;i=0\\)</span> is not guaranteed; in fact, since <span class="math-inline">\\(y&#95;i=h(x&#95;i)+e&#95;i\\)</span>,

<div class="math-display">
$$
\sum_{i=1}^n y_i e_i=\sum_{i=1}^n h(x_i)e_i+\sum_{i=1}^n e_i^2=\sum_{i=1}^n e_i^2
$$
</div>

 which is only <span class="math-inline">\\(0\\)</span> when the fit line has zero error on every point, i.e. passes through every single point.

**Above, you may be wondering why it's the case that**

<div class="math-display">
$$
\sum_{i = 1}^n h(x_i) e_i = 0
$$
</div>

Intentionally, I haven't provided the proof of this! I want you to piece the proof together. Start by using the fact that the first two options in this question are true.
</details>

</div>
</div>

</div>

---

## SP26 Final · Problem 2 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">9 pts</span> <span class="badge" data-flag="mt1-redemption" style="background-color: #9A3324; color: #FFFFFF; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">MT1 Redemption</span>

<p class="worksheet-source">From <a href="/exams/sp26-final/">SP26 Final</a></p>

Suppose we fit a simple linear regression model to a dataset of <span class="math-inline">\\(n\\)</span> points, <span class="math-inline">\\((x&#95;1,y&#95;1),(x&#95;2,y&#95;2),\ldots,(x&#95;n,y&#95;n)\\)</span>, by minimizing mean squared error. Let <span class="math-inline">\\(\bar x\\)</span> and <span class="math-inline">\\(\bar y\\)</span> be the means of the <span class="math-inline">\\(x\\)</span>-values and <span class="math-inline">\\(y\\)</span>-values, respectively, and suppose the standard deviations <span class="math-inline">\\(\sigma&#95;x\\)</span> and <span class="math-inline">\\(\sigma&#95;y\\)</span> are both positive. Let

<div class="math-display">
$$
h(x_i)=w_0^*+w_1^*x_i
$$
</div>

 be the best simple linear regression line for the original dataset.

Now, we create a new dataset of <span class="math-inline">\\(n+1\\)</span> points by starting with the original dataset and adding one new point,

<div class="math-display">
$$
(x_{n+1},y_{n+1})=(\bar x,c)
$$
</div>

 where <span class="math-inline">\\(c\\)</span> is a constant. Let

<div class="math-display">
$$
h_{\text{new}}(x_i)=w_0'+w_1'x_i
$$
</div>

 be the best simple linear regression line for the new dataset.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Prove that <span class="math-inline">\\(w&#95;1' = w&#95;1^{\ast}\\)</span>, i.e. that the new slope is the same as the old slope, no matter what <span class="math-inline">\\(c\\)</span> is. <em>Hint: Start with any of the formulas for the optimal slope that involve summations in the numerator and denominator, and separate the sums.</em>

<details markdown="1"><summary>Solution</summary>

The optimal slope for simple linear regression can be written as

<div class="math-display">
$$
w_1^*
=
\frac{\sum_{i=1}^n (x_i-\bar{x})y_i}{\sum_{i=1}^n (x_i-\bar{x}) x_i}
$$
</div>

 as derived in [Chapter 2.3](https://notes.eecs245.org/simple-linear-regression/finding-optimal-parameters/). There are several other equivalent formulas, e.g. with <span class="math-inline">\\(\sum&#95;{i=1}^n (x&#95;i-\bar{x})(y&#95;i-\bar{y})\\)</span> on the numerator, but this one keeps the algebra simplest, as it doesn't require us to think about the new value of <span class="math-inline">\\(\bar y\\)</span>.

For the new dataset, the mean of the <span class="math-inline">\\(x\\)</span>-values is still <span class="math-inline">\\(\bar{x}\\)</span>, since

<div class="math-display">
$$
\bar{x}'=\frac{n\bar{x}+\bar{x}}{n+1}=\bar{x}
$$
</div>

 The denominator of the new slope is therefore

<div class="math-display">
$$
\sum_{i=1}^{n+1}(x_i-\bar{x}')x_i
=
\sum_{i=1}^n(x_i-\bar{x})x_i + (\bar{x}-\bar{x})\bar{x}
=
\sum_{i=1}^n(x_i-\bar{x})x_i
$$
</div>

 The numerator of the new slope is

<div class="math-display">
$$
\begin{align*}
\sum_{i=1}^{n+1}(x_i-\bar{x}')y_i
&=
\sum_{i=1}^{n}(x_i-\bar{x})y_i
+(\bar{x}-\bar{x})c \\\\
&=
\sum_{i=1}^{n}(x_i-\bar{x})y_i
\end{align*}
$$
</div>

So the numerator and denominator in this formula are both unchanged, meaning <span class="math-inline">\\(w&#95;1'=w&#95;1^{\ast}\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> Which of the following expressions is equal to <span class="math-inline">\\(w&#95;0' - w&#95;0^{\ast}\\)</span>, the difference between the new intercept and the old intercept?

<span class="mc-bubble" aria-hidden="true"></span> None of these

<details markdown="1"><summary>Solution</summary>

<span class="mc-bubble" aria-hidden="true"></span> None of these

The intercept of the optimal simple linear regression line is

<div class="math-display">
$$
w_0^* = \bar{y}-w_1^*\bar{x}
$$
</div>

 The new <span class="math-inline">\\(x\\)</span>-mean is still <span class="math-inline">\\(\bar{x}\\)</span>, and part **a)** showed that the new slope is still <span class="math-inline">\\(w&#95;1^{\ast}\\)</span>. The new <span class="math-inline">\\(y\\)</span>-mean is

<div class="math-display">
$$
\bar{y}'=\frac{n\bar{y}+c}{n+1}
$$
</div>

 So,

<div class="math-display">
$$
\begin{align*}
w_0'-w_0^*
&=
(\bar{y}'-w_1^*\bar{x})-(\bar{y}-w_1^*\bar{x}) \\\\
&= \bar{y}'-\bar{y} \\\\
&= \frac{n\bar{y}+c}{n+1}-\bar{y} \\\\
&= \frac{c-\bar{y}}{n+1}
\end{align*}
$$
</div>

</details>

</div>
</div>

</div>

---

## More practice (PDF only)

- [MOCK MT1 Problem 3](/resources/exams/mock-mt1.pdf#page=6)

{% endraw %}
