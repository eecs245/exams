---
layout: minimal
title: "Chapter 6: Linear Transformations and Projections"
description: "Practice problems for Chapter 6: Linear Transformations and Projections."
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
</style>
<nav class="exam-breadcrumb" aria-label="Breadcrumb">
<a href="/">← Back</a>
</nav>

# Chapter 6: Linear Transformations and Projections

*Topics: linear transformations, inverses, projecting onto column space, complete solution to the normal equations*

Problems below are collected from past exams; each links back to its full exam. Solutions are in the dropdowns.

## Problems

- [FA25 MT1 · Problem 5](#fa25-mt1--problem-5-back-to-normal-12-pts)
- [FA25 MT2 · Problem 5](#fa25-mt2--problem-5-orthodontist-12-pts)
- [WN26 MT1 · Problem 3](#wn26-mt1--problem-3-12-pts)
- [WN26 MT1 · Problem 5](#wn26-mt1--problem-5-12-pts)
- [WN26 MT2 · Problem 4](#wn26-mt2--problem-4-13-pts)
- [WN26 Final · Problem 6](#wn26-final--problem-6-12-pts-mt2-redemption)
- [WN26 Final · Problem 5](#wn26-final--problem-5-11-pts-mt2-redemption)
- [SP26 MT2 · Problem 4](#sp26-mt2--problem-4-14-pts)
- [SP26 Final · Problem 6](#sp26-final--problem-6-6-pts-mt2-redemption)
- [SP26 Final · Problem 7](#sp26-final--problem-7-12-pts-mt2-redemption)

---

## FA25 MT1 · Problem 5: Back to Normal <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>

<p class="worksheet-source">From <a href="/exams/fa25-mt1/">FA25 MT1</a></p>

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
<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 1</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 2</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 3</span></div>

2.  Show your work in the box below. English explanations are not enough.

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 1</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 2</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> 3</span></div>

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

## FA25 MT2 · Problem 5: Ortho\...dontist? <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>

<p class="worksheet-source">From <a href="/exams/fa25-mt2/">FA25 MT2</a></p>

Let <span class="math-inline">\\(A = \begin{bmatrix} 1 &amp; 0 \\\\ 1 &amp; 4 \\\\ 1 &amp; 4 \\\\ 1 &amp; 4 \end{bmatrix}\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Find a matrix <span class="math-inline">\\(Q\\)</span> such that <span class="math-inline">\\(\text{colsp}(Q) = \text{colsp}(A)\\)</span> and <span class="math-inline">\\(Q^TQ = I\\)</span>. Show your work and <span class="math-inline">\\(\boxed{\text{circle}}\\)</span> your final answer, which should be a matrix with two columns and no variables. <em>Hint: One of the columns may involve square roots.</em>

<details markdown="1"><summary>Solution</summary>

Since we want <span class="math-inline">\\(Q^TQ = I\\)</span>, we're looking for a matrix <span class="math-inline">\\(Q\\)</span> with two columns that are orthogonal to each other and are both unit vectors.

The "standard" way to answer this part is to use the Gram-Schmidt process, first introduced in Homework 7, Problem 4. But, since <span class="math-inline">\\(A\\)</span> only has two columns, it's okay if you forgot about the specifics, and instead realized the core of Gram-Schmidt, which takes advantage of the fact that **the error when projecting <span class="math-inline">\\(\vec u\\)</span> onto <span class="math-inline">\\(\vec v\\)</span> is orthogonal to <span class="math-inline">\\(\vec v\\)</span>**.

Let

<div class="math-display">
$$
\vec v = \begin{bmatrix} 1 \\\\ 1 \\\\ 1 \\\\ 1 \end{bmatrix}
\qquad
\vec u = \begin{bmatrix} 0 \\\\ 4 \\\\ 4 \\\\ 4 \end{bmatrix}
$$
</div>

Then the projection of <span class="math-inline">\\(\vec u\\)</span> onto <span class="math-inline">\\(\vec v\\)</span> is

<div class="math-display">
$$
\vec p = \frac{\vec u \cdot \vec v}{\vec v \cdot \vec v}\vec v
= \frac{0\cdot 1 + 4\cdot 1 + 4\cdot 1 + 4\cdot 1}{1^2+1^2+1^2+1^2}
\begin{bmatrix} 1 \\\\ 1 \\\\ 1 \\\\ 1 \end{bmatrix}
= \frac{12}{4}
\begin{bmatrix} 1 \\\\ 1 \\\\ 1 \\\\ 1 \end{bmatrix}
= 3
\begin{bmatrix} 1 \\\\ 1 \\\\ 1 \\\\ 1 \end{bmatrix}
$$
</div>

So the error vector is

<div class="math-display">
$$
\vec e = \vec u - \vec p
=
\begin{bmatrix} 0 \\\\ 4 \\\\ 4 \\\\ 4 \end{bmatrix}
-
\begin{bmatrix} 3 \\\\ 3 \\\\ 3 \\\\ 3 \end{bmatrix}
=
\begin{bmatrix} -3 \\\\ 1 \\\\ 1 \\\\ 1 \end{bmatrix}
$$
</div>

This vector <span class="math-inline">\\(\vec e\\)</span> is orthogonal to <span class="math-inline">\\(\vec v\\)</span>, and together <span class="math-inline">\\(\vec v\\)</span> and <span class="math-inline">\\(\vec e\\)</span> have the same span as <span class="math-inline">\\(\text{colsp}(A)\\)</span>. To make the columns orthonormal, we normalize both vectors:

<div class="math-display">
$$
\|\vec v\| = \sqrt{1^2+1^2+1^2+1^2} = 2
\qquad
\|\vec e\| = \sqrt{(-3)^2+1^2+1^2+1^2} = \sqrt{12}
$$
</div>

Therefore, one valid matrix <span class="math-inline">\\(Q\\)</span> is

<div class="math-display">
$$
\boxed{
Q=
\begin{bmatrix}
1/2 & -3/\sqrt{12} \\\\
1/2 & 1/\sqrt{12} \\\\
1/2 & 1/\sqrt{12} \\\\
1/2 & 1/\sqrt{12}
\end{bmatrix}
}
$$
</div>

Another common solution is to observe that the vectors

<div class="math-display">
$$
\begin{bmatrix} 1 \\\\ 0 \\\\ 0 \\\\ 0 \end{bmatrix}
\qquad \text{and} \qquad
\begin{bmatrix} 0 \\\\ 1 \\\\ 1 \\\\ 1 \end{bmatrix}
$$
</div>

 are orthogonal to each other and span <span class="math-inline">\\(\text{colsp}(A)\\)</span>. Normalizing these two vectors gives another valid answer:

<div class="math-display">
$$
\boxed{
\begin{bmatrix}
1 & 0 \\\\
0 & 1/\sqrt{3} \\\\
0 & 1/\sqrt{3} \\\\
0 & 1/\sqrt{3}
\end{bmatrix}
}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">2 pts</span> True or False: The matrix <span class="math-inline">\\(Q\\)</span> you found above is an orthogonal matrix.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> False</span></div>

No matter how you find <span class="math-inline">\\(Q\\)</span> in part **a)**, the answer is false, because <span class="math-inline">\\(Q\\)</span> is not a square matrix, so it cannot be orthogonal!

For <span class="math-inline">\\(Q\\)</span> to be orthogonal, we'd need **both** <span class="math-inline">\\(Q^TQ = I\\)</span> **and** <span class="math-inline">\\(QQ^T = I\\)</span>. Since <span class="math-inline">\\(Q\\)</span> is not square, these can't both be true at the same time (the dimensions don't match, since the former would be <span class="math-inline">\\(2 \times 2\\)</span> while the latter would be <span class="math-inline">\\(4 \times 4\\)</span>).
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Let <span class="math-inline">\\(R = \begin{bmatrix} r&#95;1 &amp; \boxed{r&#95;2} \\\\ \boxed{r&#95;3} &amp; r&#95;4 \end{bmatrix}\\)</span> be a <span class="math-inline">\\(2 \times 2\\)</span> matrix such that <span class="math-inline">\\(A = QR\\)</span>, where <span class="math-inline">\\(Q\\)</span> is the matrix you found above.

Find <span class="math-inline">\\(r&#95;2\\)</span> and <span class="math-inline">\\(r&#95;3\\)</span>. Give your answers as scalars without variables.

<span class="math-inline">\\(r&#95;2 = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;, \qquad r&#95;3 = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>

<details markdown="1"><summary>Solution</summary>

**We ended up giving full credit to everyone for this problem, since there's no unique answer, and it's difficult to answer this correctly if you found an invalid <span class="math-inline">\\(Q\\)</span>.**

The main idea being assessed here, taken from Homework 7, Problem 4, is that if <span class="math-inline">\\(Q\\)</span> is a matrix such that <span class="math-inline">\\(\text{colsp}(Q) = \text{colsp}(A)\\)</span> and <span class="math-inline">\\(Q^T Q = I\\)</span>, then

<div class="math-display">
$$
A = QR \implies Q^TA = Q^TQR \implies R = Q^TA
$$
</div>

As we saw in that homework problem, **if you use Gram-Schmidt to find <span class="math-inline">\\(Q\\)</span>**, <span class="math-inline">\\(R\\)</span> is an **upper triangular** matrix, meaning that <span class="math-inline">\\(r&#95;3 = 0\\)</span>. (We won't elaborate on this here: read the solutions to Homework 7, Problem 4.)

For two different <span class="math-inline">\\(Q\\)</span>'s, we'll find the corresponding <span class="math-inline">\\(R\\)</span>'s to give you some sample possible answers.

-   For

<div class="math-display">
$$
Q =
        \begin{bmatrix}
        1/2 & -3/\sqrt{12} \\\\
        1/2 & 1/\sqrt{12} \\\\
        1/2 & 1/\sqrt{12} \\\\
        1/2 & 1/\sqrt{12}
        \end{bmatrix}
$$
</div>

 **which did result from Gram-Schmidt**,

<div class="math-display">
$$
R = Q^TA
        =
        \begin{bmatrix}
        2 & 6 \\\\
        0 & 12/\sqrt{12}
        \end{bmatrix}
        =
        \begin{bmatrix}
        2 & 6 \\\\
        0 & \sqrt{12}
        \end{bmatrix}
$$
</div>

 This <span class="math-inline">\\(R\\)</span> **is** upper triangular.

-   For

<div class="math-display">
$$
Q =
        \begin{bmatrix}
        1 & 0 \\\\
        0 & 1/\sqrt{3} \\\\
        0 & 1/\sqrt{3} \\\\
        0 & 1/\sqrt{3}
        \end{bmatrix}
$$
</div>

 **which did not result from Gram-Schmidt**,

<div class="math-display">
$$
R = Q^TA
        =
        \begin{bmatrix}
        1 & 0 \\\\
        \sqrt{3} & 4\sqrt{3}
        \end{bmatrix}
$$
</div>

 This <span class="math-inline">\\(R\\)</span> **is not** upper triangular.
</details>

</div>
</div>

</div>

---

## WN26 MT1 · Problem 3 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>

<p class="worksheet-source">From <a href="/exams/wn26-mt1/">WN26 MT1</a></p>

Consider the following two planes, <span class="math-inline">\\(P&#95;1\\)</span> and <span class="math-inline">\\(P&#95;2\\)</span>, in <span class="math-inline">\\(\mathbb{R}^3\\)</span>.

-   <span class="math-inline">\\(P&#95;1\\)</span> is the plane spanned by the vectors <span class="math-inline">\\(\begin{bmatrix} 3 \\\\ 2 \\\\ 0 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\begin{bmatrix} 6 \\\\ -4 \\\\ -3 \end{bmatrix}\\)</span>.

-   <span class="math-inline">\\(P&#95;2\\)</span> is the plane defined by the equation <span class="math-inline">\\(5x + 3y - z = 0\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Find the equation of <span class="math-inline">\\(P&#95;1\\)</span> in standard form, i.e. <span class="math-inline">\\(ax + by + cz + d = 0\\)</span>. Show your work and <span class="math-inline">\\(\boxed{\text{circle}}\\)</span> your final answer.

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(2x - 3y + 8z = 0\\)</span>.

As discussed in [Chapter 4.4](https://notes.eecs245.org/linear-independence/lines-planes-hyperplanes/), the solution is to take the cross product of the two vectors used to span the plane; this will give us a vector <span class="math-inline">\\(\begin{bmatrix} a \\\\ b \\\\ c \end{bmatrix}\\)</span> that is orthogonal to both vectors, and therefore both will satisfy <span class="math-inline">\\(ax + by + cz + d = 0\\)</span>. We know <span class="math-inline">\\(d = 0\\)</span> since the span of a set of vectors must contain the origin.

<div class="math-display">
$$
\begin{bmatrix} 3 \\\\ 2 \\\\ 0 \end{bmatrix} \times \begin{bmatrix} 6 \\\\ -4 \\\\ -3 \end{bmatrix} = \begin{bmatrix} 2 \cdot (-3) - 0 \cdot (-4) \\\\ 0 \cdot 6 - 3 \cdot (-3) \\\\ 3 \cdot (-4) - 2 \cdot 6 \end{bmatrix} = \begin{bmatrix} -6 \\\\ 9 \\\\ -24 \end{bmatrix}
$$
</div>

So, the equation of <span class="math-inline">\\(P&#95;1\\)</span> is <span class="math-inline">\\(-6x + 9y - 24z = 0\\)</span>, or simplified, <span class="math-inline">\\(\boxed{2x - 3y + 8z = 0}\\)</span>. To verify, we should plug in both vectors to make sure they satisfy the equation:

<div class="math-display">
$$
2(3) - 3(2) + 8(0) = 6 - 6 + 0 = 0, \qquad 2(6) - 3(-4) + 8(-3) = 12 + 12 - 24 = 0
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Planes <span class="math-inline">\\(P&#95;1\\)</span> and <span class="math-inline">\\(P&#95;2\\)</span> intersect at a line. Find the equation of this line in parametric form. Show your work and <span class="math-inline">\\(\boxed{\text{circle}}\\)</span> your final answer. <em>Hint: This can be done without knowing the answer to the previous part.</em>

<details markdown="1"><summary>Solution</summary>

<div class="math-display">
$$
L = t \begin{bmatrix} 1 \\\\ -2 \\\\ -1 \end{bmatrix}, \quad t \in \mathbb{R}
$$
</div>

 (where the direction vector could be scaled by any non-zero scalar)

There are a few possible techniques here.

**(i)** We can find the intersection of the two planes by solving the system of equations:

<div class="math-display">
$$
\begin{align*}
5x + 3y - z   &= 0 \\\\
2x - 3y + 8z &= 0
\end{align*}
$$
</div>

Adding both equations gives

<div class="math-display">
$$
7x + 7z = 0 \implies z = -x
$$
</div>

We know that the system will have infinitely many solutions, so we can let our "parameter" be <span class="math-inline">\\(x\\)</span>. So far, we know two of the three components of the line: <span class="math-inline">\\(x\\)</span> is the free variable, and <span class="math-inline">\\(z = -x\\)</span>. Finally, let's solve for <span class="math-inline">\\(y\\)</span> in terms of <span class="math-inline">\\(x\\)</span>.

<div class="math-display">
$$
5x + 3y + x = 0 \implies 6x + 3y = 0 \implies y = - 2x
$$
</div>

Therefore, the parametric equation of the line is

<div class="math-display">
$$
L = \begin{bmatrix} x \\\\ -2x \\\\ -x \end{bmatrix} = x \begin{bmatrix} 1 \\\\ -2 \\\\ -1 \end{bmatrix}, \quad x \in \mathbb{R}
$$
</div>

**(ii)** Another solution is to recognize that any point on the first plane can be written as a linear combination of the two vectors that span the plane, i.e.

<div class="math-display">
$$
s \begin{bmatrix} 3 \\\\ 2 \\\\ 0 \end{bmatrix} + t \begin{bmatrix} 6 \\\\ -4 \\\\ -3 \end{bmatrix} = \begin{bmatrix} 3s + 6t \\\\ 2s - 4t \\\\ -3t \end{bmatrix}
$$
</div>

Any vector on the first plane can be written in the form above. For a vector to be in both planes (i.e. in the intersection), it must be able to be written in the form above **and** satisfy the equation of the second plane, <span class="math-inline">\\(5x + 3y - z = 0\\)</span>.

<div class="math-display">
$$
\begin{align*}
5(3s + 6t) + 3(2s - 4t) - (-3t) &= 0 \\\\
15s + 30t + 6s - 12t + 3t &= 0 \\\\
21s + 21t &= 0 \\\\
t &= -s
\end{align*}
$$
</div>

So, as long as we pick <span class="math-inline">\\(s\\)</span> and <span class="math-inline">\\(t\\)</span> such that <span class="math-inline">\\(t = -s\\)</span>, the resulting vector, <span class="math-inline">\\(\begin{bmatrix} 3s + 6t \\\\ 2s - 4t \\\\ -3t \end{bmatrix}\\)</span>, will be in both planes. There are infinitely many pairs of such <span class="math-inline">\\(s\\)</span> and <span class="math-inline">\\(t\\)</span> -- <span class="math-inline">\\(1\\)</span> and <span class="math-inline">\\(-1\\)</span>, <span class="math-inline">\\(2\\)</span> and <span class="math-inline">\\(-2\\)</span>, etc. -- and these fill out the line of intersection. To find one of them, let <span class="math-inline">\\(s = 1\\)</span> and <span class="math-inline">\\(t = -1\\)</span>:

<div class="math-display">
$$
\begin{bmatrix} 3(1) + 6(-1) \\\\ 2(1) - 4(-1) \\\\ -3(-1) \end{bmatrix} = \begin{bmatrix} 3 - 6 \\\\ 2 + 4 \\\\ 3 \end{bmatrix} = \begin{bmatrix} -3 \\\\ 6 \\\\ 3 \end{bmatrix}
$$
</div>

Therefore, the parametric equation of the line is

<div class="math-display">
$$
L = t \begin{bmatrix} -3 \\\\ 6 \\\\ 3 \end{bmatrix}, \quad t \in \mathbb{R}
$$
</div>

which is equivalent to

<div class="math-display">
$$
L = t \begin{bmatrix} 1 \\\\ -2 \\\\ -1 \end{bmatrix}, \quad t \in \mathbb{R}
$$
</div>

This is the same line we found earlier, just with a scaled direction vector, which doesn't change the line.

**(iii)** A final solution is to (1) find a vector that is perpendicular to each plane (i.e. a normal vector), and (2) take the cross product of those two vectors. This will give us a vector that is in both planes, and therefore spans the intersecting line, which we know must also pass through the origin.

<div class="math-display">
$$
\begin{align*}
\begin{bmatrix} 5 \\\\ 3 \\\\ -1 \end{bmatrix} \times \begin{bmatrix} 2 \\\\ -3 \\\\ 8 \end{bmatrix} = \begin{bmatrix} 3 \cdot 8 - (-1) \cdot (-3) \\\\ (-1) \cdot 2 - 5 \cdot 8 \\\\ 5 \cdot (-3) - 3 \cdot 2 \end{bmatrix} = \begin{bmatrix} 21 \\\\ -42 \\\\ -21 \end{bmatrix} = 21 \begin{bmatrix} 1 \\\\ -2 \\\\ -1 \end{bmatrix}
\end{align*}
$$
</div>

So, once again, we find that <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ -2 \\\\ -1 \end{bmatrix}\\)</span> is a direction vector for the line of intersection.
</details>

</div>
</div>

</div>

---

## WN26 MT1 · Problem 5 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>

<p class="worksheet-source">From <a href="/exams/wn26-mt1/">WN26 MT1</a></p>

Suppose <span class="math-inline">\\(\vec u, \vec v \in \mathbb{R}^n\\)</span>. Let <span class="math-inline">\\(\vec p\\)</span> be the projection of <span class="math-inline">\\(\vec u\\)</span> onto <span class="math-inline">\\(\vec v\\)</span>. Furthermore, we know that:

<div class="math-display">
$$
\underbrace{\lVert \vec v \rVert = 2}_{\text{length of } \vec v \: (\text{not } \vec u)} \qquad \lVert \vec p \rVert = 3
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Find <span class="math-inline">\\(| \vec u \cdot \vec v |\\)</span>. Show your work and <span class="math-inline">\\(\boxed{\text{circle}}\\)</span> your final answer, which should be a number with no variables.

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(|\vec u \cdot \vec v| = 6\\)</span>.

Let's start with the formula for <span class="math-inline">\\(\vec p\\)</span>.

<div class="math-display">
$$
\vec p = \frac{\vec u \cdot \vec v}{\vec v \cdot \vec v} \vec v = \frac{\vec u \cdot \vec v}{\lVert \vec v \rVert^2} \vec v
$$
</div>

We know that <span class="math-inline">\\(\lVert \vec p \rVert = 3\\)</span>, so let's try and find the magnitude of <span class="math-inline">\\(\vec p\\)</span> in the formula above, which will allow us to learn more about <span class="math-inline">\\(\vec u \cdot \vec v\\)</span>.

The key to remember that <span class="math-inline">\\(\lVert k x \rVert = |k| \lVert x \rVert\\)</span> for any scalar <span class="math-inline">\\(k\\)</span> and vector <span class="math-inline">\\(x\\)</span>. The absolute value is necessary because the scalar <span class="math-inline">\\(k\\)</span> could be negative, but the length of a vector is always non-negative.

<div class="math-display">
$$
\lVert \vec p \rVert = \left| \frac{\vec u \cdot \vec v}{\lVert \vec v \rVert^2} \right| \lVert \vec v \rVert = \left| \frac{\vec u \cdot \vec v}{2^2} \right| 2 = \left| \frac{\vec u \cdot \vec v}{4} \right| 2 = \frac{\left| \vec u \cdot \vec v \right|}{2}
$$
</div>

So, we know that <span class="math-inline">\\(\frac{\left| \vec u \cdot \vec v \right|}{2} = 3\\)</span>, which means that <span class="math-inline">\\(\boxed{\left| \vec u \cdot \vec v \right| = 6}\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> For each pair of vectors, determine whether they are orthogonal, linearly dependent, or neither. Make sure to select **one bubble per row**.

|  | pair of vectors | orthogonal | linearly dependent | neither |
|:--:|:---|:--:|:--:|:--:|
| <span class="math-inline">\\(i\\)</span> | <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec u - \vec p\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> |
| <span class="math-inline">\\(ii\\)</span> | <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v - \vec p\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> |
| <span class="math-inline">\\(iii\\)</span> | <span class="math-inline">\\(\vec v\\)</span> and <span class="math-inline">\\(\vec u - \vec p\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> |
| <span class="math-inline">\\(iv\\)</span> | <span class="math-inline">\\(\vec v\\)</span> and <span class="math-inline">\\(\vec v - \vec p\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> |
| <span class="math-inline">\\(v\\)</span> | <span class="math-inline">\\(\vec p\\)</span> and <span class="math-inline">\\(\vec u - \vec p\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> |
| <span class="math-inline">\\(vi\\)</span> | <span class="math-inline">\\(\vec p\\)</span> and <span class="math-inline">\\(\vec v - \vec p\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> |

<details markdown="1"><summary>Solution</summary>

The key fact about orthogonality when it comes to projections is that the error vector --- here, <span class="math-inline">\\(\vec e = \vec u - \vec p\\)</span> --- is orthogonal to the vector we're projecting onto, <span class="math-inline">\\(\vec v\\)</span>.

This means that <span class="math-inline">\\(\vec v\\)</span> and <span class="math-inline">\\(\vec u - \vec p\\)</span> are orthogonal (iii). But, <span class="math-inline">\\(\vec p\\)</span> is a scalar multiple of <span class="math-inline">\\(\vec v\\)</span>, so <span class="math-inline">\\(\vec p\\)</span> and <span class="math-inline">\\(\vec u - \vec p\\)</span> are also orthogonal (v).

Remember that <span class="math-inline">\\(\vec p\\)</span> is a scalar multiple of <span class="math-inline">\\(\vec v\\)</span>, so <span class="math-inline">\\(\vec v - \vec p\\)</span> is a scalar multiple of <span class="math-inline">\\(\vec v\\)</span> too. So, <span class="math-inline">\\(\vec v\\)</span> and <span class="math-inline">\\(\vec v - \vec p\\)</span> are linearly dependent (iv), as are <span class="math-inline">\\(\vec p\\)</span> and <span class="math-inline">\\(\vec v - \vec p\\)</span> (vi).

Now, we need to address (i) and (ii), which ask about <span class="math-inline">\\(\vec u\\)</span>'s relation to <span class="math-inline">\\(\vec u - \vec p\\)</span> and <span class="math-inline">\\(\vec v - \vec p\\)</span>, respectively. <span class="math-inline">\\(\vec u - \vec p\\)</span> is the error vector of the projection, which in general is orthogonal to <span class="math-inline">\\(\vec v\\)</span> and neither orthogonal nor linearly dependent with <span class="math-inline">\\(\vec u\\)</span>.

The only possible "edge case" here is when <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> are orthogonal, in which case <span class="math-inline">\\(\vec p = \frac{\vec u \cdot \vec v}{\vec v \cdot \vec v} \vec v = \frac{0}{\vec v \cdot \vec v} \vec v = \vec 0\\)</span>, which would mean that <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v - \vec p\\)</span> are orthogonal and <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec u - \vec p\\)</span> are the same vector and thus linearly dependent. However, we know that <span class="math-inline">\\(\vec p \neq \vec 0\\)</span> since <span class="math-inline">\\(\lVert \vec p \rVert = 3 &gt; 0\\)</span>. So, this edge case doesn't apply to this problem, and therefore <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec u - \vec p\\)</span> are neither orthogonal nor linearly dependent (i), and same with <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v - \vec p\\)</span> (ii).
</details>

</div>
</div>

</div>

---

## WN26 MT2 · Problem 4 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">13 pts</span>

<p class="worksheet-source">From <a href="/exams/wn26-mt2/">WN26 MT2</a></p>

Suppose <span class="math-inline">\\(X\\)</span> is some <span class="math-inline">\\(3 \times d\\)</span> matrix, for some integer <span class="math-inline">\\(d\\)</span>. Let

<div class="math-display">
$$
\vec y = \begin{bmatrix} 9 \\\\ -5 \\\\ 3 \end{bmatrix}
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">5 pts</span> Which of the following **could** be the projection of <span class="math-inline">\\(\vec y\\)</span> onto <span class="math-inline">\\(\text{colsp}(X)\\)</span>?

Select an answer, then briefly justify your answer in the space provided using properties of projections. Correct answers without justification may not receive full credit.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} 5 \\\\ -7 \\\\ 4 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} 7 \\\\ -7 \\\\ 4 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} 6 \\\\ -7 \\\\ 4 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} 6 \\\\ -7 \\\\ 3 \end{bmatrix}\\)</span></span></div>

<details markdown="1"><summary>Solution</summary>

<span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} 6 \\\\ -7 \\\\ 3 \end{bmatrix}\\)</span>

If <span class="math-inline">\\(\vec p\\)</span> is the projection of <span class="math-inline">\\(\vec y\\)</span> onto <span class="math-inline">\\(\text{colsp}(X)\\)</span>, then the error

<div class="math-display">
$$
\vec y - \vec p
$$
</div>

 must be orthogonal to all vectors in <span class="math-inline">\\(\text{colsp}(X)\\)</span>, and hence orthogonal to <span class="math-inline">\\(\vec p\\)</span> itself.

For the third option, <span class="math-inline">\\(\vec p = \begin{bmatrix} 6 \\\\ -7 \\\\ 4 \end{bmatrix}\\)</span>, we have

<div class="math-display">
$$
\vec p = \begin{bmatrix} 6 \\\\ -7 \\\\ 4 \end{bmatrix} \implies
\vec y - \vec p = \begin{bmatrix} 9 \\\\ -5 \\\\ 3 \end{bmatrix} - \begin{bmatrix} 6 \\\\ -7 \\\\ 4 \end{bmatrix} = \begin{bmatrix} 3 \\\\ 2 \\\\ -1 \end{bmatrix}
$$
</div>

 The dot product of <span class="math-inline">\\(\vec p\\)</span> and <span class="math-inline">\\(\vec y - \vec p\\)</span> is

<div class="math-display">
$$
\begin{align*}
\vec p \cdot (\vec y - \vec p) = \begin{bmatrix} 6 \\\\ -7 \\\\ 4 \end{bmatrix} \cdot \begin{bmatrix} 3 \\\\ 2 \\\\ -1 \end{bmatrix}
&= 18 - 14 - 4 = 0
\end{align*}
$$
</div>

So <span class="math-inline">\\(\vec p = \begin{bmatrix} 6 \\\\ -7 \\\\ 4 \end{bmatrix}\\)</span> could be the projection of <span class="math-inline">\\(\vec y\\)</span> onto <span class="math-inline">\\(\text{colsp}(X)\\)</span>. If you repeat this calculation for the other three options, you'll find that <span class="math-inline">\\(\vec p\\)</span> and <span class="math-inline">\\(\vec y - \vec p\\)</span> are not orthogonal.
</details>

In each of the remaining parts, identify whether the statement is True or False and justify your answer in the space provided. Correct answers without justification may not receive full credit.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> If the projection of <span class="math-inline">\\(\vec y\\)</span> onto <span class="math-inline">\\(\text{colsp}(X)\\)</span> is <span class="math-inline">\\(\vec y\\)</span> itself, then <span class="math-inline">\\(\text{rank}(X)\\)</span> must be 3.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> False</span></div>

This is false. If the projection of <span class="math-inline">\\(\vec y\\)</span> onto <span class="math-inline">\\(\text{colsp}(X)\\)</span> is <span class="math-inline">\\(\vec y\\)</span> itself, that only tells us that <span class="math-inline">\\(\vec y \in \text{colsp}(X)\\)</span>.

But <span class="math-inline">\\(\text{colsp}(X)\\)</span> could still be a 1-dimensional or 2-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^3\\)</span> that happens to contain <span class="math-inline">\\(\vec y\\)</span>. For example, if <span class="math-inline">\\(\text{colsp}(X) = \text{span}\left(\left\lbrace \vec y \right\rbrace\right)\\)</span>, then the projection of <span class="math-inline">\\(\vec y\\)</span> is still <span class="math-inline">\\(\vec y\\)</span>, but <span class="math-inline">\\(\text{rank}(X)=1\\)</span>, not 3.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> If <span class="math-inline">\\(\text{rank}(X) = 3\\)</span>, then the projection of <span class="math-inline">\\(\vec y\\)</span> onto <span class="math-inline">\\(\text{colsp}(X)\\)</span> must be <span class="math-inline">\\(\vec y\\)</span> itself.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

This is true. If <span class="math-inline">\\(\text{rank}(X)=3\\)</span> and <span class="math-inline">\\(X\\)</span> is a <span class="math-inline">\\(3 \times d\\)</span> matrix, then <span class="math-inline">\\(\text{colsp}(X)\\)</span> is a 3-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^3\\)</span>. The only 3-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^3\\)</span> is all of <span class="math-inline">\\(\mathbb{R}^3\\)</span>.

But, this means every vector in <span class="math-inline">\\(\mathbb{R}^3\\)</span>, including <span class="math-inline">\\(\vec y\\)</span>, is in <span class="math-inline">\\(\text{colsp}(X)\\)</span>. Therefore, the projection of <span class="math-inline">\\(\vec y\\)</span> onto <span class="math-inline">\\(\text{colsp}(X)\\)</span> is just <span class="math-inline">\\(\vec y\\)</span> itself.
</details>

</div>
</div>

</div>

---

## WN26 Final · Problem 6 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span> <span class="badge" data-flag="mt2-redemption" style="background-color: #9A3324; color: #FFFFFF; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">MT2 Redemption</span>

<p class="worksheet-source">From <a href="/exams/wn26-final/">WN26 Final</a></p>

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

<span class="math-inline">\\(\vec p = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;  \vec x^{(1)} + \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;  \vec x^{(2)} + \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;  \vec x^{(3)}\\)</span>

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

<span class="math-inline">\\(\text{set of all possible } \vec w^{\ast} = \left\lbrace \&#95;\&#95;\&#95;\&#95;\&#95;\&#95; + t  \&#95;\&#95;\&#95;\&#95;\&#95;\&#95; : t \in \mathbb{R} \right\rbrace\\)</span>.

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

## WN26 Final · Problem 5 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">11 pts</span> <span class="badge" data-flag="mt2-redemption" style="background-color: #9A3324; color: #FFFFFF; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">MT2 Redemption</span>

<p class="worksheet-source">From <a href="/exams/wn26-final/">WN26 Final</a></p>

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

<span class="math-inline">\\(\text{rank}(A) = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;  \dim(\text{nullsp}(A^T)) = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>

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
\vec a^{(1)} & \square  \quad  \\\\
\vec a^{(2)} & \square  \quad  \\\\
\vec a^{(3)} & \square  \quad  \\\\
\vec a^{(4)} & \square  \quad  \\\\
\vec a^{(5)} & \square  \quad
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

## SP26 MT2 · Problem 4 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">14 pts</span>

<p class="worksheet-source">From <a href="/exams/sp26-mt2/">SP26 MT2</a></p>

Suppose <span class="math-inline">\\(X\\)</span> is a matrix such that

<div class="math-display">
$$
X^TX =
\begin{bmatrix}
4 & 0\\\\
0 & 4
\end{bmatrix}
\qquad
XX^T =
\begin{bmatrix}
1 & \sqrt{3} & 0 & 0 \\\\
\sqrt{3} & 3 & 0 & 0 \\\\
0 & 0 & 0 & 0 \\\\
0 & 0 & 0 & 4
\end{bmatrix}
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> Fill in each blank with an integer with no variables.

X has \_\_\_\_\_\_ rows, \_\_\_\_\_\_ columns, and <span class="math-inline">\\(\text{rank}(X) =\\)</span> \_\_\_\_\_\_.

<details markdown="1"><summary>Solution</summary>

Recall that if <span class="math-inline">\\(X\\)</span> is an <span class="math-inline">\\(n \times d\\)</span> matrix, then <span class="math-inline">\\(X^T X\\)</span> is an <span class="math-inline">\\(d \times d\\)</span> matrix containing the dot products of all pairs of <span class="math-inline">\\(X\\)</span>'s columns, and <span class="math-inline">\\(XX^T\\)</span> is an <span class="math-inline">\\(n \times n\\)</span> matrix containing the dot products of all pairs of <span class="math-inline">\\(X\\)</span>'s rows.

Here, since <span class="math-inline">\\(X^T X\\)</span> is <span class="math-inline">\\(2 \times 2\\)</span>, <span class="math-inline">\\(X\\)</span> must have 2 columns and since <span class="math-inline">\\(XX^T\\)</span> is <span class="math-inline">\\(4 \times 4\\)</span>, <span class="math-inline">\\(X\\)</span> must have 4 rows. So <span class="math-inline">\\(X\\)</span> is <span class="math-inline">\\(4 \times 2\\)</span>.

Also, recall that <span class="math-inline">\\(\text{rank}(X) = \text{rank}(X^T X) = \text{rank}(XX^T)\\)</span>, as proven [here](https://notes.eecs245.org/matrices/null-space-rank-nullity/#example-rank-of-x-tx). Since <span class="math-inline">\\(\text{rank}(X^T X) = 2\\)</span> (as it is a diagonal matrix with 2 non-zero entries), we have that <span class="math-inline">\\(\text{rank}(X)=2\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> For each statement below, determine whether it is true or false.

1.  The columns of <span class="math-inline">\\(X\\)</span> are all orthogonal to each other.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

2.  The columns of <span class="math-inline">\\(X\\)</span> are orthonormal.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> False</span></div>

**(i)** This is true. The entries of <span class="math-inline">\\(X^TX\\)</span> are the dot products of the columns of <span class="math-inline">\\(X\\)</span> with each other. Since the off-diagonal entries are 0, the columns of <span class="math-inline">\\(X\\)</span> are orthogonal to each other.

**(ii)** This is false. The diagonal entries of <span class="math-inline">\\(X^TX\\)</span> are the squared lengths of the columns of <span class="math-inline">\\(X\\)</span>. Since both diagonal entries are 4, both columns have length 2, not 1.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">7 pts</span> Suppose <span class="math-inline">\\(P\\)</span> is the matrix that projects onto the column space of <span class="math-inline">\\(X\\)</span>. In other words, for any <span class="math-inline">\\(\vec y\\)</span> of the appropriate shape, <span class="math-inline">\\(P \vec y\\)</span> is the projection of <span class="math-inline">\\(\vec y\\)</span> onto <span class="math-inline">\\(\text{colsp}(X)\\)</span>. **Find <span class="math-inline">\\(P\\)</span>**. Show your work, and <span class="math-inline">\\(\boxed{\text{circle}}\\)</span> your final answer, which should be a matrix with no variables.

<details markdown="1"><summary>Solution</summary>

Since <span class="math-inline">\\(X\\)</span> has linearly independent columns, the projection matrix onto <span class="math-inline">\\(\text{colsp}(X)\\)</span> is

<div class="math-display">
$$
P = X(X^T X)^{-1}X^T
$$
</div>

 Here,

<div class="math-display">
$$
X^TX = 4I
\qquad \Longrightarrow \qquad
(X^TX)^{-1} = \frac{1}{4}I
$$
</div>

 So,

<div class="math-display">
$$
P = X\left(\frac{1}{4}I\right)X^T
=
\frac{1}{4}XX^T
$$
</div>

 Using the given value of <span class="math-inline">\\(XX^T\\)</span>,

<div class="math-display">
$$
P =
\begin{bmatrix}
1/4 & \sqrt{3}/4 & 0 & 0 \\\\
\sqrt{3}/4 & 3/4 & 0 & 0 \\\\
0 & 0 & 0 & 0 \\\\
0 & 0 & 0 & 1
\end{bmatrix}
$$
</div>

Note that we're only able to answer this problem because <span class="math-inline">\\(X^TX\\)</span> is a multiple of the identity matrix, so its inverse is just a multiple of the identity matrix. If <span class="math-inline">\\(X^TX\\)</span> was not a multiple of the identity matrix, even if it was diagonal, we wouldn't be able to find <span class="math-inline">\\(P\\)</span> using just the information in this problem.
</details>

</div>
</div>

</div>

---

## SP26 Final · Problem 6 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> <span class="badge" data-flag="mt2-redemption" style="background-color: #9A3324; color: #FFFFFF; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">MT2 Redemption</span>

<p class="worksheet-source">From <a href="/exams/sp26-final/">SP26 Final</a></p>

Find the area enclosed by the polygon with vertices <span class="math-inline">\\((0, 0)\\)</span>, <span class="math-inline">\\((4, 6)\\)</span>, <span class="math-inline">\\((1, 8)\\)</span>, and <span class="math-inline">\\((-3, 2)\\)</span>. Show your work, and write your answer in the box provided.

<div class="math-display">
$$
\text{area} = \_\_\_\_\_\_
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
<img src="imgs/sp26-final-q06/polygon-determinant-area.png" alt="image" style="width: 75%; max-width: 100%;">
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

## SP26 Final · Problem 7 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span> <span class="badge" data-flag="mt2-redemption" style="background-color: #9A3324; color: #FFFFFF; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">MT2 Redemption</span>

<p class="worksheet-source">From <a href="/exams/sp26-final/">SP26 Final</a></p>

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

{% endraw %}
