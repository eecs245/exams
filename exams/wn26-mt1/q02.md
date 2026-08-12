---
number: 2
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">14 pts</span>
points: 14
flags: []
has_solution: true
images: []
---

Suppose we'd like to fit a simple linear regression model to a dataset of <span class="math-inline">\\(n\\)</span> points,

<span class="math-inline">\\((x&#95;1, y&#95;1), (x&#95;2, y&#95;2), \ldots, (x&#95;n, y&#95;n)\\)</span>, by minimizing mean squared error.

Suppose <span class="math-inline">\\(w&#95;0^{\ast}\\)</span> and <span class="math-inline">\\(w&#95;1^{\ast}\\)</span> are the optimal intercept and slope parameters, respectively, and let

<div class="math-display">
$$
M = \frac{1}{n} \sum_{i=1}^n (y_i - (w_0^* + w_1^* x_i))^2
$$
</div>

 Finally, let <span class="math-inline">\\(\sigma&#95;x\\)</span> and <span class="math-inline">\\(\sigma&#95;y\\)</span> be the standard deviations of the <span class="math-inline">\\(x\\)</span>-values and <span class="math-inline">\\(y\\)</span>-values in the dataset, respectively. Assume that <span class="math-inline">\\(\sigma&#95;x &gt; 0\\)</span> and <span class="math-inline">\\(\sigma&#95;y &gt; 0\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">5 pts</span> Which of the following is the relationship between <span class="math-inline">\\(M\\)</span> and <span class="math-inline">\\(\sigma&#95;y^2\\)</span>? Select an answer and provide a brief explanation in the box provided.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(M \leq \sigma&#95;y^2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(M = \sigma&#95;y^2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(M \geq \sigma&#95;y^2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Impossible to tell</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(M \leq \sigma&#95;y^2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(M = \sigma&#95;y^2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(M \geq \sigma&#95;y^2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Impossible to tell</span></div>

<span class="math-inline">\\(M\\)</span> is the mean squared error of the best simple linear regression model for the dataset; it minimizes the mean squared error among all models of the form

<div class="math-display">
$$
h(x_i) = w_0 + w_1 x_i
$$
</div>

The constant model, <span class="math-inline">\\(h(x&#95;i) = w\\)</span>, can be thought of as a more restrictive version of the simple linear regression model, in that it has an intercept <span class="math-inline">\\(w\\)</span> and slope of <span class="math-inline">\\(0\\)</span>. So, the best simple linear regression model is at least as good as the best constant model, when both are measured by mean squared error. If the <span class="math-inline">\\(x\\)</span> and <span class="math-inline">\\(y\\)</span> values in the dataset have no linear association, meaning the correlation coefficient <span class="math-inline">\\(r\\)</span> is 0, then the best simple linear regression model is the same as the best constant model; otherwise, the best simple linear regression model is better, since it has all of the flexibility of the constant model, and more. The first section of [Chapter 2.5](https://notes.eecs245.org/simple-linear-regression/least-squares/) discusses this idea further.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">5 pts</span> Suppose that <span class="math-inline">\\(M = 0\\)</span>. What is the value of <span class="math-inline">\\(r\\)</span>, the correlation coefficient between the <span class="math-inline">\\(x\\)</span>-values and <span class="math-inline">\\(y\\)</span>-values in the dataset? <span class="math-inline">\\(\boxed{\text{Circle}}\\)</span> your final answer and provide a brief explanation. If there are multiple possible values, state them all.

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(r = 1\\)</span> or <span class="math-inline">\\(r = -1\\)</span>.

The only case in which <span class="math-inline">\\(M = 0\\)</span> is when the best simple linear regression model makes 0 errors, i.e. it passes through every point in the dataset. This happens when the <span class="math-inline">\\(x\\)</span> and <span class="math-inline">\\(y\\)</span> values in the dataset have a perfect linear association, meaning <span class="math-inline">\\(r = 1\\)</span> (positive linear association) or <span class="math-inline">\\(r = -1\\)</span> (negative linear association).
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">2 pts</span> True or False: It is possible for there to be multiple pairs of <span class="math-inline">\\((\text{intercept}, \text{slope})\\)</span> with a mean squared error of <span class="math-inline">\\(M\\)</span>.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> False</span></div>

The values of <span class="math-inline">\\(w&#95;0^{\ast}\\)</span> and <span class="math-inline">\\(w&#95;1^{\ast}\\)</span> are unique. We've seen several formulas for them in the notes; they are the unique minimizers of

<div class="math-display">
$$
R_\text{sq}(w_0, w_1) = \frac{1}{n} \sum_{i=1}^n (y_i - (w_0 + w_1 x_i))^2
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">2 pts</span> True or False: It is possible for there to be multiple pairs of <span class="math-inline">\\((\text{intercept}, \text{slope})\\)</span> with a mean squared error of <span class="math-inline">\\(M + 1\\)</span>.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

The values of <span class="math-inline">\\(w&#95;0\\)</span> and <span class="math-inline">\\(w&#95;1\\)</span> that minimize <span class="math-inline">\\(R&#95;\text{sq}(w&#95;0, w&#95;1)\\)</span> are unique, but we're not discussing the minimizers here, so that fact is irrelevant.

Instead, it's asking whether it's possible for there to be multiple pairs of <span class="math-inline">\\((w&#95;0, w&#95;1)\\)</span> with a mean squared error of something bigger than <span class="math-inline">\\(M\\)</span>. The <span class="math-inline">\\(+1\\)</span> is not important; we could have stated <span class="math-inline">\\(+17\\)</span> or <span class="math-inline">\\(+3\pi^2\\)</span> and the question would be the same.

Recall from [Chapter 2.3](https://notes.eecs245.org/simple-linear-regression/finding-optimal-parameters/) that the graph of <span class="math-inline">\\(R&#95;\text{sq}(w&#95;0, w&#95;1)\\)</span> looks like a bowl in <span class="math-inline">\\(\mathbb{R}^3\\)</span>. While there's only one point at which the bowl is minimized, for any height (<span class="math-inline">\\(z\\)</span>-value) greater than <span class="math-inline">\\(M\\)</span>, there are infinitely many pairs of <span class="math-inline">\\((w&#95;0, w&#95;1)\\)</span> that give that height. To see this, imagine slicing the bowl with the plane <span class="math-inline">\\(z = M + 1\\)</span>. This slice is an ellipse (stretched circle), upon which infinitely many combinations of <span class="math-inline">\\((w&#95;0, w&#95;1)\\)</span> lie.

So, yes, it is possible for there to be multiple pairs of <span class="math-inline">\\((w&#95;0, w&#95;1)\\)</span> with a mean squared error of <span class="math-inline">\\(M + 1\\)</span> --- in fact, that's guaranteed.
</details>

</div>
</div>

</div>
