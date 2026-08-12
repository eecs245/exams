---
number: 6
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>
points: 12
flags: []
has_solution: true
images: []
---

Suppose <span class="math-inline">\\(A\\)</span> is an <span class="math-inline">\\(n \times d\\)</span> matrix and <span class="math-inline">\\(\vec x \in \mathbb{R}^d\\)</span>. Consider the function <span class="math-inline">\\(f: \mathbb{R}^d \to \mathbb{R}\\)</span> given by

<div class="math-display">
$$
f(\vec x) = \left\|A\vec x\right\|
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">2 pts</span> True or False: <span class="math-inline">\\(f(\vec x)\\)</span> is a linear transformation.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> False</span></div>

This is false. Recall, a linear transformation must satisfy <span class="math-inline">\\(f(c \vec x) = c f(\vec x)\\)</span> for any scalar <span class="math-inline">\\(c\\)</span>. But, suppose we pick <span class="math-inline">\\(n = d = 1\\)</span>, and let <span class="math-inline">\\(A = [1]\\)</span> (here we're thinking of a <span class="math-inline">\\(1 \times 1\\)</span> matrix as a scalar). Then, <span class="math-inline">\\(f(x)\\)</span> is just the absolute value of the scalar <span class="math-inline">\\(x\\)</span>.

<div class="math-display">
$$
f(x) = |x|
$$
</div>

But, <span class="math-inline">\\(f(-2) = 2\\)</span> is not the same as <span class="math-inline">\\(-2 f(1) = -2\\)</span>. So, this <span class="math-inline">\\(f(x)\\)</span> is not a linear transformation, and thus in general <span class="math-inline">\\(f(\vec x) = \lVert A \vec x \rVert\\)</span> is not a linear transformation.

Another way to think about why <span class="math-inline">\\(f(\vec x)\\)</span> is not linear is to use the fact that <span class="math-inline">\\(\lVert A \vec x \rVert^2 = \vec x^T A^T A \vec x\\)</span>:

<div class="math-display">
$$
f(\vec x) = \sqrt{\vec x^T A^T A \vec x}
$$
</div>

 <span class="math-inline">\\(f(\vec x)\\)</span> is the square root of a quadratic form, which is not linear.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">10 pts</span> Find <span class="math-inline">\\(\nabla f(\vec x)\\)</span>. Assume that <span class="math-inline">\\(A \vec x \neq \vec 0\\)</span>. Show your work, and write your final answer in the bottom-right corner of the box. Your answer should be an expression in terms of <span class="math-inline">\\(A\\)</span>, <span class="math-inline">\\(\vec x\\)</span>, and/or constants. <em>Hint: Start by taking the gradient of <span class="math-inline">\\(\lVert A \vec x \rVert^2\\)</span>, then apply the chain rule.</em>

<div class="math-display">
$$
\nabla f(\vec x) = \_\_\_\_\_\_
$$
</div>

<details markdown="1"><summary>Solution</summary>

As the hint suggests, let's start by writing

<div class="math-display">
$$
\left\|A\vec x\right\|^2
=
(A\vec x)^T(A\vec x)
=
\vec x^T A^T A \vec x
$$
</div>

 Using the quadratic-form gradient rule,

<div class="math-display">
$$
\nabla \left\|A\vec x\right\|^2 = 2A^TA\vec x
$$
</div>

 Now,

<div class="math-display">
$$
f(\vec x) = \left\|A\vec x\right\|
=
\sqrt{\left\|A\vec x\right\|^2}
$$
</div>

 The chain rule from [Chapter 8.2](https://notes.eecs245.org/gradients/gradients-matrix-vector-operations/#chain-rule-for-vector-to-scalar-functions) states that if <span class="math-inline">\\(f(\vec x) = h(g(\vec x))\\)</span>, where <span class="math-inline">\\(h: \mathbb{R} \to \mathbb{R}\\)</span> and <span class="math-inline">\\(g: \mathbb{R}^d \to \mathbb{R}\\)</span> are both differentiable, then <span class="math-inline">\\(\nabla f(\vec x) = h'(g(\vec x)) \nabla g(\vec x)\\)</span>.

Here, <span class="math-inline">\\(h(x) = \sqrt{x}\\)</span> (so <span class="math-inline">\\(h'(x) = \displaystyle \frac{1}{2\sqrt{x}}\\)</span>) and <span class="math-inline">\\(g(\vec x) = \left\|A\vec x\right\|^2\\)</span>, so

<div class="math-display">
$$
\nabla f(\vec x)
=
\frac{1}{2\sqrt{\left\|A\vec x\right\|^2}}
\left( 2A^TA\vec x \right)
=
\frac{A^TA\vec x}{\left\|A\vec x\right\|}
$$
</div>

</details>

</div>
</div>

</div>
