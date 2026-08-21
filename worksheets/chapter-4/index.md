---
layout: minimal
title: "Chapter 4: Linear Independence"
description: "Practice problems for Chapter 4: Linear Independence."
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

# Chapter 4: Linear Independence

*Topics: span, linear independence, lines/planes/hyperplanes, vector spaces/basis/dimension*

Problems below are collected from past exams; each links back to its full exam. Solutions are in the dropdowns.

## Problems

- [FA25 MT1 · Problem 6](#fa25-mt1--problem-6-needed-me-11-pts)
- [FA25 MT1 · Problem 7](#fa25-mt1--problem-7-high-definition-12-pts)
- [FA25 Final · Problem 4](#fa25-final--problem-4-8-pts-mt2-redemption)
- [WN26 MT1 · Problem 6](#wn26-mt1--problem-6-14-pts)
- [WN26 Final · Problem 4](#wn26-final--problem-4-4-pts-mt1-redemption)
- [SP26 MT1 · Problem 6](#sp26-mt1--problem-6-11-pts)
- [SP26 MT1 · Problem 7](#sp26-mt1--problem-7-10-pts)
- [SP26 MT1 · Problem 8](#sp26-mt1--problem-8-8-pts)
- [SP26 Final · Problem 4](#sp26-final--problem-4-5-pts-mt1-redemption)

---

## FA25 MT1 · Problem 6: Needed Me <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">11 pts</span>

<p class="worksheet-source">From <a href="/exams/fa25-mt1/">FA25 MT1</a></p>

Suppose <span class="math-inline">\\(\vec x = \begin{bmatrix} c \\\\ 1 \\\\ 0 \end{bmatrix}\\)</span>, <span class="math-inline">\\(\vec y = \begin{bmatrix} 1 \\\\ c \\\\ 1 \end{bmatrix}\\)</span>, and <span class="math-inline">\\(\vec z = \begin{bmatrix} 0 \\\\ 1 \\\\ c \end{bmatrix}\\)</span>, where <span class="math-inline">\\(c \in \mathbb{R}\\)</span> is a constant.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">8 pts</span> Find a **positive value** of <span class="math-inline">\\(c\\)</span> such that <span class="math-inline">\\(\vec x\\)</span>, <span class="math-inline">\\(\vec y\\)</span>, and <span class="math-inline">\\(\vec z\\)</span> are linearly **dependent**. Show your work, and <span class="math-inline">\\(\boxed{\text{circle}}\\)</span> your final answer, which should be a positive number with no variables.

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(c = \sqrt{2}\\)</span>.

For <span class="math-inline">\\(\vec x\\)</span>, <span class="math-inline">\\(\vec y\\)</span>, and <span class="math-inline">\\(\vec z\\)</span> to be linearly dependent, there must exist scalars <span class="math-inline">\\(a\\)</span>, <span class="math-inline">\\(b\\)</span>, and <span class="math-inline">\\(c\\)</span> such that

<div class="math-display">
$$
a \vec x + b \vec y + \vec z
$$
</div>

(or equivalently, <span class="math-inline">\\(a \vec x + b \vec y + d\vec z = \vec 0\\)</span>, but the former approach involves one fewer variable to solve for).

Substituting in the given vectors, we have

<div class="math-display">
$$
a \begin{bmatrix} c \\\\ 1 \\\\ 0 \end{bmatrix} + b \begin{bmatrix} 1 \\\\ c \\\\ 1 \end{bmatrix} = \begin{bmatrix} 0 \\\\ 1 \\\\ c \end{bmatrix}
$$
</div>

As a system of equations, we have

<div class="math-display">
$$
\begin{align*}
c a + b &= 0 \\\\
a + c b &= 1 \\\\
b &= c
\end{align*}
$$
</div>

The third equation gives us <span class="math-inline">\\(b = c\\)</span>, and the second gives us <span class="math-inline">\\(a = 1 - cb = 1 - c^2\\)</span>. Substituting these into the first equation gives us

<div class="math-display">
$$
c(1 - c^2) + c = 0 \implies c - c^3 + c = 0 \implies c(2 - c^2) = 0
$$
</div>

This equation has three solutions for <span class="math-inline">\\(c\\)</span>: <span class="math-inline">\\(c = 0\\)</span>, <span class="math-inline">\\(c = \sqrt{2}\\)</span>, and <span class="math-inline">\\(c = -\sqrt{2}\\)</span>. We're asked to find a **positive** value of <span class="math-inline">\\(c\\)</span>, so <span class="math-inline">\\(c = \sqrt{2}\\)</span> for this part, and either <span class="math-inline">\\(0\\)</span> or <span class="math-inline">\\(-\sqrt{2}\\)</span> for the next part.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> Provide one **other** value of <span class="math-inline">\\(c\\)</span> (that is, not your answer from the previous part) such that <span class="math-inline">\\(\vec x\\)</span>, <span class="math-inline">\\(\vec y\\)</span>, and <span class="math-inline">\\(\vec z\\)</span> are linearly **dependent**. Your answer should be a number with no variables.

other value of <span class="math-inline">\\(c =\\)</span> \_\_\_\_\_\_

</div>
</div>

</div>

---

## FA25 MT1 · Problem 7: High Definition <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>

<p class="worksheet-source">From <a href="/exams/fa25-mt1/">FA25 MT1</a></p>

Suppose <span class="math-inline">\\(\vec x&#95;1, \vec x&#95;2, \ldots \vec x&#95;{12}\\)</span> are 12 non-zero vectors in <span class="math-inline">\\(\mathbb{R}^{7}\\)</span>. Furthermore, suppose:

-   <span class="math-inline">\\(\vec x&#95;1\\)</span>, <span class="math-inline">\\(\vec x&#95;2\\)</span>, and <span class="math-inline">\\(\vec x&#95;3\\)</span> span a 2-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^{7}\\)</span>.

-   <span class="math-inline">\\(\vec x&#95;4\\)</span>, <span class="math-inline">\\(\vec x&#95;5\\)</span>, and <span class="math-inline">\\(\vec x&#95;6\\)</span> span **the same** 2-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^{7}\\)</span> as <span class="math-inline">\\(\vec x&#95;1\\)</span>, <span class="math-inline">\\(\vec x&#95;2\\)</span>, and <span class="math-inline">\\(\vec x&#95;3\\)</span>, i.e.

<div class="math-display">
$$
\text{span}(\{\vec x_4, \vec x_5, \vec x_6\}) = \text{span}(\{\vec x_1, \vec x_2, \vec x_3\})
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Let <span class="math-inline">\\(r\\)</span> be the dimension of the subspace of <span class="math-inline">\\(\mathbb{R}^{7}\\)</span> spanned by <span class="math-inline">\\(\vec x&#95;1, \vec x&#95;2, \ldots \vec x&#95;{12}\\)</span>. What are the smallest and largest possible values of <span class="math-inline">\\(r\\)</span>? Your answers should be integers with no variables.

smallest possible value of <span class="math-inline">\\(r =\\)</span> \_\_\_\_\_\_ largest possible value of <span class="math-inline">\\(r =\\)</span> \_\_\_\_\_\_

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Which of the following **could** form a basis for <span class="math-inline">\\(\mathbb{R}^{7}\\)</span>? Select all that apply. Blank answers will receive no credit.

<span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\lbrace\vec x&#95;7, \vec x&#95;8, \vec x&#95;9, \vec x&#95;{10}, \vec x&#95;{11}, \vec x&#95;{12}\rbrace\\)</span>

<span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\lbrace\vec x&#95;6, \vec x&#95;7, \vec x&#95;8, \vec x&#95;9, \vec x&#95;{10}, \vec x&#95;{11}, \vec x&#95;{12}\rbrace\\)</span>

<span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\lbrace\vec x&#95;1, \vec x&#95;5, \vec x&#95;8, \vec x&#95;9, \vec x&#95;{10}, \vec x&#95;{11}, \vec x&#95;{12}\rbrace\\)</span>

<span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\lbrace\vec x&#95;1, \vec x&#95;2, \vec x&#95;5, \vec x&#95;9, \vec x&#95;{10}, \vec x&#95;{11}, \vec x&#95;{12}\rbrace\\)</span>

<span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\lbrace\vec x&#95;1, \vec x&#95;2, \vec x&#95;8, \vec x&#95;9, \vec x&#95;{10}, \vec x&#95;{11}, \vec x&#95;{12}\rbrace\\)</span>

<details markdown="1"><summary>Solution</summary>

<span class="mc-square mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(\lbrace\vec x&#95;1, \vec x&#95;2, \vec x&#95;8, \vec x&#95;9, \vec x&#95;{10}, \vec x&#95;{11}, \vec x&#95;{12}\rbrace\\)</span>

The first choice only includes 6 vectors, but since the span of <span class="math-inline">\\(\vec x&#95;1, \vec x&#95;2, \ldots \vec x&#95;{12}\\)</span> is 7-dimensional, it must include at least 7 vectors. So, the first choice is not a valid basis.

The fourth choice includes 7 vectors, but we know that <span class="math-inline">\\(\vec x&#95;1, \vec x&#95;2, \vec x&#95;5\\)</span> are a linearly **dependent** set since they all lie on the same 2-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^7\\)</span> (and you only need 2 vectors to uniquely define a 2-dimensional subspace), so the fourth choice is not a valid basis.

The other options all include 7 vectors that *could* be linearly independent, and so they could form a basis for <span class="math-inline">\\(\mathbb{R}^7\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Suppose the intersection of <span class="math-inline">\\(\text{span}(\lbrace\vec x&#95;1, \vec x&#95;2\rbrace)\\)</span> and <span class="math-inline">\\(\text{span}(\lbrace \vec x&#95;4, \vec x&#95;5 \rbrace)\\)</span> is a line (i.e. a 1-dimensional subspace) in <span class="math-inline">\\(\mathbb{R}^{7}\\)</span>. Which of the following **must** be true? Select all that apply. Blank answers will receive no credit.

<em>Hint: Don't forget the assumptions introduced at the start of the problem.</em>

<span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\vec x&#95;2\\)</span>, <span class="math-inline">\\(\vec x&#95;4\\)</span>, and <span class="math-inline">\\(\vec x&#95;5\\)</span> can all be written as scalar multiples of <span class="math-inline">\\(\vec x&#95;1\\)</span>.

<span class="mc-square" aria-hidden="true"></span> The set <span class="math-inline">\\(\lbrace \vec x&#95;2, \vec x&#95;4 \rbrace\\)</span> is linearly independent.

<span class="mc-square" aria-hidden="true"></span> The set <span class="math-inline">\\(\lbrace \vec x&#95;3, \vec x&#95;4 \rbrace\\)</span> is linearly independent.

<span class="mc-square" aria-hidden="true"></span> The set <span class="math-inline">\\(\lbrace \vec x&#95;3, \vec x&#95;6 \rbrace\\)</span> is linearly independent.

<span class="mc-square" aria-hidden="true"></span> None of the above.

<details markdown="1"><summary>Solution</summary>

<span class="mc-square" aria-hidden="true"></span> None of the above.

The intended answer to the problem was options 1 and 3. The scenario we had in mind was that <span class="math-inline">\\(\operatorname{span}(\lbrace\vec x&#95;1, \vec x&#95;2\rbrace) = \operatorname{span}(\lbrace\vec x&#95;4, \vec x&#95;5\rbrace) = \text{the same line}\\)</span>. The two spans can't both be different planes that happen to intersect in a line, since we're told that <span class="math-inline">\\(\vec x&#95;1, \vec x&#95;2, \vec x&#95;3\\)</span> span a 2-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^7\\)</span> and <span class="math-inline">\\(\vec x&#95;4, \vec x&#95;5, \vec x&#95;6\\)</span> span the same 2-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^7\\)</span>. So, if the two spans are planes, they're the same plane, and they would intersect at a plane. Since the two spans intersect at a line, **we thought** they'd both have to be lines. If that was the case, then <span class="math-inline">\\(\vec x&#95;2\\)</span>, <span class="math-inline">\\(\vec x&#95;4\\)</span>, and <span class="math-inline">\\(\vec x&#95;5\\)</span> would all be scalar multiples of <span class="math-inline">\\(\vec x&#95;1\\)</span>, and so <span class="math-inline">\\(\vec x&#95;3\\)</span> would have to not be on that line (for <span class="math-inline">\\(\vec x&#95;1, \vec x&#95;2, \vec x&#95;3\\)</span> to span a 2-dimensional subspace), which is why Options 1 and 3 were our originally intended answers.

But after releasing exam scores, a student brought up a possibility we hadn't considered: it's possible that <span class="math-inline">\\(\operatorname{span}(\lbrace\vec x&#95;1, \vec x&#95;2\rbrace)\\)</span> is a plane, and <span class="math-inline">\\(\operatorname{span}(\lbrace\vec x&#95;4, \vec x&#95;5\rbrace)\\)</span> is a line that is contained on that plane. That setup would satisfy all of the assumptions provided in the problem statement, but it would imply that none of the options are true.

So, retroactively, we gave full credit to everyone for this part.
</details>

</div>
</div>

</div>

---

## FA25 Final · Problem 4 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">8 pts</span> <span class="badge" data-flag="mt2-redemption" style="background-color: #9A3324; color: #FFFFFF; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">MT2 Redemption</span>

<p class="worksheet-source">From <a href="/exams/fa25-final/">FA25 Final</a></p>

Let <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> be as in the previous problem.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Suppose that for some value of <span class="math-inline">\\(c\\)</span>, <span class="math-inline">\\(P\\)</span> is the matrix that projects vectors in <span class="math-inline">\\(\mathbb{R}^3\\)</span> onto <span class="math-inline">\\(\text{span}(\lbrace\vec u, \vec v\rbrace)\\)</span>. **Select all** true statements below.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(P^2 = P\\)</span></span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(P\\)</span> is invertible</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(P\\)</span> is orthogonal</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(P\\)</span> is symmetric</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-square mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(P^2 = P\\)</span></span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(P\\)</span> is invertible</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(P\\)</span> is orthogonal</span><span class="mc-option"><span class="mc-square mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(P\\)</span> is symmetric</span></div>

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

## WN26 MT1 · Problem 6 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">14 pts</span>

<p class="worksheet-source">From <a href="/exams/wn26-mt1/">WN26 MT1</a></p>

Suppose <span class="math-inline">\\(\vec x&#95;1, \vec x&#95;2, \vec x&#95;3, \vec x&#95;4, \vec x&#95;5, \vec x&#95;6\\)</span> are 6 vectors in <span class="math-inline">\\(\mathbb{R}^9\\)</span> such that

<div class="math-display">
$$
S = \text{span}\left(\{\vec x_1, \vec x_2, \vec x_3, \vec x_4, \vec x_5, \vec x_6\}\right)
$$
</div>

 is a **4-dimensional** subspace of <span class="math-inline">\\(\mathbb{R}^9\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">2 pts</span> True or False: The set <span class="math-inline">\\(\lbrace\vec x&#95;1, \vec x&#95;2, \vec x&#95;3, \vec x&#95;4, \vec x&#95;5, \vec x&#95;6\rbrace\\)</span> is linearly independent.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> False</span></div>

This is false.

If these vectors were linearly independent, they would span a 6-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^9\\)</span>; since they only span a 4-dimensional subspace, they must be linearly dependent, and two of them are "redundant".
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Consider the statement:

"There exists a vector <span class="math-inline">\\(\vec b \in \mathbb{R}^9\\)</span> such that the number of ways to write <span class="math-inline">\\(\vec b\\)</span> as a linear combination of <span class="math-inline">\\(\vec x&#95;1, \ldots, \vec x&#95;6\\)</span> is ."

In each part below, a possible way to fill in the blank is given. Determine whether the statement that results from filling in the blank is **True** or **False**.

1.  zero

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

{: start="2"}
2.  exactly one

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

{: start="3"}
3.  exactly two

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

{: start="4"}
4.  infinite

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

-   **(True) zero ways**: <span class="math-inline">\\(S\\)</span>, the set of all linear combinations of <span class="math-inline">\\(\vec x&#95;1, \ldots, \vec x&#95;6\\)</span>, is a 4-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^9\\)</span>. Since <span class="math-inline">\\(S\\)</span> isn't all of <span class="math-inline">\\(\mathbb{R}^9\\)</span>, there are plenty of vectors <span class="math-inline">\\(\vec b \in \mathbb{R}^9\\)</span> that are not in <span class="math-inline">\\(S\\)</span>, and therefore can't be written as a linear combination of <span class="math-inline">\\(\vec x&#95;1, \ldots, \vec x&#95;6\\)</span>. So, it's true that there are some <span class="math-inline">\\(\vec b\\)</span>'s such that there are zero ways to write <span class="math-inline">\\(\vec b\\)</span> as a linear combination of <span class="math-inline">\\(\vec x&#95;1, \ldots, \vec x&#95;6\\)</span>.

-   **(False) exactly one way**: Linear combinations are only unique if the spanning vectors are linearly independent. Since <span class="math-inline">\\(\vec x&#95;1, \ldots, \vec x&#95;6\\)</span> are linearly dependent, there is a non-trivial linear combination of them that equals the zero vector, which could be added to any other existing linear combination that sums to <span class="math-inline">\\(\vec b\\)</span> to "invent" a new, different-looking linear combination that sums to <span class="math-inline">\\(\vec b\\)</span>. So, it's false that there is exactly one way to write <span class="math-inline">\\(\vec b\\)</span> as a linear combination of <span class="math-inline">\\(\vec x&#95;1, \ldots, \vec x&#95;6\\)</span> --- if there is one way, there are infinitely many.

-   **(False) exactly two ways**: Same logic as above. If this thinking is a bit confusing, see the solution to part **c)**.

-   **(True) infinite ways**: For any vector <span class="math-inline">\\(\vec b \in S\\)</span>, there are infinitely many ways to write <span class="math-inline">\\(\vec b\\)</span> as a linear combination of <span class="math-inline">\\(\vec x&#95;1, \ldots, \vec x&#95;6\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Suppose <span class="math-inline">\\(\vec b\\)</span> is some vector in <span class="math-inline">\\(S\\)</span> such that both of the following equations are true:

<div class="math-display">
$$

$$
</div>

\begin{aligned}
\vec b &= 4 \vec x_1 - 2 \vec x_2 + 6 \vec x_3

\vec b &= 3 \vec x_1 + 3 \vec x_3 - \vec x_5
\end{aligned}

<div class="math-display">
$$

$$
</div>

State **one** other linear combination of <span class="math-inline">\\(\vec x&#95;1, \ldots, \vec x&#95;6\\)</span> that is equal to <span class="math-inline">\\(\vec b\\)</span>. Fill in each box with a number with no variables.

<span class="math-inline">\\(\vec b = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;  \vec x&#95;1 + \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;  \vec x&#95;2 + \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;  \vec x&#95;3 + \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;  \vec x&#95;4 + \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;  \vec x&#95;5 + \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;  \vec x&#95;6\\)</span>

<details markdown="1"><summary>Solution</summary>

Arguably, answering part **c)** may have helped clarify the answer to part **b)**.

Let's try adding the two representation of <span class="math-inline">\\(\vec b\\)</span> together.

<div class="math-display">
$$

$$
</div>

\begin{aligned}
\vec b &= 4 \vec x_1 - 2 \vec x_2 + 6 \vec x_3

\vec b &= 3 \vec x_1 + 3 \vec x_3 - \vec x_5

\implies 2 \vec b &= 7 \vec x_1 - 2 \vec x_2 + 9 \vec x_3 - \vec x_5
\end{aligned}

<div class="math-display">
$$

$$
</div>

Dividing both sides by 2 gives us

<div class="math-display">
$$
\boxed{\vec b = \frac{7}{2} \vec x_1 - \vec x_2 + \frac{9}{2} \vec x_3 - \frac{1}{2} \vec x_5}
$$
</div>

This is not the only possible answer, but it's probably the easiest one. For example, you could repeat this process with one of the original two <span class="math-inline">\\(\vec b\\)</span>'s along with the new representation of <span class="math-inline">\\(\vec b\\)</span> to get another valid representation of <span class="math-inline">\\(\vec b\\)</span>.

You also could have subtracted the two representations of <span class="math-inline">\\(\vec b\\)</span> to get a linear combination of <span class="math-inline">\\(\vec x&#95;1, \ldots, \vec x&#95;6\\)</span> that equals the zero vector, which could be added to any other existing linear combination that sums to <span class="math-inline">\\(\vec b\\)</span> to "invent" a new, different-looking linear combination that sums to <span class="math-inline">\\(\vec b\\)</span> (as we said in the solution to part **b)**). If you did this, you'd find that

<div class="math-display">
$$
\vec 0 = \vec x_1 - 2 \vec x_2 + 3 \vec x_3 + \vec x_5
$$
</div>

This must mean that

<div class="math-display">
$$
\vec b + \vec 0 = (4 \vec x_1 - 2 \vec x_2 + 6 \vec x_3) + (\vec x_1 - 2 \vec x_2 + 3 \vec x_3 + \vec x_5) = 5 \vec x_1 - 4 \vec x_2 + 9 \vec x_3 + \vec x_5
$$
</div>

is another way to represent <span class="math-inline">\\(\vec b\\)</span> as a linear combination of <span class="math-inline">\\(\vec x&#95;1, \ldots, \vec x&#95;6\\)</span>,

and so is

<div class="math-display">
$$
\vec b + 245 (\vec 0) = (4 \vec x_1 - 2 \vec x_2 + 6 \vec x_3) + 245(\vec x_1 - 2 \vec x_2 + 3 \vec x_3 + \vec x_5)
$$
</div>

(for instance).
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Let <span class="math-inline">\\(T = \text{span}(\lbrace \vec x&#95;1, \vec x&#95;2, \vec x&#95;3 \rbrace)\\)</span> and <span class="math-inline">\\(U = \text{span}(\lbrace \vec x&#95;4, \vec x&#95;5, \vec x&#95;6 \rbrace)\\)</span>. Suppose <span class="math-inline">\\(W\\)</span> is the **intersection** of <span class="math-inline">\\(T\\)</span> and <span class="math-inline">\\(U\\)</span>, i.e. <span class="math-inline">\\(W = T \cap U\\)</span>. <span class="math-inline">\\(W\\)</span> is also a subspace of <span class="math-inline">\\(\mathbb{R}^9\\)</span>.

What are the smallest and largest possible values of <span class="math-inline">\\(\text{dim}(W)\\)</span>, the dimension of <span class="math-inline">\\(W\\)</span>? Give your answers as integers.

<span class="math-inline">\\(=\\)</span> \_\_\_\_\_\_ <span class="math-inline">\\(=\\)</span> \_\_\_\_\_\_

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(T\\)</span> and <span class="math-inline">\\(U\\)</span> are each individually at most 3-dimensional, since they are each spanned by 3 vectors. So, the intersection <span class="math-inline">\\(W\\)</span> must be at most 3-dimensional. This means the possible dimensions to consider are 3, 2, 1, or 0. Let's reason about them, starting with 3.

To give examples, we'll use the standard basis vectors <span class="math-inline">\\(\vec e&#95;1, \vec e&#95;2, \ldots, \vec e&#95;9\\)</span> of <span class="math-inline">\\(\mathbb{R}^9\\)</span>. In <span class="math-inline">\\(\mathbb{R}^2\\)</span>, <span class="math-inline">\\(\vec e&#95;1 = \begin{bmatrix} 1 \\\\ 0 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec e&#95;2 = \begin{bmatrix} 0 \\\\ 1 \end{bmatrix}\\)</span>, so (for instance) in <span class="math-inline">\\(\mathbb{R}^9\\)</span>,

<div class="math-display">
$$
\vec e_5 = \begin{bmatrix} 0 \\\\ 0 \\\\ 0 \\\\ 0 \\\\ 1 \\\\ 0 \\\\ 0 \\\\ 0 \\\\ 0 \end{bmatrix}
$$
</div>

-   Could <span class="math-inline">\\(\text{dim}(W) = 3\\)</span>? **No**. If <span class="math-inline">\\(\text{dim}(W) = 3\\)</span>, it would mean that <span class="math-inline">\\(T\\)</span> and <span class="math-inline">\\(U\\)</span> are both **the same** 3-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^9\\)</span>, and intersect everywhere. But if that were the case, then <span class="math-inline">\\(S = \text{span}(\lbrace \vec x&#95;1, \vec x&#95;2, \vec x&#95;3, \vec x&#95;4, \vec x&#95;5, \vec x&#95;6 \rbrace)\\)</span> would be a 3-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^9\\)</span>, which contradicts the problem statement that <span class="math-inline">\\(S\\)</span> is a 4-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^9\\)</span>. So, <span class="math-inline">\\(\text{dim}(W) &lt; 3\\)</span>, and the maximum possible value is something less than 3.

-   Could <span class="math-inline">\\(\text{dim}(W) = 2\\)</span>? **Yes**, and all smaller values are also possible. <span class="math-inline">\\(T\\)</span> and <span class="math-inline">\\(U\\)</span> could overlap in a 2-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^9\\)</span>, while each containing a direction that the other doesn't.

   For example, <span class="math-inline">\\(T\\)</span> could be the span of <span class="math-inline">\\(\lbrace\vec e&#95;1, \vec e&#95;2, \vec e&#95;3\rbrace\\)</span> and <span class="math-inline">\\(U\\)</span> could be the span of <span class="math-inline">\\(\lbrace\vec e&#95;2, \vec e&#95;3, \vec e&#95;4\rbrace\\)</span>. In this case, <span class="math-inline">\\(W\\)</span> would be the span of <span class="math-inline">\\(\lbrace\vec e&#95;2, \vec e&#95;3\rbrace\\)</span>, which is a 2-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^9\\)</span>.

-   Could <span class="math-inline">\\(\text{dim}(W) = 1\\)</span>? **Yes**. For example, <span class="math-inline">\\(T\\)</span> could be the span of <span class="math-inline">\\(\lbrace\vec e&#95;1, \vec e&#95;2\rbrace\\)</span> and <span class="math-inline">\\(U\\)</span> could be the span of <span class="math-inline">\\(\lbrace\vec e&#95;2, \vec e&#95;3, \vec e&#95;4 \rbrace\\)</span>. In this case, <span class="math-inline">\\(W\\)</span> would be the span of <span class="math-inline">\\(\lbrace\vec e&#95;2\rbrace\\)</span>, which is 1-dimensional, while <span class="math-inline">\\(S\\)</span> would still be 4-dimensional. (In this example, we said that <span class="math-inline">\\(T\\)</span> is the span of <span class="math-inline">\\(\vec e&#95;1\\)</span> and <span class="math-inline">\\(\vec e&#95;2\\)</span> though we defined it in the problem statement to be the span of three vectors. No problem --- just pick the third vector to be a linear combination of <span class="math-inline">\\(\vec e&#95;1\\)</span> and <span class="math-inline">\\(\vec e&#95;2\\)</span>. That is, <span class="math-inline">\\(\vec x&#95;1 = \vec e&#95;1\\)</span>, <span class="math-inline">\\(\vec x&#95;2 = \vec e&#95;2\\)</span>, and <span class="math-inline">\\(\vec x&#95;3 = \vec e&#95;1 + \vec e&#95;2\\)</span> would work as an example.)

-   Could <span class="math-inline">\\(\text{dim}(W) = 0\\)</span>? **Yes**. <span class="math-inline">\\(T\\)</span> and <span class="math-inline">\\(U\\)</span> could be two completely disjoint subspaces, except for <span class="math-inline">\\(\vec 0\\)</span>, which is in every subspace.

   For example, let <span class="math-inline">\\(\vec x&#95;1 = \vec e&#95;1\\)</span>, <span class="math-inline">\\(\vec x&#95;2 = \vec e&#95;2\\)</span>, <span class="math-inline">\\(\vec x&#95;3 = \vec e&#95;1 + \vec e&#95;2\\)</span>, which makes <span class="math-inline">\\(T\\)</span> a 2-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^9\\)</span>, and <span class="math-inline">\\(\vec x&#95;4 = \vec e&#95;3\\)</span>, <span class="math-inline">\\(\vec x&#95;5 = \vec e&#95;4\\)</span>, <span class="math-inline">\\(\vec x&#95;6 = \vec e&#95;3 + \vec e&#95;4\\)</span>, which makes <span class="math-inline">\\(U\\)</span> a 2-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^9\\)</span>. In this case, <span class="math-inline">\\(W\\)</span> would be the set <span class="math-inline">\\(\lbrace\vec 0\rbrace\\)</span>, while <span class="math-inline">\\(S\\)</span> would still be 4-dimensional.

So, the smallest possible value of <span class="math-inline">\\(\text{dim}(W)\\)</span> is <span class="math-inline">\\(\boxed{0}\\)</span>, and the largest possible value is <span class="math-inline">\\(\boxed{2}\\)</span>.
</details>

</div>
</div>

</div>

---

## WN26 Final · Problem 4 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> <span class="badge" data-flag="mt1-redemption" style="background-color: #9A3324; color: #FFFFFF; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">MT1 Redemption</span>

<p class="worksheet-source">From <a href="/exams/wn26-final/">WN26 Final</a></p>

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

<span class="math-inline">\\(\dim(S)=\&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>

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

## SP26 MT1 · Problem 6 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">11 pts</span>

<p class="worksheet-source">From <a href="/exams/sp26-mt1/">SP26 MT1</a></p>

Suppose <span class="math-inline">\\(c \in \mathbb R\\)</span> is a constant and

<div class="math-display">
$$
\vec u=\begin{bmatrix}3\\\\1\\\\c\end{bmatrix},
\qquad
\vec v=\begin{bmatrix}6\\\\c\\\\-2\end{bmatrix}
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Fill in the blanks to complete the sentence:

For all values of <span class="math-inline">\\(c\\)</span>, <span class="math-inline">\\(\text{span}(\lbrace\vec u,\vec v\rbrace)\\)</span> is a \_\_(i)\_\_-dimensional subspace of \_\_(ii)\_\_.

(i): \_\_\_\_\_\_ (ii): \_\_\_\_\_\_

<details markdown="1"><summary>Solution</summary>

The vectors <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> are never scalar multiples of each other. If <span class="math-inline">\\(\vec v=\lambda\vec u\\)</span>, then the first entries force <span class="math-inline">\\(\lambda=2\\)</span>, the second entries force <span class="math-inline">\\(c=2\\)</span>, and the third entries force <span class="math-inline">\\(-2=2c=4\\)</span>, which is impossible. Therefore, the span is always a 2-dimensional subspace of <span class="math-inline">\\(\mathbb R^3\\)</span>.

Why <span class="math-inline">\\(\mathbb R^3\\)</span>? Because both <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> live in <span class="math-inline">\\(\mathbb R^3\\)</span>, so their span must also live in <span class="math-inline">\\(\mathbb R^3\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">7 pts</span> Suppose the plane spanned by <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> is

<div class="math-display">
$$
ax+24y+3z=0
$$
</div>

 where <span class="math-inline">\\(a\\)</span> is also a constant. Find the value of <span class="math-inline">\\(c\\)</span>. Show your work in the space provided, and write your final answer in the box provided. Your answer should be a number with no variables.

<div class="math-display">
$$
c = \_\_\_\_\_\_
$$
</div>

<details markdown="1"><summary>Solution</summary>

There are a few ways to approach this. The first way starts by using the fact that <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> lie in the plane, which gives us a system of two equations and two unknowns. Plugging in the coordinates of <span class="math-inline">\\(\vec u\\)</span> into the plane gives us

<div class="math-display">
$$
3a+24+3c=0 \implies a + 8 + c = 0
$$
</div>

 and plugging in the coordinates of <span class="math-inline">\\(\vec v\\)</span> into the plane gives us

<div class="math-display">
$$
6a+24c-6=0 \implies a + 4c - 1 = 0
$$
</div>

 Subtracting the simplified versions of the two equations gives us

<div class="math-display">
$$
(8 + c) - (4c - 1) = 0 \implies 9 - 3c = 0 \implies c = 3
$$
</div>

Another way to approach this is to find the cross product of <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span>, and try and write it as a scalar multiple of the vector <span class="math-inline">\\(\begin{bmatrix} a \\\\ 24 \\\\ 3 \end{bmatrix}\\)</span>.

<div class="math-display">
$$
\vec u \times \vec v = \begin{bmatrix} 3 \\\\ 1 \\\\ c \end{bmatrix} \times \begin{bmatrix} 6 \\\\ c \\\\ -2 \end{bmatrix} = \begin{bmatrix} 1 \cdot (-2) - c \cdot c \\\\ c \cdot 6 - 3 \cdot (-2) \\\\ 3 \cdot c - 1 \cdot 6 \end{bmatrix} = \begin{bmatrix} -2 - c^2 \\\\ 6c + 6 \\\\ 3c - 6 \end{bmatrix}
$$
</div>

Strictly speaking, this vector, <span class="math-inline">\\(\begin{bmatrix} -2 - c^2 \\\\ 6c + 6 \\\\ 3c - 6 \end{bmatrix}\\)</span>, is a scalar multiple of <span class="math-inline">\\(\begin{bmatrix} a \\\\ 24 \\\\ 3 \end{bmatrix}\\)</span>, but we don't know what the scalar is yet. So, we really should try and solve

<div class="math-display">
$$
\begin{bmatrix} -2 - c^2 \\\\ 6c + 6 \\\\ 3c - 6 \end{bmatrix} = k \begin{bmatrix} a \\\\ 24 \\\\ 3 \end{bmatrix}
$$
</div>

But, notice that <span class="math-inline">\\(6c + 6 = 24 \implies c = 3\\)</span>, and <span class="math-inline">\\(c = 3\\)</span> also satisfies <span class="math-inline">\\(3c - 6 = 3\\)</span>, so the scalar <span class="math-inline">\\(k = 1\\)</span>, and thus <span class="math-inline">\\(\boxed{c = 3}\\)</span>.
</details>

</div>
</div>

</div>

---

## SP26 MT1 · Problem 7 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">10 pts</span>

<p class="worksheet-source">From <a href="/exams/sp26-mt1/">SP26 MT1</a></p>

Suppose <span class="math-inline">\\(\vec v&#95;1,\vec v&#95;2,\vec v&#95;3,\vec v&#95;4\in\mathbb R^n\\)</span> are a **linearly independent** collection of vectors. Define

<div class="math-display">
$$
\vec p=\vec v_1+\vec v_2,\qquad
\vec q=\vec v_2+\vec v_3,\qquad
\vec r=\vec v_3+\vec v_4,\qquad
\vec s=\vec v_4+\vec v_1
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">7 pts</span> Are <span class="math-inline">\\(\lbrace\vec p,\vec q,\vec r,\vec s\rbrace\\)</span> linearly independent?

1.  Select an answer:
<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Yes</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> No</span></div>

{: start="2"}
2.  Prove your answer using the formal definition of linear independence. <em>Hint: You did something similar in Homework 4, Problem 6.</em>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Yes</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> No</span></div>

If <span class="math-inline">\\(\vec p,\vec q,\vec r,\vec s\\)</span> are linearly independent, then the only solution to the equation <span class="math-inline">\\(a \vec p + b \vec q + c \vec r + d \vec s = \vec 0\\)</span> is <span class="math-inline">\\(a = b = c = d = 0\\)</span>.

That's not the case here! Consider the linear combination

<div class="math-display">
$$
\vec p-\vec q+\vec r-\vec s
$$
</div>

 How did I think of this? I noticed that if I start with <span class="math-inline">\\(\vec p\\)</span>, subtracting <span class="math-inline">\\(\vec q\\)</span> gets rid of all <span class="math-inline">\\(\vec v&#95;2\\)</span>'s, but makes <span class="math-inline">\\(\vec v&#95;3\\)</span> negative, so I need a positive <span class="math-inline">\\(\vec r\\)</span> to cancel that out. Then, <span class="math-inline">\\(\vec p - \vec q + \vec r = \vec v&#95;1 + \vec v&#95;4\\)</span>; subtracting <span class="math-inline">\\(\vec s\\)</span> then gets rid of both <span class="math-inline">\\(\vec v&#95;1\\)</span> and <span class="math-inline">\\(\vec v&#95;4\\)</span>, leaving me with <span class="math-inline">\\(\vec 0\\)</span>.

<div class="math-display">
$$
\vec p - \vec q + \vec r - \vec s = (\vec v_1+\vec v_2)-(\vec v_2+\vec v_3)+(\vec v_3+\vec v_4)-(\vec v_4+\vec v_1)=\vec 0
$$
</div>

 The coefficients <span class="math-inline">\\(1,-1,1,-1\\)</span> are not all zero, so this proves that <span class="math-inline">\\(\lbrace\vec p,\vec q,\vec r,\vec s\rbrace\\)</span> is linearly dependent.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> What is the dimension of <span class="math-inline">\\(\text{span}(\lbrace\vec p,\vec q,\vec r,\vec s\rbrace)\\)</span>? Give your answer as a number with no variables.

<span class="math-inline">\\(\dim(\text{span}(\lbrace\vec p,\vec q,\vec r,\vec s\rbrace)) = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>

<details markdown="1"><summary>Solution</summary>

Part **a)** shows that the four vectors are linearly **dependent**, so the dimension of <span class="math-inline">\\(\text{span}(\lbrace\vec p,\vec q,\vec r,\vec s\rbrace)\\)</span> is **at most** <span class="math-inline">\\(3\\)</span>. (For the dimension to be 4, which is the number of vectors in question, they would need to be linearly independent. There's no way to have a span of 5 or more dimensions using just 4 vectors.)

But just because the dimension of <span class="math-inline">\\(\text{span}(\lbrace\vec p,\vec q,\vec r,\vec s\rbrace)\\)</span> is at most <span class="math-inline">\\(3\\)</span> doesn't mean that the dimension is actually <span class="math-inline">\\(3\\)</span> --- for this span to be 3-dimensional, it needs to be the span of 3 linearly independent vectors.

Fortunately, <span class="math-inline">\\(\vec p,\vec q,\vec r\\)</span> are linearly independent. If

<div class="math-display">
$$
a\vec p+b\vec q+c\vec r=\vec 0
$$
</div>

 then

<div class="math-display">
$$
a\vec v_1+(a+b)\vec v_2+(b+c)\vec v_3+c\vec v_4=\vec 0
$$
</div>

 Since <span class="math-inline">\\(\vec v&#95;1,\vec v&#95;2,\vec v&#95;3,\vec v&#95;4\\)</span> are linearly independent, we must have

<div class="math-display">
$$
a=0,\qquad a+b=0,\qquad b+c=0,\qquad c=0
$$
</div>

 This gives <span class="math-inline">\\(a=b=c=0\\)</span>, so <span class="math-inline">\\(\vec p,\vec q,\vec r\\)</span> are linearly independent. Therefore, among <span class="math-inline">\\(\left\lbrace \vec p,\vec q,\vec r,\vec s \right\rbrace\\)</span>, there are 3 linearly independent vectors, and thus

<div class="math-display">
$$
\boxed{\dim(\text{span}(\{\vec p,\vec q,\vec r,\vec s\}))=3}
$$
</div>

</details>

</div>
</div>

</div>

---

## SP26 MT1 · Problem 8 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">8 pts</span>

<p class="worksheet-source">From <a href="/exams/sp26-mt1/">SP26 MT1</a></p>

Suppose <span class="math-inline">\\(S\\)</span> is the subspace of <span class="math-inline">\\(\mathbb R^4\\)</span> defined by

<div class="math-display">
$$
S=\left\{
\begin{bmatrix}x_1\\\\x_2\\\\x_3\\\\x_4\end{bmatrix}\in\mathbb R^4 :
x_1-x_2+x_3-x_4=0
\right\}
$$
</div>

Which of the following sets is a basis for <span class="math-inline">\\(S\\)</span>? **Select all** that apply.

<span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\left\lbrace \begin{bmatrix}1\\\\1\\\\0\\\\0\end{bmatrix}, \begin{bmatrix}0\\\\1\\\\1\\\\0\end{bmatrix}, \begin{bmatrix}0\\\\0\\\\1\\\\1\end{bmatrix} \right\rbrace\\)</span>

<span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\left\lbrace \begin{bmatrix}1\\\\1\\\\0\\\\0\end{bmatrix}, \begin{bmatrix}0\\\\1\\\\1\\\\0\end{bmatrix}, \begin{bmatrix}0\\\\0\\\\1\\\\1\end{bmatrix}, \begin{bmatrix}1\\\\0\\\\0\\\\1\end{bmatrix} \right\rbrace\\)</span>

<span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\left\lbrace \begin{bmatrix}1\\\\0\\\\0\\\\1\end{bmatrix}, \begin{bmatrix}0\\\\1\\\\0\\\\-1\end{bmatrix}, \begin{bmatrix}0\\\\0\\\\1\\\\1\end{bmatrix} \right\rbrace\\)</span>

<span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\left\lbrace \begin{bmatrix}1\\\\0\\\\0\\\\1\end{bmatrix}, \begin{bmatrix}0\\\\1\\\\0\\\\-1\end{bmatrix}, \begin{bmatrix}1\\\\1\\\\0\\\\0\end{bmatrix} \right\rbrace\\)</span>

<details markdown="1"><summary>Solution</summary>

<span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\left\lbrace \begin{bmatrix}1\\\\0\\\\0\\\\1\end{bmatrix}, \begin{bmatrix}0\\\\1\\\\0\\\\-1\end{bmatrix}, \begin{bmatrix}1\\\\1\\\\0\\\\0\end{bmatrix} \right\rbrace\\)</span>

The subspace <span class="math-inline">\\(S\\)</span> has dimension <span class="math-inline">\\(3\\)</span> because the single constraint lets us solve

<div class="math-display">
$$
x_4=x_1-x_2+x_3
$$
</div>

 This means that components 1, 2, and 3 are free to vary, and component 4 is fully determined by those first three components. So, <span class="math-inline">\\(S\\)</span> has three "degrees of freedom", and therefore has dimension <span class="math-inline">\\(3\\)</span>.

So a basis for <span class="math-inline">\\(S\\)</span> is any set of **three linearly independent vectors** that all lie in <span class="math-inline">\\(S\\)</span>.

The first and third choices are bases: in both of those choices, the set has 3 vectors that are linearly independent, and all 3 vectors lie in <span class="math-inline">\\(S\\)</span>.

The second choice has 4 vectors in a 3-dimensional subspace, so it cannot be a basis.

The fourth choice has 3 vectors but they are not linearly independent, since at least one of them can be written as a linear combination of the other two:

<div class="math-display">
$$
\begin{bmatrix}1\\\\1\\\\0\\\\0\end{bmatrix} = \begin{bmatrix}1\\\\0\\\\0\\\\1\end{bmatrix} + \begin{bmatrix}0\\\\1\\\\0\\\\-1\end{bmatrix}
$$
</div>

So, only the first and third choices are bases for <span class="math-inline">\\(S\\)</span>.
</details>

---

## SP26 Final · Problem 4 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">5 pts</span> <span class="badge" data-flag="mt1-redemption" style="background-color: #9A3324; color: #FFFFFF; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">MT1 Redemption</span>

<p class="worksheet-source">From <a href="/exams/sp26-final/">SP26 Final</a></p>

Suppose <span class="math-inline">\\(S = \left\lbrace \begin{bmatrix} x&#95;1 \\\\ x&#95;2 \\\\ x&#95;3 \\\\ x&#95;4 \end{bmatrix} : x&#95;1 + x&#95;2 + 2x&#95;3 = 0 \text{ and } x&#95;3 = x&#95;4 \right\rbrace\\)</span>. State one basis for <span class="math-inline">\\(S\\)</span>. Your answer should be a list of vectors with no variables.

<span class="math-inline">\\(\text{one basis for } S =\\)</span> \_\_\_\_\_\_

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

{% endraw %}
