---
number: 6
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">11 pts</span>
points: 11
flags: []
has_solution: true
images: []
---

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

(i): \_\_\_\_\_\_ (ii): \_\_\_\_\_\_

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
$$
c = \_\_\_\_\_\_
$$
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
