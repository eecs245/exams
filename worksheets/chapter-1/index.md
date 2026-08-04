---
layout: minimal
title: "Chapter 1: Introduction to Supervised Learning"
description: "Practice problems for Chapter 1: Introduction to Supervised Learning."
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

# Chapter 1: Introduction to Supervised Learning

*Topics: squared loss and the constant model, absolute loss, comparing loss functions*

*Problems below are collected from past exams; each links back to its full exam. Solutions are in the dropdowns.*

## Problems

- [FA25 MT1 · Problem 1](#fa25-mt1--problem-1-consider-the-following-15-pts)
- [FA25 MT1 · Problem 2](#fa25-mt1--problem-2-absolute-madness-17-pts)
- [FA25 Final · Problem 1](#fa25-final--problem-1-10-pts-mt1-redemption)
- [WN26 MT1 · Problem 1](#wn26-mt1--problem-1-16-pts)
- [WN26 MT1 · Problem 7](#wn26-mt1--problem-7-20-pts)
- [WN26 Final · Problem 1](#wn26-final--problem-1-12-pts-mt1-redemption)
- [SP26 MT1 · Problem 1](#sp26-mt1--problem-1-16-pts)
- [SP26 MT1 · Problem 2](#sp26-mt1--problem-2-10-pts)
- [SP26 Final · Problem 1](#sp26-final--problem-1-14-pts-mt1-redemption)

---

## FA25 MT1 · Problem 1: Consider the Following\... <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">15 pts</span>

<p class="worksheet-source">From <a href="/exams/fa25-mt1/">FA25 MT1</a></p>


Consider the following dataset of <span class="math-inline">\\(n = 9\\)</span> values.

| <span class="math-inline">\\(y&#95;1\\)</span> | <span class="math-inline">\\(y&#95;2\\)</span> | <span class="math-inline">\\(y&#95;3\\)</span> | <span class="math-inline">\\(y&#95;4\\)</span> | <span class="math-inline">\\(y&#95;5\\)</span> | <span class="math-inline">\\(y&#95;6\\)</span> | <span class="math-inline">\\(y&#95;7\\)</span> | <span class="math-inline">\\(y&#95;8\\)</span> | <span class="math-inline">\\(y&#95;9\\)</span> |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| <span class="math-inline">\\(7\\)</span> | <span class="math-inline">\\(8\\)</span> | <span class="math-inline">\\(10\\)</span> | <span class="math-inline">\\(10\\)</span> | <span class="math-inline">\\(11\\)</span> | <span class="math-inline">\\(13\\)</span> | <span class="math-inline">\\(14\\)</span> | <span class="math-inline">\\(17\\)</span> | <span class="math-inline">\\(27\\)</span> |

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

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 1</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 2</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 3</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 4</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 5</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> N/A</span></div>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(2.5 pts) **11** is the value of <span class="math-inline">\\(w\\)</span> that minimizes\...

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 1</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 2</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 3</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 4</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 5</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> N/A</span></div>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(2.5 pts) **12** is the value of <span class="math-inline">\\(w\\)</span> that minimizes\...

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 1</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 2</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 3</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 4</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 5</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> N/A</span></div>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
(2.5 pts) **13** is the value of <span class="math-inline">\\(w\\)</span> that minimizes\...

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 1</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 2</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 3</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 4</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 5</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> N/A</span></div>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">e)</div>
<div class="assignment-part-content" markdown="1">
(2.5 pts) **17** is the value of <span class="math-inline">\\(w\\)</span> that minimizes\...

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 1</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 2</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 3</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 4</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 5</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> N/A</span></div>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">f)</div>
<div class="assignment-part-content" markdown="1">
(2.5 pts) **27** is the value of <span class="math-inline">\\(w\\)</span> that minimizes\...

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 1</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 2</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 3</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 4</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 5</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> N/A</span></div>

</div>
</div>

</div>


---

## FA25 MT1 · Problem 2: Absolute Madness <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">17 pts</span>

<p class="worksheet-source">From <a href="/exams/fa25-mt1/">FA25 MT1</a></p>


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

<span class="mc-bubble" aria-hidden="true"></span> The value of <span class="math-inline">\\(w^{\ast}\\)</span> is unique, and is equal to \_\_\_\_\_\_.

<span class="mc-bubble" aria-hidden="true"></span> The value of <span class="math-inline">\\(w^{\ast}\\)</span> is not unique; any value between \_\_\_\_\_\_ and \_\_\_\_\_\_ is a minimizer.

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

## FA25 Final · Problem 1 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">10 pts</span> <span class="badge" data-flag="mt1-redemption" style="background-color: #9A3324; color: #FFFFFF; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">MT1 Redemption</span>

<p class="worksheet-source">From <a href="/exams/fa25-final/">FA25 Final</a></p>


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
<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(10\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(15\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(20\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(30\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(40\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(60\\)</span></span></div>

2.  Justify your answer in the box below.

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(10\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(15\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(20\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(30\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(40\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(60\\)</span></span></div>

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

<span class="math-inline">\\(\text{minimizer} = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>

<details markdown="1"><summary>Solution</summary>

The minimizer of mean absolute error is the median of the dataset. When the number of data points is even, any value between the middle two values, inclusive, minimizes mean absolute error. Here, any value between 3 and 5 inclusive minimizes mean absolute error; the value <span class="math-inline">\\(\boxed{4}\\)</span> is the only integer in this range that isn't in the dataset itself, so it is the minimizer we're looking for.
</details>

</div>
</div>

</div>


---

## WN26 MT1 · Problem 1 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">16 pts</span>

<p class="worksheet-source">From <a href="/exams/wn26-mt1/">WN26 MT1</a></p>


Consider a dataset of <span class="math-inline">\\(n\\)</span> values, <span class="math-inline">\\(y&#95;1, y&#95;2, \ldots, y&#95;n\\)</span>, with:

-   a mean of <span class="math-inline">\\(\bar{y} = 18\\)</span>

-   a median of 15

-   a standard deviation of <span class="math-inline">\\(\sigma&#95;y = 7\\)</span>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> In the space provided, sketch the graph of <span class="math-inline">\\(R&#95;\text{sq}(w)\\)</span>, the mean squared error of a constant prediction <span class="math-inline">\\(w\\)</span> on the dataset. For full credit:

-   The shape of the graph must be correct.

-   You must clearly label the coordinates of the **minimum point** on the graph.

<div style="text-align: center;">
<img src="/exams/wn26-mt1/imgs/w_r_axes.png" alt="image" style="width: 70%; max-width: 100%;">
</div>

<details markdown="1"><summary>Solution</summary>

<div style="text-align: center;">
<img src="/exams/wn26-mt1/imgs/w_r_axes_solution.png" alt="image" style="width: 90%; max-width: 100%;">
</div>

Recall that

<div class="math-display">
$$
R_\text{sq}(w) = \frac{1}{n} \sum_{i=1}^n (y_i - w)^2
$$
</div>

is a parabola, minimized at <span class="math-inline">\\(w = \bar y\\)</span>. When <span class="math-inline">\\(w = \bar y\\)</span>,

<div class="math-display">
$$
R_\text{sq}(w) = \frac{1}{n} \sum_{i=1}^n (y_i - \bar y)^2 = \sigma_y^2
$$
</div>

 is the variance of the dataset. Here, the mean is 18 and the variance is 49, so the minimum point is at <span class="math-inline">\\((18, 49)\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Which of the following quantities is **guaranteed** to be equal to 0? Select all that apply.

<span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \frac{1}{n} \sum&#95;{i=1}^n (y&#95;i - 15)\\)</span>

<span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \frac{1}{n} \sum&#95;{i=1}^n (y&#95;i - 18)\\)</span>

<span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \frac{1}{n}\sum&#95;{i=1}^n (y&#95;i - 15)^2\\)</span>

<span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \frac{1}{n}\sum&#95;{i=1}^n (y&#95;i - 18)^2\\)</span>

<span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \frac{1}{n}\sum&#95;{i=1}^n (y&#95;i - 15)^2 - 7^2\\)</span>

<span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \frac{1}{n}\sum&#95;{i=1}^n (y&#95;i - 18)^2 - 7^2\\)</span>

<details markdown="1"><summary>Solution</summary>

<span class="mc-square mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \frac{1}{n}\sum&#95;{i=1}^n (y&#95;i - 18)^2 - 7^2\\)</span>

There are two key ideas at play here:

-   The mean is the unique point in the dataset such that the sum of deviations from the mean is 0. In other words,

<div class="math-display">
$$
\sum_{i=1}^n (y_i - \bar y) = \sum_{i=1}^n y_i - n \bar y = n \bar y - n \bar y = 0
$$
</div>

-   The variance of a dataset is the average of the squared deviations from the mean. In other words,

<div class="math-display">
$$
\sigma_y^2 = \frac{1}{n} \sum_{i=1}^n (y_i - \bar y)^2
$$
</div>

 Equivalently, this is the value of <span class="math-inline">\\(R&#95;\text{sq}(w)\\)</span> when <span class="math-inline">\\(w = \bar y\\)</span>.

With this in mind, let's look at the options:

**(i)** (**False**) <span class="math-inline">\\(\displaystyle \frac{1}{n} \sum&#95;{i=1}^n (y&#95;i - 15)\\)</span>: This is the average of the deviations from the median, which is not 0. This is only true for the mean.

**(ii)** (**True**) <span class="math-inline">\\(\displaystyle \frac{1}{n} \sum&#95;{i=1}^n (y&#95;i - 18)\\)</span>: This is the average of the deviations from the mean, which is 0. This is only true for the mean.

**(iii)** (**False**) <span class="math-inline">\\(\displaystyle \frac{1}{n}\sum&#95;{i=1}^n (y&#95;i - 15)^2\\)</span>: This is the function <span class="math-inline">\\(R&#95;\text{sq}(w)\\)</span> when <span class="math-inline">\\(w = 15\\)</span>. As we see in the solution to part **a)**, this is not 0.

**(iv)** (**False**) <span class="math-inline">\\(\displaystyle \frac{1}{n}\sum&#95;{i=1}^n (y&#95;i - 18)^2\\)</span>: This is the function <span class="math-inline">\\(R&#95;\text{sq}(w)\\)</span> when <span class="math-inline">\\(w = 18\\)</span>, i.e. it is the variance of the dataset. As we see in the solution to part **a)**, this is also not zero --- here, it is <span class="math-inline">\\(\sigma&#95;y^2 = 7^2 = 49\\)</span>. One point of confusion may be that <span class="math-inline">\\(w = \bar{y}\\)</span> is the point at which <span class="math-inline">\\(R&#95;\text{sq}(w)\\)</span> is minimized and <span class="math-inline">\\(R&#95;\text{sq}(w)\\)</span> has a **derivative** of 0, but <span class="math-inline">\\(R&#95;\text{sq}(\bar y) \neq 0\\)</span> in general.

**(v)** (**False**) <span class="math-inline">\\(\displaystyle \frac{1}{n}\sum&#95;{i=1}^n (y&#95;i - 15)^2 - 7^2\\)</span>: This would be true if the 15 were replaced with the mean, 18, but it is not.

**(vi)** (**True**) <span class="math-inline">\\(\displaystyle \frac{1}{n}\sum&#95;{i=1}^n (y&#95;i - 18)^2 - 7^2\\)</span>: This is the variance of the dataset minus the variance of the dataset, which indeed is 0.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Recall that <span class="math-inline">\\(R&#95;\text{abs}(w)\\)</span> is the mean absolute error of a constant prediction <span class="math-inline">\\(w\\)</span> on the dataset. A snippet of the graph of <span class="math-inline">\\(R&#95;\text{abs}(w)\\)</span> is shown below.

<div style="text-align: center;">
<img src="/exams/wn26-mt1/imgs/line_graph_gray.png" alt="image" style="width: 50%; max-width: 100%;">
</div>

For clarity, the circles at <span class="math-inline">\\((15, 4)\\)</span>, <span class="math-inline">\\((18, 5)\\)</span>, and <span class="math-inline">\\((22, 7)\\)</span> indicate the points at which the slope of <span class="math-inline">\\(R&#95;\text{abs}(w)\\)</span> changes.

Given that there are <span class="math-inline">\\(n = 72\\)</span> values in the dataset, how many values in the dataset are equal to **18**? Show your work and <span class="math-inline">\\(\boxed{\text{circle}}\\)</span> your final answer, which should be an integer with no variables.

<details markdown="1"><summary>Solution</summary>

The number of values in the dataset that are equal to 18 is 6.

Recall, the slope of <span class="math-inline">\\(R&#95;\text{abs}(w)\\)</span> at any <span class="math-inline">\\(w\\)</span> that is not a data point is:

<div class="math-display">
$$
\frac{\text{d}}{\text{d}w} R_\text{abs}(w) = \frac{\# \text{ left of } w - \# \text{ right of } w}{n}
$$
</div>

There are two line segments of interest here: the one between <span class="math-inline">\\(w=15\\)</span> and <span class="math-inline">\\(w=18\\)</span>, and the one between <span class="math-inline">\\(w=18\\)</span> and <span class="math-inline">\\(w=22\\)</span>. We have two ways of computing the slope of each one: by using <span class="math-inline">\\(\text{slope} = \frac{\text{change in } y}{\text{change in } x}\\)</span> and by using the formula above. We'll use both formulas on each line segment.

-   **Between <span class="math-inline">\\(w=15\\)</span> and <span class="math-inline">\\(w=18\\)</span>:**

-   Method 1: Using <span class="math-inline">\\(\text{slope} = \frac{\text{change in } y}{\text{change in } x}\\)</span>, the graph rises from <span class="math-inline">\\((15, 4)\\)</span> to <span class="math-inline">\\((18, 5)\\)</span>, which gives a slope of



<div class="math-display">
$$
s_1 = \frac{5 - 4}{18 - 15} = \frac{1}{3}
$$
</div>

-   Method 2: Using the formula for the slope of <span class="math-inline">\\(R&#95;\text{abs}(w)\\)</span>, let <span class="math-inline">\\(l\\)</span> be the number of values in the dataset less than or equal to 15. Then, the slope in this interval is



<div class="math-display">
$$
s_1 = \frac{l - (72 - l)}{72} = \frac{2l - 72}{72}
$$
</div>

   At this point, we have enough information to solve for <span class="math-inline">\\(l\\)</span>:



<div class="math-display">
$$
\frac{2l - 72}{72} = \frac{1}{3} \implies l = 48
$$
</div>

-   **Between <span class="math-inline">\\(w=18\\)</span> and <span class="math-inline">\\(w=22\\)</span>:**

-   Method 1:

<div class="math-display">
$$
s_2 = \frac{7 - 5}{22 - 18} = \frac{2}{4} = \frac{1}{2}
$$
</div>

-   Method 2: Let <span class="math-inline">\\(k\\)</span> be the number of values in the dataset **equal to** 18. Ultimately, this is what we're trying to find. Then, the number of values in the dataset less than or equal to 18 is <span class="math-inline">\\(l + k\\)</span>. In this interval, the slope is



<div class="math-display">
$$
s_2 = \frac{(l + k) - (72 - (l + k))}{72} = \frac{2(l + k) - 72}{72}
$$
</div>

   So, we need to solve for <span class="math-inline">\\(k\\)</span> in



<div class="math-display">
$$
\frac{2(l + k) - 72}{72}
$$
</div>

   But, we know that <span class="math-inline">\\(l = 48\\)</span>, so



<div class="math-display">
$$
\frac{2(48 + k) - 72}{72} = \frac{1}{2} \implies 96 + 2k - 72 = 36 \implies 2k = 12 \implies \boxed{k = 6}
$$
</div>

Therefore, there are 6 values in the dataset that are equal to 18.
</details>

</div>
</div>

</div>


---

## WN26 MT1 · Problem 7 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">20 pts</span>

<p class="worksheet-source">From <a href="/exams/wn26-mt1/">WN26 MT1</a></p>


Suppose we'd like to find the optimal constant parameter, <span class="math-inline">\\(w^{\ast}\\)</span>, for the constant model <span class="math-inline">\\(h(x&#95;i) = w\\)</span>, given a dataset of <span class="math-inline">\\(n\\)</span> points <span class="math-inline">\\((x&#95;1, y&#95;1), (x&#95;2, y&#95;2), \ldots, (x&#95;n, y&#95;n)\\)</span>. To do so, we use the **sub-squared** loss function, <span class="math-inline">\\(L&#95;\text{ss}\\)</span>, defined below.

<div class="math-display">
$$
L_\text{ss}(y_i, w) = (\sqrt{y_i} - \sqrt{w})^2
$$
</div>

This requires us to assume that all <span class="math-inline">\\(y&#95;i \ge 0\\)</span>, as are all possible values of <span class="math-inline">\\(w\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Find <span class="math-inline">\\(\frac{\text{d}}{\text{d}w} R&#95;\text{ss}(w)\\)</span>, the derivative of **average** sub-squared loss (i.e. the empirical risk) with respect to <span class="math-inline">\\(w\\)</span>. Show your work and <span class="math-inline">\\(\boxed{\text{circle}}\\)</span> your final answer, which should be an expression in terms of the <span class="math-inline">\\(y&#95;i\\)</span>'s, <span class="math-inline">\\(n\\)</span>, and/or any constants. <em>Hint: The derivative of <span class="math-inline">\\(f(x) = \sqrt{x}\\)</span> is <span class="math-inline">\\(\frac{\text{d}}{\text{d}x} \sqrt{x} = \frac{1}{2\sqrt{x}}\\)</span>.</em>

<details markdown="1"><summary>Solution</summary>

The definition of average sub-squared loss is

<div class="math-display">
$$
R_\text{ss}(w) = \frac{1}{n} \sum_{i=1}^n L_\text{ss}(y_i, w) = \frac{1}{n} \sum_{i=1}^n (\sqrt{y_i} - \sqrt{w})^2
$$
</div>

Then,

<div class="math-display">
$$
\begin{align*}
\frac{\text{d}}{\text{d}w} R_\text{ss}(w)
&= \frac{\text{d}}{\text{d}w} \left( \frac{1}{n} \sum_{i=1}^n (\sqrt{y_i} - \sqrt{w})^2 \right) \\\\
&= \frac{1}{n} \sum_{i=1}^n \frac{\text{d}}{\text{d}w} \left[(\sqrt{y_i} - \sqrt{w})^2\right] \\\\
&= \frac{1}{n} \sum_{i=1}^n 2(\sqrt{y_i} - \sqrt{w}) \cdot \frac{\text{d}}{\text{d}w} (\sqrt{y_i} - \sqrt{w}) \\\\
&= \frac{1}{n} \sum_{i=1}^n 2(\sqrt{y_i} - \sqrt{w}) \cdot \left(0 -\frac{1}{2\sqrt{w}} \right) \\\\
&= \boxed{-\frac{1}{n} \sum_{i=1}^n \frac{\sqrt{y_i} - \sqrt{w}}{\sqrt{w}}}
\end{align*}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Show that the value of <span class="math-inline">\\(w^{\ast}\\)</span> that minimizes average sub-squared loss is

<div class="math-display">
$$
\displaystyle w^* = \left( \frac{1}{n} \sum_{i=1}^n \sqrt{y_i} \right)^2
$$
</div>

<details markdown="1"><summary>Solution</summary>

We've found that

<div class="math-display">
$$
\frac{\text{d}}{\text{d}w} R_\text{ss}(w) = -\frac{1}{n} \sum_{i=1}^n \frac{\sqrt{y_i} - \sqrt{w}}{\sqrt{w}}
$$
</div>

To find <span class="math-inline">\\(w^{\ast}\\)</span>, we need to set this expression equal to 0 and solve for <span class="math-inline">\\(w\\)</span>.

<div class="math-display">
$$
\begin{align*}
-\frac{1}{n} \sum_{i=1}^n \frac{\sqrt{y_i} - \sqrt{w}}{\sqrt{w}} = 0 \\\\
\sum_{i=1}^n \frac{\sqrt{y_i} - \sqrt{w}}{\sqrt{w}} = 0 \\\\
\sum_{i=1}^n (\sqrt{y_i} - \sqrt{w}) = 0 \\\\
\sum_{i=1}^n \sqrt{y_i} - n \sqrt{w} = 0 \\\\
\sqrt{w} = \frac{1}{n} \sum_{i=1}^n \sqrt{y_i} \\\\
w = \left( \frac{1}{n} \sum_{i=1}^n \sqrt{y_i} \right)^2
\end{align*}
$$
</div>

So, the value of <span class="math-inline">\\(w^{\ast}\\)</span> that minimizes average sub-squared loss is

<div class="math-display">
$$
\boxed{w^* = \left( \frac{1}{n} \sum_{i=1}^n \sqrt{y_i} \right)^2}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Using the Cauchy-Schwarz inequality, prove that

<div class="math-display">
$$
\left( \frac{1}{n} \sum_{i=1}^n \sqrt{y_i} \right)^2 \leq \bar{y}
$$
</div>

where <span class="math-inline">\\(\bar{y}\\)</span> is the mean of the <span class="math-inline">\\(y&#95;i\\)</span>'s.

<em>Solutions that do not use the Cauchy-Schwarz inequality will not receive credit.</em>

<details markdown="1"><summary>Solution</summary>

The Cauchy-Schwarz inequality states that

<div class="math-display">
$$
\left| \vec u \cdot \vec v \right| \leq \lVert \vec u \rVert \lVert \vec v \rVert
$$
</div>

for any two vectors <span class="math-inline">\\(\vec u, \vec v \in \mathbb{R}^n\\)</span>. The problem boils down to constructing <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> such that the Cauchy-Schwarz inequality, for that <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span>, implies the inequality we're trying to prove.

For hints on how to proceed, let's expand the definition of <span class="math-inline">\\(\bar y\\)</span> in the inequality we're trying to prove.

<div class="math-display">
$$
\left( \frac{1}{n} \sum_{i=1}^n \sqrt{y_i} \right)^2 \leq \frac{1}{n} \sum_{i=1}^n y_i
$$
</div>

On the left, we have a sum of <span class="math-inline">\\(\sqrt{y&#95;i}\\)</span>'s, and on the right, we have a sum of <span class="math-inline">\\(y&#95;i\\)</span>'s. We know that in the norm of a vector, the individual components are squared, which would allow us to turn <span class="math-inline">\\(\sqrt{y&#95;i}\\)</span> into <span class="math-inline">\\(y&#95;i\\)</span>. So, one possible path forward is

<div class="math-display">
$$
\vec u = \begin{bmatrix} \sqrt{y_1} \\\\ \sqrt{y_2} \\\\ \vdots \\\\ \sqrt{y_n} \end{bmatrix}, \qquad \vec v = \begin{bmatrix} 1 \\\\ 1 \\\\ \vdots \\\\ 1 \end{bmatrix}
$$
</div>

The dot product of <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> is <span class="math-inline">\\(\sum&#95;{i=1}^n \sqrt{y&#95;i}\\)</span>, which seems promising. Let's plug <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> into the Cauchy-Schwarz inequality and see what we get.

<div class="math-display">
$$
\begin{align*}
\left| \vec u \cdot \vec v \right| &\leq \lVert \vec u \rVert \lVert \vec v \rVert \\\\
\left| \sum_{i=1}^n \sqrt{y_i} \right| &\leq \left \lVert \begin{bmatrix} \sqrt{y_1} \\\\ \sqrt{y_2} \\\\ \vdots \\\\ \sqrt{y_n} \end{bmatrix} \right \rVert \left \lVert \begin{bmatrix} 1 \\\\ 1 \\\\ \vdots \\\\ 1 \end{bmatrix} \right \rVert \\\\
\sum_{i=1}^n \sqrt{y_i} &\leq \sqrt{\sum_{i=1}^n y_i} \sqrt{n} \\\\
\end{align*}
$$
</div>

Seems like we're getting somewhere. Let's square both sides.

<div class="math-display">
$$
\begin{align*}
\left( \sum_{i=1}^n \sqrt{y_i} \right)^2 &\leq \left( \sqrt{\sum_{i=1}^n y_i} \sqrt{n} \right)^2 \\\\
\left( \sum_{i=1}^n \sqrt{y_i} \right)^2 & \leq n\sum_{i=1}^n y_i
\end{align*}
$$
</div>

Now, all that's left is to divide both sides by <span class="math-inline">\\(n^2\\)</span>.

<div class="math-display">
$$
\begin{align*}
\left( \sum_{i=1}^n \sqrt{y_i} \right)^2 & \leq n\sum_{i=1}^n y_i \\\\
\frac{\left( \sum_{i=1}^n \sqrt{y_i} \right)^2}{n^2} & \leq \frac{n\sum_{i=1}^n y_i}{n^2} \\\\
\left( \frac{1}{n} \sum_{i=1}^n \sqrt{y_i} \right)^2 & \leq \frac{1}{n} \sum_{i=1}^n y_i
\end{align*}
$$
</div>

This is exactly the inequality we're trying to prove, so we're done!
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">2 pts</span> What is the value of <span class="math-inline">\\(w\\)</span> that minimizes the following function:

<div class="math-display">
$$
R(w) = \frac{1}{n}\sum_{i=1}^n (y_i^4 - w^4)^2
$$
</div>

<em>Hint: This can be done without using any calculus --- don't try and take the derivative.</em>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \left(\frac{1}{n} \sum&#95;{i=1}^n y&#95;i \right)^4\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\left(\displaystyle \frac{1}{n} \sum&#95;{i=1}^n y&#95;i^{1/4}\right)^4\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \left(\frac{1}{n} \sum&#95;{i=1}^n y&#95;i^4 \right)^{1/4}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \left(\frac{1}{n} \sum&#95;{i=1}^n y&#95;i^{1/2} \right)^{1/4}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \left(\frac{1}{n} \sum&#95;{i=1}^n y&#95;i^{4} \right)^{1/2}\\)</span></span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \left(\frac{1}{n} \sum&#95;{i=1}^n y&#95;i \right)^4\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\left(\displaystyle \frac{1}{n} \sum&#95;{i=1}^n y&#95;i^{1/4}\right)^4\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \left(\frac{1}{n} \sum&#95;{i=1}^n y&#95;i^4 \right)^{1/4}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \left(\frac{1}{n} \sum&#95;{i=1}^n y&#95;i^{1/2} \right)^{1/4}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \left(\frac{1}{n} \sum&#95;{i=1}^n y&#95;i^{4} \right)^{1/2}\\)</span></span></div>

The idea here is to make a substitution that reduces the problem to one we've already seen --- the problem of minimizing mean squared error for the constant model.

Let <span class="math-inline">\\(z&#95;i = y&#95;i^4\\)</span>, and let <span class="math-inline">\\(t = w^4\\)</span>. Then,

<div class="math-display">
$$
\frac{1}{n}\sum_{i=1}^n (z_i - t)^2 = \frac{1}{n}\sum_{i=1}^n (y_i^4 - w^4)^2
$$
</div>

What is <span class="math-inline">\\(t^{\ast}\\)</span>, the minimizer of <span class="math-inline">\\(\frac{1}{n}\sum&#95;{i=1}^n (z&#95;i - t)^2\\)</span>? That's <span class="math-inline">\\(\bar{z}\\)</span>, which is

<div class="math-display">
$$
t^* = \bar{z} = \frac{1}{n} \sum_{i=1}^n z_i = \frac{1}{n} \sum_{i=1}^n y_i^4
$$
</div>

But, <span class="math-inline">\\(t = w^4\\)</span>, so <span class="math-inline">\\(w = t^{1/4}\\)</span>, meaning

<div class="math-display">
$$
w^* = \boxed{\left( \frac{1}{n} \sum_{i=1}^n y_i^4 \right)^{1/4}}
$$
</div>

Notice how this relates to parts **a)** and **b)** --- those could have been solved the same way, if you wrote <span class="math-inline">\\(\sqrt{x}\\)</span> as <span class="math-inline">\\(x^{1/2}\\)</span>.
</details>
</div>
</div>

</div>

---

## WN26 Final · Problem 1 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span> <span class="badge" data-flag="mt1-redemption" style="background-color: #9A3324; color: #FFFFFF; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">MT1 Redemption</span>

<p class="worksheet-source">From <a href="/exams/wn26-final/">WN26 Final</a></p>


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

   For (i), the minimizer of mean squared error is the mean, so

<div class="math-display">
$$
w^* = \frac{3+6+6+13}{4} = \boxed{7}
$$
</div>

</details>

2.  (3 pts) What value of <span class="math-inline">\\(w^{\ast}\\)</span> minimizes <span class="math-inline">\\(R(w) = \displaystyle \lim&#95;{p \to \infty} \displaystyle \frac{1}{4} \sum&#95;{i=1}^4 |y&#95;i - w|^p\\)</span>?

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(A\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(B\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(C\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(D\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(E\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(F\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(G\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(H\\)</span></span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(A\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(B\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(C\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(D\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(E\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(F\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(G\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(H\\)</span></span></div>

   For (ii), as <span class="math-inline">\\(p \to \infty\\)</span>, the largest value of <span class="math-inline">\\(|y&#95;i-w|\\)</span> dominates. So we should put <span class="math-inline">\\(w\\)</span> halfway between the smallest and largest data values, as discussed in [Chapter 1.4](https://notes.eecs245.org/introduction-to-supervised-learning/comparing-loss-functions/#beyond-absolute-and-squared-loss).

<div class="math-display">
$$
w^* = \frac{3+13}{2} = \boxed{8}
$$
</div>

</details>

3.  (3 pts) What value of <span class="math-inline">\\(w^{\ast}\\)</span> minimizes <span class="math-inline">\\(R(w) = \displaystyle \frac{1}{4} \sum&#95;{i=1}^4 (\log(y&#95;i) - \log(w))^2\\)</span>?

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(A\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(B\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(C\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(D\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(E\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(F\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(G\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(H\\)</span></span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(A\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(B\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(C\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(D\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(E\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(F\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(G\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(H\\)</span></span></div>

   For (iii), let <span class="math-inline">\\(u=\log(w)\\)</span>. The problem is now asking for the best constant prediction for the transformed values <span class="math-inline">\\(\log(y&#95;i)\\)</span>, so

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

4.  (3 pts) The slope of the graph of <span class="math-inline">\\(R(w) = \displaystyle\frac{1}{4} \sum&#95;{i = 1}^4 |y&#95;i - w|\\)</span> at <span class="math-inline">\\(w = \alpha\\)</span> is <span class="math-inline">\\(-1/2\\)</span>. Among the options above, which could be <span class="math-inline">\\(\alpha\\)</span>?

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(A\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(B\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(C\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(D\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(E\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(F\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(G\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(H\\)</span></span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(A\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(B\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(C\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(D\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(E\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(F\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(G\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(H\\)</span></span></div>

   For (iv), the slope of mean absolute error at any <span class="math-inline">\\(w\\)</span> that is not a data point is



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

## SP26 MT1 · Problem 1 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">16 pts</span>

<p class="worksheet-source">From <a href="/exams/sp26-mt1/">SP26 MT1</a></p>


Suppose we'd like to find the optimal parameter, <span class="math-inline">\\(w^{\ast}\\)</span>, for the constant model <span class="math-inline">\\(h(x&#95;i)=w\\)</span>, using the following dataset of <span class="math-inline">\\(n = 4\\)</span> values, <span class="math-inline">\\(y&#95;1, y&#95;2, y&#95;3, y&#95;4\\)</span>:

<div class="math-display">
$$
0, \quad 2, \quad 4, \quad 20
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> First, suppose we find the optimal parameter by minimizing mean squared error, <span class="math-inline">\\(R&#95;\text{sq}(w)\\)</span>. Which value of <span class="math-inline">\\(w\\)</span> minimizes <span class="math-inline">\\(R&#95;\text{sq}(w)\\)</span>? Give your answer as a number with no variables.

<span class="math-inline">\\(\text{minimizer of } R&#95;\text{sq}(w) = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>

<details markdown="1"><summary>Solution</summary>

For the constant model, average squared loss is minimized at the mean of the <span class="math-inline">\\(y&#95;i\\)</span>'s. Here,

<div class="math-display">
$$
\frac{0+2+4+20}{4}=\frac{26}{4}=\boxed{\frac{13}{2}}
$$
</div>

</details>

Now, consider the **clipped** loss function, defined below.

<div class="math-display">
$$
\displaystyle L_\text{clip}(y_i,h(x_i))=\min\{(y_i-h(x_i))^2,9\}
$$
</div>

 For example, <span class="math-inline">\\(L&#95;\text{clip}(10, 5) = 9\\)</span> and <span class="math-inline">\\(L&#95;\text{clip}(5, 3) = 4\\)</span>.

Let <span class="math-inline">\\(R&#95;\text{clip}(w)\\)</span> be the average clipped loss for the constant model and this dataset.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> State one value of <span class="math-inline">\\(w\\)</span> where the derivative of <span class="math-inline">\\(R&#95;\text{clip}(w)\\)</span> is not defined.

<span class="math-inline">\\(\text{one value of } w \text{ where the derivative of } R&#95;\text{clip}(w) \text{ is not defined} =\\)</span> \_\_\_\_\_\_

<details markdown="1"><summary>Solution</summary>

The clipped loss changes formulas whenever

<div class="math-display">
$$
(y_i-w)^2=9
$$
</div>

 Equivalently, this happens when <span class="math-inline">\\(w=y&#95;i\pm 3\\)</span>. Since <span class="math-inline">\\(20-3=17\\)</span>, one valid answer is <span class="math-inline">\\(\boxed{17}\\)</span>.

For context, here's what average clipped loss looks like for this dataset:

<div style="text-align: center;">
<img src="/exams/sp26-mt1/imgs/p1-sol.png" alt="image" style="width: 90%; max-width: 100%;">
</div>
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> Suppose we restrict <span class="math-inline">\\(w\\)</span> to the interval <span class="math-inline">\\(1 \leq w \leq 3\\)</span>. Among all values of <span class="math-inline">\\(w\\)</span> in this interval, which value minimizes <span class="math-inline">\\(R&#95;\text{clip}(w)\\)</span>? Give your answer as a number with no variables.

<span class="math-inline">\\(\text{minimizer of } R&#95;\text{clip}(w) \text{ within the interval } [1, 3] = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>

<details markdown="1"><summary>Solution</summary>

Once <span class="math-inline">\\(w\\)</span> is more than 3 units away from any particular <span class="math-inline">\\(y&#95;i\\)</span> value, the value <span class="math-inline">\\((y&#95;i - w)^2\\)</span> is replaced by the constant <span class="math-inline">\\(9\\)</span> when computing average loss.

What do we know about constants when they are added to functions? **They don't affect the minimizer!** That is, the minimizer of <span class="math-inline">\\(f(x)\\)</span> and of <span class="math-inline">\\(f(x) + c\\)</span> are the same.

What this is saying is that if <span class="math-inline">\\(w\\)</span> is restricted to the interval <span class="math-inline">\\(1 \leq w \leq 3\\)</span>, we can ignore <span class="math-inline">\\(y&#95;4 = 20\\)</span> when computing the minimizer, and this just reduces to minimizing average squared loss (mean squared error) across the data points that are within 3 units of <span class="math-inline">\\(w\\)</span>. As long as <span class="math-inline">\\(1 \leq w \leq 3\\)</span>, we are within 3 units of <span class="math-inline">\\(y&#95;1 = 0\\)</span>, <span class="math-inline">\\(y&#95;2 = 2\\)</span>, and <span class="math-inline">\\(y&#95;3 = 4\\)</span>.

What constant minimizes average squared loss, for the dataset <span class="math-inline">\\(0, 2, 4\\)</span>? That's the mean of <span class="math-inline">\\(0, 2, 4\\)</span>, which is <span class="math-inline">\\(2\\)</span>. So the minimizer of <span class="math-inline">\\(R&#95;\text{clip}(w)\\)</span> within the interval <span class="math-inline">\\(1 \leq w \leq 3\\)</span> is <span class="math-inline">\\(\boxed{2}\\)</span>.

If you'd like to see this a little more formally, then when <span class="math-inline">\\(1 \leq w \leq 3\\)</span>,

<div class="math-display">
$$
R_\text{clip}(w)=\frac14\left(w^2+(2-w)^2+(4-w)^2+9\right)
$$
</div>

 Taking the derivative,

<div class="math-display">
$$
\frac{\text{d}}{\text{d}w}R_\text{clip}(w)=\frac14(2w+2(w-2)+2(w-4))=\frac{6w-12}{4}
$$
</div>

 Setting this equal to <span class="math-inline">\\(0\\)</span> gives <span class="math-inline">\\(w = 2\\)</span>, as we intuited earlier.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> Now suppose there are no restrictions on <span class="math-inline">\\(w\\)</span>. Among all possible values of <span class="math-inline">\\(w\\)</span>, which value minimizes <span class="math-inline">\\(R&#95;\text{clip}(w)\\)</span>? Give your answer as a number with no variables.

<span class="math-inline">\\(\text{minimizer of } R&#95;\text{clip}(w) = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>

<details markdown="1"><summary>Solution</summary>

The best <span class="math-inline">\\(w\\)</span> is still <span class="math-inline">\\(w = 2\\)</span>. As a refresher, let's look at the graph of <span class="math-inline">\\(R&#95;\text{clip}(w)\\)</span> again:

<div style="text-align: center;">
<img src="/exams/sp26-mt1/imgs/p1-sol.png" alt="image" style="width: 90%; max-width: 100%;">
</div>

First, note that <span class="math-inline">\\(w = 20\\)</span> is a local minimizer of <span class="math-inline">\\(R&#95;\text{clip}(w)\\)</span>: if we zoom in to the graph of <span class="math-inline">\\(R&#95;\text{clip}(w)\\)</span> around <span class="math-inline">\\(w = 20\\)</span>, it looks like a parabola that opens up, centered at <span class="math-inline">\\(w = 20\\)</span>. But, when we zoom out, we see that the graph falls even lower near <span class="math-inline">\\(w = 2\\)</span> than it does near <span class="math-inline">\\(w = 20\\)</span>.

Why is this? It's because there are many more <span class="math-inline">\\(y&#95;i\\)</span> values within 3 units of <span class="math-inline">\\(w = 2\\)</span> than there are within 3 units of <span class="math-inline">\\(w = 20\\)</span>. Remembering that we have <span class="math-inline">\\(y&#95;1 = 0, y&#95;2 = 2, y&#95;3 = 4, y&#95;4 = 20\\)</span>:

<div class="math-display">
$$
R_\text{clip}(20) = \frac{1}{4} \sum_{i=1}^4 \min\{(20-y_i)^2, 9\} = \frac{1}{4} \left( 9 + 9 + 9 + 0 \right) = \frac{27}{4}
$$
</div>



<div class="math-display">
$$
R_\text{clip}(2) = \frac{1}{4} \sum_{i=1}^4 \min\{(2-y_i)^2, 9\} = \frac{1}{4} \left( 4 + 0 + 4 + 9 \right) = \frac{17}{4}
$$
</div>

So, <span class="math-inline">\\(R&#95;\text{clip}(20) = \frac{27}{4} &gt; \frac{13}{4} = R&#95;\text{clip}(2)\\)</span>.

The question, then, is whether <span class="math-inline">\\(w=2\\)</span> is the global minimizer, or just that it's better than <span class="math-inline">\\(w=20\\)</span>. Crucially, you wouldn't have had the graph of <span class="math-inline">\\(R&#95;\text{clip}(w)\\)</span> during the exam, so you would have needed to reason about this without it. One way to see how <span class="math-inline">\\(w = 2\\)</span> is the global minimizer is to realize that as <span class="math-inline">\\(w\\)</span> increases from <span class="math-inline">\\(2\\)</span>, the average loss only increases, until it reaches 9, where it "coasts" until it we reach <span class="math-inline">\\(w = 17\\)</span>, where it decreases once again.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">e)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> State one pro and one con of using clipped loss instead of squared loss to find optimal model parameters.

<details markdown="1"><summary>Solution</summary>

One pro is that clipped loss is less sensitive to outliers, since very large errors all receive the same loss of <span class="math-inline">\\(9\\)</span>. One con is that it stops distinguishing between bad and very bad predictions once the error is large enough; it also introduces points where the derivative is not defined, when the two cases of the min function switch.
</details>

</div>
</div>

</div>


---

## SP26 MT1 · Problem 2 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">10 pts</span>

<p class="worksheet-source">From <a href="/exams/sp26-mt1/">SP26 MT1</a></p>


We will continue to use the constant model, <span class="math-inline">\\(h(x&#95;i)=w\\)</span>, and the same dataset of <span class="math-inline">\\(n=4\\)</span> values as in Problem 1:

<div class="math-display">
$$
0,\quad 2,\quad 4,\quad 20
$$
</div>

 Instead of the clipped loss function, consider the **weighted absolute** loss function, defined below.

<div class="math-display">
$$
L_\text{WA}(y_i,h(x_i))=
\begin{cases}
\beta(y_i-h(x_i)), & h(x_i)<y_i \\\\
h(x_i)-y_i, & h(x_i)\ge y_i
\end{cases}
$$
</div>

 where <span class="math-inline">\\(\beta\\)</span> is a positive integer. Let <span class="math-inline">\\(R&#95;\text{WA}(w)\\)</span> be the average weighted absolute loss for the constant model and this dataset.

The slope of <span class="math-inline">\\(R&#95;\text{WA}(w)\\)</span> at <span class="math-inline">\\(w\\)</span>, for any value of <span class="math-inline">\\(w\\)</span> not equal to one of the <span class="math-inline">\\(y&#95;i\\)</span> values, is

<div class="math-display">
$$
\text{slope of } R_\text{WA}(w) \text{ at } w = \frac{\#\text{ left of } w - \beta(\#\text{ right of } w)}{4}
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Suppose <span class="math-inline">\\(\beta = 1\\)</span>. Which value of <span class="math-inline">\\(w\\)</span> minimizes <span class="math-inline">\\(R&#95;\text{WA}(w)\\)</span>? Show your work, and write your final answer in the box provided. Your answer should be a number with no variables. If there are multiple possible answers, state just one.

<div class="math-display">
$$
\text{minimizer of } R_\text{WA}(w) = \_\_\_\_\_\_
$$
</div>

<details markdown="1"><summary>Solution</summary>

When <span class="math-inline">\\(\beta = 1\\)</span>, <span class="math-inline">\\(R&#95;{\text{WA}}(w)\\)</span> is just mean absolute error, <span class="math-inline">\\(R&#95;\text{abs}(w)\\)</span>. We know that the minimizer of mean absolute error is the median of the dataset, or any value between the middle two values if the dataset has an even number of values.

This dataset has an even number of values, so any <span class="math-inline">\\(w\\)</span> in the interval <span class="math-inline">\\(2 \leq w \leq 4\\)</span> minimizes <span class="math-inline">\\(R&#95;\text{WA}(w)\\)</span>. One such value is <span class="math-inline">\\(\boxed{3}\\)</span>, but <span class="math-inline">\\(2\\)</span>, <span class="math-inline">\\(4\\)</span>, <span class="math-inline">\\(\pi\\)</span>, etc. are all valid answers.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Now suppose <span class="math-inline">\\(\beta = 2\\)</span>. Which value of <span class="math-inline">\\(w\\)</span> minimizes <span class="math-inline">\\(R&#95;\text{WA}(w)\\)</span>? Show your work, and write your final answer in the box provided. Your answer should be a number with no variables. If there are multiple possible answers, state just one.

<div class="math-display">
$$
\text{minimizer of } R_\text{WA}(w) = \_\_\_\_\_\_
$$
</div>

<details markdown="1"><summary>Solution</summary>

When <span class="math-inline">\\(\beta=2\\)</span>, the slopes between consecutive data values are

<div class="math-display">
$$
-2,\quad -\frac54,\quad -\frac12,\quad \frac14,\quad 1
$$
</div>

 on the intervals <span class="math-inline">\\((-\infty,0)\\)</span>, <span class="math-inline">\\((0,2)\\)</span>, <span class="math-inline">\\((2,4)\\)</span>, <span class="math-inline">\\((4,20)\\)</span>, and <span class="math-inline">\\((20,\infty)\\)</span>. The slope changes from negative to positive at <span class="math-inline">\\(w=4\\)</span>, so the minimizer is <span class="math-inline">\\(\boxed{4}\\)</span>.

Conceptually, the fact that the errors in the case where <span class="math-inline">\\(y&#95;i &gt; h(x&#95;i)\\)</span> are multiplied by <span class="math-inline">\\(\beta\\)</span> forces the optimal <span class="math-inline">\\(w^{\ast}\\)</span> to be larger than the median (since we want the <span class="math-inline">\\(y&#95;i &gt; h(x&#95;i)\\)</span> case to not trigger as often when computing the average loss across the entire dataset).
</details>

</div>
</div>

</div>


---

## SP26 Final · Problem 1 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">14 pts</span> <span class="badge" data-flag="mt1-redemption" style="background-color: #9A3324; color: #FFFFFF; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">MT1 Redemption</span>

<p class="worksheet-source">From <a href="/exams/sp26-final/">SP26 Final</a></p>


Suppose we'd like to find the optimal constant parameter, <span class="math-inline">\\(w^{\ast}\\)</span>, for the constant model <span class="math-inline">\\(h(x&#95;i)=w\\)</span>, using the following dataset of <span class="math-inline">\\(n=5\\)</span> values:

<div class="math-display">
$$
1,\quad 1,\quad 4,\quad 9,\quad 25
$$
</div>

 In each part, find the value of <span class="math-inline">\\(w^{\ast}\\)</span> that minimizes the given <span class="math-inline">\\(R(w)\\)</span>. Show your work in the space provided, and write your final answer in the bottom-right corner of the box. Your answers should be numbers with no variables. *Note: There is no need to use calculus here.*

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span>
<span class="math-inline">\\(\displaystyle R(w) = \frac{1}{5} \sum&#95;{i=1}^5 (y&#95;i - w)^2\\)</span>

<div class="math-display">
$$
w^* = \_\_\_\_\_\_
$$
</div>

<details markdown="1"><summary>Solution</summary>

The minimizer of mean squared error for a constant model is the mean, as discussed in [Chapter 1.2](https://notes.eecs245.org/introduction-to-supervised-learning/squared-loss-constant-model/). So,

<div class="math-display">
$$
w^* = \frac{1+1+4+9+25}{5} = \frac{40}{5} = 8
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span>
<span class="math-inline">\\(\displaystyle R(w) = \frac{1}{5} \sum&#95;{i=1}^5 (\sqrt{y&#95;i} - w)^2\\)</span>

<div class="math-display">
$$
w^* = \_\_\_\_\_\_
$$
</div>

<details markdown="1"><summary>Solution</summary>

This is asking for the best constant prediction for the transformed values <span class="math-inline">\\(\sqrt{y&#95;i}\\)</span>. The transformed data are

<div class="math-display">
$$
1,\quad 1,\quad 2,\quad 3,\quad 5
$$
</div>

 so

<div class="math-display">
$$
w^* = \frac{1+1+2+3+5}{5} = \frac{12}{5}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span>
<span class="math-inline">\\(\displaystyle R(w) = \frac{1}{5} \sum&#95;{i=1}^5 (y&#95;i - \sqrt{w})^2\\)</span>

<div class="math-display">
$$
w^* = \_\_\_\_\_\_
$$
</div>

<details markdown="1"><summary>Solution</summary>

Let <span class="math-inline">\\(u=\sqrt{w}\\)</span>. The loss becomes

<div class="math-display">
$$
R(u) = \frac{1}{5}\sum_{i=1}^5 (y_i-u)^2
$$
</div>

 which is minimized at the mean of the original <span class="math-inline">\\(y&#95;i\\)</span> values:

<div class="math-display">
$$
u^* = \frac{1+1+4+9+25}{5} = 8
$$
</div>

 Since <span class="math-inline">\\(u=\sqrt{w}\\)</span>, we have

<div class="math-display">
$$
w^* = 8^2 = 64
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">2 pts</span> Which answer from above is also the minimizer of <span class="math-inline">\\(\displaystyle R(w) = \sqrt{\frac{1}{5} \sum&#95;{i=1}^5 (y&#95;i - w)^2}\\)</span>?

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Answer from part (a)</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Answer from part (b)</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Answer from part (c)</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> None</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> Answer from part (a)</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Answer from part (b)</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Answer from part (c)</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> None</span></div>

The square root function is strictly increasing, so minimizing

<div class="math-display">
$$
\sqrt{\frac{1}{5} \sum_{i=1}^5 (y_i-w)^2}
$$
</div>

 is equivalent to minimizing

<div class="math-display">
$$
\frac{1}{5} \sum_{i=1}^5 (y_i-w)^2
$$
</div>

That is exactly the objective from part **a)**, so the answer is the answer from part **a)**.
</details>

</div>
</div>

</div>


---

## More practice (PDF only)

- [MOCK MT1 Problem 1](/resources/exams/mock-mt1.pdf#page=3)
- [MOCK MT1 Problem 2](/resources/exams/mock-mt1.pdf#page=4)

{% endraw %}
