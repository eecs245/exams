---
number: 6
title: Needed Me
heading_suffix: : Needed Me <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">11 pts</span>
points: 11
flags: []
has_solution: true
images: []
---

Suppose <span class="math-inline">\\(\vec x = \begin{bmatrix} c \\\\ 1 \\\\ 0 \end{bmatrix}\\)</span>, <span class="math-inline">\\(\vec y = \begin{bmatrix} 1 \\\\ c \\\\ 1 \end{bmatrix}\\)</span>, and <span class="math-inline">\\(\vec z = \begin{bmatrix} 0 \\\\ 1 \\\\ c \end{bmatrix}\\)</span>, where <span class="math-inline">\\(c \in \mathbb{R}\\)</span> is a constant.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">8 pts</span> Find a **positive value** of <span class="math-inline">\\(c\\)</span> such that <span class="math-inline">\\(\vec x\\)</span>, <span class="math-inline">\\(\vec y\\)</span>, and <span class="math-inline">\\(\vec z\\)</span> are linearly **dependent**. Show your work, and <span class="math-inline">\\(\boxed{\text{circle}}\\)</span> your final answer, which should be a positive number with no variables.

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(c = \sqrt{2}\\)</span>.

For <span class="math-inline">\\(\vec x\\)</span>, <span class="math-inline">\\(\vec y\\)</span>, and <span class="math-inline">\\(\vec z\\)</span> to be linearly dependent, there must exist scalars <span class="math-inline">\\(a\\)</span>, <span class="math-inline">\\(b\\)</span>, and <span class="math-inline">\\(c\\)</span> such that

<div class="math-display">
$$
a \vec x + b \vec y + \vec z
$$
</div>

(or equivalently, <span class="math-inline">\\(a \vec x + b \vec y + d\vec z = \vec 0\\)</span>, but the former approach involves one fewer variable to solve for).

Substituting in the given vectors, we have

<div class="math-display">
$$
a \begin{bmatrix} c \\\\ 1 \\\\ 0 \end{bmatrix} + b \begin{bmatrix} 1 \\\\ c \\\\ 1 \end{bmatrix} = \begin{bmatrix} 0 \\\\ 1 \\\\ c \end{bmatrix}
$$
</div>

As a system of equations, we have

<div class="math-display">
$$
\begin{align*}
c a + b &= 0 \\\\
a + c b &= 1 \\\\
b &= c
\end{align*}
$$
</div>

The third equation gives us <span class="math-inline">\\(b = c\\)</span>, and the second gives us <span class="math-inline">\\(a = 1 - cb = 1 - c^2\\)</span>. Substituting these into the first equation gives us

<div class="math-display">
$$
c(1 - c^2) + c = 0 \implies c - c^3 + c = 0 \implies c(2 - c^2) = 0
$$
</div>

This equation has three solutions for <span class="math-inline">\\(c\\)</span>: <span class="math-inline">\\(c = 0\\)</span>, <span class="math-inline">\\(c = \sqrt{2}\\)</span>, and <span class="math-inline">\\(c = -\sqrt{2}\\)</span>. We're asked to find a **positive** value of <span class="math-inline">\\(c\\)</span>, so <span class="math-inline">\\(c = \sqrt{2}\\)</span> for this part, and either <span class="math-inline">\\(0\\)</span> or <span class="math-inline">\\(-\sqrt{2}\\)</span> for the next part.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> Provide one **other** value of <span class="math-inline">\\(c\\)</span> (that is, not your answer from the previous part) such that <span class="math-inline">\\(\vec x\\)</span>, <span class="math-inline">\\(\vec y\\)</span>, and <span class="math-inline">\\(\vec z\\)</span> are linearly **dependent**. Your answer should be a number with no variables.

other value of <span class="math-inline">\\(c =\\)</span> \_\_\_\_\_\_

</div>
</div>

</div>
