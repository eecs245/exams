---
number: 2
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">10 pts</span>
points: 10
flags: []
has_solution: true
images: []
---

Suppose <span class="math-inline">\\(A\\)</span> is a matrix such that <span class="math-inline">\\(A \begin{bmatrix} 1 \\\\ 0 \\\\ 0 \\\\ 0 \end{bmatrix} = \begin{bmatrix} 6 \\\\ 0 \\\\ 1 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\left\lbrace \begin{bmatrix} 1 \\\\ 4 \\\\ -2 \\\\ 0 \end{bmatrix}, \begin{bmatrix} 0 \\\\ 1 \\\\ 1 \\\\ 0\end{bmatrix} \right\rbrace\\)</span> is a basis for <span class="math-inline">\\(\text{nullsp}(A)\\)</span>.

Find one possible matrix <span class="math-inline">\\(A\\)</span>. Show your work, and <span class="math-inline">\\(\boxed{\text{circle}}\\)</span> your final answer, which should be a matrix with no variables.

<details markdown="1"><summary>Solution</summary>

Let the columns of <span class="math-inline">\\(A\\)</span> be <span class="math-inline">\\(\vec c&#95;1, \vec c&#95;2, \vec c&#95;3, \vec c&#95;4\\)</span>. Since

<div class="math-display">
$$
A \begin{bmatrix} 1 \\\\ 0 \\\\ 0 \\\\ 0 \end{bmatrix} = 1\vec c_1 + 0\vec c_2 + 0\vec c_3 + 0\vec c_4 = \begin{bmatrix} 6 \\\\ 0 \\\\ 1 \end{bmatrix},
$$
</div>

 we know that the first column of <span class="math-inline">\\(A\\)</span> must be <span class="math-inline">\\(\begin{bmatrix} 6 \\\\ 0 \\\\ 1 \end{bmatrix}\\)</span>.

Now, let's use the information given about the null space to find the other columns of <span class="math-inline">\\(A\\)</span>. Since

<div class="math-display">
$$
\begin{bmatrix} 0 \\\\ 1 \\\\ 1 \\\\ 0 \end{bmatrix} \in \text{nullsp}(A),
$$
</div>

 we have

<div class="math-display">
$$
\vec c_2 + \vec c_3 = \vec 0 \implies \vec c_3 = -\vec c_2
$$
</div>

Also, since

<div class="math-display">
$$
\begin{bmatrix} 1 \\\\ 4 \\\\ -2 \\\\ 0 \end{bmatrix} \in \text{nullsp}(A),
$$
</div>

 we have

<div class="math-display">
$$
\vec c_1 + 4\vec c_2 - 2\vec c_3 = \vec 0
$$
</div>

 Substituting <span class="math-inline">\\(\vec c&#95;3 = -\vec c&#95;2\\)</span> gives

<div class="math-display">
$$
\begin{align*}
\vec c_1 + 6\vec c_2 &= \vec 0 \\\\
\vec c_2 &= -\frac{1}{6}\vec c_1 = \begin{bmatrix} -1 \\\\ 0 \\\\ -1/6 \end{bmatrix}.
\end{align*}
$$
</div>

So,

<div class="math-display">
$$
\vec c_3 = -\vec c_2 = \begin{bmatrix} 1 \\\\ 0 \\\\ 1/6 \end{bmatrix}
$$
</div>

Finally, <span class="math-inline">\\(\text{dim}(\text{nullsp}(A)) = 2\\)</span> and <span class="math-inline">\\(A\\)</span> has 4 columns, so by rank-nullity,

<div class="math-display">
$$
\begin{align*}
\text{rank}(A) &= 4 - 2 = 2
\end{align*}
$$
</div>

So we should choose <span class="math-inline">\\(\vec c&#95;4\\)</span> to be linearly independent from <span class="math-inline">\\(\vec c&#95;1\\)</span>. One easy choice is

<div class="math-display">
$$
\vec c_4 = \begin{bmatrix} 0 \\\\ 1 \\\\ 0 \end{bmatrix}
$$
</div>

This gives one possible matrix.

<div class="math-display">
$$
\boxed{
A = \begin{bmatrix}
6 & -1 & 1 & 0 \\\\
0 & 0 & 0 & 1 \\\\
1 & -1/6 & 1/6 & 0
\end{bmatrix}
}
$$
</div>

</details>
