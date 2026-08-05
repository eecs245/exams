---
number: 9
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">9 pts</span> <span class="badge" data-flag="mt2-redemption" style="background-color: #9A3324; color: #FFFFFF; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">MT2 Redemption</span>
points: 9
flags: [mt2-redemption]
has_solution: true
images: [convexity-counterexample.png]
---

Let <span class="math-inline">\\(\vec a \in \mathbb{R}^2\\)</span> and let

<div class="math-display">
$$
f(\vec x) = \log(\vec a \cdot \vec x)
$$
</div>

 for all vectors <span class="math-inline">\\(\vec x\\)</span> such that <span class="math-inline">\\(\vec a \cdot \vec x &gt; 0\\)</span>; if <span class="math-inline">\\(\vec a \cdot \vec x \leq 0\\)</span>, then <span class="math-inline">\\(f(\vec x)\\)</span> is undefined. Suppose that

<div class="math-display">
$$
\nabla f\left(\begin{bmatrix}2\\\\1\end{bmatrix}\right)
=
\begin{bmatrix}1/5\\\\3/5\end{bmatrix}
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> Which of the following could be <span class="math-inline">\\(\vec a\\)</span>? **Select all** that apply.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix}3\\\\1\end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix}1\\\\3\end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix}-1\\\\-3\end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix}1\\\\2\end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix}5\\\\3\end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix}2\\\\6\end{bmatrix}\\)</span></span></div>

<details markdown="1"><summary>Solution</summary>

<span class="mc-square mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix}2\\\\6\end{bmatrix}\\)</span>

Let

<div class="math-display">
$$
g(\vec{x})=\vec{a}\cdot\vec{x}=a_1x_1+a_2x_2
\qquad\text{and}\qquad
h(u)=\log(u)
$$
</div>

 Then <span class="math-inline">\\(f(\vec{x})=h(g(\vec{x}))\\)</span>. Using the chain rule from [Chapter 8.2](https://notes.eecs245.org/gradients/gradients-matrix-vector-operations/#chain-rule-for-vector-to-scalar-functions),

<div class="math-display">
$$
\nabla f(\vec{x})
=
h'(g(\vec{x}))\nabla g(\vec{x})
$$
</div>

 Now,

<div class="math-display">
$$
h'(u)=\frac{1}{u}
\qquad\text{and}\qquad
\nabla g(\vec{x})=
\begin{bmatrix}a_1\\\\a_2\end{bmatrix}
=\vec{a}
$$
</div>

 so

<div class="math-display">
$$
\nabla f(\vec{x})
=
h'(\vec a \cdot \vec x) \nabla g(\vec{x}) =
\frac{\vec{a}}{\vec{a}\cdot\vec{x}}
$$
</div>

 At <span class="math-inline">\\(\vec{x}=\begin{bmatrix}2\\\\1\end{bmatrix}\\)</span>, this becomes

<div class="math-display">
$$
\frac{\vec{a}}{2a_1+a_2}
=
\begin{bmatrix}1/5\\\\3/5\end{bmatrix}
$$
</div>

 Since <span class="math-inline">\\(f\\)</span> is defined at <span class="math-inline">\\(\begin{bmatrix}2\\\\1\end{bmatrix}\\)</span>, this must mean that <span class="math-inline">\\(\vec a \cdot \vec x\\)</span>, which is equal to <span class="math-inline">\\(2a&#95;1 + a&#95;2\\)</span>, is positive. Multiplying both sides by this positive denominator gives

<div class="math-display">
$$
\vec{a}
=
(2a_1+a_2)
\begin{bmatrix}1/5\\\\3/5\end{bmatrix}
=
\frac{2a_1+a_2}{5}
\begin{bmatrix}1\\\\3\end{bmatrix}
$$
</div>

 This says <span class="math-inline">\\(\vec{a}\\)</span> must be a positive scalar multiple of <span class="math-inline">\\(\begin{bmatrix}1\\\\3\end{bmatrix}\\)</span>. Among the answer choices, the vectors with that form are <span class="math-inline">\\(\begin{bmatrix}1\\\\3\end{bmatrix}\\)</span> and <span class="math-inline">\\(\begin{bmatrix}2\\\\6\end{bmatrix}\\)</span>.

Another way to approach this would be to take the equation

<div class="math-display">
$$
\frac{\vec a}{2a_1+a_2} = \begin{bmatrix}1/5\\\\3/5\end{bmatrix}
$$
</div>

from above, and realize the expression on the right is also equal to <span class="math-inline">\\(\frac{1}{2a&#95;1+a&#95;2} \begin{bmatrix}a&#95;1\\\\a&#95;2\end{bmatrix}\\)</span>, which allows us to set up a system of equations directly for <span class="math-inline">\\(a&#95;1\\)</span> and <span class="math-inline">\\(a&#95;2\\)</span>:

<div class="math-display">
$$
\begin{align*}
\frac{a_1}{2a_1+a_2} &= 1/5 \\\\
\frac{a_2}{2a_1+a_2} &= 3/5
\end{align*}
$$
</div>

Both equations say the same thing: <span class="math-inline">\\(a&#95;2 = 3a&#95;1\\)</span>, i.e. that <span class="math-inline">\\(a&#95;2\\)</span> must be triple <span class="math-inline">\\(a&#95;1\\)</span>, so <span class="math-inline">\\(\vec a\\)</span> is a scalar multiple of <span class="math-inline">\\(\begin{bmatrix}1\\\\3\end{bmatrix}\\)</span>. But, don't forget the added constraint that <span class="math-inline">\\(2a&#95;1 + a&#95;2\\)</span> must be positive.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Suppose we use gradient descent to minimize <span class="math-inline">\\(f(\vec x)\\)</span> using an initial guess of <span class="math-inline">\\(\vec x^{(0)} = \begin{bmatrix} 2 \\\\ 1 \end{bmatrix}\\)</span> and a learning rate of <span class="math-inline">\\(\alpha = 1/2\\)</span>. Find <span class="math-inline">\\(\vec x^{(1)}\\)</span>. Show your work, and write your answer in the box provided. Your answer should be a vector with no variables.

<div class="math-display">
$$
\vec x^{(1)} = \_\_\_\_\_\_
$$
</div>

<details markdown="1"><summary>Solution</summary>

The gradient descent update from [Chapter 8.3](https://notes.eecs245.org/gradients/gradient-descent/) is

<div class="math-display">
$$
\vec{x}^{(1)}
=
\vec{x}^{(0)}-\alpha\nabla f(\vec{x}^{(0)})
$$
</div>

 Here, <span class="math-inline">\\(\vec{x}^{(0)}=\begin{bmatrix}2\\\\1\end{bmatrix}\\)</span>, <span class="math-inline">\\(\alpha=1/2\\)</span>, and <span class="math-inline">\\(\nabla f(\vec{x}^{(0)})=\begin{bmatrix}1/5\\\\3/5\end{bmatrix}\\)</span>. So,

<div class="math-display">
$$
\vec{x}^{(1)}
=
\begin{bmatrix}2\\\\1\end{bmatrix}
-
\frac{1}{2}\begin{bmatrix}1/5\\\\3/5\end{bmatrix}
=
\begin{bmatrix}2\\\\1\end{bmatrix}
-
\begin{bmatrix}1/10\\\\3/10\end{bmatrix}
=
\begin{bmatrix}19/10\\\\7/10\end{bmatrix}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">2 pts</span> This part is unrelated to the previous parts.

Suppose <span class="math-inline">\\(g: \mathbb{R} \to \mathbb{R}\\)</span>. True or false: if <span class="math-inline">\\(g\\)</span> has a global minimum and no local maxima, it must be convex.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> False</span></div>

This is false. For instance, consider

<div class="math-display">
$$
g(x)=x^4+x^3
$$
</div>

 This function has a global minimum, since <span class="math-inline">\\(g(x)\to\infty\\)</span> as <span class="math-inline">\\(x\to\infty\\)</span> and as <span class="math-inline">\\(x\to-\infty\\)</span>. Also,

<div class="math-display">
$$
g'(x)=4x^3+3x^2=x^2(4x+3)
$$
</div>

 The derivative only changes sign at <span class="math-inline">\\(x=-3/4\\)</span>, where it changes from negative to positive, so <span class="math-inline">\\(g\\)</span> has a local minimum and no local maxima. But,

<div class="math-display">
$$
g''(x)=12x^2+6x
$$
</div>

 which is negative for some <span class="math-inline">\\(x\\)</span> values, for instance <span class="math-inline">\\(x=-1/4\\)</span>. So <span class="math-inline">\\(g\\)</span> is not convex. See [Chapter 8.5](https://notes.eecs245.org/gradients/convexity/) for the convexity condition.

<div style="text-align: center;">
<img src="imgs/convexity-counterexample.png" alt="image" style="width: 82%; max-width: 100%;">
</div>
</details>

</div>
</div>

</div>
