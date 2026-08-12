---
number: 2
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">10 pts</span>
points: 10
flags: []
has_solution: true
images: []
---

We will continue to use the constant model, <span class="math-inline">\\(h(x&#95;i)=w\\)</span>, and the same dataset of <span class="math-inline">\\(n=4\\)</span> values as in Problem 1:

<div class="math-display">
$$
0,\quad 2,\quad 4,\quad 20
$$
</div>

 Instead of the clipped loss function, consider the **weighted absolute** loss function, defined below.

<div class="math-display">
$$
L_\text{WA}(y_i,h(x_i))=
\begin{cases}
\beta(y_i-h(x_i)), & h(x_i)<y_i \\\\
h(x_i)-y_i, & h(x_i)\ge y_i
\end{cases}
$$
</div>

 where <span class="math-inline">\\(\beta\\)</span> is a positive integer. Let <span class="math-inline">\\(R&#95;\text{WA}(w)\\)</span> be the average weighted absolute loss for the constant model and this dataset.

The slope of <span class="math-inline">\\(R&#95;\text{WA}(w)\\)</span> at <span class="math-inline">\\(w\\)</span>, for any value of <span class="math-inline">\\(w\\)</span> not equal to one of the <span class="math-inline">\\(y&#95;i\\)</span> values, is

<div class="math-display">
$$
\text{slope of } R_\text{WA}(w) \text{ at } w = \frac{\#\text{ left of } w - \beta(\#\text{ right of } w)}{4}
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Suppose <span class="math-inline">\\(\beta = 1\\)</span>. Which value of <span class="math-inline">\\(w\\)</span> minimizes <span class="math-inline">\\(R&#95;\text{WA}(w)\\)</span>? Show your work, and write your final answer in the box provided. Your answer should be a number with no variables. If there are multiple possible answers, state just one.

<div class="math-display">
$$
\text{minimizer of } R_\text{WA}(w) = \_\_\_\_\_\_
$$
</div>

<details markdown="1"><summary>Solution</summary>

When <span class="math-inline">\\(\beta = 1\\)</span>, <span class="math-inline">\\(R&#95;{\text{WA}}(w)\\)</span> is just mean absolute error, <span class="math-inline">\\(R&#95;\text{abs}(w)\\)</span>. We know that the minimizer of mean absolute error is the median of the dataset, or any value between the middle two values if the dataset has an even number of values.

This dataset has an even number of values, so any <span class="math-inline">\\(w\\)</span> in the interval <span class="math-inline">\\(2 \leq w \leq 4\\)</span> minimizes <span class="math-inline">\\(R&#95;\text{WA}(w)\\)</span>. One such value is <span class="math-inline">\\(\boxed{3}\\)</span>, but <span class="math-inline">\\(2\\)</span>, <span class="math-inline">\\(4\\)</span>, <span class="math-inline">\\(\pi\\)</span>, etc. are all valid answers.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Now suppose <span class="math-inline">\\(\beta = 2\\)</span>. Which value of <span class="math-inline">\\(w\\)</span> minimizes <span class="math-inline">\\(R&#95;\text{WA}(w)\\)</span>? Show your work, and write your final answer in the box provided. Your answer should be a number with no variables. If there are multiple possible answers, state just one.

<div class="math-display">
$$
\text{minimizer of } R_\text{WA}(w) = \_\_\_\_\_\_
$$
</div>

<details markdown="1"><summary>Solution</summary>

When <span class="math-inline">\\(\beta=2\\)</span>, the slopes between consecutive data values are

<div class="math-display">
$$
-2,\quad -\frac54,\quad -\frac12,\quad \frac14,\quad 1
$$
</div>

 on the intervals <span class="math-inline">\\((-\infty,0)\\)</span>, <span class="math-inline">\\((0,2)\\)</span>, <span class="math-inline">\\((2,4)\\)</span>, <span class="math-inline">\\((4,20)\\)</span>, and <span class="math-inline">\\((20,\infty)\\)</span>. The slope changes from negative to positive at <span class="math-inline">\\(w=4\\)</span>, so the minimizer is <span class="math-inline">\\(\boxed{4}\\)</span>.

Conceptually, the fact that the errors in the case where <span class="math-inline">\\(y&#95;i &gt; h(x&#95;i)\\)</span> are multiplied by <span class="math-inline">\\(\beta\\)</span> forces the optimal <span class="math-inline">\\(w^{\ast}\\)</span> to be larger than the median (since we want the <span class="math-inline">\\(y&#95;i &gt; h(x&#95;i)\\)</span> case to not trigger as often when computing the average loss across the entire dataset).
</details>

</div>
</div>

</div>
