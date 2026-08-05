---
number: 3
title: Nilpotence
heading_suffix: : Nilpotence <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>
points: 12
flags: []
has_solution: true
images: []
---

Suppose <span class="math-inline">\\(A\\)</span> is an <span class="math-inline">\\(n \times n\\)</span> matrix such that <span class="math-inline">\\(A^2 = 0&#95;{n \times n}\\)</span>, where <span class="math-inline">\\(0&#95;{n \times n}\\)</span> is an <span class="math-inline">\\(n \times n\\)</span> matrix of all zeros.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Prove that if <span class="math-inline">\\(\vec x \in \text{colsp}(A)\\)</span>, then <span class="math-inline">\\(\vec x \in \text{nullsp}(A)\\)</span>.

<details markdown="1"><summary>Solution</summary>

If <span class="math-inline">\\(\vec x \in \text{colsp}(A)\\)</span>, then <span class="math-inline">\\(\vec x = A \vec v\\)</span> for some <span class="math-inline">\\(\vec v \in \mathbb{R}^n\\)</span>. Then, multiplying both sides of <span class="math-inline">\\(\vec x = A \vec v\\)</span> by <span class="math-inline">\\(A\\)</span> on the left gives us:

<div class="math-display">
$$
A \vec x = A (A \vec v) = A^2 \vec v = 0_{n \times n} \vec v = \vec 0
$$
</div>

Since <span class="math-inline">\\(\vec x = A \vec v \implies A \vec x = \vec 0\\)</span>, we have <span class="math-inline">\\(\vec x \in \text{nullsp}(A)\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> In part **a)**, you showed that <span class="math-inline">\\(\text{colsp}(A)\\)</span> is a subset of <span class="math-inline">\\(\text{nullsp}(A)\\)</span>. Using this fact, find the **maximum** possible value of <span class="math-inline">\\(\text{rank}(A)\\)</span>. Show your work and <span class="math-inline">\\(\boxed{\text{circle}}\\)</span> your final answer, which should be an expression involving <span class="math-inline">\\(n\\)</span> and/or constants.

<details markdown="1"><summary>Solution</summary>

In the previous part, we showed that every element in <span class="math-inline">\\(\text{colsp}(A)\\)</span> is also in <span class="math-inline">\\(\text{nullsp}(A)\\)</span>. (The converse is not true.) Intuitively, this means that the column space is a subset of the null space, so it's "smaller" than the null space.

This means that

<div class="math-display">
$$
\text{dim}(\text{colsp}(A)) \leq \text{dim}(\text{nullsp}(A))
$$
</div>

 or in other words

<div class="math-display">
$$
\text{rank}(A) \leq \text{dim}(\text{nullsp}(A))
$$
</div>

Let's add <span class="math-inline">\\(\text{rank}(A)\\)</span> to both sides of the inequality; this will make the right-hand side look like something involved in the rank-nullity theorem.

<div class="math-display">
$$
\text{rank}(A) + \text{rank}(A) \leq \text{rank}(A) + \text{dim}(\text{nullsp}(A)) = n
$$
</div>

This tells us that <span class="math-inline">\\(2\text{rank}(A) \leq n\\)</span>, so <span class="math-inline">\\(\boxed{\text{rank}(A) \leq \frac{n}{2}}\\)</span> and so <span class="math-inline">\\(\frac{n}{2}\\)</span> is the maximum possible value of <span class="math-inline">\\(\text{rank}(A)\\)</span>.
</details>

</div>
</div>

</div>
