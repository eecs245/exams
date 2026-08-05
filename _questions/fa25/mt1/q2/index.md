---
number: 2
title: Absolute Madness
heading_suffix: : Absolute Madness <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">17 pts</span>
points: 17
flags: []
has_solution: true
images: []
---

Consider a dataset of <span class="math-inline">\\(n = 8\\)</span> values, where

<div class="math-display">
$$
y_1 = 1,\quad y_2 = y_3 = 4, \quad y_4 = y_5 = y_6 = \alpha,\quad y_7 = y_8 = 20
$$
</div>

and <span class="math-inline">\\(4 &lt; \alpha &lt; 20\\)</span>.

As usual, let <span class="math-inline">\\(R&#95;\text{abs}(w)\\)</span> represent the mean absolute error of a constant prediction <span class="math-inline">\\(w\\)</span> on this dataset of 8 values.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> Is the value of <span class="math-inline">\\(w^{\ast}\\)</span>, the minimizer of <span class="math-inline">\\(R&#95;\text{abs}(w)\\)</span>, unique? Select and fill out one option below.

<span class="mc-bubble" aria-hidden="true"></span> The value of <span class="math-inline">\\(w^{\ast}\\)</span> is unique, and is equal to \_\_\_\_\_\_.

<span class="mc-bubble" aria-hidden="true"></span> The value of <span class="math-inline">\\(w^{\ast}\\)</span> is not unique; any value between \_\_\_\_\_\_ and \_\_\_\_\_\_ is a minimizer.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Find the value of <span class="math-inline">\\(R&#95;\text{abs}(\alpha)\\)</span>, for any valid choice of <span class="math-inline">\\(\alpha\\)</span>. Show your work, and <span class="math-inline">\\(\boxed{\text{circle}}\\)</span> your final answer, which should be an expression involving <span class="math-inline">\\(\alpha\\)</span> and other constants, but no other variables, and no summation notation.

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(R&#95;\text{abs}(\alpha) = \frac{\alpha + 31}{8}\\)</span>.

Let's start with the definition of <span class="math-inline">\\(R&#95;\text{abs}(w)\\)</span> and plug in <span class="math-inline">\\(w = \alpha\\)</span>.

<div class="math-display">
$$
\begin{align*}
R_\text{abs}(\alpha) &= \frac{1}{8} \sum_{i=1}^8 |y_i - \alpha| \\\\
&= \frac{|1 - \alpha| + |4 - \alpha| + |4 - \alpha| + |\alpha - \alpha| + |\alpha - \alpha| + |\alpha - \alpha| + |20 - \alpha| + |20 - \alpha|}{8} \\\\
&= \frac{|1 - \alpha| + 2|4 - \alpha| + 2|20 - \alpha|}{8}
\end{align*}
$$
</div>

Since <span class="math-inline">\\(\alpha &gt; 1\\)</span> and <span class="math-inline">\\(\alpha &gt; 4\\)</span>, we know that <span class="math-inline">\\(|1 - \alpha| = \alpha - 1\\)</span> and <span class="math-inline">\\(|4 - \alpha| = \alpha - 4\\)</span>. Similarly, since <span class="math-inline">\\(\alpha &lt; 20\\)</span>, we have <span class="math-inline">\\(|20 - \alpha| = 20 - \alpha\\)</span>.

<div class="math-display">
$$
\begin{align*}
R_\text{abs}(\alpha) &= \frac{|1 - \alpha| + 2|4 - \alpha| + 2|20 - \alpha|}{8} \\\\
&= \frac{\alpha - 1 + 2(\alpha - 4) + 2(20 - \alpha)}{8} \\\\
&= \frac{\alpha - 1 + 2\alpha - 8 + 40 - 2\alpha}{8} \\\\
&= \frac{\alpha + 31}{8}
\end{align*}
$$
</div>

</details>

Recall,

<div class="math-display">
$$
y_1 = 1,\quad y_2 = y_3 = 4, \quad y_4 = y_5 = y_6 = \alpha,\quad y_7 = y_8 = 20
$$
</div>

where <span class="math-inline">\\(4 &lt; \alpha &lt; 20\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">8 pts</span> Let the minimum possible value of <span class="math-inline">\\(R&#95;\text{abs}(w)\\)</span> be <span class="math-inline">\\(M\\)</span>. Given that

<div class="math-display">
$$
R_\text{abs}(20) - M = \frac{9}{2}
$$
</div>

find the value of <span class="math-inline">\\(\alpha\\)</span>. Show your work, and <span class="math-inline">\\(\boxed{\text{circle}}\\)</span> your final answer, which should be a number with no variables.

<em>Hint: It's possible to answer this without using your answer from the previous part.</em>

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(\alpha = 11\\)</span>.

Since <span class="math-inline">\\(\alpha\\)</span> minimizes <span class="math-inline">\\(R&#95;\text{abs}(w)\\)</span>, we know that <span class="math-inline">\\(R&#95;\text{abs}(\alpha) = M\\)</span>. In the previous part, we found an expression for <span class="math-inline">\\(R&#95;\text{abs}(\alpha)\\)</span>. One common solution was to find another expression for <span class="math-inline">\\(R&#95;\text{abs}(20)\\)</span> (which is also a function of <span class="math-inline">\\(\alpha\\)</span>), and then to solve for the <span class="math-inline">\\(\alpha\\)</span> such that

<div class="math-display">
$$
R_\text{abs}(20) - R_\text{abs}(\alpha) = \frac{9}{2}
$$
</div>

Here's another solution. Since <span class="math-inline">\\((\alpha, M)\\)</span> is the vertex of <span class="math-inline">\\(R&#95;\text{abs}(w)\\)</span>, we know that the slope to the left of it is negative and the slope to the right of it is positive.

The slope on the line segment between <span class="math-inline">\\((\alpha, M)\\)</span> and <span class="math-inline">\\((20, M + \frac{9}{2})\\)</span> is

<div class="math-display">
$$
\text{slope} = \frac{\# \text{left} - \# \text{right}}{n} = \frac{6 - 2}{8} = \frac{1}{2}
$$
</div>

So, now we know that on the line segment between <span class="math-inline">\\((\alpha, M)\\)</span> and <span class="math-inline">\\((20, M + \frac{9}{2})\\)</span>, the slope is <span class="math-inline">\\(\frac{1}{2}\\)</span>. This is all we need to solve for <span class="math-inline">\\(\alpha\\)</span>. Since the slope of a line segment is its change in <span class="math-inline">\\(y\\)</span> over its change in <span class="math-inline">\\(x\\)</span>, we have:

<div class="math-display">
$$
\frac{M + \frac{9}{2} - M}{20 - \alpha} = \frac{1}{2}
$$
</div>

Solving for <span class="math-inline">\\(\alpha\\)</span>, we get:

<div class="math-display">
$$
\alpha = 11
$$
</div>

</details>

</div>
</div>

</div>
