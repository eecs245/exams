---
number: 5
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">13 pts</span>
points: 13
flags: []
has_solution: true
images: []
---

Let

<div class="math-display">
$$
A = \begin{bmatrix} 1 & 0 & 0 & 0 & 0 \\\\ 2 & 1 & 0 & 0 & 4 \\\\ 3 & 1 & 0 & -7 & 4 \end{bmatrix}
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">5 pts</span> Recall, a CR decomposition of an <span class="math-inline">\\(n \times d\\)</span> matrix <span class="math-inline">\\(A\\)</span> is a product <span class="math-inline">\\(A = CR\\)</span>, where <span class="math-inline">\\(C\\)</span> is an <span class="math-inline">\\(n \times r\\)</span> matrix with linearly independent columns and <span class="math-inline">\\(R\\)</span> is an <span class="math-inline">\\(r \times d\\)</span> matrix with linearly independent rows, and <span class="math-inline">\\(r = \text{rank}(A)\\)</span>.

Provide a CR decomposition of <span class="math-inline">\\(A\\)</span>. Your answers should be matrices with no variables.

<span class="math-inline">\\(C = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;, \quad R = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>

<details markdown="1"><summary>Solution</summary>

The columns of <span class="math-inline">\\(A\\)</span> are

<div class="math-display">
$$
\vec c_1 = \begin{bmatrix} 1 \\\\ 2 \\\\ 3 \end{bmatrix}, \quad
\vec c_2 = \begin{bmatrix} 0 \\\\ 1 \\\\ 1 \end{bmatrix}, \quad
\vec c_3 = \begin{bmatrix} 0 \\\\ 0 \\\\ 0 \end{bmatrix}, \quad
\vec c_4 = \begin{bmatrix} 0 \\\\ 0 \\\\ -7 \end{bmatrix}, \quad
\vec c_5 = \begin{bmatrix} 0 \\\\ 4 \\\\ 4 \end{bmatrix}
$$
</div>

Reading left-to-right, columns 1, 2, and 4 are linearly independent, so we place them in <span class="math-inline">\\(C\\)</span>:

<div class="math-display">
$$
C = \begin{bmatrix}
1 & 0 & 0 \\\\
2 & 1 & 0 \\\\
3 & 1 & -7
\end{bmatrix}
$$
</div>

Now we need to express each column of <span class="math-inline">\\(A\\)</span> as a linear combination of the columns of <span class="math-inline">\\(C\\)</span>:

<div class="math-display">
$$
\vec c_1 = 1\vec c_1 + 0\vec c_2 + 0\vec c_4, \quad
\vec c_2 = 0\vec c_1 + 1\vec c_2 + 0\vec c_4, \quad
\vec c_3 = \vec 0,
$$
</div>



<div class="math-display">
$$
\vec c_4 = 0\vec c_1 + 0\vec c_2 + 1\vec c_4, \quad
\vec c_5 = 0\vec c_1 + 4\vec c_2 + 0\vec c_4
$$
</div>

 The coefficients in each linear combination are the entries in the corresponding column of <span class="math-inline">\\(R\\)</span>. So,

<div class="math-display">
$$
R = \begin{bmatrix}
1 & 0 & 0 & 0 & 0 \\\\
0 & 1 & 0 & 0 & 4 \\\\
0 & 0 & 0 & 1 & 0
\end{bmatrix}
$$
</div>

Thus, one CR decomposition is

<div class="math-display">
$$
A =
\begin{bmatrix}
1 & 0 & 0 \\\\
2 & 1 & 0 \\\\
3 & 1 & -7
\end{bmatrix}
\begin{bmatrix}
1 & 0 & 0 & 0 & 0 \\\\
0 & 1 & 0 & 0 & 4 \\\\
0 & 0 & 0 & 1 & 0
\end{bmatrix}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> Find <span class="math-inline">\\(\text{dim}(\text{nullsp}(A^T))\\)</span>. Give your answer as an integer with no variables.

<span class="math-inline">\\(\text{dim}(\text{nullsp}(A^T)) = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>

<details markdown="1"><summary>Solution</summary>

The matrix <span class="math-inline">\\(A\\)</span> has 3 rows and rank 3. Applying rank-nullity to <span class="math-inline">\\(A^T\\)</span>, we get

<div class="math-display">
$$
\begin{align*}
\text{rank}(A^T) + \dim(\text{nullsp}(A^T)) &= \text{number of columns of } A^T = 3
\end{align*}
$$
</div>

Since <span class="math-inline">\\(\text{rank}(A^T)=\text{rank}(A)=3\\)</span>,

<div class="math-display">
$$
\begin{align*}
3 + \dim(\text{nullsp}(A^T)) &= 3 \\\\
\dim(\text{nullsp}(A^T)) &= 0
\end{align*}
$$
</div>

This means that <span class="math-inline">\\(A^T\\)</span>'s null space is <span class="math-inline">\\(\left\lbrace \vec 0 \right\rbrace\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
(5 pts) Suppose we apply the Gram-Schmidt process to the **rows** of <span class="math-inline">\\(A\\)</span>, and place the resulting orthonormal vectors into the **rows** of a new matrix, <span class="math-inline">\\(Q\\)</span>.

Let <span class="math-inline">\\(P\\)</span> be the matrix that projects vectors in <span class="math-inline">\\(\mathbb{R}^5\\)</span> onto <span class="math-inline">\\(\text{colsp}(Q^T)\\)</span> (the row space of <span class="math-inline">\\(Q\\)</span>). In other words, if <span class="math-inline">\\(\vec y \in \mathbb{R}^5\\)</span>, then <span class="math-inline">\\(P\vec y\\)</span> is the projection of <span class="math-inline">\\(\vec y\\)</span> onto <span class="math-inline">\\(\text{colsp}(Q^T)\\)</span>.

Find an expression for <span class="math-inline">\\(P\\)</span> in terms of <span class="math-inline">\\(Q\\)</span> and <span class="math-inline">\\(Q^T\\)</span>. Show your work, and <span class="math-inline">\\(\boxed{\text{circle}}\\)</span> your final answer, which should be an expression in terms of <span class="math-inline">\\(Q\\)</span> and <span class="math-inline">\\(Q^T\\)</span>. Answers that aren't fully simplified will not be given credit.

<div class="math-display">
$$
P = \_\_\_\_\_\_
$$
</div>

<details markdown="1"><summary>Solution</summary>

In general, the projection matrix onto <span class="math-inline">\\(\text{colsp}(X)\\)</span>, where <span class="math-inline">\\(X\\)</span> is any matrix with linearly independent columns, is

<div class="math-display">
$$
P = X(X^TX)^{-1}X^T
$$
</div>

Here, we want to project onto <span class="math-inline">\\(\text{colsp}(Q^T)\\)</span>, so we should use <span class="math-inline">\\(X = Q^T\\)</span>:

<div class="math-display">
$$
P = Q^T((Q^T)^TQ^T)^{-1}(Q^T)^T = Q^T(QQ^T)^{-1}Q
$$
</div>

But, since <span class="math-inline">\\(Q\\)</span>'s rows are orthonormal, <span class="math-inline">\\(QQ^T = I\\)</span>. This is because <span class="math-inline">\\(QQ^T\\)</span> is a matrix containing the dot products of the rows of <span class="math-inline">\\(Q\\)</span> with each other (the same way <span class="math-inline">\\(Q^TQ\\)</span> is a matrix containing the dot products of the columns of <span class="math-inline">\\(Q\\)</span> with each other). Since the rows of <span class="math-inline">\\(Q\\)</span> are orthonormal, the dot products are all 0 except for the diagonal, which is 1.

So,

<div class="math-display">
$$
P = Q^T I Q = Q^T Q
$$
</div>

</details>

</div>
</div>

</div>
