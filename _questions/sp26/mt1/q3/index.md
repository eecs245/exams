---
number: 3
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">14 pts</span>
points: 14
flags: []
has_solution: true
images: []
---

Suppose we fit a simple linear regression model **with** an intercept term, <span class="math-inline">\\(h(x&#95;i)=w&#95;0+w&#95;1x&#95;i\\)</span>, to a dataset of <span class="math-inline">\\(n\\)</span> points <span class="math-inline">\\((x&#95;1, y&#95;1), (x&#95;2, y&#95;2), \ldots, (x&#95;n, y&#95;n)\\)</span> by minimizing mean squared error. You are given the following information:

-   The fit model satisfies <span class="math-inline">\\(h(-4) = 5\\)</span> and <span class="math-inline">\\(h(8) = 14\\)</span>.

-   The mean of <span class="math-inline">\\(y&#95;1, y&#95;2, \ldots, y&#95;n\\)</span> is <span class="math-inline">\\(\bar y = 2\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Find <span class="math-inline">\\(\bar x\\)</span>, the mean of <span class="math-inline">\\(x&#95;1, x&#95;2, \ldots, x&#95;n\\)</span>. Show your work, and write your final answer in the box provided. Your answer should be a number with no variables. <em>Hint: What property does the line <span class="math-inline">\\(h(x&#95;i)\\)</span> satisfy?</em>

<div class="math-display">
$$
\bar x = \_\_\_\_\_\_
$$
</div>

<details markdown="1"><summary>Solution</summary>

The line through <span class="math-inline">\\((-4,5)\\)</span> and <span class="math-inline">\\((8,14)\\)</span> has slope

<div class="math-display">
$$
w_1^*=\frac{14-5}{8-(-4)}=\frac{9}{12}=\frac34
$$
</div>

 Using <span class="math-inline">\\(h(-4)=5\\)</span>,

<div class="math-display">
$$
5=w_0^*+\frac34(-4)=w_0^*-3
$$
</div>

 so <span class="math-inline">\\(w&#95;0^{\ast}=8\\)</span>, and the fit model is <span class="math-inline">\\(h(x&#95;i) = 8 + \frac{3}{4}x&#95;i\\)</span>.

For simple linear regression with an intercept, the fit line passes through <span class="math-inline">\\((\bar x,\bar y)\\)</span>. Since <span class="math-inline">\\(\bar y=2\\)</span>,

<div class="math-display">
$$
2=8+\frac34\bar x \implies \bar x = -8
$$
</div>

 which gives <span class="math-inline">\\(\boxed{\bar x=-8}\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Suppose the correlation coefficient between the <span class="math-inline">\\(x\\)</span>-values and <span class="math-inline">\\(y\\)</span>-values is <span class="math-inline">\\(r = 1/3\\)</span>.

The standard deviation of <span class="math-inline">\\(y\\)</span>, <span class="math-inline">\\(\sigma&#95;y\\)</span>, is <span class="math-inline">\\(c\\)</span> times the standard deviation of <span class="math-inline">\\(x\\)</span>, <span class="math-inline">\\(\sigma&#95;x\\)</span>. In other words,

<div class="math-display">
$$
\sigma_y = c \sigma_x
$$
</div>

 What is the value of <span class="math-inline">\\(c\\)</span>?

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1/4\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(4/9\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(3/4\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(9/4\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(3\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(4\\)</span></span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1/4\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(4/9\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(3/4\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(9/4\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(3\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(4\\)</span></span></div>

For simple linear regression, one (of the many equivalent) formula for the slope <span class="math-inline">\\(w&#95;1^{\ast}\\)</span> is

<div class="math-display">
$$
w_1^*=r\frac{\sigma_y}{\sigma_x}
$$
</div>

 From part **a)**, <span class="math-inline">\\(w&#95;1^{\ast}=\frac34\\)</span>. Since <span class="math-inline">\\(r=\frac13\\)</span> and <span class="math-inline">\\(\sigma&#95;y=c\sigma&#95;x\\)</span>,

<div class="math-display">
$$
\frac34=\frac13c
$$
</div>

 so <span class="math-inline">\\(\boxed{c=\frac94}\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Let <span class="math-inline">\\(e&#95;i=y&#95;i-h(x&#95;i)\\)</span> be the fit model's error for the <span class="math-inline">\\(i\\)</span>th point. Note that <span class="math-inline">\\(e&#95;i\\)</span> may either be positive or negative. Which of the following statements are **guaranteed** to be true? **Select all** that apply.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle\sum&#95;{i=1}^n e&#95;i=0\\)</span></span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle\sum&#95;{i=1}^n x&#95;i e&#95;i=0\\)</span></span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle\sum&#95;{i=1}^n y&#95;i e&#95;i=0\\)</span></span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle\sum&#95;{i=1}^n e&#95;i (x&#95;i - \bar x)=0\\)</span></span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-square mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle\sum&#95;{i=1}^n e&#95;i=0\\)</span></span><span class="mc-option"><span class="mc-square mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle\sum&#95;{i=1}^n x&#95;i e&#95;i=0\\)</span></span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle\sum&#95;{i=1}^n y&#95;i e&#95;i=0\\)</span></span><span class="mc-option"><span class="mc-square mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle\sum&#95;{i=1}^n e&#95;i (x&#95;i - \bar x)=0\\)</span></span></div>

How did we find <span class="math-inline">\\(w&#95;0^{\ast}\\)</span> and <span class="math-inline">\\(w&#95;1^{\ast}\\)</span>? By minimizing mean squared error:

<div class="math-display">
$$
R_\text{sq}(w_0, w_1) = \frac{1}{n} \sum_{i=1}^n (y_i - (w_0 + w_1 x_i))^2
$$
</div>

To do so, we took the partial derivatives with respect to <span class="math-inline">\\(w&#95;0\\)</span> and <span class="math-inline">\\(w&#95;1\\)</span> and set them equal to 0:

<div class="math-display">
$$
\frac{\partial R_\text{sq}}{\partial w_0} = \frac{1}{n} \sum_{i=1}^n -2(y_i - (w_0 + w_1 x_i)) = 0
$$
</div>



<div class="math-display">
$$
\frac{\partial R_\text{sq}}{\partial w_1} = \frac{1}{n} \sum_{i=1}^n -2x_i(y_i - (w_0 + w_1 x_i)) = 0
$$
</div>

Solving these equations gave us <span class="math-inline">\\(w&#95;0^{\ast}\\)</span> and <span class="math-inline">\\(w&#95;1^{\ast}\\)</span>. But if we take a closer look, these equations are telling us properties about the errors, <span class="math-inline">\\(e&#95;i = y&#95;i - h(x&#95;i) = y&#95;i - (w&#95;0 + w&#95;1 x&#95;i)\\)</span>. Above, I'll substitute in <span class="math-inline">\\(e&#95;i\\)</span> every time I see a <span class="math-inline">\\(y&#95;i - (w&#95;0 + w&#95;1 x&#95;i)\\)</span>.

The first equation becomes

<div class="math-display">
$$
\frac{1}{n} \sum_{i=1}^n -2e_i = 0 \implies \sum_{i=1}^n e_i = 0
$$
</div>

and the second equation becomes

<div class="math-display">
$$
\frac{1}{n} \sum_{i=1}^n -2x_i e_i = 0 \implies \sum_{i=1}^n x_i e_i = 0
$$
</div>

So, hidden in plain sight were these properties about the errors! Recall, the four options in this question are:

-   <span class="math-inline">\\(\displaystyle\sum&#95;{i=1}^n e&#95;i=0\\)</span>

-   <span class="math-inline">\\(\displaystyle\sum&#95;{i=1}^n x&#95;i e&#95;i=0\\)</span>

-   <span class="math-inline">\\(\displaystyle\sum&#95;{i=1}^n y&#95;i e&#95;i=0\\)</span>

-   <span class="math-inline">\\(\displaystyle\sum&#95;{i=1}^n e&#95;i(x&#95;i-\bar x)=0\\)</span>

So, we know the first two are true.

What about the third option, <span class="math-inline">\\(\displaystyle\sum&#95;{i=1}^n y&#95;i e&#95;i=0\\)</span>? The short answer is that there's no reason to believe this is true; if it were, it would have emerged from our analysis above. To be sure that it's not true, let's find a counterexample.

We know that <span class="math-inline">\\(y&#95;i = h(x&#95;i) + e&#95;i\\)</span>, so

<div class="math-display">
$$
\sum_{i=1}^n y_i e_i = \sum_{i=1}^n (h(x_i) + e_i) e_i = \sum_{i=1}^n h(x_i) e_i + \sum_{i=1}^n e_i^2
$$
</div>

This is only <span class="math-inline">\\(0\\)</span> when the fit line has zero error on every point. So, the third option is not guaranteed to be true.

Finally, let's look at the fourth option, <span class="math-inline">\\(\sum&#95;{i=1}^n e&#95;i(x&#95;i-\bar x)=0\\)</span>. This is true, because the first two options are true:

<div class="math-display">
$$
\sum_{i=1}^n e_i(x_i-\bar x)=\sum_{i=1}^n e_i x_i -\sum_{i=1}^n e_i \bar x = 0 - \bar x \sum_{i=1}^n e_i = 0
$$
</div>

 The statement <span class="math-inline">\\(\sum&#95;{i=1}^n y&#95;i e&#95;i=0\\)</span> is not guaranteed; in fact, since <span class="math-inline">\\(y&#95;i=h(x&#95;i)+e&#95;i\\)</span>,

<div class="math-display">
$$
\sum_{i=1}^n y_i e_i=\sum_{i=1}^n h(x_i)e_i+\sum_{i=1}^n e_i^2=\sum_{i=1}^n e_i^2
$$
</div>

 which is only <span class="math-inline">\\(0\\)</span> when the fit line has zero error on every point, i.e. passes through every single point.

**Above, you may be wondering why it's the case that**

<div class="math-display">
$$
\sum_{i = 1}^n h(x_i) e_i = 0
$$
</div>

Intentionally, I haven't provided the proof of this! I want you to piece the proof together. Start by using the fact that the first two options in this question are true.
</details>

</div>
</div>

</div>
