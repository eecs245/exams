---
number: 8
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">9 pts</span> <span class="badge" data-flag="mt2-redemption" style="background-color: #9A3324; color: #FFFFFF; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">MT2 Redemption</span>
points: 9
flags: [mt2-redemption]
has_solution: true
images: []
---

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
