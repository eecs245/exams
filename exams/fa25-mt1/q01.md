---
number: 1
title: Consider the Following\...
heading_suffix: : Consider the Following\... <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">15 pts</span>
points: 15
flags: []
has_solution: false
images: []
---

Consider the following dataset of <span class="math-inline">\\(n = 9\\)</span> values.

| <span class="math-inline">\\(y&#95;1\\)</span> | <span class="math-inline">\\(y&#95;2\\)</span> | <span class="math-inline">\\(y&#95;3\\)</span> | <span class="math-inline">\\(y&#95;4\\)</span> | <span class="math-inline">\\(y&#95;5\\)</span> | <span class="math-inline">\\(y&#95;6\\)</span> | <span class="math-inline">\\(y&#95;7\\)</span> | <span class="math-inline">\\(y&#95;8\\)</span> | <span class="math-inline">\\(y&#95;9\\)</span> |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| <span class="math-inline">\\(7\\)</span> | <span class="math-inline">\\(8\\)</span> | <span class="math-inline">\\(10\\)</span> | <span class="math-inline">\\(10\\)</span> | <span class="math-inline">\\(11\\)</span> | <span class="math-inline">\\(13\\)</span> | <span class="math-inline">\\(14\\)</span> | <span class="math-inline">\\(17\\)</span> | <span class="math-inline">\\(27\\)</span> |

Suppose we'd like to find the optimal parameter, <span class="math-inline">\\(w^{\ast}\\)</span>, for the constant model <span class="math-inline">\\(h(x&#95;i) = w\\)</span>, given this dataset of 9 values.

In parts **a)** through **f)**, choose the empirical risk function <span class="math-inline">\\(R(w)\\)</span> that the given value of <span class="math-inline">\\(w^{\ast}\\)</span> is the minimizer of, for this particular dataset. If you believe the given value of <span class="math-inline">\\(w^{\ast}\\)</span> does not minimize any of the five options, select N/A.

-   **Option 1**: <span class="math-inline">\\(\displaystyle R(w) = \frac{1}{n} \sum&#95;{i = 1}^n (y&#95;i - w)^2\\)</span>

-   **Option 2**: <span class="math-inline">\\(\displaystyle R(w) = \frac{1}{n} \sum&#95;{i = 1}^n (27y&#95;i - 13w)^2\\)</span>

-   **Option 3**: <span class="math-inline">\\(\displaystyle R(w) = \frac{1}{n} \sum&#95;{i = 1}^n 13|y&#95;i - w|\\)</span>

-   **Option 4**: <span class="math-inline">\\(\displaystyle R(w) = \frac{1}{n} \sum&#95;{i = 1}^n \begin{cases} 13 &amp; \text{if } y&#95;i = w \\\\ 27 &amp; \text{if } y&#95;i \neq w \end{cases}\\)</span>

-   **Option 5**: <span class="math-inline">\\(\displaystyle R(w) = \lim&#95;{p \rightarrow \infty} \frac{1}{n} \sum&#95;{i = 1}^n |y&#95;i - w|^p\\)</span>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(2.5 pts) **10** is the value of <span class="math-inline">\\(w\\)</span> that minimizes\...

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 1</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 2</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 3</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 4</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 5</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> N/A</span></div>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(2.5 pts) **11** is the value of <span class="math-inline">\\(w\\)</span> that minimizes\...

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 1</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 2</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 3</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 4</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 5</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> N/A</span></div>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(2.5 pts) **12** is the value of <span class="math-inline">\\(w\\)</span> that minimizes\...

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 1</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 2</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 3</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 4</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 5</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> N/A</span></div>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
(2.5 pts) **13** is the value of <span class="math-inline">\\(w\\)</span> that minimizes\...

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 1</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 2</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 3</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 4</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 5</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> N/A</span></div>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">e)</div>
<div class="assignment-part-content" markdown="1">
(2.5 pts) **17** is the value of <span class="math-inline">\\(w\\)</span> that minimizes\...

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 1</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 2</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 3</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 4</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 5</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> N/A</span></div>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">f)</div>
<div class="assignment-part-content" markdown="1">
(2.5 pts) **27** is the value of <span class="math-inline">\\(w\\)</span> that minimizes\...

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 1</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 2</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 3</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 4</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Option 5</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> N/A</span></div>

</div>
</div>

</div>
