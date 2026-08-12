---
number: 10
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>
points: 12
flags: []
has_solution: true
images: []
---

Let <span class="math-inline">\\(A=\begin{bmatrix}2&amp;4\\\\4&amp;2\end{bmatrix}\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">8 pts</span> Find all eigenvalues and eigenvectors of <span class="math-inline">\\(A\\)</span>. Show your work, and organize your answers as follows:

-   Put the larger eigenvalue in <span class="math-inline">\\(\lambda&#95;1\\)</span>, and a corresponding eigenvector in <span class="math-inline">\\(\vec v&#95;1\\)</span>.

-   Put the smaller eigenvalue in <span class="math-inline">\\(\lambda&#95;2\\)</span>, and a corresponding eigenvector in <span class="math-inline">\\(\vec v&#95;2\\)</span>.

<details markdown="1"><summary>Solution</summary>

The characteristic polynomial is

<div class="math-display">
$$
\begin{align*}
\det(A-\lambda I)
&=
\det\left(
\begin{bmatrix}
2-\lambda & 4\\\\
4 & 2-\lambda
\end{bmatrix}
\right) \\\\
&=
(2-\lambda)^2-16 \\\\
&=
\lambda^2-4\lambda-12 \\\\
&=
(\lambda-6)(\lambda+2)
\end{align*}
$$
</div>

So the eigenvalues are <span class="math-inline">\\(6\\)</span> and <span class="math-inline">\\(-2\\)</span>. Alternatively, using the trace and determinant facts from [Chapter 9.1](https://notes.eecs245.org/eigenvalues-and-eigenvectors/eigenvalues-eigenvectors/), you can arrive at this quickly by seeing that the eigenvalues must add to <span class="math-inline">\\(\text{trace}(A) = 2 + 2 = 4\\)</span> and multiply to <span class="math-inline">\\(\det(A) = 2 \cdot 2 - 4 \cdot 4 = -12\\)</span>.

For <span class="math-inline">\\(\lambda=6\\)</span>, write an eigenvector as

<div class="math-display">
$$
\vec{v}=\begin{bmatrix}a\\\\b\end{bmatrix}
$$
</div>

 Then

<div class="math-display">
$$
A\vec{v}
=
\begin{bmatrix}
2a+4b\\\\
4a+2b
\end{bmatrix}
=
6\begin{bmatrix}a\\\\b\end{bmatrix}
=
\begin{bmatrix}
6a\\\\
6b
\end{bmatrix}
$$
</div>

 so

<div class="math-display">
$$
2a+4b=6a
\qquad\text{and}\qquad
4a+2b=6b
$$
</div>

 Both equations say <span class="math-inline">\\(a=b\\)</span>, so one corresponding eigenvector is <span class="math-inline">\\(\begin{bmatrix}1\\\\1\end{bmatrix}\\)</span>.

For <span class="math-inline">\\(\lambda=-2\\)</span>, we similarly solve

<div class="math-display">
$$
\begin{bmatrix}
2a+4b\\\\
4a+2b
\end{bmatrix}
=
-2\begin{bmatrix}a\\\\b\end{bmatrix}
=
\begin{bmatrix}
-2a\\\\
-2b
\end{bmatrix}
$$
</div>

 so

<div class="math-display">
$$
2a+4b=-2a
\qquad\text{and}\qquad
4a+2b=-2b
$$
</div>

 Both equations say <span class="math-inline">\\(a=-b\\)</span>, so one corresponding eigenvector is <span class="math-inline">\\(\begin{bmatrix}1\\\\-1\end{bmatrix}\\)</span>. Therefore,

<div class="math-display">
$$
\lambda_1=6,\quad \vec{v}_1=\begin{bmatrix}1\\\\1\end{bmatrix},
\qquad
\lambda_2=-2,\quad \vec{v}_2=\begin{bmatrix}1\\\\-1\end{bmatrix}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> True or false: for all integer values of <span class="math-inline">\\(k\\)</span>, the matrix <span class="math-inline">\\(B=\begin{bmatrix}2&amp;4&amp;0\\\\4&amp;2&amp;0\\\\0&amp;0&amp;k\end{bmatrix}\\)</span> is diagonalizable.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

This is true. Since <span class="math-inline">\\(B\\)</span> is block diagonal (see [Chapter 9.4](https://notes.eecs245.org/eigenvalues-and-eigenvectors/multiplicities-diagonalization/#example-another-diagonalizable-matrix)), we can read off eigenvalues and eigenvectors from its individual blocks.

<div class="math-display">
$$
B=
\left[
\begin{array}{c|c}
\begin{array}{cc}
2 & 4 \\\\
4 & 2
\end{array}
&
\begin{array}{c}
0 \\\\ 0
\end{array}
\\\\
\hline
\begin{array}{cc}
0 & 0
\end{array}
&
\boxed{k}
\end{array}
\right]
$$
</div>

 The top-left block has two linearly independent eigenvectors, <span class="math-inline">\\(\begin{bmatrix}1\\\\1\\\\0\end{bmatrix}\\)</span> and <span class="math-inline">\\(\begin{bmatrix}1\\\\-1\\\\0\end{bmatrix}\\)</span>, with eigenvalues <span class="math-inline">\\(6\\)</span> and <span class="math-inline">\\(-2\\)</span>, and <span class="math-inline">\\(\begin{bmatrix}0\\\\0\\\\1\end{bmatrix}\\)</span> is an eigenvector with eigenvalue <span class="math-inline">\\(k\\)</span>. These three eigenvectors are linearly independent no matter what <span class="math-inline">\\(k\\)</span> is. Therefore <span class="math-inline">\\(B\\)</span> is diagonalizable for all integer values of <span class="math-inline">\\(k\\)</span>.

Another way to think about this is that for any <span class="math-inline">\\(k\\)</span>, the matrix <span class="math-inline">\\(B\\)</span> is symmetric, and hence diagonalizable, as told to us by the spectral theorem.
</details>

</div>
</div>

</div>
