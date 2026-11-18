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

**False.** Consider

<div class="math-display">
$$
\vec u=\begin{bmatrix}1/\sqrt2\\\\0\end{bmatrix},\qquad
    \vec v=\begin{bmatrix}-1/\sqrt2\\\\0\end{bmatrix}
$$
</div>

 Both satisfy <span class="math-inline">\\(\vec x^TA\vec x=1\\)</span>, so <span class="math-inline">\\(f(\vec u)=f(\vec v)=0\\)</span>.

   Their midpoint is <span class="math-inline">\\(\vec0\\)</span>, but

<div class="math-display">
$$
f\left(\frac{\vec u+\vec v}{2}\right)=f(\vec0)=1>
    \frac{f(\vec u)+f(\vec v)}{2}=0
$$
</div>

 This violates the defining inequality for a convex function.
</details>
</li>
<li markdown="1">
(2 pts) <span class="math-inline">\\(f\\)</span> attains its global minimum at exactly one vector.
<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> False</span></div>

**False.** Since <span class="math-inline">\\(f\\)</span> is a square, it is always nonnegative. The two vectors from part (i) both attain <span class="math-inline">\\(0\\)</span>, so the global minimizer is not unique.
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
