---
layout: minimal
title: "Chapter 8: Gradients"
description: "Practice problems for Chapter 8: Gradients."
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

# Chapter 8: Gradients

*Topics: gradient vector, gradients + matrix/vector operations, gradient descent, convexity, positive definite matrices*

Problems below are collected from past exams; each links back to its full exam. Solutions are in the dropdowns.

## Problems

- [FA25 MT2 · Problem 6](#fa25-mt2--problem-6-quadratus-formulus-14-pts)
- [FA25 MT2 · Problem 7](#fa25-mt2--problem-7-complexity-10-pts)
- [FA25 Final · Problem 6](#fa25-final--problem-6-4-pts-mt2-redemption)
- [FA25 Final · Problem 7](#fa25-final--problem-7-6-pts-mt2-redemption)
- [WN26 MT2 · Problem 7](#wn26-mt2--problem-7-10-pts)
- [WN26 MT2 · Problem 8](#wn26-mt2--problem-8-11-pts)
- [WN26 Final · Problem 8](#wn26-final--problem-8-9-pts-mt2-redemption)
- [SP26 MT2 · Problem 6](#sp26-mt2--problem-6-12-pts)
- [SP26 MT2 · Problem 7](#sp26-mt2--problem-7-15-pts)
- [SP26 Final · Problem 9](#sp26-final--problem-9-9-pts-mt2-redemption)

---

## FA25 MT2 · Problem 6: Quadratus Formulus <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">14 pts</span>

<p class="worksheet-source">From <a href="/exams/fa25-mt2/">FA25 MT2</a></p>

Let <span class="math-inline">\\(\displaystyle f(\vec x) = \frac{1}{2} \vec x^T S \vec x - \vec b^T \vec x\\)</span>, where <span class="math-inline">\\(S\\)</span> is a symmetric <span class="math-inline">\\(n \times n\\)</span> matrix and <span class="math-inline">\\(\vec b \in \mathbb{R}^n\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Find <span class="math-inline">\\(\nabla f(\vec x)\\)</span>, the gradient of <span class="math-inline">\\(f(\vec x)\\)</span>. Show your work, and <span class="math-inline">\\(\boxed{\text{circle}}\\)</span> your final answer, which should be an expression in terms of <span class="math-inline">\\(\vec x\\)</span>, <span class="math-inline">\\(S\\)</span>, <span class="math-inline">\\(\vec b\\)</span>, and/or constants. <em>Hint: There's no need to re-prove gradient rules from class.</em>

<details markdown="1"><summary>Solution</summary>

<div class="math-display">
$$
\begin{align*}
\nabla f(\vec x) &= \nabla_{\vec x}\left(\frac{1}{2} \vec x^T S \vec x\right) - \nabla_{\vec x}\left(\vec b^T \vec x\right)
\\\\ &= \frac{1}{2}(2S \vec x) - \vec b
\\\\ &= \boxed{S\vec x - \vec b}
\end{align*}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">2 pts</span> True or False: As long as <span class="math-inline">\\(S\\)</span> is invertible, if <span class="math-inline">\\(\nabla f(\vec a) = \vec 0\\)</span>, then <span class="math-inline">\\(\vec a\\)</span> is a global minimum of <span class="math-inline">\\(f(\vec x)\\)</span>.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> False</span></div>

In general, this is **false**. Even if <span class="math-inline">\\(S\\)</span> is invertible, <span class="math-inline">\\(\nabla f(\vec a) = \vec 0\\)</span> could mean that <span class="math-inline">\\(\vec a\\)</span> is at a local maxima, local minima, or saddle point.

For example, let <span class="math-inline">\\(\vec x = \begin{bmatrix} x \\\\ y \end{bmatrix}\\)</span>, <span class="math-inline">\\(\vec b = \begin{bmatrix} 0 \\\\ 0 \end{bmatrix}\\)</span>, and <span class="math-inline">\\(S = \begin{bmatrix} 2 &amp; 0 \\\\ 0 &amp; -2 \end{bmatrix}\\)</span>, which is an invertible matrix. Then,

<div class="math-display">
$$
f(\vec x) = \frac{1}{2} \begin{bmatrix} x & y \end{bmatrix} \begin{bmatrix} 2 & 0 \\\\ 0 & -2 \end{bmatrix} \begin{bmatrix} x \\\\ y \end{bmatrix} - \begin{bmatrix} 0 \\\\ 0 \end{bmatrix} \cdot \begin{bmatrix} x \\\\ y \end{bmatrix} = x^2 - y^2
$$
</div>

but <span class="math-inline">\\(f(\vec x) = x^2 - y^2\\)</span> has no global minimum, since you can make <span class="math-inline">\\(f(\vec x)\\)</span> arbitrarily negative by setting <span class="math-inline">\\(x = 0\\)</span> and <span class="math-inline">\\(y = -\text{large number}\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">2 pts</span> True or False: As long as all of the components of <span class="math-inline">\\(S\\)</span> are positive real numbers, if

<span class="math-inline">\\(\nabla f(\vec a) = \vec 0\\)</span>, then <span class="math-inline">\\(\vec a\\)</span> is a global minimum of <span class="math-inline">\\(f(\vec x)\\)</span>.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> False</span></div>

This is also **false**. Even if all of the components of <span class="math-inline">\\(S\\)</span> are positive real numbers, <span class="math-inline">\\(f(\vec x)\\)</span> may not have a global minimum. As we saw later in the semester, the convexity of <span class="math-inline">\\(f\\)</span> has to do with whether or not <span class="math-inline">\\(S\\)</span> is **positive semidefinite**. But, this was not a concept we knew about on the midterm, so the problem is answerable without that concept.

Instead, the way to think through this is through counterexamples. For example, let <span class="math-inline">\\(\vec x = \begin{bmatrix} x \\\\ y \end{bmatrix}\\)</span>, <span class="math-inline">\\(\vec b = \begin{bmatrix} 1 \\\\ 0 \end{bmatrix}\\)</span>, and <span class="math-inline">\\(S = \begin{bmatrix} 2 &amp; 4 \\\\ 4 &amp; 8 \end{bmatrix}\\)</span>, which is a symmetric matrix with all positive real components. Then,

<div class="math-display">
$$
f(\vec x) = \frac{1}{2} \begin{bmatrix} x & y \end{bmatrix} \begin{bmatrix} 2 & 4 \\\\ 4 & 8 \end{bmatrix} \begin{bmatrix} x \\\\ y \end{bmatrix} - \begin{bmatrix} 1 \\\\ 0 \end{bmatrix} \cdot \begin{bmatrix} x \\\\ y \end{bmatrix} = x^2 + 4xy + 4y^2 - x = (x + 2y)^2 - x
$$
</div>

<span class="math-inline">\\(f(\vec x)\\)</span> has no global minimum, since you can keep decreasing the output by picking a really large positive value of <span class="math-inline">\\(x\\)</span> and set <span class="math-inline">\\(y = -\frac{x}{2}\\)</span>, which makes

<div class="math-display">
$$
f(\vec x) = (x + 2 \cdot -\frac{x}{2})^2 - x = 0 - x = -x
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> We'd like to use gradient descent to minimize <span class="math-inline">\\(f(\vec x)\\)</span>. Suppose <span class="math-inline">\\(S = \begin{bmatrix} 2 &amp; 0 \\\\ 0 &amp; 6 \end{bmatrix}\\)</span>, <span class="math-inline">\\(\vec b = \begin{bmatrix} 1 \\\\ -4 \end{bmatrix}\\)</span>, and we use a learning rate of <span class="math-inline">\\(\alpha = 1\\)</span>. After one iteration of gradient descent, we have <span class="math-inline">\\(\vec x^{(1)} = \begin{bmatrix} - 2 \\\\ -4 \end{bmatrix}\\)</span>. What was our initial guess, <span class="math-inline">\\(\vec x^{(0)}\\)</span>? Show your work, and <span class="math-inline">\\(\boxed{\text{circle}}\\)</span> your final answer, which should be a vector with two entries and no variables.

<details markdown="1"><summary>Solution</summary>

The gradient update rule is <span class="math-inline">\\(\vec x^{(t+1)} = \vec x^{(t)} - \alpha \nabla f(\vec x^{(t)})\\)</span>. Plugging in <span class="math-inline">\\(\alpha = 1\\)</span> and <span class="math-inline">\\(t = 0\\)</span> simplifies our problem to

<div class="math-display">
$$
\begin{align*}
\vec x^{(1)} &= \vec x^{(0)}-\alpha \nabla f(\vec x^{(0)})
\\\\&= \vec x^{(0)}-(S\vec x^{(0)}-\vec b)
\\\\&= \vec x^{(0)}-S\vec x^{(0)}+\vec b
\end{align*}
$$
</div>

Now, all we need to do is substitute our known vector <span class="math-inline">\\(\vec x^{(1)} = \begin{bmatrix} - 2 \\\\ -4 \end{bmatrix}\\)</span> and matrix <span class="math-inline">\\(S\\)</span> into the above equation and solve for <span class="math-inline">\\(\vec x^{(0)}\\)</span>.

<div class="math-display">
$$
\begin{align*}
\\\\\begin{bmatrix} - 2 \\\\ -4 \end{bmatrix}&= \vec x^{(0)}-\begin{bmatrix} 2 & 0 \\\\ 0 & 6 \end{bmatrix}\vec x^{(0)}+\begin{bmatrix} 1 \\\\ -4 \end{bmatrix}
\\\\\begin{bmatrix} - 3 \\\\ 0 \end{bmatrix}&= \vec x^{(0)}-\begin{bmatrix} 2 & 0 \\\\ 0 & 6 \end{bmatrix}\vec x^{(0)}
\\\\\begin{bmatrix} - 3 \\\\ 0 \end{bmatrix}&= \vec x^{(0)}-\begin{bmatrix} 2x^{(0)}_1 \\\\ 6x^{(0)}_2 \end{bmatrix}
\\\\\begin{bmatrix} - 3 \\\\ 0 \end{bmatrix}&= \begin{bmatrix} -x^{(0)}_1 \\\\ -5x^{(0)}_2 \end{bmatrix} \\\\ x^{(0)}_1=3 &, \: x^{(0)}_2 = 0
\end{align*}
$$
</div>

So, our initial guess was

<div class="math-display">
$$
\boxed{\vec x^{(0)}=\begin{bmatrix}3 \\\\ 0 \end{bmatrix}}
$$
</div>

</details>

</div>
</div>

</div>

---

## FA25 MT2 · Problem 7: Complexity <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">10 pts</span>

<p class="worksheet-source">From <a href="/exams/fa25-mt2/">FA25 MT2</a></p>

Suppose <span class="math-inline">\\(f: \mathbb{R} \to \mathbb{R}\\)</span> is a convex function.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Find scalars <span class="math-inline">\\(a\\)</span> and <span class="math-inline">\\(b\\)</span> such that <span class="math-inline">\\(f(3) \leq a f(2) + b f(6)\\)</span>. Show your work and <span class="math-inline">\\(\boxed{\text{circle}}\\)</span> your final answer, which should be a pair of scalars.

<details markdown="1"><summary>Solution</summary>

Recall the definition of convexity (which is relevant, since <span class="math-inline">\\(f\\)</span> is told to us to be convex):

<div class="math-display">
$$
f((1-t) x + ty) \leq (1-t) f(x) + t f(y)
$$
</div>

Matching the right-side of the inequality above to the right-side of the inequality given, we see that <span class="math-inline">\\(a = 1-t\\)</span> and <span class="math-inline">\\(b = t\\)</span>.

So, our job is to find <span class="math-inline">\\(1-t\\)</span> and <span class="math-inline">\\(t\\)</span> such that

<div class="math-display">
$$
3 = (1-t) \cdot 2 + t \cdot 6
$$
</div>

 i.e. <span class="math-inline">\\(\textbf{to write 3 as a linear combination of 2 and 6}\\)</span>.

<div class="math-display">
$$
3 = (1 - t) \cdot 2 + t \cdot 6 = 2 - 2t + 6t = 2 + 4t \implies t = \frac{3 - 2}{4} = \frac{1}{4}
$$
</div>

So, <span class="math-inline">\\(\boxed{a = \frac{3}{4}, b = \frac{1}{4}}\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Using the result from part **a)**, prove that <span class="math-inline">\\(f(3) + f(5) \leq f(2) + f(6)\\)</span>.

<details markdown="1"><summary>Solution</summary>

In part **a)**, we proved

<div class="math-display">
$$
f(3) \leq \frac{3}{4} f(2) + \frac{1}{4} f(6)
$$
</div>

 Since there's an <span class="math-inline">\\(f(5)\\)</span> in the left side of expression we want to prove, we need to find an inequality for <span class="math-inline">\\(f(5)\\)</span> in terms of <span class="math-inline">\\(f(2)\\)</span> and <span class="math-inline">\\(f(6)\\)</span>.

Trying to match the pattern, let <span class="math-inline">\\(t = \frac{3}{4}\\)</span>, and keep <span class="math-inline">\\(x = 2\\)</span> and <span class="math-inline">\\(y = 6\\)</span>. Where did <span class="math-inline">\\(t = \frac{3}{4}\\)</span> come from? You could have found it from solving <span class="math-inline">\\((1-t) \cdot 2 + t \cdot 6 = 5\\)</span>, or by guessing/observing that no other value of <span class="math-inline">\\(t\\)</span> would eventually allow us to add the two inequalities together to get <span class="math-inline">\\(f(2) + f(6)\\)</span> on the right.

<div class="math-display">
$$
\begin{align*}
f((1-t)x + ty) &\leq (1-t)f(x) + t f(y) \\\\
f\left( (1-\frac{3}{4}) \cdot 2 + \frac{3}{4} \cdot 6 \right) &\leq (1-\frac{3}{4}) f(2) + \frac{3}{4} f(6) \\\\
f(5) &\leq \frac{1}{4} f(2) + \frac{3}{4} f(6)
\end{align*}
$$
</div>

Let's add this to our previous inequality.

<div class="math-display">
$$
\begin{align*}
f(3) + f(5) &\leq \frac{3}{4} f(2) + \frac{1}{4} f(6) + \frac{1}{4} f(2) + \frac{3}{4} f(6)
\\\\ f(3) + f(5) &\leq f(2) + f(6)
\end{align*}
$$
</div>

as required!
</details>
</div>
</div>

</div>

---

## FA25 Final · Problem 6 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> <span class="badge" data-flag="mt2-redemption" style="background-color: #9A3324; color: #FFFFFF; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">MT2 Redemption</span>

<p class="worksheet-source">From <a href="/exams/fa25-final/">FA25 Final</a></p>

Suppose <span class="math-inline">\\(A\\)</span> and <span class="math-inline">\\(B\\)</span> are both (not necessarily symmetric!) <span class="math-inline">\\(n \times n\\)</span> matrices. Which of the following is <span class="math-inline">\\(\nabla f(\vec x)\\)</span>, the gradient of

<div class="math-display">
$$
f(\vec x) = (A \vec x)^T (B \vec x)
$$
</div>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(2AB \vec x\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(A^TB \vec x\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(2A^TB \vec x\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(2B^TA \vec x\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\((A^TB + B^TA) \vec x\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\((A^TB - B^TA) \vec x\\)</span></span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(2AB \vec x\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(A^TB \vec x\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(2A^TB \vec x\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(2B^TA \vec x\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\((A^TB + B^TA) \vec x\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\((A^TB - B^TA) \vec x\\)</span></span></div>

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

## FA25 Final · Problem 7 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> <span class="badge" data-flag="mt2-redemption" style="background-color: #9A3324; color: #FFFFFF; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">MT2 Redemption</span>

<p class="worksheet-source">From <a href="/exams/fa25-final/">FA25 Final</a></p>

Consider the function <span class="math-inline">\\(f: \mathbb{R} \to \mathbb{R}\\)</span> graphed below.

<div style="text-align: center;">
<img src="imgs/fa25-final-q07/convexity-scale.png" alt="image" style="width: 60%; max-width: 100%;">
</div>

Note that <span class="math-inline">\\(f\\)</span> is a piecewise linear function, with slopes of <span class="math-inline">\\(0\\)</span>, <span class="math-inline">\\(4\\)</span>, and <span class="math-inline">\\(-4\\)</span>. The slope changes at the following values of <span class="math-inline">\\(x\\)</span>: <span class="math-inline">\\(-6, -5, -2, -1, 1, 2, 5, 6\\)</span>.

Suppose we want to minimize <span class="math-inline">\\(f(x)\\)</span> using gradient descent. There are several values of <span class="math-inline">\\(x\\)</span> such that <span class="math-inline">\\(f\\)</span> is not differentiable at <span class="math-inline">\\(x\\)</span>; if any of our guesses <span class="math-inline">\\(x^{(0)}, x^{(1)}, x^{(2)}, \ldots\\)</span> ever evaluate to one of these values, we say that gradient descent **crashes**.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">2 pts</span> True or False: <span class="math-inline">\\(f(x)\\)</span> is convex on the domain <span class="math-inline">\\(x \in [-9, 9]\\)</span>.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> False</span></div>

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

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1.4\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1.6\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1.8\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1.9\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(2.0\\)</span></span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1.4\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(1.6\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1.8\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1.9\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(2.0\\)</span></span></div>

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

## WN26 MT2 · Problem 7 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">10 pts</span>

<p class="worksheet-source">From <a href="/exams/wn26-mt2/">WN26 MT2</a></p>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Suppose <span class="math-inline">\\(A\\)</span> is a <span class="math-inline">\\(4 \times 4\\)</span> matrix and <span class="math-inline">\\(\vec x \in \mathbb{R}^4\\)</span>. Furthermore, suppose that the gradient of the function <span class="math-inline">\\(f(\vec x) = \vec x^T A \vec x\\)</span> is given by

<div class="math-display">
$$
\nabla f(\vec x) = \begin{bmatrix} 2x_1 \\\\ -15 x_2 \\\\ 10 x_3 \\\\ x_4 \end{bmatrix}
$$
</div>

Find one possible matrix <span class="math-inline">\\(A\\)</span>. Your answer should be a <span class="math-inline">\\(4 \times 4\\)</span> matrix with no variables.

<span class="math-inline">\\(A = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>

<details markdown="1"><summary>Solution</summary>

Recall that for

<div class="math-display">
$$
f(\vec x) = \vec x^T A \vec x,
$$
</div>

 the gradient is

<div class="math-display">
$$
\nabla f(\vec x) = (A + A^T)\vec x
$$
</div>

We want

<div class="math-display">
$$
(A + A^T)\vec x = \begin{bmatrix} 2x_1 \\\\ -15x_2 \\\\ 10x_3 \\\\ x_4 \end{bmatrix}
$$
</div>

 One easy way to make this happen is to choose <span class="math-inline">\\(A\\)</span> to be diagonal and symmetric. Then <span class="math-inline">\\(A + A^T = 2A\\)</span>, so we want

<div class="math-display">
$$
\begin{align*}
2A &= \begin{bmatrix}
2 & 0 & 0 & 0 \\\\
0 & -15 & 0 & 0 \\\\
0 & 0 & 10 & 0 \\\\
0 & 0 & 0 & 1
\end{bmatrix}
\end{align*}
$$
</div>

Thus, one possible choice is

<div class="math-display">
$$
A = \begin{bmatrix}
1 & 0 & 0 & 0 \\\\
0 & -15/2 & 0 & 0 \\\\
0 & 0 & 5 & 0 \\\\
0 & 0 & 0 & 1/2
\end{bmatrix}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Suppose <span class="math-inline">\\(A\\)</span> is an <span class="math-inline">\\(n \times n\\)</span> matrix, <span class="math-inline">\\(\vec b \in \mathbb{R}^n\\)</span>, and that <span class="math-inline">\\(g: \mathbb{R}^n \to \mathbb{R}\\)</span> is defined by

<div class="math-display">
$$
g(\vec x) = (\vec b^T A \vec x)^2
$$
</div>

Which of the following is <span class="math-inline">\\(\nabla g(\vec x)\\)</span>, the gradient of <span class="math-inline">\\(g(\vec x)\\)</span>?

<span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(2 A^T \vec b\\)</span>

<span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\((\vec b^T A \vec x) A^T \vec b\\)</span>

<span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(2 (\vec b^T A \vec x) \vec b\\)</span>

<span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(2 (\vec b^T A \vec x) A^T \vec b\\)</span>

<span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(2 (\vec b^T A \vec x) A^T \vec x\\)</span>

<span class="mc-bubble" aria-hidden="true"></span> None of the above

<details markdown="1"><summary>Solution</summary>

<span class="mc-bubble" aria-hidden="true"></span> None of the above

Let

<div class="math-display">
$$
f(\vec x) = \vec b^T A \vec x = (A^T \vec b)^T \vec x = (A^T \vec b) \cdot \vec x
$$
</div>

 Then

<div class="math-display">
$$
g(\vec x) = (g(\vec x))^2
$$
</div>

The gradient of <span class="math-inline">\\(f(\vec x)\\)</span> can be computed using the dot product "big three" rule, which tells us that

<div class="math-display">
$$
\nabla f(\vec x) = A^T \vec b
$$
</div>

 Applying the chain rule,

<div class="math-display">
$$
\begin{align*}
\nabla g(\vec x) &= 2 f(\vec x) \nabla f(\vec x) \\\\
&= 2 (\vec b^T A \vec x) A^T \vec b
\end{align*}
$$
</div>

</details>

</div>
</div>

</div>

---

## WN26 MT2 · Problem 8 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">11 pts</span>

<p class="worksheet-source">From <a href="/exams/wn26-mt2/">WN26 MT2</a></p>

Let <span class="math-inline">\\(\vec x = \begin{bmatrix} x&#95;1 \\\\ x&#95;2 \end{bmatrix}\\)</span>. Consider the function

<div class="math-display">
$$
f(\vec x) = (x_1 + x_2 - 4)^2
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> Fill in the blanks: The set of all vectors <span class="math-inline">\\(\vec x^{\ast}\\)</span> that minimize <span class="math-inline">\\(f(\vec x)\\)</span> form a \_\_(i)\_\_ in <span class="math-inline">\\(\mathbb{R}^2\\)</span>. This set \_\_(ii)\_\_ a subspace of <span class="math-inline">\\(\mathbb{R}^2\\)</span>.

1.
<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> point</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> line</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> plane</span></div>

2.
<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> is not</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> is</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> is not</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> is</span></div>

We have

<div class="math-display">
$$
f(\vec x) = (x_1 + x_2 - 4)^2
$$
</div>

 so the minimum value is 0, which happens exactly when

<div class="math-display">
$$
x_1 + x_2 - 4 = 0 \iff x_1 + x_2 = 4
$$
</div>

The equation

<div class="math-display">
$$
x_1 + x_2 = 4
$$
</div>

 describes a **line** in <span class="math-inline">\\(\mathbb{R}^2\\)</span>.

This line is **not** a subspace, because it does not pass through the origin. For example,

<div class="math-display">
$$
\begin{bmatrix} 0 \\\\ 0 \end{bmatrix}
$$
</div>

 is not a minimizer. Therefore, this set **is not** a subspace.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">8 pts</span> Suppose we use gradient descent to minimize <span class="math-inline">\\(f(\vec x)\\)</span> using an initial guess of <span class="math-inline">\\(\vec x^{(0)} = \begin{bmatrix} 1 \\\\ 1 \end{bmatrix}\\)</span>.

Find the learning rate/step size <span class="math-inline">\\(\alpha\\)</span> that will cause gradient descent to converge to a global minimum of <span class="math-inline">\\(f(\vec x)\\)</span> **in one iteration**, i.e. such that <span class="math-inline">\\(\vec x^{(1)}\\)</span> is a minimizer of <span class="math-inline">\\(f(\vec x)\\)</span>.

Show your work in the space provided, and write your final answer in the bottom-right corner of the box. Your answer should be a number with no variables.

<div class="math-display">
$$
\alpha = \_\_\_\_\_\_
$$
</div>

<details markdown="1"><summary>Solution</summary>

First, we need to compute the gradient of <span class="math-inline">\\(f(\vec x)\\)</span>:

<div class="math-display">
$$
f(\vec x) = (x_1 + x_2 - 4)^2
\quad \Longrightarrow \quad
\nabla f(\vec x) = \begin{bmatrix}
2(x_1 + x_2 - 4) \\\\
2(x_1 + x_2 - 4)
\end{bmatrix}
$$
</div>

At

<div class="math-display">
$$
\vec x^{(0)} = \begin{bmatrix} 1 \\\\ 1 \end{bmatrix}
$$
</div>

 we have

<div class="math-display">
$$
x_1^{(0)} + x_2^{(0)} - 4 = 1 + 1 - 4 = -2
$$
</div>

 so

<div class="math-display">
$$
\nabla f(\vec x^{(0)}) = \begin{bmatrix} -4 \\\\ -4 \end{bmatrix}
$$
</div>

One gradient descent step gives

<div class="math-display">
$$
\begin{align*}
\vec x^{(1)} &= \vec x^{(0)} - \alpha \nabla f(\vec x^{(0)}) \\\\
&= \begin{bmatrix} 1 \\\\ 1 \end{bmatrix} - \alpha \begin{bmatrix} -4 \\\\ -4 \end{bmatrix} \\\\
&= \begin{bmatrix} 1 + 4\alpha \\\\ 1 + 4\alpha \end{bmatrix}
\end{align*}
$$
</div>

We want <span class="math-inline">\\(\vec x^{(1)}\\)</span> to be a minimizer, so it must satisfy

<div class="math-display">
$$
x_1^{(1)} + x_2^{(1)} = 4
$$
</div>

 That gives

<div class="math-display">
$$
\begin{align*}
(1 + 4\alpha) + (1 + 4\alpha) &= 4 \\\\
2 + 8\alpha &= 4 \\\\
8\alpha &= 2 \\\\
\alpha &= \frac{1}{4}
\end{align*}
$$
</div>

</details>
</div>
</div>

</div>

---

## WN26 Final · Problem 8 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">9 pts</span> <span class="badge" data-flag="mt2-redemption" style="background-color: #9A3324; color: #FFFFFF; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">MT2 Redemption</span>

<p class="worksheet-source">From <a href="/exams/wn26-final/">WN26 Final</a></p>

Consider the function <span class="math-inline">\\(g: \mathbb{R}^3 \to \mathbb{R}\\)</span>. We'd like to minimize <span class="math-inline">\\(g\\)</span> using gradient descent.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(6 pts) Suppose two separate runs of gradient descent are started from **the same initial guess** <span class="math-inline">\\(\vec x^{(0)}\\)</span>, but with different learning rates (step sizes), <span class="math-inline">\\(\alpha\\)</span>.

If <span class="math-inline">\\(\alpha = 1/2\\)</span>, then <span class="math-inline">\\(\vec x^{(1)} = \begin{bmatrix} 1 \\\\ 1 \\\\ 1 \end{bmatrix}\\)</span>, and if <span class="math-inline">\\(\alpha = 1/4\\)</span>, then <span class="math-inline">\\(\vec x^{(1)} = \begin{bmatrix} 2 \\\\ 3 \\\\ 2 \end{bmatrix}\\)</span>.

Find <span class="math-inline">\\(\nabla g(\vec x^{(0)})\\)</span>, the gradient of <span class="math-inline">\\(g\\)</span> at <span class="math-inline">\\(\vec x^{(0)}\\)</span>. Show your work, and write your final answer in the box provided. Your answer should be a vector with no variables.

<div class="math-display">
$$
\nabla g(\vec x^{(0)}) = \_\_\_\_\_\_
$$
</div>

<details markdown="1"><summary>Solution</summary>

Let <span class="math-inline">\\(\vec d = \nabla g(\vec x^{(0)})\\)</span>. The gradient descent update rule is

<div class="math-display">
$$
\vec x^{(1)} = \vec x^{(0)} - \alpha \nabla g(\vec x^{(0)})
$$
</div>

 The two runs give

<div class="math-display">
$$
\begin{bmatrix}
1\\\\
1\\\\
1
\end{bmatrix}
=
\vec x^{(0)} - \frac{1}{2}\nabla g(\vec x^{(0)})
$$
</div>

 and

<div class="math-display">
$$
\begin{bmatrix}
2\\\\
3\\\\
2
\end{bmatrix}
=
\vec x^{(0)} - \frac{1}{4}\nabla g(\vec x^{(0)})
$$
</div>

 Subtracting the second equation from the first eliminates <span class="math-inline">\\(\vec x^{(0)}\\)</span>:

<div class="math-display">
$$
\begin{bmatrix}
-1\\\\
-2\\\\
-1
\end{bmatrix}
=
-\frac{1}{4}\nabla g(\vec x^{(0)})
$$
</div>

 So

<div class="math-display">
$$
\nabla g(\vec x^{(0)}) =
\boxed{
\begin{bmatrix}
4\\\\
8\\\\
4
\end{bmatrix}}
$$
</div>

</details>

Now let <span class="math-inline">\\(\vec x = \begin{bmatrix} x&#95;1 \\\\ x&#95;2 \end{bmatrix}\\)</span>, and consider the function <span class="math-inline">\\(f: \mathbb{R}^2 \to \mathbb{R}\\)</span> defined by

<div class="math-display">
$$
f(\vec x) = (x_1 + 2x_2 - 6)^2 + \lVert \vec x \rVert^2
$$
</div>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> Suppose

<div class="math-display">
$$
\nabla f(\vec x)
=
M
\begin{bmatrix}
x_1\\\\
x_2\\\\
1
\end{bmatrix}
$$
</div>

for some <span class="math-inline">\\(2 \times 3\\)</span> matrix <span class="math-inline">\\(M\\)</span>. Which of the following matrices is <span class="math-inline">\\(M\\)</span>?

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} 2 &amp; 2 &amp; -6 \\\\ 2 &amp; 5 &amp; -12 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} 4 &amp; 2 &amp; -12 \\\\ 2 &amp; 10 &amp; -24 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} 4 &amp; 4 &amp; -12 \\\\ 4 &amp; 10 &amp; -24 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} 4 &amp; 4 &amp; 12 \\\\ 4 &amp; 10 &amp; 24 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} 4 &amp; 4 &amp; -12 \\\\ 2 &amp; 6 &amp; -12 \end{bmatrix}\\)</span></span></div>

<details markdown="1"><summary>Solution</summary>

<span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} 4 &amp; 4 &amp; -12 \\\\ 2 &amp; 6 &amp; -12 \end{bmatrix}\\)</span>

We have

<div class="math-display">
$$
f(\vec x) = (x_1 + 2x_2 - 6)^2 + \lVert \vec x \rVert^2
$$
</div>

Using the chain rule,

<div class="math-display">
$$
\nabla f(\vec x)
=
2(x_1+2x_2-6)
\begin{bmatrix}
1\\\\
2
\end{bmatrix}
+
2\vec x
$$
</div>

We applied the chain rule above by writing <span class="math-inline">\\(\left( x&#95;1 + 2x&#95;2 - 6 \right)^2 = (\begin{bmatrix} 1 \\\\ 2 \end{bmatrix} \cdot \vec x - 6)^2\\)</span>. If this feels foreign, we can instead take partial derivatives with respect to <span class="math-inline">\\(x&#95;1\\)</span> and <span class="math-inline">\\(x&#95;2\\)</span> separately.

<div class="math-display">
$$
\frac{\partial f}{\partial x_1} = 2(x_1 + 2x_2 - 6) \cdot 1 + 2x_1 = 4x_1 + 4x_2 - 12
$$
</div>



<div class="math-display">
$$
\frac{\partial f}{\partial x_2} = 2(x_1 + 2x_2 - 6) \cdot 2 + 2x_2 = 4x_1 + 10x_2 - 24
$$
</div>

Either way, <span class="math-inline">\\(\nabla f(\vec x)\\)</span> simplifies to

<div class="math-display">
$$
\nabla f(\vec x)
=
\begin{bmatrix}
2(x_1+2x_2-6)+2x_1\\\\
4(x_1+2x_2-6)+2x_2
\end{bmatrix}
=
\begin{bmatrix}
4x_1+4x_2-12\\\\
4x_1+10x_2-24
\end{bmatrix}
=
\begin{bmatrix}
4 & 4 & -12\\\\
4 & 10 & -24
\end{bmatrix}
\begin{bmatrix}
x_1 \\\\ x_2 \\\\ 1
\end{bmatrix}
$$
</div>

 So,

<div class="math-display">
$$
M =
\boxed{
\begin{bmatrix}
4 & 4 & -12\\\\
4 & 10 & -24
\end{bmatrix}}
$$
</div>

</details>

</div>
</div>

</div>

---

## SP26 MT2 · Problem 6 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>

<p class="worksheet-source">From <a href="/exams/sp26-mt2/">SP26 MT2</a></p>

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

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> False</span></div>

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
$$
\nabla f(\vec x) = \_\_\_\_\_\_
$$
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

## SP26 MT2 · Problem 7 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">15 pts</span>

<p class="worksheet-source">From <a href="/exams/sp26-mt2/">SP26 MT2</a></p>

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
$$
\alpha = \_\_\_\_\_\_
$$
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
$$
d = \_\_\_\_\_\_
$$
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
</div>
</div>

</div>

---

## SP26 Final · Problem 9 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">9 pts</span> <span class="badge" data-flag="mt2-redemption" style="background-color: #9A3324; color: #FFFFFF; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">MT2 Redemption</span>

<p class="worksheet-source">From <a href="/exams/sp26-final/">SP26 Final</a></p>

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
\vec x^{(1)} = \_\_\_\_\_\_
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
<img src="imgs/sp26-final-q09/convexity-counterexample.png" alt="image" style="width: 82%; max-width: 100%;">
</div>
</details>

</div>
</div>

</div>

---

{% endraw %}
