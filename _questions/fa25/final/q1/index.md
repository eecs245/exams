---
number: 1
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">10 pts</span> <span class="badge" data-flag="mt1-redemption" style="background-color: #9A3324; color: #FFFFFF; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">MT1 Redemption</span>
points: 10
flags: [mt1-redemption]
has_solution: true
images: []
---

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Suppose we'd like to find the optimal constant prediction, <span class="math-inline">\\(w^{\ast}\\)</span>, for the constant model <span class="math-inline">\\(h(x&#95;i) = w\\)</span>, given a dataset of <span class="math-inline">\\(n\\)</span> values <span class="math-inline">\\(y&#95;1, y&#95;2, \ldots, y&#95;n\\)</span>. To do so, we minimize mean Bursley error, defined as

<div class="math-display">
$$
R_{\text{B}}(w) = \frac{1}{n} \sum_{i=1}^n | 2y_i - w |^2
$$
</div>

Suppose the mean of <span class="math-inline">\\(y&#95;1, y&#95;2, \ldots, y&#95;n\\)</span> is 20 and the median of <span class="math-inline">\\(y&#95;1, y&#95;2, \ldots, y&#95;n\\)</span> is 30.

Which value of <span class="math-inline">\\(w^{\ast}\\)</span> minimizes <span class="math-inline">\\(R&#95;{\text{B}}(w)\\)</span> for this dataset? Select one of the answers below, then justify your answer in the box provided.

Hint: Look very closely at the definition of <span class="math-inline">\\(R&#95;{\text{B}}(w)\\)</span>. You do not need to re-prove any results from class; you can fully find and explain your answer without using calculus.

1.  Answer:
<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(10\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(15\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(20\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(30\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(40\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(60\\)</span></span></div>

2.  Justify your answer in the box below.

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(10\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(15\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(20\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(30\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(40\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(60\\)</span></span></div>

First, notice that the use of absolute values is a distraction: since <span class="math-inline">\\(|x|^2 = x^2\\)</span>, we can rewrite <span class="math-inline">\\(R&#95;{\text{B}}(w)\\)</span> as

<div class="math-display">
$$
R_{\text{B}}(w) = \frac{1}{n} \sum_{i=1}^n (2y_i - w)^2
$$
</div>

While it's possible to solve this problem by taking the derivative of <span class="math-inline">\\(R&#95;{\text{B}}(w)\\)</span> with respect to <span class="math-inline">\\(w\\)</span> and setting it equal to 0, it's quicker to leverage what we already know. We know that if there wasn't a coefficient of <span class="math-inline">\\(2\\)</span> in front of <span class="math-inline">\\(y&#95;i\\)</span>, the minimizer would be the mean of the dataset.

One way to reason about the effect of the coefficient of <span class="math-inline">\\(2\\)</span> is to consider a substitution. Let <span class="math-inline">\\(z&#95;i = 2y&#95;i\\)</span>. Then, <span class="math-inline">\\(R&#95;{\text{B}}(w)\\)</span> becomes

<div class="math-display">
$$
R_{\text{B}}(w) = \frac{1}{n} \sum_{i=1}^n (z_i - w)^2
$$
</div>

 which is the same as the mean squared error of the dataset <span class="math-inline">\\(z&#95;1, z&#95;2, \ldots, z&#95;n\\)</span>, and so <span class="math-inline">\\(w^{\ast} = \bar{z}\\)</span>. But <span class="math-inline">\\(\bar{z} = 2 \bar{y}\\)</span>, and so

<div class="math-display">
$$
w^* = 2 \bar{y} = 2 \cdot 20 = \boxed{40}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> This part does not use any of the numbers from part **a)**.

Recall that the mean absolute error, <span class="math-inline">\\(R&#95;{\text{abs}}(w)\\)</span>, of a constant prediction <span class="math-inline">\\(w\\)</span> on a dataset of <span class="math-inline">\\(n\\)</span> values <span class="math-inline">\\(y&#95;1, y&#95;2, \ldots, y&#95;n\\)</span> is given by

<div class="math-display">
$$
R_{\text{abs}}(w) = \frac{1}{n} \sum_{i=1}^n |y_i - w|
$$
</div>

Consider the dataset of 4 values, <span class="math-inline">\\(1, 3, 5, 9\\)</span>. Among all integers **not in this dataset**, which **integer** minimizes <span class="math-inline">\\(R&#95;{\text{abs}}(w)\\)</span> for this dataset?

<span class="math-inline">\\(\text{minimizer} = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>

<details markdown="1"><summary>Solution</summary>

The minimizer of mean absolute error is the median of the dataset. When the number of data points is even, any value between the middle two values, inclusive, minimizes mean absolute error. Here, any value between 3 and 5 inclusive minimizes mean absolute error; the value <span class="math-inline">\\(\boxed{4}\\)</span> is the only integer in this range that isn't in the dataset itself, so it is the minimizer we're looking for.
</details>

</div>
</div>

</div>
