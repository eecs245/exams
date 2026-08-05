---
number: 4
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>
points: 12
flags: []
has_solution: true
images: []
---

Suppose <span class="math-inline">\\(\vec u = \begin{bmatrix} 1 \\\\ 0 \\\\ 0 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec u + \vec v + \vec w = \begin{bmatrix} 4 \\\\ 0 \\\\ 0 \end{bmatrix}\\)</span>. Assume that none of <span class="math-inline">\\(\vec u\\)</span>, <span class="math-inline">\\(\vec v\\)</span>, or <span class="math-inline">\\(\vec w\\)</span> are the zero vector, <span class="math-inline">\\(\vec 0\\)</span>.

For each statement below, identify whether it is **impossible**, **possible**, or **guaranteed**, and provide a brief explanation in the box provided.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span>
<span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> are orthogonal.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Impossible</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Possible</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Guaranteed</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Impossible</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> Possible</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Guaranteed</span></div>

This is possible.

There is nothing stopping <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> from being orthogonal. For example, let <span class="math-inline">\\(\vec v = \begin{bmatrix} 0 \\\\ 1 \\\\ 0 \end{bmatrix}\\)</span>. Then, <span class="math-inline">\\(\vec u \cdot \vec v = 0 \cdot 0 + 0 \cdot 1 + 0 \cdot 0 = 0\\)</span>, so <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> are orthogonal, and we can still find a <span class="math-inline">\\(\vec w\\)</span> such that <span class="math-inline">\\(\vec u + \vec v + \vec w = \begin{bmatrix} 4 \\\\ 0 \\\\ 0 \end{bmatrix}\\)</span>. For example, let <span class="math-inline">\\(\vec w = \begin{bmatrix} 4 \\\\ 0 \\\\ 0 \end{bmatrix} - \vec u - \vec v = \begin{bmatrix} 3 \\\\ -1 \\\\ 0 \end{bmatrix}\\)</span>.

However, it's not guaranteed: <span class="math-inline">\\(\vec v = \begin{bmatrix} 2 \\\\ 0 \\\\ 0 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec w = \begin{bmatrix} 1 \\\\ 0 \\\\ 0 \end{bmatrix}\\)</span> satisfy <span class="math-inline">\\(\vec u + \vec v + \vec w = \begin{bmatrix} 4 \\\\ 0 \\\\ 0 \end{bmatrix}\\)</span>, but <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> are not orthogonal.

So, it is possible for <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> to be orthogonal.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> The set <span class="math-inline">\\(\lbrace\vec u, \vec v, \vec w\rbrace\\)</span> is linearly dependent.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Impossible</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Possible</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Guaranteed</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Impossible</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Possible</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> Guaranteed</span></div>

This is guaranteed.

<div class="math-display">
$$
\vec u + \vec v + \vec w = \begin{bmatrix} 4 \\\\ 0 \\\\ 0 \end{bmatrix}
$$
</div>

Since <span class="math-inline">\\(\vec u = \begin{bmatrix} 1 \\\\ 0 \\\\ 0 \end{bmatrix}\\)</span>, we can subtract <span class="math-inline">\\(4 \vec u\\)</span> from both sides to get

<div class="math-display">
$$
\vec u + \vec v + \vec w - 4 \vec u = \vec w - 3 \vec u = \begin{bmatrix} 4 \\\\ 0 \\\\ 0 \end{bmatrix} - 4 \begin{bmatrix} 1 \\\\ 0 \\\\ 0 \end{bmatrix}
$$
</div>

Or, equivalently,

<div class="math-display">
$$
- 3 \vec u + \vec v + \vec w = \vec 0
$$
</div>

This is a non-trivial linear combination of <span class="math-inline">\\(\vec u\\)</span>, <span class="math-inline">\\(\vec v\\)</span>, and <span class="math-inline">\\(\vec w\\)</span> that equals the zero vector, so the set <span class="math-inline">\\(\lbrace\vec u, \vec v, \vec w\rbrace\\)</span> is linearly dependent. Equivalently, we could say <span class="math-inline">\\(\vec w = 3 \vec u - \vec v\\)</span>, which means <span class="math-inline">\\(\vec w\\)</span> is a linear combination of <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span>, which also means the set is linearly dependent.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span>
<span class="math-inline">\\(\vec u\\)</span>, <span class="math-inline">\\(\vec v\\)</span>, and <span class="math-inline">\\(\vec w\\)</span> all have the same norm (length).

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Impossible</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Possible</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Guaranteed</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> Impossible</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Possible</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Guaranteed</span></div>

This is impossible.

Recall that the triangle inequality states that for any two vectors <span class="math-inline">\\(\vec v\\)</span> and <span class="math-inline">\\(\vec w\\)</span>,

<div class="math-display">
$$
\lVert \vec v + \vec w \rVert \leq \lVert \vec v \rVert + \lVert \vec w \rVert
$$
</div>

We know that <span class="math-inline">\\(\lVert \vec u \rVert = 1\\)</span>, so in order for the statement to be possible, we'd need both <span class="math-inline">\\(\lVert \vec v \rVert = 1\\)</span> and <span class="math-inline">\\(\lVert \vec w \rVert = 1\\)</span>. But, <span class="math-inline">\\(\vec v + \vec w = \begin{bmatrix} 3 \\\\ 0 \\\\ 0 \end{bmatrix}\\)</span>, so <span class="math-inline">\\(\lVert \vec v + \vec w \rVert = \sqrt{3^2 + 0^2 + 0^2} = \sqrt{9} = 3\\)</span>. In the triangle inequality, this would mean

<div class="math-display">
$$
\lVert \vec v + \vec w \rVert \leq \lVert \vec v \rVert + \lVert \vec w \rVert \implies 3 \leq 2
$$
</div>

This is a contradiction, so it is impossible for both <span class="math-inline">\\(\vec v\\)</span> and <span class="math-inline">\\(\vec w\\)</span> to have a norm of 1, and therefore impossible for all three vectors to have the same norm.
</details>

</div>
</div>

</div>
