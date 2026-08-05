---
layout: minimal
title: "Chapter 10: Singular Value Decomposition"
description: "Practice problems for Chapter 10: Singular Value Decomposition."
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

# Chapter 10: Singular Value Decomposition

*Topics: computing SVD, low-rank approximation, best direction, principal components analysis*

*Problems below are collected from past exams; each links back to its full exam. Solutions are in the dropdowns.*

## Problems

- [FA25 Final · Problem 12](#fa25-final--problem-12-12-pts)
- [WN26 Final · Problem 12](#wn26-final--problem-12-12-pts)
- [SP26 Final · Problem 13](#sp26-final--problem-13-12-pts)

---

## FA25 Final · Problem 12 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>

<p class="worksheet-source">From <a href="/exams/fa25/final/">FA25 Final</a></p>

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

<span class="math-inline">\\(\text{rank}(\tilde X) = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>

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

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Impossible to tell</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> False</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Impossible to tell</span></div>

This is **False**. The eigenvalues of <span class="math-inline">\\(\tilde X \tilde X^T\\)</span> are the squares of the singular values of <span class="math-inline">\\(\tilde X\\)</span>, so they are <span class="math-inline">\\(144\\)</span>, <span class="math-inline">\\(4\\)</span>, and <span class="math-inline">\\(0\\)</span>. Since 2 is not an eigenvalue of <span class="math-inline">\\(\tilde X \tilde X^T\\)</span>, no such vector <span class="math-inline">\\(\vec z\\)</span> exists.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">5 pts</span> What is the largest possible variance of the components of <span class="math-inline">\\(\tilde X \vec w\\)</span>, where <span class="math-inline">\\(\vec w \in \mathbb{R}^3\\)</span> is a unit vector? Select one of the answers below, then justify your answer in the box provided.

1.  Answer:
<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(6\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(12\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(24\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(144\\)</span></span></div>

2.  Justify your answer in the box below.

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(2\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(6\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(12\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(24\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(144\\)</span></span></div>

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

## WN26 Final · Problem 12 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>

<p class="worksheet-source">From <a href="/exams/wn26/final/">WN26 Final</a></p>

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

<span class="math-inline">\\(\vec v&#95;1 = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>

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

<span class="math-inline">\\(n = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>

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

## SP26 Final · Problem 13 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>

<p class="worksheet-source">From <a href="/exams/sp26/final/">SP26 Final</a></p>

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

maximum possible variance of principal component <span class="math-inline">\\(2\\)</span> = \_\_\_\_\_\_

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

{% endraw %}
