---
layout: minimal
title: "Spring 2026 Midterm 1"
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

# Spring 2026 Midterm 1

**administered**

<div class="assignment-actions">
<a class="btn btn-info assignment-pdf-button" href="/resources/exams/sp26-mt1.pdf" target="_blank">View as PDF ✏️</a>
<a class="btn btn-info assignment-pdf-button" href="/resources/exams/sp26-mt1-solutions.pdf" target="_blank">Solutions PDF ✅</a>
</div>

{: .yellow }
<div markdown="1">
**Instructions**

-   This exam consists of 9 problems, worth 100 points, spread across 12 pages (6 sheets of paper).

-   You have 120 minutes to complete this exam, unless you have extended-time accommodations through SSD.

-   Write your uniqname in the top right corner of each page.

-   For free response problems, **you must show all of your work**, and <span class="math-inline">\\(\boxed{\text{circle}}\\)</span> your final answer. We will not grade work that appears elsewhere, and you may lose points if your work is not shown.

-   For multiple choice problems, completely fill in bubbles and square boxes; if we cannot tell which option(s) you selected, you may lose points.



-   You may refer to **one double-sided 8.5x11" handwritten notes sheet**. Other than that, you may not refer to any other resources or technology during the exam (no phones, watches, or calculators).
</div>

---

## Problems

- [Problem 1](#problem-1-16-pts)
- [Problem 2](#problem-2-10-pts)
- [Problem 3](#problem-3-14-pts)
- [Problem 4](#problem-4-8-pts)
- [Problem 5](#problem-5-13-pts)
- [Problem 6](#problem-6-11-pts)
- [Problem 7](#problem-7-10-pts)
- [Problem 8](#problem-8-8-pts)
- [Problem 9](#problem-9-10-pts)

---

## Problem 1 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">16 pts</span>

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

<span class="math-inline">\\(\text{minimizer of } R&#95;\text{sq}(w) = \minibox{3cm}{13/2 = 6.5}[1cm]\\)</span>

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

<span class="math-inline">\\(\text{one value of } w \text{ where the derivative of } R&#95;\text{clip}(w) \text{ is not defined} =\\)</span>

<div class="math-display">

<div class="math-display">
$$
1cm
$$
</div>

</div>

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

<span class="math-inline">\\(\text{minimizer of } R&#95;\text{clip}(w) \text{ within the interval } [1, 3] = \minibox{3cm}{2}[1cm]\\)</span>

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

<span class="math-inline">\\(\text{minimizer of } R&#95;\text{clip}(w) = \minibox{3cm}{2}[1cm]\\)</span>

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

---

## Problem 2 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">10 pts</span>

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

<div class="math-display">
$$
3cm
$$
</div>

</div>

<div class="math-display">

<div class="math-display">
$$
3cm
$$
</div>

</div>

<div class="math-display">

<div class="math-display">
$$
1cm
$$
</div>

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

<div class="math-display">
$$
7cm
$$
</div>

</div>

<div class="math-display">

<div class="math-display">
$$
3cm
$$
</div>

</div>

<div class="math-display">

<div class="math-display">
$$
1cm
$$
</div>

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

---

## Problem 3 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">14 pts</span>

Suppose we fit a simple linear regression model **with** an intercept term, <span class="math-inline">\\(h(x&#95;i)=w&#95;0+w&#95;1x&#95;i\\)</span>, to a dataset of <span class="math-inline">\\(n\\)</span> points <span class="math-inline">\\((x&#95;1, y&#95;1), (x&#95;2, y&#95;2), \ldots, (x&#95;n, y&#95;n)\\)</span> by minimizing mean squared error. You are given the following information:

-   The fit model satisfies <span class="math-inline">\\(h(-4) = 5\\)</span> and <span class="math-inline">\\(h(8) = 14\\)</span>.

-   The mean of <span class="math-inline">\\(y&#95;1, y&#95;2, \ldots, y&#95;n\\)</span> is <span class="math-inline">\\(\bar y = 2\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Find <span class="math-inline">\\(\bar x\\)</span>, the mean of <span class="math-inline">\\(x&#95;1, x&#95;2, \ldots, x&#95;n\\)</span>. Show your work, and write your final answer in the box provided. Your answer should be a number with no variables. <em>Hint: What property does the line <span class="math-inline">\\(h(x&#95;i)\\)</span> satisfy?</em>

<div class="math-display">

<div class="math-display">
$$
12cm
$$
</div>

</div>

<div class="math-display">

<div class="math-display">
$$
3cm
$$
</div>

</div>

<div class="math-display">

<div class="math-display">
$$
1cm
$$
</div>

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

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1/4\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(4/9\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(3/4\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(9/4\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(3\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(4\\)</span></span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1/4\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(4/9\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(3/4\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(9/4\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(3\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(4\\)</span></span></div>

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

<div class="mc-options"><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle\sum&#95;{i=1}^n e&#95;i=0\\)</span></span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle\sum&#95;{i=1}^n x&#95;i e&#95;i=0\\)</span></span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle\sum&#95;{i=1}^n y&#95;i e&#95;i=0\\)</span></span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle\sum&#95;{i=1}^n e&#95;i (x&#95;i - \bar x)=0\\)</span></span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-square mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle\sum&#95;{i=1}^n e&#95;i=0\\)</span></span><span class="mc-option"><span class="mc-square mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle\sum&#95;{i=1}^n x&#95;i e&#95;i=0\\)</span></span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle\sum&#95;{i=1}^n y&#95;i e&#95;i=0\\)</span></span><span class="mc-option"><span class="mc-square mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle\sum&#95;{i=1}^n e&#95;i (x&#95;i - \bar x)=0\\)</span></span></div>

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

---

## Problem 4 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">8 pts</span>

Let <span class="math-inline">\\(\vec u,\vec v\in\mathbb R^n\\)</span> be vectors satisfying

<div class="math-display">
$$
\|\vec v\|=5,\qquad \|\vec u+\vec v\|=10,\qquad \|\vec u-\vec v\|=6
$$
</div>

Find <span class="math-inline">\\(\lVert \vec u \rVert^2\\)</span> (**not** <span class="math-inline">\\(\lVert \vec u \rVert\\)</span>). Show your work, and write your final answer in the box provided. Your answer should be a number with no variables.

<div class="math-display">

<div class="math-display">
$$
14.5cm
$$
</div>

</div>

<div class="math-display">

<div class="math-display">
$$
3cm
$$
</div>

</div>

<div class="math-display">

<div class="math-display">
$$
1cm
$$
</div>

</div>

<details markdown="1"><summary>Solution</summary>

We have

<div class="math-display">
$$
10^2=\|\vec u+\vec v\|^2=\|\vec u\|^2+2\vec u\cdot\vec v+\|\vec v\|^2
$$
</div>

 and

<div class="math-display">
$$
6^2=\|\vec u-\vec v\|^2=\|\vec u\|^2-2\vec u\cdot\vec v+\|\vec v\|^2
$$
</div>

 Notice that the expressions on the right-hand side are similar, except for the signs of <span class="math-inline">\\(2 \vec u \cdot \vec v\\)</span>. So, adding these equations gives

<div class="math-display">
$$
136=2\|\vec u\|^2+2\|\vec v\|^2=2\|\vec u\|^2+50
$$
</div>

 so

<div class="math-display">
$$
\lVert \vec u \rVert^2 = \frac{136 - 50}{2} = \boxed{43}
$$
</div>

</details>

---

## Problem 5 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">13 pts</span>

Suppose <span class="math-inline">\\(\vec u,\vec v\in\mathbb R^n\\)</span> are non-zero vectors and <span class="math-inline">\\(k\\)</span> is a scalar. Let

<div class="math-display">
$$
f(k) = \lVert \vec u - k \vec v \rVert^2 + C k^2
$$
</div>

 where <span class="math-inline">\\(C \geq 0\\)</span> is a non-negative constant.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> In this part only, suppose <span class="math-inline">\\(C=0\\)</span>, <span class="math-inline">\\(\vec u = \begin{bmatrix} 1 \\\\ 2 \end{bmatrix}\\)</span>, and <span class="math-inline">\\(\vec v = \begin{bmatrix} 3 \\\\ 1 \end{bmatrix}\\)</span>. Find the value of <span class="math-inline">\\(k\\)</span> that minimizes <span class="math-inline">\\(f(k)\\)</span>. Show your work, and write your final answer in the box provided. Your answer should be a number with no variables.

<div class="math-display">

<div class="math-display">
$$
4cm
$$
</div>

</div>

<div class="math-display">

<div class="math-display">
$$
3cm
$$
</div>

</div>

<div class="math-display">

<div class="math-display">
$$
1cm
$$
</div>

</div>

<details markdown="1"><summary>Solution</summary>

There are several ways to think about this problem. What I expected most students to see is that when <span class="math-inline">\\(C = 0\\)</span>, this is really asking for the orthogonal projection of <span class="math-inline">\\(\vec u\\)</span> onto <span class="math-inline">\\(\vec v\\)</span>; the minimizer of <span class="math-inline">\\(f(k)\\)</span> is the value of <span class="math-inline">\\(k\\)</span> that makes <span class="math-inline">\\(\vec u - k \vec v\\)</span> orthogonal to <span class="math-inline">\\(\vec v\\)</span>.

Using that logic, we know from [Chapter 3.4](https://notes.eecs245.org/vectors/orthogonal-projection/) that the orthogonal projection of <span class="math-inline">\\(\vec u\\)</span> onto <span class="math-inline">\\(\vec v\\)</span> is given by

<div class="math-display">
$$
\vec p = k^* \vec v = \left( \frac{\vec u \cdot \vec v}{\vec v \cdot \vec v} \right) \vec v
$$
</div>

So,

<div class="math-display">
$$
k^* = \frac{\vec u \cdot \vec v}{\vec v \cdot \vec v} = \frac{1 \cdot 3 + 2 \cdot 1}{3^2 + 1^2} = \frac{5}{10} = \boxed{\frac{1}{2}}
$$
</div>

There's another way to approach this problem, which is to simplify <span class="math-inline">\\(f(k)\\)</span> and treat this like a calculus problem.

<div class="math-display">
$$
f(k)=\left\|\begin{bmatrix}1\\\\2\end{bmatrix}-k\begin{bmatrix}3\\\\1\end{bmatrix}\right\|^2=(1-3k)^2+(2-k)^2
$$
</div>

 Expanding,

<div class="math-display">
$$
f(k)=10k^2-10k+5
$$
</div>

 so

<div class="math-display">
$$
f'(k)=20k-10
$$
</div>

 Setting <span class="math-inline">\\(f'(k)=0\\)</span> gives <span class="math-inline">\\(k^{\ast} = \frac{1}{2}\\)</span> as well.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Note that <span class="math-inline">\\(f(k)\\)</span> *almost* looks like the squared norm of the vector <span class="math-inline">\\(\vec u - k \vec v\\)</span>, but with an extra term <span class="math-inline">\\(C k^2\\)</span>. Let's try and rewrite <span class="math-inline">\\(f(k)\\)</span> so that it *is* the squared norm of another related vector.

Define two new vectors, <span class="math-inline">\\(\vec U, \vec V \in \mathbb R^{n+1}\\)</span> by appending the scalar <span class="math-inline">\\(a\\)</span> to the end of <span class="math-inline">\\(\vec u\\)</span> and the scalar <span class="math-inline">\\(b\\)</span> to the end of <span class="math-inline">\\(\vec v\\)</span>.

<div class="math-display">
$$
\vec U = \begin{bmatrix} u_1 \\\\ u_2 \\\\ \vdots \\\\ u_n \\\\ a\end{bmatrix}, \quad \vec V = \begin{bmatrix} v_1 \\\\ v_2 \\\\ \vdots \\\\ v_n \\\\ b\end{bmatrix}
$$
</div>

Select values of <span class="math-inline">\\(a\\)</span> and <span class="math-inline">\\(b\\)</span> so that <span class="math-inline">\\(f(k) = \lVert \vec U - k \vec V \rVert^2\\)</span>, for all possible non-negative values of <span class="math-inline">\\(C\\)</span>.

1.  What is the value of <span class="math-inline">\\(a\\)</span>?
<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 0</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(C\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(C^2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\sqrt{C}\\)</span></span></div>

2.  What is the value of <span class="math-inline">\\(b\\)</span>?
<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 0</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(C\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(C^2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\sqrt{C}\\)</span></span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 0</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(C\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(C^2\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(\sqrt{C}\\)</span></span></div>

First, let's try and get a better sense of how <span class="math-inline">\\(\lVert \vec U - k \vec V \rVert^2\\)</span> works.

<div class="math-display">
$$
\begin{align*}
\lVert \vec U - k \vec V \rVert^2 &= \left\lVert \begin{bmatrix} u_1 \\\\ u_2 \\\\ \vdots \\\\ u_n \\\\ a\end{bmatrix} - k \begin{bmatrix} v_1 \\\\ v_2 \\\\ \vdots \\\\ v_n \\\\ b\end{bmatrix} \right\rVert^2 \\\\
&= \left\lVert \begin{bmatrix} u_1 - kv_1 \\\\ u_2 - kv_2 \\\\ \vdots \\\\ u_n - kv_n \\\\ a - kb\end{bmatrix} \right\rVert^2 \\\\
&= \sum_{i=1}^n (u_i - kv_i)^2 + (a - kb)^2 \\\\
&= \lVert \vec u - k \vec v \rVert^2 + (a - kb)^2 \\\\
\end{align*}
$$
</div>

Our job is to find <span class="math-inline">\\(a\\)</span> and <span class="math-inline">\\(b\\)</span> so that <span class="math-inline">\\(f(k)\\)</span>, which we were told is defined as

<div class="math-display">
$$
f(k) =\lVert \vec u - k \vec v \rVert^2 + C k^2
$$
</div>

 is **also** equal to

<div class="math-display">
$$
\lVert \vec U - k \vec V \rVert^2 = \lVert \vec u - k \vec v \rVert^2 + (a - kb)^2
$$
</div>

If we set <span class="math-inline">\\(f(k) = \lVert \vec U - k \vec V \rVert^2\\)</span>, we see that this boils down to finding <span class="math-inline">\\(a\\)</span> and <span class="math-inline">\\(b\\)</span> such that

<div class="math-display">
$$
(a - kb)^2 = C k^2
$$
</div>

Notice the right-hand side of the expression above is just <span class="math-inline">\\(Ck^2\\)</span>, not <span class="math-inline">\\(Ck^2 + \text{some constant} \cdot k + \text{some other constant}\\)</span>. This means that <span class="math-inline">\\(a = 0\\)</span>, and that forces <span class="math-inline">\\(b = \sqrt{C}\\)</span>:

<div class="math-display">
$$
(0 - k\sqrt{C})^2 = Ck^2
$$
</div>

So, the correct answers are <span class="math-inline">\\(\boxed{a=0}\\)</span> and <span class="math-inline">\\(\boxed{b=\sqrt{C}}\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> As <span class="math-inline">\\(C\\)</span> increases, what happens to the value of <span class="math-inline">\\(k\\)</span> that minimizes <span class="math-inline">\\(f(k)\\)</span>? Explain your reasoning.

<details markdown="1"><summary>Solution</summary>

There are a couple of ways to think about this. First, if we use the interpretation provided in part **b)**, the vectors <span class="math-inline">\\(\vec U\\)</span> and <span class="math-inline">\\(\vec V\\)</span> "bake in" the value of <span class="math-inline">\\(C\\)</span>:

<div class="math-display">
$$
\vec U = \begin{bmatrix} u_1 \\\\ u_2 \\\\ \vdots \\\\ u_n \\\\ 0\end{bmatrix}, \quad \vec V = \begin{bmatrix} v_1 \\\\ v_2 \\\\ \vdots \\\\ v_n \\\\ \sqrt{C}\end{bmatrix}
$$
</div>

Increasing <span class="math-inline">\\(C\\)</span> keeps the dot product of <span class="math-inline">\\(\vec U\\)</span> and <span class="math-inline">\\(\vec V\\)</span> fixed, but increases the norm of <span class="math-inline">\\(\vec V\\)</span>. Why is this relevant? Since <span class="math-inline">\\(f(k) = \lVert \vec U - k \vec V \rVert^2\\)</span>, the minimizer <span class="math-inline">\\(k^{\ast}\\)</span> of <span class="math-inline">\\(f(k)\\)</span> is equal to

<div class="math-display">
$$
k^* = \frac{\vec U \cdot \vec V}{\vec V \cdot \vec V}
$$
</div>

So, as <span class="math-inline">\\(C\\)</span> increases, the denominator of <span class="math-inline">\\(k^{\ast}\\)</span> increases, so <span class="math-inline">\\(k^{\ast}\\)</span> moves toward <span class="math-inline">\\(0\\)</span>, though this may happen either from the left or the right, since <span class="math-inline">\\(\vec U \cdot \vec V\\)</span> may be positive or negative.

If you'd prefer, you *could* just expand the original definition of <span class="math-inline">\\(f(k)\\)</span>, take the derivative to find the closed-form expression for the minimizing <span class="math-inline">\\(k^{\ast}\\)</span> for an arbitrary <span class="math-inline">\\(C\\)</span>, and look at what happens to <span class="math-inline">\\(k^{\ast}\\)</span> as <span class="math-inline">\\(C\\)</span> increases.

Recall, the original definition of <span class="math-inline">\\(f(k)\\)</span> is <span class="math-inline">\\(f(k)=\lVert \vec u - k \vec v \rVert^2 + C k^2\\)</span>, so

<div class="math-display">
$$
f(k)=\vec u \cdot \vec u - 2k(\vec u\cdot\vec v)+k^2\vec v \cdot \vec v+Ck^2
$$
</div>

 Therefore,

<div class="math-display">
$$
f'(k)=-2(\vec u\cdot\vec v)+2k(\vec v \cdot \vec v+C)
$$
</div>

 so the minimizer is

<div class="math-display">
$$
k^*=\frac{\vec u\cdot\vec v}{\vec v \cdot \vec v+C}
$$
</div>

 As <span class="math-inline">\\(C\\)</span> increases, the denominator increases (but <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> are fixed --- notice these are the original <span class="math-inline">\\(\vec u, \vec v\\)</span>, not the new <span class="math-inline">\\(\vec U, \vec V\\)</span>), so <span class="math-inline">\\(k^{\ast}\\)</span> moves toward <span class="math-inline">\\(0\\)</span>.
</details>

</div>
</div>

</div>

---

## Problem 6 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">11 pts</span>

Suppose <span class="math-inline">\\(c \in \mathbb R\\)</span> is a constant and

<div class="math-display">
$$
\vec u=\begin{bmatrix}3\\\\1\\\\c\end{bmatrix},
\qquad
\vec v=\begin{bmatrix}6\\\\c\\\\-2\end{bmatrix}
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Fill in the blanks to complete the sentence:

For all values of <span class="math-inline">\\(c\\)</span>, <span class="math-inline">\\(\text{span}(\lbrace\vec u,\vec v\rbrace)\\)</span> is a \_\_(i)\_\_-dimensional subspace of \_\_(ii)\_\_.

(i):

<div class="math-display">

<div class="math-display">
$$
1cm
$$
</div>

</div>

 (ii):

<div class="math-display">

<div class="math-display">
$$
1cm
$$
</div>

</div>

<details markdown="1"><summary>Solution</summary>

The vectors <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> are never scalar multiples of each other. If <span class="math-inline">\\(\vec v=\lambda\vec u\\)</span>, then the first entries force <span class="math-inline">\\(\lambda=2\\)</span>, the second entries force <span class="math-inline">\\(c=2\\)</span>, and the third entries force <span class="math-inline">\\(-2=2c=4\\)</span>, which is impossible. Therefore, the span is always a 2-dimensional subspace of <span class="math-inline">\\(\mathbb R^3\\)</span>.

Why <span class="math-inline">\\(\mathbb R^3\\)</span>? Because both <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> live in <span class="math-inline">\\(\mathbb R^3\\)</span>, so their span must also live in <span class="math-inline">\\(\mathbb R^3\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">7 pts</span> Suppose the plane spanned by <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> is

<div class="math-display">
$$
ax+24y+3z=0
$$
</div>

 where <span class="math-inline">\\(a\\)</span> is also a constant. Find the value of <span class="math-inline">\\(c\\)</span>. Show your work in the space provided, and write your final answer in the box provided. Your answer should be a number with no variables.

<div class="math-display">

<div class="math-display">
$$
13cm
$$
</div>

</div>

<div class="math-display">

<div class="math-display">
$$
3cm
$$
</div>

</div>

<div class="math-display">

<div class="math-display">
$$
1cm
$$
</div>

</div>

<details markdown="1"><summary>Solution</summary>

There are a few ways to approach this. The first way starts by using the fact that <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> lie in the plane, which gives us a system of two equations and two unknowns. Plugging in the coordinates of <span class="math-inline">\\(\vec u\\)</span> into the plane gives us

<div class="math-display">
$$
3a+24+3c=0 \implies a + 8 + c = 0
$$
</div>

 and plugging in the coordinates of <span class="math-inline">\\(\vec v\\)</span> into the plane gives us

<div class="math-display">
$$
6a+24c-6=0 \implies a + 4c - 1 = 0
$$
</div>

 Subtracting the simplified versions of the two equations gives us

<div class="math-display">
$$
(8 + c) - (4c - 1) = 0 \implies 9 - 3c = 0 \implies c = 3
$$
</div>

Another way to approach this is to find the cross product of <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span>, and try and write it as a scalar multiple of the vector <span class="math-inline">\\(\begin{bmatrix} a \\\\ 24 \\\\ 3 \end{bmatrix}\\)</span>.

<div class="math-display">
$$
\vec u \times \vec v = \begin{bmatrix} 3 \\\\ 1 \\\\ c \end{bmatrix} \times \begin{bmatrix} 6 \\\\ c \\\\ -2 \end{bmatrix} = \begin{bmatrix} 1 \cdot (-2) - c \cdot c \\\\ c \cdot 6 - 3 \cdot (-2) \\\\ 3 \cdot c - 1 \cdot 6 \end{bmatrix} = \begin{bmatrix} -2 - c^2 \\\\ 6c + 6 \\\\ 3c - 6 \end{bmatrix}
$$
</div>

Strictly speaking, this vector, <span class="math-inline">\\(\begin{bmatrix} -2 - c^2 \\\\ 6c + 6 \\\\ 3c - 6 \end{bmatrix}\\)</span>, is a scalar multiple of <span class="math-inline">\\(\begin{bmatrix} a \\\\ 24 \\\\ 3 \end{bmatrix}\\)</span>, but we don't know what the scalar is yet. So, we really should try and solve

<div class="math-display">
$$
\begin{bmatrix} -2 - c^2 \\\\ 6c + 6 \\\\ 3c - 6 \end{bmatrix} = k \begin{bmatrix} a \\\\ 24 \\\\ 3 \end{bmatrix}
$$
</div>

But, notice that <span class="math-inline">\\(6c + 6 = 24 \implies c = 3\\)</span>, and <span class="math-inline">\\(c = 3\\)</span> also satisfies <span class="math-inline">\\(3c - 6 = 3\\)</span>, so the scalar <span class="math-inline">\\(k = 1\\)</span>, and thus <span class="math-inline">\\(\boxed{c = 3}\\)</span>.
</details>

</div>
</div>

</div>

---

## Problem 7 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">10 pts</span>

Suppose <span class="math-inline">\\(\vec v&#95;1,\vec v&#95;2,\vec v&#95;3,\vec v&#95;4\in\mathbb R^n\\)</span> are a **linearly independent** collection of vectors. Define

<div class="math-display">
$$
\vec p=\vec v_1+\vec v_2,\qquad
\vec q=\vec v_2+\vec v_3,\qquad
\vec r=\vec v_3+\vec v_4,\qquad
\vec s=\vec v_4+\vec v_1
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">7 pts</span> Are <span class="math-inline">\\(\lbrace\vec p,\vec q,\vec r,\vec s\rbrace\\)</span> linearly independent?

1.  Select an answer:
<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Yes</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> No</span></div>

2.  Prove your answer using the formal definition of linear independence. <em>Hint: You did something similar in Homework 4, Problem 6.</em>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Yes</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> No</span></div>

If <span class="math-inline">\\(\vec p,\vec q,\vec r,\vec s\\)</span> are linearly independent, then the only solution to the equation <span class="math-inline">\\(a \vec p + b \vec q + c \vec r + d \vec s = \vec 0\\)</span> is <span class="math-inline">\\(a = b = c = d = 0\\)</span>.

That's not the case here! Consider the linear combination

<div class="math-display">
$$
\vec p-\vec q+\vec r-\vec s
$$
</div>

 How did I think of this? I noticed that if I start with <span class="math-inline">\\(\vec p\\)</span>, subtracting <span class="math-inline">\\(\vec q\\)</span> gets rid of all <span class="math-inline">\\(\vec v&#95;2\\)</span>'s, but makes <span class="math-inline">\\(\vec v&#95;3\\)</span> negative, so I need a positive <span class="math-inline">\\(\vec r\\)</span> to cancel that out. Then, <span class="math-inline">\\(\vec p - \vec q + \vec r = \vec v&#95;1 + \vec v&#95;4\\)</span>; subtracting <span class="math-inline">\\(\vec s\\)</span> then gets rid of both <span class="math-inline">\\(\vec v&#95;1\\)</span> and <span class="math-inline">\\(\vec v&#95;4\\)</span>, leaving me with <span class="math-inline">\\(\vec 0\\)</span>.

<div class="math-display">
$$
\vec p - \vec q + \vec r - \vec s = (\vec v_1+\vec v_2)-(\vec v_2+\vec v_3)+(\vec v_3+\vec v_4)-(\vec v_4+\vec v_1)=\vec 0
$$
</div>

 The coefficients <span class="math-inline">\\(1,-1,1,-1\\)</span> are not all zero, so this proves that <span class="math-inline">\\(\lbrace\vec p,\vec q,\vec r,\vec s\rbrace\\)</span> is linearly dependent.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> What is the dimension of <span class="math-inline">\\(\text{span}(\lbrace\vec p,\vec q,\vec r,\vec s\rbrace)\\)</span>? Give your answer as a number with no variables.

<span class="math-inline">\\(\dim(\text{span}(\lbrace\vec p,\vec q,\vec r,\vec s\rbrace)) = \minibox{3cm}{3}[1cm]\\)</span>

<details markdown="1"><summary>Solution</summary>

Part **a)** shows that the four vectors are linearly **dependent**, so the dimension of <span class="math-inline">\\(\text{span}(\lbrace\vec p,\vec q,\vec r,\vec s\rbrace)\\)</span> is **at most** <span class="math-inline">\\(3\\)</span>. (For the dimension to be 4, which is the number of vectors in question, they would need to be linearly independent. There's no way to have a span of 5 or more dimensions using just 4 vectors.)

But just because the dimension of <span class="math-inline">\\(\text{span}(\lbrace\vec p,\vec q,\vec r,\vec s\rbrace)\\)</span> is at most <span class="math-inline">\\(3\\)</span> doesn't mean that the dimension is actually <span class="math-inline">\\(3\\)</span> --- for this span to be 3-dimensional, it needs to be the span of 3 linearly independent vectors.

Fortunately, <span class="math-inline">\\(\vec p,\vec q,\vec r\\)</span> are linearly independent. If

<div class="math-display">
$$
a\vec p+b\vec q+c\vec r=\vec 0
$$
</div>

 then

<div class="math-display">
$$
a\vec v_1+(a+b)\vec v_2+(b+c)\vec v_3+c\vec v_4=\vec 0
$$
</div>

 Since <span class="math-inline">\\(\vec v&#95;1,\vec v&#95;2,\vec v&#95;3,\vec v&#95;4\\)</span> are linearly independent, we must have

<div class="math-display">
$$
a=0,\qquad a+b=0,\qquad b+c=0,\qquad c=0
$$
</div>

 This gives <span class="math-inline">\\(a=b=c=0\\)</span>, so <span class="math-inline">\\(\vec p,\vec q,\vec r\\)</span> are linearly independent. Therefore, among <span class="math-inline">\\(\left\lbrace \vec p,\vec q,\vec r,\vec s \right\rbrace\\)</span>, there are 3 linearly independent vectors, and thus

<div class="math-display">
$$
\boxed{\dim(\text{span}(\{\vec p,\vec q,\vec r,\vec s\}))=3}
$$
</div>

</details>

</div>
</div>

</div>

---

## Problem 8 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">8 pts</span>

Suppose <span class="math-inline">\\(S\\)</span> is the subspace of <span class="math-inline">\\(\mathbb R^4\\)</span> defined by

<div class="math-display">
$$
S=\left\{
\begin{bmatrix}x_1\\\\x_2\\\\x_3\\\\x_4\end{bmatrix}\in\mathbb R^4 :
x_1-x_2+x_3-x_4=0
\right\}
$$
</div>

Which of the following sets is a basis for <span class="math-inline">\\(S\\)</span>? **Select all** that apply.

<details markdown="1"><summary>Solution</summary>

The subspace <span class="math-inline">\\(S\\)</span> has dimension <span class="math-inline">\\(3\\)</span> because the single constraint lets us solve

<div class="math-display">
$$
x_4=x_1-x_2+x_3
$$
</div>

 This means that components 1, 2, and 3 are free to vary, and component 4 is fully determined by those first three components. So, <span class="math-inline">\\(S\\)</span> has three "degrees of freedom", and therefore has dimension <span class="math-inline">\\(3\\)</span>.

So a basis for <span class="math-inline">\\(S\\)</span> is any set of **three linearly independent vectors** that all lie in <span class="math-inline">\\(S\\)</span>.

The first and third choices are bases: in both of those choices, the set has 3 vectors that are linearly independent, and all 3 vectors lie in <span class="math-inline">\\(S\\)</span>.

The second choice has 4 vectors in a 3-dimensional subspace, so it cannot be a basis.

The fourth choice has 3 vectors but they are not linearly independent, since at least one of them can be written as a linear combination of the other two:

<div class="math-display">
$$
\begin{bmatrix}1\\\\1\\\\0\\\\0\end{bmatrix} = \begin{bmatrix}1\\\\0\\\\0\\\\1\end{bmatrix} + \begin{bmatrix}0\\\\1\\\\0\\\\-1\end{bmatrix}
$$
</div>

So, only the first and third choices are bases for <span class="math-inline">\\(S\\)</span>.
</details>

---

## Problem 9 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">10 pts</span>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">7 pts</span> Suppose <span class="math-inline">\\(x\\)</span> and <span class="math-inline">\\(y\\)</span> are non-negative numbers. Using the Cauchy-Schwarz inequality, prove that

<div class="math-display">
$$
\frac{(x+y)^2}{2}\le x^2+y^2
$$
</div>

<em>Solutions that do not use the Cauchy-Schwarz inequality will not receive credit.</em>

<details markdown="1"><summary>Solution</summary>

Recall, the Cauchy-Schwarz inequality states that for any two vectors <span class="math-inline">\\(\vec u, \vec v \in \mathbb{R}^n\\)</span>,

<div class="math-display">
$$
|\vec u \cdot \vec v| \leq \|\vec u\| \|\vec v\|
$$
</div>

Applying Cauchy-Schwarz to the vectors <span class="math-inline">\\(\vec u=\begin{bmatrix}x\\\\y\end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec v=\begin{bmatrix}1\\\\1\end{bmatrix}\\)</span> gives

<div class="math-display">
$$
|x + y| \leq \sqrt{x^2 + y^2} \sqrt{1^2 + 1^2} = \sqrt{2(x^2 + y^2)}
$$
</div>

 Squaring both sides gives

<div class="math-display">
$$
(x + y)^2 \leq 2(x^2 + y^2)
$$
</div>

 and finally, dividing both sides by <span class="math-inline">\\(2\\)</span> gives

<div class="math-display">
$$
\frac{(x+y)^2}{2}\le x^2+y^2
$$
</div>

 as needed.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> Now suppose <span class="math-inline">\\(x\\)</span>, <span class="math-inline">\\(y\\)</span>, and <span class="math-inline">\\(z\\)</span> are non-negative numbers. Which inequality is guaranteed to be true?

| <span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \frac{(x+y+z)^2}{2}\le x^2+y^2+z^2\\)</span> |
|:--------------------------------------------------------------|
| <span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \frac{(x+y+z)^2}{3}\le x^2+y^2+z^2\\)</span> |
| <span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \frac{(x+y+z)^2}{2}\le x^3+y^3+z^3\\)</span> |
| <span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \frac{(x+y+z)^3}{3}\le x^3+y^3+z^3\\)</span> |
| <span class="mc-bubble" aria-hidden="true"></span> None of the above                                  |

<details markdown="1"><summary>Solution</summary>

<span class="mc-bubble" aria-hidden="true"></span> None of the above

The Cauchy-Schwarz inequality directly implies one of the options, and the other options are all not guaranteed to be true. Extending our argument from part **a)**, let's now apply Cauchy-Schwarz to the vectors <span class="math-inline">\\(\vec u=\begin{bmatrix}x\\\\y\\\\z\end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec v=\begin{bmatrix}1\\\\1\\\\1\end{bmatrix}\\)</span>. This gives

<div class="math-display">
$$
|x+y+z|\le \sqrt{x^2+y^2+z^2} \sqrt{1^2+1^2+1^2} = \sqrt{3(x^2+y^2+z^2)}
$$
</div>

 Squaring both sides and dividing by <span class="math-inline">\\(3\\)</span> gives

<div class="math-display">
$$
\frac{(x+y+z)^2}{3}\le x^2+y^2+z^2
$$
</div>

 which is the second option.
</details>

Congrats on finishing Midterm 1! Feel free to draw us a picture about EECS 245 in the box below.
</div>
</div>

</div>

{% endraw %}
