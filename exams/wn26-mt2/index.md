---
layout: minimal
title: "Winter 2026 Midterm 2"
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

# Winter 2026 Midterm 2

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/exams/wn26-mt2.pdf" target="_blank">View as PDF ✏️</a>
<a class="btn btn-info assignment-pdf-button" href="/resources/exams/wn26-mt2-solutions.pdf" target="_blank">Solutions PDF ✅</a>
</div>

{: .yellow }
<div markdown="1">
**Instructions**

-   This exam consists of 8 problems, worth a total of 100 points, spread across 12 pages (6 sheets of paper).

-   You have 120 minutes to complete this exam, unless you have extended-time accommodations through SSD.

-   Write your uniqname in the top right corner of each page.

-   For free response problems, **you must show all of your work**, and <span class="math-inline">\\(\boxed{\text{circle}}\\)</span> your final answer. We will not grade work that appears elsewhere, and you may lose points if your work is not shown.

-   For multiple choice problems, completely fill in bubbles and square boxes; if we cannot tell which option(s) you selected, you may lose points.



-   You may refer to **two double-sided 8.5x11" handwritten notes sheets**. Other than that, you may not refer to any other resources or technology during the exam (no phones, watches, or calculators).
</div>

---

## Problems

- [Problem 1](#problem-1-12-pts)
- [Problem 2](#problem-2-10-pts)
- [Problem 3](#problem-3-11-pts)
- [Problem 4](#problem-4-13-pts)
- [Problem 5](#problem-5-13-pts)
- [Problem 6](#problem-6-20-pts)
- [Problem 7](#problem-7-10-pts)
- [Problem 8](#problem-8-11-pts)

---

## Problem 1 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>

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
k = \boxed{\textbf{6}}
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
k = \boxed{\textbf{5}}
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
k = \boxed{\textbf{4}}
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

## Problem 2 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">10 pts</span>

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

## Problem 3 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">11 pts</span>

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

## Problem 4 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">13 pts</span>

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

## Problem 5 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">13 pts</span>

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

<span class="math-inline">\\(C = \boxed{\textbf{\begin{bmatrix} 1 &amp; 0 &amp; 0 \\\\ 2 &amp; 1 &amp; 0 \\\\ 3 &amp; 1 &amp; -7 \end{bmatrix}}}, \quad R = \boxed{\textbf{\begin{bmatrix} 1 &amp; 0 &amp; 0 &amp; 0 &amp; 0 \\\\ 0 &amp; 1 &amp; 0 &amp; 0 &amp; 4 \\\\ 0 &amp; 0 &amp; 0 &amp; 1 &amp; 0 \end{bmatrix}}}\\)</span>

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

<span class="math-inline">\\(\text{dim}(\text{nullsp}(A^T)) = \boxed{\textbf{0}}\\)</span>

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
P = \boxed{\textbf{Q^TQ}}
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

## Problem 6 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">20 pts</span>

Suppose we'd like to fit a multiple linear regression model **without** an intercept term to **predict the number of fans in attendance at a Michigan football home game** given various features.

For each row in the dataset, the corresponding feature vector is <span class="math-inline">\\(\vec x&#95;i = \begin{bmatrix} \text{tempF}&#95;i \\\\ \text{tempC}&#95;i \\\\ \text{night}&#95;i \\\\ \text{day}&#95;i \end{bmatrix}\\)</span>, where:

-   <span class="math-inline">\\(\text{tempF}&#95;i\\)</span> is the temperature, in degrees **Fahrenheit**, at kickoff for game <span class="math-inline">\\(i\\)</span>

-   <span class="math-inline">\\(\text{tempC}&#95;i\\)</span> is the temperature, in degrees **Celsius**, at kickoff for game <span class="math-inline">\\(i\\)</span>

-   <span class="math-inline">\\(\text{night}&#95;i\\)</span> is 1 if game <span class="math-inline">\\(i\\)</span> is a night game and 0 otherwise

-   <span class="math-inline">\\(\text{day}&#95;i\\)</span> is 0 if game <span class="math-inline">\\(i\\)</span> is a night game and 1 otherwise

**Important**: Note that

<div class="math-display">
$$
\text{tempC}_i = \frac{5}{9} (\text{tempF}_i - 32)
$$
</div>

So, our model is of the form

<div class="math-display">
$$
h(\vec x_i) = w_1 \cdot \text{tempF}_i + w_2 \cdot \text{tempC}_i + w_3 \cdot \text{night}_i + w_4 \cdot \text{day}_i
$$
</div>

 We find optimal model parameters, <span class="math-inline">\\(\vec w^{\ast} = \begin{bmatrix} w&#95;1^{\ast} \\\\ w&#95;2^{\ast} \\\\ w&#95;3^{\ast} \\\\ w&#95;4^{\ast} \end{bmatrix}\\)</span>, by solving the normal equation.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> The first two rows of the dataset have the following information:

-   Game 1: 77 degrees Fahrenheit, 25 degrees Celsius, not night game, 102,111 fans

-   Game 2: 59 degrees Fahrenheit, 15 degrees Celsius, night game, 101,982 fans

Write the first two rows of the design matrix, <span class="math-inline">\\(X\\)</span>. Your answer should be a matrix with two rows and no variables.

<span class="math-inline">\\(X = \boxed{\textbf{\begin{bmatrix} 77 &amp; 25 &amp; 0 &amp; 1 \\\\ 59 &amp; 15 &amp; 1 &amp; 0 \end{bmatrix}}}\\)</span>

<details markdown="1"><summary>Solution</summary>

Each row of the design matrix is just the feature vector for that game:

<div class="math-display">
$$
\vec x_i = \begin{bmatrix} \text{tempF}_i \\\\ \text{tempC}_i \\\\ \text{night}_i \\\\ \text{day}_i \end{bmatrix}
$$
</div>

So,

<div class="math-display">
$$
\text{Game 1}: \begin{bmatrix} 77 & 25 & 0 & 1 \end{bmatrix}
\qquad
\text{Game 2}: \begin{bmatrix} 59 & 15 & 1 & 0 \end{bmatrix}
$$
</div>

Therefore, the first two rows of <span class="math-inline">\\(X\\)</span> are

<div class="math-display">
$$
X = \begin{bmatrix}
77 & 25 & 0 & 1 \\\\
59 & 15 & 1 & 0
\end{bmatrix}
$$
</div>

</details>

Recall, our model is of the form

<div class="math-display">
$$
h(\vec x_i) = w_1 \cdot \text{tempF}_i + w_2 \cdot \text{tempC}_i + w_3 \cdot \text{night}_i + w_4 \cdot \text{day}_i
$$
</div>

where <span class="math-inline">\\(\text{tempC}&#95;i = \frac{5}{9} (\text{tempF}&#95;i - 32)\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Suppose <span class="math-inline">\\(\vec w'\\)</span> is one solution to the normal equation for this model. Which option describes the **complete set** of solutions to the normal equation?

|     |     |
|:----|:----|
|     |     |

<details markdown="1"><summary>Solution</summary>

If we add any vector in <span class="math-inline">\\(\text{nullsp}(X)\\)</span> to one solution of the normal equation, we get another solution. So we just need to find a non-zero vector in <span class="math-inline">\\(\text{nullsp}(X)\\)</span>.

For any row of <span class="math-inline">\\(X\\)</span>, the following two statements must be true:

<div class="math-display">
$$
\begin{align*}
\text{tempC}_i &= \frac{5}{9}(\text{tempF}_i - 32) \\\\
\text{night}_i + \text{day}_i &= 1
\end{align*}
$$
</div>

The idea is to use this information to find a linear combination of <span class="math-inline">\\(X\\)</span>'s columns that equals the zero vector.

Using the first equation, we have

<div class="math-display">
$$
\text{tempF}_i - \frac{9}{5}\text{tempC}_i - 32 = 0
$$
</div>

In order to write this as a linear combination of <span class="math-inline">\\(X\\)</span>'s columns, the 32 needs to come from a vector that is "constant" across all rows. Fortunately, that's true of the sum of the night and day columns, since <span class="math-inline">\\(\text{night}&#95;i + \text{day}&#95;i = 1\\)</span> for all rows. So, this means

<div class="math-display">
$$
\begin{align*}
\text{tempF}_i - \frac{9}{5}\text{tempC}_i - 32(\text{night}_i + \text{day}_i) &= 0 \\\\
\text{tempF}_i - \frac{9}{5}\text{tempC}_i - 32 \text{night}_i - 32 \text{day}_i &= 0 \\\\
\end{align*}
$$
</div>

Meaning that

<div class="math-display">
$$
\begin{bmatrix} 1 \\\\ -9/5 \\\\ -32 \\\\ -32 \end{bmatrix} \in \text{nullsp}(X)
$$
</div>

Therefore, if <span class="math-inline">\\(\vec w'\\)</span> is one solution, the complete set of solutions is

<div class="math-display">
$$
\left \{ \vec w' + t\begin{bmatrix} 1 \\\\ -9/5 \\\\ -32 \\\\ -32 \end{bmatrix} \: , \: t \in \mathbb{R} \right \}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> First, assume <span class="math-inline">\\(h(\vec x&#95;i)\\)</span> is the model at the top of the page.

1.  What is the **largest possible** rank of the design matrix, <span class="math-inline">\\(X\\)</span>? (Note that we're asking about the full design matrix, not just its first two rows.)

   <span class="math-inline">\\(\text{largest possible value of }\text{rank}(X) = \boxed{\textbf{3}}\\)</span>

2.  True or False: The sum of the errors of the model's predictions is 0.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

3.  True or False: The sum of the errors of the model's predictions **on just the rows of the dataset corresponding to night games** is 0.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

Let <span class="math-inline">\\(\vec e = \vec y - X \vec w^{\ast}\\)</span> be the error vector. Since <span class="math-inline">\\(\vec w^{\ast}\\)</span> satisfies the normal equation, <span class="math-inline">\\(\vec e\\)</span> is orthogonal to every column of <span class="math-inline">\\(X\\)</span>, and to every linear combination of those columns.

**(i)** The largest possible rank of <span class="math-inline">\\(X\\)</span> is 3, which happens when the tempF, tempC, and night columns are linearly independent. When the day column is added, the columns become linearly dependent. (Equivalently, the tempF, night, and day columns are linearly independent, but linearly dependent with the tempC column.)

**(ii)** This is true. Even though there is no explicit intercept term (and thus, no column of all ones), the all-ones vector is still in <span class="math-inline">\\(\text{colsp}(X)\\)</span>, because the night and day columns add up to 1 for each row.

<div class="math-display">
$$
\vec 1 = \text{night column} + \text{day column}
$$
</div>

 Since <span class="math-inline">\\(\vec e\\)</span> is orthogonal to every vector in <span class="math-inline">\\(\text{colsp}(X)\\)</span>, it is orthogonal to <span class="math-inline">\\(\vec 1\\)</span>, so

<div class="math-display">
$$
\begin{align*}
\vec 1^T \vec e &= \sum_{i=1}^n e_i = 0
\end{align*}
$$
</div>

**(iii)** This is also true. The night indicator is itself a column of <span class="math-inline">\\(X\\)</span>, so

<div class="math-display">
$$
\vec e \cdot (\text{night column}) = \vec e \cdot \begin{bmatrix} 0 \\\\ 1 \\\\ \vdots \end{bmatrix} = e_2 + ... = 0
$$
</div>

 But this dot product is exactly the sum of the errors for just the night games, because the night column has 1s on night rows and 0s elsewhere.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Now, suppose we remove the <span class="math-inline">\\(\textbf{day}&#95;i\\)</span> feature from our model, meaning our model is

<div class="math-display">
$$
h(\vec x_i) = w_1 \cdot \text{tempF}_i + w_2 \cdot \text{tempC}_i + w_3 \cdot \text{night}_i
$$
</div>

1.  After removing the day column, what is the **largest possible** rank of the **new** design matrix?

   <span class="math-inline">\\(\text{largest possible value of }\text{rank}(\text{new design matrix}) = \boxed{\textbf{3}}\\)</span>

2.  True or False: The sum of the errors of the new model's predictions is 0.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

3.  True or False: The sum of the errors of the new model's predictions **on just the rows of the dataset corresponding to night games** is 0.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

Let <span class="math-inline">\\(\vec e&#95;{\text{new}}\\)</span> be the error vector for the new model.

**(i)** After removing the day column, the new design matrix has 3 columns, and there is no longer a forced linear dependence among them. So the largest possible rank is still 3. What's new now is that <span class="math-inline">\\(X\\)</span>'s columns are all linearly independent, meaning there is a unique solution to the normal equation.

**(ii)** This is false. The normal equations still tell us that <span class="math-inline">\\(\vec e&#95;{\text{new}}\\)</span> is orthogonal to each column of the new design matrix, but there is no guarantee that the all-ones vector is in the column space anymore. So the errors are not guaranteed to sum to 0.

**(iii)** This is true. The night indicator column is still present in the new design matrix, so <span class="math-inline">\\(\vec e&#95;{\text{new}}\\)</span> is orthogonal to that column. Therefore, the sum of the errors over the night-game rows is still 0.
</details>

</div>
</div>

</div>

---

## Problem 7 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">10 pts</span>

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

<span class="math-inline">\\(A = \boxed{\textbf{\begin{bmatrix} 1 &amp; 0 &amp; 0 &amp; 0 \\\\ 0 &amp; -15/2 &amp; 0 &amp; 0 \\\\ 0 &amp; 0 &amp; 5 &amp; 0 \\\\ 0 &amp; 0 &amp; 0 &amp; 1/2 \end{bmatrix}}}\\)</span>

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

## Problem 8 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">11 pts</span>

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
\alpha = \boxed{\textbf{1/4}}
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

Congrats on finishing Midterm 2!

Feel free to draw us a picture about EECS 245 in the box below (or use it for scratch work).

Did you notice any violations of the Honor Code during the exam? If so, share details with us here. We will keep your identity anonymous when investigating any cases.
</div>
</div>

</div>

{% endraw %}
