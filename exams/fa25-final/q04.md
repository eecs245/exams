---
number: 4
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">8 pts</span> <span class="badge" data-flag="mt2-redemption" style="background-color: #9A3324; color: #FFFFFF; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">MT2 Redemption</span>
points: 8
flags: [mt2-redemption]
has_solution: true
images: []
---

Let <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> be as in the previous problem.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Suppose that for some value of <span class="math-inline">\\(c\\)</span>, <span class="math-inline">\\(P\\)</span> is the matrix that projects vectors in <span class="math-inline">\\(\mathbb{R}^3\\)</span> onto <span class="math-inline">\\(\text{span}(\lbrace\vec u, \vec v\rbrace)\\)</span>. **Select all** true statements below.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(P^2 = P\\)</span></span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(P\\)</span> is invertible</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(P\\)</span> is orthogonal</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(P\\)</span> is symmetric</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-square mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(P^2 = P\\)</span></span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(P\\)</span> is invertible</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(P\\)</span> is orthogonal</span><span class="mc-option"><span class="mc-square mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(P\\)</span> is symmetric</span></div>

If we let <span class="math-inline">\\(X = \begin{bmatrix} | &amp; | \\\\ \vec u &amp; \vec v \\\\ | &amp; | \end{bmatrix}\\)</span>, then no matter what <span class="math-inline">\\(c\\)</span> is, <span class="math-inline">\\(\text{rank}(X) = 2\\)</span>, meaning the <span class="math-inline">\\(2 \times 2\\)</span> matrix <span class="math-inline">\\(X^TX\\)</span> is invertible. Then,

<div class="math-display">
$$
P = X (X^TX)^{-1}X^T
$$
</div>

With this in mind:

-   <span class="math-inline">\\(P^2 = P\\)</span> is **true**. This is the defining property of a projection matrix: once a vector has been projected onto the plane, projecting it again does nothing.

-   Conceptually, <span class="math-inline">\\(P\\)</span> is **not** invertible, because multiple different vectors <span class="math-inline">\\(\vec y\\)</span> can be projected onto the same vector <span class="math-inline">\\(\vec p\\)</span>. The act of multiplying by <span class="math-inline">\\(P\\)</span> is not one-to-one, so <span class="math-inline">\\(P\\)</span> is not invertible.

-   <span class="math-inline">\\(P\\)</span> is **not** an orthogonal matrix. Orthogonal matrices preserve lengths, but projection usually shortens vectors unless they already lie in the plane. Also, orthogonal matrices are invertible, but <span class="math-inline">\\(P\\)</span> is not.

-   <span class="math-inline">\\(P\\)</span> is **symmetric**. This is a standard property of orthogonal projection matrices, and you can also verify it directly from <span class="math-inline">\\(P = X(X^TX)^{-1}X^T\\)</span> by taking the transpose.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Now, suppose <span class="math-inline">\\(\vec y \in \mathbb{R}^3\\)</span>. Let <span class="math-inline">\\(\vec p \\)</span> be the projection of <span class="math-inline">\\(\vec y\\)</span> onto <span class="math-inline">\\(\text{span}(\lbrace\vec u, \vec v\rbrace)\\)</span>, and let <span class="math-inline">\\(\vec e = \vec y - \vec p\\)</span>.

There is no value of <span class="math-inline">\\(c\\)</span> that guarantees that the components of <span class="math-inline">\\(\vec e\\)</span> sum to 0, for every <span class="math-inline">\\(\vec y \in \mathbb{R}^3\\)</span>. That is, it is **not** guaranteed that <span class="math-inline">\\(e&#95;1 + e&#95;2 + e&#95;3 = 0\\)</span> for every <span class="math-inline">\\(\vec y \in \mathbb{R}^3\\)</span>.

Give a 1-2 sentence English explanation for why it is **not** guaranteed that <span class="math-inline">\\(e&#95;1 + e&#95;2 + e&#95;3 = 0\\)</span> for every <span class="math-inline">\\(\vec y \in \mathbb{R}^3\\)</span>. <em>Hint: What <strong>would</strong> have to be true about <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> to make this guarantee for every <span class="math-inline">\\(\vec y\\)</span>?</em>

<details markdown="1"><summary>Solution</summary>

For <span class="math-inline">\\(e&#95;1 + e&#95;2 + e&#95;3\\)</span> to always equal 0, every error vector <span class="math-inline">\\(\vec e\\)</span> would have to be orthogonal to <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ 1 \\\\ 1 \end{bmatrix}\\)</span>. Since every error vector is orthogonal to <span class="math-inline">\\(\text{span}(\lbrace\vec u, \vec v\rbrace)\\)</span>, this would require <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ 1 \\\\ 1 \end{bmatrix}\\)</span> to lie in <span class="math-inline">\\(\text{span}(\lbrace\vec u, \vec v\rbrace)\\)</span>, but no value of <span class="math-inline">\\(c\\)</span> makes that happen.
</details>

</div>
</div>

</div>
