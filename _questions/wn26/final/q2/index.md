---
number: 2
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">13 pts</span> <span class="badge" data-flag="mt1-redemption" style="background-color: #9A3324; color: #FFFFFF; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">MT1 Redemption</span>
points: 13
flags: [mt1-redemption]
has_solution: true
images: []
---

Suppose a dataset of <span class="math-inline">\\(n\\)</span> points, <span class="math-inline">\\((x&#95;1, y&#95;1), (x&#95;2, y&#95;2), \ldots, (x&#95;n, y&#95;n)\\)</span>, has the following properties:

<div class="math-display">
$$
\text{mean of }y\text{-values} = \bar y = 11,
\qquad
\text{standard deviation of }x\text{-values} = \sigma_x = 2,
\qquad
\sigma_y = 6
$$
</div>

 The simple linear regression line that minimizes mean squared error for predicting <span class="math-inline">\\(y&#95;i\\)</span> from <span class="math-inline">\\(x&#95;i\\)</span> is

<div class="math-display">
$$
h(x_i) = 15 - x_i
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> What is <span class="math-inline">\\(\bar x\\)</span>, the mean of the <span class="math-inline">\\(x\\)</span>-values? Give your answer as a number with no variables.

<span class="math-inline">\\(\bar x = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>

<details markdown="1"><summary>Solution</summary>

The regression line must pass through <span class="math-inline">\\((\bar x, \bar y)\\)</span>, so

<div class="math-display">
$$
11 = 15 - \bar x
$$
</div>

 This gives

<div class="math-display">
$$
\bar x = \boxed{4}
$$
</div>

</details>

Now, consider a new dataset, <span class="math-inline">\\((t&#95;1, z&#95;1), (t&#95;2, z&#95;2), \ldots, (t&#95;n, z&#95;n)\\)</span>, defined by <span class="math-inline">\\(t&#95;i = 5 - x&#95;i\\)</span> and <span class="math-inline">\\(z&#95;i = 2y&#95;i - 1\\)</span>.

Let <span class="math-inline">\\(g(t&#95;i) = \beta&#95;0^{\ast} + \beta&#95;1^{\ast} t&#95;i\\)</span> be the best simple linear regression line for predicting <span class="math-inline">\\(z&#95;i\\)</span> from <span class="math-inline">\\(t&#95;i\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Find <span class="math-inline">\\(\beta&#95;0^{\ast}\\)</span>, the intercept of the best simple linear regression line for predicting <span class="math-inline">\\(z&#95;i\\)</span> from <span class="math-inline">\\(t&#95;i\\)</span>. Show your work, and write your final answer in the box provided. Your answer should be a number with no variables.

<div class="math-display">
$$
\beta_0^* = \_\_\_\_\_\_
$$
</div>

<details markdown="1"><summary>Solution</summary>

First, use the original regression line to find the original correlation, which we'll call <span class="math-inline">\\(r&#95;{xy}\\)</span>. The slope is <span class="math-inline">\\(-1\\)</span>, so

<div class="math-display">
$$
-1 = r_{xy} \cdot \frac{\sigma_y}{\sigma_x}
= r \cdot \frac{6}{2}
= 3r_{xy}
$$
</div>

 This gives

<div class="math-display">
$$
r_{xy} = -\frac{1}{3}
$$
</div>

Now, what is <span class="math-inline">\\(r&#95;{tz}\\)</span>? Replacing <span class="math-inline">\\(x&#95;i\\)</span> with <span class="math-inline">\\(t&#95;i=5-x&#95;i\\)</span> flips the sign of the correlation, while replacing <span class="math-inline">\\(y&#95;i\\)</span> with <span class="math-inline">\\(z&#95;i=2y&#95;i-1\\)</span> keeps the sign the same. So the correlation between <span class="math-inline">\\(t&#95;i\\)</span> and <span class="math-inline">\\(z&#95;i\\)</span> is

<div class="math-display">
$$
r_{tz} = \frac{1}{3}
$$
</div>

Also,

<div class="math-display">
$$
\bar t = 5-\bar x = 5 - 4 = 1,
\qquad
\bar z = 2\bar y - 1 = 2 \cdot 11 - 1 = 21
$$
</div>



<div class="math-display">
$$
\sigma_t = \sigma_x = 2,
\qquad
\sigma_z = |2| \sigma_y = 2 \cdot 6 = 12
$$
</div>

Where did these facts come from? In general, if <span class="math-inline">\\(x&#95;1, x&#95;2, ..., x&#95;n\\)</span> have a mean of <span class="math-inline">\\(\bar x\\)</span> and a standard deviation of <span class="math-inline">\\(\sigma&#95;x\\)</span>, then <span class="math-inline">\\(a x&#95;1 + b, a x&#95;2 + b, ..., a x&#95;n + b\\)</span> have a mean of <span class="math-inline">\\(a \bar x + b\\)</span> and a standard deviation of <span class="math-inline">\\(|a| \sigma&#95;x\\)</span>. This was discussed in an early homework problem.

The new slope is, then

<div class="math-display">
$$
\beta_1^* = r_{tz} \cdot \frac{\sigma_z}{\sigma_t} = r_{tz} \cdot \frac{12}{2} = 6 r_{tz} = 6 \cdot \frac{1}{3} = 2
$$
</div>

 Since the new regression line passes through <span class="math-inline">\\((\bar t,\bar z) = (1, 21)\\)</span>, we have

<div class="math-display">
$$
\bar z = \beta_0^* + \beta_1^* \bar t \implies 21 = \beta_0^* + 2 \cdot 1 \implies \beta_0^* = 19
$$
</div>

Thus, <span class="math-inline">\\(\boxed{\beta&#95;0^{\ast} = 19}\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Let <span class="math-inline">\\(M\\)</span> be the mean squared error of the model <span class="math-inline">\\(h(x&#95;i) = 15 - x&#95;i\\)</span>'s predictions on the dataset <span class="math-inline">\\((x&#95;1, y&#95;1), (x&#95;2, y&#95;2), \ldots, (x&#95;n, y&#95;n)\\)</span>, and <span class="math-inline">\\(M'\\)</span> be the mean squared error of the model <span class="math-inline">\\(g(t&#95;i) = \beta&#95;0^{\ast} + \beta&#95;1^{\ast} t&#95;i\\)</span>'s predictions on the dataset <span class="math-inline">\\((t&#95;1, z&#95;1), (t&#95;2, z&#95;2), \ldots, (t&#95;n, z&#95;n)\\)</span>.

What is the value of the fraction <span class="math-inline">\\(\frac{M}{M'}\\)</span>? *If it's not clear, <span class="math-inline">\\(M'\\)</span> is on the denominator.*

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1/5\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1/4\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1/2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(4\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(5\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Impossible to tell</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1/5\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1/4\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1/2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(4\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(5\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Impossible to tell</span></div>

The intuitive answer is that since we've stretched out the <span class="math-inline">\\(y\\)</span>-values by a factor of <span class="math-inline">\\(2\\)</span>, the mean squared error is multiplied by a factor of <span class="math-inline">\\(4\\)</span>, so the fraction <span class="math-inline">\\(\frac{M}{M'}\\)</span> is <span class="math-inline">\\(\frac{1}{4}\\)</span>.

Let's show this a bit more formally. First, note that

<div class="math-display">
$$
M = \frac{1}{n} \sum_{i=1}^n (y_i - (15 - x_i))^2
$$
</div>

Can we write <span class="math-inline">\\(M'\\)</span> in terms of <span class="math-inline">\\(M\\)</span>? Yes, we can.

<div class="math-display">
$$
M' = \frac{1}{n} \sum_{i=1}^n (z_i - (\beta_0^* + \beta_1^* t_i))^2
$$
</div>

Using the fact that <span class="math-inline">\\(z&#95;i = 2y&#95;i - 1\\)</span>, <span class="math-inline">\\(t&#95;i = 5 - x&#95;i\\)</span>, <span class="math-inline">\\(\beta&#95;0^{\ast} = 19\\)</span>, and <span class="math-inline">\\(\beta&#95;1^{\ast} = 2\\)</span> gives

<div class="math-display">
$$
\begin{align*}
M' &= \frac{1}{n} \sum_{i=1}^n \big(z_i - (\beta_0^* + \beta_1^* t_i)\big)^2 \\\\
&= \frac{1}{n} \sum_{i=1}^n \big((2y_i - 1) - (19 + 2 (5 - x_i))\big)^2 \\\\
&= \frac{1}{n} \sum_{i=1}^n \big((2y_i - 1) - (19 + 10 - 2x_i)\big)^2 \\\\
&= \frac{1}{n} \sum_{i=1}^n \big(2y_i - 30 + 2x_i\big)^2 \\\\
&= \frac{1}{n} \sum_{i=1}^n \big(2(y_i - 15 + x_i)\big)^2 \\\\
&= 4 \cdot \frac{1}{n} \sum_{i=1}^n (y_i - (15 - x_i))^2 \\\\
&= 4M
\end{align*}
$$
</div>

So, since <span class="math-inline">\\(M' = 4M\\)</span>,

<div class="math-display">
$$
\frac{M}{M'} = \frac{M}{4M} = \boxed{\frac{1}{4}}
$$
</div>

</details>

</div>
</div>

</div>
