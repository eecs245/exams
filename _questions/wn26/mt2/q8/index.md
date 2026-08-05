---
number: 8
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">11 pts</span>
points: 11
flags: []
has_solution: true
images: []
---

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
