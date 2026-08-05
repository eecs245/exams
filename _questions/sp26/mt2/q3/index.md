---
number: 3
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>
points: 12
flags: []
has_solution: true
images: []
---

Suppose <span class="math-inline">\\(A\\)</span> is an <span class="math-inline">\\(n \times n\\)</span> matrix.

For each statement below, determine whether it is true or false. If true, prove that it is true. If false, give a counterexample or a short explanation.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> If <span class="math-inline">\\(A\\)</span> is symmetric, then <span class="math-inline">\\(A^2\\)</span> must be symmetric.

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
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> If <span class="math-inline">\\(A^2\\)</span> is symmetric, then <span class="math-inline">\\(A\\)</span> must be symmetric.

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
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> If <span class="math-inline">\\(\vec x \in \text{nullsp}(A^T)\\)</span> and <span class="math-inline">\\(\vec y \in \text{colsp}(A)\\)</span>, then <span class="math-inline">\\(\vec x\\)</span> and <span class="math-inline">\\(\vec y\\)</span> are orthogonal.

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
