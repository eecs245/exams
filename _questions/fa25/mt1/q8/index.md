---
number: 8
title: Worst-Case Scenario
heading_suffix: : Worst-Case Scenario <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">8 pts</span>
points: 8
flags: []
has_solution: true
images: []
---

Suppose <span class="math-inline">\\(a, b, c, d, e\\)</span> are positive real numbers. Find the **largest** real number <span class="math-inline">\\(T\\)</span> such that it's guaranteed that

<div class="math-display">
$$
(a + b + c + d + e) \left( \frac{1}{a} + \frac{1}{b} + \frac{1}{c} + \frac{1}{d} + \frac{1}{e} \right) \geq T
$$
</div>

Think of <span class="math-inline">\\(T\\)</span> as the "best possible lower bound". For instance, we know that the expression on the left-hand side above must be greater than or equal to 0, since <span class="math-inline">\\(a, b, c, d, e\\)</span> are all positive, but <span class="math-inline">\\(T = 0\\)</span> is not the answer, since there's a larger value of <span class="math-inline">\\(T\\)</span> that also guarantees the inequality holds.

Show your work, and <span class="math-inline">\\(\boxed{\text{circle}}\\)</span> your final answer, which should be a number with no variables.

<em>Hint: Use the Cauchy-Schwarz inequality.</em>

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(T = 25\\)</span>.

Recall, the Cauchy-Schwarz inequality states that for any two vectors <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span>,

<div class="math-display">
$$
|\vec u \cdot \vec v| \leq \lVert \vec u \rVert \lVert \vec v \rVert
$$
</div>

Let's define two vectors <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> and then apply the Cauchy-Schwarz inequality to them.

<div class="math-display">
$$
\vec u = \begin{bmatrix} \sqrt{a} \\\\ \sqrt{b} \\\\ \sqrt{c} \\\\ \sqrt{d} \\\\ \sqrt{e} \end{bmatrix}, \quad \vec v = \begin{bmatrix} \frac{1}{\sqrt{a}} \\\\ \frac{1}{\sqrt{b}} \\\\ \frac{1}{\sqrt{c}} \\\\ \frac{1}{\sqrt{d}} \\\\ \frac{1}{\sqrt{e}} \end{bmatrix}
$$
</div>

Let's compute the three quantities involved in the inequality.

-   <span class="math-inline">\\(\lVert \vec u \rVert = \sqrt{a + b + c + d + e}\\)</span>

-   <span class="math-inline">\\(\lVert \vec v \rVert = \sqrt{\frac{1}{a} + \frac{1}{b} + \frac{1}{c} + \frac{1}{d} + \frac{1}{e}}\\)</span>

-   <span class="math-inline">\\(|\vec u \cdot \vec v| = |\sqrt{a} \cdot \frac{1}{\sqrt{a}} + \sqrt{b} \cdot \frac{1}{\sqrt{b}} + \sqrt{c} \cdot \frac{1}{\sqrt{c}} + \sqrt{d} \cdot \frac{1}{\sqrt{d}} + \sqrt{e} \cdot \frac{1}{\sqrt{e}}| = 5\\)</span>

So, we have that

<div class="math-display">
$$
5 \leq \sqrt{a + b + c + d + e} \cdot \sqrt{\frac{1}{a} + \frac{1}{b} + \frac{1}{c} + \frac{1}{d} + \frac{1}{e}}
$$
</div>

Squaring both sides of the inequality gives us

<div class="math-display">
$$
25 \leq (a + b + c + d + e) \left( \frac{1}{a} + \frac{1}{b} + \frac{1}{c} + \frac{1}{d} + \frac{1}{e} \right)
$$
</div>

This means that for any positive values of <span class="math-inline">\\(a, b, c, d, e\\)</span>, it's impossible for <span class="math-inline">\\((a + b + c + d + e) \left( \frac{1}{a} + \frac{1}{b} + \frac{1}{c} + \frac{1}{d} + \frac{1}{e} \right)\\)</span> to be less than 25. Finding a value equal to 25 is doable if we set <span class="math-inline">\\(a = b = c = d = e = 1\\)</span>. So, <span class="math-inline">\\(T = 25\\)</span> is the largest possible value of <span class="math-inline">\\(T\\)</span> that guarantees the inequality holds.
</details>
