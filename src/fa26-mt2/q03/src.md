Let <span class="math-inline">\\(X=CR\\)</span>, where <span class="math-inline">\\(a,b\\)</span> are unknown scalars. Furthermore, suppose that

<div class="math-display">
$$
C=\begin{bmatrix}4&0\\\\-2&5\\\\3&-1\\\\0&6\end{bmatrix},\qquad
R=\begin{bmatrix}1&3&a&-2&5\\\\0&4&8&b&0\end{bmatrix},\qquad
\begin{bmatrix}-5\\\\0\\\\1\\\\-2\\\\1\end{bmatrix}\in\text{nullsp}(X)
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge badge-points">4 pts</span> Determine the following values.

<span class="math-inline">\\(\text{rank}(X)=\\)</span> \_\_\_\_\_\_

<span class="math-inline">\\(\dim(\text{nullsp}(X))=\\)</span> \_\_\_\_\_\_

<details markdown="1"><summary>Solution</summary>

The columns of <span class="math-inline">\\(C\\)</span> are independent, and the rows of <span class="math-inline">\\(R\\)</span> are independent. This CR factorization therefore has <span class="math-inline">\\(\text{rank}(X)=2\\)</span>. Since <span class="math-inline">\\(X\\)</span> has five columns, rank-nullity gives <span class="math-inline">\\(\dim(\text{nullsp}(X))=5-2=3\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge badge-points">8 pts</span> Find <span class="math-inline">\\(a\\)</span> and <span class="math-inline">\\(b\\)</span>.

<details markdown="1"><summary>Solution</summary>

Let <span class="math-inline">\\(\vec v\\)</span> be the given vector in <span class="math-inline">\\(\text{nullsp}(X)\\)</span>. Then <span class="math-inline">\\(CR\vec v=\vec0\\)</span>. Since the columns of <span class="math-inline">\\(C\\)</span> are linearly independent, this requires <span class="math-inline">\\(R\vec v=\vec0\\)</span>. Therefore,

<div class="math-display">
$$
R\vec v=\begin{bmatrix}-5+a+4+5\\\\8-2b\end{bmatrix}
=\begin{bmatrix}a+4\\\\8-2b\end{bmatrix}=\vec0
$$
</div>

 It follows that <span class="math-inline">\\(\boxed{a=-4,\ b=4}\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge badge-points">4 pts</span> Which of the following choices of columns of <span class="math-inline">\\(X\\)</span> form a basis for <span class="math-inline">\\(\text{colsp}(X)\\)</span>? **Select all that apply.**

<span class="mc-square" aria-hidden="true"></span> Columns 1 and 2

<span class="mc-square" aria-hidden="true"></span> Columns 1 and 5

<span class="mc-square" aria-hidden="true"></span> Columns 2 and 3

<span class="mc-square" aria-hidden="true"></span> Columns 3 and 4

<span class="mc-square" aria-hidden="true"></span> Columns 4 and 5

<span class="mc-square" aria-hidden="true"></span> Columns 1, 2, and 3

<details markdown="1"><summary>Solution</summary>

<span class="mc-square mc-correct" aria-hidden="true"></span> Columns 1 and 2

<span class="mc-square" aria-hidden="true"></span> Columns 1 and 5

<span class="mc-square mc-correct" aria-hidden="true"></span> Columns 2 and 3

<span class="mc-square" aria-hidden="true"></span> Columns 3 and 4

<span class="mc-square mc-correct" aria-hidden="true"></span> Columns 4 and 5

<span class="mc-square" aria-hidden="true"></span> Columns 1, 2, and 3

Because <span class="math-inline">\\(C\\)</span> has linearly independent columns, we can check independence using the corresponding columns of <span class="math-inline">\\(R\\)</span>, with <span class="math-inline">\\(a=-4\\)</span> and <span class="math-inline">\\(b=4\\)</span>. Columns <span class="math-inline">\\(1\\)</span> and <span class="math-inline">\\(5\\)</span> are scalar multiples, as are columns <span class="math-inline">\\(3\\)</span> and <span class="math-inline">\\(4\\)</span>. Each remaining listed pair is independent.

To make this more explicit, let's write out <span class="math-inline">\\(X\\)</span> using <span class="math-inline">\\(X=CR\\)</span> and the values of <span class="math-inline">\\(a\\)</span> and <span class="math-inline">\\(b\\)</span>.

<div class="math-display">
$$
X=
\begin{bmatrix}4&0\\\\-2&5\\\\3&-1\\\\0&6\end{bmatrix}
\begin{bmatrix}1&3&-4&-2&5\\\\0&4&8&4&0\end{bmatrix}
=
\begin{bmatrix}
4&12&-16&-8&20\\\\
-2&14&48&24&-10\\\\
3&5&-20&-10&15\\\\
0&24&48&24&0
\end{bmatrix}
$$
</div>

 Column 5 is five times column 1, and column 4 is half of column 3. In each of the other listed pairs, the two columns are nonzero and neither is a scalar multiple of the other.

Since <span class="math-inline">\\(\text{rank}(X)=2\\)</span>, the valid bases are **columns 1 and 2, columns 2 and 3, and columns 4 and 5**. Three columns cannot form a basis for this two-dimensional space.
</details>

</div>
</div>

</div>
