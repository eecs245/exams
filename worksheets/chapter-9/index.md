---
layout: minimal
title: "Chapter 9: Eigenvalues and Eigenvectors"
description: "Practice problems for Chapter 9: Eigenvalues and Eigenvectors."
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

# Chapter 9: Eigenvalues and Eigenvectors

*Topics: eigenvalues and eigenvectors, characteristic polynomial, markov chains + adjacency matrices, multiplicities + diagonalization*

*Problems below are collected from past exams; each links back to its full exam. Solutions are in the dropdowns.*

## Problems

- [FA25 Final · Problem 9](#fa25-final--problem-9-18-pts)
- [FA25 Final · Problem 10](#fa25-final--problem-10-12-pts)
- [FA25 Final · Problem 11](#fa25-final--problem-11-12-pts)
- [WN26 MT2 · Problem 1](#wn26-mt2--problem-1-12-pts)
- [WN26 Final · Problem 9](#wn26-final--problem-9-12-pts)
- [WN26 Final · Problem 10](#wn26-final--problem-10-14-pts)
- [WN26 Final · Problem 11](#wn26-final--problem-11-10-pts)
- [SP26 Final · Problem 10](#sp26-final--problem-10-12-pts)
- [SP26 Final · Problem 11](#sp26-final--problem-11-10-pts)
- [SP26 Final · Problem 12](#sp26-final--problem-12-11-pts)

---

## FA25 Final · Problem 9 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">18 pts</span>

<p class="worksheet-source">From <a href="/exams/fa25-final/">FA25 Final</a></p>

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

<span class="math-inline">\\(c = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;, \qquad \lambda&#95;1 = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;, \qquad \lambda&#95;2 = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>

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

<span class="math-inline">\\(c = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;, \qquad \lambda&#95;1 = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;, \qquad \lambda&#95;2 = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>

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

<span class="math-inline">\\(c = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;, \qquad \lambda&#95;1 = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;, \qquad \lambda&#95;2 = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>

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

## FA25 Final · Problem 10 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>

<p class="worksheet-source">From <a href="/exams/fa25-final/">FA25 Final</a></p>

Consider the adjacency matrix <span class="math-inline">\\(A = \begin{bmatrix} 0.4 &amp; 0 &amp; 0.5 \\\\ 0.4 &amp; 0 &amp; 0.5 \\\\ a &amp; b &amp; c \end{bmatrix}\\)</span> for a Markov chain with three states, where <span class="math-inline">\\(a, b, c \in \mathbb{R}\\)</span> are some constants.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Find <span class="math-inline">\\(a\\)</span>, <span class="math-inline">\\(b\\)</span>, and <span class="math-inline">\\(c\\)</span> such that <span class="math-inline">\\(A\\)</span> is a valid adjacency matrix. Give your answers as numbers with no variables.

<span class="math-inline">\\(a = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;, \qquad b = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;, \qquad c = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>

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
<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \begin{bmatrix} 1/3 \\\\ 1/3 \\\\ 1/3 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \begin{bmatrix} 4/9 \\\\ 0 \\\\ 5/9 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \begin{bmatrix} 5/16 \\\\ 5/16 \\\\ 6/16 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \begin{bmatrix} 5/16 \\\\ 6/16 \\\\ 5/16 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \begin{bmatrix} 3/16 \\\\ 3/16 \\\\ 10/16 \end{bmatrix}\\)</span></span></div>

2.  because <span class="math-inline">\\(\vec x^{\ast}\\)</span> is the eigenvector of <span class="math-inline">\\(A\\)</span> corresponding to the eigenvalue



<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(-1\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(0\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(0.4\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1.8\\)</span></span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(-1\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(0\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(0.4\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(1\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1.8\\)</span></span></div>

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

## FA25 Final · Problem 11 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>

<p class="worksheet-source">From <a href="/exams/fa25-final/">FA25 Final</a></p>

Let <span class="math-inline">\\(A\\)</span> be a <span class="math-inline">\\(4 \times 4\\)</span> **symmetric** matrix with eigenvalue decomposition <span class="math-inline">\\(A = V \Lambda V^{-1}\\)</span>. Suppose the columns of <span class="math-inline">\\(V\\)</span> are <span class="math-inline">\\(\vec v&#95;1\\)</span>, <span class="math-inline">\\(\vec v&#95;2\\)</span>, <span class="math-inline">\\(\vec v&#95;3\\)</span>, and <span class="math-inline">\\(\vec v&#95;4\\)</span>, in that order, and that the columns of <span class="math-inline">\\(V\\)</span> are unit vectors.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">2 pts</span> Suppose <span class="math-inline">\\(\Lambda = \begin{bmatrix} 4 &amp; 0 &amp; 0 &amp; 0 \\\\ 0 &amp; 3 &amp; 0 &amp; 0 \\\\ 0 &amp; 0 &amp; 2 &amp; 0 \\\\ 0 &amp; 0 &amp; 0 &amp; 1 \end{bmatrix}\\)</span>.

True or False: <span class="math-inline">\\(V\\)</span> is guaranteed to be an orthogonal matrix.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

This is true. Since <span class="math-inline">\\(A\\)</span> is symmetric, the spectral theorem states that eigenvectors corresponding to different eigenvalues are automatically orthogonal. Additionally, <span class="math-inline">\\(A\\)</span> has four unique eigenvalues. This means that the columns of <span class="math-inline">\\(V\\)</span> are guaranteed to be orthogonal. Since we're told that the columns of <span class="math-inline">\\(V\\)</span> are unit vectors, they are orthonormal, so <span class="math-inline">\\(V\\)</span> is orthogonal.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">2 pts</span> Suppose <span class="math-inline">\\(\Lambda = \begin{bmatrix} 4 &amp; 0 &amp; 0 &amp; 0 \\\\ 0 &amp; 2 &amp; 0 &amp; 0 \\\\ 0 &amp; 0 &amp; 2 &amp; 0 \\\\ 0 &amp; 0 &amp; 0 &amp; 1 \end{bmatrix}\\)</span>.

True or False: <span class="math-inline">\\(V\\)</span> is guaranteed to be an orthogonal matrix.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> False</span></div>

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
<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(3\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(4\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(5\\)</span></span></div>

2.  Justify your answer in the box below.

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(2\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(3\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(4\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(5\\)</span></span></div>

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

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\vec v&#95;1\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\vec v&#95;2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\vec v&#95;3\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\vec v&#95;4\\)</span></span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\vec v&#95;1\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\vec v&#95;2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\vec v&#95;3\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(\vec v&#95;4\\)</span></span></div>

From part **c)**, the relevant eigenvalues have magnitudes 2, 3, 0, and 4. As <span class="math-inline">\\(k \to \infty\\)</span>, the component corresponding to the largest eigenvalue magnitude dominates, so the direction of <span class="math-inline">\\(A^k \vec x\\)</span> approaches the direction of <span class="math-inline">\\(\boxed{\vec v&#95;4}\\)</span>.
</details>

</div>
</div>

</div>

---

## WN26 MT2 · Problem 1 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>

<p class="worksheet-source">From <a href="/exams/wn26-mt2/">WN26 MT2</a></p>

Suppose <span class="math-inline">\\(k\\)</span> is a real number. Let

<div class="math-display">
$$
A = \begin{bmatrix} 3 & 2 \\\\ k & 4 \end{bmatrix}
$$
</div>

In each part, you are provided with information about <span class="math-inline">\\(A\\)</span>. **Your job is to find the value of <span class="math-inline">\\(k\\)</span> that satisfies the given condition.** Show your work in the space provided, and write your final answer in the bottom-right corner of the box. Your answers should be numbers with no variables.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span>
<span class="math-inline">\\(\text{rank}(A) = 1\\)</span>

<div class="math-display">
$$
k = \_\_\_\_\_\_
$$
</div>

<details markdown="1"><summary>Solution</summary>

If <span class="math-inline">\\(\text{rank}(A) = 1\\)</span>, then <span class="math-inline">\\(A\\)</span> is not invertible, which means <span class="math-inline">\\(\text{det}(A) = 0\\)</span>. So,

<div class="math-display">
$$
\begin{align*}
\det(A) &= (3)(4) - (2)(k) = 12 - 2k = 0 \\\\
2k &= 12 \\\\
k &= 6
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
<span class="math-inline">\\(\text{det}(A) = 2\\)</span>

<div class="math-display">
$$
k = \_\_\_\_\_\_
$$
</div>

<details markdown="1"><summary>Solution</summary>

The determinant of a <span class="math-inline">\\(2 \times 2\\)</span> matrix <span class="math-inline">\\(\begin{bmatrix} a &amp; b \\\\ c &amp; d \end{bmatrix}\\)</span> is <span class="math-inline">\\(ad - bc\\)</span>. So,

<div class="math-display">
$$
\begin{align*}
\det(A) &= (3)(4) - (2)(k) = 12 - 2k
\end{align*}
$$
</div>

We're told that <span class="math-inline">\\(\det(A) = 2\\)</span>, so

<div class="math-display">
$$
\begin{align*}
12 - 2k &= 2 \\\\
2k &= 10 \\\\
k &= 5
\end{align*}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span>
<span class="math-inline">\\(A^{-1} = \begin{bmatrix} 1 &amp; -1/2 \\\\ -1 &amp; 3/4 \end{bmatrix}\\)</span>

<div class="math-display">
$$
k = \_\_\_\_\_\_
$$
</div>

<details markdown="1"><summary>Solution</summary>

The inverse of a <span class="math-inline">\\(2 \times 2\\)</span> matrix <span class="math-inline">\\(\begin{bmatrix} a &amp; b \\\\ c &amp; d \end{bmatrix}\\)</span> is <span class="math-inline">\\(\frac{1}{ad - bc} \begin{bmatrix} d &amp; -b \\\\ -c &amp; a \end{bmatrix}\\)</span>. So,

<div class="math-display">
$$
\begin{align*}
A^{-1} &= \frac{1}{12 - 2k} \begin{bmatrix} 4 & -2 \\\\ -k & 3 \end{bmatrix}
\end{align*}
$$
</div>

Since we're told that

<div class="math-display">
$$
A^{-1} = \begin{bmatrix} 1 & -1/2 \\\\ -1 & 3/4 \end{bmatrix},
$$
</div>

 we can match entries. For example, using the bottom-right entry,

<div class="math-display">
$$
\begin{align*}
\frac{3}{12 - 2k} &= \frac{3}{4} \\\\
12 - 2k &= 4 \\\\
2k &= 8 \\\\
k &= 4
\end{align*}
$$
</div>

</details>

</div>
</div>

</div>

---

## WN26 Final · Problem 9 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>

<p class="worksheet-source">From <a href="/exams/wn26-final/">WN26 Final</a></p>

Consider the matrix <span class="math-inline">\\(A = \begin{bmatrix} 2 &amp; 3 \\\\ -4 &amp; k \end{bmatrix}\\)</span> where <span class="math-inline">\\(k \in \mathbb{R}\\)</span> is some unknown constant.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> Suppose <span class="math-inline">\\(\lambda&#95;1 = 0\\)</span> is an eigenvalue of <span class="math-inline">\\(A\\)</span>. Find the value of <span class="math-inline">\\(k\\)</span>. Give your answer as a number with no variables.

<span class="math-inline">\\(k = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>

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
k = \_\_\_\_\_\_
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
\lambda_2 = \_\_\_\_\_\_
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

## WN26 Final · Problem 10 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">14 pts</span>

<p class="worksheet-source">From <a href="/exams/wn26-final/">WN26 Final</a></p>

The state diagram below describes a Markov chain with four states.

![image](imgs/wn26-final-q10/tikz-4049c66dfd05.svg)

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Find the adjacency matrix <span class="math-inline">\\(A\\)</span> for this Markov chain.

<span class="math-inline">\\(A =\\)</span> \_\_\_\_\_\_

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

State 1: \_\_\_\_\_\_ State 2: \_\_\_\_\_\_ State 3: \_\_\_\_\_\_ State 4: \_\_\_\_\_\_

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

![image](imgs/wn26-final-q10/tikz-d6c2facf0597.svg)

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

## WN26 Final · Problem 11 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">10 pts</span>

<p class="worksheet-source">From <a href="/exams/wn26-final/">WN26 Final</a></p>

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

<span class="math-inline">\\(S^2 \vec x = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;  \vec v&#95;1 + \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;  \vec v&#95;2 + \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;  \vec v&#95;3\\)</span>

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

## SP26 Final · Problem 10 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>

<p class="worksheet-source">From <a href="/exams/sp26-final/">SP26 Final</a></p>

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

## SP26 Final · Problem 11 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">10 pts</span>

<p class="worksheet-source">From <a href="/exams/sp26-final/">SP26 Final</a></p>

The state diagram below describes a Markov chain with three states. <span class="math-inline">\\(a\\)</span> and <span class="math-inline">\\(b\\)</span> are both constants between 0 and 1.

![image](imgs/sp26-final-q11/tikz-c9b7fae1abbb.svg)

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

## SP26 Final · Problem 12 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">11 pts</span>

<p class="worksheet-source">From <a href="/exams/sp26-final/">SP26 Final</a></p>

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
\Lambda = \_\_\_\_\_\_
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
A\vec v = \_\_\_\_\_\_
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

{% endraw %}
