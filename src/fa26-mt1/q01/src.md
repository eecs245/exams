Consider two datasets, <span class="math-inline">\\(A=\lbrace y&#95;1,y&#95;2,\ldots,y&#95;n\rbrace \\)</span> and <span class="math-inline">\\(B=\lbrace z&#95;1,z&#95;2,\ldots,z&#95;m\rbrace \\)</span>. Let <span class="math-inline">\\(R&#95;A(w)\\)</span> and <span class="math-inline">\\(R&#95;B(w)\\)</span> represent the mean squared errors of the constant prediction <span class="math-inline">\\(w\\)</span> on datasets <span class="math-inline">\\(A\\)</span> and <span class="math-inline">\\(B\\)</span>, respectively:

<div class="math-display">
$$
R_A(w)=\frac{1}{n}\sum_{i=1}^n(y_i-w)^2=(7-w)^2+5,\qquad
R_B(w)=(13-w)^2+17
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge badge-points">3 pts</span> Which dataset below could be <span class="math-inline">\\(A\\)</span>?

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 7, 8, 10</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 4, 6, 8, 10</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 5, 6, 7, 8, 9</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 2, 3, 6, 7, 8</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 7, 8, 10</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> 4, 6, 8, 10</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 5, 6, 7, 8, 9</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 2, 3, 6, 7, 8</span></div>

Recall that the mean squared error of a constant prediction can be written as

<div class="math-display">
$$
R_A(w)=(w-\bar y)^2+\sigma_y^2
$$
</div>

 So, the dataset must have a mean of <span class="math-inline">\\(7\\)</span> and a variance of <span class="math-inline">\\(5\\)</span>. The dataset <span class="math-inline">\\(\boxed{4,6,8,10}\\)</span> satisfies both requirements:

<div class="math-display">
$$
\bar y=\frac{4+6+8+10}{4}=7,\qquad
\sigma_y^2=\frac{9+1+1+9}{4}=5
$$
</div>

 The dataset <span class="math-inline">\\(5,6,7,8,9\\)</span> also has a mean of <span class="math-inline">\\(7\\)</span>, but its variance is <span class="math-inline">\\(2\\)</span>, so it does not work.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge badge-points">3 pts</span> Let <span class="math-inline">\\(S(w)\\)</span> be the **sum** of the two mean squared error functions:

<div class="math-display">
$$
S(w)=R_A(w)+R_B(w)
$$
</div>

 Find <span class="math-inline">\\(w^{\ast}\\)</span>, the value of <span class="math-inline">\\(w\\)</span> that minimizes <span class="math-inline">\\(S(w)\\)</span>. Give your answer as a number with no variables.

<details markdown="1"><summary>Solution</summary>

Add the two mean squared errors and take the derivative:

<div class="math-display">
$$
\begin{align*}
S(w)&=(7-w)^2+5+(13-w)^2+17\\\\
\frac{\mathrm d}{\mathrm dw}S(w)&=2(w-7)+2(w-13)=4w-40
\end{align*}
$$
</div>

Setting this equal to zero gives <span class="math-inline">\\(\boxed{w^{\ast}=10}\\)</span>. The derivative is negative below <span class="math-inline">\\(10\\)</span> and positive above <span class="math-inline">\\(10\\)</span>, so this is the minimizer.

This is the same kind of optimization we used to minimize mean squared error: the optimal prediction balances the two squared deviations. The constants <span class="math-inline">\\(+5\\)</span> and <span class="math-inline">\\(+17\\)</span> disappear when we take the derivative, so they do not affect the minimizer.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge badge-points">6 pts</span> Let <span class="math-inline">\\(M(w)\\)</span> return the **larger** of the two mean squared error functions:

<div class="math-display">
$$
M(w)=\max(R_A(w),R_B(w))
$$
</div>

 Find <span class="math-inline">\\(w^{\ast}\\)</span>, the value of <span class="math-inline">\\(w\\)</span> that minimizes <span class="math-inline">\\(M(w)\\)</span>. Give your answer as a number with no variables. <em>Hint: Draw a picture --- a clearly annotated picture, accompanied by some algebra, is sufficient justification.</em>

<details markdown="1"><summary>Solution</summary>

First, find where the two curves intersect:

<div class="math-display">
$$
\begin{align*}
(w-7)^2+5&=(w-13)^2+17\\\\
w^2-14w+54&=w^2-26w+186\\\\
12w&=132\\\\
w&=11
\end{align*}
$$
</div>

Since <span class="math-inline">\\(R&#95;A(w)-R&#95;B(w)=12(w-11)\\)</span>, when <span class="math-inline">\\(w&gt;11\\)</span>, we have <span class="math-inline">\\(R&#95;A(w)&gt;R&#95;B(w)\\)</span>, so <span class="math-inline">\\(M(w)\\)</span> returns <span class="math-inline">\\(R&#95;A(w)\\)</span>. Otherwise, <span class="math-inline">\\(M(w)\\)</span> returns <span class="math-inline">\\(R&#95;B(w)\\)</span>; at <span class="math-inline">\\(w=11\\)</span>, the two are equal. Thus,

<div class="math-display">
$$
M(w)=\begin{cases}
R_B(w),&w\leq11\\\\
R_A(w),&w\geq11
\end{cases}
$$
</div>

 <span class="math-inline">\\(R&#95;B\\)</span> is decreasing for <span class="math-inline">\\(w&lt;11\\)</span>, since its vertex is at <span class="math-inline">\\(13\\)</span>. <span class="math-inline">\\(R&#95;A\\)</span> is increasing for <span class="math-inline">\\(w&gt;11\\)</span>, since its vertex is at <span class="math-inline">\\(7\\)</span>. Therefore, <span class="math-inline">\\(M\\)</span> decreases up to <span class="math-inline">\\(11\\)</span> and increases after <span class="math-inline">\\(11\\)</span>, giving <span class="math-inline">\\(\boxed{w^{\ast}=11}\\)</span> and <span class="math-inline">\\(M(11)=21\\)</span>.

![image](imgs/tikz-bed4cd72e345.svg)
</details>

</div>
</div>

</div>
