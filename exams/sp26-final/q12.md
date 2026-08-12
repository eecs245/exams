---
number: 12
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">11 pts</span>
points: 11
flags: []
has_solution: true
images: []
---

Suppose <span class="math-inline">\\(A\\)</span> is a <span class="math-inline">\\(3 \times 3\\)</span> symmetric matrix with rank <span class="math-inline">\\(2\\)</span>. The eigenspace corresponding to <span class="math-inline">\\(\lambda=9\\)</span> is the plane

<div class="math-display">
$$
2x-y+2z=0
$$
</div>

 Suppose <span class="math-inline">\\(A=Q\Lambda Q^T\\)</span>, where <span class="math-inline">\\(Q\\)</span> is an orthogonal matrix and <span class="math-inline">\\(\Lambda\\)</span> is a diagonal matrix with eigenvalues of <span class="math-inline">\\(A\\)</span> on the diagonal, **sorted** from largest to smallest.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> Find <span class="math-inline">\\(\Lambda\\)</span>. Your answer should be a matrix with no variables.

<div class="math-display">
$$
\Lambda = \_\_\_\_\_\_
$$
</div>

<details markdown="1"><summary>Solution</summary>

Since <span class="math-inline">\\(A\\)</span> is symmetric, the spectral theorem from [Chapter 9.5](https://notes.eecs245.org/eigenvalues-and-eigenvectors/symmetric-matrices-spectral-theorem/) tells us that <span class="math-inline">\\(A\\)</span> is diagonalizable with orthogonal eigenspaces. The eigenspace for <span class="math-inline">\\(\lambda=9\\)</span> is a plane, so it is 2-dimensional. Since <span class="math-inline">\\(A\\)</span> has rank <span class="math-inline">\\(2\\)</span>, it is not invertible, so it has at least one eigenvalue of <span class="math-inline">\\(0\\)</span>. In fact, it has exactly one eigenvalue of <span class="math-inline">\\(0\\)</span>, since the other two eigenvalues are both <span class="math-inline">\\(9\\)</span>.

Since the eigenvalues are sorted from largest to smallest,

<div class="math-display">
$$
\Lambda=
\begin{bmatrix}
9&0&0\\\\
0&9&0\\\\
0&0&0
\end{bmatrix}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">8 pts</span> Consider the vector

<div class="math-display">
$$
\vec v
=
\begin{bmatrix}2 \\\\ 9 \\\\ -2\end{bmatrix}
=
4\begin{bmatrix}1\\\\2\\\\0\end{bmatrix}
-\begin{bmatrix}2\\\\-1\\\\2\end{bmatrix}
$$
</div>

 Find <span class="math-inline">\\(A\vec v\\)</span>. Show your work, and write your final answer in the box provided. Your answer should be a vector with no variables. <em>Hint: What does the spectral theorem tell us?</em>

<div class="math-display">
$$
A\vec v = \_\_\_\_\_\_
$$
</div>

<details markdown="1"><summary>Solution</summary>

The vector <span class="math-inline">\\(\begin{bmatrix}1\\\\2\\\\0\end{bmatrix}\\)</span> is in the eigenspace for <span class="math-inline">\\(\lambda=9\\)</span>, since it satisfies the equation of the eigenspace, <span class="math-inline">\\(2x-y+2z=0\\)</span>:

<div class="math-display">
$$
2(1)-2+2(0)=0
$$
</div>

 This means <span class="math-inline">\\(\begin{bmatrix}1\\\\2\\\\0\end{bmatrix}\\)</span> is an eigenvector of <span class="math-inline">\\(A\\)</span> with eigenvalue <span class="math-inline">\\(9\\)</span>.

The vector <span class="math-inline">\\(\begin{bmatrix}2\\\\-1\\\\2\end{bmatrix}\\)</span> is **orthogonal** to the plane <span class="math-inline">\\(2x-y+2z=0\\)</span> (conveniently, <span class="math-inline">\\(\begin{bmatrix} 2 \\\\ -1 \\\\ 2 \end{bmatrix}\\)</span> contains the coefficients of the plane equation, and the coefficients of the plane equation define a vector orthogonal to the plane). The spectral theorem tells us that this vector is in the eigenspace corresponding to <span class="math-inline">\\(\lambda=0\\)</span>, because **eigenvectors for different eigenvalues are orthogonal for symmetric matrices**. Therefore,

<div class="math-display">
$$
\begin{align*}
A\vec{v}
&=
A\left(4\begin{bmatrix}1\\\\2\\\\0\end{bmatrix}
-\begin{bmatrix}2\\\\-1\\\\2\end{bmatrix}\right) \\\\
&=
4\underbrace{A\begin{bmatrix}1\\\\2\\\\0\end{bmatrix}}_{\substack{\text{eigenvector} \\\\ \lambda = 9}}
- \underbrace{A\begin{bmatrix}2\\\\-1\\\\2\end{bmatrix}}_{\substack{\text{eigenvector} \\\\ \lambda = 0}} \\\\
&=
4\cdot 9\begin{bmatrix}1\\\\2\\\\0\end{bmatrix}
- 0\begin{bmatrix}2\\\\-1\\\\2\end{bmatrix} \\\\
&=
\begin{bmatrix}36\\\\72\\\\0\end{bmatrix}
\end{align*}
$$
</div>

</details>

</div>
</div>

</div>
