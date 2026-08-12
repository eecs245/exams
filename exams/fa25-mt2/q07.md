---
number: 7
title: Complexity
heading_suffix: : Complexity <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">10 pts</span>
points: 10
flags: []
has_solution: true
images: []
---

Suppose <span class="math-inline">\\(f: \mathbb{R} \to \mathbb{R}\\)</span> is a convex function.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Find scalars <span class="math-inline">\\(a\\)</span> and <span class="math-inline">\\(b\\)</span> such that <span class="math-inline">\\(f(3) \leq a f(2) + b f(6)\\)</span>. Show your work and <span class="math-inline">\\(\boxed{\text{circle}}\\)</span> your final answer, which should be a pair of scalars.

<details markdown="1"><summary>Solution</summary>

Recall the definition of convexity (which is relevant, since <span class="math-inline">\\(f\\)</span> is told to us to be convex):

<div class="math-display">
$$
f((1-t) x + ty) \leq (1-t) f(x) + t f(y)
$$
</div>

Matching the right-side of the inequality above to the right-side of the inequality given, we see that <span class="math-inline">\\(a = 1-t\\)</span> and <span class="math-inline">\\(b = t\\)</span>.

So, our job is to find <span class="math-inline">\\(1-t\\)</span> and <span class="math-inline">\\(t\\)</span> such that

<div class="math-display">
$$
3 = (1-t) \cdot 2 + t \cdot 6
$$
</div>

 i.e. <span class="math-inline">\\(\textbf{to write 3 as a linear combination of 2 and 6}\\)</span>.

<div class="math-display">
$$
3 = (1 - t) \cdot 2 + t \cdot 6 = 2 - 2t + 6t = 2 + 4t \implies t = \frac{3 - 2}{4} = \frac{1}{4}
$$
</div>

So, <span class="math-inline">\\(\boxed{a = \frac{3}{4}, b = \frac{1}{4}}\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Using the result from part **a)**, prove that <span class="math-inline">\\(f(3) + f(5) \leq f(2) + f(6)\\)</span>.

<details markdown="1"><summary>Solution</summary>

In part **a)**, we proved

<div class="math-display">
$$
f(3) \leq \frac{3}{4} f(2) + \frac{1}{4} f(6)
$$
</div>

 Since there's an <span class="math-inline">\\(f(5)\\)</span> in the left side of expression we want to prove, we need to find an inequality for <span class="math-inline">\\(f(5)\\)</span> in terms of <span class="math-inline">\\(f(2)\\)</span> and <span class="math-inline">\\(f(6)\\)</span>.

Trying to match the pattern, let <span class="math-inline">\\(t = \frac{3}{4}\\)</span>, and keep <span class="math-inline">\\(x = 2\\)</span> and <span class="math-inline">\\(y = 6\\)</span>. Where did <span class="math-inline">\\(t = \frac{3}{4}\\)</span> come from? You could have found it from solving <span class="math-inline">\\((1-t) \cdot 2 + t \cdot 6 = 5\\)</span>, or by guessing/observing that no other value of <span class="math-inline">\\(t\\)</span> would eventually allow us to add the two inequalities together to get <span class="math-inline">\\(f(2) + f(6)\\)</span> on the right.

<div class="math-display">
$$
\begin{align*}
f((1-t)x + ty) &\leq (1-t)f(x) + t f(y) \\\\
f\left( (1-\frac{3}{4}) \cdot 2 + \frac{3}{4} \cdot 6 \right) &\leq (1-\frac{3}{4}) f(2) + \frac{3}{4} f(6) \\\\
f(5) &\leq \frac{1}{4} f(2) + \frac{3}{4} f(6)
\end{align*}
$$
</div>

Let's add this to our previous inequality.

<div class="math-display">
$$
\begin{align*}
f(3) + f(5) &\leq \frac{3}{4} f(2) + \frac{1}{4} f(6) + \frac{1}{4} f(2) + \frac{3}{4} f(6)
\\\\ f(3) + f(5) &\leq f(2) + f(6)
\end{align*}
$$
</div>

as required!
</details>
</div>
</div>

</div>
