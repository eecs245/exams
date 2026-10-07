Consider the line <span class="math-inline">\\(L\\)</span> in <span class="math-inline">\\(\mathbb R^3\\)</span> defined below.

<div class="math-display">
$$
L=\left\{\begin{bmatrix}6\\\\2\\\\-4\end{bmatrix}+t\begin{bmatrix}3\\\\1\\\\-2\end{bmatrix}:t\in\mathbb R\right\}
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge badge-points">2 pts</span> True or False: <span class="math-inline">\\(L\\)</span> is a subspace of <span class="math-inline">\\(\mathbb R^3\\)</span>.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

**True.** The initial vector is twice the direction vector, so

<div class="math-display">
$$
\begin{bmatrix}6\\\\2\\\\-4\end{bmatrix}+t\begin{bmatrix}3\\\\1\\\\-2\end{bmatrix}
=(t+2)\begin{bmatrix}3\\\\1\\\\-2\end{bmatrix}
$$
</div>

 As <span class="math-inline">\\(t\\)</span> ranges over <span class="math-inline">\\(\mathbb R\\)</span>, so does <span class="math-inline">\\(t+2\\)</span>. Hence <span class="math-inline">\\(L\\)</span> is the span of <span class="math-inline">\\(\begin{bmatrix}3\\\\1\\\\-2\end{bmatrix}\\)</span>, so it is a subspace of <span class="math-inline">\\(\mathbb R^3\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge badge-points">3 pts</span> Consider the following two planes:

<div class="math-display">
$$
\begin{aligned}
x+2y+z&=0 \\\\
4x+4y+z&=0
\end{aligned}
$$
</div>

 Describe the set of points that lie on <span class="math-inline">\\(L\\)</span> and on **both** planes.

<span class="mc-bubble" aria-hidden="true"></span> There are no points in the intersection.

<span class="mc-bubble" aria-hidden="true"></span> A single point.

<span class="mc-bubble" aria-hidden="true"></span> An entire line of points.

<span class="mc-bubble" aria-hidden="true"></span> An entire plane of points.

<details markdown="1"><summary>Solution</summary>

<span class="mc-bubble" aria-hidden="true"></span> An entire plane of points.

**A single point.** A point on <span class="math-inline">\\(L\\)</span> has coordinates <span class="math-inline">\\(x=6+3t\\)</span>, <span class="math-inline">\\(y=2+t\\)</span>, and <span class="math-inline">\\(z=-4-2t\\)</span>. Substituting into the two plane equations gives

<div class="math-display">
$$
6+3t=0,\qquad 28+14t=0
$$
</div>

 Both hold exactly when <span class="math-inline">\\(t=-2\\)</span>, which gives the origin. Thus, the common intersection is <span class="math-inline">\\(\lbrace \vec 0\rbrace \\)</span>.
</details>

</div>
</div>

</div>
