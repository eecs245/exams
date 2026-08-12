---
number: 9
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">10 pts</span>
points: 10
flags: []
has_solution: true
images: []
---

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">7 pts</span> Suppose <span class="math-inline">\\(x\\)</span> and <span class="math-inline">\\(y\\)</span> are non-negative numbers. Using the Cauchy-Schwarz inequality, prove that

<div class="math-display">
$$
\frac{(x+y)^2}{2}\le x^2+y^2
$$
</div>

<em>Solutions that do not use the Cauchy-Schwarz inequality will not receive credit.</em>

<details markdown="1"><summary>Solution</summary>

Recall, the Cauchy-Schwarz inequality states that for any two vectors <span class="math-inline">\\(\vec u, \vec v \in \mathbb{R}^n\\)</span>,

<div class="math-display">
$$
|\vec u \cdot \vec v| \leq \|\vec u\| \|\vec v\|
$$
</div>

Applying Cauchy-Schwarz to the vectors <span class="math-inline">\\(\vec u=\begin{bmatrix}x\\\\y\end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec v=\begin{bmatrix}1\\\\1\end{bmatrix}\\)</span> gives

<div class="math-display">
$$
|x + y| \leq \sqrt{x^2 + y^2} \sqrt{1^2 + 1^2} = \sqrt{2(x^2 + y^2)}
$$
</div>

 Squaring both sides gives

<div class="math-display">
$$
(x + y)^2 \leq 2(x^2 + y^2)
$$
</div>

 and finally, dividing both sides by <span class="math-inline">\\(2\\)</span> gives

<div class="math-display">
$$
\frac{(x+y)^2}{2}\le x^2+y^2
$$
</div>

 as needed.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> Now suppose <span class="math-inline">\\(x\\)</span>, <span class="math-inline">\\(y\\)</span>, and <span class="math-inline">\\(z\\)</span> are non-negative numbers. Which inequality is guaranteed to be true?

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \frac{(x+y+z)^2}{2}\le x^2+y^2+z^2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \frac{(x+y+z)^2}{3}\le x^2+y^2+z^2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \frac{(x+y+z)^2}{2}\le x^3+y^3+z^3\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \frac{(x+y+z)^3}{3}\le x^3+y^3+z^3\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> None of the above</span></div>

<details markdown="1"><summary>Solution</summary>

<span class="mc-bubble" aria-hidden="true"></span> None of the above

The Cauchy-Schwarz inequality directly implies one of the options, and the other options are all not guaranteed to be true. Extending our argument from part **a)**, let's now apply Cauchy-Schwarz to the vectors <span class="math-inline">\\(\vec u=\begin{bmatrix}x\\\\y\\\\z\end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec v=\begin{bmatrix}1\\\\1\\\\1\end{bmatrix}\\)</span>. This gives

<div class="math-display">
$$
|x+y+z|\le \sqrt{x^2+y^2+z^2} \sqrt{1^2+1^2+1^2} = \sqrt{3(x^2+y^2+z^2)}
$$
</div>

 Squaring both sides and dividing by <span class="math-inline">\\(3\\)</span> gives

<div class="math-display">
$$
\frac{(x+y+z)^2}{3}\le x^2+y^2+z^2
$$
</div>

 which is the second option.
</details>
</div>
</div>

</div>
