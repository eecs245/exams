---
number: 7
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> <span class="badge" data-flag="mt2-redemption" style="background-color: #9A3324; color: #FFFFFF; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">MT2 Redemption</span>
points: 6
flags: [mt2-redemption]
has_solution: true
images: [convexity-scale.png]
---

Consider the function <span class="math-inline">\\(f: \mathbb{R} \to \mathbb{R}\\)</span> graphed below.

<div style="text-align: center;">
<img src="imgs/convexity-scale.png" alt="image" style="width: 60%; max-width: 100%;">
</div>

Note that <span class="math-inline">\\(f\\)</span> is a piecewise linear function, with slopes of <span class="math-inline">\\(0\\)</span>, <span class="math-inline">\\(4\\)</span>, and <span class="math-inline">\\(-4\\)</span>. The slope changes at the following values of <span class="math-inline">\\(x\\)</span>: <span class="math-inline">\\(-6, -5, -2, -1, 1, 2, 5, 6\\)</span>.

Suppose we want to minimize <span class="math-inline">\\(f(x)\\)</span> using gradient descent. There are several values of <span class="math-inline">\\(x\\)</span> such that <span class="math-inline">\\(f\\)</span> is not differentiable at <span class="math-inline">\\(x\\)</span>; if any of our guesses <span class="math-inline">\\(x^{(0)}, x^{(1)}, x^{(2)}, \ldots\\)</span> ever evaluate to one of these values, we say that gradient descent **crashes**.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">2 pts</span> True or False: <span class="math-inline">\\(f(x)\\)</span> is convex on the domain <span class="math-inline">\\(x \in [-9, 9]\\)</span>.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> False</span></div>

This is false. In order for a function to be convex, it must be the case that we can draw a line segment between any two points on the function and the line segment never passes below the function, but this is not the case for this <span class="math-inline">\\(f\\)</span>. For example, connect <span class="math-inline">\\((-3, 1)\\)</span> to <span class="math-inline">\\((-1, -3)\\)</span>; the line segment is entirely beneath the function.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Suppose we choose a learning rate/step size of <span class="math-inline">\\(\alpha = 0.1\\)</span>.

Among the options below, which value of <span class="math-inline">\\(x^{(0)}\\)</span> will allow gradient descent to **converge to the global minimum** of <span class="math-inline">\\(f(x)\\)</span> **without crashing**?

If multiple values of <span class="math-inline">\\(x^{(0)}\\)</span> are possible, **select the value that converges the quickest** (i.e. in the fewest number of iterations).

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1.4\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1.6\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1.8\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1.9\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(2.0\\)</span></span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1.4\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(1.6\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1.8\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1.9\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(2.0\\)</span></span></div>

When <span class="math-inline">\\(x\\)</span> is between <span class="math-inline">\\(1\\)</span> and <span class="math-inline">\\(2\\)</span>, the slope is 4, so with learning rate <span class="math-inline">\\(\alpha = 0.1\\)</span>, gradient descent updates by 

<div class="math-display">
$$
x^{(t+1)} = x^{(t)} - 0.1(4) = x^{(t)} - 0.4
$$
</div>

 Now, let's check the options:

-   <span class="math-inline">\\(1.4 \to 1.0\\)</span>, so gradient descent crashes at the nondifferentiable point <span class="math-inline">\\(x=1\\)</span>.

-   <span class="math-inline">\\(1.6 \to 1.2 \to 0.8\\)</span>, so it reaches the flat global-minimum region without crashing.

-   <span class="math-inline">\\(1.8 \to 1.4 \to 1.0\\)</span>, so it crashes.

-   <span class="math-inline">\\(1.9 \to 1.5 \to 1.1 \to 0.7\\)</span>, so it also works, but it takes more iterations than starting at 1.6.

-   Starting at <span class="math-inline">\\(2.0\\)</span> crashes immediately, because <span class="math-inline">\\(f\\)</span> is not differentiable there.

Therefore, the correct choice is <span class="math-inline">\\(\boxed{1.6}\\)</span>.
</details>

</div>
</div>

</div>
