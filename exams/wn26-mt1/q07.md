---
number: 7
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">20 pts</span>
points: 20
flags: []
has_solution: true
images: []
---

Suppose we'd like to find the optimal constant parameter, <span class="math-inline">\\(w^{\ast}\\)</span>, for the constant model <span class="math-inline">\\(h(x&#95;i) = w\\)</span>, given a dataset of <span class="math-inline">\\(n\\)</span> points <span class="math-inline">\\((x&#95;1, y&#95;1), (x&#95;2, y&#95;2), \ldots, (x&#95;n, y&#95;n)\\)</span>. To do so, we use the **sub-squared** loss function, <span class="math-inline">\\(L&#95;\text{ss}\\)</span>, defined below.

<div class="math-display">
$$
L_\text{ss}(y_i, w) = (\sqrt{y_i} - \sqrt{w})^2
$$
</div>

This requires us to assume that all <span class="math-inline">\\(y&#95;i \ge 0\\)</span>, as are all possible values of <span class="math-inline">\\(w\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Find <span class="math-inline">\\(\frac{\text{d}}{\text{d}w} R&#95;\text{ss}(w)\\)</span>, the derivative of **average** sub-squared loss (i.e. the empirical risk) with respect to <span class="math-inline">\\(w\\)</span>. Show your work and <span class="math-inline">\\(\boxed{\text{circle}}\\)</span> your final answer, which should be an expression in terms of the <span class="math-inline">\\(y&#95;i\\)</span>'s, <span class="math-inline">\\(n\\)</span>, and/or any constants. <em>Hint: The derivative of <span class="math-inline">\\(f(x) = \sqrt{x}\\)</span> is <span class="math-inline">\\(\frac{\text{d}}{\text{d}x} \sqrt{x} = \frac{1}{2\sqrt{x}}\\)</span>.</em>

<details markdown="1"><summary>Solution</summary>

The definition of average sub-squared loss is

<div class="math-display">
$$
R_\text{ss}(w) = \frac{1}{n} \sum_{i=1}^n L_\text{ss}(y_i, w) = \frac{1}{n} \sum_{i=1}^n (\sqrt{y_i} - \sqrt{w})^2
$$
</div>

Then,

<div class="math-display">
$$
\begin{align*}
\frac{\text{d}}{\text{d}w} R_\text{ss}(w)
&= \frac{\text{d}}{\text{d}w} \left( \frac{1}{n} \sum_{i=1}^n (\sqrt{y_i} - \sqrt{w})^2 \right) \\\\
&= \frac{1}{n} \sum_{i=1}^n \frac{\text{d}}{\text{d}w} \left[(\sqrt{y_i} - \sqrt{w})^2\right] \\\\
&= \frac{1}{n} \sum_{i=1}^n 2(\sqrt{y_i} - \sqrt{w}) \cdot \frac{\text{d}}{\text{d}w} (\sqrt{y_i} - \sqrt{w}) \\\\
&= \frac{1}{n} \sum_{i=1}^n 2(\sqrt{y_i} - \sqrt{w}) \cdot \left(0 -\frac{1}{2\sqrt{w}} \right) \\\\
&= \boxed{-\frac{1}{n} \sum_{i=1}^n \frac{\sqrt{y_i} - \sqrt{w}}{\sqrt{w}}}
\end{align*}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Show that the value of <span class="math-inline">\\(w^{\ast}\\)</span> that minimizes average sub-squared loss is

<div class="math-display">
$$
\displaystyle w^* = \left( \frac{1}{n} \sum_{i=1}^n \sqrt{y_i} \right)^2
$$
</div>

<details markdown="1"><summary>Solution</summary>

We've found that

<div class="math-display">
$$
\frac{\text{d}}{\text{d}w} R_\text{ss}(w) = -\frac{1}{n} \sum_{i=1}^n \frac{\sqrt{y_i} - \sqrt{w}}{\sqrt{w}}
$$
</div>

To find <span class="math-inline">\\(w^{\ast}\\)</span>, we need to set this expression equal to 0 and solve for <span class="math-inline">\\(w\\)</span>.

<div class="math-display">
$$
\begin{align*}
-\frac{1}{n} \sum_{i=1}^n \frac{\sqrt{y_i} - \sqrt{w}}{\sqrt{w}} = 0 \\\\
\sum_{i=1}^n \frac{\sqrt{y_i} - \sqrt{w}}{\sqrt{w}} = 0 \\\\
\sum_{i=1}^n (\sqrt{y_i} - \sqrt{w}) = 0 \\\\
\sum_{i=1}^n \sqrt{y_i} - n \sqrt{w} = 0 \\\\
\sqrt{w} = \frac{1}{n} \sum_{i=1}^n \sqrt{y_i} \\\\
w = \left( \frac{1}{n} \sum_{i=1}^n \sqrt{y_i} \right)^2
\end{align*}
$$
</div>

So, the value of <span class="math-inline">\\(w^{\ast}\\)</span> that minimizes average sub-squared loss is

<div class="math-display">
$$
\boxed{w^* = \left( \frac{1}{n} \sum_{i=1}^n \sqrt{y_i} \right)^2}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Using the Cauchy-Schwarz inequality, prove that

<div class="math-display">
$$
\left( \frac{1}{n} \sum_{i=1}^n \sqrt{y_i} \right)^2 \leq \bar{y}
$$
</div>

where <span class="math-inline">\\(\bar{y}\\)</span> is the mean of the <span class="math-inline">\\(y&#95;i\\)</span>'s.

<em>Solutions that do not use the Cauchy-Schwarz inequality will not receive credit.</em>

<details markdown="1"><summary>Solution</summary>

The Cauchy-Schwarz inequality states that

<div class="math-display">
$$
\left| \vec u \cdot \vec v \right| \leq \lVert \vec u \rVert \lVert \vec v \rVert
$$
</div>

for any two vectors <span class="math-inline">\\(\vec u, \vec v \in \mathbb{R}^n\\)</span>. The problem boils down to constructing <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> such that the Cauchy-Schwarz inequality, for that <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span>, implies the inequality we're trying to prove.

For hints on how to proceed, let's expand the definition of <span class="math-inline">\\(\bar y\\)</span> in the inequality we're trying to prove.

<div class="math-display">
$$
\left( \frac{1}{n} \sum_{i=1}^n \sqrt{y_i} \right)^2 \leq \frac{1}{n} \sum_{i=1}^n y_i
$$
</div>

On the left, we have a sum of <span class="math-inline">\\(\sqrt{y&#95;i}\\)</span>'s, and on the right, we have a sum of <span class="math-inline">\\(y&#95;i\\)</span>'s. We know that in the norm of a vector, the individual components are squared, which would allow us to turn <span class="math-inline">\\(\sqrt{y&#95;i}\\)</span> into <span class="math-inline">\\(y&#95;i\\)</span>. So, one possible path forward is

<div class="math-display">
$$
\vec u = \begin{bmatrix} \sqrt{y_1} \\\\ \sqrt{y_2} \\\\ \vdots \\\\ \sqrt{y_n} \end{bmatrix}, \qquad \vec v = \begin{bmatrix} 1 \\\\ 1 \\\\ \vdots \\\\ 1 \end{bmatrix}
$$
</div>

The dot product of <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> is <span class="math-inline">\\(\sum&#95;{i=1}^n \sqrt{y&#95;i}\\)</span>, which seems promising. Let's plug <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> into the Cauchy-Schwarz inequality and see what we get.

<div class="math-display">
$$
\begin{align*}
\left| \vec u \cdot \vec v \right| &\leq \lVert \vec u \rVert \lVert \vec v \rVert \\\\
\left| \sum_{i=1}^n \sqrt{y_i} \right| &\leq \left \lVert \begin{bmatrix} \sqrt{y_1} \\\\ \sqrt{y_2} \\\\ \vdots \\\\ \sqrt{y_n} \end{bmatrix} \right \rVert \left \lVert \begin{bmatrix} 1 \\\\ 1 \\\\ \vdots \\\\ 1 \end{bmatrix} \right \rVert \\\\
\sum_{i=1}^n \sqrt{y_i} &\leq \sqrt{\sum_{i=1}^n y_i} \sqrt{n} \\\\
\end{align*}
$$
</div>

Seems like we're getting somewhere. Let's square both sides.

<div class="math-display">
$$
\begin{align*}
\left( \sum_{i=1}^n \sqrt{y_i} \right)^2 &\leq \left( \sqrt{\sum_{i=1}^n y_i} \sqrt{n} \right)^2 \\\\
\left( \sum_{i=1}^n \sqrt{y_i} \right)^2 & \leq n\sum_{i=1}^n y_i
\end{align*}
$$
</div>

Now, all that's left is to divide both sides by <span class="math-inline">\\(n^2\\)</span>.

<div class="math-display">
$$
\begin{align*}
\left( \sum_{i=1}^n \sqrt{y_i} \right)^2 & \leq n\sum_{i=1}^n y_i \\\\
\frac{\left( \sum_{i=1}^n \sqrt{y_i} \right)^2}{n^2} & \leq \frac{n\sum_{i=1}^n y_i}{n^2} \\\\
\left( \frac{1}{n} \sum_{i=1}^n \sqrt{y_i} \right)^2 & \leq \frac{1}{n} \sum_{i=1}^n y_i
\end{align*}
$$
</div>

This is exactly the inequality we're trying to prove, so we're done!
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">2 pts</span> What is the value of <span class="math-inline">\\(w\\)</span> that minimizes the following function:

<div class="math-display">
$$
R(w) = \frac{1}{n}\sum_{i=1}^n (y_i^4 - w^4)^2
$$
</div>

<em>Hint: This can be done without using any calculus --- don't try and take the derivative.</em>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \left(\frac{1}{n} \sum&#95;{i=1}^n y&#95;i \right)^4\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\left(\displaystyle \frac{1}{n} \sum&#95;{i=1}^n y&#95;i^{1/4}\right)^4\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \left(\frac{1}{n} \sum&#95;{i=1}^n y&#95;i^4 \right)^{1/4}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \left(\frac{1}{n} \sum&#95;{i=1}^n y&#95;i^{1/2} \right)^{1/4}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \left(\frac{1}{n} \sum&#95;{i=1}^n y&#95;i^{4} \right)^{1/2}\\)</span></span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \left(\frac{1}{n} \sum&#95;{i=1}^n y&#95;i \right)^4\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\left(\displaystyle \frac{1}{n} \sum&#95;{i=1}^n y&#95;i^{1/4}\right)^4\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \left(\frac{1}{n} \sum&#95;{i=1}^n y&#95;i^4 \right)^{1/4}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \left(\frac{1}{n} \sum&#95;{i=1}^n y&#95;i^{1/2} \right)^{1/4}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \left(\frac{1}{n} \sum&#95;{i=1}^n y&#95;i^{4} \right)^{1/2}\\)</span></span></div>

The idea here is to make a substitution that reduces the problem to one we've already seen --- the problem of minimizing mean squared error for the constant model.

Let <span class="math-inline">\\(z&#95;i = y&#95;i^4\\)</span>, and let <span class="math-inline">\\(t = w^4\\)</span>. Then,

<div class="math-display">
$$
\frac{1}{n}\sum_{i=1}^n (z_i - t)^2 = \frac{1}{n}\sum_{i=1}^n (y_i^4 - w^4)^2
$$
</div>

What is <span class="math-inline">\\(t^{\ast}\\)</span>, the minimizer of <span class="math-inline">\\(\frac{1}{n}\sum&#95;{i=1}^n (z&#95;i - t)^2\\)</span>? That's <span class="math-inline">\\(\bar{z}\\)</span>, which is

<div class="math-display">
$$
t^* = \bar{z} = \frac{1}{n} \sum_{i=1}^n z_i = \frac{1}{n} \sum_{i=1}^n y_i^4
$$
</div>

But, <span class="math-inline">\\(t = w^4\\)</span>, so <span class="math-inline">\\(w = t^{1/4}\\)</span>, meaning

<div class="math-display">
$$
w^* = \boxed{\left( \frac{1}{n} \sum_{i=1}^n y_i^4 \right)^{1/4}}
$$
</div>

Notice how this relates to parts **a)** and **b)** --- those could have been solved the same way, if you wrote <span class="math-inline">\\(\sqrt{x}\\)</span> as <span class="math-inline">\\(x^{1/2}\\)</span>.
</details>
</div>
</div>

</div>
