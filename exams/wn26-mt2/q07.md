---
number: 7
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">10 pts</span>
points: 10
flags: []
has_solution: true
images: []
---

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
