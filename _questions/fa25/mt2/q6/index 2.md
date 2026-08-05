---
number: 6
title: Quadratus Formulus
heading_suffix: : Quadratus Formulus <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">14 pts</span>
points: 14
flags: []
has_solution: true
images: []
---

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
