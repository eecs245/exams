---
number: 4
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">13 pts</span>
points: 13
flags: []
has_solution: true
images: []
---

Suppose <span class="math-inline">\\(X\\)</span> is some <span class="math-inline">\\(3 \times d\\)</span> matrix, for some integer <span class="math-inline">\\(d\\)</span>. Let

<div class="math-display">
$$
\vec y = \begin{bmatrix} 9 \\\\ -5 \\\\ 3 \end{bmatrix}
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">5 pts</span> Which of the following **could** be the projection of <span class="math-inline">\\(\vec y\\)</span> onto <span class="math-inline">\\(\text{colsp}(X)\\)</span>?

Select an answer, then briefly justify your answer in the space provided using properties of projections. Correct answers without justification may not receive full credit.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} 5 \\\\ -7 \\\\ 4 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} 7 \\\\ -7 \\\\ 4 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} 6 \\\\ -7 \\\\ 4 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} 6 \\\\ -7 \\\\ 3 \end{bmatrix}\\)</span></span></div>

<details markdown="1"><summary>Solution</summary>

<span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} 6 \\\\ -7 \\\\ 3 \end{bmatrix}\\)</span>

If <span class="math-inline">\\(\vec p\\)</span> is the projection of <span class="math-inline">\\(\vec y\\)</span> onto <span class="math-inline">\\(\text{colsp}(X)\\)</span>, then the error

<div class="math-display">
$$
\vec y - \vec p
$$
</div>

 must be orthogonal to all vectors in <span class="math-inline">\\(\text{colsp}(X)\\)</span>, and hence orthogonal to <span class="math-inline">\\(\vec p\\)</span> itself.

For the third option, <span class="math-inline">\\(\vec p = \begin{bmatrix} 6 \\\\ -7 \\\\ 4 \end{bmatrix}\\)</span>, we have

<div class="math-display">
$$
\vec p = \begin{bmatrix} 6 \\\\ -7 \\\\ 4 \end{bmatrix} \implies
\vec y - \vec p = \begin{bmatrix} 9 \\\\ -5 \\\\ 3 \end{bmatrix} - \begin{bmatrix} 6 \\\\ -7 \\\\ 4 \end{bmatrix} = \begin{bmatrix} 3 \\\\ 2 \\\\ -1 \end{bmatrix}
$$
</div>

 The dot product of <span class="math-inline">\\(\vec p\\)</span> and <span class="math-inline">\\(\vec y - \vec p\\)</span> is

<div class="math-display">
$$
\begin{align*}
\vec p \cdot (\vec y - \vec p) = \begin{bmatrix} 6 \\\\ -7 \\\\ 4 \end{bmatrix} \cdot \begin{bmatrix} 3 \\\\ 2 \\\\ -1 \end{bmatrix}
&= 18 - 14 - 4 = 0
\end{align*}
$$
</div>

So <span class="math-inline">\\(\vec p = \begin{bmatrix} 6 \\\\ -7 \\\\ 4 \end{bmatrix}\\)</span> could be the projection of <span class="math-inline">\\(\vec y\\)</span> onto <span class="math-inline">\\(\text{colsp}(X)\\)</span>. If you repeat this calculation for the other three options, you'll find that <span class="math-inline">\\(\vec p\\)</span> and <span class="math-inline">\\(\vec y - \vec p\\)</span> are not orthogonal.
</details>

In each of the remaining parts, identify whether the statement is True or False and justify your answer in the space provided. Correct answers without justification may not receive full credit.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> If the projection of <span class="math-inline">\\(\vec y\\)</span> onto <span class="math-inline">\\(\text{colsp}(X)\\)</span> is <span class="math-inline">\\(\vec y\\)</span> itself, then <span class="math-inline">\\(\text{rank}(X)\\)</span> must be 3.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> False</span></div>

This is false. If the projection of <span class="math-inline">\\(\vec y\\)</span> onto <span class="math-inline">\\(\text{colsp}(X)\\)</span> is <span class="math-inline">\\(\vec y\\)</span> itself, that only tells us that <span class="math-inline">\\(\vec y \in \text{colsp}(X)\\)</span>.

But <span class="math-inline">\\(\text{colsp}(X)\\)</span> could still be a 1-dimensional or 2-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^3\\)</span> that happens to contain <span class="math-inline">\\(\vec y\\)</span>. For example, if <span class="math-inline">\\(\text{colsp}(X) = \text{span}\left(\left\lbrace \vec y \right\rbrace\right)\\)</span>, then the projection of <span class="math-inline">\\(\vec y\\)</span> is still <span class="math-inline">\\(\vec y\\)</span>, but <span class="math-inline">\\(\text{rank}(X)=1\\)</span>, not 3.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> If <span class="math-inline">\\(\text{rank}(X) = 3\\)</span>, then the projection of <span class="math-inline">\\(\vec y\\)</span> onto <span class="math-inline">\\(\text{colsp}(X)\\)</span> must be <span class="math-inline">\\(\vec y\\)</span> itself.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

This is true. If <span class="math-inline">\\(\text{rank}(X)=3\\)</span> and <span class="math-inline">\\(X\\)</span> is a <span class="math-inline">\\(3 \times d\\)</span> matrix, then <span class="math-inline">\\(\text{colsp}(X)\\)</span> is a 3-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^3\\)</span>. The only 3-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^3\\)</span> is all of <span class="math-inline">\\(\mathbb{R}^3\\)</span>.

But, this means every vector in <span class="math-inline">\\(\mathbb{R}^3\\)</span>, including <span class="math-inline">\\(\vec y\\)</span>, is in <span class="math-inline">\\(\text{colsp}(X)\\)</span>. Therefore, the projection of <span class="math-inline">\\(\vec y\\)</span> onto <span class="math-inline">\\(\text{colsp}(X)\\)</span> is just <span class="math-inline">\\(\vec y\\)</span> itself.
</details>

</div>
</div>

</div>
