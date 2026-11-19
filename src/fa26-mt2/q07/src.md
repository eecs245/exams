Let <span class="math-inline">\\(\vec x\in\mathbb R^2\\)</span>, and consider

<div class="math-display">
$$
A=\begin{bmatrix}2&1\\\\1&2\end{bmatrix},\qquad
f(\vec x)=\left(\vec x^TA\vec x-1\right)^2
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge badge-points">6 pts</span>
<ol class="roman">
<li markdown="1">
(2 pts) Which of the following is the fully simplified expression for <span class="math-inline">\\(\nabla f(\vec x)\\)</span>?

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(2(\vec x^TA\vec x-1)A\vec x\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(4(\vec x^TA\vec x-1)\vec x\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(4(\vec x^TA\vec x-1)A\vec x\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(4(\vec x^TA\vec x)A\vec x\\)</span></span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(2(\vec x^TA\vec x-1)A\vec x\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(4(\vec x^TA\vec x-1)\vec x\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(4(\vec x^TA\vec x-1)A\vec x\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(4(\vec x^TA\vec x)A\vec x\\)</span></span></div>

   The **third expression** is correct.
</details>
</li>
<li markdown="1">
(4 pts) Justify your answer.

<details markdown="1"><summary>Solution</summary>

   Let <span class="math-inline">\\(g(\vec x)=\vec x^TA\vec x-1\\)</span>, so <span class="math-inline">\\(f(\vec x)=g(\vec x)^2\\)</span>. Since <span class="math-inline">\\(A\\)</span> is symmetric,

<div class="math-display">
$$
\nabla g(\vec x)=(A+A^T)\vec x=2A\vec x
$$
</div>

 The chain rule gives

<div class="math-display">
$$
\boxed{\nabla f(\vec x)=2g(\vec x)\nabla g(\vec x)=4(\vec x^TA\vec x-1)A\vec x}
$$
</div>

</details>
</li>
</ol>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge badge-points">4 pts</span> Identify whether each statement is true or false. <em>Hint: There is no need to think about second partial derivatives.</em>

<ol class="roman">
<li markdown="1">
(2 pts) <span class="math-inline">\\(f\\)</span> is convex.
<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> False</span></div>

**False.** From part (a), <span class="math-inline">\\(\nabla f(\vec x)=4(\vec x^TA\vec x-1)A\vec x\\)</span>. Since <span class="math-inline">\\(A\\)</span> is invertible, <span class="math-inline">\\(A\vec x=\vec 0\\)</span> only when <span class="math-inline">\\(\vec x=\vec 0\\)</span>. The gradient is zero in two cases:

-   Since <span class="math-inline">\\(f(\vec x)=(\vec x^TA\vec x-1)^2\\)</span> is a square and can equal zero, its minimum value is <span class="math-inline">\\(0\\)</span>. Every <span class="math-inline">\\(\vec x\\)</span> satisfying <span class="math-inline">\\(\vec x^TA\vec x=1\\)</span> is a global minimizer, and there are infinitely many such vectors. This also explains why (ii) is false.

-   When <span class="math-inline">\\(\vec x=\vec 0\\)</span>, the gradient is also zero, but <span class="math-inline">\\(f(\vec 0)=1\\)</span>. To classify this point, try a small step away from the origin, such as <span class="math-inline">\\(\vec x=\begin{bmatrix}0\\\\0.1\end{bmatrix}\\)</span>. Then <span class="math-inline">\\(\vec x^TA\vec x=2(0.1)^2=0.02\\)</span>, so <span class="math-inline">\\(f(\vec x)=(0.02-1)^2=0.9604&lt;1\\)</span>. In fact, <span class="math-inline">\\(\vec x^TA\vec x=x&#95;1^2+x&#95;2^2+(x&#95;1+x&#95;2)^2\\)</span> is positive for every nonzero <span class="math-inline">\\(\vec x\\)</span> and tends to zero near the origin. Hence <span class="math-inline">\\(0&lt;\vec x^TA\vec x&lt;1\\)</span> for every sufficiently small nonzero <span class="math-inline">\\(\vec x\\)</span>, and <span class="math-inline">\\(f(\vec x)&lt;f(\vec 0)\\)</span>. The origin is a strict local maximum, which rules out convexity.

   To see the contradiction directly, convexity would require

<div class="math-display">
$$
f((1-t)\vec x+t\vec y)\leq (1-t)f(\vec x)+tf(\vec y)
    \qquad\text{for every }t\in[0,1].
$$
</div>

 Take a sufficiently small nonzero <span class="math-inline">\\(\vec x\\)</span>, set <span class="math-inline">\\(\vec y=-\vec x\\)</span>, and take <span class="math-inline">\\(t=1/2\\)</span>. The left side is <span class="math-inline">\\(f(\vec 0)=1\\)</span>, while the right side is the average of two values strictly below <span class="math-inline">\\(1\\)</span>.
</details>
</li>
<li markdown="1">
(2 pts) <span class="math-inline">\\(f\\)</span> attains its global minimum at exactly one vector.
<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> False</span></div>

**False.** As discussed in (i), <span class="math-inline">\\(f(\vec x)\\)</span> is minimized when <span class="math-inline">\\(\vec x^TA\vec x-1=0\\)</span>. Expanding with the given matrix gives

<div class="math-display">
$$
\vec x^TA\vec x=2x_1^2+2x_1x_2+2x_2^2.
$$
</div>

 For example, <span class="math-inline">\\(\begin{bmatrix}1/\sqrt{2}\\\\0\end{bmatrix}\\)</span> and <span class="math-inline">\\(\begin{bmatrix}-1/\sqrt{2}\\\\0\end{bmatrix}\\)</span> both make this expression equal to <span class="math-inline">\\(1\\)</span>. In fact, for any nonzero direction <span class="math-inline">\\(\vec u\\)</span>, the vector <span class="math-inline">\\(\vec u/\sqrt{\vec u^TA\vec u}\\)</span> does too. There are infinitely many global minimizers.

   To see the shape in retrospect, you can [view the graph in Desmos](https://www.desmos.com/3d/8uyka4tjla).

<iframe src="https://www.desmos.com/3d/8uyka4tjla?embed" title="Interactive 3D graph in Desmos" width="720" height="440" style="max-width:100%;border:0" loading="lazy" allowfullscreen></iframe>
</details>
</li>
</ol>

Recall, <span class="math-inline">\\(\vec x\in\mathbb R^2\\)</span> and

<div class="math-display">
$$
A=\begin{bmatrix}2&1\\\\1&2\end{bmatrix},\qquad
f(\vec x)=\left(\vec x^TA\vec x-1\right)^2
$$
</div>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge badge-points">8 pts</span> We run gradient descent on <span class="math-inline">\\(f\\)</span> twice, starting from the **same** unknown vector <span class="math-inline">\\(\vec x^{(0)}\\)</span>.

-   With step size <span class="math-inline">\\(\alpha=\frac14\\)</span>, the first iteration gives <span class="math-inline">\\(\vec x^{(1)}=\frac14\begin{bmatrix}-14\\\\1\end{bmatrix}\\)</span>.

-   With step size <span class="math-inline">\\(\alpha=\frac34\\)</span>, the first iteration gives <span class="math-inline">\\(\vec x^{(1)}=\frac14\begin{bmatrix}-54\\\\11\end{bmatrix}\\)</span>.

Find <span class="math-inline">\\(\vec x^{(0)}\\)</span>. Your answer should be a vector with no variables. You can answer this part without using your answer to part (a).

<details markdown="1"><summary>Solution</summary>

Let <span class="math-inline">\\(\vec g=\nabla f(\vec x^{(0)})\\)</span>. Both runs have the same gradient at their starting point. The update rule gives

<div class="math-display">
$$
\vec x^{(0)}-\frac14\vec g=\frac14\begin{bmatrix}-14\\\\1\end{bmatrix},\qquad
\vec x^{(0)}-\frac34\vec g=\frac14\begin{bmatrix}-54\\\\11\end{bmatrix}
$$
</div>

 Multiply the first equation by <span class="math-inline">\\(3\\)</span> and subtract the second to eliminate <span class="math-inline">\\(\vec g\\)</span>:

<div class="math-display">
$$
2\vec x^{(0)}=\frac14\left(3\begin{bmatrix}-14\\\\1\end{bmatrix}-\begin{bmatrix}-54\\\\11\end{bmatrix}\right)
=\begin{bmatrix}3\\\\-2\end{bmatrix}
$$
</div>

 Therefore,

<div class="math-display">
$$
\boxed{\vec x^{(0)}=\begin{bmatrix}3/2\\\\-1\end{bmatrix}}
$$
</div>

</details>
</div>
</div>

</div>
