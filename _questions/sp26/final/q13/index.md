---
number: 13
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>
points: 12
flags: []
has_solution: true
images: []
---

Let <span class="math-inline">\\(\tilde X\\)</span> be a <span class="math-inline">\\(4 \times 2\\)</span> centered matrix (i.e. in which each column has a mean of 0) with columns <span class="math-inline">\\(\vec a\\)</span> and <span class="math-inline">\\(\vec b\\)</span>:

<div class="math-display">
$$
\tilde X = \begin{bmatrix} \mid & \mid \\\\ \vec a & \vec b \\\\ \mid & \mid \end{bmatrix}
$$
</div>

 Suppose <span class="math-inline">\\(\tilde X = U \Sigma V^T\\)</span> is the singular value decomposition of <span class="math-inline">\\(\tilde X\\)</span>, <span class="math-inline">\\(\vec v&#95;1 = \begin{bmatrix}3/5\\\\4/5\end{bmatrix}\\)</span> is the first column of <span class="math-inline">\\(V\\)</span>, and <span class="math-inline">\\(\sigma&#95;1 = 10\\)</span> is the largest singular value.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> How many possible vectors are there for <span class="math-inline">\\(\vec v&#95;2\\)</span>, the second column of <span class="math-inline">\\(V\\)</span>?

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 1</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 2</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 3</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 4</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> infinitely many <span class="math-inline">\\(\vec v&#95;2\\)</span>'s are possible</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 1</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> 2</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 3</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 4</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> infinitely many <span class="math-inline">\\(\vec v&#95;2\\)</span>'s are possible</span></div>

Since <span class="math-inline">\\(V\\)</span> is an orthogonal matrix, its columns must be unit vectors that are orthogonal to each other. In <span class="math-inline">\\(\mathbb{R}^2\\)</span>, there are exactly two unit vectors orthogonal to <span class="math-inline">\\(\begin{bmatrix}3/5\\\\4/5\end{bmatrix}\\)</span>, namely <span class="math-inline">\\(\begin{bmatrix}-4/5\\\\3/5\end{bmatrix}\\)</span> and <span class="math-inline">\\(\begin{bmatrix}4/5\\\\-3/5\end{bmatrix}\\)</span>. So there are two possible vectors for <span class="math-inline">\\(\vec{v}&#95;2\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">5 pts</span> Write <span class="math-inline">\\(\vec u&#95;1\\)</span>, the first column of <span class="math-inline">\\(U\\)</span>, as a linear combination of the columns of <span class="math-inline">\\(\tilde X\\)</span>. Show your work, and fill in each box with a number with no variables.

<details markdown="1"><summary>Solution</summary>

Recall that the key relationship linking the first column of <span class="math-inline">\\(U\\)</span> and the first column of <span class="math-inline">\\(V\\)</span> in <span class="math-inline">\\(\tilde X = U \Sigma V^T\\)</span> is

<div class="math-display">
$$
\tilde{X}\vec{v}_1=\sigma_1\vec{u}_1
$$
</div>

 This means

<div class="math-display">
$$
\vec{u}_1=\frac{1}{\sigma_1}\tilde{X}\vec{v}_1
$$
</div>

 Since the columns of <span class="math-inline">\\(\tilde{X}\\)</span> are <span class="math-inline">\\(\vec{a}\\)</span> and <span class="math-inline">\\(\vec{b}\\)</span>,

<div class="math-display">
$$
\tilde{X}\vec{v}_1
=
\tilde{X}\begin{bmatrix}3/5\\\\4/5\end{bmatrix}
=
\frac{3}{5}\vec{a}+\frac{4}{5}\vec{b}
$$
</div>

 and since <span class="math-inline">\\(\sigma&#95;1=10\\)</span>,

<div class="math-display">
$$
\vec{u}_1
=
\frac{1}{10}\left(\frac{3}{5}\vec{a}+\frac{4}{5}\vec{b}\right)
=
\frac{3}{50}\vec{a}+\frac{2}{25}\vec{b}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Given the information above, what is the maximum possible variance of principal component <span class="math-inline">\\(2\\)</span>? Give your answer as a number with no variables.

maximum possible variance of principal component <span class="math-inline">\\(2\\)</span> = \_\_\_\_\_\_

<details markdown="1"><summary>Solution</summary>

[Chapter 10.4](https://notes.eecs245.org/singular-value-decomposition/principal-components-analysis/) tells us that the variance of principal component <span class="math-inline">\\(j\\)</span> is

<div class="math-display">
$$
\frac{\sigma_j^2}{n}
$$
</div>

We also know that the singular values are sorted from largest to smallest, so <span class="math-inline">\\(\sigma&#95;1 \geq \sigma&#95;2\\)</span>. So, the variance of principal component <span class="math-inline">\\(2\\)</span>, <span class="math-inline">\\(\frac{\sigma&#95;2^2}{n}\\)</span>, is **at most** equal to the variance of principal component <span class="math-inline">\\(1\\)</span>, <span class="math-inline">\\(\frac{\sigma&#95;1^2}{n}\\)</span>.

Therefore, the maximum possible variance of principal component <span class="math-inline">\\(2\\)</span> is the variance of principal component <span class="math-inline">\\(1\\)</span>:

<div class="math-display">
$$
\frac{\sigma_1^2}{n}=\frac{10^2}{4}=25
$$
</div>

</details>

</div>
</div>

</div>
