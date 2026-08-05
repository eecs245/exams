---
number: 3
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>
points: 12
flags: []
has_solution: true
images: []
---

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
