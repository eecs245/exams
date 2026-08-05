---
number: 3
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">9 pts</span> <span class="badge" data-flag="mt1-redemption" style="background-color: #9A3324; color: #FFFFFF; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">MT1 Redemption</span>
points: 9
flags: [mt1-redemption]
has_solution: true
images: []
---

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">5 pts</span> Suppose <span class="math-inline">\\(\vec a = \begin{bmatrix} 0 \\\\ 3 \\\\ 6 \end{bmatrix}\\)</span> and that <span class="math-inline">\\(\vec b\\)</span> is another vector in <span class="math-inline">\\(\mathbb{R}^3\\)</span> such that:

-   <span class="math-inline">\\(\vec a\\)</span> and <span class="math-inline">\\(\vec b\\)</span> are orthogonal, and

-   the plane spanned by <span class="math-inline">\\(\vec a\\)</span> and <span class="math-inline">\\(\vec b\\)</span> is

<div class="math-display">
$$
4x - 2y + z = 0
$$
</div>

There are infinitely many possible vectors <span class="math-inline">\\(\vec b\\)</span> that satisfy the given conditions. State **one** of them. Show your work, and write your final answer in the box provided. Your answer should be a vector with no variables.

<div class="math-display">
$$
\text{one possible }\vec b = \_\_\_\_\_\_
$$
</div>

<details markdown="1"><summary>Solution</summary>

Let <span class="math-inline">\\(\vec b = \begin{bmatrix} x \\\\ y \\\\ z \end{bmatrix}\\)</span>.

Since <span class="math-inline">\\(\vec b\\)</span> lies in the given plane,

<div class="math-display">
$$
4x-2y+z=0
$$
</div>

 Since <span class="math-inline">\\(\vec a\\)</span> and <span class="math-inline">\\(\vec b\\)</span> are orthogonal,

<div class="math-display">
$$
\vec a \cdot \vec b = 3y+6z=0
$$
</div>

 The second equation gives <span class="math-inline">\\(y=-2z\\)</span>. Plugging this into the first equation gives

<div class="math-display">
$$
4x+4z+z=0
\implies
x=-\frac{5}{4}z
$$
</div>

 There are infinitely many solutions for <span class="math-inline">\\(x\\)</span>, <span class="math-inline">\\(y\\)</span>, and <span class="math-inline">\\(z\\)</span>; they all lie on a line. To state one, let's just fix a value of <span class="math-inline">\\(z\\)</span>. Arbitrarily choosing <span class="math-inline">\\(z = 4\\)</span> gives

<div class="math-display">
$$
\vec b = \boxed{\begin{bmatrix}-5\\\\-8\\\\4\end{bmatrix}}
$$
</div>

Here's another solution: really, the question is asking for a vector that is orthogonal to both <span class="math-inline">\\(\vec a\\)</span> and <span class="math-inline">\\(\begin{bmatrix} 4 \\\\ -2 \\\\ 1 \end{bmatrix}\\)</span>. Such a vector would be orthogonal to <span class="math-inline">\\(\vec a\\)</span> and would lie in the plane <span class="math-inline">\\(4x-2y+z=0\\)</span>. So, all we need to do is take the cross product of <span class="math-inline">\\(\vec a\\)</span> and <span class="math-inline">\\(\begin{bmatrix} 4 \\\\ -2 \\\\ 1 \end{bmatrix}\\)</span>.

<div class="math-display">
$$
\underbrace{\begin{bmatrix} 0 \\\\ 3 \\\\ 6 \end{bmatrix}}_{\vec a} \times \begin{bmatrix} 4 \\\\ -2 \\\\ 1 \end{bmatrix} = \begin{bmatrix} 3 \cdot 1 - 6 \cdot (-2) \\\\ 6 \cdot 4 - 0 \cdot 1 \\\\ 0 \cdot (-2) - 3 \cdot 4 \end{bmatrix} = \boxed{\begin{bmatrix} 15 \\\\ 24 \\\\ -12 \end{bmatrix}}
$$
</div>

Note that this is just <span class="math-inline">\\(-3\\)</span> times the vector we found above. Indeed, any scalar multiple of <span class="math-inline">\\(\begin{bmatrix} -5 \\\\ -8 \\\\ 4 \end{bmatrix}\\)</span> is also a solution.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> This part is unrelated to the previous part. Suppose <span class="math-inline">\\(\vec u, \vec v \in \mathbb{R}^n\\)</span>, and that:

-   <span class="math-inline">\\(\vec u\\)</span> is a unit vector,

-   <span class="math-inline">\\(\cos(\theta) = 2/3\\)</span>, where <span class="math-inline">\\(\theta\\)</span> is the angle between <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span>,

-   the projection of <span class="math-inline">\\(\vec v\\)</span> onto <span class="math-inline">\\(\vec u\\)</span> is <span class="math-inline">\\(6 \vec u\\)</span>.

What is the value of <span class="math-inline">\\(\lVert \vec v \rVert\\)</span>?

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(3\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(4\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(6\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(9\\)</span></span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(3\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(4\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(6\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(9\\)</span></span></div>

Since <span class="math-inline">\\(\vec u\\)</span> is a unit vector,

<div class="math-display">
$$
\vec p
= \frac{\vec v \cdot \vec u}{\vec u \cdot \vec u} \vec u
=
(\vec v \cdot \vec u)\vec u
$$
</div>

But this projection is also <span class="math-inline">\\(6 \vec u\\)</span>, so

<div class="math-display">
$$
\vec u \cdot \vec v = 6
$$
</div>

Now, let's use the fact that <span class="math-inline">\\(\cos(\theta) = 2/3\\)</span>, where <span class="math-inline">\\(\theta\\)</span> is the angle between <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span>, and plug in the values we know.

<div class="math-display">
$$
\begin{align*}
\cos \theta &= \frac{\vec u \cdot \vec v}{\lVert \vec u \rVert \lVert \vec v \rVert} \\\\
\frac{2}{3} &= \frac{6}{1 \cdot \lVert \vec v \rVert} \\\\
\lVert \vec v \rVert &= 9
\end{align*}
$$
</div>

So, <span class="math-inline">\\(\boxed{\lVert \vec v \rVert = 9}\\)</span>.
</details>

</div>
</div>

</div>
