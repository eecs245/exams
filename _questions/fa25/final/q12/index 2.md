---
number: 12
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>
points: 12
flags: []
has_solution: true
images: []
---

Suppose <span class="math-inline">\\(\tilde X\\)</span> is a <span class="math-inline">\\(24 \times 3\\)</span> matrix whose columns are mean-centered (i.e. have a mean of 0). Let <span class="math-inline">\\(\tilde X = U \Sigma V^T\\)</span> be the singular value decomposition of <span class="math-inline">\\(\tilde X\\)</span>, where

<div class="math-display">
$$
\tilde X = U \underbrace{\begin{bmatrix} 12 & 0 & 0 \\\\ 0 & 2 & 0 \\\\ 0 & 0 & 0 \\\\\vdots & \vdots & \vdots \end{bmatrix}}_{\Sigma} \underbrace{\begin{bmatrix} 1/\sqrt{10} & 3/\sqrt{10} & 0 \\\\ \cdots & \vec v_2^T & \cdots \\\\ 0 & 0 & 1 \end{bmatrix}}_{V^T}
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">2 pts</span> Find <span class="math-inline">\\(\text{rank}(\tilde X)\\)</span>. Give your answer as an integer with no variables.

<span class="math-inline">\\(\text{rank}(\tilde X) = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>

<details markdown="1"><summary>Solution</summary>

The rank of a matrix is equal to its number of non-zero singular values. Here, the singular values are 12, 2, and 0, so 

<div class="math-display">
$$
\text{rank}(\tilde X) = \boxed{2}.
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> It is possible to find <span class="math-inline">\\(\vec v&#95;2^T\\)</span>, the second row of <span class="math-inline">\\(V^T\\)</span>, solely using the information provided (without knowing any of the values in <span class="math-inline">\\(\tilde X\\)</span>). In one English sentence, **explain how** to find it.

<details markdown="1"><summary>Solution</summary>

Since <span class="math-inline">\\(V\\)</span> is orthogonal, the rows of <span class="math-inline">\\(V^T\\)</span> must be orthonormal, so <span class="math-inline">\\(\vec v&#95;2^T\\)</span> is the unit vector orthogonal to both <span class="math-inline">\\(\begin{bmatrix} 1/\sqrt{10} \\\\ 3/\sqrt{10} \\\\ 0 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\begin{bmatrix} 0 \\\\ 0 \\\\ 1 \end{bmatrix}\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">2 pts</span> True or False: There exists some vector <span class="math-inline">\\(\vec z \in \mathbb{R}^{24}\\)</span> such that <span class="math-inline">\\(\tilde X \tilde X^T \vec z = 2 \vec z\\)</span>.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Impossible to tell</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> False</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Impossible to tell</span></div>

This is **False**. The eigenvalues of <span class="math-inline">\\(\tilde X \tilde X^T\\)</span> are the squares of the singular values of <span class="math-inline">\\(\tilde X\\)</span>, so they are <span class="math-inline">\\(144\\)</span>, <span class="math-inline">\\(4\\)</span>, and <span class="math-inline">\\(0\\)</span>. Since 2 is not an eigenvalue of <span class="math-inline">\\(\tilde X \tilde X^T\\)</span>, no such vector <span class="math-inline">\\(\vec z\\)</span> exists.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">5 pts</span> What is the largest possible variance of the components of <span class="math-inline">\\(\tilde X \vec w\\)</span>, where <span class="math-inline">\\(\vec w \in \mathbb{R}^3\\)</span> is a unit vector? Select one of the answers below, then justify your answer in the box provided.

1.  Answer:
<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(6\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(12\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(24\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(144\\)</span></span></div>

2.  Justify your answer in the box below.

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(2\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(6\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(12\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(24\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(144\\)</span></span></div>

Because the columns of <span class="math-inline">\\(\tilde X\\)</span> are mean-centered, the variance of the components of <span class="math-inline">\\(\tilde X\vec w\\)</span> is 

<div class="math-display">
$$
\frac{1}{n}\|\tilde X\vec w\|^2 = \frac{1}{24}\|\tilde X\vec w\|^2
$$
</div>

 This is maximized when <span class="math-inline">\\(\vec w\\)</span> is the first right singular vector (<span class="math-inline">\\(\vec v&#95;1\\)</span>), and the maximum value is 

<div class="math-display">
$$
\frac{\sigma_1^2}{24} = \frac{12^2}{24} = \frac{144}{24} = 6
$$
</div>

 So the largest possible variance is <span class="math-inline">\\(\boxed{6}\\)</span>.
</details>

</div>
</div>

</div>
