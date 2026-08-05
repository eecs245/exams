---
number: 2
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">16 pts</span>
points: 16
flags: []
has_solution: true
images: []
---

Suppose <span class="math-inline">\\(A\\)</span> is a <span class="math-inline">\\(3 \times 3\\)</span> matrix whose null space is the plane

<div class="math-display">
$$
5x - y + 3z = 0
$$
</div>

In other words, <span class="math-inline">\\(\text{nullsp}(A) = \left\lbrace \begin{bmatrix} x \\\\ y \\\\ z \end{bmatrix} \mid   5x - y + 3z = 0 \right\rbrace\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> Determine the following values. Give your answers as integers with no variables.

<span class="math-inline">\\(\text{rank}(A) =\\)</span> \_\_\_\_\_\_ <span class="math-inline">\\(\text{dim}(\text{nullsp}(A)) =\\)</span> \_\_\_\_\_\_

<details markdown="1"><summary>Solution</summary>

The null space is a plane in <span class="math-inline">\\(\mathbb{R}^3\\)</span>, which is a <span class="math-inline">\\(2\\)</span>-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^3\\)</span>. So,

<div class="math-display">
$$
\dim(\text{nullsp}(A)) = 2
$$
</div>

 Since <span class="math-inline">\\(A\\)</span> has 3 columns, the rank-nullity theorem gives

<div class="math-display">
$$
\begin{align*}
\text{rank}(A) + \dim(\text{nullsp}(A)) &= 3 \\\\
\text{rank}(A) + 2 &= 3 \\\\
\text{rank}(A) &= 1
\end{align*}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> State one basis for <span class="math-inline">\\(\text{nullsp}(A)\\)</span>. Your answer should be a list of vectors with no variables.

<span class="math-inline">\\(\text{one basis for }\text{nullsp}(A) =\\)</span> \_\_\_\_\_\_

<details markdown="1"><summary>Solution</summary>

The null space consists of all vectors satisfying

<div class="math-display">
$$
5x-y+3z = 0
$$
</div>

 A basis for the null space, then, consists of any two linearly independent vectors that satisfy this equation. <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ 5 \\\\ 0 \end{bmatrix}\\)</span> satisfies it, since <span class="math-inline">\\(5 \cdot 1 - (5) + 3 \cdot 0 = 0\\)</span>, and similarly <span class="math-inline">\\(\begin{bmatrix} 0 \\\\ 3 \\\\ 1 \end{bmatrix}\\)</span> satisfies it. Therefore, one basis is

<div class="math-display">
$$
\left\{ \begin{bmatrix} 1 \\\\ 5 \\\\ 0 \end{bmatrix}, \begin{bmatrix} 0 \\\\ 3 \\\\ 1 \end{bmatrix} \right\}
$$
</div>

</details>

though there are infinitely many possible answers.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> State one basis for <span class="math-inline">\\(\text{colsp}(A^T)\\)</span>, the row space of <span class="math-inline">\\(A\\)</span>. Your answer should be a list of vectors with no variables.

<span class="math-inline">\\(\text{one basis for }\text{colsp}(A^T) =\\)</span> \_\_\_\_\_\_

<details markdown="1"><summary>Solution</summary>

A key fact to remember here is that the row space and null space of a matrix are orthogonal complements, as discussed in [Chapter 5.4](https://notes.eecs245.org/matrices/null-space-rank-nullity/#example-orthogonal-complements). This means that every element in the row space must be orthogonal to every element in the null space.

We're given that the null space consists of all vectors <span class="math-inline">\\(\vec x = \begin{bmatrix} x \\\\ y \\\\ z \end{bmatrix}\\)</span> such that <span class="math-inline">\\(5x-y+3z = 0\\)</span>. Equivalently, this means that <span class="math-inline">\\(\begin{bmatrix} 5 \\\\ -1 \\\\ 3 \end{bmatrix} \cdot \vec x = 0\\)</span>. So, this means that every element in the null space is orthogonal to <span class="math-inline">\\(\begin{bmatrix} 5 \\\\ -1 \\\\ 3 \end{bmatrix}\\)</span>, so <span class="math-inline">\\(\begin{bmatrix} 5 \\\\ -1 \\\\ 3 \end{bmatrix}\\)</span> must be in the row space. The row space is <span class="math-inline">\\(1\\)</span>-dimensional, since <span class="math-inline">\\(\text{rank}(A)=1\\)</span>. So, one basis is <span class="math-inline">\\(\left\lbrace \begin{bmatrix} 5 \\\\ -1 \\\\ 3 \end{bmatrix} \right\rbrace\\)</span>.

If you didn't remember this key fact, no problem --- you could have arrived at this conclusion from scratch on the exam. We know <span class="math-inline">\\(A\\)</span> is <span class="math-inline">\\(3 \times 3\\)</span>, so suppose it looks like

<div class="math-display">
$$
A = \begin{bmatrix} a_{11} & a_{12} & a_{13} \\\\ a_{21} & a_{22} & a_{23} \\\\ a_{31} & a_{32} & a_{33} \end{bmatrix}
$$
</div>

If <span class="math-inline">\\(\vec x = \begin{bmatrix} x \\\\ y \\\\ z \end{bmatrix}\\)</span> is in the null space, it must mean that <span class="math-inline">\\(A \vec x = \vec 0\\)</span>:

<div class="math-display">
$$
A \vec x = \begin{bmatrix} a_{11} & a_{12} & a_{13} \\\\ a_{21} & a_{22} & a_{23} \\\\ a_{31} & a_{32} & a_{33} \end{bmatrix} \begin{bmatrix} x \\\\ y \\\\ z \end{bmatrix} = \begin{bmatrix} a_{11}x + a_{12}y + a_{13}z \\\\ a_{21}x + a_{22}y + a_{23}z \\\\ a_{31}x + a_{32}y + a_{33}z \end{bmatrix} = \begin{bmatrix} 0 \\\\ 0 \\\\ 0 \end{bmatrix}
$$
</div>

From here, you see that the dot product of each row of <span class="math-inline">\\(A\\)</span> with <span class="math-inline">\\(\vec x\\)</span> must be 0, so each row of <span class="math-inline">\\(A\\)</span> must be orthogonal to <span class="math-inline">\\(\vec x\\)</span>. The plane form of the null space, <span class="math-inline">\\(5x-y+3z=0\\)</span>, tells you that <span class="math-inline">\\(\begin{bmatrix} 5 \\\\ -1 \\\\ 3 \end{bmatrix}\\)</span> is orthogonal to every vector in the null space, so putting these facts together gives us that <span class="math-inline">\\(\begin{bmatrix} 5 \\\\ -1 \\\\ 3 \end{bmatrix}\\)</span> is in the row space. Together with the fact that the row space is <span class="math-inline">\\(1\\)</span>-dimensional, since <span class="math-inline">\\(\text{rank}(A)=1\\)</span>, we have that a basis is <span class="math-inline">\\(\left\lbrace \begin{bmatrix} 5 \\\\ -1 \\\\ 3 \end{bmatrix} \right\rbrace\\)</span>.

All other possible answers involve (non-zero) scalar multiples of <span class="math-inline">\\(\begin{bmatrix} 5 \\\\ -1 \\\\ 3 \end{bmatrix}\\)</span>.
</details>

Recall, <span class="math-inline">\\(A\\)</span> is a <span class="math-inline">\\(3 \times 3\\)</span> matrix whose null space is the plane <span class="math-inline">\\(5x-y+3z=0\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Suppose that

<div class="math-display">
$$
A \begin{bmatrix} 3 \\\\ 0 \\\\ 0 \end{bmatrix} = \begin{bmatrix} 15 \\\\ 30 \\\\ 0 \end{bmatrix}
$$
</div>

 Find <span class="math-inline">\\(A\\)</span>. Show your work, and <span class="math-inline">\\(\boxed{\text{circle}}\\)</span> your final answer, which should be a matrix with no variables.

<details markdown="1"><summary>Solution</summary>

Since <span class="math-inline">\\(\text{rank}(A)=1\\)</span> and the row space is

<div class="math-display">
$$
\text{span}\left( \left\{ \begin{bmatrix} 5 \\\\ -1 \\\\ 3 \end{bmatrix} \right\} \right),
$$
</div>

 each row of <span class="math-inline">\\(A\\)</span> must be a scalar multiple of <span class="math-inline">\\(\begin{bmatrix} 5 &amp; -1 &amp; 3 \end{bmatrix}\\)</span>. So, for some constants <span class="math-inline">\\(a\\)</span>, <span class="math-inline">\\(b\\)</span>, and <span class="math-inline">\\(c\\)</span>,

<div class="math-display">
$$
A =
\begin{bmatrix}
5a & -a & 3a \\\\
5b & -b & 3b \\\\
5c & -c & 3c
\end{bmatrix}
$$
</div>

 We're told that

<div class="math-display">
$$
A \begin{bmatrix} 3 \\\\ 0 \\\\ 0 \end{bmatrix}
=
\begin{bmatrix} 15 \\\\ 30 \\\\ 0 \end{bmatrix}
$$
</div>

 The left-hand side is 3 times the first column of <span class="math-inline">\\(A\\)</span>, so the first column of <span class="math-inline">\\(A\\)</span> is

<div class="math-display">
$$
\begin{bmatrix} 5 \\\\ 10 \\\\ 0 \end{bmatrix}
$$
</div>

 This gives

<div class="math-display">
$$
5a = 5, \qquad 5b = 10, \qquad 5c = 0
$$
</div>

 so <span class="math-inline">\\(a=1\\)</span>, <span class="math-inline">\\(b=2\\)</span>, and <span class="math-inline">\\(c=0\\)</span>. Therefore,

<div class="math-display">
$$
A =
\begin{bmatrix}
5 & -1 & 3 \\\\
10 & -2 & 6 \\\\
0 & 0 & 0
\end{bmatrix}
$$
</div>

</details>

</div>
</div>

</div>
