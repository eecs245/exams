---
layout: minimal
title: "Spring 2026 Final Exam"
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

# Spring 2026 Final Exam

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/exams/sp26-final.pdf" target="_blank">View as PDF ✏️</a>
<a class="btn btn-info assignment-pdf-button" href="/resources/exams/sp26-final-solutions.pdf" target="_blank">Solutions PDF ✅</a>
</div>

{: .yellow }
<div markdown="1">
**Instructions**

-   This exam consists of 14 problems, worth a total of 130 points, spread across 14 pages (7 sheets of paper). **All problems count towards your Final Exam score; certain problems also count towards your Midterm 1 or Midterm 2 redemption scores.**

-   You have 120 minutes to complete this exam, unless you have extended-time accommodations through SSD.

-   Write your uniqname in the top right corner of every page in the space provided.

-   For free response problems, show your work unless otherwise specified, and write your final answer in the box provided.

-   For multiple choice problems, completely fill in bubbles and square boxes; if we cannot tell which option(s) you selected, you may lose points.



-   You may refer to **3** two-sided handwritten notes sheets. No other resources or technology are allowed.
</div>

---

## Problems

- [Problem 1: (14 pts) $\boxed{\text{Counts towards Midterm 1 redemption score}}$](#problem-1-14-pts-boxedtextcounts-towards-midterm-1-redemption-score)
- [Problem 2: (9 pts) $\boxed{\text{Counts towards Midterm 1 redemption score}}$](#problem-2-9-pts-boxedtextcounts-towards-midterm-1-redemption-score)
- [Problem 3: (10 pts) $\boxed{\text{Counts towards Midterm 1 redemption score}}$](#problem-3-10-pts-boxedtextcounts-towards-midterm-1-redemption-score)
- [Problem 4: (5 pts) $\boxed{\text{Counts towards Midterm 1 redemption score}}$](#problem-4-5-pts-boxedtextcounts-towards-midterm-1-redemption-score)
- [Problem 5: (4 pts) $\boxed{\text{Counts towards Midterm 2 redemption score}}$](#problem-5-4-pts-boxedtextcounts-towards-midterm-2-redemption-score)
- [Problem 6: (6 pts) $\boxed{\text{Counts towards Midterm 2 redemption score}}$](#problem-6-6-pts-boxedtextcounts-towards-midterm-2-redemption-score)
- [Problem 7: (12 pts) $\boxed{\text{Counts towards Midterm 2 redemption score}}$](#problem-7-12-pts-boxedtextcounts-towards-midterm-2-redemption-score)
- [Problem 8: (12 pts) $\boxed{\text{Counts towards Midterm 2 redemption score}}$](#problem-8-12-pts-boxedtextcounts-towards-midterm-2-redemption-score)
- [Problem 9: (9 pts) $\boxed{\text{Counts towards Midterm 2 redemption score}}$](#problem-9-9-pts-boxedtextcounts-towards-midterm-2-redemption-score)
- [Problem 10](#problem-10-12-pts)
- [Problem 11](#problem-11-10-pts)
- [Problem 12](#problem-12-11-pts)
- [Problem 13](#problem-13-12-pts)
- [Problem 14](#problem-14-4-pts)

---

## Problem 1: (14 pts) <span class="math-inline">\\(\boxed{\text{Counts towards Midterm 1 redemption score}}\\)</span>

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
w^* = \boxed{\textbf{8}}
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
w^* = \boxed{\textbf{12/5}}
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
w^* = \boxed{\textbf{64}}
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

## Problem 2: (9 pts) <span class="math-inline">\\(\boxed{\text{Counts towards Midterm 1 redemption score}}\\)</span>

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

## Problem 3: (10 pts) <span class="math-inline">\\(\boxed{\text{Counts towards Midterm 1 redemption score}}\\)</span>

Let <span class="math-inline">\\(\vec x = \begin{bmatrix} 2 \\\\ 1 \\\\ 1 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec z = \begin{bmatrix} 3 \\\\ 9 \\\\ 3 \end{bmatrix}\\)</span>, and suppose <span class="math-inline">\\(\vec y \in \mathbb{R}^3\\)</span> is such that

the projection of <span class="math-inline">\\(\vec x\\)</span> onto <span class="math-inline">\\(\vec y\\)</span> is <span class="math-inline">\\(\vec 0\\)</span> and that <span class="math-inline">\\(\vec y \cdot \vec y = \vec y \cdot \vec z = 45\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Find the projection of <span class="math-inline">\\(\vec z\\)</span> onto <span class="math-inline">\\(\vec x\\)</span>. Show your work, and write your final answer in the box provided. Give your answer as a vector with no variables.

<div class="math-display">
$$
\text{projection of \vec z onto \vec x} = \boxed{\textbf{\begin{bmatrix}6\\\\3\\\\3\end{bmatrix}}}
$$
</div>

<details markdown="1"><summary>Solution</summary>

Using the projection formula from [Chapter 3.4](https://notes.eecs245.org/vectors/projecting-onto-a-single-vector/),

<div class="math-display">
$$
\vec p =
\frac{\vec{z}\cdot\vec{x}}{\vec{x}\cdot\vec{x}}\vec{x}
$$
</div>

 Here,

<div class="math-display">
$$
\vec{z}\cdot\vec{x}=3(2)+9(1)+3(1)=18,
\qquad
\vec{x}\cdot\vec{x}=2^2+1^2+1^2=6
$$
</div>

 so

<div class="math-display">
$$
\vec p
=
\frac{18}{6}\vec{x}
=
3\begin{bmatrix}2\\\\1\\\\1\end{bmatrix}
=
\begin{bmatrix}6\\\\3\\\\3\end{bmatrix}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Write <span class="math-inline">\\(\vec z\\)</span> as a linear combination of <span class="math-inline">\\(\vec x\\)</span> and <span class="math-inline">\\(\vec y\\)</span>. Show your work, and fill in each box with a number with no variables. <em>Hint: What is the relationship between <span class="math-inline">\\(\vec x\\)</span> and <span class="math-inline">\\(\vec y\\)</span>?</em>

<details markdown="1"><summary>Solution</summary>

Since the projection of <span class="math-inline">\\(\vec{x}\\)</span> onto <span class="math-inline">\\(\vec{y}\\)</span> is <span class="math-inline">\\(\vec{0}\\)</span> and <span class="math-inline">\\(\vec{y}\cdot\vec{y}=45\\)</span>, <span class="math-inline">\\(\vec{y}\\)</span> is nonzero and <span class="math-inline">\\(\vec{x}\cdot\vec{y}=0\\)</span>. In other words, <span class="math-inline">\\(\vec{x}\\)</span> and <span class="math-inline">\\(\vec{y}\\)</span> are orthogonal.

Suppose

<div class="math-display">
$$
\vec{z}=a\vec{x}+b\vec{y}
$$
</div>

 Taking dot products with <span class="math-inline">\\(\vec{x}\\)</span> gives

<div class="math-display">
$$
\vec{z}\cdot\vec{x}=a(\vec{x}\cdot\vec{x})+b(\vec{y}\cdot\vec{x})
$$
</div>

 Using the work from part **a)**, <span class="math-inline">\\(\vec{z}\cdot\vec{x}=18\\)</span> and <span class="math-inline">\\(\vec{x}\cdot\vec{x}=6\\)</span>. Since <span class="math-inline">\\(\vec{y}\cdot\vec{x}=0\\)</span>,

<div class="math-display">
$$
18 = 6a
$$
</div>

 so <span class="math-inline">\\(a=3\\)</span>.

Now take dot products with <span class="math-inline">\\(\vec{y}\\)</span>:

<div class="math-display">
$$
\vec{z}\cdot\vec{y}=a(\vec{x}\cdot\vec{y})+b(\vec{y}\cdot\vec{y})
$$
</div>

 The problem tells us that <span class="math-inline">\\(\vec{z}\cdot\vec{y}=\vec{y}\cdot\vec{y}=45\\)</span>, and <span class="math-inline">\\(\vec{x}\cdot\vec{y}=0\\)</span>, so

<div class="math-display">
$$
45=45b
$$
</div>

 and therefore <span class="math-inline">\\(b=1\\)</span>. So,

<div class="math-display">
$$
\vec{z}=3\vec{x}+\vec{y}
$$
</div>

</details>

</div>
</div>

</div>

---

## Problem 4: (5 pts) <span class="math-inline">\\(\boxed{\text{Counts towards Midterm 1 redemption score}}\\)</span>

Suppose <span class="math-inline">\\(S = \left\lbrace \begin{bmatrix} x&#95;1 \\\\ x&#95;2 \\\\ x&#95;3 \\\\ x&#95;4 \end{bmatrix} : x&#95;1 + x&#95;2 + 2x&#95;3 = 0 \text{ and } x&#95;3 = x&#95;4 \right\rbrace\\)</span>. State one basis for <span class="math-inline">\\(S\\)</span>. Your answer should be a list of vectors with no variables.

<span class="math-inline">\\(\text{one basis for } S =\\)</span>

<details markdown="1"><summary>Solution</summary>

The condition <span class="math-inline">\\(x&#95;3=x&#95;4\\)</span> means we can write <span class="math-inline">\\(x&#95;3=x&#95;4=b\\)</span>. The other condition gives

<div class="math-display">
$$
x_1+x_2+2b=0
$$
</div>

 so <span class="math-inline">\\(x&#95;1=-x&#95;2-2b\\)</span>. Let <span class="math-inline">\\(x&#95;2=a\\)</span>. Then every vector in <span class="math-inline">\\(S\\)</span> can be written as

<div class="math-display">
$$
\begin{bmatrix}
x_1\\\\x_2\\\\x_3\\\\x_4
\end{bmatrix}
=
\begin{bmatrix}
-a-2b\\\\a\\\\b\\\\b
\end{bmatrix}
=
a\begin{bmatrix}-1\\\\1\\\\0\\\\0\end{bmatrix}
+b\begin{bmatrix}-2\\\\0\\\\1\\\\1\end{bmatrix}
$$
</div>

 So, one basis for <span class="math-inline">\\(S\\)</span> is

<div class="math-display">
$$
\left\{
\begin{bmatrix}-1\\\\1\\\\0\\\\0\end{bmatrix},
\begin{bmatrix}-2\\\\0\\\\1\\\\1\end{bmatrix}
\right\}
$$
</div>

Another way to think about this: since <span class="math-inline">\\(\dim(S)=2\\)</span> (the subspace has two "degrees of freedom", or free variables), any two linearly independent vectors in <span class="math-inline">\\(S\\)</span> span all of <span class="math-inline">\\(S\\)</span> (see [Chapter 4.3](https://notes.eecs245.org/linear-independence/vector-spaces-basis-dimension/)). So, we could just play with the numbers until we end up with two vectors that are not scalar multiples of each other that both satisfy the conditions of inclusion in <span class="math-inline">\\(S\\)</span>. For instance,

<div class="math-display">
$$
\left\{\begin{bmatrix}-1\\\\1\\\\0\\\\0\end{bmatrix},\begin{bmatrix}-3 \\\\ 1 \\\\ 1 \\\\ 1\end{bmatrix}\right\}
$$
</div>

 is also a valid basis.
</details>

---

## Problem 5: (4 pts) <span class="math-inline">\\(\boxed{\text{Counts towards Midterm 2 redemption score}}\\)</span>

Suppose <span class="math-inline">\\(A\\)</span> is a <span class="math-inline">\\(7 \times 12\\)</span> matrix. Fill in each blank with an integer with no variables.

1.  (2 pts) What is the minimum possible value of <span class="math-inline">\\(\text{dim}(\text{nullsp}(A))\\)</span>?

2.  (2 pts) What is the maximum possible value of <span class="math-inline">\\(\text{dim}(\text{nullsp}(A))\\)</span>?

<details markdown="1"><summary>Solution</summary>

By the rank-nullity theorem from [Chapter 5.4](https://notes.eecs245.org/matrices/null-space-rank-nullity/),

<div class="math-display">
$$
\text{rank}(A)+\text{dim}(\text{nullsp}(A))=12
$$
</div>

 The rank of a <span class="math-inline">\\(7\times 12\\)</span> matrix is at least <span class="math-inline">\\(0\\)</span> and at most <span class="math-inline">\\(7\\)</span>. So the dimension of the null space is

<div class="math-display">
$$
\text{dim}(\text{nullsp}(A))=12-\text{rank}(A)
$$
</div>

 This is as small as possible when <span class="math-inline">\\(\text{rank}(A)=7\\)</span>, giving minimum <span class="math-inline">\\(\text{dim}(\text{nullsp}(A)) = 5\\)</span>, and as large as possible when <span class="math-inline">\\(\text{rank}(A)=0\\)</span>, giving maximum <span class="math-inline">\\(\text{dim}(\text{nullsp}(A)) = 12\\)</span>.
</details>

---

## Problem 6: (6 pts) <span class="math-inline">\\(\boxed{\text{Counts towards Midterm 2 redemption score}}\\)</span>

Find the area enclosed by the polygon with vertices <span class="math-inline">\\((0, 0)\\)</span>, <span class="math-inline">\\((4, 6)\\)</span>, <span class="math-inline">\\((1, 8)\\)</span>, and <span class="math-inline">\\((-3, 2)\\)</span>. Show your work, and write your answer in the box provided.

<div class="math-display">
$$
\text{area} = \boxed{\textbf{26}}
$$
</div>

<details markdown="1"><summary>Solution</summary>

Let

<div class="math-display">
$$
\vec{u}=\begin{bmatrix}4\\\\6\end{bmatrix}
\qquad\text{and}\qquad
\vec{v}=\begin{bmatrix}-3\\\\2\end{bmatrix}
$$
</div>

 Then

<div class="math-display">
$$
\vec{u}+\vec{v}
=
\begin{bmatrix}1\\\\8\end{bmatrix}
$$
</div>

 so the four vertices are the coordinates of <span class="math-inline">\\(\vec{0}\\)</span>, <span class="math-inline">\\(\vec{u}\\)</span>, <span class="math-inline">\\(\vec{u}+\vec{v}\\)</span>, and <span class="math-inline">\\(\vec{v}\\)</span>. This means the polygon is a parallelogram. The area of the parallelogram is the absolute value of the determinant of the matrix whose columns are the two side vectors, as in [Chapter 6.1](https://notes.eecs245.org/linear-transformations-and-projections/linear-transformations/#the-determinant). We picked <span class="math-inline">\\(\vec{u}\\)</span> and <span class="math-inline">\\(\vec{v}\\)</span> because they are the side vectors from the origin, but using any two of the three nonzero vertices as the columns would give the same answer after taking the absolute value: adding one column to another does not change the determinant.

<div style="text-align: center;">
<img src="imgs/polygon-determinant-area.png" alt="image" style="width: 75%; max-width: 100%;">
</div>

So,

<div class="math-display">
$$
\text{area}
=
\left|
\det\left(
\begin{bmatrix}
4 & -3\\\\
6 & 2
\end{bmatrix}
\right)
\right|
=
\left|4(2)-(-3)(6)\right|
=26
$$
</div>

</details>

---

## Problem 7: (12 pts) <span class="math-inline">\\(\boxed{\text{Counts towards Midterm 2 redemption score}}\\)</span>

Suppose <span class="math-inline">\\(X\\)</span> is an <span class="math-inline">\\(n \times d\\)</span> matrix with linearly independent columns, <span class="math-inline">\\(d&lt;n\\)</span>, and <span class="math-inline">\\(\vec y \in \mathbb{R}^n\\)</span>.

Furthermore, suppose <span class="math-inline">\\(P\\)</span> is the matrix that projects vectors in <span class="math-inline">\\(\mathbb{R}^n\\)</span> onto <span class="math-inline">\\(\text{colsp}(X)\\)</span>, and <span class="math-inline">\\(\vec p = P \vec y\\)</span> is the projection of <span class="math-inline">\\(\vec y\\)</span> onto <span class="math-inline">\\(\text{colsp}(X)\\)</span>.

Finally, let <span class="math-inline">\\(Q\\)</span> be an <span class="math-inline">\\(n \times n\\)</span> orthogonal matrix.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span>
1.  (2 pts) What is <span class="math-inline">\\(\text{det}(P)\\)</span>?
<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(-1\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(0\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(-1\\)</span> or <span class="math-inline">\\(1\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> None of these</span></div>

2.  (2 pts) What is <span class="math-inline">\\(\text{det}(Q)\\)</span>?
<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(-1\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(0\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(-1\\)</span> or <span class="math-inline">\\(1\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> None of these</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(-1\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(0\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(-1\\)</span> or <span class="math-inline">\\(1\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> None of these</span></div>

**(i)** Since <span class="math-inline">\\(P\\)</span> projects onto <span class="math-inline">\\(\text{colsp}(X)\\)</span> and <span class="math-inline">\\(d&lt;n\\)</span>, multiple vectors in <span class="math-inline">\\(\mathbb{R}^n\\)</span> will have the same projection onto <span class="math-inline">\\(\text{colsp}(X)\\)</span>. So <span class="math-inline">\\(P\\)</span> is not invertible, and therefore <span class="math-inline">\\(\det(P)=0\\)</span>.

**(ii)** Since <span class="math-inline">\\(Q\\)</span> is orthogonal, <span class="math-inline">\\(Q^TQ=I\\)</span>. Taking determinants gives

<div class="math-display">
$$
\det(Q^TQ)=\det(I)
$$
</div>

 so, since <span class="math-inline">\\(\det(I)=1\\)</span>, <span class="math-inline">\\(\text{det}(Q^T) = \det(Q)\\)</span>, and in general <span class="math-inline">\\(\text{det}(AB) = \det(A)\det(B)\\)</span> for square <span class="math-inline">\\(A\\)</span> and <span class="math-inline">\\(B\\)</span>, we have

<div class="math-display">
$$
\det(Q)^2=1
$$
</div>

 and therefore <span class="math-inline">\\(\det(Q)\\)</span> is either <span class="math-inline">\\(-1\\)</span> or <span class="math-inline">\\(1\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">2 pts</span> Which of the following vectors is orthogonal to <span class="math-inline">\\(\text{colsp}(X)\\)</span>?

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\vec y\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(P \vec y\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(Q \vec y\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\((I - P) \vec y\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\((I - Q) \vec y\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> None of these</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\vec y\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(P \vec y\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(Q \vec y\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\((I - P) \vec y\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\((I - Q) \vec y\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> None of these</span></div>

The vector <span class="math-inline">\\(P\vec{y}\\)</span> is the projection of <span class="math-inline">\\(\vec{y}\\)</span> onto <span class="math-inline">\\(\text{colsp}(X)\\)</span>, so the error vector

<div class="math-display">
$$
\vec y - \vec p = \vec{y}-P\vec{y}=(I-P)\vec{y}
$$
</div>

 is orthogonal to <span class="math-inline">\\(\text{colsp}(X)\\)</span>. This is the same projection geometry used in [Chapter 6.3](https://notes.eecs245.org/linear-transformations-and-projections/projecting-onto-column-space/); the novel thing here was the representation of the error vector as a linear combination of the columns of <span class="math-inline">\\(I-P\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Prove that the projection of <span class="math-inline">\\(Q \vec y\\)</span> onto <span class="math-inline">\\(\text{colsp}(QX)\\)</span> is <span class="math-inline">\\(Q \vec p\\)</span>. <em>Hint: Start by showing that the matrix that projects vectors in <span class="math-inline">\\(\mathbb{R}^n\\)</span> onto <span class="math-inline">\\(\text{colsp}(QX)\\)</span> is <span class="math-inline">\\(Q P Q^T\\)</span>.</em>

<details markdown="1"><summary>Solution</summary>

Since <span class="math-inline">\\(X\\)</span> has linearly independent columns, the matrix that projects onto <span class="math-inline">\\(\text{colsp}(X)\\)</span> is

<div class="math-display">
$$
P=X(X^TX)^{-1}X^T
$$
</div>

 Now, the matrix that projects onto <span class="math-inline">\\(\text{colsp}(QX)\\)</span> is

<div class="math-display">
$$
\begin{align*}
QX((QX)^T(QX))^{-1}(QX)^T
&=
QX(X^TQ^TQX)^{-1}X^TQ^T \\\\
&=
QX(X^TX)^{-1}X^TQ^T \\\\
&=
QPQ^T
\end{align*}
$$
</div>

using the fact that <span class="math-inline">\\(Q^TQ=I\\)</span>. Therefore, the projection of <span class="math-inline">\\(Q\vec{y}\\)</span> onto <span class="math-inline">\\(\text{colsp}(QX)\\)</span> is

<div class="math-display">
$$
(QPQ^T)(Q\vec{y})
=
QP(Q^TQ)\vec{y}
=
QP\vec{y}
=
Q\vec{p}
$$
</div>

Why does this happen? Think of <span class="math-inline">\\(Q\\)</span> as a rotation matrix. This is saying that if we:

**(i)** Rotate <span class="math-inline">\\(\vec y\\)</span> and rotate <span class="math-inline">\\(\text{colsp}(X)\\)</span>, and project the rotated <span class="math-inline">\\(\vec y\\)</span> onto the rotated <span class="math-inline">\\(\text{colsp}(X)\\)</span>, OR

**(ii)** Project the original <span class="math-inline">\\(\vec y\\)</span> onto the original <span class="math-inline">\\(\text{colsp}(X)\\)</span>, and then rotate the projected vector,

we end up with the same vector in either case.
</details>

</div>
</div>

</div>

---

## Problem 8: (12 pts) <span class="math-inline">\\(\boxed{\text{Counts towards Midterm 2 redemption score}}\\)</span>

Suppose we'd like to fit a multiple linear regression model to predict <span class="math-inline">\\(\texttt{cost}&#95;i\\)</span>, the cost in dollars of parking in an Ann Arbor parking garage, using <span class="math-inline">\\(\texttt{hours}&#95;i\\)</span>, the number of hours parked.

For each row <span class="math-inline">\\(i\\)</span>, the corresponding augmented feature vector is <span class="math-inline">\\(\text{Aug}(\vec x&#95;i) = \begin{bmatrix} 1 &amp; \texttt{hours}&#95;i &amp; \max(0,\texttt{hours}&#95;i-2) \end{bmatrix}^T\\)</span> so the model is of the form

<div class="math-display">
$$
h(\vec x_i)
=
w_0 + w_1 \texttt{hours}_i + w_2 \max(0, \texttt{hours}_i - 2)
$$
</div>

 The model is fit by minimizing mean squared error.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Suppose the dataset has four rows, and the number of hours parked in those rows is

<span class="math-inline">\\(3\\)</span>, <span class="math-inline">\\(0\\)</span>, <span class="math-inline">\\(5\\)</span>, and <span class="math-inline">\\(1\\)</span>, respectively. Write the first four rows of the design matrix <span class="math-inline">\\(X\\)</span>. Your answer should be a matrix with four rows and no variables.

<span class="math-inline">\\(X =\\)</span>

<details markdown="1"><summary>Solution</summary>

Each row is the transpose of the augmented feature vector

<div class="math-display">
$$
\begin{bmatrix}
1\\\\
\texttt{hours}_i\\\\
\max(0,\texttt{hours}_i-2)
\end{bmatrix}
$$
</div>

 For <span class="math-inline">\\(\texttt{hours}&#95;i=3,0,5,1\\)</span>, the values of <span class="math-inline">\\(\max(0,\texttt{hours}&#95;i-2)\\)</span> are <span class="math-inline">\\(1,0,3,0\\)</span>, respectively. So,

<div class="math-display">
$$
X=
\begin{bmatrix}
1&3&1\\\\
1&0&0\\\\
1&5&3\\\\
1&1&0
\end{bmatrix}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">2 pts</span> Give a one-sentence English explanation of the meaning of <span class="math-inline">\\(w&#95;2\\)</span>.

<details markdown="1"><summary>Solution</summary>

The coefficient <span class="math-inline">\\(w&#95;2\\)</span> is the change in the hourly slope after 2 hours; after the first 2 hours, each additional hour changes the predicted cost by <span class="math-inline">\\(w&#95;1+w&#95;2\\)</span> dollars instead of <span class="math-inline">\\(w&#95;1\\)</span> dollars.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Once again, suppose the dataset has four rows. In each of the following subparts, we provide the number of hours parked in the dataset. Find the rank of the design matrix <span class="math-inline">\\(X\\)</span> in each case. Fill in each blank with an integer with no variables.

1.  (2 pts) <span class="math-inline">\\(3\\)</span>, <span class="math-inline">\\(0\\)</span>, <span class="math-inline">\\(5\\)</span>, and <span class="math-inline">\\(1\\)</span> <span class="math-inline">\\(\text{rank}(X) = \boxed{\textbf{3}}\\)</span>

2.  (2 pts) <span class="math-inline">\\(2\\)</span>, <span class="math-inline">\\(0\\)</span>, <span class="math-inline">\\(2\\)</span>, and <span class="math-inline">\\(1\\)</span> <span class="math-inline">\\(\text{rank}(X) = \boxed{\textbf{2}}\\)</span>

3.  (2 pts) <span class="math-inline">\\(3\\)</span>, <span class="math-inline">\\(4\\)</span>, <span class="math-inline">\\(5\\)</span>, and <span class="math-inline">\\(6\\)</span> <span class="math-inline">\\(\text{rank}(X) = \boxed{\textbf{2}}\\)</span>

<details markdown="1"><summary>Solution</summary>

This feature engineering setup is an example of the multiple linear regression design matrices from [Chapter 7.2](https://notes.eecs245.org/regression-using-linear-algebra/multiple-linear-regression/).

**(i)** The design matrix is

<div class="math-display">
$$
\begin{bmatrix}
    1&3&1\\\\
    1&0&0\\\\
    1&5&3\\\\
    1&1&0
    \end{bmatrix}
$$
</div>

 The three columns are linearly independent, so <span class="math-inline">\\(\text{rank}(X)=3\\)</span>.

**(ii)** The design matrix is

<div class="math-display">
$$
\begin{bmatrix}
    1&2&0\\\\
    1&0&0\\\\
    1&2&0\\\\
    1&1&0
    \end{bmatrix}
$$
</div>

 The third column is all zero, while the first two columns are linearly independent. So <span class="math-inline">\\(\text{rank}(X)=2\\)</span>.

**(iii)** If all hour values are greater than <span class="math-inline">\\(2\\)</span>, then

<div class="math-display">
$$
\max(0,\texttt{hours}_i-2)=\texttt{hours}_i-2
$$
</div>

 This means column 2 is equal to <span class="math-inline">\\(2\\)</span> times column 1 plus column 3:

<div class="math-display">
$$
\text{column 2}=2(\text{column 1})+\text{column 3}
$$
</div>

 So the rank is at most <span class="math-inline">\\(2\\)</span>. Since the hour values are not all the same, columns 1 and 3 are linearly independent, and <span class="math-inline">\\(\text{rank}(X)=2\\)</span>.
</details>

</div>
</div>

</div>

---

## Problem 9: (9 pts) <span class="math-inline">\\(\boxed{\text{Counts towards Midterm 2 redemption score}}\\)</span>

Let <span class="math-inline">\\(\vec a \in \mathbb{R}^2\\)</span> and let

<div class="math-display">
$$
f(\vec x) = \log(\vec a \cdot \vec x)
$$
</div>

 for all vectors <span class="math-inline">\\(\vec x\\)</span> such that <span class="math-inline">\\(\vec a \cdot \vec x &gt; 0\\)</span>; if <span class="math-inline">\\(\vec a \cdot \vec x \leq 0\\)</span>, then <span class="math-inline">\\(f(\vec x)\\)</span> is undefined. Suppose that

<div class="math-display">
$$
\nabla f\left(\begin{bmatrix}2\\\\1\end{bmatrix}\right)
=
\begin{bmatrix}1/5\\\\3/5\end{bmatrix}
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> Which of the following could be <span class="math-inline">\\(\vec a\\)</span>? **Select all** that apply.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix}3\\\\1\end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix}1\\\\3\end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix}-1\\\\-3\end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix}1\\\\2\end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix}5\\\\3\end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix}2\\\\6\end{bmatrix}\\)</span></span></div>

<details markdown="1"><summary>Solution</summary>

<span class="mc-square mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix}2\\\\6\end{bmatrix}\\)</span>

Let

<div class="math-display">
$$
g(\vec{x})=\vec{a}\cdot\vec{x}=a_1x_1+a_2x_2
\qquad\text{and}\qquad
h(u)=\log(u)
$$
</div>

 Then <span class="math-inline">\\(f(\vec{x})=h(g(\vec{x}))\\)</span>. Using the chain rule from [Chapter 8.2](https://notes.eecs245.org/gradients/gradients-matrix-vector-operations/#chain-rule-for-vector-to-scalar-functions),

<div class="math-display">
$$
\nabla f(\vec{x})
=
h'(g(\vec{x}))\nabla g(\vec{x})
$$
</div>

 Now,

<div class="math-display">
$$
h'(u)=\frac{1}{u}
\qquad\text{and}\qquad
\nabla g(\vec{x})=
\begin{bmatrix}a_1\\\\a_2\end{bmatrix}
=\vec{a}
$$
</div>

 so

<div class="math-display">
$$
\nabla f(\vec{x})
=
h'(\vec a \cdot \vec x) \nabla g(\vec{x}) =
\frac{\vec{a}}{\vec{a}\cdot\vec{x}}
$$
</div>

 At <span class="math-inline">\\(\vec{x}=\begin{bmatrix}2\\\\1\end{bmatrix}\\)</span>, this becomes

<div class="math-display">
$$
\frac{\vec{a}}{2a_1+a_2}
=
\begin{bmatrix}1/5\\\\3/5\end{bmatrix}
$$
</div>

 Since <span class="math-inline">\\(f\\)</span> is defined at <span class="math-inline">\\(\begin{bmatrix}2\\\\1\end{bmatrix}\\)</span>, this must mean that <span class="math-inline">\\(\vec a \cdot \vec x\\)</span>, which is equal to <span class="math-inline">\\(2a&#95;1 + a&#95;2\\)</span>, is positive. Multiplying both sides by this positive denominator gives

<div class="math-display">
$$
\vec{a}
=
(2a_1+a_2)
\begin{bmatrix}1/5\\\\3/5\end{bmatrix}
=
\frac{2a_1+a_2}{5}
\begin{bmatrix}1\\\\3\end{bmatrix}
$$
</div>

 This says <span class="math-inline">\\(\vec{a}\\)</span> must be a positive scalar multiple of <span class="math-inline">\\(\begin{bmatrix}1\\\\3\end{bmatrix}\\)</span>. Among the answer choices, the vectors with that form are <span class="math-inline">\\(\begin{bmatrix}1\\\\3\end{bmatrix}\\)</span> and <span class="math-inline">\\(\begin{bmatrix}2\\\\6\end{bmatrix}\\)</span>.

Another way to approach this would be to take the equation

<div class="math-display">
$$
\frac{\vec a}{2a_1+a_2} = \begin{bmatrix}1/5\\\\3/5\end{bmatrix}
$$
</div>

from above, and realize the expression on the right is also equal to <span class="math-inline">\\(\frac{1}{2a&#95;1+a&#95;2} \begin{bmatrix}a&#95;1\\\\a&#95;2\end{bmatrix}\\)</span>, which allows us to set up a system of equations directly for <span class="math-inline">\\(a&#95;1\\)</span> and <span class="math-inline">\\(a&#95;2\\)</span>:

<div class="math-display">
$$
\begin{align*}
\frac{a_1}{2a_1+a_2} &= 1/5 \\\\
\frac{a_2}{2a_1+a_2} &= 3/5
\end{align*}
$$
</div>

Both equations say the same thing: <span class="math-inline">\\(a&#95;2 = 3a&#95;1\\)</span>, i.e. that <span class="math-inline">\\(a&#95;2\\)</span> must be triple <span class="math-inline">\\(a&#95;1\\)</span>, so <span class="math-inline">\\(\vec a\\)</span> is a scalar multiple of <span class="math-inline">\\(\begin{bmatrix}1\\\\3\end{bmatrix}\\)</span>. But, don't forget the added constraint that <span class="math-inline">\\(2a&#95;1 + a&#95;2\\)</span> must be positive.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Suppose we use gradient descent to minimize <span class="math-inline">\\(f(\vec x)\\)</span> using an initial guess of <span class="math-inline">\\(\vec x^{(0)} = \begin{bmatrix} 2 \\\\ 1 \end{bmatrix}\\)</span> and a learning rate of <span class="math-inline">\\(\alpha = 1/2\\)</span>. Find <span class="math-inline">\\(\vec x^{(1)}\\)</span>. Show your work, and write your answer in the box provided. Your answer should be a vector with no variables.

<div class="math-display">
$$
\vec x^{(1)} = \boxed{\textbf{\begin{bmatrix}19/10\\\\7/10\end{bmatrix}}}
$$
</div>

<details markdown="1"><summary>Solution</summary>

The gradient descent update from [Chapter 8.3](https://notes.eecs245.org/gradients/gradient-descent/) is

<div class="math-display">
$$
\vec{x}^{(1)}
=
\vec{x}^{(0)}-\alpha\nabla f(\vec{x}^{(0)})
$$
</div>

 Here, <span class="math-inline">\\(\vec{x}^{(0)}=\begin{bmatrix}2\\\\1\end{bmatrix}\\)</span>, <span class="math-inline">\\(\alpha=1/2\\)</span>, and <span class="math-inline">\\(\nabla f(\vec{x}^{(0)})=\begin{bmatrix}1/5\\\\3/5\end{bmatrix}\\)</span>. So,

<div class="math-display">
$$
\vec{x}^{(1)}
=
\begin{bmatrix}2\\\\1\end{bmatrix}
-
\frac{1}{2}\begin{bmatrix}1/5\\\\3/5\end{bmatrix}
=
\begin{bmatrix}2\\\\1\end{bmatrix}
-
\begin{bmatrix}1/10\\\\3/10\end{bmatrix}
=
\begin{bmatrix}19/10\\\\7/10\end{bmatrix}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">2 pts</span> This part is unrelated to the previous parts.

Suppose <span class="math-inline">\\(g: \mathbb{R} \to \mathbb{R}\\)</span>. True or false: if <span class="math-inline">\\(g\\)</span> has a global minimum and no local maxima, it must be convex.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> False</span></div>

This is false. For instance, consider

<div class="math-display">
$$
g(x)=x^4+x^3
$$
</div>

 This function has a global minimum, since <span class="math-inline">\\(g(x)\to\infty\\)</span> as <span class="math-inline">\\(x\to\infty\\)</span> and as <span class="math-inline">\\(x\to-\infty\\)</span>. Also,

<div class="math-display">
$$
g'(x)=4x^3+3x^2=x^2(4x+3)
$$
</div>

 The derivative only changes sign at <span class="math-inline">\\(x=-3/4\\)</span>, where it changes from negative to positive, so <span class="math-inline">\\(g\\)</span> has a local minimum and no local maxima. But,

<div class="math-display">
$$
g''(x)=12x^2+6x
$$
</div>

 which is negative for some <span class="math-inline">\\(x\\)</span> values, for instance <span class="math-inline">\\(x=-1/4\\)</span>. So <span class="math-inline">\\(g\\)</span> is not convex. See [Chapter 8.5](https://notes.eecs245.org/gradients/convexity/) for the convexity condition.

<div style="text-align: center;">
<img src="imgs/convexity-counterexample.png" alt="image" style="width: 82%; max-width: 100%;">
</div>
</details>

</div>
</div>

</div>

---

## Problem 10 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>

Let <span class="math-inline">\\(A=\begin{bmatrix}2&amp;4\\\\4&amp;2\end{bmatrix}\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">8 pts</span> Find all eigenvalues and eigenvectors of <span class="math-inline">\\(A\\)</span>. Show your work, and organize your answers as follows:

-   Put the larger eigenvalue in <span class="math-inline">\\(\lambda&#95;1\\)</span>, and a corresponding eigenvector in <span class="math-inline">\\(\vec v&#95;1\\)</span>.

-   Put the smaller eigenvalue in <span class="math-inline">\\(\lambda&#95;2\\)</span>, and a corresponding eigenvector in <span class="math-inline">\\(\vec v&#95;2\\)</span>.

<details markdown="1"><summary>Solution</summary>

The characteristic polynomial is

<div class="math-display">
$$
\begin{align*}
\det(A-\lambda I)
&=
\det\left(
\begin{bmatrix}
2-\lambda & 4\\\\
4 & 2-\lambda
\end{bmatrix}
\right) \\\\
&=
(2-\lambda)^2-16 \\\\
&=
\lambda^2-4\lambda-12 \\\\
&=
(\lambda-6)(\lambda+2)
\end{align*}
$$
</div>

So the eigenvalues are <span class="math-inline">\\(6\\)</span> and <span class="math-inline">\\(-2\\)</span>. Alternatively, using the trace and determinant facts from [Chapter 9.1](https://notes.eecs245.org/eigenvalues-and-eigenvectors/eigenvalues-eigenvectors/), you can arrive at this quickly by seeing that the eigenvalues must add to <span class="math-inline">\\(\text{trace}(A) = 2 + 2 = 4\\)</span> and multiply to <span class="math-inline">\\(\det(A) = 2 \cdot 2 - 4 \cdot 4 = -12\\)</span>.

For <span class="math-inline">\\(\lambda=6\\)</span>, write an eigenvector as

<div class="math-display">
$$
\vec{v}=\begin{bmatrix}a\\\\b\end{bmatrix}
$$
</div>

 Then

<div class="math-display">
$$
A\vec{v}
=
\begin{bmatrix}
2a+4b\\\\
4a+2b
\end{bmatrix}
=
6\begin{bmatrix}a\\\\b\end{bmatrix}
=
\begin{bmatrix}
6a\\\\
6b
\end{bmatrix}
$$
</div>

 so

<div class="math-display">
$$
2a+4b=6a
\qquad\text{and}\qquad
4a+2b=6b
$$
</div>

 Both equations say <span class="math-inline">\\(a=b\\)</span>, so one corresponding eigenvector is <span class="math-inline">\\(\begin{bmatrix}1\\\\1\end{bmatrix}\\)</span>.

For <span class="math-inline">\\(\lambda=-2\\)</span>, we similarly solve

<div class="math-display">
$$
\begin{bmatrix}
2a+4b\\\\
4a+2b
\end{bmatrix}
=
-2\begin{bmatrix}a\\\\b\end{bmatrix}
=
\begin{bmatrix}
-2a\\\\
-2b
\end{bmatrix}
$$
</div>

 so

<div class="math-display">
$$
2a+4b=-2a
\qquad\text{and}\qquad
4a+2b=-2b
$$
</div>

 Both equations say <span class="math-inline">\\(a=-b\\)</span>, so one corresponding eigenvector is <span class="math-inline">\\(\begin{bmatrix}1\\\\-1\end{bmatrix}\\)</span>. Therefore,

<div class="math-display">
$$
\lambda_1=6,\quad \vec{v}_1=\begin{bmatrix}1\\\\1\end{bmatrix},
\qquad
\lambda_2=-2,\quad \vec{v}_2=\begin{bmatrix}1\\\\-1\end{bmatrix}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> True or false: for all integer values of <span class="math-inline">\\(k\\)</span>, the matrix <span class="math-inline">\\(B=\begin{bmatrix}2&amp;4&amp;0\\\\4&amp;2&amp;0\\\\0&amp;0&amp;k\end{bmatrix}\\)</span> is diagonalizable.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

This is true. Since <span class="math-inline">\\(B\\)</span> is block diagonal (see [Chapter 9.4](https://notes.eecs245.org/eigenvalues-and-eigenvectors/multiplicities-diagonalization/#example-another-diagonalizable-matrix)), we can read off eigenvalues and eigenvectors from its individual blocks.

<div class="math-display">
$$
B=
\left[
\begin{array}{c|c}
\begin{array}{cc}
2 & 4 \\\\
4 & 2
\end{array}
&
\begin{array}{c}
0 \\\\ 0
\end{array}
\\\\
\hline
\begin{array}{cc}
0 & 0
\end{array}
&
\boxed{k}
\end{array}
\right]
$$
</div>

 The top-left block has two linearly independent eigenvectors, <span class="math-inline">\\(\begin{bmatrix}1\\\\1\\\\0\end{bmatrix}\\)</span> and <span class="math-inline">\\(\begin{bmatrix}1\\\\-1\\\\0\end{bmatrix}\\)</span>, with eigenvalues <span class="math-inline">\\(6\\)</span> and <span class="math-inline">\\(-2\\)</span>, and <span class="math-inline">\\(\begin{bmatrix}0\\\\0\\\\1\end{bmatrix}\\)</span> is an eigenvector with eigenvalue <span class="math-inline">\\(k\\)</span>. These three eigenvectors are linearly independent no matter what <span class="math-inline">\\(k\\)</span> is. Therefore <span class="math-inline">\\(B\\)</span> is diagonalizable for all integer values of <span class="math-inline">\\(k\\)</span>.

Another way to think about this is that for any <span class="math-inline">\\(k\\)</span>, the matrix <span class="math-inline">\\(B\\)</span> is symmetric, and hence diagonalizable, as told to us by the spectral theorem.
</details>

</div>
</div>

</div>

---

## Problem 11 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">10 pts</span>

The state diagram below describes a Markov chain with three states. <span class="math-inline">\\(a\\)</span> and <span class="math-inline">\\(b\\)</span> are both constants between 0 and 1.

Suppose that in the long run, <span class="math-inline">\\(\displaystyle\frac{25}{60}\\)</span> of the time is spent in state 1, <span class="math-inline">\\(\displaystyle\frac{21}{60}\\)</span> of the time is spent in state 2, and <span class="math-inline">\\(\displaystyle\frac{14}{60}\\)</span> of the time is spent in state 3.

Find the values of <span class="math-inline">\\(a\\)</span> and <span class="math-inline">\\(b\\)</span>. Show your work, and write your final answers in the boxes provided. Your answers should be numbers with no variables.

<details markdown="1"><summary>Solution</summary>

As discussed in [Chapter 9.3](https://notes.eecs245.org/eigenvalues-and-eigenvectors/markov-chains-adjacency-matrices/), a steady-state distribution is an eigenvector of the adjacency matrix with eigenvalue <span class="math-inline">\\(1\\)</span>, with the additional constraint that its entries sum to <span class="math-inline">\\(1\\)</span>. We are given that the steady-state distribution is

<div class="math-display">
$$
\vec x
=
\begin{bmatrix}
25/60\\\\
21/60\\\\
14/60
\end{bmatrix}
$$
</div>

 which already sums to <span class="math-inline">\\(1\\)</span>. The adjacency matrix for this Markov chain is

<div class="math-display">
$$
A=
\begin{bmatrix}
1-a & 1-b & 0\\\\
a & 0 & 1\\\\
0 & b & 0
\end{bmatrix}
$$
</div>

 So we need to choose <span class="math-inline">\\(a\\)</span> and <span class="math-inline">\\(b\\)</span> so that <span class="math-inline">\\(A\vec x=1\vec x=\vec x\\)</span>. This gives

<div class="math-display">
$$
\begin{bmatrix}
1-a & 1-b & 0\\\\
a & 0 & 1\\\\
0 & b & 0
\end{bmatrix}
\begin{bmatrix}
25/60\\\\
21/60\\\\
14/60
\end{bmatrix}
=
\begin{bmatrix}
25/60\\\\
21/60\\\\
14/60
\end{bmatrix}
$$
</div>

 or equivalently,

<div class="math-display">
$$
\begin{cases}
(1-a)\frac{25}{60}+(1-b)\frac{21}{60}=\frac{25}{60}\\\\
a\frac{25}{60}+\frac{14}{60}=\frac{21}{60}\\\\
b\frac{21}{60}=\frac{14}{60}
\end{cases}
$$
</div>

 The second equation gives

<div class="math-display">
$$
a\frac{25}{60}=\frac{7}{60}
\qquad\Rightarrow\qquad
a=\frac{7}{25}
$$
</div>

 The third equation gives

<div class="math-display">
$$
b=\frac{14}{21}=\frac{2}{3}
$$
</div>

 These values also satisfy the first equation, since

<div class="math-display">
$$
(1-\frac{7}{25})\frac{25}{60}+(1-\frac{2}{3})\frac{21}{60}
=
\frac{18}{60}+\frac{7}{60}
=
\frac{25}{60}
$$
</div>

</details>

---

## Problem 12 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">11 pts</span>

Suppose <span class="math-inline">\\(A\\)</span> is a <span class="math-inline">\\(3 \times 3\\)</span> symmetric matrix with rank <span class="math-inline">\\(2\\)</span>. The eigenspace corresponding to <span class="math-inline">\\(\lambda=9\\)</span> is the plane

<div class="math-display">
$$
2x-y+2z=0
$$
</div>

 Suppose <span class="math-inline">\\(A=Q\Lambda Q^T\\)</span>, where <span class="math-inline">\\(Q\\)</span> is an orthogonal matrix and <span class="math-inline">\\(\Lambda\\)</span> is a diagonal matrix with eigenvalues of <span class="math-inline">\\(A\\)</span> on the diagonal, **sorted** from largest to smallest.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> Find <span class="math-inline">\\(\Lambda\\)</span>. Your answer should be a matrix with no variables.

<div class="math-display">
$$
\Lambda = \boxed{\textbf{\begin{bmatrix}9&0&0\\\\0&9&0\\\\0&0&0\end{bmatrix}}}
$$
</div>

<details markdown="1"><summary>Solution</summary>

Since <span class="math-inline">\\(A\\)</span> is symmetric, the spectral theorem from [Chapter 9.5](https://notes.eecs245.org/eigenvalues-and-eigenvectors/symmetric-matrices-spectral-theorem/) tells us that <span class="math-inline">\\(A\\)</span> is diagonalizable with orthogonal eigenspaces. The eigenspace for <span class="math-inline">\\(\lambda=9\\)</span> is a plane, so it is 2-dimensional. Since <span class="math-inline">\\(A\\)</span> has rank <span class="math-inline">\\(2\\)</span>, it is not invertible, so it has at least one eigenvalue of <span class="math-inline">\\(0\\)</span>. In fact, it has exactly one eigenvalue of <span class="math-inline">\\(0\\)</span>, since the other two eigenvalues are both <span class="math-inline">\\(9\\)</span>.

Since the eigenvalues are sorted from largest to smallest,

<div class="math-display">
$$
\Lambda=
\begin{bmatrix}
9&0&0\\\\
0&9&0\\\\
0&0&0
\end{bmatrix}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">8 pts</span> Consider the vector

<div class="math-display">
$$
\vec v
=
\begin{bmatrix}2 \\\\ 9 \\\\ -2\end{bmatrix}
=
4\begin{bmatrix}1\\\\2\\\\0\end{bmatrix}
-\begin{bmatrix}2\\\\-1\\\\2\end{bmatrix}
$$
</div>

 Find <span class="math-inline">\\(A\vec v\\)</span>. Show your work, and write your final answer in the box provided. Your answer should be a vector with no variables. <em>Hint: What does the spectral theorem tell us?</em>

<div class="math-display">
$$
A\vec v = \boxed{\textbf{\begin{bmatrix}36\\\\72\\\\0\end{bmatrix}}}
$$
</div>

<details markdown="1"><summary>Solution</summary>

The vector <span class="math-inline">\\(\begin{bmatrix}1\\\\2\\\\0\end{bmatrix}\\)</span> is in the eigenspace for <span class="math-inline">\\(\lambda=9\\)</span>, since it satisfies the equation of the eigenspace, <span class="math-inline">\\(2x-y+2z=0\\)</span>:

<div class="math-display">
$$
2(1)-2+2(0)=0
$$
</div>

 This means <span class="math-inline">\\(\begin{bmatrix}1\\\\2\\\\0\end{bmatrix}\\)</span> is an eigenvector of <span class="math-inline">\\(A\\)</span> with eigenvalue <span class="math-inline">\\(9\\)</span>.

The vector <span class="math-inline">\\(\begin{bmatrix}2\\\\-1\\\\2\end{bmatrix}\\)</span> is **orthogonal** to the plane <span class="math-inline">\\(2x-y+2z=0\\)</span> (conveniently, <span class="math-inline">\\(\begin{bmatrix} 2 \\\\ -1 \\\\ 2 \end{bmatrix}\\)</span> contains the coefficients of the plane equation, and the coefficients of the plane equation define a vector orthogonal to the plane). The spectral theorem tells us that this vector is in the eigenspace corresponding to <span class="math-inline">\\(\lambda=0\\)</span>, because **eigenvectors for different eigenvalues are orthogonal for symmetric matrices**. Therefore,

<div class="math-display">
$$
\begin{align*}
A\vec{v}
&=
A\left(4\begin{bmatrix}1\\\\2\\\\0\end{bmatrix}
-\begin{bmatrix}2\\\\-1\\\\2\end{bmatrix}\right) \\\\
&=
4\underbrace{A\begin{bmatrix}1\\\\2\\\\0\end{bmatrix}}_{\substack{\text{eigenvector} \\\\ \lambda = 9}}
- \underbrace{A\begin{bmatrix}2\\\\-1\\\\2\end{bmatrix}}_{\substack{\text{eigenvector} \\\\ \lambda = 0}} \\\\
&=
4\cdot 9\begin{bmatrix}1\\\\2\\\\0\end{bmatrix}
- 0\begin{bmatrix}2\\\\-1\\\\2\end{bmatrix} \\\\
&=
\begin{bmatrix}36\\\\72\\\\0\end{bmatrix}
\end{align*}
$$
</div>

</details>

</div>
</div>

</div>

---

## Problem 13 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>

Let <span class="math-inline">\\(\tilde X\\)</span> be a <span class="math-inline">\\(4 \times 2\\)</span> centered matrix (i.e. in which each column has a mean of 0) with columns <span class="math-inline">\\(\vec a\\)</span> and <span class="math-inline">\\(\vec b\\)</span>:

<div class="math-display">
$$
\tilde X = \begin{bmatrix} \mid & \mid \\\\ \vec a & \vec b \\\\ \mid & \mid \end{bmatrix}
$$
</div>

 Suppose <span class="math-inline">\\(\tilde X = U \Sigma V^T\\)</span> is the singular value decomposition of <span class="math-inline">\\(\tilde X\\)</span>, <span class="math-inline">\\(\vec v&#95;1 = \begin{bmatrix}3/5\\\\4/5\end{bmatrix}\\)</span> is the first column of <span class="math-inline">\\(V\\)</span>, and <span class="math-inline">\\(\sigma&#95;1 = 10\\)</span> is the largest singular value.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> How many possible vectors are there for <span class="math-inline">\\(\vec v&#95;2\\)</span>, the second column of <span class="math-inline">\\(V\\)</span>?

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 1</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 2</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 3</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 4</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> infinitely many <span class="math-inline">\\(\vec v&#95;2\\)</span>'s are possible</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 1</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> 2</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 3</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 4</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> infinitely many <span class="math-inline">\\(\vec v&#95;2\\)</span>'s are possible</span></div>

Since <span class="math-inline">\\(V\\)</span> is an orthogonal matrix, its columns must be unit vectors that are orthogonal to each other. In <span class="math-inline">\\(\mathbb{R}^2\\)</span>, there are exactly two unit vectors orthogonal to <span class="math-inline">\\(\begin{bmatrix}3/5\\\\4/5\end{bmatrix}\\)</span>, namely <span class="math-inline">\\(\begin{bmatrix}-4/5\\\\3/5\end{bmatrix}\\)</span> and <span class="math-inline">\\(\begin{bmatrix}4/5\\\\-3/5\end{bmatrix}\\)</span>. So there are two possible vectors for <span class="math-inline">\\(\vec{v}&#95;2\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">5 pts</span> Write <span class="math-inline">\\(\vec u&#95;1\\)</span>, the first column of <span class="math-inline">\\(U\\)</span>, as a linear combination of the columns of <span class="math-inline">\\(\tilde X\\)</span>. Show your work, and fill in each box with a number with no variables.

<details markdown="1"><summary>Solution</summary>

Recall that the key relationship linking the first column of <span class="math-inline">\\(U\\)</span> and the first column of <span class="math-inline">\\(V\\)</span> in <span class="math-inline">\\(\tilde X = U \Sigma V^T\\)</span> is

<div class="math-display">
$$
\tilde{X}\vec{v}_1=\sigma_1\vec{u}_1
$$
</div>

 This means

<div class="math-display">
$$
\vec{u}_1=\frac{1}{\sigma_1}\tilde{X}\vec{v}_1
$$
</div>

 Since the columns of <span class="math-inline">\\(\tilde{X}\\)</span> are <span class="math-inline">\\(\vec{a}\\)</span> and <span class="math-inline">\\(\vec{b}\\)</span>,

<div class="math-display">
$$
\tilde{X}\vec{v}_1
=
\tilde{X}\begin{bmatrix}3/5\\\\4/5\end{bmatrix}
=
\frac{3}{5}\vec{a}+\frac{4}{5}\vec{b}
$$
</div>

 and since <span class="math-inline">\\(\sigma&#95;1=10\\)</span>,

<div class="math-display">
$$
\vec{u}_1
=
\frac{1}{10}\left(\frac{3}{5}\vec{a}+\frac{4}{5}\vec{b}\right)
=
\frac{3}{50}\vec{a}+\frac{2}{25}\vec{b}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Given the information above, what is the maximum possible variance of principal component <span class="math-inline">\\(2\\)</span>? Give your answer as a number with no variables.

maximum possible variance of principal component <span class="math-inline">\\(2\\)</span> =

<details markdown="1"><summary>Solution</summary>

[Chapter 10.4](https://notes.eecs245.org/singular-value-decomposition/principal-components-analysis/) tells us that the variance of principal component <span class="math-inline">\\(j\\)</span> is

<div class="math-display">
$$
\frac{\sigma_j^2}{n}
$$
</div>

We also know that the singular values are sorted from largest to smallest, so <span class="math-inline">\\(\sigma&#95;1 \geq \sigma&#95;2\\)</span>. So, the variance of principal component <span class="math-inline">\\(2\\)</span>, <span class="math-inline">\\(\frac{\sigma&#95;2^2}{n}\\)</span>, is **at most** equal to the variance of principal component <span class="math-inline">\\(1\\)</span>, <span class="math-inline">\\(\frac{\sigma&#95;1^2}{n}\\)</span>.

Therefore, the maximum possible variance of principal component <span class="math-inline">\\(2\\)</span> is the variance of principal component <span class="math-inline">\\(1\\)</span>:

<div class="math-display">
$$
\frac{\sigma_1^2}{n}=\frac{10^2}{4}=25
$$
</div>

</details>

</div>
</div>

</div>

---

## Problem 14 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span>

What is one topic you studied a lot for that was not on the Final Exam? **Blank answers will receive no credit!**

Congrats on completing the Final Exam for EECS 245! We'll really miss you; please stay in touch.

Feel free to draw us a picture about EECS 245 in the box below.

{% endraw %}
