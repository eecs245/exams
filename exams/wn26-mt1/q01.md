---
number: 1
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">16 pts</span>
points: 16
flags: []
has_solution: true
images: [line_graph_gray.png, w_r_axes.png, w_r_axes_solution.png]
---

Consider a dataset of <span class="math-inline">\\(n\\)</span> values, <span class="math-inline">\\(y&#95;1, y&#95;2, \ldots, y&#95;n\\)</span>, with:

-   a mean of <span class="math-inline">\\(\bar{y} = 18\\)</span>

-   a median of 15

-   a standard deviation of <span class="math-inline">\\(\sigma&#95;y = 7\\)</span>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> In the space provided, sketch the graph of <span class="math-inline">\\(R&#95;\text{sq}(w)\\)</span>, the mean squared error of a constant prediction <span class="math-inline">\\(w\\)</span> on the dataset. For full credit:

-   The shape of the graph must be correct.

-   You must clearly label the coordinates of the **minimum point** on the graph.

<div style="text-align: center;">
<img src="imgs/w_r_axes.png" alt="image" style="width: 70%; max-width: 100%;">
</div>

<details markdown="1"><summary>Solution</summary>

<div style="text-align: center;">
<img src="imgs/w_r_axes_solution.png" alt="image" style="width: 90%; max-width: 100%;">
</div>

Recall that

<div class="math-display">
$$
R_\text{sq}(w) = \frac{1}{n} \sum_{i=1}^n (y_i - w)^2
$$
</div>

is a parabola, minimized at <span class="math-inline">\\(w = \bar y\\)</span>. When <span class="math-inline">\\(w = \bar y\\)</span>,

<div class="math-display">
$$
R_\text{sq}(w) = \frac{1}{n} \sum_{i=1}^n (y_i - \bar y)^2 = \sigma_y^2
$$
</div>

 is the variance of the dataset. Here, the mean is 18 and the variance is 49, so the minimum point is at <span class="math-inline">\\((18, 49)\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Which of the following quantities is **guaranteed** to be equal to 0? Select all that apply.

<span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \frac{1}{n} \sum&#95;{i=1}^n (y&#95;i - 15)\\)</span>

<span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \frac{1}{n} \sum&#95;{i=1}^n (y&#95;i - 18)\\)</span>

<span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \frac{1}{n}\sum&#95;{i=1}^n (y&#95;i - 15)^2\\)</span>

<span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \frac{1}{n}\sum&#95;{i=1}^n (y&#95;i - 18)^2\\)</span>

<span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \frac{1}{n}\sum&#95;{i=1}^n (y&#95;i - 15)^2 - 7^2\\)</span>

<span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \frac{1}{n}\sum&#95;{i=1}^n (y&#95;i - 18)^2 - 7^2\\)</span>

<details markdown="1"><summary>Solution</summary>

<span class="mc-square mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \frac{1}{n}\sum&#95;{i=1}^n (y&#95;i - 18)^2 - 7^2\\)</span>

There are two key ideas at play here:

-   The mean is the unique point in the dataset such that the sum of deviations from the mean is 0. In other words,

<div class="math-display">
$$
\sum_{i=1}^n (y_i - \bar y) = \sum_{i=1}^n y_i - n \bar y = n \bar y - n \bar y = 0
$$
</div>

-   The variance of a dataset is the average of the squared deviations from the mean. In other words,

<div class="math-display">
$$
\sigma_y^2 = \frac{1}{n} \sum_{i=1}^n (y_i - \bar y)^2
$$
</div>

 Equivalently, this is the value of <span class="math-inline">\\(R&#95;\text{sq}(w)\\)</span> when <span class="math-inline">\\(w = \bar y\\)</span>.

With this in mind, let's look at the options:

**(i)** (**False**) <span class="math-inline">\\(\displaystyle \frac{1}{n} \sum&#95;{i=1}^n (y&#95;i - 15)\\)</span>: This is the average of the deviations from the median, which is not 0. This is only true for the mean.

**(ii)** (**True**) <span class="math-inline">\\(\displaystyle \frac{1}{n} \sum&#95;{i=1}^n (y&#95;i - 18)\\)</span>: This is the average of the deviations from the mean, which is 0. This is only true for the mean.

**(iii)** (**False**) <span class="math-inline">\\(\displaystyle \frac{1}{n}\sum&#95;{i=1}^n (y&#95;i - 15)^2\\)</span>: This is the function <span class="math-inline">\\(R&#95;\text{sq}(w)\\)</span> when <span class="math-inline">\\(w = 15\\)</span>. As we see in the solution to part **a)**, this is not 0.

**(iv)** (**False**) <span class="math-inline">\\(\displaystyle \frac{1}{n}\sum&#95;{i=1}^n (y&#95;i - 18)^2\\)</span>: This is the function <span class="math-inline">\\(R&#95;\text{sq}(w)\\)</span> when <span class="math-inline">\\(w = 18\\)</span>, i.e. it is the variance of the dataset. As we see in the solution to part **a)**, this is also not zero --- here, it is <span class="math-inline">\\(\sigma&#95;y^2 = 7^2 = 49\\)</span>. One point of confusion may be that <span class="math-inline">\\(w = \bar{y}\\)</span> is the point at which <span class="math-inline">\\(R&#95;\text{sq}(w)\\)</span> is minimized and <span class="math-inline">\\(R&#95;\text{sq}(w)\\)</span> has a **derivative** of 0, but <span class="math-inline">\\(R&#95;\text{sq}(\bar y) \neq 0\\)</span> in general.

**(v)** (**False**) <span class="math-inline">\\(\displaystyle \frac{1}{n}\sum&#95;{i=1}^n (y&#95;i - 15)^2 - 7^2\\)</span>: This would be true if the 15 were replaced with the mean, 18, but it is not.

**(vi)** (**True**) <span class="math-inline">\\(\displaystyle \frac{1}{n}\sum&#95;{i=1}^n (y&#95;i - 18)^2 - 7^2\\)</span>: This is the variance of the dataset minus the variance of the dataset, which indeed is 0.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Recall that <span class="math-inline">\\(R&#95;\text{abs}(w)\\)</span> is the mean absolute error of a constant prediction <span class="math-inline">\\(w\\)</span> on the dataset. A snippet of the graph of <span class="math-inline">\\(R&#95;\text{abs}(w)\\)</span> is shown below.

<div style="text-align: center;">
<img src="imgs/line_graph_gray.png" alt="image" style="width: 50%; max-width: 100%;">
</div>

For clarity, the circles at <span class="math-inline">\\((15, 4)\\)</span>, <span class="math-inline">\\((18, 5)\\)</span>, and <span class="math-inline">\\((22, 7)\\)</span> indicate the points at which the slope of <span class="math-inline">\\(R&#95;\text{abs}(w)\\)</span> changes.

Given that there are <span class="math-inline">\\(n = 72\\)</span> values in the dataset, how many values in the dataset are equal to **18**? Show your work and <span class="math-inline">\\(\boxed{\text{circle}}\\)</span> your final answer, which should be an integer with no variables.

<details markdown="1"><summary>Solution</summary>

The number of values in the dataset that are equal to 18 is 6.

Recall, the slope of <span class="math-inline">\\(R&#95;\text{abs}(w)\\)</span> at any <span class="math-inline">\\(w\\)</span> that is not a data point is:

<div class="math-display">
$$
\frac{\text{d}}{\text{d}w} R_\text{abs}(w) = \frac{\# \text{ left of } w - \# \text{ right of } w}{n}
$$
</div>

There are two line segments of interest here: the one between <span class="math-inline">\\(w=15\\)</span> and <span class="math-inline">\\(w=18\\)</span>, and the one between <span class="math-inline">\\(w=18\\)</span> and <span class="math-inline">\\(w=22\\)</span>. We have two ways of computing the slope of each one: by using <span class="math-inline">\\(\text{slope} = \frac{\text{change in } y}{\text{change in } x}\\)</span> and by using the formula above. We'll use both formulas on each line segment.

-   **Between <span class="math-inline">\\(w=15\\)</span> and <span class="math-inline">\\(w=18\\)</span>:**

-   Method 1: Using <span class="math-inline">\\(\text{slope} = \frac{\text{change in } y}{\text{change in } x}\\)</span>, the graph rises from <span class="math-inline">\\((15, 4)\\)</span> to <span class="math-inline">\\((18, 5)\\)</span>, which gives a slope of



<div class="math-display">
$$
s_1 = \frac{5 - 4}{18 - 15} = \frac{1}{3}
$$
</div>

-   Method 2: Using the formula for the slope of <span class="math-inline">\\(R&#95;\text{abs}(w)\\)</span>, let <span class="math-inline">\\(l\\)</span> be the number of values in the dataset less than or equal to 15. Then, the slope in this interval is



<div class="math-display">
$$
s_1 = \frac{l - (72 - l)}{72} = \frac{2l - 72}{72}
$$
</div>

   At this point, we have enough information to solve for <span class="math-inline">\\(l\\)</span>:



<div class="math-display">
$$
\frac{2l - 72}{72} = \frac{1}{3} \implies l = 48
$$
</div>

-   **Between <span class="math-inline">\\(w=18\\)</span> and <span class="math-inline">\\(w=22\\)</span>:**

-   Method 1:

<div class="math-display">
$$
s_2 = \frac{7 - 5}{22 - 18} = \frac{2}{4} = \frac{1}{2}
$$
</div>

-   Method 2: Let <span class="math-inline">\\(k\\)</span> be the number of values in the dataset **equal to** 18. Ultimately, this is what we're trying to find. Then, the number of values in the dataset less than or equal to 18 is <span class="math-inline">\\(l + k\\)</span>. In this interval, the slope is



<div class="math-display">
$$
s_2 = \frac{(l + k) - (72 - (l + k))}{72} = \frac{2(l + k) - 72}{72}
$$
</div>

   So, we need to solve for <span class="math-inline">\\(k\\)</span> in



<div class="math-display">
$$
\frac{2(l + k) - 72}{72}
$$
</div>

   But, we know that <span class="math-inline">\\(l = 48\\)</span>, so



<div class="math-display">
$$
\frac{2(48 + k) - 72}{72} = \frac{1}{2} \implies 96 + 2k - 72 = 36 \implies 2k = 12 \implies \boxed{k = 6}
$$
</div>

Therefore, there are 6 values in the dataset that are equal to 18.
</details>

</div>
</div>

</div>
