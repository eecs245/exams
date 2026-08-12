---
number: 6
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> <span class="badge" data-flag="mt2-redemption" style="background-color: #9A3324; color: #FFFFFF; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">MT2 Redemption</span>
points: 6
flags: [mt2-redemption]
has_solution: true
images: [polygon-determinant-area.png]
---

Find the area enclosed by the polygon with vertices <span class="math-inline">\\((0, 0)\\)</span>, <span class="math-inline">\\((4, 6)\\)</span>, <span class="math-inline">\\((1, 8)\\)</span>, and <span class="math-inline">\\((-3, 2)\\)</span>. Show your work, and write your answer in the box provided.

<div class="math-display">
$$
\text{area} = \_\_\_\_\_\_
$$
</div>

<details markdown="1"><summary>Solution</summary>

Let

<div class="math-display">
$$
\vec{u}=\begin{bmatrix}4\\\\6\end{bmatrix}
\qquad\text{and}\qquad
\vec{v}=\begin{bmatrix}-3\\\\2\end{bmatrix}
$$
</div>

 Then

<div class="math-display">
$$
\vec{u}+\vec{v}
=
\begin{bmatrix}1\\\\8\end{bmatrix}
$$
</div>

 so the four vertices are the coordinates of <span class="math-inline">\\(\vec{0}\\)</span>, <span class="math-inline">\\(\vec{u}\\)</span>, <span class="math-inline">\\(\vec{u}+\vec{v}\\)</span>, and <span class="math-inline">\\(\vec{v}\\)</span>. This means the polygon is a parallelogram. The area of the parallelogram is the absolute value of the determinant of the matrix whose columns are the two side vectors, as in [Chapter 6.1](https://notes.eecs245.org/linear-transformations-and-projections/linear-transformations/#the-determinant). We picked <span class="math-inline">\\(\vec{u}\\)</span> and <span class="math-inline">\\(\vec{v}\\)</span> because they are the side vectors from the origin, but using any two of the three nonzero vertices as the columns would give the same answer after taking the absolute value: adding one column to another does not change the determinant.

<div style="text-align: center;">
<img src="imgs/polygon-determinant-area.png" alt="image" style="width: 75%; max-width: 100%;">
</div>

So,

<div class="math-display">
$$
\text{area}
=
\left|
\det\left(
\begin{bmatrix}
4 & -3\\\\
6 & 2
\end{bmatrix}
\right)
\right|
=
\left|4(2)-(-3)(6)\right|
=26
$$
</div>

</details>
