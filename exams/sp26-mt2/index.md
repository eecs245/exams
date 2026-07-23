---
layout: minimal
title: "Spring 2026 Midterm 2"
description: "Midterm 2 problems."
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

# Spring 2026 Midterm 2

**administered**

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/exams/sp26-mt2.pdf" target="_blank">View as PDF ✏️</a>
<a class="btn btn-info assignment-pdf-button" href="/resources/exams/sp26-mt2-solutions.pdf" target="_blank">Solutions PDF ✅</a>
</div>

{: .yellow }
<div markdown="1">
**Instructions**

-   This exam consists of 7 problems, worth 100 points, spread across 14 pages (7 sheets of paper).

-   You have 120 minutes to complete this exam, unless you have extended-time accommodations through SSD.

-   Write your uniqname in the top right corner of each page.

-   For free response problems, **you must show all of your work**, and <span class="math-inline">\\(\boxed{\text{circle}}\\)</span> your final answer. We will not grade work that appears elsewhere, and you may lose points if your work is not shown.

-   For multiple choice problems, completely fill in bubbles and square boxes; if we cannot tell which option(s) you selected, you may lose points.



-   You may refer to **two double-sided 8.5x11" handwritten notes sheets**. Other than that, you may not refer to any other resources or technology during the exam (no phones, watches, or calculators).
</div>

---

## Problems

- [Problem 1](#problem-1-12-pts)
- [Problem 2](#problem-2-16-pts)
- [Problem 3](#problem-3-12-pts)
- [Problem 4](#problem-4-14-pts)
- [Problem 5](#problem-5-19-pts)
- [Problem 6](#problem-6-12-pts)
- [Problem 7](#problem-7-15-pts)

---

## Problem 1 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>

Suppose <span class="math-inline">\\(k\\)</span> is a real number. Let

<div class="math-display">
$$
A =
\begin{bmatrix}
1 & k+1 \\\\
1 & 2k+3
\end{bmatrix}
$$
</div>

In each part, you are provided with information about <span class="math-inline">\\(A\\)</span>. **Your job is to find the value of <span class="math-inline">\\(k\\)</span> that satisfies the given condition.** Show your work in the space provided, and write your final answer in the bottom-right corner of the box. Your answers should be numbers with no variables.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span>
<span class="math-inline">\\(\det(A) = 14\\)</span>.

<div class="math-display">

<div class="math-display">
$$
4cm
$$
</div>

</div>

<div class="math-display">

<div class="math-display">
$$
3cm
$$
</div>

</div>

<div class="math-display">

<div class="math-display">
$$
1cm
$$
</div>

</div>

<details markdown="1"><summary>Solution</summary>

Since <span class="math-inline">\\(A\\)</span> is a <span class="math-inline">\\(2 \times 2\\)</span> matrix, its determinant is

<div class="math-display">
$$
\begin{align*}
\det(A) &= 1(2k+3) - 1(k+1) \\\\
&= k + 2
\end{align*}
$$
</div>

We're told that <span class="math-inline">\\(\det(A) = 14\\)</span>, so

<div class="math-display">
$$
\begin{align*}
k + 2 &= 14 \\\\
k &= 12
\end{align*}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span>
<span class="math-inline">\\(A\\)</span> is not invertible.

<div class="math-display">

<div class="math-display">
$$
4cm
$$
</div>

</div>

<div class="math-display">

<div class="math-display">
$$
3cm
$$
</div>

</div>

<div class="math-display">

<div class="math-display">
$$
1cm
$$
</div>

</div>

<details markdown="1"><summary>Solution</summary>

If <span class="math-inline">\\(A\\)</span> is not invertible, then <span class="math-inline">\\(\det(A) = 0\\)</span>. From part **a)**,

<div class="math-display">
$$
\det(A) = k + 2
$$
</div>

 so

<div class="math-display">
$$
\begin{align*}
k + 2 &= 0 \\\\
k &= -2
\end{align*}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> The bottom-right entry of <span class="math-inline">\\(A^{-1}\\)</span> is <span class="math-inline">\\(1/4\\)</span>.

<div class="math-display">

<div class="math-display">
$$
5cm
$$
</div>

</div>

<div class="math-display">

<div class="math-display">
$$
3cm
$$
</div>

</div>

<div class="math-display">

<div class="math-display">
$$
1cm
$$
</div>

</div>

<details markdown="1"><summary>Solution</summary>

The inverse of a <span class="math-inline">\\(2 \times 2\\)</span> matrix is

<div class="math-display">
$$
\begin{bmatrix}
a & b \\\\
c & d
\end{bmatrix}^{-1}
=
\frac{1}{ad-bc}
\begin{bmatrix}
d & -b \\\\
-c & a
\end{bmatrix}
$$
</div>

 Here, <span class="math-inline">\\(\det(A)=k+2\\)</span>, so

<div class="math-display">
$$
A^{-1}
=
\frac{1}{k+2}
\begin{bmatrix}
2k+3 & -(k+1) \\\\
-1 & 1
\end{bmatrix}
$$
</div>

 The bottom-right entry is <span class="math-inline">\\(\frac{1}{k+2}\\)</span>, and we're told that this equals <span class="math-inline">\\(\frac{1}{4}\\)</span>. So,

<div class="math-display">
$$
\begin{align*}
\frac{1}{k+2} &= \frac{1}{4} \\\\
k+2 &= 4 \\\\
k &= 2
\end{align*}
$$
</div>

</details>

</div>
</div>

</div>

---

## Problem 2 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">16 pts</span>

Suppose <span class="math-inline">\\(A\\)</span> is a <span class="math-inline">\\(3 \times 3\\)</span> matrix whose null space is the plane

<div class="math-display">
$$
5x - y + 3z = 0
$$
</div>

In other words, <span class="math-inline">\\(\text{nullsp}(A) = \left\lbrace \begin{bmatrix} x \\\\ y \\\\ z \end{bmatrix} \mid   5x - y + 3z = 0 \right\rbrace\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> Determine the following values. Give your answers as integers with no variables.

<span class="math-inline">\\(\text{rank}(A) =\\)</span>

<div class="math-display">

<div class="math-display">
$$
1.5cm
$$
</div>

</div>

 <span class="math-inline">\\(\text{dim}(\text{nullsp}(A)) =\\)</span>

<div class="math-display">

<div class="math-display">
$$
1.5cm
$$
</div>

</div>

<details markdown="1"><summary>Solution</summary>

The null space is a plane in <span class="math-inline">\\(\mathbb{R}^3\\)</span>, which is a <span class="math-inline">\\(2\\)</span>-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^3\\)</span>. So,

<div class="math-display">
$$
\dim(\text{nullsp}(A)) = 2
$$
</div>

 Since <span class="math-inline">\\(A\\)</span> has 3 columns, the rank-nullity theorem gives

<div class="math-display">
$$
\begin{align*}
\text{rank}(A) + \dim(\text{nullsp}(A)) &= 3 \\\\
\text{rank}(A) + 2 &= 3 \\\\
\text{rank}(A) &= 1
\end{align*}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> State one basis for <span class="math-inline">\\(\text{nullsp}(A)\\)</span>. Your answer should be a list of vectors with no variables.

<span class="math-inline">\\(\text{one basis for }\text{nullsp}(A) =\\)</span>

<div class="math-display">

<div class="math-display">
$$
5cm
$$
</div>

</div>

<details markdown="1"><summary>Solution</summary>

The null space consists of all vectors satisfying

<div class="math-display">
$$
5x-y+3z = 0
$$
</div>

 A basis for the null space, then, consists of any two linearly independent vectors that satisfy this equation. <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ 5 \\\\ 0 \end{bmatrix}\\)</span> satisfies it, since <span class="math-inline">\\(5 \cdot 1 - (5) + 3 \cdot 0 = 0\\)</span>, and similarly <span class="math-inline">\\(\begin{bmatrix} 0 \\\\ 3 \\\\ 1 \end{bmatrix}\\)</span> satisfies it. Therefore, one basis is

<div class="math-display">
$$
\left\{ \begin{bmatrix} 1 \\\\ 5 \\\\ 0 \end{bmatrix}, \begin{bmatrix} 0 \\\\ 3 \\\\ 1 \end{bmatrix} \right\}
$$
</div>

</details>

though there are infinitely many possible answers.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> State one basis for <span class="math-inline">\\(\text{colsp}(A^T)\\)</span>, the row space of <span class="math-inline">\\(A\\)</span>. Your answer should be a list of vectors with no variables.

<span class="math-inline">\\(\text{one basis for }\text{colsp}(A^T) =\\)</span>

<div class="math-display">

<div class="math-display">
$$
5cm
$$
</div>

</div>

<details markdown="1"><summary>Solution</summary>

A key fact to remember here is that the row space and null space of a matrix are orthogonal complements, as discussed in [Chapter 5.4](https://notes.eecs245.org/matrices/null-space-rank-nullity/#example-orthogonal-complements). This means that every element in the row space must be orthogonal to every element in the null space.

We're given that the null space consists of all vectors <span class="math-inline">\\(\vec x = \begin{bmatrix} x \\\\ y \\\\ z \end{bmatrix}\\)</span> such that <span class="math-inline">\\(5x-y+3z = 0\\)</span>. Equivalently, this means that <span class="math-inline">\\(\begin{bmatrix} 5 \\\\ -1 \\\\ 3 \end{bmatrix} \cdot \vec x = 0\\)</span>. So, this means that every element in the null space is orthogonal to <span class="math-inline">\\(\begin{bmatrix} 5 \\\\ -1 \\\\ 3 \end{bmatrix}\\)</span>, so <span class="math-inline">\\(\begin{bmatrix} 5 \\\\ -1 \\\\ 3 \end{bmatrix}\\)</span> must be in the row space. The row space is <span class="math-inline">\\(1\\)</span>-dimensional, since <span class="math-inline">\\(\text{rank}(A)=1\\)</span>. So, one basis is <span class="math-inline">\\(\left\lbrace \begin{bmatrix} 5 \\\\ -1 \\\\ 3 \end{bmatrix} \right\rbrace\\)</span>.

If you didn't remember this key fact, no problem --- you could have arrived at this conclusion from scratch on the exam. We know <span class="math-inline">\\(A\\)</span> is <span class="math-inline">\\(3 \times 3\\)</span>, so suppose it looks like

<div class="math-display">
$$
A = \begin{bmatrix} a_{11} & a_{12} & a_{13} \\\\ a_{21} & a_{22} & a_{23} \\\\ a_{31} & a_{32} & a_{33} \end{bmatrix}
$$
</div>

If <span class="math-inline">\\(\vec x = \begin{bmatrix} x \\\\ y \\\\ z \end{bmatrix}\\)</span> is in the null space, it must mean that <span class="math-inline">\\(A \vec x = \vec 0\\)</span>:

<div class="math-display">
$$
A \vec x = \begin{bmatrix} a_{11} & a_{12} & a_{13} \\\\ a_{21} & a_{22} & a_{23} \\\\ a_{31} & a_{32} & a_{33} \end{bmatrix} \begin{bmatrix} x \\\\ y \\\\ z \end{bmatrix} = \begin{bmatrix} a_{11}x + a_{12}y + a_{13}z \\\\ a_{21}x + a_{22}y + a_{23}z \\\\ a_{31}x + a_{32}y + a_{33}z \end{bmatrix} = \begin{bmatrix} 0 \\\\ 0 \\\\ 0 \end{bmatrix}
$$
</div>

From here, you see that the dot product of each row of <span class="math-inline">\\(A\\)</span> with <span class="math-inline">\\(\vec x\\)</span> must be 0, so each row of <span class="math-inline">\\(A\\)</span> must be orthogonal to <span class="math-inline">\\(\vec x\\)</span>. The plane form of the null space, <span class="math-inline">\\(5x-y+3z=0\\)</span>, tells you that <span class="math-inline">\\(\begin{bmatrix} 5 \\\\ -1 \\\\ 3 \end{bmatrix}\\)</span> is orthogonal to every vector in the null space, so putting these facts together gives us that <span class="math-inline">\\(\begin{bmatrix} 5 \\\\ -1 \\\\ 3 \end{bmatrix}\\)</span> is in the row space. Together with the fact that the row space is <span class="math-inline">\\(1\\)</span>-dimensional, since <span class="math-inline">\\(\text{rank}(A)=1\\)</span>, we have that a basis is <span class="math-inline">\\(\left\lbrace \begin{bmatrix} 5 \\\\ -1 \\\\ 3 \end{bmatrix} \right\rbrace\\)</span>.

All other possible answers involve (non-zero) scalar multiples of <span class="math-inline">\\(\begin{bmatrix} 5 \\\\ -1 \\\\ 3 \end{bmatrix}\\)</span>.
</details>

Recall, <span class="math-inline">\\(A\\)</span> is a <span class="math-inline">\\(3 \times 3\\)</span> matrix whose null space is the plane <span class="math-inline">\\(5x-y+3z=0\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Suppose that

<div class="math-display">
$$
A \begin{bmatrix} 3 \\\\ 0 \\\\ 0 \end{bmatrix} = \begin{bmatrix} 15 \\\\ 30 \\\\ 0 \end{bmatrix}
$$
</div>

 Find <span class="math-inline">\\(A\\)</span>. Show your work, and <span class="math-inline">\\(\boxed{\text{circle}}\\)</span> your final answer, which should be a matrix with no variables.

<details markdown="1"><summary>Solution</summary>

Since <span class="math-inline">\\(\text{rank}(A)=1\\)</span> and the row space is

<div class="math-display">
$$
\text{span}\left( \left\{ \begin{bmatrix} 5 \\\\ -1 \\\\ 3 \end{bmatrix} \right\} \right),
$$
</div>

 each row of <span class="math-inline">\\(A\\)</span> must be a scalar multiple of <span class="math-inline">\\(\begin{bmatrix} 5 &amp; -1 &amp; 3 \end{bmatrix}\\)</span>. So, for some constants <span class="math-inline">\\(a\\)</span>, <span class="math-inline">\\(b\\)</span>, and <span class="math-inline">\\(c\\)</span>,

<div class="math-display">
$$
A =
\begin{bmatrix}
5a & -a & 3a \\\\
5b & -b & 3b \\\\
5c & -c & 3c
\end{bmatrix}
$$
</div>

 We're told that

<div class="math-display">
$$
A \begin{bmatrix} 3 \\\\ 0 \\\\ 0 \end{bmatrix}
=
\begin{bmatrix} 15 \\\\ 30 \\\\ 0 \end{bmatrix}
$$
</div>

 The left-hand side is 3 times the first column of <span class="math-inline">\\(A\\)</span>, so the first column of <span class="math-inline">\\(A\\)</span> is

<div class="math-display">
$$
\begin{bmatrix} 5 \\\\ 10 \\\\ 0 \end{bmatrix}
$$
</div>

 This gives

<div class="math-display">
$$
5a = 5, \qquad 5b = 10, \qquad 5c = 0
$$
</div>

 so <span class="math-inline">\\(a=1\\)</span>, <span class="math-inline">\\(b=2\\)</span>, and <span class="math-inline">\\(c=0\\)</span>. Therefore,

<div class="math-display">
$$
A =
\begin{bmatrix}
5 & -1 & 3 \\\\
10 & -2 & 6 \\\\
0 & 0 & 0
\end{bmatrix}
$$
</div>

</details>

</div>
</div>

</div>

---

## Problem 3 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>

Suppose <span class="math-inline">\\(A\\)</span> is an <span class="math-inline">\\(n \times n\\)</span> matrix.

For each statement below, determine whether it is true or false. If true, prove that it is true. If false, give a counterexample or a short explanation.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> If <span class="math-inline">\\(A\\)</span> is symmetric, then <span class="math-inline">\\(A^2\\)</span> must be symmetric.

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

This is true. Since <span class="math-inline">\\(A\\)</span> is symmetric, <span class="math-inline">\\(A^T = A\\)</span>. So,

<div class="math-display">
$$
(A^2)^T = (AA)^T = A^T A^T = AA = A^2
$$
</div>

 Therefore, <span class="math-inline">\\(A^2\\)</span> is symmetric.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> If <span class="math-inline">\\(A^2\\)</span> is symmetric, then <span class="math-inline">\\(A\\)</span> must be symmetric.

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> False</span></div>

This is false. For example, let

<div class="math-display">
$$
A =
  \begin{bmatrix}
  0 & 1 \\\\
  -1 & 0
  \end{bmatrix}
$$
</div>

 This matrix is not symmetric, but

<div class="math-display">
$$
A^2 =
  \begin{bmatrix}
  -1 & 0 \\\\
  0 & -1
  \end{bmatrix}
$$
</div>

 which is symmetric.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> If <span class="math-inline">\\(\vec x \in \text{nullsp}(A^T)\\)</span> and <span class="math-inline">\\(\vec y \in \text{colsp}(A)\\)</span>, then <span class="math-inline">\\(\vec x\\)</span> and <span class="math-inline">\\(\vec y\\)</span> are orthogonal.

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

This is true. If <span class="math-inline">\\(\vec y \in \text{colsp}(A)\\)</span>, then <span class="math-inline">\\(\vec y = A\vec v\\)</span> for some vector <span class="math-inline">\\(\vec v\\)</span>. Since <span class="math-inline">\\(\vec x \in \text{nullsp}(A^T)\\)</span>, we know <span class="math-inline">\\(A^T \vec x = \vec 0\\)</span>. So,

<div class="math-display">
$$
\vec x \cdot \vec y
  =
  \vec x^T A \vec v
  =
  (A^T \vec x)^T \vec v
  =
  \vec 0^T \vec v
  =
  0
$$
</div>

 Therefore, <span class="math-inline">\\(\vec x\\)</span> and <span class="math-inline">\\(\vec y\\)</span> are orthogonal.
</details>

</div>
</div>

</div>

---

## Problem 4 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">14 pts</span>

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

X has

<div class="math-display">

<div class="math-display">
$$
2cm
$$
</div>

</div>

 rows,

<div class="math-display">

<div class="math-display">
$$
2cm
$$
</div>

</div>

 columns, and <span class="math-inline">\\(\text{rank}(X) =\\)</span>

<div class="math-display">

<div class="math-display">
$$
2cm
$$
</div>

</div>

.

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

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

2.  The columns of <span class="math-inline">\\(X\\)</span> are orthonormal.

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> False</span></div>

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

## Problem 5 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">19 pts</span>

Suppose we're given a dataset with <span class="math-inline">\\(n = 5\\)</span> rows, and we use it to fit a multiple linear regression model with two features and an intercept term.

<div class="math-display">
$$
h(\vec x_i) = w_0 + w_1 x_i^{(1)} + w_2 x_i^{(2)}
$$
</div>

 Let <span class="math-inline">\\(X\\)</span> be the corresponding <span class="math-inline">\\(5 \times 3\\)</span> design matrix and <span class="math-inline">\\(\vec y \in \mathbb{R}^5\\)</span> be the corresponding observation vector. Suppose the matrix <span class="math-inline">\\(P\\)</span> that projects onto the column space of <span class="math-inline">\\(X\\)</span> is

<div class="math-display">
$$
P = \begin{bmatrix} 1/4 & 1/4 & 1/4 & 1/4 & 0 \\\\ 1/4 & 1/4 & 1/4 & 1/4 & 0 \\\\ 1/4 & 1/4 & 1/4 & 1/4 & 0 \\\\ 1/4 & 1/4 & 1/4 & 1/4 & 0 \\\\ 0 & 0 & 0 & 0 & 1 \end{bmatrix}
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> **In parts a) and b) only**, suppose the projection of <span class="math-inline">\\(\vec y\\)</span> onto <span class="math-inline">\\(\text{colsp}(X)\\)</span> is <span class="math-inline">\\(\vec p = \begin{bmatrix} 3 \\\\ 3 \\\\ 3 \\\\ 3 \\\\ 3 \end{bmatrix}\\)</span>. There are infinitely many such vectors <span class="math-inline">\\(\vec y\\)</span>. State one possible vector <span class="math-inline">\\(\vec y\\)</span> **whose five components are all different**. Give your answer as a vector with no variables.

one possible vector <span class="math-inline">\\(\vec y =\\)</span>

<div class="math-display">

<div class="math-display">
$$
5cm
$$
</div>

</div>

<details markdown="1"><summary>Solution</summary>

For any vector <span class="math-inline">\\(\vec y\\)</span>, multiplying by <span class="math-inline">\\(P\\)</span> averages the first four components of <span class="math-inline">\\(\vec y\\)</span> and leaves the fifth component unchanged:

<div class="math-display">
$$
P\vec y =
\begin{bmatrix}
\displaystyle \frac{y_1+y_2+y_3+y_4}{4} \\\\ \\\\
\displaystyle \frac{y_1+y_2+y_3+y_4}{4} \\\\ \\\\
\displaystyle \frac{y_1+y_2+y_3+y_4}{4} \\\\ \\\\
\displaystyle \frac{y_1+y_2+y_3+y_4}{4} \\\\ \\\\
\displaystyle y_5
\end{bmatrix}
$$
</div>

 We want this to equal <span class="math-inline">\\(\begin{bmatrix} 3 \\\\ 3 \\\\ 3 \\\\ 3 \\\\ 3 \end{bmatrix}\\)</span>, so the first four components of <span class="math-inline">\\(\vec y\\)</span> need to have average 3, and the fifth component needs to be 3.

One possible choice is

<div class="math-display">
$$
\vec y =
\begin{bmatrix}
0 \\\\
1 \\\\
5 \\\\
6 \\\\
3
\end{bmatrix}
$$
</div>

 The first four components have average 3, and all five components are different. There are infinitely many possible answers, though.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> Let <span class="math-inline">\\(\vec y\\)</span> and <span class="math-inline">\\(\vec p \\)</span> be as defined in part (a). True or false: <span class="math-inline">\\(X^T (\vec p - \vec y) = \vec 0\\)</span>.

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

This is true. If <span class="math-inline">\\(\vec p\\)</span> is the projection of <span class="math-inline">\\(\vec y\\)</span> onto <span class="math-inline">\\(\text{colsp}(X)\\)</span>, then the error vector <span class="math-inline">\\(\vec y - \vec p\\)</span> is orthogonal to every vector in <span class="math-inline">\\(\text{colsp}(X)\\)</span>. This is how we arrived at the normal equations, <span class="math-inline">\\(X^TX \vec w = X^T \vec y\\)</span>. Here, this means

<div class="math-display">
$$
X^T(\vec y - \vec p) = \vec 0
$$
</div>

 Multiplying by <span class="math-inline">\\(-1\\)</span> gives

<div class="math-display">
$$
X^T(\vec p - \vec y) = \vec 0
$$
</div>

</details>

For the rest of the problem, suppose that both <span class="math-inline">\\(\vec w^{\ast} = \begin{bmatrix} 2 \\\\ 3 \\\\ 1 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec w' = \begin{bmatrix} 3 \\\\ 1 \\\\ 0 \end{bmatrix}\\)</span> are both optimal parameter vectors that minimize mean squared error.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Which of these vectors are in <span class="math-inline">\\(\text{nullsp}(X)\\)</span>? **Select all** that apply.

<div class="mc-options"><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} 2 \\\\ 3 \\\\ 1 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} 5 \\\\ 4 \\\\ 1 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ -2 \\\\ -1 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} 4 \\\\ 6 \\\\ 2 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} -2 \\\\ 4 \\\\ 2 \end{bmatrix}\\)</span></span></div>

<details markdown="1"><summary>Solution</summary>

<span class="mc-square mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} -2 \\\\ 4 \\\\ 2 \end{bmatrix}\\)</span>

If two parameter vectors are both solutions to the normal equation, their difference is in <span class="math-inline">\\(\text{nullsp}(X)\\)</span>. So,

<div class="math-display">
$$
\vec w' - \vec w^*
=
\begin{bmatrix} 3 \\\\ 1 \\\\ 0 \end{bmatrix}
-
\begin{bmatrix} 2 \\\\ 3 \\\\ 1 \end{bmatrix}
=
\begin{bmatrix} 1 \\\\ -2 \\\\ -1 \end{bmatrix}
\in \text{nullsp}(X)
$$
</div>

Where did this come from? The fact that <span class="math-inline">\\(\vec w'\\)</span> and <span class="math-inline">\\(\vec w^{\ast}\\)</span> are both optimal parameter vectors means that they both result in the same projection of <span class="math-inline">\\(\vec y\\)</span> onto <span class="math-inline">\\(\text{colsp}(X)\\)</span>, so

<div class="math-display">
$$
X \vec w^* = X \vec w'
$$
</div>

But, this means <span class="math-inline">\\(X(\vec w' - \vec w^{\ast}) = \vec 0\\)</span>, which says that <span class="math-inline">\\(\vec w' - \vec w^{\ast}\\)</span> is in <span class="math-inline">\\(\text{nullsp}(X)\\)</span>.

Also, <span class="math-inline">\\(P\\)</span> projects onto <span class="math-inline">\\(\text{colsp}(X)\\)</span>, and <span class="math-inline">\\(P\\)</span> has rank 2. Therefore <span class="math-inline">\\(\text{rank}(X)=2\\)</span> (the logic behind this is described [here](https://notes.eecs245.org/linear-transformations-and-projections/complete-solution/#example-is-p-invertible)). Since <span class="math-inline">\\(X\\)</span> has 3 columns, the rank-nullity theorem gives

<div class="math-display">
$$
\dim(\text{nullsp}(X)) = 3 - 2 = 1
$$
</div>

 So <span class="math-inline">\\(\text{nullsp}(X)\\)</span> is exactly

<div class="math-display">
$$
\text{nullsp}(X) =
\text{span}\left( \left\{ \begin{bmatrix} 1 \\\\ -2 \\\\ -1 \end{bmatrix} \right\} \right)
$$
</div>

 Among the listed choices, the vectors in this span are <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ -2 \\\\ -1 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\begin{bmatrix} -2 \\\\ 4 \\\\ 2 \end{bmatrix}\\)</span>.

The rank-nullity logic wasn't strictly necessary to answer the question; I've included it here for completeness, as it fully justifies why none of the other listed vectors are in <span class="math-inline">\\(\text{nullsp}(X)\\)</span>.
</details>

**The information stated below, above part **d)**, is the same as the information stated on the previous page. It's provided for your convenience.**

Recall, <span class="math-inline">\\(X\\)</span> is a <span class="math-inline">\\(5 \times 3\\)</span> design matrix for the model

<div class="math-display">
$$
h(\vec x_i) = w_0 + w_1 x_i^{(1)} + w_2 x_i^{(2)}
$$
</div>

 Additionally, <span class="math-inline">\\(\vec y \in \mathbb{R}^5\\)</span> is an observation vector, both <span class="math-inline">\\(\vec w^{\ast} = \begin{bmatrix} 2 \\\\ 3 \\\\ 1 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec w' = \begin{bmatrix} 3 \\\\ 1 \\\\ 0 \end{bmatrix}\\)</span> are both optimal parameter vectors that minimize mean squared error, and the matrix <span class="math-inline">\\(P\\)</span> that projects onto the column space of <span class="math-inline">\\(X\\)</span> is

<div class="math-display">
$$
P = \begin{bmatrix} 1/4 & 1/4 & 1/4 & 1/4 & 0 \\\\ 1/4 & 1/4 & 1/4 & 1/4 & 0 \\\\ 1/4 & 1/4 & 1/4 & 1/4 & 0 \\\\ 1/4 & 1/4 & 1/4 & 1/4 & 0 \\\\ 0 & 0 & 0 & 0 & 1 \end{bmatrix}
$$
</div>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">8 pts</span> Find one possible design matrix <span class="math-inline">\\(X\\)</span>, consistent with all of the information above. Show your work, and <span class="math-inline">\\(\boxed{\text{circle}}\\)</span> your final answer, which should be a matrix with no variables.

<details markdown="1"><summary>Solution</summary>

Since <span class="math-inline">\\(P\\)</span> projects onto <span class="math-inline">\\(\text{colsp}(X)\\)</span>, we need <span class="math-inline">\\(\text{colsp}(X) = \text{colsp}(P)\\)</span>. Notice that the result <span class="math-inline">\\(P \vec y\\)</span> for any vector <span class="math-inline">\\(\vec y \in \mathbb{R}^5\\)</span> will have equal first four components (resulting from averaging the original first four components of <span class="math-inline">\\(\vec y\\)</span>) and the fifth component will be unchanged. If we think of the space of possible values of <span class="math-inline">\\(P \vec y\\)</span>, we realize that any <span class="math-inline">\\(P \vec y\\)</span> is of the form

<div class="math-display">
$$
\begin{bmatrix} a \\\\ a \\\\ a \\\\ a \\\\ b \end{bmatrix} = a \begin{bmatrix} 1 \\\\ 1 \\\\ 1 \\\\ 1 \\\\ 0 \end{bmatrix} + b \begin{bmatrix} 0 \\\\ 0 \\\\ 0 \\\\ 0 \\\\ 1 \end{bmatrix}
$$
</div>

This means

<div class="math-display">
$$
\text{colsp}(X) = \text{span}\left( \left\{ \begin{bmatrix} 1 \\\\ 1 \\\\ 1 \\\\ 1 \\\\ 0 \end{bmatrix}, \begin{bmatrix} 0 \\\\ 0 \\\\ 0 \\\\ 0 \\\\ 1 \end{bmatrix} \right\} \right)
$$
</div>

Now, the problem boils down to finding a design matrix <span class="math-inline">\\(X\\)</span> with the above column space, that also meets the other requirements. Here are the other relevant requirements:

**(i)** Since the model has an intercept term, the first column of <span class="math-inline">\\(X\\)</span> should be <span class="math-inline">\\(\vec 1 = \begin{bmatrix} 1 \\\\ 1 \\\\ 1 \\\\ 1 \\\\ 1 \end{bmatrix}\\)</span>.

**(ii)** From part **c)**, we need <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ -2 \\\\ -1 \end{bmatrix} \in \text{nullsp}(X)\\)</span>.

If the columns of <span class="math-inline">\\(X\\)</span> are <span class="math-inline">\\(\vec x^{(0)}\\)</span>, <span class="math-inline">\\(\vec x^{(1)}\\)</span>, and <span class="math-inline">\\(\vec x^{(2)}\\)</span> (we're told <span class="math-inline">\\(X\\)</span> has 3 columns), the first requirement states

<div class="math-display">
$$
\vec x^{(0)} = \begin{bmatrix} 1 \\\\ 1 \\\\ 1 \\\\ 1 \\\\ 1 \end{bmatrix}
$$
</div>

The second requirement states

<div class="math-display">
$$
\underbrace{\begin{bmatrix} | & | & | \\\\ \vec x^{(0)} & \vec x^{(1)} & \vec x^{(2)} \\\\ | & | & | \end{bmatrix}}_{X} \begin{bmatrix} 1 \\\\ -2 \\\\ -1 \end{bmatrix} = \vec 0
$$
</div>

or, in other words, <span class="math-inline">\\(\vec x^{(0)} - 2\vec x^{(1)} - \vec x^{(2)} = \vec 0\\)</span>.

To guarantee <span class="math-inline">\\(\text{colsp}(X)\\)</span> is the span we set out before,

<div class="math-display">
$$
\text{colsp}(X) = \text{span} \left( \left\{ \begin{bmatrix} 1 \\\\ 1 \\\\ 1 \\\\ 1 \\\\ 1 \end{bmatrix}, \begin{bmatrix} 1 \\\\ 1 \\\\ 1 \\\\ 1 \\\\ 0 \end{bmatrix}\right\} \right)
$$
</div>

let's just pick <span class="math-inline">\\(\vec x^{(1)} = \begin{bmatrix} 1 \\\\ 1 \\\\ 1 \\\\ 1 \\\\ 0 \end{bmatrix}\\)</span>. Since <span class="math-inline">\\(\vec x^{(0)} - \vec x^{(1)} = \begin{bmatrix} 0 \\\\ 0 \\\\ 0 \\\\ 0 \\\\ 1 \end{bmatrix}\\)</span>, we have accomplished the goal of finding a design matrix <span class="math-inline">\\(X\\)</span> with the desired column space. With our choices of <span class="math-inline">\\(\vec x^{(0)}\\)</span> and <span class="math-inline">\\(\vec x^{(1)}\\)</span> out of the way, <span class="math-inline">\\(\vec x^{(2)}\\)</span> is fully determined for us:

<div class="math-display">
$$
\vec x^{(0)} - 2 \vec x^{(1)} - \vec x^{(2)} = \vec 0 \implies \vec x^{(2)} = \vec x^{(0)} - 2 \vec x^{(1)} = \begin{bmatrix} 1 \\\\ 1 \\\\ 1 \\\\ 1 \\\\ 1 \end{bmatrix} - 2 \begin{bmatrix} 1 \\\\ 1 \\\\ 1 \\\\ 1 \\\\ 0 \end{bmatrix} = \begin{bmatrix} -1 \\\\ -1 \\\\ -1 \\\\ -1 \\\\ 1 \end{bmatrix}
$$
</div>

Therefore, one possible design matrix is

<div class="math-display">
$$
X =
\begin{bmatrix}
1 & 1 & -1 \\\\
1 & 1 & -1 \\\\
1 & 1 & -1 \\\\
1 & 1 & -1 \\\\
1 & 0 & 1
\end{bmatrix}
$$
</div>

This design matrix has a column space of <span class="math-inline">\\(\text{span} \left( \left\lbrace \begin{bmatrix} 1 \\\\ 1 \\\\ 1 \\\\ 1 \\\\ 1 \end{bmatrix}, \begin{bmatrix} 1 \\\\ 1 \\\\ 1 \\\\ 1 \\\\ 0 \end{bmatrix}\right\rbrace \right)\\)</span>, which is the same as the column space of <span class="math-inline">\\(P\\)</span>. It also has the required null space, which is why it would be wrong to just pick, say,

<div class="math-display">
$$
\begin{bmatrix} 1 & 1 & 0 \\\\ 1 & 1 & 0 \\\\ 1 & 1 & 0 \\\\ 1 & 1 & 0 \\\\ 0 & 0 & 1 \end{bmatrix}
$$
</div>

--- the above matrix has a null space spanned by <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ -1 \\\\ -1 \end{bmatrix}\\)</span>, not <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ -2 \\\\ -1 \end{bmatrix}\\)</span>.
</details>

</div>
</div>

</div>

---

## Problem 6 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>

Suppose <span class="math-inline">\\(A\\)</span> is an <span class="math-inline">\\(n \times d\\)</span> matrix and <span class="math-inline">\\(\vec x \in \mathbb{R}^d\\)</span>. Consider the function <span class="math-inline">\\(f: \mathbb{R}^d \to \mathbb{R}\\)</span> given by

<div class="math-display">
$$
f(\vec x) = \left\|A\vec x\right\|
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">2 pts</span> True or False: <span class="math-inline">\\(f(\vec x)\\)</span> is a linear transformation.

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> False</span></div>

This is false. Recall, a linear transformation must satisfy <span class="math-inline">\\(f(c \vec x) = c f(\vec x)\\)</span> for any scalar <span class="math-inline">\\(c\\)</span>. But, suppose we pick <span class="math-inline">\\(n = d = 1\\)</span>, and let <span class="math-inline">\\(A = [1]\\)</span> (here we're thinking of a <span class="math-inline">\\(1 \times 1\\)</span> matrix as a scalar). Then, <span class="math-inline">\\(f(x)\\)</span> is just the absolute value of the scalar <span class="math-inline">\\(x\\)</span>.

<div class="math-display">
$$
f(x) = |x|
$$
</div>

But, <span class="math-inline">\\(f(-2) = 2\\)</span> is not the same as <span class="math-inline">\\(-2 f(1) = -2\\)</span>. So, this <span class="math-inline">\\(f(x)\\)</span> is not a linear transformation, and thus in general <span class="math-inline">\\(f(\vec x) = \lVert A \vec x \rVert\\)</span> is not a linear transformation.

Another way to think about why <span class="math-inline">\\(f(\vec x)\\)</span> is not linear is to use the fact that <span class="math-inline">\\(\lVert A \vec x \rVert^2 = \vec x^T A^T A \vec x\\)</span>:

<div class="math-display">
$$
f(\vec x) = \sqrt{\vec x^T A^T A \vec x}
$$
</div>

 <span class="math-inline">\\(f(\vec x)\\)</span> is the square root of a quadratic form, which is not linear.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">10 pts</span> Find <span class="math-inline">\\(\nabla f(\vec x)\\)</span>. Assume that <span class="math-inline">\\(A \vec x \neq \vec 0\\)</span>. Show your work, and write your final answer in the bottom-right corner of the box. Your answer should be an expression in terms of <span class="math-inline">\\(A\\)</span>, <span class="math-inline">\\(\vec x\\)</span>, and/or constants. <em>Hint: Start by taking the gradient of <span class="math-inline">\\(\lVert A \vec x \rVert^2\\)</span>, then apply the chain rule.</em>

<div class="math-display">

<div class="math-display">
$$
17cm
$$
</div>

</div>

<div class="math-display">

<div class="math-display">
$$
7cm
$$
</div>

</div>

<div class="math-display">

<div class="math-display">
$$
4cm
$$
</div>

</div>

<details markdown="1"><summary>Solution</summary>

As the hint suggests, let's start by writing

<div class="math-display">
$$
\left\|A\vec x\right\|^2
=
(A\vec x)^T(A\vec x)
=
\vec x^T A^T A \vec x
$$
</div>

 Using the quadratic-form gradient rule,

<div class="math-display">
$$
\nabla \left\|A\vec x\right\|^2 = 2A^TA\vec x
$$
</div>

 Now,

<div class="math-display">
$$
f(\vec x) = \left\|A\vec x\right\|
=
\sqrt{\left\|A\vec x\right\|^2}
$$
</div>

 The chain rule from [Chapter 8.2](https://notes.eecs245.org/gradients/gradients-matrix-vector-operations/#chain-rule-for-vector-to-scalar-functions) states that if <span class="math-inline">\\(f(\vec x) = h(g(\vec x))\\)</span>, where <span class="math-inline">\\(h: \mathbb{R} \to \mathbb{R}\\)</span> and <span class="math-inline">\\(g: \mathbb{R}^d \to \mathbb{R}\\)</span> are both differentiable, then <span class="math-inline">\\(\nabla f(\vec x) = h'(g(\vec x)) \nabla g(\vec x)\\)</span>.

Here, <span class="math-inline">\\(h(x) = \sqrt{x}\\)</span> (so <span class="math-inline">\\(h'(x) = \displaystyle \frac{1}{2\sqrt{x}}\\)</span>) and <span class="math-inline">\\(g(\vec x) = \left\|A\vec x\right\|^2\\)</span>, so

<div class="math-display">
$$
\nabla f(\vec x)
=
\frac{1}{2\sqrt{\left\|A\vec x\right\|^2}}
\left( 2A^TA\vec x \right)
=
\frac{A^TA\vec x}{\left\|A\vec x\right\|}
$$
</div>

</details>

</div>
</div>

</div>

---

## Problem 7 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">15 pts</span>

Let <span class="math-inline">\\(\vec x = \begin{bmatrix} x&#95;1 \\\\ x&#95;2 \end{bmatrix}\\)</span>. Consider the function <span class="math-inline">\\(f: \mathbb{R}^2 \to \mathbb{R}\\)</span> given by

<div class="math-display">
$$
f(\vec x) = c x_1^2 + d x_2^2
$$
</div>

 where <span class="math-inline">\\(c\\)</span> and <span class="math-inline">\\(d\\)</span> are constants. We'd like to use gradient descent to minimize <span class="math-inline">\\(f(\vec x)\\)</span>. For some values of <span class="math-inline">\\(c\\)</span> and <span class="math-inline">\\(d\\)</span>, and some initial guess <span class="math-inline">\\(\vec x^{(0)}\\)</span> and learning rate/step size <span class="math-inline">\\(\alpha\\)</span>, we find that

<div class="math-display">
$$
\vec x^{(1)} = \begin{bmatrix} 4 \\\\ 1 \end{bmatrix}, \qquad \nabla f(\vec x^{(1)}) = \begin{bmatrix} 6 \\\\ -2 \end{bmatrix}, \qquad \vec x^{(2)} = \begin{bmatrix} 2.8 \\\\ 1.4 \end{bmatrix}
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">5 pts</span> Find the value of <span class="math-inline">\\(\alpha\\)</span>. Show your work, and write your final answer in the bottom-right corner of the box. Your answer should be a number with no variables.

<div class="math-display">

<div class="math-display">
$$
6.5cm
$$
</div>

</div>

<div class="math-display">

<div class="math-display">
$$
3cm
$$
</div>

</div>

<div class="math-display">

<div class="math-display">
$$
1cm
$$
</div>

</div>

<details markdown="1"><summary>Solution</summary>

Gradient descent uses the update

<div class="math-display">
$$
\vec x^{(2)} = \vec x^{(1)} - \alpha \nabla f(\vec x^{(1)})
$$
</div>

 Substituting the given values,

<div class="math-display">
$$
\begin{bmatrix} 2.8 \\\\ 1.4 \end{bmatrix}
=
\begin{bmatrix} 4 \\\\ 1 \end{bmatrix}
-
\alpha
\begin{bmatrix} 6 \\\\ -2 \end{bmatrix}
=
\begin{bmatrix} 4 - 6\alpha \\\\ 1 + 2\alpha \end{bmatrix}
$$
</div>

 Using either component,

<div class="math-display">
$$
\begin{align*}
4 - 6\alpha &= 2.8 \\\\
6\alpha &= 1.2 \\\\
\alpha &= \frac{1}{5}
\end{align*}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">5 pts</span> Find the value of <span class="math-inline">\\(d\\)</span> (**not** <span class="math-inline">\\(c\\)</span>). Show your work, and write your final answer in the bottom-right corner of the boxes. Your answer should be a number with no variables.

<div class="math-display">

<div class="math-display">
$$
6.5cm
$$
</div>

</div>

<div class="math-display">

<div class="math-display">
$$
3cm
$$
</div>

</div>

<div class="math-display">

<div class="math-display">
$$
1cm
$$
</div>

</div>

<details markdown="1"><summary>Solution</summary>

The gradient of

<div class="math-display">
$$
f(\vec x) = cx_1^2 + dx_2^2
$$
</div>

 is

<div class="math-display">
$$
\nabla f(\vec x)
=
\begin{bmatrix}
2cx_1 \\\\
2dx_2
\end{bmatrix}
$$
</div>

 At <span class="math-inline">\\(\vec x^{(1)} = \begin{bmatrix} 4 \\\\ 1 \end{bmatrix}\\)</span>, we're told that

<div class="math-display">
$$
\nabla f(\vec x^{(1)})
=
\begin{bmatrix} 6 \\\\ -2 \end{bmatrix}
$$
</div>

 Using the second component (because we're only asked for <span class="math-inline">\\(d\\)</span>),

<div class="math-display">
$$
\begin{align*}
2d(1) &= -2 \\\\
d &= -1
\end{align*}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">5 pts</span> Your friend claims that gradient descent always converges to a minimum because each iteration moves in the direction of steepest decrease. Based on the information in this problem, is your friend correct? State "yes" or "no", and briefly explain your reasoning.

<details markdown="1"><summary>Solution</summary>

No. From part **b)**, <span class="math-inline">\\(d=-1\\)</span>, so

<div class="math-display">
$$
f(\vec x) = cx_1^2 - x_2^2
$$
</div>

 This function does not have a minimum, because we can make <span class="math-inline">\\(f(\vec x)\\)</span> arbitrarily negative by making <span class="math-inline">\\(|x&#95;2|\\)</span> arbitrarily large. So, in this problem, gradient descent cannot converge to a minimum.
</details>

This page has been intentionally left blank. Feel free to use it for scratch work.

Congrats on finishing Midterm 2!

Feel free to draw us a picture about EECS 245 in the box below.
</div>
</div>

</div>

{% endraw %}
