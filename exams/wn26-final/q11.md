---
number: 11
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">10 pts</span>
points: 10
flags: []
has_solution: true
images: []
---

Let <span class="math-inline">\\(S\\)</span> be a <span class="math-inline">\\(3 \times 3\\)</span> **symmetric** matrix with eigenvectors <span class="math-inline">\\(\vec v&#95;1\\)</span>, <span class="math-inline">\\(\vec v&#95;2\\)</span>, and <span class="math-inline">\\(\vec v&#95;3\\)</span> corresponding to eigenvalues <span class="math-inline">\\(5\\)</span>, <span class="math-inline">\\(2\\)</span>, and <span class="math-inline">\\(-1\\)</span>, respectively. Assume that each <span class="math-inline">\\(\vec v&#95;i\\)</span> is a unit vector.

Suppose <span class="math-inline">\\(\vec x \in \mathbb{R}^3\\)</span> and that

<div class="math-display">
$$
\vec x = 3\vec v_1 - 4\vec v_2 + \vec v_3
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Write <span class="math-inline">\\(S^2 \vec x\\)</span> as a linear combination of <span class="math-inline">\\(\vec v&#95;1\\)</span>, <span class="math-inline">\\(\vec v&#95;2\\)</span>, and <span class="math-inline">\\(\vec v&#95;3\\)</span>. Fill in each box with a number with no variables.

<span class="math-inline">\\(S^2 \vec x = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;  \vec v&#95;1 + \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;  \vec v&#95;2 + \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;  \vec v&#95;3\\)</span>

<details markdown="1"><summary>Solution</summary>

Applying <span class="math-inline">\\(S^2\\)</span> multiplies each eigenvector by the square of its eigenvalue, so

<div class="math-display">
$$
S^2\vec x
=
3(5^2)\vec v_1 - 4(2^2)\vec v_2 + ((-1)^2)\vec v_3
=
\boxed{75\vec v_1 - 16\vec v_2 + \vec v_3}
$$
</div>

 This result doesn't rely on the fact that <span class="math-inline">\\(\vec v&#95;1\\)</span>, <span class="math-inline">\\(\vec v&#95;2\\)</span>, and <span class="math-inline">\\(\vec v&#95;3\\)</span> are unit vectors or orthogonal; we'll use these assumptions in the next part.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> What is the value of <span class="math-inline">\\(\lVert S\vec x \rVert^2\\)</span>?

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(24\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(26\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(218\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(290\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(5882\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Not enough information</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(24\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(26\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(218\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(290\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(5882\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Not enough information</span></div>

Applying <span class="math-inline">\\(S\\)</span> once gives

<div class="math-display">
$$
S\vec x = 15\vec v_1 - 8\vec v_2 - \vec v_3
$$
</div>

 Since <span class="math-inline">\\(S\\)</span> is symmetric, eigenvectors corresponding to distinct eigenvalues are orthogonal. The vectors <span class="math-inline">\\(\vec v&#95;1\\)</span>, <span class="math-inline">\\(\vec v&#95;2\\)</span>, and <span class="math-inline">\\(\vec v&#95;3\\)</span> are also unit vectors, so

<div class="math-display">
$$
\begin{align*}
\lVert S\vec x \rVert^2 &= \lVert 15\vec v_1 - 8\vec v_2 - \vec v_3 \rVert^2 \\\\
&= (15 \vec v_1 - 8\vec v_2 - \vec v_3) \cdot (15\vec v_1 - 8\vec v_2 - \vec v_3) \\\\
&= 15^2 \underbrace{(\vec v_1 \cdot \vec v_1)}_{1} - 8 \cdot 15 \underbrace{(\vec v_1 \cdot \vec v_2)}_{0} - 15 (\vec v_1 \cdot \vec v_3) \\\\
& \quad - 8 \cdot 15 (\vec v_2 \cdot \vec v_1) + 8^2 (\vec v_2 \cdot \vec v_2) + 8 (\vec v_2 \cdot \vec v_3) \\\\
& \quad - (\vec v_3 \cdot \vec v_1) - 8 (\vec v_3 \cdot \vec v_2) + (-1)^2(\vec v_3 \cdot \vec v_3) \\\\
&= 15^2 + 8^2 + 1^2 \\\\
&= 290
\end{align*}
$$
</div>

Yet another way to look at this is to see that <span class="math-inline">\\(S = Q \Lambda Q^T\\)</span>, where the columns of <span class="math-inline">\\(Q\\)</span> are the vectors <span class="math-inline">\\(\vec v&#95;i\\)</span> and the diagonal entries of <span class="math-inline">\\(\Lambda\\)</span> are <span class="math-inline">\\(5\\)</span>, <span class="math-inline">\\(2\\)</span>, and <span class="math-inline">\\(-1\\)</span>. So,

<div class="math-display">
$$
\begin{align*}
\lVert S\vec x \rVert^2
&= \vec x^T S^T S \vec x \\\\
&= \vec x^T S^2 \vec x \\\\
&= \vec x^T (Q \Lambda Q^T)^2 \vec x \\\\
&= \vec x^T Q \Lambda^2 Q^T \vec x \\\\
&= \vec x^T Q
\begin{bmatrix}
25 & 0 & 0 \\\\
0 & 4 & 0 \\\\
0 & 0 & 1
\end{bmatrix}
Q^T \vec x \\\\
&= \begin{bmatrix} 3 & -4 & 1 \end{bmatrix}
\begin{bmatrix}
25 & 0 & 0 \\\\
0 & 4 & 0 \\\\
0 & 0 & 1
\end{bmatrix}
\begin{bmatrix} 3 \\\\ -4 \\\\ 1 \end{bmatrix} \\\\
&= \boxed{290}
\end{align*}
$$
</div>

In this solution, we used the fact that <span class="math-inline">\\(\vec x = 3 \vec v&#95;1 - 4 \vec v&#95;2 + \vec v&#95;3 = Q \begin{bmatrix} 3 \\\\ -4 \\\\ 1 \end{bmatrix}\\)</span>, and since <span class="math-inline">\\(Q^T Q = I\\)</span> (if <span class="math-inline">\\(Q\\)</span>'s columns are the orthonormal <span class="math-inline">\\(\vec v&#95;i\\)</span>'s), then <span class="math-inline">\\(Q^T \vec x = Q^TQ \begin{bmatrix} 3 \\\\ -4 \\\\ 1 \end{bmatrix} = \begin{bmatrix} 3 \\\\ -4 \\\\ 1 \end{bmatrix}\\)</span>.
</details>

</div>
</div>

</div>
