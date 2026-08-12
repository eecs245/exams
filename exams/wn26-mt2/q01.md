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
A = \begin{bmatrix} 3 & 2 \\\\ k & 4 \end{bmatrix}
$$
</div>

In each part, you are provided with information about <span class="math-inline">\\(A\\)</span>. **Your job is to find the value of <span class="math-inline">\\(k\\)</span> that satisfies the given condition.** Show your work in the space provided, and write your final answer in the bottom-right corner of the box. Your answers should be numbers with no variables.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span>
<span class="math-inline">\\(\text{rank}(A) = 1\\)</span>

<div class="math-display">
$$
k = \_\_\_\_\_\_
$$
</div>

<details markdown="1"><summary>Solution</summary>

If <span class="math-inline">\\(\text{rank}(A) = 1\\)</span>, then <span class="math-inline">\\(A\\)</span> is not invertible, which means <span class="math-inline">\\(\text{det}(A) = 0\\)</span>. So,

<div class="math-display">
$$
\begin{align*}
\det(A) &= (3)(4) - (2)(k) = 12 - 2k = 0 \\\\
2k &= 12 \\\\
k &= 6
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
<span class="math-inline">\\(\text{det}(A) = 2\\)</span>

<div class="math-display">
$$
k = \_\_\_\_\_\_
$$
</div>

<details markdown="1"><summary>Solution</summary>

The determinant of a <span class="math-inline">\\(2 \times 2\\)</span> matrix <span class="math-inline">\\(\begin{bmatrix} a &amp; b \\\\ c &amp; d \end{bmatrix}\\)</span> is <span class="math-inline">\\(ad - bc\\)</span>. So,

<div class="math-display">
$$
\begin{align*}
\det(A) &= (3)(4) - (2)(k) = 12 - 2k
\end{align*}
$$
</div>

We're told that <span class="math-inline">\\(\det(A) = 2\\)</span>, so

<div class="math-display">
$$
\begin{align*}
12 - 2k &= 2 \\\\
2k &= 10 \\\\
k &= 5
\end{align*}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span>
<span class="math-inline">\\(A^{-1} = \begin{bmatrix} 1 &amp; -1/2 \\\\ -1 &amp; 3/4 \end{bmatrix}\\)</span>

<div class="math-display">
$$
k = \_\_\_\_\_\_
$$
</div>

<details markdown="1"><summary>Solution</summary>

The inverse of a <span class="math-inline">\\(2 \times 2\\)</span> matrix <span class="math-inline">\\(\begin{bmatrix} a &amp; b \\\\ c &amp; d \end{bmatrix}\\)</span> is <span class="math-inline">\\(\frac{1}{ad - bc} \begin{bmatrix} d &amp; -b \\\\ -c &amp; a \end{bmatrix}\\)</span>. So,

<div class="math-display">
$$
\begin{align*}
A^{-1} &= \frac{1}{12 - 2k} \begin{bmatrix} 4 & -2 \\\\ -k & 3 \end{bmatrix}
\end{align*}
$$
</div>

Since we're told that

<div class="math-display">
$$
A^{-1} = \begin{bmatrix} 1 & -1/2 \\\\ -1 & 3/4 \end{bmatrix},
$$
</div>

 we can match entries. For example, using the bottom-right entry,

<div class="math-display">
$$
\begin{align*}
\frac{3}{12 - 2k} &= \frac{3}{4} \\\\
12 - 2k &= 4 \\\\
2k &= 8 \\\\
k &= 4
\end{align*}
$$
</div>

</details>

</div>
</div>

</div>
