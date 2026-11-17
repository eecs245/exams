Suppose <span class="math-inline">\\(A\\)</span> is an <span class="math-inline">\\(n \times n\\)</span> matrix.

For each statement below, determine whether it is true or false. If true, prove that it is true. If false, give a counterexample or a short explanation.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge badge-points">4 pts</span> If <span class="math-inline">\\(A\\)</span> is symmetric, then <span class="math-inline">\\(A^2\\)</span> must be symmetric.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

This is true. Since <span class="math-inline">\\(A\\)</span> is symmetric, <span class="math-inline">\\(A^T = A\\)</span>. So,

<div class="math-display">
$$
(A^2)^T = (AA)^T = A^T A^T = AA = A^2
$$
</div>

 Therefore, <span class="math-inline">\\(A^2\\)</span> is symmetric.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge badge-points">4 pts</span> If <span class="math-inline">\\(A^2\\)</span> is symmetric, then <span class="math-inline">\\(A\\)</span> must be symmetric.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> False</span></div>

This is false. For example, let

<div class="math-display">
$$
A =
  \begin{bmatrix}
  0 & 1 \\\\
  -1 & 0
  \end{bmatrix}
$$
</div>

 This matrix is not symmetric, but

<div class="math-display">
$$
A^2 =
  \begin{bmatrix}
  -1 & 0 \\\\
  0 & -1
  \end{bmatrix}
$$
</div>

 which is symmetric.

To see how to come up with more counterexamples, write

<div class="math-display">
$$
A = \begin{bmatrix} a & b \\\\ c & d \end{bmatrix},
  \qquad
  A^2 = \begin{bmatrix}
  a^2 + bc & b(a+d) \\\\
  c(a+d) & bc + d^2
  \end{bmatrix}
$$
</div>

 The off-diagonal entries of <span class="math-inline">\\(A^2\\)</span> agree exactly when <span class="math-inline">\\((b-c)(a+d)=0\\)</span>. Choose <span class="math-inline">\\(b \ne c\\)</span> so that <span class="math-inline">\\(A\\)</span> is not symmetric, and set <span class="math-inline">\\(d=-a\\)</span> so that both off-diagonal entries of <span class="math-inline">\\(A^2\\)</span> are zero. For example,

<div class="math-display">
$$
\begin{aligned}
\begin{bmatrix} -2 & 6 \\\\ 11 & 2 \end{bmatrix}^2
&= \begin{bmatrix} 70 & 0 \\\\ 0 & 70 \end{bmatrix} \\\\[6pt]
\begin{bmatrix} 1 & 1 \\\\ 0 & -1 \end{bmatrix}^2
&= \begin{bmatrix} 1 & 0 \\\\ 0 & 1 \end{bmatrix}
\end{aligned}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge badge-points">4 pts</span> If <span class="math-inline">\\(\vec x \in \text{nullsp}(A^T)\\)</span> and <span class="math-inline">\\(\vec y \in \text{colsp}(A)\\)</span>, then <span class="math-inline">\\(\vec x\\)</span> and <span class="math-inline">\\(\vec y\\)</span> are orthogonal.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

This is true. If <span class="math-inline">\\(\vec y \in \text{colsp}(A)\\)</span>, then <span class="math-inline">\\(\vec y = A\vec v\\)</span> for some vector <span class="math-inline">\\(\vec v\\)</span>. Since <span class="math-inline">\\(\vec x \in \text{nullsp}(A^T)\\)</span>, we know <span class="math-inline">\\(A^T \vec x = \vec 0\\)</span>. So,

<div class="math-display">
$$
\vec x \cdot \vec y
  =
  \vec x^T A \vec v
  =
  (A^T \vec x)^T \vec v
  =
  \vec 0^T \vec v
  =
  0
$$
</div>

 Therefore, <span class="math-inline">\\(\vec x\\)</span> and <span class="math-inline">\\(\vec y\\)</span> are orthogonal.
</details>

</div>
</div>

</div>
