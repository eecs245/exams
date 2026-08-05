---
number: 1
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">16 pts</span>
points: 16
flags: []
has_solution: true
images: [p1-sol.png]
---

Suppose we'd like to find the optimal parameter, <span class="math-inline">\\(w^{\ast}\\)</span>, for the constant model <span class="math-inline">\\(h(x&#95;i)=w\\)</span>, using the following dataset of <span class="math-inline">\\(n = 4\\)</span> values, <span class="math-inline">\\(y&#95;1, y&#95;2, y&#95;3, y&#95;4\\)</span>:

<div class="math-display">
$$
0, \quad 2, \quad 4, \quad 20
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> First, suppose we find the optimal parameter by minimizing mean squared error, <span class="math-inline">\\(R&#95;\text{sq}(w)\\)</span>. Which value of <span class="math-inline">\\(w\\)</span> minimizes <span class="math-inline">\\(R&#95;\text{sq}(w)\\)</span>? Give your answer as a number with no variables.

<span class="math-inline">\\(\text{minimizer of } R&#95;\text{sq}(w) = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>

<details markdown="1"><summary>Solution</summary>

For the constant model, average squared loss is minimized at the mean of the <span class="math-inline">\\(y&#95;i\\)</span>'s. Here,

<div class="math-display">
$$
\frac{0+2+4+20}{4}=\frac{26}{4}=\boxed{\frac{13}{2}}
$$
</div>

</details>

Now, consider the **clipped** loss function, defined below.

<div class="math-display">
$$
\displaystyle L_\text{clip}(y_i,h(x_i))=\min\{(y_i-h(x_i))^2,9\}
$$
</div>

 For example, <span class="math-inline">\\(L&#95;\text{clip}(10, 5) = 9\\)</span> and <span class="math-inline">\\(L&#95;\text{clip}(5, 3) = 4\\)</span>.

Let <span class="math-inline">\\(R&#95;\text{clip}(w)\\)</span> be the average clipped loss for the constant model and this dataset.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> State one value of <span class="math-inline">\\(w\\)</span> where the derivative of <span class="math-inline">\\(R&#95;\text{clip}(w)\\)</span> is not defined.

<span class="math-inline">\\(\text{one value of } w \text{ where the derivative of } R&#95;\text{clip}(w) \text{ is not defined} =\\)</span> \_\_\_\_\_\_

<details markdown="1"><summary>Solution</summary>

The clipped loss changes formulas whenever

<div class="math-display">
$$
(y_i-w)^2=9
$$
</div>

 Equivalently, this happens when <span class="math-inline">\\(w=y&#95;i\pm 3\\)</span>. Since <span class="math-inline">\\(20-3=17\\)</span>, one valid answer is <span class="math-inline">\\(\boxed{17}\\)</span>.

For context, here's what average clipped loss looks like for this dataset:

<div style="text-align: center;">
<img src="imgs/p1-sol.png" alt="image" style="width: 90%; max-width: 100%;">
</div>
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> Suppose we restrict <span class="math-inline">\\(w\\)</span> to the interval <span class="math-inline">\\(1 \leq w \leq 3\\)</span>. Among all values of <span class="math-inline">\\(w\\)</span> in this interval, which value minimizes <span class="math-inline">\\(R&#95;\text{clip}(w)\\)</span>? Give your answer as a number with no variables.

<span class="math-inline">\\(\text{minimizer of } R&#95;\text{clip}(w) \text{ within the interval } [1, 3] = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>

<details markdown="1"><summary>Solution</summary>

Once <span class="math-inline">\\(w\\)</span> is more than 3 units away from any particular <span class="math-inline">\\(y&#95;i\\)</span> value, the value <span class="math-inline">\\((y&#95;i - w)^2\\)</span> is replaced by the constant <span class="math-inline">\\(9\\)</span> when computing average loss.

What do we know about constants when they are added to functions? **They don't affect the minimizer!** That is, the minimizer of <span class="math-inline">\\(f(x)\\)</span> and of <span class="math-inline">\\(f(x) + c\\)</span> are the same.

What this is saying is that if <span class="math-inline">\\(w\\)</span> is restricted to the interval <span class="math-inline">\\(1 \leq w \leq 3\\)</span>, we can ignore <span class="math-inline">\\(y&#95;4 = 20\\)</span> when computing the minimizer, and this just reduces to minimizing average squared loss (mean squared error) across the data points that are within 3 units of <span class="math-inline">\\(w\\)</span>. As long as <span class="math-inline">\\(1 \leq w \leq 3\\)</span>, we are within 3 units of <span class="math-inline">\\(y&#95;1 = 0\\)</span>, <span class="math-inline">\\(y&#95;2 = 2\\)</span>, and <span class="math-inline">\\(y&#95;3 = 4\\)</span>.

What constant minimizes average squared loss, for the dataset <span class="math-inline">\\(0, 2, 4\\)</span>? That's the mean of <span class="math-inline">\\(0, 2, 4\\)</span>, which is <span class="math-inline">\\(2\\)</span>. So the minimizer of <span class="math-inline">\\(R&#95;\text{clip}(w)\\)</span> within the interval <span class="math-inline">\\(1 \leq w \leq 3\\)</span> is <span class="math-inline">\\(\boxed{2}\\)</span>.

If you'd like to see this a little more formally, then when <span class="math-inline">\\(1 \leq w \leq 3\\)</span>,

<div class="math-display">
$$
R_\text{clip}(w)=\frac14\left(w^2+(2-w)^2+(4-w)^2+9\right)
$$
</div>

 Taking the derivative,

<div class="math-display">
$$
\frac{\text{d}}{\text{d}w}R_\text{clip}(w)=\frac14(2w+2(w-2)+2(w-4))=\frac{6w-12}{4}
$$
</div>

 Setting this equal to <span class="math-inline">\\(0\\)</span> gives <span class="math-inline">\\(w = 2\\)</span>, as we intuited earlier.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> Now suppose there are no restrictions on <span class="math-inline">\\(w\\)</span>. Among all possible values of <span class="math-inline">\\(w\\)</span>, which value minimizes <span class="math-inline">\\(R&#95;\text{clip}(w)\\)</span>? Give your answer as a number with no variables.

<span class="math-inline">\\(\text{minimizer of } R&#95;\text{clip}(w) = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>

<details markdown="1"><summary>Solution</summary>

The best <span class="math-inline">\\(w\\)</span> is still <span class="math-inline">\\(w = 2\\)</span>. As a refresher, let's look at the graph of <span class="math-inline">\\(R&#95;\text{clip}(w)\\)</span> again:

<div style="text-align: center;">
<img src="imgs/p1-sol.png" alt="image" style="width: 90%; max-width: 100%;">
</div>

First, note that <span class="math-inline">\\(w = 20\\)</span> is a local minimizer of <span class="math-inline">\\(R&#95;\text{clip}(w)\\)</span>: if we zoom in to the graph of <span class="math-inline">\\(R&#95;\text{clip}(w)\\)</span> around <span class="math-inline">\\(w = 20\\)</span>, it looks like a parabola that opens up, centered at <span class="math-inline">\\(w = 20\\)</span>. But, when we zoom out, we see that the graph falls even lower near <span class="math-inline">\\(w = 2\\)</span> than it does near <span class="math-inline">\\(w = 20\\)</span>.

Why is this? It's because there are many more <span class="math-inline">\\(y&#95;i\\)</span> values within 3 units of <span class="math-inline">\\(w = 2\\)</span> than there are within 3 units of <span class="math-inline">\\(w = 20\\)</span>. Remembering that we have <span class="math-inline">\\(y&#95;1 = 0, y&#95;2 = 2, y&#95;3 = 4, y&#95;4 = 20\\)</span>:

<div class="math-display">
$$
R_\text{clip}(20) = \frac{1}{4} \sum_{i=1}^4 \min\{(20-y_i)^2, 9\} = \frac{1}{4} \left( 9 + 9 + 9 + 0 \right) = \frac{27}{4}
$$
</div>



<div class="math-display">
$$
R_\text{clip}(2) = \frac{1}{4} \sum_{i=1}^4 \min\{(2-y_i)^2, 9\} = \frac{1}{4} \left( 4 + 0 + 4 + 9 \right) = \frac{17}{4}
$$
</div>

So, <span class="math-inline">\\(R&#95;\text{clip}(20) = \frac{27}{4} &gt; \frac{13}{4} = R&#95;\text{clip}(2)\\)</span>.

The question, then, is whether <span class="math-inline">\\(w=2\\)</span> is the global minimizer, or just that it's better than <span class="math-inline">\\(w=20\\)</span>. Crucially, you wouldn't have had the graph of <span class="math-inline">\\(R&#95;\text{clip}(w)\\)</span> during the exam, so you would have needed to reason about this without it. One way to see how <span class="math-inline">\\(w = 2\\)</span> is the global minimizer is to realize that as <span class="math-inline">\\(w\\)</span> increases from <span class="math-inline">\\(2\\)</span>, the average loss only increases, until it reaches 9, where it "coasts" until it we reach <span class="math-inline">\\(w = 17\\)</span>, where it decreases once again.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">e)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> State one pro and one con of using clipped loss instead of squared loss to find optimal model parameters.

<details markdown="1"><summary>Solution</summary>

One pro is that clipped loss is less sensitive to outliers, since very large errors all receive the same loss of <span class="math-inline">\\(9\\)</span>. One con is that it stops distinguishing between bad and very bad predictions once the error is large enough; it also introduces points where the derivative is not defined, when the two cases of the min function switch.
</details>

</div>
</div>

</div>
