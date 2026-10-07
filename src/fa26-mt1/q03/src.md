Consider a dataset of <span class="math-inline">\\(n\\)</span> points, <span class="math-inline">\\((x&#95;1,y&#95;1),\ldots,(x&#95;n,y&#95;n)\\)</span>, where not all of the <span class="math-inline">\\(x&#95;i\\)</span> are the same. We'd like to fit a **modified** simple linear regression model whose slope and intercept are forced to be the same:

<div class="math-display">
$$
h(x_i)=w+wx_i
$$
</div>

 The value of <span class="math-inline">\\(w\\)</span> that minimizes mean squared error for this model is

<div class="math-display">
$$
w^*=\frac{\displaystyle\sum_{i=1}^n(1+x_i)y_i}{\displaystyle\sum_{i=1}^n(1+x_i)^2}
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge badge-points">3 pts</span> Suppose:

-   <span class="math-inline">\\(h^{\ast}(x&#95;i)=w^{\ast}+w^{\ast}x&#95;i\\)</span> is the fitted **modified** model, where <span class="math-inline">\\(w^{\ast}\\)</span> minimizes mean squared error.

-   <span class="math-inline">\\(g^{\ast}(x&#95;i)=w&#95;0^{\ast}+w&#95;1^{\ast}x&#95;i\\)</span> is the **regular** simple linear regression model fitted to the same dataset, where <span class="math-inline">\\(w&#95;0^{\ast}\\)</span> and <span class="math-inline">\\(w&#95;1^{\ast}\\)</span> are chosen to minimize mean squared error.

Fill in the <span class="math-inline">\\(\boxed{???}\\)</span> with the relationship that is **guaranteed**:

<div class="math-display">
$$
\frac{1}{n}\sum_{i=1}^n(y_i-g^*(x_i))^2\quad\boxed{???}\quad\frac{1}{n}\sum_{i=1}^n(y_i-h^*(x_i))^2
$$
</div>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(&gt;\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\geq\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(=\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(&lt;\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\leq\\)</span></span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(&gt;\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\geq\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(=\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(&lt;\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(\leq\\)</span></span></div>

The relationship is <span class="math-inline">\\(\boxed{\leq}\\)</span>.

Think of regular simple linear regression as being more flexible: it *can* have the same slope and intercept if that minimizes MSE, and it can have different slope and intercept if that minimizes MSE even further. Anything the modified model can do, the regular model can do, and more. So the regular model's minimum MSE cannot be larger.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge badge-points">6 pts</span> Let <span class="math-inline">\\(r\\)</span> be the correlation coefficient between the <span class="math-inline">\\(x\\)</span>- and <span class="math-inline">\\(y\\)</span>-values, and let <span class="math-inline">\\(\sigma&#95;x\\)</span> and <span class="math-inline">\\(\sigma&#95;y\\)</span> be their standard deviations, respectively. Suppose

<div class="math-display">
$$
r=-\frac35,\qquad \sigma_x=4,\qquad \sigma_y=10
$$
</div>

 Give each answer as a number with no variables. If it is not possible to determine an answer from the information given, write **N/A** in the box.

<ol class="roman">
<li markdown="1">
(3 pts) What is <span class="math-inline">\\(w^{\ast}\\)</span>, the optimal slope for the **modified** simple linear regression model?

   <span class="math-inline">\\(w^{\ast}=\&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>
</li>
<li markdown="1">
(3 pts) What is <span class="math-inline">\\(w&#95;1^{\ast}\\)</span>, the optimal slope for the **regular** simple linear regression model?

   <span class="math-inline">\\(w&#95;1^{\ast}=\&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>

<details markdown="1"><summary>Solution</summary>

**(i)** <span class="math-inline">\\(\boxed{\text{N/A}}\\)</span>. Moving the data changes which modified line fits best, even if its shape, correlation, and standard deviations stay the same. Every modified line <span class="math-inline">\\(y=w+wx\\)</span> passes through <span class="math-inline">\\((-1,0)\\)</span>, so it cannot simply move along with the data.

For example, use <span class="math-inline">\\(x\\)</span>-values <span class="math-inline">\\(-1,-1,7,7\\)</span> and <span class="math-inline">\\(y\\)</span>-values <span class="math-inline">\\(-2,14,-14,2\\)</span> in the left panel. In the right panel, add <span class="math-inline">\\(8\\)</span> to every <span class="math-inline">\\(y\\)</span>-value. Both datasets have <span class="math-inline">\\(r=-3/5\\)</span>, <span class="math-inline">\\(\sigma&#95;x=4\\)</span>, and <span class="math-inline">\\(\sigma&#95;y=10\\)</span>.

![image](imgs/tikz-1daca4940c41.svg)

At <span class="math-inline">\\(x=-1\\)</span>, the prediction is always <span class="math-inline">\\(0\\)</span>, regardless of <span class="math-inline">\\(w\\)</span>. At <span class="math-inline">\\(x=7\\)</span>, the prediction is <span class="math-inline">\\(8w\\)</span>, so the best choice makes <span class="math-inline">\\(8w\\)</span> equal to the mean of the two <span class="math-inline">\\(y\\)</span>-values there. This gives <span class="math-inline">\\(w^{\ast}=-3/4\\)</span> on the left and <span class="math-inline">\\(w^{\ast}=1/4\\)</span> on the right.

**(ii)** For regular simple linear regression,

<div class="math-display">
$$
w_1^*=r\frac{\sigma_y}{\sigma_x}
=-\frac35\cdot\frac{10}{4}=\boxed{-\frac32}
$$
</div>

</details>
</li>
</ol>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge badge-points">7 pts</span> Show that <span class="math-inline">\\(w^{\ast}\\)</span>, the value of <span class="math-inline">\\(w\\)</span> that minimizes mean squared error for the modified simple linear regression model <span class="math-inline">\\(h(x&#95;i)=w+wx&#95;i\\)</span>, is

<div class="math-display">
$$
w^*=\frac{\displaystyle\sum_{i=1}^n(1+x_i)y_i}{\displaystyle\sum_{i=1}^n(1+x_i)^2}
$$
</div>

<details markdown="1"><summary>Solution</summary>

The mean squared error of the modified model is

<div class="math-display">
$$
R(w)=\frac1n\sum_{i=1}^n\bigl(y_i-w(1+x_i)\bigr)^2
$$
</div>

 Taking the derivative with respect to <span class="math-inline">\\(w\\)</span> gives

<div class="math-display">
$$
R'(w)=-\frac2n\sum_{i=1}^n(1+x_i)\bigl(y_i-w(1+x_i)\bigr)
$$
</div>

 Set the derivative equal to zero and solve for <span class="math-inline">\\(w\\)</span>:

<div class="math-display">
$$
\begin{align*}
\sum_{i=1}^n(1+x_i)y_i-w\sum_{i=1}^n(1+x_i)^2&=0\\\\
w\sum_{i=1}^n(1+x_i)^2&=\sum_{i=1}^n(1+x_i)y_i\\\\
w^*&=\boxed{\frac{\displaystyle\sum_{i=1}^n(1+x_i)y_i}{\displaystyle\sum_{i=1}^n(1+x_i)^2}}
\end{align*}
$$
</div>

The objective is a quadratic in <span class="math-inline">\\(w\\)</span> with a positive coefficient on <span class="math-inline">\\(w^2\\)</span>, so this critical point is its minimum. **A second derivative test is not necessary.**
</details>

</div>
</div>

</div>
