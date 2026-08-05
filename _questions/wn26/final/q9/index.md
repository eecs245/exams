---
number: 9
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>
points: 12
flags: []
has_solution: true
images: []
---

Consider the matrix <span class="math-inline">\\(A = \begin{bmatrix} 2 &amp; 3 \\\\ -4 &amp; k \end{bmatrix}\\)</span> where <span class="math-inline">\\(k \in \mathbb{R}\\)</span> is some unknown constant.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> Suppose <span class="math-inline">\\(\lambda&#95;1 = 0\\)</span> is an eigenvalue of <span class="math-inline">\\(A\\)</span>. Find the value of <span class="math-inline">\\(k\\)</span>. Give your answer as a number with no variables.

<span class="math-inline">\\(k = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>

<details markdown="1"><summary>Solution</summary>

If <span class="math-inline">\\(0\\)</span> is an eigenvalue, then <span class="math-inline">\\(\det(A)=0\\)</span>. So

<div class="math-display">
$$
\det(A)=2k-3(-4)=2k+12=0
$$
</div>

 This gives

<div class="math-display">
$$
k=\boxed{-6}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Suppose <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ 1 \end{bmatrix}\\)</span> is an eigenvector of <span class="math-inline">\\(A\\)</span>. Find the value of <span class="math-inline">\\(k\\)</span>. Give your answer as a number with no variables.

<div class="math-display">
$$
k = \_\_\_\_\_\_
$$
</div>

<details markdown="1"><summary>Solution</summary>

If <span class="math-inline">\\(\begin{bmatrix}1\\\\1\end{bmatrix}\\)</span> is an eigenvector, then

<div class="math-display">
$$
A\begin{bmatrix}1\\\\1\end{bmatrix}
=
\begin{bmatrix}5\\\\k-4\end{bmatrix}
$$
</div>

 must be a scalar multiple of <span class="math-inline">\\(\begin{bmatrix}1\\\\1\end{bmatrix}\\)</span>. Therefore,

<div class="math-display">
$$
k-4=5
$$
</div>

 so

<div class="math-display">
$$
k=\boxed{9}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">5 pts</span> Suppose <span class="math-inline">\\(\lambda&#95;1 = 3\\)</span> is an eigenvalue of <span class="math-inline">\\(A\\)</span>. Find <span class="math-inline">\\(\lambda&#95;2\\)</span>, the **other eigenvalue** of <span class="math-inline">\\(A\\)</span>. Show your work, and write your final answer in the box provided. Give your answer as a number with no variables.

<div class="math-display">
$$
\lambda_2 = \_\_\_\_\_\_
$$
</div>

<details markdown="1"><summary>Solution</summary>

If <span class="math-inline">\\(3\\)</span> is an eigenvalue, then

<div class="math-display">
$$
\det(A-3I)=0
$$
</div>

 So

<div class="math-display">
$$
\det\left(
\begin{bmatrix}
-1 & 3\\\\
-4 & k-3
\end{bmatrix}
\right)
=
-(k-3)+12
=
15-k
=0
$$
</div>

 This gives <span class="math-inline">\\(k=15\\)</span>. The trace of <span class="math-inline">\\(A\\)</span> is then <span class="math-inline">\\(2+15=17\\)</span>, so the two eigenvalues sum to <span class="math-inline">\\(17\\)</span>. Thus,

<div class="math-display">
$$
\lambda_2 = 17-3 = \boxed{14}
$$
</div>

</details>

</div>
</div>

</div>
