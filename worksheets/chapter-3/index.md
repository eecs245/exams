---
layout: minimal
title: "Chapter 3: Vectors"
description: "Practice problems for Chapter 3: Vectors."
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

# Chapter 3: Vectors

*Topics: vectors and linear combinations, norms, dot product, projecting onto a single vector*

*Problems below are collected from past exams; each links back to its full exam. Solutions are in the dropdowns.*

## Problems

- [FA25 MT1 · Problem 4](#fa25-mt1--problem-4-mission-impossible-12-pts)
- [FA25 MT1 · Problem 8](#fa25-mt1--problem-8-worst-case-scenario-8-pts)
- [FA25 Final · Problem 3](#fa25-final--problem-3-16-pts-mt1-redemption)
- [WN26 MT1 · Problem 4](#wn26-mt1--problem-4-12-pts)
- [WN26 Final · Problem 3](#wn26-final--problem-3-9-pts-mt1-redemption)
- [SP26 MT1 · Problem 4](#sp26-mt1--problem-4-8-pts)
- [SP26 MT1 · Problem 5](#sp26-mt1--problem-5-13-pts)
- [SP26 MT1 · Problem 9](#sp26-mt1--problem-9-10-pts)
- [SP26 Final · Problem 3](#sp26-final--problem-3-10-pts-mt1-redemption)

---

## FA25 MT1 · Problem 4: Mission Impossible <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>

<p class="worksheet-source">From <a href="/exams/fa25-mt1/">FA25 MT1</a></p>


<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Suppose <span class="math-inline">\\(\vec u, \vec v \in \mathbb{R}^n\\)</span> are **non-zero** vectors, and suppose that

<div class="math-display">
$$
| \vec u \cdot \vec v | = \lVert \vec u \rVert \lVert \vec v \rVert
$$
</div>

For each statement below, determine whether it is impossible, possible, or guaranteed to be true, given the above assumptions. **Select exactly one option from each row**. The first statement has been done for you as an example.

|  | **statement** | **impossible?** | **possible?** | **guaranteed?** |
|:--:|:---|:--:|:--:|:--:|
| <span class="math-inline">\\(i\\)</span> | <span class="math-inline">\\(\lVert \vec u \rVert = 5\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> |
| <span class="math-inline">\\(ii\\)</span> | <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> are orthogonal | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> |
| <span class="math-inline">\\(iii\\)</span> | <span class="math-inline">\\(\lVert \vec u - \vec v \rVert = 0\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> |
| <span class="math-inline">\\(iv\\)</span> | <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> span a 1-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^n\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> |
| <span class="math-inline">\\(v\\)</span> | <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> span a 2-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^n\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> |
| <span class="math-inline">\\(vi\\)</span> | <span class="math-inline">\\(\lVert \vec u + \vec v \rVert = \lVert \vec u \rVert + \lVert \vec v \rVert\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> |

<details markdown="1"><summary>Solution</summary>

Remember that for **any** two vectors <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span>,

<div class="math-display">
$$
\vec u \cdot \vec v = \lVert \vec u \rVert \lVert \vec v \rVert \cos \theta
$$
</div>

The fact that we're told that

<div class="math-display">
$$
| \vec u \cdot \vec v | = \lVert \vec u \rVert \lVert \vec v \rVert
$$
</div>

tells us that <span class="math-inline">\\(\cos \theta = 1\\)</span> or <span class="math-inline">\\(\cos \theta = -1\\)</span>, which means that the angle between <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> is <span class="math-inline">\\(0^\circ\\)</span> or <span class="math-inline">\\(180^\circ\\)</span>, which means that <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> are scalar multiples of each other. (They may point in the same or opposite directions.) This is the key insight to assessing each of the statements.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Suppose <span class="math-inline">\\(\vec w, \vec z \in \mathbb{R}^n\\)</span>. Given that <span class="math-inline">\\(\lVert \vec w \rVert = \lVert \vec z \rVert = \lVert \vec w - \vec z \rVert = 1\\)</span>, find <span class="math-inline">\\(\lVert \vec w + \vec z \rVert\\)</span>. Show your work, and <span class="math-inline">\\(\boxed{\text{circle}}\\)</span> your final answer, which should be a number with no variables.

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(\lVert \vec w + \vec z \rVert = \sqrt{3}\\)</span>.

We're asked to find <span class="math-inline">\\(\lVert \vec w + \vec z \rVert\\)</span>. To do so, let's expand out <span class="math-inline">\\(\lVert \vec w + \vec z \rVert^2\\)</span> as we've done in the past, and see how to utilize what we were given.

<div class="math-display">
$$
\begin{align*}
\lVert \vec w + \vec z \rVert^2 &= (\vec w + \vec z) \cdot (\vec w + \vec z) \\\\
&= \vec w \cdot \vec w + 2 \vec w \cdot \vec z + \vec z \cdot \vec z \\\\
&= \lVert \vec w \rVert^2 + 2 \vec w \cdot \vec z + \lVert \vec z \rVert^2 \\\\
&= 1 + 2 \vec w \cdot \vec z + 1 \\\\
&= 2 + 2 \vec w \cdot \vec z
\end{align*}
$$
</div>

Above, we've plugged in <span class="math-inline">\\(\lVert \vec w \rVert^2 = 1\\)</span> and <span class="math-inline">\\(\lVert \vec z \rVert^2 = 1\\)</span>. We need to know <span class="math-inline">\\(\vec w \cdot \vec z\\)</span>, which we don't yet know.

But, we have enough information to find it, if we expand out <span class="math-inline">\\(\lVert \vec w - \vec z \rVert^2\\)</span>, which we were told is equal to 1.

<div class="math-display">
$$
\begin{align*}
\lVert \vec w - \vec z \rVert^2 &= (\vec w - \vec z) \cdot (\vec w - \vec z) \\\\
1 &= \vec w \cdot \vec w - 2 \vec w \cdot \vec z + \vec z \cdot \vec z \\\\
1 &= \lVert \vec w \rVert^2 - 2 \vec w \cdot \vec z + \lVert \vec z \rVert^2 \\\\
1 &= 1 - 2 \vec w \cdot \vec z + 1 \\\\
1 &= 2 - 2 \vec w \cdot \vec z
\end{align*}
$$
</div>

Solving the above gives us <span class="math-inline">\\(\vec w \cdot \vec z = \frac{1}{2}\\)</span>. This gives

<div class="math-display">
$$
\lVert \vec w + \vec z \rVert^2 = 2 + 2 \vec w \cdot \vec z = 2 + 2 \cdot \frac{1}{2} = 3
$$
</div>

And so,

<div class="math-display">
$$
\lVert \vec w + \vec z \rVert = \sqrt{3}
$$
</div>

</details>

</div>
</div>

</div>


---

## FA25 MT1 · Problem 8: Worst-Case Scenario <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">8 pts</span>

<p class="worksheet-source">From <a href="/exams/fa25-mt1/">FA25 MT1</a></p>


Suppose <span class="math-inline">\\(a, b, c, d, e\\)</span> are positive real numbers. Find the **largest** real number <span class="math-inline">\\(T\\)</span> such that it's guaranteed that

<div class="math-display">
$$
(a + b + c + d + e) \left( \frac{1}{a} + \frac{1}{b} + \frac{1}{c} + \frac{1}{d} + \frac{1}{e} \right) \geq T
$$
</div>

Think of <span class="math-inline">\\(T\\)</span> as the "best possible lower bound". For instance, we know that the expression on the left-hand side above must be greater than or equal to 0, since <span class="math-inline">\\(a, b, c, d, e\\)</span> are all positive, but <span class="math-inline">\\(T = 0\\)</span> is not the answer, since there's a larger value of <span class="math-inline">\\(T\\)</span> that also guarantees the inequality holds.

Show your work, and <span class="math-inline">\\(\boxed{\text{circle}}\\)</span> your final answer, which should be a number with no variables.

<em>Hint: Use the Cauchy-Schwarz inequality.</em>

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(T = 25\\)</span>.

Recall, the Cauchy-Schwarz inequality states that for any two vectors <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span>,

<div class="math-display">
$$
|\vec u \cdot \vec v| \leq \lVert \vec u \rVert \lVert \vec v \rVert
$$
</div>

Let's define two vectors <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> and then apply the Cauchy-Schwarz inequality to them.

<div class="math-display">
$$
\vec u = \begin{bmatrix} \sqrt{a} \\\\ \sqrt{b} \\\\ \sqrt{c} \\\\ \sqrt{d} \\\\ \sqrt{e} \end{bmatrix}, \quad \vec v = \begin{bmatrix} \frac{1}{\sqrt{a}} \\\\ \frac{1}{\sqrt{b}} \\\\ \frac{1}{\sqrt{c}} \\\\ \frac{1}{\sqrt{d}} \\\\ \frac{1}{\sqrt{e}} \end{bmatrix}
$$
</div>

Let's compute the three quantities involved in the inequality.

-   <span class="math-inline">\\(\lVert \vec u \rVert = \sqrt{a + b + c + d + e}\\)</span>

-   <span class="math-inline">\\(\lVert \vec v \rVert = \sqrt{\frac{1}{a} + \frac{1}{b} + \frac{1}{c} + \frac{1}{d} + \frac{1}{e}}\\)</span>

-   <span class="math-inline">\\(|\vec u \cdot \vec v| = |\sqrt{a} \cdot \frac{1}{\sqrt{a}} + \sqrt{b} \cdot \frac{1}{\sqrt{b}} + \sqrt{c} \cdot \frac{1}{\sqrt{c}} + \sqrt{d} \cdot \frac{1}{\sqrt{d}} + \sqrt{e} \cdot \frac{1}{\sqrt{e}}| = 5\\)</span>

So, we have that

<div class="math-display">
$$
5 \leq \sqrt{a + b + c + d + e} \cdot \sqrt{\frac{1}{a} + \frac{1}{b} + \frac{1}{c} + \frac{1}{d} + \frac{1}{e}}
$$
</div>

Squaring both sides of the inequality gives us

<div class="math-display">
$$
25 \leq (a + b + c + d + e) \left( \frac{1}{a} + \frac{1}{b} + \frac{1}{c} + \frac{1}{d} + \frac{1}{e} \right)
$$
</div>

This means that for any positive values of <span class="math-inline">\\(a, b, c, d, e\\)</span>, it's impossible for <span class="math-inline">\\((a + b + c + d + e) \left( \frac{1}{a} + \frac{1}{b} + \frac{1}{c} + \frac{1}{d} + \frac{1}{e} \right)\\)</span> to be less than 25. Finding a value equal to 25 is doable if we set <span class="math-inline">\\(a = b = c = d = e = 1\\)</span>. So, <span class="math-inline">\\(T = 25\\)</span> is the largest possible value of <span class="math-inline">\\(T\\)</span> that guarantees the inequality holds.
</details>

---

## FA25 Final · Problem 3 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">16 pts</span> <span class="badge" data-flag="mt1-redemption" style="background-color: #9A3324; color: #FFFFFF; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">MT1 Redemption</span>

<p class="worksheet-source">From <a href="/exams/fa25-final/">FA25 Final</a></p>


Consider the vectors <span class="math-inline">\\(\vec u = \begin{bmatrix} 3 \\\\ 3 \\\\ 6 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec v = \begin{bmatrix} 1 \\\\ 0 \\\\ c \end{bmatrix}\\)</span>, where <span class="math-inline">\\(c \in \mathbb{R}\\)</span> is some constant.

In parts **a)** and **b)**, if there are multiple possible values of <span class="math-inline">\\(c\\)</span>, give just one.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> Suppose <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> are orthogonal. Find <span class="math-inline">\\(c\\)</span>. Give your answer as a number with no variables.

<span class="math-inline">\\(c = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>

<details markdown="1"><summary>Solution</summary>

Since <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> are orthogonal, their dot product is 0.

<div class="math-display">
$$
\begin{bmatrix} 3 \\\\ 3 \\\\ 6 \end{bmatrix} \cdot \begin{bmatrix} 1 \\\\ 0 \\\\ c \end{bmatrix} = 0
$$
</div>



<div class="math-display">
$$
3 + 0 + 6c = 0
$$
</div>



<div class="math-display">
$$
6c = -3
$$
</div>



<div class="math-display">
$$
c = -1/2
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> Suppose <span class="math-inline">\\(\lVert \vec v \rVert = 4\\)</span>. Find <span class="math-inline">\\(c\\)</span>. Give your answer as a number with no variables.

<span class="math-inline">\\(c = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>

<details markdown="1"><summary>Solution</summary>

Since <span class="math-inline">\\(\lVert \vec v \rVert = 4\\)</span>, we have

<div class="math-display">
$$
\sqrt{1^2 + 0^2 + c^2} = 4
$$
</div>



<div class="math-display">
$$
1 + c^2 = 16
$$
</div>



<div class="math-display">
$$
c^2 = 15
$$
</div>



<div class="math-display">
$$
c = \sqrt{15}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Suppose the projection of <span class="math-inline">\\(\vec v\\)</span> onto <span class="math-inline">\\(\vec u\\)</span> is <span class="math-inline">\\(\begin{bmatrix} 1.5 \\\\ 1.5 \\\\ 3 \end{bmatrix}\\)</span>. What is the value of <span class="math-inline">\\(c\\)</span>? Select one of the answers below, then justify your answer in the box provided.

1.  Answer:
<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1/2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(3/2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(4\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(6\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(6 + \sqrt{41}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(27\\)</span></span></div>

2.  Justify your answer in the box below.

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1/2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(3/2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(2\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(4\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(6\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(6 + \sqrt{41}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(27\\)</span></span></div>

The projection of <span class="math-inline">\\(\vec v\\)</span> onto <span class="math-inline">\\(\vec u\\)</span> is given by

<div class="math-display">
$$
\vec p = \frac{\vec v \cdot \vec u}{\vec u \cdot \vec u} \vec u
$$
</div>

Since we're told that <span class="math-inline">\\(\vec p = \begin{bmatrix} 1.5 \\\\ 1.5 \\\\ 3 \end{bmatrix}\\)</span>, this means that <span class="math-inline">\\(p = \frac{1}{2} \begin{bmatrix} 3 \\\\ 3 \\\\ 6 \end{bmatrix} = \frac{1}{2} \vec u\\)</span>. So,

<div class="math-display">
$$
\frac{\vec v \cdot \vec u}{\vec u \cdot \vec u} = \frac{1}{2}
$$
</div>

Substituting in <span class="math-inline">\\(\vec v = \begin{bmatrix} 1 \\\\ 0 \\\\ c \end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec u = \begin{bmatrix} 3 \\\\ 3 \\\\ 6 \end{bmatrix}\\)</span> gives us

<div class="math-display">
$$
\frac{1 \cdot 3 + 0 \cdot 3 + c \cdot 6}{3^2 + 3^2 + 6^2} = \frac{1}{2} \implies \frac{3 + 6c}{54} = \frac{1}{2} \implies 3 + 6c = 27 \implies \boxed{c = 4}
$$
</div>

</details>

Recall from the previous page that <span class="math-inline">\\(\vec u = \begin{bmatrix} 3 \\\\ 3 \\\\ 6 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec v = \begin{bmatrix} 1 \\\\ 0 \\\\ c \end{bmatrix}\\)</span>, where <span class="math-inline">\\(c \in \mathbb{R}\\)</span> is some constant.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Suppose <span class="math-inline">\\(\text{span}(\lbrace\vec u, \vec v\rbrace)\\)</span> is the plane <span class="math-inline">\\(2x + 4y - 3z = 0\\)</span>. Find <span class="math-inline">\\(c\\)</span>. Show your work, and <span class="math-inline">\\(\boxed{\text{circle}}\\)</span> your final answer, which should be a number with no variables. <em>Hint: While you could compute the cross product, there is no need to --- there is a much quicker solution.</em>

<details markdown="1"><summary>Solution</summary>

One way to find the equation of the plane <span class="math-inline">\\(ax + by + cz = 0\\)</span> spanned by <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> in <span class="math-inline">\\(\mathbb{R}^3\\)</span> is to take the cross product of the two vectors, and setting <span class="math-inline">\\(a\\)</span> to the first component of the cross product, <span class="math-inline">\\(b\\)</span> to the second component, and <span class="math-inline">\\(c\\)</span> to the third component. We could compute the cross product in terms of <span class="math-inline">\\(c\\)</span>, and solve for where it is equal to <span class="math-inline">\\(\begin{bmatrix} 2 \\\\ 4 \\\\ -3 \end{bmatrix}\\)</span>.

But this is overly complicated, and there's an easier solution: if this plane is spanned by <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span>, then <span class="math-inline">\\(\vec v\\)</span> needs to satisfy the equation of the plane, which is <span class="math-inline">\\(2x + 4y - 3z = 0\\)</span>.

Substituting in <span class="math-inline">\\(\vec v = \begin{bmatrix} 1 \\\\ 0 \\\\ c \end{bmatrix}\\)</span> gives us

<div class="math-display">
$$
2 \cdot 1 + 4 \cdot 0 - 3 \cdot c = 0 \implies 2 - 3c = 0 \implies \boxed{c = 2/3}
$$
</div>

</details>

</div>
</div>

</div>


---

## WN26 MT1 · Problem 4 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>

<p class="worksheet-source">From <a href="/exams/wn26-mt1/">WN26 MT1</a></p>


Suppose <span class="math-inline">\\(\vec u = \begin{bmatrix} 1 \\\\ 0 \\\\ 0 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec u + \vec v + \vec w = \begin{bmatrix} 4 \\\\ 0 \\\\ 0 \end{bmatrix}\\)</span>. Assume that none of <span class="math-inline">\\(\vec u\\)</span>, <span class="math-inline">\\(\vec v\\)</span>, or <span class="math-inline">\\(\vec w\\)</span> are the zero vector, <span class="math-inline">\\(\vec 0\\)</span>.

For each statement below, identify whether it is **impossible**, **possible**, or **guaranteed**, and provide a brief explanation in the box provided.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span>
<span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> are orthogonal.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Impossible</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Possible</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Guaranteed</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Impossible</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> Possible</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Guaranteed</span></div>

This is possible.

There is nothing stopping <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> from being orthogonal. For example, let <span class="math-inline">\\(\vec v = \begin{bmatrix} 0 \\\\ 1 \\\\ 0 \end{bmatrix}\\)</span>. Then, <span class="math-inline">\\(\vec u \cdot \vec v = 0 \cdot 0 + 0 \cdot 1 + 0 \cdot 0 = 0\\)</span>, so <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> are orthogonal, and we can still find a <span class="math-inline">\\(\vec w\\)</span> such that <span class="math-inline">\\(\vec u + \vec v + \vec w = \begin{bmatrix} 4 \\\\ 0 \\\\ 0 \end{bmatrix}\\)</span>. For example, let <span class="math-inline">\\(\vec w = \begin{bmatrix} 4 \\\\ 0 \\\\ 0 \end{bmatrix} - \vec u - \vec v = \begin{bmatrix} 3 \\\\ -1 \\\\ 0 \end{bmatrix}\\)</span>.

However, it's not guaranteed: <span class="math-inline">\\(\vec v = \begin{bmatrix} 2 \\\\ 0 \\\\ 0 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec w = \begin{bmatrix} 1 \\\\ 0 \\\\ 0 \end{bmatrix}\\)</span> satisfy <span class="math-inline">\\(\vec u + \vec v + \vec w = \begin{bmatrix} 4 \\\\ 0 \\\\ 0 \end{bmatrix}\\)</span>, but <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> are not orthogonal.

So, it is possible for <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> to be orthogonal.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> The set <span class="math-inline">\\(\lbrace\vec u, \vec v, \vec w\rbrace\\)</span> is linearly dependent.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Impossible</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Possible</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Guaranteed</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Impossible</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Possible</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> Guaranteed</span></div>

This is guaranteed.

<div class="math-display">
$$
\vec u + \vec v + \vec w = \begin{bmatrix} 4 \\\\ 0 \\\\ 0 \end{bmatrix}
$$
</div>

Since <span class="math-inline">\\(\vec u = \begin{bmatrix} 1 \\\\ 0 \\\\ 0 \end{bmatrix}\\)</span>, we can subtract <span class="math-inline">\\(4 \vec u\\)</span> from both sides to get

<div class="math-display">
$$
\vec u + \vec v + \vec w - 4 \vec u = \vec w - 3 \vec u = \begin{bmatrix} 4 \\\\ 0 \\\\ 0 \end{bmatrix} - 4 \begin{bmatrix} 1 \\\\ 0 \\\\ 0 \end{bmatrix}
$$
</div>

Or, equivalently,

<div class="math-display">
$$
- 3 \vec u + \vec v + \vec w = \vec 0
$$
</div>

This is a non-trivial linear combination of <span class="math-inline">\\(\vec u\\)</span>, <span class="math-inline">\\(\vec v\\)</span>, and <span class="math-inline">\\(\vec w\\)</span> that equals the zero vector, so the set <span class="math-inline">\\(\lbrace\vec u, \vec v, \vec w\rbrace\\)</span> is linearly dependent. Equivalently, we could say <span class="math-inline">\\(\vec w = 3 \vec u - \vec v\\)</span>, which means <span class="math-inline">\\(\vec w\\)</span> is a linear combination of <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span>, which also means the set is linearly dependent.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span>
<span class="math-inline">\\(\vec u\\)</span>, <span class="math-inline">\\(\vec v\\)</span>, and <span class="math-inline">\\(\vec w\\)</span> all have the same norm (length).

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Impossible</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Possible</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Guaranteed</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> Impossible</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Possible</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Guaranteed</span></div>

This is impossible.

Recall that the triangle inequality states that for any two vectors <span class="math-inline">\\(\vec v\\)</span> and <span class="math-inline">\\(\vec w\\)</span>,

<div class="math-display">
$$
\lVert \vec v + \vec w \rVert \leq \lVert \vec v \rVert + \lVert \vec w \rVert
$$
</div>

We know that <span class="math-inline">\\(\lVert \vec u \rVert = 1\\)</span>, so in order for the statement to be possible, we'd need both <span class="math-inline">\\(\lVert \vec v \rVert = 1\\)</span> and <span class="math-inline">\\(\lVert \vec w \rVert = 1\\)</span>. But, <span class="math-inline">\\(\vec v + \vec w = \begin{bmatrix} 3 \\\\ 0 \\\\ 0 \end{bmatrix}\\)</span>, so <span class="math-inline">\\(\lVert \vec v + \vec w \rVert = \sqrt{3^2 + 0^2 + 0^2} = \sqrt{9} = 3\\)</span>. In the triangle inequality, this would mean

<div class="math-display">
$$
\lVert \vec v + \vec w \rVert \leq \lVert \vec v \rVert + \lVert \vec w \rVert \implies 3 \leq 2
$$
</div>

This is a contradiction, so it is impossible for both <span class="math-inline">\\(\vec v\\)</span> and <span class="math-inline">\\(\vec w\\)</span> to have a norm of 1, and therefore impossible for all three vectors to have the same norm.
</details>

</div>
</div>

</div>


---

## WN26 Final · Problem 3 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">9 pts</span> <span class="badge" data-flag="mt1-redemption" style="background-color: #9A3324; color: #FFFFFF; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">MT1 Redemption</span>

<p class="worksheet-source">From <a href="/exams/wn26-final/">WN26 Final</a></p>


<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">5 pts</span> Suppose <span class="math-inline">\\(\vec a = \begin{bmatrix} 0 \\\\ 3 \\\\ 6 \end{bmatrix}\\)</span> and that <span class="math-inline">\\(\vec b\\)</span> is another vector in <span class="math-inline">\\(\mathbb{R}^3\\)</span> such that:

-   <span class="math-inline">\\(\vec a\\)</span> and <span class="math-inline">\\(\vec b\\)</span> are orthogonal, and

-   the plane spanned by <span class="math-inline">\\(\vec a\\)</span> and <span class="math-inline">\\(\vec b\\)</span> is

<div class="math-display">
$$
4x - 2y + z = 0
$$
</div>

There are infinitely many possible vectors <span class="math-inline">\\(\vec b\\)</span> that satisfy the given conditions. State **one** of them. Show your work, and write your final answer in the box provided. Your answer should be a vector with no variables.

<div class="math-display">
$$
\text{one possible }\vec b = \_\_\_\_\_\_
$$
</div>

<details markdown="1"><summary>Solution</summary>

Let <span class="math-inline">\\(\vec b = \begin{bmatrix} x \\\\ y \\\\ z \end{bmatrix}\\)</span>.

Since <span class="math-inline">\\(\vec b\\)</span> lies in the given plane,

<div class="math-display">
$$
4x-2y+z=0
$$
</div>

 Since <span class="math-inline">\\(\vec a\\)</span> and <span class="math-inline">\\(\vec b\\)</span> are orthogonal,

<div class="math-display">
$$
\vec a \cdot \vec b = 3y+6z=0
$$
</div>

 The second equation gives <span class="math-inline">\\(y=-2z\\)</span>. Plugging this into the first equation gives

<div class="math-display">
$$
4x+4z+z=0
\implies
x=-\frac{5}{4}z
$$
</div>

 There are infinitely many solutions for <span class="math-inline">\\(x\\)</span>, <span class="math-inline">\\(y\\)</span>, and <span class="math-inline">\\(z\\)</span>; they all lie on a line. To state one, let's just fix a value of <span class="math-inline">\\(z\\)</span>. Arbitrarily choosing <span class="math-inline">\\(z = 4\\)</span> gives

<div class="math-display">
$$
\vec b = \boxed{\begin{bmatrix}-5\\\\-8\\\\4\end{bmatrix}}
$$
</div>

Here's another solution: really, the question is asking for a vector that is orthogonal to both <span class="math-inline">\\(\vec a\\)</span> and <span class="math-inline">\\(\begin{bmatrix} 4 \\\\ -2 \\\\ 1 \end{bmatrix}\\)</span>. Such a vector would be orthogonal to <span class="math-inline">\\(\vec a\\)</span> and would lie in the plane <span class="math-inline">\\(4x-2y+z=0\\)</span>. So, all we need to do is take the cross product of <span class="math-inline">\\(\vec a\\)</span> and <span class="math-inline">\\(\begin{bmatrix} 4 \\\\ -2 \\\\ 1 \end{bmatrix}\\)</span>.

<div class="math-display">
$$
\underbrace{\begin{bmatrix} 0 \\\\ 3 \\\\ 6 \end{bmatrix}}_{\vec a} \times \begin{bmatrix} 4 \\\\ -2 \\\\ 1 \end{bmatrix} = \begin{bmatrix} 3 \cdot 1 - 6 \cdot (-2) \\\\ 6 \cdot 4 - 0 \cdot 1 \\\\ 0 \cdot (-2) - 3 \cdot 4 \end{bmatrix} = \boxed{\begin{bmatrix} 15 \\\\ 24 \\\\ -12 \end{bmatrix}}
$$
</div>

Note that this is just <span class="math-inline">\\(-3\\)</span> times the vector we found above. Indeed, any scalar multiple of <span class="math-inline">\\(\begin{bmatrix} -5 \\\\ -8 \\\\ 4 \end{bmatrix}\\)</span> is also a solution.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> This part is unrelated to the previous part. Suppose <span class="math-inline">\\(\vec u, \vec v \in \mathbb{R}^n\\)</span>, and that:

-   <span class="math-inline">\\(\vec u\\)</span> is a unit vector,

-   <span class="math-inline">\\(\cos(\theta) = 2/3\\)</span>, where <span class="math-inline">\\(\theta\\)</span> is the angle between <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span>,

-   the projection of <span class="math-inline">\\(\vec v\\)</span> onto <span class="math-inline">\\(\vec u\\)</span> is <span class="math-inline">\\(6 \vec u\\)</span>.

What is the value of <span class="math-inline">\\(\lVert \vec v \rVert\\)</span>?

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(3\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(4\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(6\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(9\\)</span></span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(3\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(4\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(6\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(9\\)</span></span></div>

Since <span class="math-inline">\\(\vec u\\)</span> is a unit vector,

<div class="math-display">
$$
\vec p
= \frac{\vec v \cdot \vec u}{\vec u \cdot \vec u} \vec u
=
(\vec v \cdot \vec u)\vec u
$$
</div>

But this projection is also <span class="math-inline">\\(6 \vec u\\)</span>, so

<div class="math-display">
$$
\vec u \cdot \vec v = 6
$$
</div>

Now, let's use the fact that <span class="math-inline">\\(\cos(\theta) = 2/3\\)</span>, where <span class="math-inline">\\(\theta\\)</span> is the angle between <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span>, and plug in the values we know.

<div class="math-display">
$$
\begin{align*}
\cos \theta &= \frac{\vec u \cdot \vec v}{\lVert \vec u \rVert \lVert \vec v \rVert} \\\\
\frac{2}{3} &= \frac{6}{1 \cdot \lVert \vec v \rVert} \\\\
\lVert \vec v \rVert &= 9
\end{align*}
$$
</div>

So, <span class="math-inline">\\(\boxed{\lVert \vec v \rVert = 9}\\)</span>.
</details>

</div>
</div>

</div>


---

## SP26 MT1 · Problem 4 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">8 pts</span>

<p class="worksheet-source">From <a href="/exams/sp26-mt1/">SP26 MT1</a></p>


Let <span class="math-inline">\\(\vec u,\vec v\in\mathbb R^n\\)</span> be vectors satisfying

<div class="math-display">
$$
\|\vec v\|=5,\qquad \|\vec u+\vec v\|=10,\qquad \|\vec u-\vec v\|=6
$$
</div>

Find <span class="math-inline">\\(\lVert \vec u \rVert^2\\)</span> (**not** <span class="math-inline">\\(\lVert \vec u \rVert\\)</span>). Show your work, and write your final answer in the box provided. Your answer should be a number with no variables.

<div class="math-display">
$$
\lVert \vec u \rVert^2 = \_\_\_\_\_\_
$$
</div>

<details markdown="1"><summary>Solution</summary>

We have

<div class="math-display">
$$
10^2=\|\vec u+\vec v\|^2=\|\vec u\|^2+2\vec u\cdot\vec v+\|\vec v\|^2
$$
</div>

 and

<div class="math-display">
$$
6^2=\|\vec u-\vec v\|^2=\|\vec u\|^2-2\vec u\cdot\vec v+\|\vec v\|^2
$$
</div>

 Notice that the expressions on the right-hand side are similar, except for the signs of <span class="math-inline">\\(2 \vec u \cdot \vec v\\)</span>. So, adding these equations gives

<div class="math-display">
$$
136=2\|\vec u\|^2+2\|\vec v\|^2=2\|\vec u\|^2+50
$$
</div>

 so

<div class="math-display">
$$
\lVert \vec u \rVert^2 = \frac{136 - 50}{2} = \boxed{43}
$$
</div>

</details>


---

## SP26 MT1 · Problem 5 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">13 pts</span>

<p class="worksheet-source">From <a href="/exams/sp26-mt1/">SP26 MT1</a></p>


Suppose <span class="math-inline">\\(\vec u,\vec v\in\mathbb R^n\\)</span> are non-zero vectors and <span class="math-inline">\\(k\\)</span> is a scalar. Let

<div class="math-display">
$$
f(k) = \lVert \vec u - k \vec v \rVert^2 + C k^2
$$
</div>

 where <span class="math-inline">\\(C \geq 0\\)</span> is a non-negative constant.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> In this part only, suppose <span class="math-inline">\\(C=0\\)</span>, <span class="math-inline">\\(\vec u = \begin{bmatrix} 1 \\\\ 2 \end{bmatrix}\\)</span>, and <span class="math-inline">\\(\vec v = \begin{bmatrix} 3 \\\\ 1 \end{bmatrix}\\)</span>. Find the value of <span class="math-inline">\\(k\\)</span> that minimizes <span class="math-inline">\\(f(k)\\)</span>. Show your work, and write your final answer in the box provided. Your answer should be a number with no variables.

<div class="math-display">
$$
\text{minimizer of } f(k) = \_\_\_\_\_\_
$$
</div>

<details markdown="1"><summary>Solution</summary>

There are several ways to think about this problem. What I expected most students to see is that when <span class="math-inline">\\(C = 0\\)</span>, this is really asking for the orthogonal projection of <span class="math-inline">\\(\vec u\\)</span> onto <span class="math-inline">\\(\vec v\\)</span>; the minimizer of <span class="math-inline">\\(f(k)\\)</span> is the value of <span class="math-inline">\\(k\\)</span> that makes <span class="math-inline">\\(\vec u - k \vec v\\)</span> orthogonal to <span class="math-inline">\\(\vec v\\)</span>.

Using that logic, we know from [Chapter 3.4](https://notes.eecs245.org/vectors/orthogonal-projection/) that the orthogonal projection of <span class="math-inline">\\(\vec u\\)</span> onto <span class="math-inline">\\(\vec v\\)</span> is given by

<div class="math-display">
$$
\vec p = k^* \vec v = \left( \frac{\vec u \cdot \vec v}{\vec v \cdot \vec v} \right) \vec v
$$
</div>

So,

<div class="math-display">
$$
k^* = \frac{\vec u \cdot \vec v}{\vec v \cdot \vec v} = \frac{1 \cdot 3 + 2 \cdot 1}{3^2 + 1^2} = \frac{5}{10} = \boxed{\frac{1}{2}}
$$
</div>

There's another way to approach this problem, which is to simplify <span class="math-inline">\\(f(k)\\)</span> and treat this like a calculus problem.

<div class="math-display">
$$
f(k)=\left\|\begin{bmatrix}1\\\\2\end{bmatrix}-k\begin{bmatrix}3\\\\1\end{bmatrix}\right\|^2=(1-3k)^2+(2-k)^2
$$
</div>

 Expanding,

<div class="math-display">
$$
f(k)=10k^2-10k+5
$$
</div>

 so

<div class="math-display">
$$
f'(k)=20k-10
$$
</div>

 Setting <span class="math-inline">\\(f'(k)=0\\)</span> gives <span class="math-inline">\\(k^{\ast} = \frac{1}{2}\\)</span> as well.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Note that <span class="math-inline">\\(f(k)\\)</span> *almost* looks like the squared norm of the vector <span class="math-inline">\\(\vec u - k \vec v\\)</span>, but with an extra term <span class="math-inline">\\(C k^2\\)</span>. Let's try and rewrite <span class="math-inline">\\(f(k)\\)</span> so that it *is* the squared norm of another related vector.

Define two new vectors, <span class="math-inline">\\(\vec U, \vec V \in \mathbb R^{n+1}\\)</span> by appending the scalar <span class="math-inline">\\(a\\)</span> to the end of <span class="math-inline">\\(\vec u\\)</span> and the scalar <span class="math-inline">\\(b\\)</span> to the end of <span class="math-inline">\\(\vec v\\)</span>.

<div class="math-display">
$$
\vec U = \begin{bmatrix} u_1 \\\\ u_2 \\\\ \vdots \\\\ u_n \\\\ a\end{bmatrix}, \quad \vec V = \begin{bmatrix} v_1 \\\\ v_2 \\\\ \vdots \\\\ v_n \\\\ b\end{bmatrix}
$$
</div>

Select values of <span class="math-inline">\\(a\\)</span> and <span class="math-inline">\\(b\\)</span> so that <span class="math-inline">\\(f(k) = \lVert \vec U - k \vec V \rVert^2\\)</span>, for all possible non-negative values of <span class="math-inline">\\(C\\)</span>.

1.  What is the value of <span class="math-inline">\\(a\\)</span>?
<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 0</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(C\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(C^2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\sqrt{C}\\)</span></span></div>

2.  What is the value of <span class="math-inline">\\(b\\)</span>?
<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 0</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(C\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(C^2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\sqrt{C}\\)</span></span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 0</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(C\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(C^2\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(\sqrt{C}\\)</span></span></div>

First, let's try and get a better sense of how <span class="math-inline">\\(\lVert \vec U - k \vec V \rVert^2\\)</span> works.

<div class="math-display">
$$
\begin{align*}
\lVert \vec U - k \vec V \rVert^2 &= \left\lVert \begin{bmatrix} u_1 \\\\ u_2 \\\\ \vdots \\\\ u_n \\\\ a\end{bmatrix} - k \begin{bmatrix} v_1 \\\\ v_2 \\\\ \vdots \\\\ v_n \\\\ b\end{bmatrix} \right\rVert^2 \\\\
&= \left\lVert \begin{bmatrix} u_1 - kv_1 \\\\ u_2 - kv_2 \\\\ \vdots \\\\ u_n - kv_n \\\\ a - kb\end{bmatrix} \right\rVert^2 \\\\
&= \sum_{i=1}^n (u_i - kv_i)^2 + (a - kb)^2 \\\\
&= \lVert \vec u - k \vec v \rVert^2 + (a - kb)^2 \\\\
\end{align*}
$$
</div>

Our job is to find <span class="math-inline">\\(a\\)</span> and <span class="math-inline">\\(b\\)</span> so that <span class="math-inline">\\(f(k)\\)</span>, which we were told is defined as

<div class="math-display">
$$
f(k) =\lVert \vec u - k \vec v \rVert^2 + C k^2
$$
</div>

 is **also** equal to

<div class="math-display">
$$
\lVert \vec U - k \vec V \rVert^2 = \lVert \vec u - k \vec v \rVert^2 + (a - kb)^2
$$
</div>

If we set <span class="math-inline">\\(f(k) = \lVert \vec U - k \vec V \rVert^2\\)</span>, we see that this boils down to finding <span class="math-inline">\\(a\\)</span> and <span class="math-inline">\\(b\\)</span> such that

<div class="math-display">
$$
(a - kb)^2 = C k^2
$$
</div>

Notice the right-hand side of the expression above is just <span class="math-inline">\\(Ck^2\\)</span>, not <span class="math-inline">\\(Ck^2 + \text{some constant} \cdot k + \text{some other constant}\\)</span>. This means that <span class="math-inline">\\(a = 0\\)</span>, and that forces <span class="math-inline">\\(b = \sqrt{C}\\)</span>:

<div class="math-display">
$$
(0 - k\sqrt{C})^2 = Ck^2
$$
</div>

So, the correct answers are <span class="math-inline">\\(\boxed{a=0}\\)</span> and <span class="math-inline">\\(\boxed{b=\sqrt{C}}\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> As <span class="math-inline">\\(C\\)</span> increases, what happens to the value of <span class="math-inline">\\(k\\)</span> that minimizes <span class="math-inline">\\(f(k)\\)</span>? Explain your reasoning.

<details markdown="1"><summary>Solution</summary>

There are a couple of ways to think about this. First, if we use the interpretation provided in part **b)**, the vectors <span class="math-inline">\\(\vec U\\)</span> and <span class="math-inline">\\(\vec V\\)</span> "bake in" the value of <span class="math-inline">\\(C\\)</span>:

<div class="math-display">
$$
\vec U = \begin{bmatrix} u_1 \\\\ u_2 \\\\ \vdots \\\\ u_n \\\\ 0\end{bmatrix}, \quad \vec V = \begin{bmatrix} v_1 \\\\ v_2 \\\\ \vdots \\\\ v_n \\\\ \sqrt{C}\end{bmatrix}
$$
</div>

Increasing <span class="math-inline">\\(C\\)</span> keeps the dot product of <span class="math-inline">\\(\vec U\\)</span> and <span class="math-inline">\\(\vec V\\)</span> fixed, but increases the norm of <span class="math-inline">\\(\vec V\\)</span>. Why is this relevant? Since <span class="math-inline">\\(f(k) = \lVert \vec U - k \vec V \rVert^2\\)</span>, the minimizer <span class="math-inline">\\(k^{\ast}\\)</span> of <span class="math-inline">\\(f(k)\\)</span> is equal to

<div class="math-display">
$$
k^* = \frac{\vec U \cdot \vec V}{\vec V \cdot \vec V}
$$
</div>

So, as <span class="math-inline">\\(C\\)</span> increases, the denominator of <span class="math-inline">\\(k^{\ast}\\)</span> increases, so <span class="math-inline">\\(k^{\ast}\\)</span> moves toward <span class="math-inline">\\(0\\)</span>, though this may happen either from the left or the right, since <span class="math-inline">\\(\vec U \cdot \vec V\\)</span> may be positive or negative.

If you'd prefer, you *could* just expand the original definition of <span class="math-inline">\\(f(k)\\)</span>, take the derivative to find the closed-form expression for the minimizing <span class="math-inline">\\(k^{\ast}\\)</span> for an arbitrary <span class="math-inline">\\(C\\)</span>, and look at what happens to <span class="math-inline">\\(k^{\ast}\\)</span> as <span class="math-inline">\\(C\\)</span> increases.

Recall, the original definition of <span class="math-inline">\\(f(k)\\)</span> is <span class="math-inline">\\(f(k)=\lVert \vec u - k \vec v \rVert^2 + C k^2\\)</span>, so

<div class="math-display">
$$
f(k)=\vec u \cdot \vec u - 2k(\vec u\cdot\vec v)+k^2\vec v \cdot \vec v+Ck^2
$$
</div>

 Therefore,

<div class="math-display">
$$
f'(k)=-2(\vec u\cdot\vec v)+2k(\vec v \cdot \vec v+C)
$$
</div>

 so the minimizer is

<div class="math-display">
$$
k^*=\frac{\vec u\cdot\vec v}{\vec v \cdot \vec v+C}
$$
</div>

 As <span class="math-inline">\\(C\\)</span> increases, the denominator increases (but <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> are fixed --- notice these are the original <span class="math-inline">\\(\vec u, \vec v\\)</span>, not the new <span class="math-inline">\\(\vec U, \vec V\\)</span>), so <span class="math-inline">\\(k^{\ast}\\)</span> moves toward <span class="math-inline">\\(0\\)</span>.
</details>

</div>
</div>

</div>


---

## SP26 MT1 · Problem 9 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">10 pts</span>

<p class="worksheet-source">From <a href="/exams/sp26-mt1/">SP26 MT1</a></p>


<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">7 pts</span> Suppose <span class="math-inline">\\(x\\)</span> and <span class="math-inline">\\(y\\)</span> are non-negative numbers. Using the Cauchy-Schwarz inequality, prove that

<div class="math-display">
$$
\frac{(x+y)^2}{2}\le x^2+y^2
$$
</div>

<em>Solutions that do not use the Cauchy-Schwarz inequality will not receive credit.</em>

<details markdown="1"><summary>Solution</summary>

Recall, the Cauchy-Schwarz inequality states that for any two vectors <span class="math-inline">\\(\vec u, \vec v \in \mathbb{R}^n\\)</span>,

<div class="math-display">
$$
|\vec u \cdot \vec v| \leq \|\vec u\| \|\vec v\|
$$
</div>

Applying Cauchy-Schwarz to the vectors <span class="math-inline">\\(\vec u=\begin{bmatrix}x\\\\y\end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec v=\begin{bmatrix}1\\\\1\end{bmatrix}\\)</span> gives

<div class="math-display">
$$
|x + y| \leq \sqrt{x^2 + y^2} \sqrt{1^2 + 1^2} = \sqrt{2(x^2 + y^2)}
$$
</div>

 Squaring both sides gives

<div class="math-display">
$$
(x + y)^2 \leq 2(x^2 + y^2)
$$
</div>

 and finally, dividing both sides by <span class="math-inline">\\(2\\)</span> gives

<div class="math-display">
$$
\frac{(x+y)^2}{2}\le x^2+y^2
$$
</div>

 as needed.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> Now suppose <span class="math-inline">\\(x\\)</span>, <span class="math-inline">\\(y\\)</span>, and <span class="math-inline">\\(z\\)</span> are non-negative numbers. Which inequality is guaranteed to be true?

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \frac{(x+y+z)^2}{2}\le x^2+y^2+z^2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \frac{(x+y+z)^2}{3}\le x^2+y^2+z^2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \frac{(x+y+z)^2}{2}\le x^3+y^3+z^3\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \frac{(x+y+z)^3}{3}\le x^3+y^3+z^3\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> None of the above</span></div>

<details markdown="1"><summary>Solution</summary>

<span class="mc-bubble" aria-hidden="true"></span> None of the above

The Cauchy-Schwarz inequality directly implies one of the options, and the other options are all not guaranteed to be true. Extending our argument from part **a)**, let's now apply Cauchy-Schwarz to the vectors <span class="math-inline">\\(\vec u=\begin{bmatrix}x\\\\y\\\\z\end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec v=\begin{bmatrix}1\\\\1\\\\1\end{bmatrix}\\)</span>. This gives

<div class="math-display">
$$
|x+y+z|\le \sqrt{x^2+y^2+z^2} \sqrt{1^2+1^2+1^2} = \sqrt{3(x^2+y^2+z^2)}
$$
</div>

 Squaring both sides and dividing by <span class="math-inline">\\(3\\)</span> gives

<div class="math-display">
$$
\frac{(x+y+z)^2}{3}\le x^2+y^2+z^2
$$
</div>

 which is the second option.
</details>
</div>
</div>

</div>

---

## SP26 Final · Problem 3 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">10 pts</span> <span class="badge" data-flag="mt1-redemption" style="background-color: #9A3324; color: #FFFFFF; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">MT1 Redemption</span>

<p class="worksheet-source">From <a href="/exams/sp26-final/">SP26 Final</a></p>


Let <span class="math-inline">\\(\vec x = \begin{bmatrix} 2 \\\\ 1 \\\\ 1 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec z = \begin{bmatrix} 3 \\\\ 9 \\\\ 3 \end{bmatrix}\\)</span>, and suppose <span class="math-inline">\\(\vec y \in \mathbb{R}^3\\)</span> is such that

the projection of <span class="math-inline">\\(\vec x\\)</span> onto <span class="math-inline">\\(\vec y\\)</span> is <span class="math-inline">\\(\vec 0\\)</span> and that <span class="math-inline">\\(\vec y \cdot \vec y = \vec y \cdot \vec z = 45\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Find the projection of <span class="math-inline">\\(\vec z\\)</span> onto <span class="math-inline">\\(\vec x\\)</span>. Show your work, and write your final answer in the box provided. Give your answer as a vector with no variables.

<div class="math-display">
$$
\text{projection of }\vec z\text{ onto }\vec x = \_\_\_\_\_\_
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

## More practice (PDF only)

- [MOCK MT1 Problem 4](/resources/exams/mock-mt1.pdf#page=7)
- [MOCK MT1 Problem 7](/resources/exams/mock-mt1.pdf#page=11)

{% endraw %}
