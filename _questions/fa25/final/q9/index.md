---
number: 9
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">18 pts</span>
points: 18
flags: []
has_solution: true
images: []
---

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
