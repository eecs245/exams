---
number: 3
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">10 pts</span> <span class="badge" data-flag="mt1-redemption" style="background-color: #9A3324; color: #FFFFFF; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">MT1 Redemption</span>
points: 10
flags: [mt1-redemption]
has_solution: true
images: []
---

Let <span class="math-inline">\\(\vec x = \begin{bmatrix} 2 \\\\ 1 \\\\ 1 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec z = \begin{bmatrix} 3 \\\\ 9 \\\\ 3 \end{bmatrix}\\)</span>, and suppose <span class="math-inline">\\(\vec y \in \mathbb{R}^3\\)</span> is such that

the projection of <span class="math-inline">\\(\vec x\\)</span> onto <span class="math-inline">\\(\vec y\\)</span> is <span class="math-inline">\\(\vec 0\\)</span> and that <span class="math-inline">\\(\vec y \cdot \vec y = \vec y \cdot \vec z = 45\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Find the projection of <span class="math-inline">\\(\vec z\\)</span> onto <span class="math-inline">\\(\vec x\\)</span>. Show your work, and write your final answer in the box provided. Give your answer as a vector with no variables.

<div class="math-display">
$$
\text{projection of }\vec z\text{ onto }\vec x = \_\_\_\_\_\_
$$
</div>

<details markdown="1"><summary>Solution</summary>

Using the projection formula from [Chapter 3.4](https://notes.eecs245.org/vectors/projecting-onto-a-single-vector/),

<div class="math-display">
$$
\vec p =
\frac{\vec{z}\cdot\vec{x}}{\vec{x}\cdot\vec{x}}\vec{x}
$$
</div>

 Here,

<div class="math-display">
$$
\vec{z}\cdot\vec{x}=3(2)+9(1)+3(1)=18,
\qquad
\vec{x}\cdot\vec{x}=2^2+1^2+1^2=6
$$
</div>

 so

<div class="math-display">
$$
\vec p
=
\frac{18}{6}\vec{x}
=
3\begin{bmatrix}2\\\\1\\\\1\end{bmatrix}
=
\begin{bmatrix}6\\\\3\\\\3\end{bmatrix}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Write <span class="math-inline">\\(\vec z\\)</span> as a linear combination of <span class="math-inline">\\(\vec x\\)</span> and <span class="math-inline">\\(\vec y\\)</span>. Show your work, and fill in each box with a number with no variables. <em>Hint: What is the relationship between <span class="math-inline">\\(\vec x\\)</span> and <span class="math-inline">\\(\vec y\\)</span>?</em>

<details markdown="1"><summary>Solution</summary>

Since the projection of <span class="math-inline">\\(\vec{x}\\)</span> onto <span class="math-inline">\\(\vec{y}\\)</span> is <span class="math-inline">\\(\vec{0}\\)</span> and <span class="math-inline">\\(\vec{y}\cdot\vec{y}=45\\)</span>, <span class="math-inline">\\(\vec{y}\\)</span> is nonzero and <span class="math-inline">\\(\vec{x}\cdot\vec{y}=0\\)</span>. In other words, <span class="math-inline">\\(\vec{x}\\)</span> and <span class="math-inline">\\(\vec{y}\\)</span> are orthogonal.

Suppose

<div class="math-display">
$$
\vec{z}=a\vec{x}+b\vec{y}
$$
</div>

 Taking dot products with <span class="math-inline">\\(\vec{x}\\)</span> gives

<div class="math-display">
$$
\vec{z}\cdot\vec{x}=a(\vec{x}\cdot\vec{x})+b(\vec{y}\cdot\vec{x})
$$
</div>

 Using the work from part **a)**, <span class="math-inline">\\(\vec{z}\cdot\vec{x}=18\\)</span> and <span class="math-inline">\\(\vec{x}\cdot\vec{x}=6\\)</span>. Since <span class="math-inline">\\(\vec{y}\cdot\vec{x}=0\\)</span>,

<div class="math-display">
$$
18 = 6a
$$
</div>

 so <span class="math-inline">\\(a=3\\)</span>.

Now take dot products with <span class="math-inline">\\(\vec{y}\\)</span>:

<div class="math-display">
$$
\vec{z}\cdot\vec{y}=a(\vec{x}\cdot\vec{y})+b(\vec{y}\cdot\vec{y})
$$
</div>

 The problem tells us that <span class="math-inline">\\(\vec{z}\cdot\vec{y}=\vec{y}\cdot\vec{y}=45\\)</span>, and <span class="math-inline">\\(\vec{x}\cdot\vec{y}=0\\)</span>, so

<div class="math-display">
$$
45=45b
$$
</div>

 and therefore <span class="math-inline">\\(b=1\\)</span>. So,

<div class="math-display">
$$
\vec{z}=3\vec{x}+\vec{y}
$$
</div>

</details>

</div>
</div>

</div>
