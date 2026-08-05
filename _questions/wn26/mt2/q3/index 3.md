---
number: 3
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">11 pts</span>
points: 11
flags: []
has_solution: true
images: []
---

Suppose <span class="math-inline">\\(A\\)</span> and <span class="math-inline">\\(B\\)</span> are both **non-zero** <span class="math-inline">\\(6 \times 6\\)</span> matrices, such that <span class="math-inline">\\(\text{rank}(A) = 4\\)</span> and that every column of <span class="math-inline">\\(B\\)</span> is in <span class="math-inline">\\(\text{nullsp}(A)\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> Fill in the blanks: The third \_\_(i)\_\_ of <span class="math-inline">\\(A\\)</span> is \_\_(ii)\_\_ to the fourth \_\_(iii)\_\_ of <span class="math-inline">\\(B\\)</span>.

1.
<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> column</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> row</span></div>

2.
<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> orthogonal</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> parallel</span></div>

3.
<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> column</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> row</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> column</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> row</span></div>

Every column of <span class="math-inline">\\(B\\)</span> is in <span class="math-inline">\\(\text{nullsp}(A)\\)</span>. From [Chapter 5.4 in the notes](https://notes.eecs245.org/matrices/null-space-rank-nullity/#example-orthogonal-complements), the row space of <span class="math-inline">\\(A\\)</span> and the null space of <span class="math-inline">\\(A\\)</span> are orthogonal complements. That means every row of <span class="math-inline">\\(A\\)</span> is orthogonal to every vector in <span class="math-inline">\\(\text{nullsp}(A)\\)</span>, and hence orthogonal to every column of <span class="math-inline">\\(B\\)</span>.

So, the third **row** of <span class="math-inline">\\(A\\)</span> is **orthogonal** to the fourth **column** of <span class="math-inline">\\(B\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> **Select all** possible values of <span class="math-inline">\\(\text{rank}(AB)\\)</span>.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 0</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 1</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 2</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 3</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 4</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 5</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 6</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 0</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 1</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 2</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 3</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 4</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 5</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 6</span></div>

Let <span class="math-inline">\\(\vec b&#95;1, \vec b&#95;2, \ldots, \vec b&#95;6\\)</span> be the columns of <span class="math-inline">\\(B\\)</span>. Since every column of <span class="math-inline">\\(B\\)</span> is in <span class="math-inline">\\(\text{nullsp}(A)\\)</span>, we have 

<div class="math-display">
$$
A \vec b_j = \vec 0
$$
</div>

 for every <span class="math-inline">\\(j\\)</span>. But the <span class="math-inline">\\(j\\)</span>th column of <span class="math-inline">\\(AB\\)</span> is exactly <span class="math-inline">\\(A \vec b&#95;j\\)</span>, so every column of <span class="math-inline">\\(AB\\)</span> is <span class="math-inline">\\(\vec 0\\)</span>.

Therefore, 

<div class="math-display">
$$
AB = 0_{6 \times 6} \implies \text{rank}(AB) = 0_{6 \times 6}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> **Select all** possible values of <span class="math-inline">\\(\text{rank}(B)\\)</span>.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 0</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 1</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 2</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 3</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 4</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 5</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 6</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 0</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 1</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 2</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 3</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 4</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 5</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 6</span></div>

Since <span class="math-inline">\\(A\\)</span> is <span class="math-inline">\\(6 \times 6\\)</span> with rank 4, the rank-nullity theorem gives 

<div class="math-display">
$$
\dim(\text{nullsp}(A)) = 6 - 4 = 2
$$
</div>

 Every column of <span class="math-inline">\\(B\\)</span> lies in <span class="math-inline">\\(\text{nullsp}(A)\\)</span>, so 

<div class="math-display">
$$
\text{colsp}(B) \subseteq \text{nullsp}(A)
$$
</div>

 Therefore, 

<div class="math-display">
$$
\text{rank}(B) = \dim(\text{colsp}(B)) \leq 2
$$
</div>

Also, <span class="math-inline">\\(B\\)</span> is non-zero, so <span class="math-inline">\\(\text{rank}(B) \neq 0\\)</span>.

So the only possible values are **1** and **2**.

Both are achievable: all columns of <span class="math-inline">\\(B\\)</span> could be multiples of one non-zero vector in <span class="math-inline">\\(\text{nullsp}(A)\\)</span>, or they could span all of <span class="math-inline">\\(\text{nullsp}(A)\\)</span> (which is a 2-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^6\\)</span>, since <span class="math-inline">\\(\text{rank}(A)=4\\)</span>).
</details>

</div>
</div>

</div>
