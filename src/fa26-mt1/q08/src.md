Consider the vectors <span class="math-inline">\\(\vec v&#95;1, \vec v&#95;2, \ldots, \vec v&#95;d\in\mathbb R^n\\)</span>, where <span class="math-inline">\\(d\geq 2\\)</span>. For some scalar <span class="math-inline">\\(t\in\mathbb R\\)</span>, define:

<div class="math-display">
$$
\vec s=t(\vec v_1+\cdots+\vec v_d)
$$
</div>

Then, for each <span class="math-inline">\\(i=1, 2, \ldots,d\\)</span>, define

<div class="math-display">
$$
\vec u_i = \vec v_i - \vec s
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge badge-points">5 pts</span> For this part only, suppose <span class="math-inline">\\(d=3\\)</span>. Find an expression for <span class="math-inline">\\(\vec u&#95;1 + \vec u&#95;2 + \vec u&#95;3\\)</span> in terms of <span class="math-inline">\\(t\\)</span>, <span class="math-inline">\\(\vec v&#95;1\\)</span>, <span class="math-inline">\\(\vec v&#95;2\\)</span>, and <span class="math-inline">\\(\vec v&#95;3\\)</span>. Note that your answer **cannot** involve <span class="math-inline">\\(\vec s\\)</span>.

<details markdown="1"><summary>Solution</summary>

For <span class="math-inline">\\(d=3\\)</span>, <span class="math-inline">\\(\vec s=t(\vec v&#95;1+\vec v&#95;2+\vec v&#95;3)\\)</span>. Therefore,

<div class="math-display">
$$
\begin{align*}
\vec u_1+\vec u_2+\vec u_3
&=(\vec v_1-\vec s)+(\vec v_2-\vec s)+(\vec v_3-\vec s)\\\\
&=\vec v_1+\vec v_2+\vec v_3-3t(\vec v_1+\vec v_2+\vec v_3)\\\\
&=\boxed{(1-3t)(\vec v_1+\vec v_2+\vec v_3)}
\end{align*}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge badge-points">4 pts</span> Find a value of <span class="math-inline">\\(t\\)</span> for which <span class="math-inline">\\(\vec u&#95;1,\ldots,\vec u&#95;d\\)</span> are **guaranteed** to be linearly dependent, regardless of the original vectors. Give your answer as an expression in terms of <span class="math-inline">\\(n\\)</span>, <span class="math-inline">\\(d\\)</span>, and/or constants.

<details markdown="1"><summary>Solution</summary>

As in part **a)**, observe what happens when we sum all of the <span class="math-inline">\\(\vec u&#95;i\\)</span>. This is a linear combination of the <span class="math-inline">\\(\vec u&#95;i\\)</span>, with every coefficient equal to <span class="math-inline">\\(1\\)</span>:

<div class="math-display">
$$
\begin{align*}
\vec u_1+\cdots+\vec u_d
&=(\vec v_1-\vec s)+\cdots+(\vec v_d-\vec s)\\\\
&=\vec v_1+\cdots+\vec v_d-dt(\vec v_1+\cdots+\vec v_d)\\\\
&=(1-dt)(\vec v_1+\cdots+\vec v_d)
\end{align*}
$$
</div>

To make this equal to <span class="math-inline">\\(\vec0\\)</span> regardless of the original vectors, set

<div class="math-display">
$$
1-dt=0
\quad\Longrightarrow\quad
\boxed{t=\frac1d}
$$
</div>

 For this value of <span class="math-inline">\\(t\\)</span>, the sum is <span class="math-inline">\\(\vec0\\)</span>. Since the coefficients in this linear combination are all <span class="math-inline">\\(1\\)</span>, they are not all zero. By the definition of linear independence, the <span class="math-inline">\\(\vec u&#95;i\\)</span> are therefore linearly dependent.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge badge-points">2 pts</span> Suppose <span class="math-inline">\\(t&gt;0\\)</span>. Fill in the <span class="math-inline">\\(\boxed{???}\\)</span> with the relationship that is **guaranteed**:

<div class="math-display">
$$
t(\lVert\vec v_1\rVert+\lVert\vec v_2\rVert+\cdots+\lVert\vec v_d\rVert)
\quad\boxed{???}\quad
\lVert\vec s\rVert
$$
</div>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(&gt;\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\geq\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(=\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(&lt;\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\leq\\)</span></span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(&gt;\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(\geq\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(=\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(&lt;\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\leq\\)</span></span></div>

Since <span class="math-inline">\\(t&gt;0\\)</span>, the triangle inequality gives

<div class="math-display">
$$
t(\lVert\vec v_1\rVert+\cdots+\lVert\vec v_d\rVert)
\geq t\lVert\vec v_1+\cdots+\vec v_d\rVert
=\lVert\vec s\rVert
$$
</div>

 The guaranteed relationship is <span class="math-inline">\\(\boxed{\geq}\\)</span>. Equality can occur, for example, when all the original vectors are the same nonzero vector, so a strict inequality is not guaranteed.
</details>
</div>
</div>

</div>
