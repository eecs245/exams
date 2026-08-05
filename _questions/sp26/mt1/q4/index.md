---
number: 4
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">8 pts</span>
points: 8
flags: []
has_solution: true
images: []
---

Let <span class="math-inline">\\(\vec u,\vec v\in\mathbb R^n\\)</span> be vectors satisfying

<div class="math-display">
$$
\|\vec v\|=5,\qquad \|\vec u+\vec v\|=10,\qquad \|\vec u-\vec v\|=6
$$
</div>

Find <span class="math-inline">\\(\lVert \vec u \rVert^2\\)</span> (**not** <span class="math-inline">\\(\lVert \vec u \rVert\\)</span>). Show your work, and write your final answer in the box provided. Your answer should be a number with no variables.

<div class="math-display">
$$
\lVert \vec u \rVert^2 = \_\_\_\_\_\_
$$
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
