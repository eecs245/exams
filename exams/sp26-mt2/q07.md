---
number: 7
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">15 pts</span>
points: 15
flags: []
has_solution: true
images: []
---

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
