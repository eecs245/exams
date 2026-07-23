---
layout: minimal
title: "Winter 2026 Midterm 1"
description: "Midterm 1 problems."
nav_exclude: true
hide_footer_hr: true
---

{% raw %}

<script>
window.MathJax = {
  tex: {inlineMath: [['$', '$'], ['\\(', '\\)']]}
};
</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js" async></script>

<style>
.main-content p {
  margin-bottom: 1.15em;
}
.assignment-pdf-button {
  font-size: 0.95rem;
  padding: 0.35rem 0.65rem;
}
.assignment-actions {
  align-items: center;
  display: flex;
  flex-wrap: wrap;
  gap: 0.55rem;
  margin: 0 0 1rem;
}
.math-display,
mjx-container[jax="CHTML"][display="true"] {
  max-width: 100%;
  overflow-x: auto;
  overflow-y: hidden;
}
.math-display {
  padding-bottom: 0.2rem;
}
.math-display mjx-container[jax="CHTML"][display="true"] {
  padding-bottom: 0.2rem;
}
.answer-blank {
  border-bottom: 1px solid currentColor;
  display: inline-block;
  min-width: 8rem;
  height: 1em;
  vertical-align: baseline;
}
.assignment-parts {
  margin: 1rem 0;
}
.assignment-part {
  column-gap: 0.55rem;
  display: grid;
  grid-template-columns: 1.4rem minmax(0, 1fr);
  margin-bottom: 1.05rem;
}
.assignment-part-label {
  font-weight: 600;
  text-align: right;
}
.assignment-part-content > :first-child {
  margin-top: 0;
}
.mc-options {
  display: flex;
  flex-wrap: wrap;
  gap: 0.9rem 1.6rem;
  margin: 0.9rem 0 1.1rem;
}
.mc-option {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  white-space: nowrap;
}
.mc-bubble,
.mc-square {
  display: inline-block;
  flex: 0 0 auto;
  height: 0.95em;
  width: 0.95em;
  vertical-align: -0.12em;
}
.mc-bubble {
  border: 1.5px solid currentColor;
  border-radius: 50%;
}
.mc-square {
  border: 1.5px solid currentColor;
}
.mc-correct {
  background: currentColor;
}
.main-content table {
  font-size: 0.9rem;
  width: auto;
  max-width: 100%;
}
.main-content table th,
.main-content table td {
  padding: 0.35rem 0.5rem;
  white-space: nowrap;
}
</style>

# Winter 2026 Midterm 1

**administered**

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/exams/wn26-mt1.pdf" target="_blank">View as PDF ✏️</a>
<a class="btn btn-info assignment-pdf-button" href="/resources/exams/wn26-mt1-solutions.pdf" target="_blank">Solutions PDF ✅</a>
</div>

{: .yellow }
<div markdown="1">
**Instructions**

-   This exam consists of 7 problems, worth a total of 100 points, spread across 12 pages (6 sheets of paper).

-   You have 120 minutes to complete this exam, unless you have extended-time accommodations through SSD.

-   Write your uniqname in the top right corner of each page.

-   For free response problems, **you must show all of your work**, and <span class="math-inline">\\(\boxed{\text{circle}}\\)</span> your final answer. We will not grade work that appears elsewhere, and you may lose points if your work is not shown.

-   For multiple choice problems, completely fill in bubbles and square boxes; if we cannot tell which option(s) you selected, you may lose points.



-   You may refer to **one double-sided 8.5x11" handwritten notes sheet**. Other than that, you may not refer to any other resources or technology during the exam (no phones, watches, or calculators).
</div>

---

## Problems

- [Problem 1](#problem-1-16-pts)
- [Problem 2](#problem-2-14-pts)
- [Problem 3](#problem-3-12-pts)
- [Problem 4](#problem-4-12-pts)
- [Problem 5](#problem-5-12-pts)
- [Problem 6](#problem-6-14-pts)
- [Problem 7](#problem-7-20-pts)

---

## Problem 1 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">16 pts</span>

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

---

## Problem 2 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">14 pts</span>

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

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(M \leq \sigma&#95;y^2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(M = \sigma&#95;y^2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(M \geq \sigma&#95;y^2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Impossible to tell</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(M \leq \sigma&#95;y^2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(M = \sigma&#95;y^2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(M \geq \sigma&#95;y^2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Impossible to tell</span></div>

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

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> False</span></div>

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

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

The values of <span class="math-inline">\\(w&#95;0\\)</span> and <span class="math-inline">\\(w&#95;1\\)</span> that minimize <span class="math-inline">\\(R&#95;\text{sq}(w&#95;0, w&#95;1)\\)</span> are unique, but we're not discussing the minimizers here, so that fact is irrelevant.

Instead, it's asking whether it's possible for there to be multiple pairs of <span class="math-inline">\\((w&#95;0, w&#95;1)\\)</span> with a mean squared error of something bigger than <span class="math-inline">\\(M\\)</span>. The <span class="math-inline">\\(+1\\)</span> is not important; we could have stated <span class="math-inline">\\(+17\\)</span> or <span class="math-inline">\\(+3\pi^2\\)</span> and the question would be the same.

Recall from [Chapter 2.3](https://notes.eecs245.org/simple-linear-regression/finding-optimal-parameters/) that the graph of <span class="math-inline">\\(R&#95;\text{sq}(w&#95;0, w&#95;1)\\)</span> looks like a bowl in <span class="math-inline">\\(\mathbb{R}^3\\)</span>. While there's only one point at which the bowl is minimized, for any height (<span class="math-inline">\\(z\\)</span>-value) greater than <span class="math-inline">\\(M\\)</span>, there are infinitely many pairs of <span class="math-inline">\\((w&#95;0, w&#95;1)\\)</span> that give that height. To see this, imagine slicing the bowl with the plane <span class="math-inline">\\(z = M + 1\\)</span>. This slice is an ellipse (stretched circle), upon which infinitely many combinations of <span class="math-inline">\\((w&#95;0, w&#95;1)\\)</span> lie.

So, yes, it is possible for there to be multiple pairs of <span class="math-inline">\\((w&#95;0, w&#95;1)\\)</span> with a mean squared error of <span class="math-inline">\\(M + 1\\)</span> --- in fact, that's guaranteed.
</details>

</div>
</div>

</div>

---

## Problem 3 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>

Consider the following two planes, <span class="math-inline">\\(P&#95;1\\)</span> and <span class="math-inline">\\(P&#95;2\\)</span>, in <span class="math-inline">\\(\mathbb{R}^3\\)</span>.

-   <span class="math-inline">\\(P&#95;1\\)</span> is the plane spanned by the vectors <span class="math-inline">\\(\begin{bmatrix} 3 \\\\ 2 \\\\ 0 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\begin{bmatrix} 6 \\\\ -4 \\\\ -3 \end{bmatrix}\\)</span>.

-   <span class="math-inline">\\(P&#95;2\\)</span> is the plane defined by the equation <span class="math-inline">\\(5x + 3y - z = 0\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Find the equation of <span class="math-inline">\\(P&#95;1\\)</span> in standard form, i.e. <span class="math-inline">\\(ax + by + cz + d = 0\\)</span>. Show your work and <span class="math-inline">\\(\boxed{\text{circle}}\\)</span> your final answer.

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(2x - 3y + 8z = 0\\)</span>.

As discussed in [Chapter 4.4](https://notes.eecs245.org/linear-independence/lines-planes-hyperplanes/), the solution is to take the cross product of the two vectors used to span the plane; this will give us a vector <span class="math-inline">\\(\begin{bmatrix} a \\\\ b \\\\ c \end{bmatrix}\\)</span> that is orthogonal to both vectors, and therefore both will satisfy <span class="math-inline">\\(ax + by + cz + d = 0\\)</span>. We know <span class="math-inline">\\(d = 0\\)</span> since the span of a set of vectors must contain the origin.

<div class="math-display">
$$
\begin{bmatrix} 3 \\\\ 2 \\\\ 0 \end{bmatrix} \times \begin{bmatrix} 6 \\\\ -4 \\\\ -3 \end{bmatrix} = \begin{bmatrix} 2 \cdot (-3) - 0 \cdot (-4) \\\\ 0 \cdot 6 - 3 \cdot (-3) \\\\ 3 \cdot (-4) - 2 \cdot 6 \end{bmatrix} = \begin{bmatrix} -6 \\\\ 9 \\\\ -24 \end{bmatrix}
$$
</div>

So, the equation of <span class="math-inline">\\(P&#95;1\\)</span> is <span class="math-inline">\\(-6x + 9y - 24z = 0\\)</span>, or simplified, <span class="math-inline">\\(\boxed{2x - 3y + 8z = 0}\\)</span>. To verify, we should plug in both vectors to make sure they satisfy the equation:

<div class="math-display">
$$
2(3) - 3(2) + 8(0) = 6 - 6 + 0 = 0, \qquad 2(6) - 3(-4) + 8(-3) = 12 + 12 - 24 = 0
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Planes <span class="math-inline">\\(P&#95;1\\)</span> and <span class="math-inline">\\(P&#95;2\\)</span> intersect at a line. Find the equation of this line in parametric form. Show your work and <span class="math-inline">\\(\boxed{\text{circle}}\\)</span> your final answer. <em>Hint: This can be done without knowing the answer to the previous part.</em>

<details markdown="1"><summary>Solution</summary>

<div class="math-display">
$$
L = t \begin{bmatrix} 1 \\\\ -2 \\\\ -1 \end{bmatrix}, \quad t \in \mathbb{R}
$$
</div>

 (where the direction vector could be scaled by any non-zero scalar)

There are a few possible techniques here.

**(i)** We can find the intersection of the two planes by solving the system of equations:

<div class="math-display">
$$
\begin{align*}
5x + 3y - z   &= 0 \\\\
2x - 3y + 8z &= 0
\end{align*}
$$
</div>

Adding both equations gives

<div class="math-display">
$$
7x + 7z = 0 \implies z = -x
$$
</div>

We know that the system will have infinitely many solutions, so we can let our "parameter" be <span class="math-inline">\\(x\\)</span>. So far, we know two of the three components of the line: <span class="math-inline">\\(x\\)</span> is the free variable, and <span class="math-inline">\\(z = -x\\)</span>. Finally, let's solve for <span class="math-inline">\\(y\\)</span> in terms of <span class="math-inline">\\(x\\)</span>.

<div class="math-display">
$$
5x + 3y + x = 0 \implies 6x + 3y = 0 \implies y = - 2x
$$
</div>

Therefore, the parametric equation of the line is

<div class="math-display">
$$
L = \begin{bmatrix} x \\\\ -2x \\\\ -x \end{bmatrix} = x \begin{bmatrix} 1 \\\\ -2 \\\\ -1 \end{bmatrix}, \quad x \in \mathbb{R}
$$
</div>

**(ii)** Another solution is to recognize that any point on the first plane can be written as a linear combination of the two vectors that span the plane, i.e.

<div class="math-display">
$$
s \begin{bmatrix} 3 \\\\ 2 \\\\ 0 \end{bmatrix} + t \begin{bmatrix} 6 \\\\ -4 \\\\ -3 \end{bmatrix} = \begin{bmatrix} 3s + 6t \\\\ 2s - 4t \\\\ -3t \end{bmatrix}
$$
</div>

Any vector on the first plane can be written in the form above. For a vector to be in both planes (i.e. in the intersection), it must be able to be written in the form above **and** satisfy the equation of the second plane, <span class="math-inline">\\(5x + 3y - z = 0\\)</span>.

<div class="math-display">
$$
\begin{align*}
5(3s + 6t) + 3(2s - 4t) - (-3t) &= 0 \\\\
15s + 30t + 6s - 12t + 3t &= 0 \\\\
21s + 21t &= 0 \\\\
t &= -s
\end{align*}
$$
</div>

So, as long as we pick <span class="math-inline">\\(s\\)</span> and <span class="math-inline">\\(t\\)</span> such that <span class="math-inline">\\(t = -s\\)</span>, the resulting vector, <span class="math-inline">\\(\begin{bmatrix} 3s + 6t \\\\ 2s - 4t \\\\ -3t \end{bmatrix}\\)</span>, will be in both planes. There are infinitely many pairs of such <span class="math-inline">\\(s\\)</span> and <span class="math-inline">\\(t\\)</span> -- <span class="math-inline">\\(1\\)</span> and <span class="math-inline">\\(-1\\)</span>, <span class="math-inline">\\(2\\)</span> and <span class="math-inline">\\(-2\\)</span>, etc. -- and these fill out the line of intersection. To find one of them, let <span class="math-inline">\\(s = 1\\)</span> and <span class="math-inline">\\(t = -1\\)</span>:

<div class="math-display">
$$
\begin{bmatrix} 3(1) + 6(-1) \\\\ 2(1) - 4(-1) \\\\ -3(-1) \end{bmatrix} = \begin{bmatrix} 3 - 6 \\\\ 2 + 4 \\\\ 3 \end{bmatrix} = \begin{bmatrix} -3 \\\\ 6 \\\\ 3 \end{bmatrix}
$$
</div>

Therefore, the parametric equation of the line is

<div class="math-display">
$$
L = t \begin{bmatrix} -3 \\\\ 6 \\\\ 3 \end{bmatrix}, \quad t \in \mathbb{R}
$$
</div>

which is equivalent to

<div class="math-display">
$$
L = t \begin{bmatrix} 1 \\\\ -2 \\\\ -1 \end{bmatrix}, \quad t \in \mathbb{R}
$$
</div>

This is the same line we found earlier, just with a scaled direction vector, which doesn't change the line.

**(iii)** A final solution is to (1) find a vector that is perpendicular to each plane (i.e. a normal vector), and (2) take the cross product of those two vectors. This will give us a vector that is in both planes, and therefore spans the intersecting line, which we know must also pass through the origin.

<div class="math-display">
$$
\begin{align*}
\begin{bmatrix} 5 \\\\ 3 \\\\ -1 \end{bmatrix} \times \begin{bmatrix} 2 \\\\ -3 \\\\ 8 \end{bmatrix} = \begin{bmatrix} 3 \cdot 8 - (-1) \cdot (-3) \\\\ (-1) \cdot 2 - 5 \cdot 8 \\\\ 5 \cdot (-3) - 3 \cdot 2 \end{bmatrix} = \begin{bmatrix} 21 \\\\ -42 \\\\ -21 \end{bmatrix} = 21 \begin{bmatrix} 1 \\\\ -2 \\\\ -1 \end{bmatrix}
\end{align*}
$$
</div>

So, once again, we find that <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ -2 \\\\ -1 \end{bmatrix}\\)</span> is a direction vector for the line of intersection.
</details>

</div>
</div>

</div>

---

## Problem 4 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>

Suppose <span class="math-inline">\\(\vec u = \begin{bmatrix} 1 \\\\ 0 \\\\ 0 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec u + \vec v + \vec w = \begin{bmatrix} 4 \\\\ 0 \\\\ 0 \end{bmatrix}\\)</span>. Assume that none of <span class="math-inline">\\(\vec u\\)</span>, <span class="math-inline">\\(\vec v\\)</span>, or <span class="math-inline">\\(\vec w\\)</span> are the zero vector, <span class="math-inline">\\(\vec 0\\)</span>.

For each statement below, identify whether it is **impossible**, **possible**, or **guaranteed**, and provide a brief explanation in the box provided.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span>
<span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> are orthogonal.

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Impossible</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Possible</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Guaranteed</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Impossible</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> Possible</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Guaranteed</span></div>

This is possible.

There is nothing stopping <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> from being orthogonal. For example, let <span class="math-inline">\\(\vec v = \begin{bmatrix} 0 \\\\ 1 \\\\ 0 \end{bmatrix}\\)</span>. Then, <span class="math-inline">\\(\vec u \cdot \vec v = 0 \cdot 0 + 0 \cdot 1 + 0 \cdot 0 = 0\\)</span>, so <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> are orthogonal, and we can still find a <span class="math-inline">\\(\vec w\\)</span> such that <span class="math-inline">\\(\vec u + \vec v + \vec w = \begin{bmatrix} 4 \\\\ 0 \\\\ 0 \end{bmatrix}\\)</span>. For example, let <span class="math-inline">\\(\vec w = \begin{bmatrix} 4 \\\\ 0 \\\\ 0 \end{bmatrix} - \vec u - \vec v = \begin{bmatrix} 3 \\\\ -1 \\\\ 0 \end{bmatrix}\\)</span>.

However, it's not guaranteed: <span class="math-inline">\\(\vec v = \begin{bmatrix} 2 \\\\ 0 \\\\ 0 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec w = \begin{bmatrix} 1 \\\\ 0 \\\\ 0 \end{bmatrix}\\)</span> satisfy <span class="math-inline">\\(\vec u + \vec v + \vec w = \begin{bmatrix} 4 \\\\ 0 \\\\ 0 \end{bmatrix}\\)</span>, but <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> are not orthogonal.

So, it is possible for <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> to be orthogonal.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> The set <span class="math-inline">\\(\lbrace\vec u, \vec v, \vec w\rbrace\\)</span> is linearly dependent.

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Impossible</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Possible</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Guaranteed</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Impossible</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Possible</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> Guaranteed</span></div>

This is guaranteed.

<div class="math-display">
$$
\vec u + \vec v + \vec w = \begin{bmatrix} 4 \\\\ 0 \\\\ 0 \end{bmatrix}
$$
</div>

Since <span class="math-inline">\\(\vec u = \begin{bmatrix} 1 \\\\ 0 \\\\ 0 \end{bmatrix}\\)</span>, we can subtract <span class="math-inline">\\(4 \vec u\\)</span> from both sides to get

<div class="math-display">
$$
\vec u + \vec v + \vec w - 4 \vec u = \vec w - 3 \vec u = \begin{bmatrix} 4 \\\\ 0 \\\\ 0 \end{bmatrix} - 4 \begin{bmatrix} 1 \\\\ 0 \\\\ 0 \end{bmatrix}
$$
</div>

Or, equivalently,

<div class="math-display">
$$
- 3 \vec u + \vec v + \vec w = \vec 0
$$
</div>

This is a non-trivial linear combination of <span class="math-inline">\\(\vec u\\)</span>, <span class="math-inline">\\(\vec v\\)</span>, and <span class="math-inline">\\(\vec w\\)</span> that equals the zero vector, so the set <span class="math-inline">\\(\lbrace\vec u, \vec v, \vec w\rbrace\\)</span> is linearly dependent. Equivalently, we could say <span class="math-inline">\\(\vec w = 3 \vec u - \vec v\\)</span>, which means <span class="math-inline">\\(\vec w\\)</span> is a linear combination of <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span>, which also means the set is linearly dependent.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span>
<span class="math-inline">\\(\vec u\\)</span>, <span class="math-inline">\\(\vec v\\)</span>, and <span class="math-inline">\\(\vec w\\)</span> all have the same norm (length).

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Impossible</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Possible</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Guaranteed</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> Impossible</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Possible</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Guaranteed</span></div>

This is impossible.

Recall that the triangle inequality states that for any two vectors <span class="math-inline">\\(\vec v\\)</span> and <span class="math-inline">\\(\vec w\\)</span>,

<div class="math-display">
$$
\lVert \vec v + \vec w \rVert \leq \lVert \vec v \rVert + \lVert \vec w \rVert
$$
</div>

We know that <span class="math-inline">\\(\lVert \vec u \rVert = 1\\)</span>, so in order for the statement to be possible, we'd need both <span class="math-inline">\\(\lVert \vec v \rVert = 1\\)</span> and <span class="math-inline">\\(\lVert \vec w \rVert = 1\\)</span>. But, <span class="math-inline">\\(\vec v + \vec w = \begin{bmatrix} 3 \\\\ 0 \\\\ 0 \end{bmatrix}\\)</span>, so <span class="math-inline">\\(\lVert \vec v + \vec w \rVert = \sqrt{3^2 + 0^2 + 0^2} = \sqrt{9} = 3\\)</span>. In the triangle inequality, this would mean

<div class="math-display">
$$
\lVert \vec v + \vec w \rVert \leq \lVert \vec v \rVert + \lVert \vec w \rVert \implies 3 \leq 2
$$
</div>

This is a contradiction, so it is impossible for both <span class="math-inline">\\(\vec v\\)</span> and <span class="math-inline">\\(\vec w\\)</span> to have a norm of 1, and therefore impossible for all three vectors to have the same norm.
</details>

</div>
</div>

</div>

---

## Problem 5 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>

Suppose <span class="math-inline">\\(\vec u, \vec v \in \mathbb{R}^n\\)</span>. Let <span class="math-inline">\\(\vec p\\)</span> be the projection of <span class="math-inline">\\(\vec u\\)</span> onto <span class="math-inline">\\(\vec v\\)</span>. Furthermore, we know that:

<div class="math-display">
$$
\underbrace{\lVert \vec v \rVert = 2}_{\text{length of } \vec v \: (\text{not } \vec u)} \qquad \lVert \vec p \rVert = 3
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Find <span class="math-inline">\\(| \vec u \cdot \vec v |\\)</span>. Show your work and <span class="math-inline">\\(\boxed{\text{circle}}\\)</span> your final answer, which should be a number with no variables.

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(|\vec u \cdot \vec v| = 6\\)</span>.

Let's start with the formula for <span class="math-inline">\\(\vec p\\)</span>.

<div class="math-display">
$$
\vec p = \frac{\vec u \cdot \vec v}{\vec v \cdot \vec v} \vec v = \frac{\vec u \cdot \vec v}{\lVert \vec v \rVert^2} \vec v
$$
</div>

We know that <span class="math-inline">\\(\lVert \vec p \rVert = 3\\)</span>, so let's try and find the magnitude of <span class="math-inline">\\(\vec p\\)</span> in the formula above, which will allow us to learn more about <span class="math-inline">\\(\vec u \cdot \vec v\\)</span>.

The key to remember that <span class="math-inline">\\(\lVert k x \rVert = |k| \lVert x \rVert\\)</span> for any scalar <span class="math-inline">\\(k\\)</span> and vector <span class="math-inline">\\(x\\)</span>. The absolute value is necessary because the scalar <span class="math-inline">\\(k\\)</span> could be negative, but the length of a vector is always non-negative.

<div class="math-display">
$$
\lVert \vec p \rVert = \left| \frac{\vec u \cdot \vec v}{\lVert \vec v \rVert^2} \right| \lVert \vec v \rVert = \left| \frac{\vec u \cdot \vec v}{2^2} \right| 2 = \left| \frac{\vec u \cdot \vec v}{4} \right| 2 = \frac{\left| \vec u \cdot \vec v \right|}{2}
$$
</div>

So, we know that <span class="math-inline">\\(\frac{\left| \vec u \cdot \vec v \right|}{2} = 3\\)</span>, which means that <span class="math-inline">\\(\boxed{\left| \vec u \cdot \vec v \right| = 6}\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> For each pair of vectors, determine whether they are orthogonal, linearly dependent, or neither. Make sure to select **one bubble per row**.

|  | pair of vectors | orthogonal | linearly dependent | neither |
|:--:|:---|:--:|:--:|:--:|
| <span class="math-inline">\\(i\\)</span> | <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec u - \vec p\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> |
| <span class="math-inline">\\(ii\\)</span> | <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v - \vec p\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> |
| <span class="math-inline">\\(iii\\)</span> | <span class="math-inline">\\(\vec v\\)</span> and <span class="math-inline">\\(\vec u - \vec p\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> |
| <span class="math-inline">\\(iv\\)</span> | <span class="math-inline">\\(\vec v\\)</span> and <span class="math-inline">\\(\vec v - \vec p\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> |
| <span class="math-inline">\\(v\\)</span> | <span class="math-inline">\\(\vec p\\)</span> and <span class="math-inline">\\(\vec u - \vec p\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> |
| <span class="math-inline">\\(vi\\)</span> | <span class="math-inline">\\(\vec p\\)</span> and <span class="math-inline">\\(\vec v - \vec p\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> |

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"></div>

The key fact about orthogonality when it comes to projections is that the error vector --- here, <span class="math-inline">\\(\vec e = \vec u - \vec p\\)</span> --- is orthogonal to the vector we're projecting onto, <span class="math-inline">\\(\vec v\\)</span>.

This means that <span class="math-inline">\\(\vec v\\)</span> and <span class="math-inline">\\(\vec u - \vec p\\)</span> are orthogonal (iii). But, <span class="math-inline">\\(\vec p\\)</span> is a scalar multiple of <span class="math-inline">\\(\vec v\\)</span>, so <span class="math-inline">\\(\vec p\\)</span> and <span class="math-inline">\\(\vec u - \vec p\\)</span> are also orthogonal (v).

Remember that <span class="math-inline">\\(\vec p\\)</span> is a scalar multiple of <span class="math-inline">\\(\vec v\\)</span>, so <span class="math-inline">\\(\vec v - \vec p\\)</span> is a scalar multiple of <span class="math-inline">\\(\vec v\\)</span> too. So, <span class="math-inline">\\(\vec v\\)</span> and <span class="math-inline">\\(\vec v - \vec p\\)</span> are linearly dependent (iv), as are <span class="math-inline">\\(\vec p\\)</span> and <span class="math-inline">\\(\vec v - \vec p\\)</span> (vi).

Now, we need to address (i) and (ii), which ask about <span class="math-inline">\\(\vec u\\)</span>'s relation to <span class="math-inline">\\(\vec u - \vec p\\)</span> and <span class="math-inline">\\(\vec v - \vec p\\)</span>, respectively. <span class="math-inline">\\(\vec u - \vec p\\)</span> is the error vector of the projection, which in general is orthogonal to <span class="math-inline">\\(\vec v\\)</span> and neither orthogonal nor linearly dependent with <span class="math-inline">\\(\vec u\\)</span>.

The only possible "edge case" here is when <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> are orthogonal, in which case <span class="math-inline">\\(\vec p = \frac{\vec u \cdot \vec v}{\vec v \cdot \vec v} \vec v = \frac{0}{\vec v \cdot \vec v} \vec v = \vec 0\\)</span>, which would mean that <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v - \vec p\\)</span> are orthogonal and <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec u - \vec p\\)</span> are the same vector and thus linearly dependent. However, we know that <span class="math-inline">\\(\vec p \neq \vec 0\\)</span> since <span class="math-inline">\\(\lVert \vec p \rVert = 3 &gt; 0\\)</span>. So, this edge case doesn't apply to this problem, and therefore <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec u - \vec p\\)</span> are neither orthogonal nor linearly dependent (i), and same with <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v - \vec p\\)</span> (ii).
</details>

</div>
</div>

</div>

---

## Problem 6 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">14 pts</span>

Suppose <span class="math-inline">\\(\vec x&#95;1, \vec x&#95;2, \vec x&#95;3, \vec x&#95;4, \vec x&#95;5, \vec x&#95;6\\)</span> are 6 vectors in <span class="math-inline">\\(\mathbb{R}^9\\)</span> such that

<div class="math-display">
$$
S = \text{span}\left(\{\vec x_1, \vec x_2, \vec x_3, \vec x_4, \vec x_5, \vec x_6\}\right)
$$
</div>

 is a **4-dimensional** subspace of <span class="math-inline">\\(\mathbb{R}^9\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">2 pts</span> True or False: The set <span class="math-inline">\\(\lbrace\vec x&#95;1, \vec x&#95;2, \vec x&#95;3, \vec x&#95;4, \vec x&#95;5, \vec x&#95;6\rbrace\\)</span> is linearly independent.

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> False</span></div>

This is false.

If these vectors were linearly independent, they would span a 6-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^9\\)</span>; since they only span a 4-dimensional subspace, they must be linearly dependent, and two of them are "redundant".
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Consider the statement:

"There exists a vector <span class="math-inline">\\(\vec b \in \mathbb{R}^9\\)</span> such that the number of ways to write <span class="math-inline">\\(\vec b\\)</span> as a linear combination of <span class="math-inline">\\(\vec x&#95;1, \ldots, \vec x&#95;6\\)</span> is ."

In each part below, a possible way to fill in the blank is given. Determine whether the statement that results from filling in the blank is **True** or **False**.

1.  zero

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

2.  exactly one

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

3.  exactly two

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

4.  infinite

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

-   **(True) zero ways**: <span class="math-inline">\\(S\\)</span>, the set of all linear combinations of <span class="math-inline">\\(\vec x&#95;1, \ldots, \vec x&#95;6\\)</span>, is a 4-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^9\\)</span>. Since <span class="math-inline">\\(S\\)</span> isn't all of <span class="math-inline">\\(\mathbb{R}^9\\)</span>, there are plenty of vectors <span class="math-inline">\\(\vec b \in \mathbb{R}^9\\)</span> that are not in <span class="math-inline">\\(S\\)</span>, and therefore can't be written as a linear combination of <span class="math-inline">\\(\vec x&#95;1, \ldots, \vec x&#95;6\\)</span>. So, it's true that there are some <span class="math-inline">\\(\vec b\\)</span>'s such that there are zero ways to write <span class="math-inline">\\(\vec b\\)</span> as a linear combination of <span class="math-inline">\\(\vec x&#95;1, \ldots, \vec x&#95;6\\)</span>.

-   **(False) exactly one way**: Linear combinations are only unique if the spanning vectors are linearly independent. Since <span class="math-inline">\\(\vec x&#95;1, \ldots, \vec x&#95;6\\)</span> are linearly dependent, there is a non-trivial linear combination of them that equals the zero vector, which could be added to any other existing linear combination that sums to <span class="math-inline">\\(\vec b\\)</span> to "invent" a new, different-looking linear combination that sums to <span class="math-inline">\\(\vec b\\)</span>. So, it's false that there is exactly one way to write <span class="math-inline">\\(\vec b\\)</span> as a linear combination of <span class="math-inline">\\(\vec x&#95;1, \ldots, \vec x&#95;6\\)</span> --- if there is one way, there are infinitely many.

-   **(False) exactly two ways**: Same logic as above. If this thinking is a bit confusing, see the solution to part **c)**.

-   **(True) infinite ways**: For any vector <span class="math-inline">\\(\vec b \in S\\)</span>, there are infinitely many ways to write <span class="math-inline">\\(\vec b\\)</span> as a linear combination of <span class="math-inline">\\(\vec x&#95;1, \ldots, \vec x&#95;6\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Suppose <span class="math-inline">\\(\vec b\\)</span> is some vector in <span class="math-inline">\\(S\\)</span> such that both of the following equations are true:

<div class="math-display">
$$

$$
</div>

\begin{aligned}
\vec b &= 4 \vec x_1 - 2 \vec x_2 + 6 \vec x_3

\vec b &= 3 \vec x_1 + 3 \vec x_3 - \vec x_5
\end{aligned}

<div class="math-display">
$$

$$
</div>

State **one** other linear combination of <span class="math-inline">\\(\vec x&#95;1, \ldots, \vec x&#95;6\\)</span> that is equal to <span class="math-inline">\\(\vec b\\)</span>. Fill in each box with a number with no variables.

<span class="math-inline">\\(\vec b = \minibox{1.5cm}{7/2}  \vec x&#95;1 + \minibox{1.5cm}{-1}  \vec x&#95;2 + \minibox{1.5cm}{9/2}  \vec x&#95;3 + \minibox{1.5cm}{0}  \vec x&#95;4 + \minibox{1.5cm}{-1/2}  \vec x&#95;5 + \minibox{1.5cm}{0}  \vec x&#95;6\\)</span>

<details markdown="1"><summary>Solution</summary>

Arguably, answering part **c)** may have helped clarify the answer to part **b)**.

Let's try adding the two representation of <span class="math-inline">\\(\vec b\\)</span> together.

<div class="math-display">
$$

$$
</div>

\begin{aligned}
\vec b &= 4 \vec x_1 - 2 \vec x_2 + 6 \vec x_3

\vec b &= 3 \vec x_1 + 3 \vec x_3 - \vec x_5

\implies 2 \vec b &= 7 \vec x_1 - 2 \vec x_2 + 9 \vec x_3 - \vec x_5
\end{aligned}

<div class="math-display">
$$

$$
</div>

Dividing both sides by 2 gives us

<div class="math-display">
$$
\boxed{\vec b = \frac{7}{2} \vec x_1 - \vec x_2 + \frac{9}{2} \vec x_3 - \frac{1}{2} \vec x_5}
$$
</div>

This is not the only possible answer, but it's probably the easiest one. For example, you could repeat this process with one of the original two <span class="math-inline">\\(\vec b\\)</span>'s along with the new representation of <span class="math-inline">\\(\vec b\\)</span> to get another valid representation of <span class="math-inline">\\(\vec b\\)</span>.

You also could have subtracted the two representations of <span class="math-inline">\\(\vec b\\)</span> to get a linear combination of <span class="math-inline">\\(\vec x&#95;1, \ldots, \vec x&#95;6\\)</span> that equals the zero vector, which could be added to any other existing linear combination that sums to <span class="math-inline">\\(\vec b\\)</span> to "invent" a new, different-looking linear combination that sums to <span class="math-inline">\\(\vec b\\)</span> (as we said in the solution to part **b)**). If you did this, you'd find that

<div class="math-display">
$$
\vec 0 = \vec x_1 - 2 \vec x_2 + 3 \vec x_3 + \vec x_5
$$
</div>

This must mean that

<div class="math-display">
$$
\vec b + \vec 0 = (4 \vec x_1 - 2 \vec x_2 + 6 \vec x_3) + (\vec x_1 - 2 \vec x_2 + 3 \vec x_3 + \vec x_5) = 5 \vec x_1 - 4 \vec x_2 + 9 \vec x_3 + \vec x_5
$$
</div>

is another way to represent <span class="math-inline">\\(\vec b\\)</span> as a linear combination of <span class="math-inline">\\(\vec x&#95;1, \ldots, \vec x&#95;6\\)</span>,

and so is

<div class="math-display">
$$
\vec b + 245 (\vec 0) = (4 \vec x_1 - 2 \vec x_2 + 6 \vec x_3) + 245(\vec x_1 - 2 \vec x_2 + 3 \vec x_3 + \vec x_5)
$$
</div>

(for instance).
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Let <span class="math-inline">\\(T = \text{span}(\lbrace \vec x&#95;1, \vec x&#95;2, \vec x&#95;3 \rbrace)\\)</span> and <span class="math-inline">\\(U = \text{span}(\lbrace \vec x&#95;4, \vec x&#95;5, \vec x&#95;6 \rbrace)\\)</span>. Suppose <span class="math-inline">\\(W\\)</span> is the **intersection** of <span class="math-inline">\\(T\\)</span> and <span class="math-inline">\\(U\\)</span>, i.e. <span class="math-inline">\\(W = T \cap U\\)</span>. <span class="math-inline">\\(W\\)</span> is also a subspace of <span class="math-inline">\\(\mathbb{R}^9\\)</span>.

What are the smallest and largest possible values of <span class="math-inline">\\(\text{dim}(W)\\)</span>, the dimension of <span class="math-inline">\\(W\\)</span>? Give your answers as integers.

<span class="math-inline">\\(=\\)</span> <span class="math-inline">\\(=\\)</span>

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(T\\)</span> and <span class="math-inline">\\(U\\)</span> are each individually at most 3-dimensional, since they are each spanned by 3 vectors. So, the intersection <span class="math-inline">\\(W\\)</span> must be at most 3-dimensional. This means the possible dimensions to consider are 3, 2, 1, or 0. Let's reason about them, starting with 3.

To give examples, we'll use the standard basis vectors <span class="math-inline">\\(\vec e&#95;1, \vec e&#95;2, \ldots, \vec e&#95;9\\)</span> of <span class="math-inline">\\(\mathbb{R}^9\\)</span>. In <span class="math-inline">\\(\mathbb{R}^2\\)</span>, <span class="math-inline">\\(\vec e&#95;1 = \begin{bmatrix} 1 \\\\ 0 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec e&#95;2 = \begin{bmatrix} 0 \\\\ 1 \end{bmatrix}\\)</span>, so (for instance) in <span class="math-inline">\\(\mathbb{R}^9\\)</span>,

<div class="math-display">
$$
\vec e_5 = \begin{bmatrix} 0 \\\\ 0 \\\\ 0 \\\\ 0 \\\\ 1 \\\\ 0 \\\\ 0 \\\\ 0 \\\\ 0 \end{bmatrix}
$$
</div>

-   Could <span class="math-inline">\\(\text{dim}(W) = 3\\)</span>? **No**. If <span class="math-inline">\\(\text{dim}(W) = 3\\)</span>, it would mean that <span class="math-inline">\\(T\\)</span> and <span class="math-inline">\\(U\\)</span> are both **the same** 3-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^9\\)</span>, and intersect everywhere. But if that were the case, then <span class="math-inline">\\(S = \text{span}(\lbrace \vec x&#95;1, \vec x&#95;2, \vec x&#95;3, \vec x&#95;4, \vec x&#95;5, \vec x&#95;6 \rbrace)\\)</span> would be a 3-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^9\\)</span>, which contradicts the problem statement that <span class="math-inline">\\(S\\)</span> is a 4-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^9\\)</span>. So, <span class="math-inline">\\(\text{dim}(W) &lt; 3\\)</span>, and the maximum possible value is something less than 3.

-   Could <span class="math-inline">\\(\text{dim}(W) = 2\\)</span>? **Yes**, and all smaller values are also possible. <span class="math-inline">\\(T\\)</span> and <span class="math-inline">\\(U\\)</span> could overlap in a 2-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^9\\)</span>, while each containing a direction that the other doesn't.

   For example, <span class="math-inline">\\(T\\)</span> could be the span of <span class="math-inline">\\(\lbrace\vec e&#95;1, \vec e&#95;2, \vec e&#95;3\rbrace\\)</span> and <span class="math-inline">\\(U\\)</span> could be the span of <span class="math-inline">\\(\lbrace\vec e&#95;2, \vec e&#95;3, \vec e&#95;4\rbrace\\)</span>. In this case, <span class="math-inline">\\(W\\)</span> would be the span of <span class="math-inline">\\(\lbrace\vec e&#95;2, \vec e&#95;3\rbrace\\)</span>, which is a 2-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^9\\)</span>.

-   Could <span class="math-inline">\\(\text{dim}(W) = 1\\)</span>? **Yes**. For example, <span class="math-inline">\\(T\\)</span> could be the span of <span class="math-inline">\\(\lbrace\vec e&#95;1, \vec e&#95;2\rbrace\\)</span> and <span class="math-inline">\\(U\\)</span> could be the span of <span class="math-inline">\\(\lbrace\vec e&#95;2, \vec e&#95;3, \vec e&#95;4 \rbrace\\)</span>. In this case, <span class="math-inline">\\(W\\)</span> would be the span of <span class="math-inline">\\(\lbrace\vec e&#95;2\rbrace\\)</span>, which is 1-dimensional, while <span class="math-inline">\\(S\\)</span> would still be 4-dimensional. (In this example, we said that <span class="math-inline">\\(T\\)</span> is the span of <span class="math-inline">\\(\vec e&#95;1\\)</span> and <span class="math-inline">\\(\vec e&#95;2\\)</span> though we defined it in the problem statement to be the span of three vectors. No problem --- just pick the third vector to be a linear combination of <span class="math-inline">\\(\vec e&#95;1\\)</span> and <span class="math-inline">\\(\vec e&#95;2\\)</span>. That is, <span class="math-inline">\\(\vec x&#95;1 = \vec e&#95;1\\)</span>, <span class="math-inline">\\(\vec x&#95;2 = \vec e&#95;2\\)</span>, and <span class="math-inline">\\(\vec x&#95;3 = \vec e&#95;1 + \vec e&#95;2\\)</span> would work as an example.)

-   Could <span class="math-inline">\\(\text{dim}(W) = 0\\)</span>? **Yes**. <span class="math-inline">\\(T\\)</span> and <span class="math-inline">\\(U\\)</span> could be two completely disjoint subspaces, except for <span class="math-inline">\\(\vec 0\\)</span>, which is in every subspace.

   For example, let <span class="math-inline">\\(\vec x&#95;1 = \vec e&#95;1\\)</span>, <span class="math-inline">\\(\vec x&#95;2 = \vec e&#95;2\\)</span>, <span class="math-inline">\\(\vec x&#95;3 = \vec e&#95;1 + \vec e&#95;2\\)</span>, which makes <span class="math-inline">\\(T\\)</span> a 2-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^9\\)</span>, and <span class="math-inline">\\(\vec x&#95;4 = \vec e&#95;3\\)</span>, <span class="math-inline">\\(\vec x&#95;5 = \vec e&#95;4\\)</span>, <span class="math-inline">\\(\vec x&#95;6 = \vec e&#95;3 + \vec e&#95;4\\)</span>, which makes <span class="math-inline">\\(U\\)</span> a 2-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^9\\)</span>. In this case, <span class="math-inline">\\(W\\)</span> would be the set <span class="math-inline">\\(\lbrace\vec 0\rbrace\\)</span>, while <span class="math-inline">\\(S\\)</span> would still be 4-dimensional.

So, the smallest possible value of <span class="math-inline">\\(\text{dim}(W)\\)</span> is <span class="math-inline">\\(\boxed{0}\\)</span>, and the largest possible value is <span class="math-inline">\\(\boxed{2}\\)</span>.
</details>

</div>
</div>

</div>

---

## Problem 7 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">20 pts</span>

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

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \left(\frac{1}{n} \sum&#95;{i=1}^n y&#95;i \right)^4\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\left(\displaystyle \frac{1}{n} \sum&#95;{i=1}^n y&#95;i^{1/4}\right)^4\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \left(\frac{1}{n} \sum&#95;{i=1}^n y&#95;i^4 \right)^{1/4}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \left(\frac{1}{n} \sum&#95;{i=1}^n y&#95;i^{1/2} \right)^{1/4}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \left(\frac{1}{n} \sum&#95;{i=1}^n y&#95;i^{4} \right)^{1/2}\\)</span></span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \left(\frac{1}{n} \sum&#95;{i=1}^n y&#95;i \right)^4\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\left(\displaystyle \frac{1}{n} \sum&#95;{i=1}^n y&#95;i^{1/4}\right)^4\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \left(\frac{1}{n} \sum&#95;{i=1}^n y&#95;i^4 \right)^{1/4}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \left(\frac{1}{n} \sum&#95;{i=1}^n y&#95;i^{1/2} \right)^{1/4}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \left(\frac{1}{n} \sum&#95;{i=1}^n y&#95;i^{4} \right)^{1/2}\\)</span></span></div>

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

Congrats on finishing Midterm 1!

Feel free to draw us a picture about EECS 245 in the box below (or use it for scratch work).
</div>
</div>

</div>

{% endraw %}
