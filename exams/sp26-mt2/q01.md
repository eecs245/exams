---
number: 1
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>
points: 12
flags: []
has_solution: true
images: []
---

Suppose <span class="math-inline">\\(k\\)</span> is a real number. Let

<div class="math-display">
$$
A =
\begin{bmatrix}
1 & k+1 \\\\
1 & 2k+3
\end{bmatrix}
$$
</div>

In each part, you are provided with information about <span class="math-inline">\\(A\\)</span>. **Your job is to find the value of <span class="math-inline">\\(k\\)</span> that satisfies the given condition.** Show your work in the space provided, and write your final answer in the bottom-right corner of the box. Your answers should be numbers with no variables.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span>
<span class="math-inline">\\(\det(A) = 14\\)</span>.

<div class="math-display">
$$
k = \_\_\_\_\_\_
$$
</div>

<details markdown="1"><summary>Solution</summary>

Since <span class="math-inline">\\(A\\)</span> is a <span class="math-inline">\\(2 \times 2\\)</span> matrix, its determinant is

<div class="math-display">
$$
\begin{align*}
\det(A) &= 1(2k+3) - 1(k+1) \\\\
&= k + 2
\end{align*}
$$
</div>

We're told that <span class="math-inline">\\(\det(A) = 14\\)</span>, so

<div class="math-display">
$$
\begin{align*}
k + 2 &= 14 \\\\
k &= 12
\end{align*}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span>
<span class="math-inline">\\(A\\)</span> is not invertible.

<div class="math-display">
$$
k = \_\_\_\_\_\_
$$
</div>

<details markdown="1"><summary>Solution</summary>

If <span class="math-inline">\\(A\\)</span> is not invertible, then <span class="math-inline">\\(\det(A) = 0\\)</span>. From part **a)**,

<div class="math-display">
$$
\det(A) = k + 2
$$
</div>

 so

<div class="math-display">
$$
\begin{align*}
k + 2 &= 0 \\\\
k &= -2
\end{align*}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> The bottom-right entry of <span class="math-inline">\\(A^{-1}\\)</span> is <span class="math-inline">\\(1/4\\)</span>.

<div class="math-display">
$$
k = \_\_\_\_\_\_
$$
</div>

<details markdown="1"><summary>Solution</summary>

The inverse of a <span class="math-inline">\\(2 \times 2\\)</span> matrix is

<div class="math-display">
$$
\begin{bmatrix}
a & b \\\\
c & d
\end{bmatrix}^{-1}
=
\frac{1}{ad-bc}
\begin{bmatrix}
d & -b \\\\
-c & a
\end{bmatrix}
$$
</div>

 Here, <span class="math-inline">\\(\det(A)=k+2\\)</span>, so

<div class="math-display">
$$
A^{-1}
=
\frac{1}{k+2}
\begin{bmatrix}
2k+3 & -(k+1) \\\\
-1 & 1
\end{bmatrix}
$$
</div>

 The bottom-right entry is <span class="math-inline">\\(\frac{1}{k+2}\\)</span>, and we're told that this equals <span class="math-inline">\\(\frac{1}{4}\\)</span>. So,

<div class="math-display">
$$
\begin{align*}
\frac{1}{k+2} &= \frac{1}{4} \\\\
k+2 &= 4 \\\\
k &= 2
\end{align*}
$$
</div>

</details>

</div>
</div>

</div>
