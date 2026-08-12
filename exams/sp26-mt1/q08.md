---
number: 8
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">8 pts</span>
points: 8
flags: []
has_solution: true
images: []
---

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

<details markdown="1"><summary>Solution</summary>

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
