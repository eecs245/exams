---
number: 2
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">9 pts</span> <span class="badge" data-flag="mt1-redemption" style="background-color: #9A3324; color: #FFFFFF; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">MT1 Redemption</span>
points: 9
flags: [mt1-redemption]
has_solution: true
images: []
---

Suppose we fit a simple linear regression model to a dataset of <span class="math-inline">\\(n\\)</span> points, <span class="math-inline">\\((x&#95;1,y&#95;1),(x&#95;2,y&#95;2),\ldots,(x&#95;n,y&#95;n)\\)</span>, by minimizing mean squared error. Let <span class="math-inline">\\(\bar x\\)</span> and <span class="math-inline">\\(\bar y\\)</span> be the means of the <span class="math-inline">\\(x\\)</span>-values and <span class="math-inline">\\(y\\)</span>-values, respectively, and suppose the standard deviations <span class="math-inline">\\(\sigma&#95;x\\)</span> and <span class="math-inline">\\(\sigma&#95;y\\)</span> are both positive. Let

<div class="math-display">
$$
h(x_i)=w_0^*+w_1^*x_i
$$
</div>

 be the best simple linear regression line for the original dataset.

Now, we create a new dataset of <span class="math-inline">\\(n+1\\)</span> points by starting with the original dataset and adding one new point,

<div class="math-display">
$$
(x_{n+1},y_{n+1})=(\bar x,c)
$$
</div>

 where <span class="math-inline">\\(c\\)</span> is a constant. Let

<div class="math-display">
$$
h_{\text{new}}(x_i)=w_0'+w_1'x_i
$$
</div>

 be the best simple linear regression line for the new dataset.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Prove that <span class="math-inline">\\(w&#95;1' = w&#95;1^{\ast}\\)</span>, i.e. that the new slope is the same as the old slope, no matter what <span class="math-inline">\\(c\\)</span> is. <em>Hint: Start with any of the formulas for the optimal slope that involve summations in the numerator and denominator, and separate the sums.</em>

<details markdown="1"><summary>Solution</summary>

The optimal slope for simple linear regression can be written as

<div class="math-display">
$$
w_1^*
=
\frac{\sum_{i=1}^n (x_i-\bar{x})y_i}{\sum_{i=1}^n (x_i-\bar{x}) x_i}
$$
</div>

 as derived in [Chapter 2.3](https://notes.eecs245.org/simple-linear-regression/finding-optimal-parameters/). There are several other equivalent formulas, e.g. with <span class="math-inline">\\(\sum&#95;{i=1}^n (x&#95;i-\bar{x})(y&#95;i-\bar{y})\\)</span> on the numerator, but this one keeps the algebra simplest, as it doesn't require us to think about the new value of <span class="math-inline">\\(\bar y\\)</span>.

For the new dataset, the mean of the <span class="math-inline">\\(x\\)</span>-values is still <span class="math-inline">\\(\bar{x}\\)</span>, since

<div class="math-display">
$$
\bar{x}'=\frac{n\bar{x}+\bar{x}}{n+1}=\bar{x}
$$
</div>

 The denominator of the new slope is therefore

<div class="math-display">
$$
\sum_{i=1}^{n+1}(x_i-\bar{x}')x_i
=
\sum_{i=1}^n(x_i-\bar{x})x_i + (\bar{x}-\bar{x})\bar{x}
=
\sum_{i=1}^n(x_i-\bar{x})x_i
$$
</div>

 The numerator of the new slope is

<div class="math-display">
$$
\begin{align*}
\sum_{i=1}^{n+1}(x_i-\bar{x}')y_i
&=
\sum_{i=1}^{n}(x_i-\bar{x})y_i
+(\bar{x}-\bar{x})c \\\\
&=
\sum_{i=1}^{n}(x_i-\bar{x})y_i
\end{align*}
$$
</div>

So the numerator and denominator in this formula are both unchanged, meaning <span class="math-inline">\\(w&#95;1'=w&#95;1^{\ast}\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> Which of the following expressions is equal to <span class="math-inline">\\(w&#95;0' - w&#95;0^{\ast}\\)</span>, the difference between the new intercept and the old intercept?

<span class="mc-bubble" aria-hidden="true"></span> None of these

<details markdown="1"><summary>Solution</summary>

<span class="mc-bubble" aria-hidden="true"></span> None of these

The intercept of the optimal simple linear regression line is

<div class="math-display">
$$
w_0^* = \bar{y}-w_1^*\bar{x}
$$
</div>

 The new <span class="math-inline">\\(x\\)</span>-mean is still <span class="math-inline">\\(\bar{x}\\)</span>, and part **a)** showed that the new slope is still <span class="math-inline">\\(w&#95;1^{\ast}\\)</span>. The new <span class="math-inline">\\(y\\)</span>-mean is

<div class="math-display">
$$
\bar{y}'=\frac{n\bar{y}+c}{n+1}
$$
</div>

 So,

<div class="math-display">
$$
\begin{align*}
w_0'-w_0^*
&=
(\bar{y}'-w_1^*\bar{x})-(\bar{y}-w_1^*\bar{x}) \\\\
&= \bar{y}'-\bar{y} \\\\
&= \frac{n\bar{y}+c}{n+1}-\bar{y} \\\\
&= \frac{c-\bar{y}}{n+1}
\end{align*}
$$
</div>

</details>

</div>
</div>

</div>
