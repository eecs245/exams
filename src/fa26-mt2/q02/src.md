Let

<div class="math-display">
$$
B=\begin{bmatrix}2&2&2\\\\3&-3&0\\\\1&1&-2\end{bmatrix}
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge badge-points">4 pts</span> Find <span class="math-inline">\\(BB^T\\)</span>.

<details markdown="1"><summary>Solution</summary>

The entries of <span class="math-inline">\\(BB^T\\)</span> are the dot products of the rows of <span class="math-inline">\\(B\\)</span>. The three rows are mutually orthogonal, and their squared lengths are

<div class="math-display">
$$
2^2+2^2+2^2=12,\qquad 3^2+(-3)^2=18,\qquad 1^2+1^2+(-2)^2=6
$$
</div>

 Hence,

<div class="math-display">
$$
\boxed{BB^T=\begin{bmatrix}12&0&0\\\\0&18&0\\\\0&0&6\end{bmatrix}}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge badge-points">6 pts</span> Find <span class="math-inline">\\(B^{-1}\\)</span>. Fully simplify each entry. <em>Hint: Use part (a), not <span class="math-inline">\\(\det(B)\\)</span> or a <span class="math-inline">\\(3\times3\\)</span> inverse formula. If <span class="math-inline">\\(BB^T=C\\)</span>, what is <span class="math-inline">\\(B^{-1}\\)</span>?</em>

<details markdown="1"><summary>Solution</summary>

Let <span class="math-inline">\\(C=BB^T\\)</span>. Since <span class="math-inline">\\(C\\)</span> is invertible,

<div class="math-display">
$$
B(B^TC^{-1})=(BB^T)C^{-1}=CC^{-1}=I
$$
</div>

 Thus, <span class="math-inline">\\(B^{-1}=B^TC^{-1}\\)</span>. Using part (a),

<div class="math-display">
$$
B^{-1}
=\begin{bmatrix}2&3&1\\\\2&-3&1\\\\2&0&-2\end{bmatrix}
\begin{bmatrix}1/12&0&0\\\\0&1/18&0\\\\0&0&1/6\end{bmatrix}
=\boxed{\begin{bmatrix}1/6&1/6&1/6\\\\1/6&-1/6&1/6\\\\1/6&0&-1/3\end{bmatrix}}
$$
</div>

</details>

</div>
</div>

</div>
