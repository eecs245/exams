---
number: 1
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">14 pts</span> <span class="badge" data-flag="mt1-redemption" style="background-color: #9A3324; color: #FFFFFF; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">MT1 Redemption</span>
points: 14
flags: [mt1-redemption]
has_solution: true
images: []
---

Suppose we'd like to find the optimal constant parameter, <span class="math-inline">\\(w^{\ast}\\)</span>, for the constant model <span class="math-inline">\\(h(x&#95;i)=w\\)</span>, using the following dataset of <span class="math-inline">\\(n=5\\)</span> values:

<div class="math-display">
$$
1,\quad 1,\quad 4,\quad 9,\quad 25
$$
</div>

 In each part, find the value of <span class="math-inline">\\(w^{\ast}\\)</span> that minimizes the given <span class="math-inline">\\(R(w)\\)</span>. Show your work in the space provided, and write your final answer in the bottom-right corner of the box. Your answers should be numbers with no variables. *Note: There is no need to use calculus here.*

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span>
<span class="math-inline">\\(\displaystyle R(w) = \frac{1}{5} \sum&#95;{i=1}^5 (y&#95;i - w)^2\\)</span>

<div class="math-display">
$$
w^* = \_\_\_\_\_\_
$$
</div>

<details markdown="1"><summary>Solution</summary>

The minimizer of mean squared error for a constant model is the mean, as discussed in [Chapter 1.2](https://notes.eecs245.org/introduction-to-supervised-learning/squared-loss-constant-model/). So,

<div class="math-display">
$$
w^* = \frac{1+1+4+9+25}{5} = \frac{40}{5} = 8
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span>
<span class="math-inline">\\(\displaystyle R(w) = \frac{1}{5} \sum&#95;{i=1}^5 (\sqrt{y&#95;i} - w)^2\\)</span>

<div class="math-display">
$$
w^* = \_\_\_\_\_\_
$$
</div>

<details markdown="1"><summary>Solution</summary>

This is asking for the best constant prediction for the transformed values <span class="math-inline">\\(\sqrt{y&#95;i}\\)</span>. The transformed data are

<div class="math-display">
$$
1,\quad 1,\quad 2,\quad 3,\quad 5
$$
</div>

 so

<div class="math-display">
$$
w^* = \frac{1+1+2+3+5}{5} = \frac{12}{5}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span>
<span class="math-inline">\\(\displaystyle R(w) = \frac{1}{5} \sum&#95;{i=1}^5 (y&#95;i - \sqrt{w})^2\\)</span>

<div class="math-display">
$$
w^* = \_\_\_\_\_\_
$$
</div>

<details markdown="1"><summary>Solution</summary>

Let <span class="math-inline">\\(u=\sqrt{w}\\)</span>. The loss becomes

<div class="math-display">
$$
R(u) = \frac{1}{5}\sum_{i=1}^5 (y_i-u)^2
$$
</div>

 which is minimized at the mean of the original <span class="math-inline">\\(y&#95;i\\)</span> values:

<div class="math-display">
$$
u^* = \frac{1+1+4+9+25}{5} = 8
$$
</div>

 Since <span class="math-inline">\\(u=\sqrt{w}\\)</span>, we have

<div class="math-display">
$$
w^* = 8^2 = 64
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">2 pts</span> Which answer from above is also the minimizer of <span class="math-inline">\\(\displaystyle R(w) = \sqrt{\frac{1}{5} \sum&#95;{i=1}^5 (y&#95;i - w)^2}\\)</span>?

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Answer from part (a)</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Answer from part (b)</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Answer from part (c)</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> None</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> Answer from part (a)</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Answer from part (b)</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Answer from part (c)</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> None</span></div>

The square root function is strictly increasing, so minimizing

<div class="math-display">
$$
\sqrt{\frac{1}{5} \sum_{i=1}^5 (y_i-w)^2}
$$
</div>

 is equivalent to minimizing

<div class="math-display">
$$
\frac{1}{5} \sum_{i=1}^5 (y_i-w)^2
$$
</div>

That is exactly the objective from part **a)**, so the answer is the answer from part **a)**.
</details>

</div>
</div>

</div>
