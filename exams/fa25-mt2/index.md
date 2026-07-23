---
layout: minimal
title: "Fall 2025 Midterm 2"
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

# Fall 2025 Midterm 2

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/exams/fa25-mt2.pdf" target="_blank">View as PDF ✏️</a>
<a class="btn btn-info assignment-pdf-button" href="/resources/exams/fa25-mt2-solutions.pdf" target="_blank">Solutions PDF ✅</a>
</div>

{: .yellow }
<div markdown="1">
**Instructions**

-   This exam consists of 7 problems, worth a total of 100 points, spread across 12 pages (6 sheets of paper).

-   You have 80 minutes to complete this exam, unless you have extended-time accommodations through SSD.

-   Write your uniqname in the top right corner of every page in the space provided.

-   For free response problems, you must show all of your work (unless otherwise specified), and <span class="math-inline">\\(\boxed{\text{circle}}\\)</span> your final answer. We will not grade work that appears elsewhere, and you may lose points if your work is not shown.

-   For multiple choice problems, completely fill in bubbles and square boxes; if we cannot tell which option(s) you selected, you may lose points.



-   You may refer to a single two-sided handwritten notes sheet. Other than that, you may not refer to any other resources or technology during the exam (no phones, watches, or calculators).
</div>

---

## Problems

- [Problem 1: Getting Started](#problem-1-getting-started-12-pts)
- [Problem 2: Space Jam](#problem-2-space-jam-20-pts)
- [Problem 3: Nilpotence](#problem-3-nilpotence-12-pts)
- [Problem 4: Poly Wants a Cracker](#problem-4-poly-wants-a-cracker-18-pts)
- [Problem 5: Ortho\...dontist?](#problem-5-orthodontist-12-pts)
- [Problem 6: Quadratus Formulus](#problem-6-quadratus-formulus-14-pts)
- [Problem 7: Complexity](#problem-7-complexity-10-pts)

---

## Problem 1: Getting Started <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> Let <span class="math-inline">\\(A = \begin{bmatrix} 2 &amp; 4 \\\\ -3 &amp; -7 \end{bmatrix}\\)</span>. Find <span class="math-inline">\\(\text{det}(A)\\)</span>, the determinant of <span class="math-inline">\\(A\\)</span>. Give your answer as an integer.

<span class="math-inline">\\(\text{det}(A) = \boxed{\textbf{-2}}\\)</span>

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

<span class="math-inline">\\(A^{-1} = \boxed{\textbf{\begin{bmatrix} 7/2 &amp; 2 \\\\ -3/2 &amp; -1 \end{bmatrix}}}\\)</span>

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

## Problem 2: Space Jam <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">20 pts</span>

Let <span class="math-inline">\\(X = \begin{bmatrix} 1 &amp; -4 &amp; 2 &amp; 2 &amp; 0 \\\\ 0 &amp; 0 &amp; -3 &amp; 3 &amp; 0 \\\\ 1 &amp; -4 &amp; 4 &amp; 0 &amp; 0 \\\\ 0 &amp; 0 &amp; 0 &amp; 0 &amp; 1 \end{bmatrix}\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(4.5 pts) Determine the values of each of the following. Give your answers as integers.

<div class="math-display">
$$
\begin{array}{lllll}
\text{dim}(\text{colsp}(X)) = &\boxed{\textbf{3}} \qquad \qquad  & \text{dim}(\text{nullsp}(X)) = &\boxed{\textbf{2}} \\\\ \\\\
\text{dim}(\text{colsp}(X^T)) = &\boxed{\textbf{3}} \qquad \qquad  & \text{dim}(\text{nullsp}(X^T)) = &\boxed{\textbf{1}} \\\\
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

## Problem 3: Nilpotence <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>

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

## Problem 4: Poly Wants a Cracker <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">18 pts</span>

Suppose we'd like to fit the model <span class="math-inline">\\(\boxed{h(x&#95;i) = w&#95;0 + w&#95;1 x&#95;i + w&#95;2 x&#95;i^2}\\)</span> by minimizing mean squared error. We use an observation vector <span class="math-inline">\\(\vec y \in \mathbb{R}^n\\)</span>, but instead of using the regular design matrix <span class="math-inline">\\(X\\)</span>,

<div class="math-display">
$$
X = \begin{bmatrix} 1 & x_1 & x_1^2 \\\\ 1 & x_2 & x_2^2 \\\\ \vdots & \vdots & \vdots \\\\ 1 & x_n & x_n^2 \end{bmatrix} = \begin{bmatrix} | & | & | \\\\ \vec x^{(0)} & \vec x^{(1)} & \vec x^{(2)} \\\\ | & | & | \end{bmatrix}
$$
</div>

we use the **centered** design matrix <span class="math-inline">\\(Z\\)</span> (where <span class="math-inline">\\(\bar{x} = \frac{1}{n} \sum&#95;{i=1}^n x&#95;i\\)</span> is the mean of the <span class="math-inline">\\(x\\)</span>'s).

<div class="math-display">
$$
Z = \begin{bmatrix} 1 & x_1 - \bar{x} & (x_1 - \bar{x})^2 \\\\ 1 & x_2 - \bar{x} & (x_2 - \bar{x})^2 \\\\ \vdots & \vdots & \vdots \\\\ 1 & x_n - \bar{x} & (x_n - \bar{x})^2 \end{bmatrix} = \begin{bmatrix} | & | & | \\\\ \vec z^{(0)} & \vec z^{(1)} & \vec z^{(2)} \\\\ | & | & | \end{bmatrix}
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> It turns out that <span class="math-inline">\\(\text{colsp}(Z) = \text{colsp}(X)\\)</span>. To show this, fill in the blanks below to express <span class="math-inline">\\(\vec z^{(2)}\\)</span> (the third column of <span class="math-inline">\\(Z\\)</span>) as a linear combination of <span class="math-inline">\\(X\\)</span>'s columns. Each box should be filled with an expression involving <span class="math-inline">\\(\bar{x}\\)</span>, <span class="math-inline">\\(n\\)</span>, and/or constants.

<div class="math-display">
$$
\vec z^{(2)} = \boxed{\textbf{\bar{x}^2}} \: \begin{bmatrix} 1 \\\\ 1 \\\\ \vdots \\\\ 1 \end{bmatrix} + \boxed{\textbf{(-2\bar{x})}} \: \begin{bmatrix} x_1 \\\\ x_2 \\\\ \vdots \\\\ x_n \end{bmatrix} + \boxed{\textbf{1}} \: \begin{bmatrix} x_1^2 \\\\ x_2^2 \\\\ \vdots \\\\ x_n^2 \end{bmatrix}
$$
</div>

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(\vec z^{(2)}\\)</span> is the column made up of terms of the form <span class="math-inline">\\((x&#95;i - \bar x)^2\\)</span>. Note that

<div class="math-display">
$$
(x_i - \bar x)^2=x_i^2 -2\bar x x_i + \bar x^2 = ({\bar x}^2)(1) + (-2\bar x)(x_i) + (1)(x_i^2)
$$
</div>

which tells us that

<div class="math-display">
$$
\vec z^{(2)} = \bar{x}^2 \begin{bmatrix} 1 \\\\ 1 \\\\ \vdots \\\\ 1 \end{bmatrix} -2\bar{x} \begin{bmatrix} x_1 \\\\ x_2 \\\\ \vdots \\\\ x_n \end{bmatrix} + \begin{bmatrix} x_1^2 \\\\ x_2^2 \\\\ \vdots \\\\ x_n^2 \end{bmatrix}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(6 pts) In this part only, assume that the values <span class="math-inline">\\(x&#95;1, x&#95;2, ..., x&#95;n\\)</span> are each either 1 or 0. For some specific values <span class="math-inline">\\(x&#95;1, x&#95;2, ..., x&#95;n\\)</span>, the matrix <span class="math-inline">\\(P\\)</span> that projects vectors in <span class="math-inline">\\(\mathbb{R}^n\\)</span> onto <span class="math-inline">\\(\text{colsp}(Z)\\)</span> is given by

<div class="math-display">
$$
P = \begin{bmatrix}
1/3 & 1/3 & 0      & 1/3 & 0      \\\\
1/3 & 1/3 & 0      & 1/3 & 0      \\\\
0      & 0      & 1/2    & 0      & 1/2    \\\\
1/3 & 1/3 & 0      & 1/3 & 0      \\\\
0      & 0      & 1/2    & 0      & 1/2
\end{bmatrix}
$$
</div>

1.  What is the rank of <span class="math-inline">\\(Z\\)</span>? Give your answer as an integer. <span class="math-inline">\\(\text{rank}(Z) = \boxed{\textbf{2}}\\)</span>

2.  Which specific values of <span class="math-inline">\\(x&#95;1, x&#95;2, ..., x&#95;n\\)</span> result in <span class="math-inline">\\(P\\)</span> being the matrix above? Give your answer as a list of values, in the order <span class="math-inline">\\(x&#95;1\\)</span>, then <span class="math-inline">\\(x&#95;2\\)</span>, then <span class="math-inline">\\(x&#95;3\\)</span>, etc. (If there are multiple possible answers, just give one.)

<details markdown="1"><summary>Solution</summary>

First, <span class="math-inline">\\(\text{rank}(Z) = 2\\)</span>. We're told in part **a)** that <span class="math-inline">\\(\text{colsp}(Z) = \text{colsp}(X)\\)</span>, so <span class="math-inline">\\(\text{rank}(Z) = \text{rank}(X)\\)</span>. I find it easier to think in terms of <span class="math-inline">\\(X\\)</span> since the numbers are more straightforward.

**Remember, throughout this part, that each <span class="math-inline">\\(x&#95;i\\)</span> is either 1 or 0!** This means that the column <span class="math-inline">\\(\vec x^{(1)} = \begin{bmatrix} x&#95;1 \\\\ x&#95;2 \\\\ \vdots \\\\ x&#95;n \end{bmatrix}\\)</span> is made up of 1's and 0's, and the column <span class="math-inline">\\(\vec x^{(2)} = \begin{bmatrix} x&#95;1^2 \\\\ x&#95;2^2 \\\\ \vdots \\\\ x&#95;n^2 \end{bmatrix}\\)</span> is made up of 1's and 0's in the same positions, since <span class="math-inline">\\(1^2 = 1\\)</span> and <span class="math-inline">\\(0^2 = 0\\)</span>.

So, <span class="math-inline">\\(X\\)</span> only really has two unique columns, and its rank is 2. But since <span class="math-inline">\\(\text{rank}(Z) = \text{rank}(X)\\)</span>, we have <span class="math-inline">\\(\text{rank}(Z) = 2\\)</span>. <span class="math-inline">\\(Z\\)</span> doesn't have any repeated columns, but as we showed above, it's still the case that one of <span class="math-inline">\\(Z\\)</span>'s columns is a linear combination of the other two.

The only case in which <span class="math-inline">\\(\text{rank}(Z) = 1\\)</span> is if all of the <span class="math-inline">\\(x&#95;i\\)</span> are the same, but the matrix <span class="math-inline">\\(P\\)</span> tells us that that is not the case.

Let's now look at the matrix <span class="math-inline">\\(P\\)</span>. Notice that rows 1, 2, and 4 of <span class="math-inline">\\(P\\)</span> are identical, as are rows 3 and 5. Let's imagine some vector <span class="math-inline">\\(\vec y \in \mathbb{R}^5\\)</span>. What would multiplying <span class="math-inline">\\(P\\)</span> by <span class="math-inline">\\(\vec y\\)</span> give us?

<div class="math-display">
$$
P \vec y = \begin{bmatrix} 1/3 & 1/3 & 0      & 1/3 & 0      \\\\
1/3 & 1/3 & 0      & 1/3 & 0      \\\\
0      & 0      & 1/2    & 0      & 1/2    \\\\
1/3 & 1/3 & 0      & 1/3 & 0      \\\\
0      & 0      & 1/2    & 0      & 1/2
\end{bmatrix} \begin{bmatrix} y_1 \\\\ y_2 \\\\ y_3 \\\\ y_4 \\\\ y_5 \end{bmatrix} = \begin{bmatrix} \frac{1}{3}y_1 + \frac{1}{3}y_2 + \frac{1}{3}y_4 \\\\ \frac{1}{3}y_1 + \frac{1}{3}y_2 + \frac{1}{3}y_4 \\\\ \frac{1}{2}y_3 + \frac{1}{2}y_5 \\\\ \frac{1}{3}y_1 + \frac{1}{3}y_2 + \frac{1}{3}y_4 \\\\ \frac{1}{2}y_3 + \frac{1}{2}y_5 \end{bmatrix} = \begin{bmatrix} \text{mean of } y_1, y_2, y_4 \\\\ \text{mean of } y_1, y_2, y_4 \\\\ \text{mean of } y_3, y_5 \\\\ \text{mean of } y_1, y_2, y_4 \\\\ \text{mean of } y_3, y_5 \end{bmatrix}
$$
</div>

We know from Chapter 1 that the mean is the constant that minimizes mean squared error. Here, it appears that the prediction returned in <span class="math-inline">\\(\vec y\\)</span> is not always the same, but is one of two possibilities --- rows 1, 2, and 4 have the same prediction, and rows 3 and 5 have the same prediction. This hints to us that rows 1, 2, and 4 come from the same <span class="math-inline">\\(x&#95;i\\)</span> value, and rows 3 and 5 come from the same <span class="math-inline">\\(x&#95;i\\)</span> value, and the optimal prediction is some **conditional** mean. This resembles [Lab 9, Activity 2](https://eecs245.org/resources/labs/lab09/lab09-solutions.pdf#page=3), on one hot encoding with beef, chicken, and fish.

The above observation alone is enough information to answer the question. The two possible answers are <span class="math-inline">\\(\boxed{x&#95;1 = 1, x&#95;2 = 1, x&#95;3 = 0, x&#95;4 = 1, x&#95;5 = 0}\\)</span> and <span class="math-inline">\\(\boxed{x&#95;1 = 0, x&#95;2 = 0, x&#95;3 = 1, x&#95;4 = 0, x&#95;5 = 1}\\)</span>.

Let's dive deeper into the math to confirm this. Let's start with what <span class="math-inline">\\(X\\)</span> would have had to be. (We can work with <span class="math-inline">\\(X\\)</span> instead of <span class="math-inline">\\(Z\\)</span> since both have the same column spaces, so projecting onto either column space will give us the same result; <span class="math-inline">\\(X\\)</span> is just easier to work with.) And, let's drop <span class="math-inline">\\(\vec x^{(2)}\\)</span> from <span class="math-inline">\\(X\\)</span>, since including it will prevent <span class="math-inline">\\(X^TX\\)</span> from being invertible while not changing <span class="math-inline">\\(\text{colsp}(X)\\)</span>.

<div class="math-display">
$$
X = \begin{bmatrix} 1 & 1 \\\\ 1 & 1 \\\\ 1 & 0 \\\\ 1 & 1 \\\\ 1 & 0 \end{bmatrix}
$$
</div>

Note that I arbitrarily picked <span class="math-inline">\\(x&#95;1 = x&#95;2 = x&#95;4 = 1\\)</span> and <span class="math-inline">\\(x&#95;3 = x&#95;5 = 0\\)</span>, but we could reverse the 1's and 0's and <span class="math-inline">\\(P\\)</span> would turn out to be the same.

The formula for the projection matrix is <span class="math-inline">\\(P = X (X^TX)^{-1}X^T\\)</span>. I won't include all of the algebra here, but if you work out <span class="math-inline">\\(P = X (X^TX)^{-1}X^T\\)</span>, you'll find that <span class="math-inline">\\(P\\)</span> is indeed the matrix provided in the problem.

Here's one final interpretation of what's going on. Suppose the optimal parameters for this <span class="math-inline">\\(X\\)</span> and some <span class="math-inline">\\(\vec y\\)</span> are <span class="math-inline">\\(\vec w^{\ast} = \begin{bmatrix} w&#95;0^{\ast} \\\\ w&#95;1^{\ast} \end{bmatrix}\\)</span>, which would lead to a hypothesis function of

<div class="math-display">
$$
h(x_i) = w_0^* + w_1^* x_i
$$
</div>

This hypothesis function only returns one of two values:

-   If <span class="math-inline">\\(x&#95;i = 1\\)</span>, then <span class="math-inline">\\(h(1) = w&#95;0^{\ast} + w&#95;1^{\ast}\\)</span>

-   If <span class="math-inline">\\(x&#95;i = 0\\)</span>, then <span class="math-inline">\\(h(0) = w&#95;0^{\ast}\\)</span>

So, <span class="math-inline">\\(w&#95;0^{\ast}\\)</span> is the mean of the <span class="math-inline">\\(y\\)</span>'s when <span class="math-inline">\\(x&#95;i = 0\\)</span>, and <span class="math-inline">\\(w&#95;0^{\ast} + w&#95;1^{\ast}\\)</span> is the mean of the <span class="math-inline">\\(y\\)</span>'s when <span class="math-inline">\\(x&#95;i = 1\\)</span>. This is exactly what we see in the matrix <span class="math-inline">\\(P\\)</span>.
</details>

Recall, <span class="math-inline">\\(Z = \begin{bmatrix} 1 &amp; x&#95;1 - \bar{x} &amp; (x&#95;1 - \bar{x})^2 \\\\ 1 &amp; x&#95;2 - \bar{x} &amp; (x&#95;2 - \bar{x})^2 \\\\ \vdots &amp; \vdots &amp; \vdots \\\\ 1 &amp; x&#95;n - \bar{x} &amp; (x&#95;n - \bar{x})^2 \end{bmatrix} = \begin{bmatrix} | &amp; | &amp; | \\\\ \vec z^{(0)} &amp; \vec z^{(1)} &amp; \vec z^{(2)} \\\\ | &amp; | &amp; | \end{bmatrix}\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Let <span class="math-inline">\\(\vec \beta^{\ast} = \begin{bmatrix} \beta&#95;0^{\ast} \\\\ \beta&#95;1^{\ast} \\\\ \beta&#95;2^{\ast} \end{bmatrix}\\)</span> be a solution to the normal equations for <span class="math-inline">\\(Z\\)</span> and <span class="math-inline">\\(\vec y\\)</span>. Show that

<div class="math-display">
$$
\beta_0^* = \bar{y} - \beta_2^* \sigma_x^2
$$
</div>

where <span class="math-inline">\\(\sigma&#95;x^2 = \frac{1}{n} \sum&#95;{i=1}^n (x&#95;i - \bar{x})^2\\)</span> is the variance of the <span class="math-inline">\\(x\\)</span>'s, and <span class="math-inline">\\(\bar{y}\\)</span> is the mean of the <span class="math-inline">\\(y\\)</span>'s. <em>Hint: Use the fact that <span class="math-inline">\\(\sum&#95;{i = 1}^n (x&#95;i - \bar{x}) = 0\\)</span>. What is the error vector? Is it orthogonal to something useful?</em>

<details markdown="1"><summary>Solution</summary>

The error vector is <span class="math-inline">\\(\vec e = \vec y - Z\vec \beta^{\ast}\\)</span>. As we studied in depth, the error vector is orthogonal to every vector in <span class="math-inline">\\(\text{colsp}(Z)\\)</span>, i.e. every linear combination of the columns of <span class="math-inline">\\(Z\\)</span>. <span class="math-inline">\\(Z\\)</span> has a column of all 1's, so the error vector is orthogonal to that, too.

<div class="math-display">
$$
(\vec y - Z\vec \beta^*) \cdot \vec 1 = 0
$$
</div>

 We'll proceed by expanding <span class="math-inline">\\(Z \vec \beta^{\ast}\\)</span> and then plugging the result into the above. This will allow us to solve for <span class="math-inline">\\(\beta^{\ast}&#95;0\\)</span>.

<div class="math-display">
$$
\begin{align*}
Z\vec \beta^* &= \beta_0^*\vec z^{(0)} + \beta_1^*\vec z^{(1)} + \beta_2^*\vec z^{(2)}
\\\\ &= \beta_0^*\begin{bmatrix} 1 \\\\ 1 \\\\ \vdots \\\\ 1  \end{bmatrix} +  \beta_1^*\begin{bmatrix} x_1 - \bar x_1 \\\\ x_2 - \bar x_2 \\\\ \vdots \\\\ x_n - \bar x_n\end{bmatrix} + \beta_2^*\begin{bmatrix} (x_1 - \bar x_1)^2 \\\\ (x_2 - \bar x_2)^2 \\\\ \vdots \\\\ (x_n - \bar x_n)^2\end{bmatrix}
\\\\ &= \begin{bmatrix} \beta_0^* + \beta_1^*(x_1 - \bar x_1) + \beta_2^*(x_1 - \bar x_1)^2 \\\\ \beta_0^* + \beta_1^*(x_2 - \bar x_2)+ \beta_2^*(x_2 - \bar x_2)^2\\\\ \vdots \\\\ \beta_0^* + \beta_1^*(x_n - \bar x_n) + \beta_2^*(x_n - \bar x_n)^2\end{bmatrix}
\end{align*}
$$
</div>

<div class="math-display">
$$
\begin{align*}
(\vec y - Z\vec \beta^*) \cdot \vec 1 &= 0
\\\\ \sum_{i=1}^{n}\left[y_i - (Z\vec \beta^*)_i\right] &= 0
\\\\ \sum_{i=1}^{n}\left[y_i - \beta_0^* - \beta_1^*(x_i - \bar x_i) - \beta_2^*(x_i - \bar x_i)^2\right] &= 0
\\\\ \underbrace{\sum_{i=1}^{n}y_i}_{n \bar{y}} - \underbrace{\sum_{i=1}^{n}\beta_0^*}_{\text{sum of constant}} - \underbrace{\sum_{i=1}^{n}\beta_1^*(x_i - \bar x_i)}_{0} - \sum_{i=1}^{n}\beta_2^*(x_i - \bar x_i)^2 &= 0
\\\\ n\bar y - n\beta_0^* - n\beta_2^*\sigma_x^2 &= 0
\\\\ n\beta_0^* &= n\bar y - n\beta_2^*\sigma_x^2
\\\\ \beta_0^* &= \boxed{\bar y - \beta_2^*\sigma_x^2}
\end{align*}
$$
</div>

</details>

</div>
</div>

</div>

---

## Problem 5: Ortho\...dontist? <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>

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

<span class="math-inline">\\(r&#95;2 = \boxed{\textbf{}}, \qquad r&#95;3 = \boxed{\textbf{}}\\)</span>

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

## Problem 6: Quadratus Formulus <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">14 pts</span>

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

## Problem 7: Complexity <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">10 pts</span>

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

(2 pts) Congrats on finishing Midterm 2! Here are two free points.

Feel free to draw us a picture about EECS 245 in the box below.
</div>
</div>

</div>

{% endraw %}
