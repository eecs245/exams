---
number: 3
title: Spreading Your Wings
heading_suffix: : Spreading Your Wings <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>
points: 12
flags: []
has_solution: true
images: []
---

Consider a dataset of <span class="math-inline">\\(n\\)</span> points, <span class="math-inline">\\((x&#95;1, y&#95;1), (x&#95;2, y&#95;2), \ldots, (x&#95;n, y&#95;n)\\)</span>, where

-   the means of <span class="math-inline">\\(x&#95;1, x&#95;2, \ldots, x&#95;n\\)</span> and <span class="math-inline">\\(y&#95;1, y&#95;2, \ldots, y&#95;n\\)</span> are 15 and 5, respectively

-   the variances of <span class="math-inline">\\(x&#95;1, x&#95;2, \ldots, x&#95;n\\)</span> and <span class="math-inline">\\(y&#95;1, y&#95;2, \ldots, y&#95;n\\)</span> are <span class="math-inline">\\(\sigma&#95;x^2\\)</span> and <span class="math-inline">\\(\sigma&#95;y^2\\)</span>, respectively

-   the correlation coefficient between <span class="math-inline">\\(x&#95;1, x&#95;2, \ldots, x&#95;n\\)</span> and <span class="math-inline">\\(y&#95;1, y&#95;2, \ldots, y&#95;n\\)</span> is <span class="math-inline">\\(r\\)</span>

We define a new set of values, <span class="math-inline">\\(z&#95;1, z&#95;2, \ldots, z&#95;n\\)</span>, as follows:

<div class="math-display">
$$
z_i = 3x_i - y_i, \quad i = 1, 2, \ldots, n
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Suppose we fit a simple linear regression line to the dataset <span class="math-inline">\\((x&#95;1, z&#95;1), (x&#95;2, z&#95;2), \ldots, (x&#95;n, z&#95;n)\\)</span> by minimizing mean squared error. Note that <span class="math-inline">\\(z\\)</span> is the variable being predicted, not <span class="math-inline">\\(y\\)</span>. Let <span class="math-inline">\\(h(x&#95;i)\\)</span> represent the corresponding line.

What is the value of <span class="math-inline">\\(h(15)\\)</span>? Your answer should be a number with no variables.

<span class="math-inline">\\(h(15) =\\)</span> \_\_\_\_\_\_

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(h(15) = 40\\)</span>.

The key fact being assessed here is that the line that minimizes mean squared error always passes through

<div class="math-display">
$$
(\text{mean of input variable}, \text{mean of output variable})
$$
</div>

Normally this is stated as the line passing through the point <span class="math-inline">\\((\bar{x}, \bar{y})\\)</span>, but here the output variable is <span class="math-inline">\\(z\\)</span>, not <span class="math-inline">\\(y\\)</span>.

The mean of <span class="math-inline">\\(z\\)</span> is <span class="math-inline">\\(3 \bar{x} - \bar{y}\\)</span>, as we explored in a homework problem, and this is

<div class="math-display">
$$
3 \bar{x} - \bar{y} = 3(15) - 5 = 40
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">8 pts</span>
<span class="math-inline">\\(\sigma&#95;z^2\\)</span>, the variance of <span class="math-inline">\\(z&#95;1, z&#95;2, \ldots, z&#95;n\\)</span>, can be written in the form <span class="math-inline">\\(\sigma&#95;z^2 = 9 \sigma&#95;x^2 + \sigma&#95;y^2 + C\\)</span>.

1.  What is the value of <span class="math-inline">\\(C\\)</span>?

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(-6 \sigma&#95;x \sigma&#95;y\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(6 \sigma&#95;x \sigma&#95;y\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(-6r \sigma&#95;x \sigma&#95;y\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(6r \sigma&#95;x \sigma&#95;y\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(-6nr \sigma&#95;x \sigma&#95;y\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(6nr \sigma&#95;x \sigma&#95;y\\)</span></span></div>

2.  Show your work in the box below. English explanations are not enough.

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(-6 \sigma&#95;x \sigma&#95;y\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(6 \sigma&#95;x \sigma&#95;y\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(-6r \sigma&#95;x \sigma&#95;y\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(6r \sigma&#95;x \sigma&#95;y\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(-6nr \sigma&#95;x \sigma&#95;y\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(6nr \sigma&#95;x \sigma&#95;y\\)</span></span></div>

We'll find the answer by expanding out the definition of <span class="math-inline">\\(\sigma&#95;z^2\\)</span> and simplifying.

<div class="math-display">
$$
\begin{align*}
\sigma_z^2 &= \frac{1}{n} \sum_{i=1}^n (z_i - \bar{z})^2 \\\\
&= \frac{1}{n} \sum_{i=1}^n (3x_i - y_i - (3\bar{x} - \bar{y}))^2 \\\\
&= \underbrace{\frac{1}{n} \sum_{i=1}^n (3x_i - 3\bar{x} - y_i + \bar{y})^2}_\text{distributed the negative sign and rearranged} \\\\
&= \frac{1}{n} \sum_{i=1}^n \underbrace{(3(x_i - \bar{x}) - (y_i - \bar{y}))^2}_\text{treat this as }(a - b)^2 \\\\
&= \frac{1}{n} \sum_{i=1}^n \left( 9(x_i - \bar{x})^2 - 6(x_i - \bar{x})(y_i - \bar{y}) + (y_i - \bar{y})^2 \right) \\\\
&= 9 \left(\frac{1}{n} \sum_{i=1}^n (x_i - \bar{x})^2 \right) - 6 \left(\frac{1}{n} \sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})\right) + \left(\frac{1}{n} \sum_{i=1}^n (y_i - \bar{y})^2 \right) \\\\
&= 9 \sigma_x^2 + \sigma_y^2 - 6 \left(\frac{1}{n} \sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})\right) \\\\
\end{align*}
$$
</div>

So,

<div class="math-display">
$$
C = -6 \left(\frac{1}{n} \sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})\right)
$$
</div>

But, recall that

<div class="math-display">
$$
r = \frac{1}{n} \sum_{i=1}^n \left( \frac{x_i - \bar{x}}{\sigma_x} \right) \left( \frac{y_i - \bar{y}}{\sigma_y} \right)
$$
</div>

which means that

<div class="math-display">
$$
r \sigma_x \sigma_y = \frac{1}{n} \sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})
$$
</div>

So,

<div class="math-display">
$$
C = -6 \left(\frac{1}{n} \sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})\right) = -6r \sigma_x \sigma_y
$$
</div>

</details>

</div>
</div>

</div>
