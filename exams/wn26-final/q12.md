---
number: 12
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>
points: 12
flags: []
has_solution: true
images: []
---

Suppose <span class="math-inline">\\(\tilde X\\)</span> is an <span class="math-inline">\\(n \times 2\\)</span> matrix whose columns are mean-centered (i.e. have a mean of 0). Furthermore, suppose

<div class="math-display">
$$
\tilde X^T \tilde X = \begin{bmatrix} 3 & 2 \\\\ 2 & 6 \end{bmatrix}
$$
</div>

 Note that <span class="math-inline">\\(\tilde X^T \tilde X\\)</span> has eigenvalues of <span class="math-inline">\\(7\\)</span> and <span class="math-inline">\\(2\\)</span>. Let <span class="math-inline">\\(\tilde X = U \Sigma V^T\\)</span> be the singular value decomposition of <span class="math-inline">\\(\tilde X\\)</span>, and let <span class="math-inline">\\(\vec v&#95;1\\)</span> be the first column of <span class="math-inline">\\(V\\)</span> (not <span class="math-inline">\\(V^T\\)</span>).

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> What is <span class="math-inline">\\(\vec v&#95;1\\)</span>? Give your answer as a vector with no variables. If there are multiple correct answers, you only need to provide one.

<span class="math-inline">\\(\vec v&#95;1 = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>

<details markdown="1"><summary>Solution</summary>

The first right singular vector, <span class="math-inline">\\(\vec v&#95;1\\)</span>, is an eigenvector of <span class="math-inline">\\(\tilde X^T\tilde X\\)</span> corresponding to the largest eigenvalue, <span class="math-inline">\\(7\\)</span>. So we solve

<div class="math-display">
$$
\begin{bmatrix}
3 & 2\\\\
2 & 6
\end{bmatrix}
\begin{bmatrix}
a\\\\b
\end{bmatrix}
=
7
\begin{bmatrix}
a\\\\b
\end{bmatrix}
$$
</div>

 The first row gives

<div class="math-display">
$$
3a+2b=7a
\implies
b=2a
$$
</div>

 One unit vector in this direction is

<div class="math-display">
$$
\vec v_1 = \boxed{\frac{1}{\sqrt 5}\begin{bmatrix}1\\\\2\end{bmatrix}}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> Suppose the variance of the **second** principal component is <span class="math-inline">\\(1/15\\)</span>. What is <span class="math-inline">\\(n\\)</span>, the number of rows in <span class="math-inline">\\(\tilde X\\)</span>? Give your answer as a number with no variables.

<span class="math-inline">\\(n = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>

<details markdown="1"><summary>Solution</summary>

The variance of the second principal component is

<div class="math-display">
$$
\frac{\sigma_2^2}{n}
$$
</div>

 Since <span class="math-inline">\\(\sigma&#95;2^2\\)</span> is the second-largest eigenvalue of <span class="math-inline">\\(\tilde X^T\tilde X\\)</span>, we have <span class="math-inline">\\(\sigma&#95;2^2=2\\)</span>. So

<div class="math-display">
$$
\frac{2}{n}=\frac{1}{15}
$$
</div>

 This gives

<div class="math-display">
$$
n=\boxed{30}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">5 pts</span> Suppose that <span class="math-inline">\\(\vec u&#95;2\\)</span> is the second column of <span class="math-inline">\\(U\\)</span>, corresponding to the singular value <span class="math-inline">\\(\sigma&#95;2\\)</span>, in the singular value decomposition of <span class="math-inline">\\(\tilde X\\)</span>.

Prove that <span class="math-inline">\\(\tilde X \vec v&#95;1\\)</span> and <span class="math-inline">\\(\sigma&#95;2 \vec u&#95;2\\)</span> are orthogonal. You do not need to re-prove any facts about the singular value decomposition, but you should state any facts you use.

<details markdown="1"><summary>Solution</summary>

Using the SVD relationship,

<div class="math-display">
$$
\tilde X\vec v_1 = \sigma_1\vec u_1
$$
</div>

 So

<div class="math-display">
$$
(\tilde X\vec v_1)^T(\sigma_2\vec u_2)
=
(\sigma_1\vec u_1)^T(\sigma_2\vec u_2)
=
\sigma_1\sigma_2 \vec u_1^T\vec u_2
$$
</div>

 The columns of <span class="math-inline">\\(U\\)</span> are orthonormal, so <span class="math-inline">\\(\vec u&#95;1^T\vec u&#95;2=0\\)</span>. Therefore,

<div class="math-display">
$$
(\tilde X\vec v_1)^T(\sigma_2\vec u_2)=0
$$
</div>

 This proves that <span class="math-inline">\\(\tilde X\vec v&#95;1\\)</span> and <span class="math-inline">\\(\sigma&#95;2\vec u&#95;2\\)</span> are orthogonal.
</details>

</div>
</div>

</div>
