---
layout: minimal
title: "Chapter 5: Matrices"
description: "Practice problems for Chapter 5: Matrices."
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

# Chapter 5: Matrices

*Topics: matrix operations, special matrices, rank and column space, null space and rank-nullity*

*Problems below are collected from past exams; each links back to its full exam. Solutions are in the dropdowns.*

## Problems

- [FA25 MT2 · Problem 1](#fa25-mt2--problem-1-getting-started-12-pts)
- [FA25 MT2 · Problem 2](#fa25-mt2--problem-2-space-jam-20-pts)
- [FA25 MT2 · Problem 3](#fa25-mt2--problem-3-nilpotence-12-pts)
- [FA25 Final · Problem 5](#fa25-final--problem-5-12-pts-mt2-redemption)
- [WN26 MT2 · Problem 2](#wn26-mt2--problem-2-10-pts)
- [WN26 MT2 · Problem 3](#wn26-mt2--problem-3-11-pts)
- [WN26 MT2 · Problem 5](#wn26-mt2--problem-5-13-pts)
- [WN26 Final · Problem 5](#wn26-final--problem-5-11-pts-mt2-redemption)
- [SP26 MT2 · Problem 1](#sp26-mt2--problem-1-12-pts)
- [SP26 MT2 · Problem 2](#sp26-mt2--problem-2-16-pts)
- [SP26 MT2 · Problem 3](#sp26-mt2--problem-3-12-pts)
- [SP26 Final · Problem 5](#sp26-final--problem-5-4-pts-mt2-redemption)

---

## FA25 MT2 · Problem 1: Getting Started <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>

<p class="worksheet-source">From <a href="/exams/fa25-mt2/">FA25 MT2</a></p>


<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> Let <span class="math-inline">\\(A = \begin{bmatrix} 2 &amp; 4 \\\\ -3 &amp; -7 \end{bmatrix}\\)</span>. Find <span class="math-inline">\\(\text{det}(A)\\)</span>, the determinant of <span class="math-inline">\\(A\\)</span>. Give your answer as an integer.

<span class="math-inline">\\(\text{det}(A) = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>

<details markdown="1"><summary>Solution</summary>

The determinant of a <span class="math-inline">\\(2 \times 2\\)</span> matrix <span class="math-inline">\\(\begin{bmatrix} a &amp; b \\\\ c &amp; d \end{bmatrix}\\)</span> is <span class="math-inline">\\(ad - bc\\)</span>. So,

<div class="math-display">
$$
\text{det}(A) = (2)(-7) - (4)(-3) = -14 + 12 = \boxed{-2}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> Using <span class="math-inline">\\(A\\)</span> from part **a)**, find <span class="math-inline">\\(A^{-1}\\)</span>, the inverse of <span class="math-inline">\\(A\\)</span>. Fully simplify your answer, i.e. don't leave any constants out front.

<span class="math-inline">\\(A^{-1} = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>

<details markdown="1"><summary>Solution</summary>

The inverse of a <span class="math-inline">\\(2 \times 2\\)</span> matrix <span class="math-inline">\\(\begin{bmatrix} a &amp; b \\\\ c &amp; d \end{bmatrix}\\)</span> is <span class="math-inline">\\(\frac{1}{ad - bc} \begin{bmatrix} d &amp; -b \\\\ -c &amp; a \end{bmatrix}\\)</span>. So,

<div class="math-display">
$$
A^{-1} = \frac{1}{(-2)} \begin{bmatrix} -7 & -4 \\\\ 3 & 2 \end{bmatrix} = \boxed{\begin{bmatrix} 7/2 & 2 \\\\ -3/2 & -1 \end{bmatrix}}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">2 pts</span> Let <span class="math-inline">\\(B = \begin{bmatrix} -1 &amp; 2 &amp; -1 \\\\ 3 &amp; 3 &amp; 2 \\\\ 0 &amp; 0 &amp; 1 \end{bmatrix}\\)</span>. What is the **first column** of <span class="math-inline">\\(B^{-1}\\)</span>, the inverse of <span class="math-inline">\\(B\\)</span>?

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} -1 \\\\ 0 \\\\ 0 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} -1 \\\\ 1/2 \\\\ -1 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} -1 \\\\1/3 \\\\ 1 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} -1/3 \\\\ 1/3 \\\\ 0 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} 1/3 \\\\ -1/3 \\\\ 0 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(B\\)</span> is not invertible</span></div>

<details markdown="1"><summary>Solution</summary>

<span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(B\\)</span> is not invertible

<span class="math-inline">\\(\boxed{\begin{bmatrix} -1/3 \\\\ 1/3 \\\\ 0\end{bmatrix}}\\)</span>.

Remember, <span class="math-inline">\\(B^{-1}\\)</span> is the matrix that satisfies <span class="math-inline">\\(B B^{-1} = I\\)</span>. Inverting <span class="math-inline">\\(B\\)</span> is not necessary: instead, all one needs to look for is the vector <span class="math-inline">\\(\vec v\\)</span> such that <span class="math-inline">\\(B \vec v = \begin{bmatrix} 1 \\\\ 0 \\\\ 0 \end{bmatrix}\\)</span>, since <span class="math-inline">\\(B\\)</span> multiplied by <span class="math-inline">\\(B^{-1}\\)</span>'s first column should give the first column of <span class="math-inline">\\(I\\)</span>.

And indeed, <span class="math-inline">\\(B \begin{bmatrix} -1/3 \\\\ 1/3 \\\\ 0 \end{bmatrix} = \begin{bmatrix} 1 \\\\ 0 \\\\ 0 \end{bmatrix}\\)</span>. So, you could have solved this just by guessing and checking each of the options.

If we asked this as an open-ended question instead, we'd be searching for the vector <span class="math-inline">\\(\begin{bmatrix} x \\\\ y \\\\ z \end{bmatrix}\\)</span> such that

<div class="math-display">
$$
\begin{bmatrix} -1 & 2 & -1 \\\\ 3 & 3 & 2 \\\\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} x \\\\ y \\\\ z \end{bmatrix} = \begin{bmatrix} 1 \\\\ 0 \\\\ 0 \end{bmatrix}
$$
</div>

From here, there are two ways to solve for <span class="math-inline">\\(\begin{bmatrix} x \\\\ y \\\\ z \end{bmatrix}\\)</span>.

-   You could solve the system of equations directly.

-   Or, you could notice that <span class="math-inline">\\(\begin{bmatrix} x \\\\ y \\\\ z \end{bmatrix}\\)</span> must be orthogonal to both the second row and third row of <span class="math-inline">\\(B\\)</span>, which means that its in the same direction as the cross product of the second and third rows. If you compute the cross product of the last two rows, you get

<div class="math-display">
$$
\begin{bmatrix} 3(1) - 2(0) \\\\ 2(0) - 3(1) \\\\ 3(0) - 3(0) \end{bmatrix} = \begin{bmatrix} 3 \\\\ -3 \\\\ 0 \end{bmatrix}
$$
</div>

 which means that <span class="math-inline">\\(\begin{bmatrix} x \\\\ y \\\\ z \end{bmatrix} = c \begin{bmatrix} 3 \\\\ -3 \\\\ 0 \end{bmatrix}\\)</span> for some constant <span class="math-inline">\\(c\\)</span>. To find <span class="math-inline">\\(c\\)</span>, solve for the <span class="math-inline">\\(c\\)</span> such that the dot product of <span class="math-inline">\\(c \begin{bmatrix} 3 \\\\ -3 \\\\ 0 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\begin{bmatrix} -1 \\\\ 2 \\\\ -1 \end{bmatrix}\\)</span> (the first row of <span class="math-inline">\\(B\\)</span>) is 1. This gives <span class="math-inline">\\(c = -1/9\\)</span>, which means that <span class="math-inline">\\(\begin{bmatrix} x \\\\ y \\\\ z \end{bmatrix} = -1/9 \begin{bmatrix} 3 \\\\ -3 \\\\ 0 \end{bmatrix} = \begin{bmatrix} -1/3 \\\\ 1/3 \\\\ 0 \end{bmatrix}\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> This part is independent of the previous parts (i.e. don't use the specific <span class="math-inline">\\(A\\)</span> or <span class="math-inline">\\(B\\)</span> from above).

**Select all** true statements below.

<span class="mc-square" aria-hidden="true"></span> If <span class="math-inline">\\(A\\)</span> and <span class="math-inline">\\(B\\)</span> are both matrices such that <span class="math-inline">\\(AB = I\\)</span>, then <span class="math-inline">\\(A\\)</span> and <span class="math-inline">\\(B\\)</span> are both invertible.

<span class="mc-square" aria-hidden="true"></span> If <span class="math-inline">\\(A\\)</span> and <span class="math-inline">\\(B\\)</span> are both invertible matrices, then <span class="math-inline">\\((A^TB)^{-1} = \left( (B^{-1})^T A^{-1} \right)^T\\)</span>.

<span class="mc-square" aria-hidden="true"></span> If <span class="math-inline">\\(A\\)</span> is an invertible matrix, then <span class="math-inline">\\(\text{rank}(A) = \text{rank}(A^{-1})\\)</span>.

<span class="mc-square" aria-hidden="true"></span> If <span class="math-inline">\\(A\\)</span>, <span class="math-inline">\\(B\\)</span>, and <span class="math-inline">\\(C\\)</span> are all symmetric matrices, then <span class="math-inline">\\(AB + C\\)</span> is also symmetric.

<details markdown="1"><summary>Solution</summary>

<span class="mc-square" aria-hidden="true"></span> If <span class="math-inline">\\(A\\)</span>, <span class="math-inline">\\(B\\)</span>, and <span class="math-inline">\\(C\\)</span> are all symmetric matrices, then <span class="math-inline">\\(AB + C\\)</span> is also symmetric.

Only Option 3 is true. Let's look at each statement one by one.

**(i)** **If <span class="math-inline">\\(A\\)</span> and <span class="math-inline">\\(B\\)</span> are both matrices such that <span class="math-inline">\\(AB = I\\)</span>, then <span class="math-inline">\\(A\\)</span> and <span class="math-inline">\\(B\\)</span> are both invertible.** This is <span class="math-inline">\\(\boxed{\text{False}}\\)</span>, because it's possible for <span class="math-inline">\\(AB = I\\)</span> to be true for two non-square matrices <span class="math-inline">\\(A\\)</span> and <span class="math-inline">\\(B\\)</span>, meaning they can't be invertible. For example, suppose <span class="math-inline">\\(B = \begin{bmatrix} 1 &amp; 0 \\\\ 0 &amp; 1 \\\\ 0 &amp; 0\end{bmatrix}\\)</span> and <span class="math-inline">\\(A = B^T = \begin{bmatrix} 1 &amp; 0 &amp; 0 \\\\ 0 &amp; 1 &amp; 0 \end{bmatrix}\\)</span>. Then,

<div class="math-display">
$$
AB = B^TB = \begin{bmatrix} 1 & 0 & 0 \\\\ 0 & 1 & 0 \end{bmatrix} \begin{bmatrix} 1 & 0 \\\\ 0 & 1 \\\\ 0 & 0 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\\\ 0 & 1  \end{bmatrix} = I
$$
</div>

**(ii)** **If <span class="math-inline">\\(A\\)</span> and <span class="math-inline">\\(B\\)</span> are both invertible matrices, then <span class="math-inline">\\((A^TB)^{-1} = \left( (B^{-1})^T A^{-1} \right)^T\\)</span>.** This is <span class="math-inline">\\(\boxed{\text{False}}\\)</span>:

-   If we expand the right-hand side, we get

<div class="math-display">
$$
((B^{-1})^T A^{-1})^T = \underbrace{(A^{-1})^T ((B^{-1})^T)^T}_{\text{reverse order of product when taking transpose}} = (A^{-1})^T (B^{-1})
$$
</div>

-   This is not the same as <span class="math-inline">\\((A^TB)^{-1}\\)</span>, which is <span class="math-inline">\\((A^TB)^{-1} = B^{-1}(A^T)^{-1}\\)</span>. Note that <span class="math-inline">\\((A^{-1})^T = (A^T)^{-1}\\)</span>, but the reason these two expressions aren't the same is because order matters for matrix multiplication --- it's not commutative.

**(iii)** **If <span class="math-inline">\\(A\\)</span> is an invertible matrix, then <span class="math-inline">\\(\text{rank}(A) = \text{rank}(A^{-1})\\)</span>.** This is <span class="math-inline">\\(\boxed{\text{True}}\\)</span>. If <span class="math-inline">\\(A\\)</span> is invertible, then <span class="math-inline">\\(\text{rank}(A) = n\\)</span>. Then, <span class="math-inline">\\(A^{-1}\\)</span> is also invertible (its inverse is <span class="math-inline">\\(A\\)</span>), so it must have a rank of <span class="math-inline">\\(n\\)</span> as well.

**(iv)** **If <span class="math-inline">\\(A\\)</span>, <span class="math-inline">\\(B\\)</span>, and <span class="math-inline">\\(C\\)</span> are all symmetric matrices, then <span class="math-inline">\\(AB + C\\)</span> is also symmetric.** This is <span class="math-inline">\\(\boxed{\text{False}}\\)</span>. Recall, what makes a matrix <span class="math-inline">\\(A\\)</span> symmetric is that <span class="math-inline">\\(A = A^T\\)</span>. Let's take the transpose of <span class="math-inline">\\(AB + C\\)</span> and see if we end up getting back <span class="math-inline">\\(AB + C\\)</span>:

<div class="math-display">
$$
(AB + C)^T = (AB)^T + C^T = B^TA^T + C^T = BA + C
$$
</div>

<span class="math-inline">\\(AB + C\\)</span> is only symmetric if <span class="math-inline">\\(AB + C = BA + C\\)</span>, i.e. if <span class="math-inline">\\(AB = BA\\)</span>, which is not true in general, even if <span class="math-inline">\\(A\\)</span> and <span class="math-inline">\\(B\\)</span> are both symmetric.
</details>

</div>
</div>

</div>


---

## FA25 MT2 · Problem 2: Space Jam <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">20 pts</span>

<p class="worksheet-source">From <a href="/exams/fa25-mt2/">FA25 MT2</a></p>


Let <span class="math-inline">\\(X = \begin{bmatrix} 1 &amp; -4 &amp; 2 &amp; 2 &amp; 0 \\\\ 0 &amp; 0 &amp; -3 &amp; 3 &amp; 0 \\\\ 1 &amp; -4 &amp; 4 &amp; 0 &amp; 0 \\\\ 0 &amp; 0 &amp; 0 &amp; 0 &amp; 1 \end{bmatrix}\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(4.5 pts) Determine the values of each of the following. Give your answers as integers.

<div class="math-display">
$$
\begin{array}{lllll}
\text{dim}(\text{colsp}(X)) = &\_\_\_\_\_\_ \qquad \qquad  & \text{dim}(\text{nullsp}(X)) = &\_\_\_\_\_\_ \\\\ \\\\
\text{dim}(\text{colsp}(X^T)) = &\_\_\_\_\_\_ \qquad \qquad  & \text{dim}(\text{nullsp}(X^T)) = &\_\_\_\_\_\_ \\\\
\end{array}
$$
</div>

<details markdown="1"><summary>Solution</summary>

Recall, the rank-nullity theorem states that for any matrix <span class="math-inline">\\(X\\)</span>,

<div class="math-display">
$$
\text{rank}(X) + \text{dim}(\text{nullsp}(X)) = \text{number of columns of } X
$$
</div>

where <span class="math-inline">\\(\text{rank}(X) = \text{dim}(\text{colsp}(X)) = \text{dim}(\text{colsp}(X^T))\\)</span>.

<span class="math-inline">\\(X\\)</span> has **3** linearly independent columns: columns 1, 4, and 5. These three columns can be used to create the other two columns:

-   Column 2 = <span class="math-inline">\\(\begin{bmatrix} -4 \\\\ 0 \\\\ -4 \\\\ 0 \end{bmatrix} = -4 \begin{bmatrix} 1 \\\\ 0 \\\\ 1 \\\\ 0 \end{bmatrix} = (-4) \cdot \text{column 1}\\)</span>

-   Column 3 = <span class="math-inline">\\(\begin{bmatrix} 2 \\\\ -3 \\\\ 4 \\\\ 0 \end{bmatrix} = 4 \begin{bmatrix} 1 \\\\ 0 \\\\ 1 \\\\ 0 \end{bmatrix} - \begin{bmatrix} 2 \\\\ 3\\\\ 0 \\\\ 0 \end{bmatrix} = 4 \cdot \text{column 1} - \text{column 4}\\)</span>

So, <span class="math-inline">\\(\text{rank}(X) = 3\\)</span>, meaning <span class="math-inline">\\(\text{dim}(\text{colsp}(X)) = \boxed{3}\\)</span> and <span class="math-inline">\\(\text{dim}(\text{colsp}(X^T)) = \boxed{3}\\)</span> also.

Since <span class="math-inline">\\(\text{rank}(X) + \text{dim}(\text{nullsp}(X)) = \text{number of columns of } X\\)</span>, we have <span class="math-inline">\\(\text{dim}(\text{nullsp}(X)) = 5 - 3 = \boxed{2}\\)</span>.

And finally, since <span class="math-inline">\\(\text{rank}(X^T) + \text{dim}(\text{nullsp}(X^T)) = \text{number of columns of } X^T\\)</span>, we have <span class="math-inline">\\(\text{dim}(\text{nullsp}(X^T)) = 5 - 4 = \boxed{1}\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(3.5 pts) Suppose <span class="math-inline">\\(\vec y \in \mathbb{R}^4\\)</span>. How many solutions <span class="math-inline">\\(\vec v \in \mathbb{R}^5\\)</span> are there to the system of equations <span class="math-inline">\\(X \vec v = \vec y\\)</span>? **Select all** possibilities, since the answer may depend on <span class="math-inline">\\(\vec y\\)</span>.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 0</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 1</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 2</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 3</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 4</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 5</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> Infinitely many</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-square mc-correct" aria-hidden="true"></span> 0</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 1</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 2</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 3</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 4</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 5</span><span class="mc-option"><span class="mc-square mc-correct" aria-hidden="true"></span> Infinitely many</span></div>

When solving <span class="math-inline">\\(X \vec v = \vec y\\)</span> for <span class="math-inline">\\(\vec v\\)</span>, there are two possible cases.

-   <span class="math-inline">\\(\vec y \notin \text{colsp}(X)\\)</span>: This is possible because <span class="math-inline">\\(\text{dim}(\text{colsp}(X))=3\\)</span>, so the columns don't span all of <span class="math-inline">\\(\mathbb{R}^4\\)</span>. In this case, <span class="math-inline">\\(\vec v\\)</span> has no solutions.

-   <span class="math-inline">\\(\vec y \in \text{colsp}(X)\\)</span>: The columns of <span class="math-inline">\\(X\\)</span> aren't linearly independent, so there are infinitely many ways to write <span class="math-inline">\\(\vec y\\)</span> as a linear combination of the columns of <span class="math-inline">\\(X\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> For some <span class="math-inline">\\(\vec y \in \mathbb{R}^4\\)</span>, the vector <span class="math-inline">\\(\vec w' = \begin{bmatrix} 8 \\\\ 0 \\\\ 0 \\\\ 3 \\\\ 11 \end{bmatrix}\\)</span> is such that <span class="math-inline">\\(X \vec w'\\)</span> is the vector in <span class="math-inline">\\(\text{colsp}(X)\\)</span> that is closest to <span class="math-inline">\\(\vec y\\)</span>. State **one other** vector <span class="math-inline">\\(\vec \beta\\)</span> such that <span class="math-inline">\\(X \vec \beta = X \vec w'\\)</span>. Show your work, and <span class="math-inline">\\(\boxed{\text{circle}}\\)</span> your final answer, which should be a vector with five entries and no variables.

<details markdown="1"><summary>Solution</summary>

There's two ways to approach this problem. The first is adding a vector in <span class="math-inline">\\(\text{nullsp}(X)\\)</span> to <span class="math-inline">\\(\vec w'\\)</span>. Why does this work? Let <span class="math-inline">\\(\vec \beta = \vec w' + \vec n\\)</span>, where <span class="math-inline">\\(X\vec n = \vec 0\\)</span>:

<div class="math-display">
$$
\begin{align*}
X\vec \beta &= X(\vec w' + \vec n)
\\\\&=X(\vec w' + \vec n)
\\\\&=X\vec w' + X\vec n
\\\\&=X\vec w' = \vec y
\end{align*}
$$
</div>

So, all we have to do is find a vector in the null space of

<div class="math-display">
$$
X = \begin{bmatrix} 1 & -4 & 2 & 2 & 0 \\\\ 0 & 0 & -3 & 3 & 0 \\\\ 1 & -4 & 4 & 0 & 0 \\\\ 0 & 0 & 0 & 0 & 1 \end{bmatrix}
$$
</div>

One such vector is <span class="math-inline">\\(\vec n = \begin{bmatrix} 0 \\\\ 1 \\\\ 1 \\\\ 1 \\\\ 0 \end{bmatrix}\\)</span>, since <span class="math-inline">\\(X\vec n = \begin{bmatrix} -4 \\\\ 0 \\\\ -4 \\\\ 0 \end{bmatrix} + \begin{bmatrix} 2 \\\\ -3 \\\\ 4 \\\\ 0 \end{bmatrix} + \begin{bmatrix} 2 \\\\ 3 \\\\ 0 \\\\ 0 \end{bmatrix} = \vec 0\\)</span>

This leaves us with <span class="math-inline">\\(\vec \beta=\vec w' + \vec n = \begin{bmatrix} 8 \\\\ 0 \\\\ 0 \\\\ 3 \\\\ 11 \end{bmatrix} + \begin{bmatrix} 0 \\\\ 1 \\\\ 1 \\\\ 1 \\\\ 0 \end{bmatrix} = \boxed{\begin{bmatrix} 8 \\\\ 1 \\\\ 1 \\\\ 4 \\\\ 11 \end{bmatrix}}\\)</span>.

The other way is to "tweak" <span class="math-inline">\\(\vec w'\\)</span> using the relationships we know about in the columns of <span class="math-inline">\\(X\\)</span>. Since <span class="math-inline">\\(\text{column 2} = -4 \cdot \text{column 1}\\)</span>, and <span class="math-inline">\\(\vec w' = \begin{bmatrix} 8 \\\\ 0 \\\\ 0 \\\\ 3 \\\\ 11 \end{bmatrix}\\)</span>, an easy swap is to change <span class="math-inline">\\(w&#95;0\\)</span> from <span class="math-inline">\\(8\\)</span> to <span class="math-inline">\\(0\\)</span> and <span class="math-inline">\\(w&#95;1\\)</span> from 0 to <span class="math-inline">\\(-2\\)</span>:

<div class="math-display">
$$
8 \cdot \begin{bmatrix} 1 \\\\ 0 \\\\ 1 \\\\ 0 \end{bmatrix} = -2 \cdot \begin{bmatrix} -4 \\\\ 0 \\\\ -4 \\\\ 0 \end{bmatrix}
$$
</div>

Doing this gives <span class="math-inline">\\(\vec \beta = \boxed{\begin{bmatrix} 0 \\\\ -2 \\\\ 0 \\\\ 3 \\\\ 11 \end{bmatrix}}\\)</span>.
</details>

Recall, <span class="math-inline">\\(X = \begin{bmatrix} 1 &amp; -4 &amp; 2 &amp; 2 &amp; 0 \\\\ 0 &amp; 0 &amp; -3 &amp; 3 &amp; 0 \\\\ 1 &amp; -4 &amp; 4 &amp; 0 &amp; 0 \\\\ 0 &amp; 0 &amp; 0 &amp; 0 &amp; 1 \end{bmatrix}\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Find a basis for <span class="math-inline">\\(\text{nullsp}(X^T)\\)</span> (**not** <span class="math-inline">\\(\text{nullsp}(X)\\)</span>). Show your work, and <span class="math-inline">\\(\boxed{\text{circle}}\\)</span> your final answer, which should be a list of vectors.

<details markdown="1"><summary>Solution</summary>

<div class="math-display">
$$
X^T=
\begin{bmatrix}
1 & 0 & 1 & 0 \\\\
-4 & 0 & -4 & 0 \\\\
2 & -3 & 4 & 0 \\\\
2 & 3 & 0 & 0 \\\\
0 & 0 & 0 & 1
\end{bmatrix}
$$
</div>

 From the rank-nullity theorem, we know that our basis will have exactly one vector, so our goal is to find a non-zero vector where <span class="math-inline">\\(X^T \vec n = \vec 0\\)</span>.

<span class="math-inline">\\(\text{Column 3}=\text{Column 1} - \frac{2}{3}\cdot \text{Column 2}\\)</span>, so one possible basis is <span class="math-inline">\\(\left\lbrace \begin{bmatrix} 1 \\\\ -\frac{2}{3} \\\\ -1 \\\\ 0\end{bmatrix}\right\rbrace\\)</span>.
</details>

</div>
</div>

</div>


---

## FA25 MT2 · Problem 3: Nilpotence <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>

<p class="worksheet-source">From <a href="/exams/fa25-mt2/">FA25 MT2</a></p>


Suppose <span class="math-inline">\\(A\\)</span> is an <span class="math-inline">\\(n \times n\\)</span> matrix such that <span class="math-inline">\\(A^2 = 0&#95;{n \times n}\\)</span>, where <span class="math-inline">\\(0&#95;{n \times n}\\)</span> is an <span class="math-inline">\\(n \times n\\)</span> matrix of all zeros.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Prove that if <span class="math-inline">\\(\vec x \in \text{colsp}(A)\\)</span>, then <span class="math-inline">\\(\vec x \in \text{nullsp}(A)\\)</span>.

<details markdown="1"><summary>Solution</summary>

If <span class="math-inline">\\(\vec x \in \text{colsp}(A)\\)</span>, then <span class="math-inline">\\(\vec x = A \vec v\\)</span> for some <span class="math-inline">\\(\vec v \in \mathbb{R}^n\\)</span>. Then, multiplying both sides of <span class="math-inline">\\(\vec x = A \vec v\\)</span> by <span class="math-inline">\\(A\\)</span> on the left gives us:

<div class="math-display">
$$
A \vec x = A (A \vec v) = A^2 \vec v = 0_{n \times n} \vec v = \vec 0
$$
</div>

Since <span class="math-inline">\\(\vec x = A \vec v \implies A \vec x = \vec 0\\)</span>, we have <span class="math-inline">\\(\vec x \in \text{nullsp}(A)\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> In part **a)**, you showed that <span class="math-inline">\\(\text{colsp}(A)\\)</span> is a subset of <span class="math-inline">\\(\text{nullsp}(A)\\)</span>. Using this fact, find the **maximum** possible value of <span class="math-inline">\\(\text{rank}(A)\\)</span>. Show your work and <span class="math-inline">\\(\boxed{\text{circle}}\\)</span> your final answer, which should be an expression involving <span class="math-inline">\\(n\\)</span> and/or constants.

<details markdown="1"><summary>Solution</summary>

In the previous part, we showed that every element in <span class="math-inline">\\(\text{colsp}(A)\\)</span> is also in <span class="math-inline">\\(\text{nullsp}(A)\\)</span>. (The converse is not true.) Intuitively, this means that the column space is a subset of the null space, so it's "smaller" than the null space.

This means that

<div class="math-display">
$$
\text{dim}(\text{colsp}(A)) \leq \text{dim}(\text{nullsp}(A))
$$
</div>

 or in other words

<div class="math-display">
$$
\text{rank}(A) \leq \text{dim}(\text{nullsp}(A))
$$
</div>

Let's add <span class="math-inline">\\(\text{rank}(A)\\)</span> to both sides of the inequality; this will make the right-hand side look like something involved in the rank-nullity theorem.

<div class="math-display">
$$
\text{rank}(A) + \text{rank}(A) \leq \text{rank}(A) + \text{dim}(\text{nullsp}(A)) = n
$$
</div>

This tells us that <span class="math-inline">\\(2\text{rank}(A) \leq n\\)</span>, so <span class="math-inline">\\(\boxed{\text{rank}(A) \leq \frac{n}{2}}\\)</span> and so <span class="math-inline">\\(\frac{n}{2}\\)</span> is the maximum possible value of <span class="math-inline">\\(\text{rank}(A)\\)</span>.
</details>

</div>
</div>

</div>


---

## FA25 Final · Problem 5 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span> <span class="badge" data-flag="mt2-redemption" style="background-color: #9A3324; color: #FFFFFF; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">MT2 Redemption</span>

<p class="worksheet-source">From <a href="/exams/fa25-final/">FA25 Final</a></p>


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

<span class="math-inline">\\(\text{rank}(A) = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>

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

<span class="math-inline">\\(a = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;, \qquad b = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>

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

<span class="math-inline">\\(\text{One vector in } \text{nullsp}(A) \text{ is:   } \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>

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

| <span class="math-inline">\\(i\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(2\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(3\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(4\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(5\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(n-2\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(n-1\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(n\\)</span> |
|:-------|:--------------------------|:--------------------------|:--------------------------|:--------------------------|:------------------------------|:------------------------------|:--------------------------|
| <span class="math-inline">\\(ii\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\mathbb{R}^2\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\mathbb{R}^3\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\mathbb{R}^4\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\mathbb{R}^5\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\mathbb{R}^{n-2}\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\mathbb{R}^{n-1}\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\mathbb{R}^n\\)</span> |

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\mathbb{R}^2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\mathbb{R}^3\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\mathbb{R}^4\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\mathbb{R}^5\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\mathbb{R}^{n-2}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\mathbb{R}^{n-1}\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(\mathbb{R}^n\\)</span></span></div>

Since <span class="math-inline">\\(\text{rank}(A)=2\\)</span> and <span class="math-inline">\\(\text{rank}(A) = \text{rank}(A^T)\\)</span>, we also have <span class="math-inline">\\(\text{rank}(A^T)=2\\)</span>. The matrix <span class="math-inline">\\(A^T\\)</span> has <span class="math-inline">\\(n\\)</span> columns, so rank-nullity gives

<div class="math-display">
$$
\dim(\text{nullsp}(A^T)) = \text{\# columns in }A^T - \text{rank}(A^T) = n - 2
$$
</div>

 Also, <span class="math-inline">\\(\text{nullsp}(A^T)\\)</span> is a subspace of <span class="math-inline">\\(\mathbb{R}^n\\)</span>, because vectors in <span class="math-inline">\\(\text{nullsp}(A^T)\\)</span> must have one entry for each column of <span class="math-inline">\\(A^T\\)</span> (row of <span class="math-inline">\\(A\\)</span>).
</details>

</div>
</div>

</div>


---

## WN26 MT2 · Problem 2 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">10 pts</span>

<p class="worksheet-source">From <a href="/exams/wn26-mt2/">WN26 MT2</a></p>


Suppose <span class="math-inline">\\(A\\)</span> is a matrix such that <span class="math-inline">\\(A \begin{bmatrix} 1 \\\\ 0 \\\\ 0 \\\\ 0 \end{bmatrix} = \begin{bmatrix} 6 \\\\ 0 \\\\ 1 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\left\lbrace \begin{bmatrix} 1 \\\\ 4 \\\\ -2 \\\\ 0 \end{bmatrix}, \begin{bmatrix} 0 \\\\ 1 \\\\ 1 \\\\ 0\end{bmatrix} \right\rbrace\\)</span> is a basis for <span class="math-inline">\\(\text{nullsp}(A)\\)</span>.

Find one possible matrix <span class="math-inline">\\(A\\)</span>. Show your work, and <span class="math-inline">\\(\boxed{\text{circle}}\\)</span> your final answer, which should be a matrix with no variables.

<details markdown="1"><summary>Solution</summary>

Let the columns of <span class="math-inline">\\(A\\)</span> be <span class="math-inline">\\(\vec c&#95;1, \vec c&#95;2, \vec c&#95;3, \vec c&#95;4\\)</span>. Since

<div class="math-display">
$$
A \begin{bmatrix} 1 \\\\ 0 \\\\ 0 \\\\ 0 \end{bmatrix} = 1\vec c_1 + 0\vec c_2 + 0\vec c_3 + 0\vec c_4 = \begin{bmatrix} 6 \\\\ 0 \\\\ 1 \end{bmatrix},
$$
</div>

 we know that the first column of <span class="math-inline">\\(A\\)</span> must be <span class="math-inline">\\(\begin{bmatrix} 6 \\\\ 0 \\\\ 1 \end{bmatrix}\\)</span>.

Now, let's use the information given about the null space to find the other columns of <span class="math-inline">\\(A\\)</span>. Since

<div class="math-display">
$$
\begin{bmatrix} 0 \\\\ 1 \\\\ 1 \\\\ 0 \end{bmatrix} \in \text{nullsp}(A),
$$
</div>

 we have

<div class="math-display">
$$
\vec c_2 + \vec c_3 = \vec 0 \implies \vec c_3 = -\vec c_2
$$
</div>

Also, since

<div class="math-display">
$$
\begin{bmatrix} 1 \\\\ 4 \\\\ -2 \\\\ 0 \end{bmatrix} \in \text{nullsp}(A),
$$
</div>

 we have

<div class="math-display">
$$
\vec c_1 + 4\vec c_2 - 2\vec c_3 = \vec 0
$$
</div>

 Substituting <span class="math-inline">\\(\vec c&#95;3 = -\vec c&#95;2\\)</span> gives

<div class="math-display">
$$
\begin{align*}
\vec c_1 + 6\vec c_2 &= \vec 0 \\\\
\vec c_2 &= -\frac{1}{6}\vec c_1 = \begin{bmatrix} -1 \\\\ 0 \\\\ -1/6 \end{bmatrix}.
\end{align*}
$$
</div>

So,

<div class="math-display">
$$
\vec c_3 = -\vec c_2 = \begin{bmatrix} 1 \\\\ 0 \\\\ 1/6 \end{bmatrix}
$$
</div>

Finally, <span class="math-inline">\\(\text{dim}(\text{nullsp}(A)) = 2\\)</span> and <span class="math-inline">\\(A\\)</span> has 4 columns, so by rank-nullity,

<div class="math-display">
$$
\begin{align*}
\text{rank}(A) &= 4 - 2 = 2
\end{align*}
$$
</div>

So we should choose <span class="math-inline">\\(\vec c&#95;4\\)</span> to be linearly independent from <span class="math-inline">\\(\vec c&#95;1\\)</span>. One easy choice is

<div class="math-display">
$$
\vec c_4 = \begin{bmatrix} 0 \\\\ 1 \\\\ 0 \end{bmatrix}
$$
</div>

This gives one possible matrix.

<div class="math-display">
$$
\boxed{
A = \begin{bmatrix}
6 & -1 & 1 & 0 \\\\
0 & 0 & 0 & 1 \\\\
1 & -1/6 & 1/6 & 0
\end{bmatrix}
}
$$
</div>

</details>


---

## WN26 MT2 · Problem 3 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">11 pts</span>

<p class="worksheet-source">From <a href="/exams/wn26-mt2/">WN26 MT2</a></p>


Suppose <span class="math-inline">\\(A\\)</span> and <span class="math-inline">\\(B\\)</span> are both **non-zero** <span class="math-inline">\\(6 \times 6\\)</span> matrices, such that <span class="math-inline">\\(\text{rank}(A) = 4\\)</span> and that every column of <span class="math-inline">\\(B\\)</span> is in <span class="math-inline">\\(\text{nullsp}(A)\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> Fill in the blanks: The third \_\_(i)\_\_ of <span class="math-inline">\\(A\\)</span> is \_\_(ii)\_\_ to the fourth \_\_(iii)\_\_ of <span class="math-inline">\\(B\\)</span>.

1.
<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> column</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> row</span></div>

2.
<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> orthogonal</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> parallel</span></div>

3.
<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> column</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> row</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> column</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> row</span></div>

Every column of <span class="math-inline">\\(B\\)</span> is in <span class="math-inline">\\(\text{nullsp}(A)\\)</span>. From [Chapter 5.4 in the notes](https://notes.eecs245.org/matrices/null-space-rank-nullity/#example-orthogonal-complements), the row space of <span class="math-inline">\\(A\\)</span> and the null space of <span class="math-inline">\\(A\\)</span> are orthogonal complements. That means every row of <span class="math-inline">\\(A\\)</span> is orthogonal to every vector in <span class="math-inline">\\(\text{nullsp}(A)\\)</span>, and hence orthogonal to every column of <span class="math-inline">\\(B\\)</span>.

So, the third **row** of <span class="math-inline">\\(A\\)</span> is **orthogonal** to the fourth **column** of <span class="math-inline">\\(B\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> **Select all** possible values of <span class="math-inline">\\(\text{rank}(AB)\\)</span>.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 0</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 1</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 2</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 3</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 4</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 5</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 6</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 0</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 1</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 2</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 3</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 4</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 5</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 6</span></div>

Let <span class="math-inline">\\(\vec b&#95;1, \vec b&#95;2, \ldots, \vec b&#95;6\\)</span> be the columns of <span class="math-inline">\\(B\\)</span>. Since every column of <span class="math-inline">\\(B\\)</span> is in <span class="math-inline">\\(\text{nullsp}(A)\\)</span>, we have

<div class="math-display">
$$
A \vec b_j = \vec 0
$$
</div>

 for every <span class="math-inline">\\(j\\)</span>. But the <span class="math-inline">\\(j\\)</span>th column of <span class="math-inline">\\(AB\\)</span> is exactly <span class="math-inline">\\(A \vec b&#95;j\\)</span>, so every column of <span class="math-inline">\\(AB\\)</span> is <span class="math-inline">\\(\vec 0\\)</span>.

Therefore,

<div class="math-display">
$$
AB = 0_{6 \times 6} \implies \text{rank}(AB) = 0_{6 \times 6}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> **Select all** possible values of <span class="math-inline">\\(\text{rank}(B)\\)</span>.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 0</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 1</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 2</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 3</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 4</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 5</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 6</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 0</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 1</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 2</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 3</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 4</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 5</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 6</span></div>

Since <span class="math-inline">\\(A\\)</span> is <span class="math-inline">\\(6 \times 6\\)</span> with rank 4, the rank-nullity theorem gives

<div class="math-display">
$$
\dim(\text{nullsp}(A)) = 6 - 4 = 2
$$
</div>

 Every column of <span class="math-inline">\\(B\\)</span> lies in <span class="math-inline">\\(\text{nullsp}(A)\\)</span>, so

<div class="math-display">
$$
\text{colsp}(B) \subseteq \text{nullsp}(A)
$$
</div>

 Therefore,

<div class="math-display">
$$
\text{rank}(B) = \dim(\text{colsp}(B)) \leq 2
$$
</div>

Also, <span class="math-inline">\\(B\\)</span> is non-zero, so <span class="math-inline">\\(\text{rank}(B) \neq 0\\)</span>.

So the only possible values are **1** and **2**.

Both are achievable: all columns of <span class="math-inline">\\(B\\)</span> could be multiples of one non-zero vector in <span class="math-inline">\\(\text{nullsp}(A)\\)</span>, or they could span all of <span class="math-inline">\\(\text{nullsp}(A)\\)</span> (which is a 2-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^6\\)</span>, since <span class="math-inline">\\(\text{rank}(A)=4\\)</span>).
</details>

</div>
</div>

</div>


---

## WN26 MT2 · Problem 5 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">13 pts</span>

<p class="worksheet-source">From <a href="/exams/wn26-mt2/">WN26 MT2</a></p>


Let

<div class="math-display">
$$
A = \begin{bmatrix} 1 & 0 & 0 & 0 & 0 \\\\ 2 & 1 & 0 & 0 & 4 \\\\ 3 & 1 & 0 & -7 & 4 \end{bmatrix}
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">5 pts</span> Recall, a CR decomposition of an <span class="math-inline">\\(n \times d\\)</span> matrix <span class="math-inline">\\(A\\)</span> is a product <span class="math-inline">\\(A = CR\\)</span>, where <span class="math-inline">\\(C\\)</span> is an <span class="math-inline">\\(n \times r\\)</span> matrix with linearly independent columns and <span class="math-inline">\\(R\\)</span> is an <span class="math-inline">\\(r \times d\\)</span> matrix with linearly independent rows, and <span class="math-inline">\\(r = \text{rank}(A)\\)</span>.

Provide a CR decomposition of <span class="math-inline">\\(A\\)</span>. Your answers should be matrices with no variables.

<span class="math-inline">\\(C = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;, \quad R = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>

<details markdown="1"><summary>Solution</summary>

The columns of <span class="math-inline">\\(A\\)</span> are

<div class="math-display">
$$
\vec c_1 = \begin{bmatrix} 1 \\\\ 2 \\\\ 3 \end{bmatrix}, \quad
\vec c_2 = \begin{bmatrix} 0 \\\\ 1 \\\\ 1 \end{bmatrix}, \quad
\vec c_3 = \begin{bmatrix} 0 \\\\ 0 \\\\ 0 \end{bmatrix}, \quad
\vec c_4 = \begin{bmatrix} 0 \\\\ 0 \\\\ -7 \end{bmatrix}, \quad
\vec c_5 = \begin{bmatrix} 0 \\\\ 4 \\\\ 4 \end{bmatrix}
$$
</div>

Reading left-to-right, columns 1, 2, and 4 are linearly independent, so we place them in <span class="math-inline">\\(C\\)</span>:

<div class="math-display">
$$
C = \begin{bmatrix}
1 & 0 & 0 \\\\
2 & 1 & 0 \\\\
3 & 1 & -7
\end{bmatrix}
$$
</div>

Now we need to express each column of <span class="math-inline">\\(A\\)</span> as a linear combination of the columns of <span class="math-inline">\\(C\\)</span>:

<div class="math-display">
$$
\vec c_1 = 1\vec c_1 + 0\vec c_2 + 0\vec c_4, \quad
\vec c_2 = 0\vec c_1 + 1\vec c_2 + 0\vec c_4, \quad
\vec c_3 = \vec 0,
$$
</div>



<div class="math-display">
$$
\vec c_4 = 0\vec c_1 + 0\vec c_2 + 1\vec c_4, \quad
\vec c_5 = 0\vec c_1 + 4\vec c_2 + 0\vec c_4
$$
</div>

 The coefficients in each linear combination are the entries in the corresponding column of <span class="math-inline">\\(R\\)</span>. So,

<div class="math-display">
$$
R = \begin{bmatrix}
1 & 0 & 0 & 0 & 0 \\\\
0 & 1 & 0 & 0 & 4 \\\\
0 & 0 & 0 & 1 & 0
\end{bmatrix}
$$
</div>

Thus, one CR decomposition is

<div class="math-display">
$$
A =
\begin{bmatrix}
1 & 0 & 0 \\\\
2 & 1 & 0 \\\\
3 & 1 & -7
\end{bmatrix}
\begin{bmatrix}
1 & 0 & 0 & 0 & 0 \\\\
0 & 1 & 0 & 0 & 4 \\\\
0 & 0 & 0 & 1 & 0
\end{bmatrix}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> Find <span class="math-inline">\\(\text{dim}(\text{nullsp}(A^T))\\)</span>. Give your answer as an integer with no variables.

<span class="math-inline">\\(\text{dim}(\text{nullsp}(A^T)) = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>

<details markdown="1"><summary>Solution</summary>

The matrix <span class="math-inline">\\(A\\)</span> has 3 rows and rank 3. Applying rank-nullity to <span class="math-inline">\\(A^T\\)</span>, we get

<div class="math-display">
$$
\begin{align*}
\text{rank}(A^T) + \dim(\text{nullsp}(A^T)) &= \text{number of columns of } A^T = 3
\end{align*}
$$
</div>

Since <span class="math-inline">\\(\text{rank}(A^T)=\text{rank}(A)=3\\)</span>,

<div class="math-display">
$$
\begin{align*}
3 + \dim(\text{nullsp}(A^T)) &= 3 \\\\
\dim(\text{nullsp}(A^T)) &= 0
\end{align*}
$$
</div>

This means that <span class="math-inline">\\(A^T\\)</span>'s null space is <span class="math-inline">\\(\left\lbrace \vec 0 \right\rbrace\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(5 pts) Suppose we apply the Gram-Schmidt process to the **rows** of <span class="math-inline">\\(A\\)</span>, and place the resulting orthonormal vectors into the **rows** of a new matrix, <span class="math-inline">\\(Q\\)</span>.

Let <span class="math-inline">\\(P\\)</span> be the matrix that projects vectors in <span class="math-inline">\\(\mathbb{R}^5\\)</span> onto <span class="math-inline">\\(\text{colsp}(Q^T)\\)</span> (the row space of <span class="math-inline">\\(Q\\)</span>). In other words, if <span class="math-inline">\\(\vec y \in \mathbb{R}^5\\)</span>, then <span class="math-inline">\\(P\vec y\\)</span> is the projection of <span class="math-inline">\\(\vec y\\)</span> onto <span class="math-inline">\\(\text{colsp}(Q^T)\\)</span>.

Find an expression for <span class="math-inline">\\(P\\)</span> in terms of <span class="math-inline">\\(Q\\)</span> and <span class="math-inline">\\(Q^T\\)</span>. Show your work, and <span class="math-inline">\\(\boxed{\text{circle}}\\)</span> your final answer, which should be an expression in terms of <span class="math-inline">\\(Q\\)</span> and <span class="math-inline">\\(Q^T\\)</span>. Answers that aren't fully simplified will not be given credit.

<div class="math-display">
$$
P = \_\_\_\_\_\_
$$
</div>

<details markdown="1"><summary>Solution</summary>

In general, the projection matrix onto <span class="math-inline">\\(\text{colsp}(X)\\)</span>, where <span class="math-inline">\\(X\\)</span> is any matrix with linearly independent columns, is

<div class="math-display">
$$
P = X(X^TX)^{-1}X^T
$$
</div>

Here, we want to project onto <span class="math-inline">\\(\text{colsp}(Q^T)\\)</span>, so we should use <span class="math-inline">\\(X = Q^T\\)</span>:

<div class="math-display">
$$
P = Q^T((Q^T)^TQ^T)^{-1}(Q^T)^T = Q^T(QQ^T)^{-1}Q
$$
</div>

But, since <span class="math-inline">\\(Q\\)</span>'s rows are orthonormal, <span class="math-inline">\\(QQ^T = I\\)</span>. This is because <span class="math-inline">\\(QQ^T\\)</span> is a matrix containing the dot products of the rows of <span class="math-inline">\\(Q\\)</span> with each other (the same way <span class="math-inline">\\(Q^TQ\\)</span> is a matrix containing the dot products of the columns of <span class="math-inline">\\(Q\\)</span> with each other). Since the rows of <span class="math-inline">\\(Q\\)</span> are orthonormal, the dot products are all 0 except for the diagonal, which is 1.

So,

<div class="math-display">
$$
P = Q^T I Q = Q^T Q
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

## SP26 MT2 · Problem 1 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>

<p class="worksheet-source">From <a href="/exams/sp26-mt2/">SP26 MT2</a></p>


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
$$
k = \_\_\_\_\_\_
$$
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
$$
k = \_\_\_\_\_\_
$$
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
$$
k = \_\_\_\_\_\_
$$
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

## SP26 MT2 · Problem 2 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">16 pts</span>

<p class="worksheet-source">From <a href="/exams/sp26-mt2/">SP26 MT2</a></p>


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

<span class="math-inline">\\(\text{rank}(A) =\\)</span> \_\_\_\_\_\_ <span class="math-inline">\\(\text{dim}(\text{nullsp}(A)) =\\)</span> \_\_\_\_\_\_

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

<span class="math-inline">\\(\text{one basis for }\text{nullsp}(A) =\\)</span> \_\_\_\_\_\_

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

<span class="math-inline">\\(\text{one basis for }\text{colsp}(A^T) =\\)</span> \_\_\_\_\_\_

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

## SP26 MT2 · Problem 3 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>

<p class="worksheet-source">From <a href="/exams/sp26-mt2/">SP26 MT2</a></p>


Suppose <span class="math-inline">\\(A\\)</span> is an <span class="math-inline">\\(n \times n\\)</span> matrix.

For each statement below, determine whether it is true or false. If true, prove that it is true. If false, give a counterexample or a short explanation.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> If <span class="math-inline">\\(A\\)</span> is symmetric, then <span class="math-inline">\\(A^2\\)</span> must be symmetric.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

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

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> False</span></div>

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

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

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

## SP26 Final · Problem 5 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> <span class="badge" data-flag="mt2-redemption" style="background-color: #9A3324; color: #FFFFFF; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">MT2 Redemption</span>

<p class="worksheet-source">From <a href="/exams/sp26-final/">SP26 Final</a></p>


Suppose <span class="math-inline">\\(A\\)</span> is a <span class="math-inline">\\(7 \times 12\\)</span> matrix. Fill in each blank with an integer with no variables.

1.  (2 pts) What is the minimum possible value of <span class="math-inline">\\(\text{dim}(\text{nullsp}(A))\\)</span>? \_\_\_\_\_\_

2.  (2 pts) What is the maximum possible value of <span class="math-inline">\\(\text{dim}(\text{nullsp}(A))\\)</span>? \_\_\_\_\_\_

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

## More practice (PDF only)

- [MOCK MT2 Problem 1](/resources/exams/mock-mt2.pdf#page=3)
- [MOCK MT2 Problem 2](/resources/exams/mock-mt2.pdf#page=4)
- [MOCK MT2 Problem 4](/resources/exams/mock-mt2.pdf#page=8)

{% endraw %}
