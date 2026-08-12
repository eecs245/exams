---
number: 5
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span> <span class="badge" data-flag="mt2-redemption" style="background-color: #9A3324; color: #FFFFFF; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">MT2 Redemption</span>
points: 12
flags: [mt2-redemption]
has_solution: true
images: []
---

Consider the <span class="math-inline">\\(n \times 5\\)</span> matrix <span class="math-inline">\\(A\\)</span>, along with a CR decomposition of it, given below.

<div class="math-display">
$$
A =
\begin{bmatrix}
2 & 2 & 2 & 2 & 2 \\\\
3 & 4 & 5 & 6 & 7 \\\\
4 & 6 & 8 & 10 & 12 \\\\
5 & 8 & 11 & 14 & 17 \\\\
6 & 10 & 14 & 18 & 22 \\\\
\vdots & \vdots & \vdots & \vdots & \vdots \\\\
n+1 & 2n & 3n - 1 & 4n - 2 & 5n - 3 \\\\
\end{bmatrix} = \underbrace{\begin{bmatrix} 2 & ? \\\\ 3 & ? \\\\ 4 & ? \\\\ 5 & ? \\\\ 6 & ? \\\\ \vdots & \vdots \\\\ n + 1 & ? \end{bmatrix}}_{C} \underbrace{\begin{bmatrix} 1 & \boxed{a} & 0 & c & -1 \\\\ 0 & \boxed{b} & 1 & d & 2\end{bmatrix}}_{R}
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">2 pts</span> Find <span class="math-inline">\\(\text{rank}(A)\\)</span>. Give your answer as an integer with no variables.

<span class="math-inline">\\(\text{rank}(A) = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>

<details markdown="1"><summary>Solution</summary>

The CR decomposition writes <span class="math-inline">\\(A = CR\\)</span>, where <span class="math-inline">\\(C\\)</span> contains linearly independent columns of <span class="math-inline">\\(A\\)</span>. Since <span class="math-inline">\\(C\\)</span> has 2 columns, <span class="math-inline">\\(A\\)</span> has 2 linearly independent columns, so

<div class="math-display">
$$
\text{rank}(A) = \boxed{2}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Find <span class="math-inline">\\(a\\)</span> and <span class="math-inline">\\(b\\)</span>. Give your answers as numbers with no variables.

<span class="math-inline">\\(a = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;, \qquad b = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>

<details markdown="1"><summary>Solution</summary>

Because columns 1 and 3 of <span class="math-inline">\\(R\\)</span> are the basis of <span class="math-inline">\\(\text{colsp}(A)\\)</span> that we're using to construct all 5 columns of <span class="math-inline">\\(A\\)</span>, column 2 of <span class="math-inline">\\(A\\)</span> must be

<div class="math-display">
$$
\text{col}_2(A) = a\,\text{col}_1(A) + b\,\text{col}_3(A)
$$
</div>

The "quick" way to spot what <span class="math-inline">\\(a\\)</span> and <span class="math-inline">\\(b\\)</span> must be is that column 2 is the average of columns 1 and 3: 2 is the average of 2 and 2, 4 is the average of 3 and 5, 6 is the average of 4 and 8, and so on. This alone tells you that <span class="math-inline">\\(a = b = \frac{1}{2}\\)</span>.

Another way to find <span class="math-inline">\\(a\\)</span> and <span class="math-inline">\\(b\\)</span> more systematically is to set up a system of equations. We have two unknowns --- <span class="math-inline">\\(a\\)</span> and <span class="math-inline">\\(b\\)</span> --- so we must need two equations, which we can get from looking at the first two rows of <span class="math-inline">\\(A\\)</span>.

<div class="math-display">
$$
\begin{align*}
2 &= 2a + 2b \\\\
4 &= 3a + 5b
\end{align*}
$$
</div>

The first equation says <span class="math-inline">\\(a+b=1\\)</span>, so <span class="math-inline">\\(a=1-b\\)</span>. Substitute into the second:

<div class="math-display">
$$
4 = 3(1-b) + 5b = 3 + 2b \implies b = \frac{1}{2}
$$
</div>

 Then <span class="math-inline">\\(a = \frac{1}{2}\\)</span> as well. Therefore,

<div class="math-display">
$$
\boxed{a = \frac{1}{2}, \qquad b = \frac{1}{2}}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> State **one** vector in <span class="math-inline">\\(\text{nullsp}(A)\\)</span>. Give your answer as a vector with no variables. <em>Hint: It is possible to find a vector in <span class="math-inline">\\(\text{nullsp}(A)\\)</span> without using your answer from part <strong>b)</strong>. Try not to rely heavily on your answer from part <strong>b)</strong> in case it's incorrect.</em>

<span class="math-inline">\\(\text{One vector in } \text{nullsp}(A) \text{ is:   } \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>

<details markdown="1"><summary>Solution</summary>

To find a vector in <span class="math-inline">\\(\text{nullsp}(A)\\)</span>, we need to find a linear combination of <span class="math-inline">\\(A\\)</span>'s columns that equals <span class="math-inline">\\(\vec 0\\)</span>. One such linear combination can be found from rearranging the linear dependence relationship from the last part:

<div class="math-display">
$$
\begin{align*}
\text{col}_2(A) &= \frac{1}{2}\,\text{col}_1(A) + \frac{1}{2}\,\text{col}_3(A) \\\\
\vec 0 &= \frac{1}{2}\,\text{col}_1(A) - \text{col}_2(A) + \frac{1}{2}\,\text{col}_3(A)
\end{align*}
$$
</div>

The coefficients on columns 1 through 3 are <span class="math-inline">\\(\frac{1}{2}\\)</span>, <span class="math-inline">\\(-1\\)</span>, and <span class="math-inline">\\(\frac{1}{2}\\)</span>; this linear combination doesn't use columns 4 and 5. So, this tells us that <span class="math-inline">\\(\begin{bmatrix} 1/2 \\\\ -1 \\\\ 1/2 \\\\ 0 \\\\ 0 \end{bmatrix}\\)</span> is in <span class="math-inline">\\(\text{nullsp}(A)\\)</span>. If we'd like to get rid of the fraction, then we could also say <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ -2 \\\\ 1 \\\\ 0 \\\\ 0 \end{bmatrix}\\)</span> is in <span class="math-inline">\\(\text{nullsp}(A)\\)</span> too.

There are plenty of other answers. For instance, the fact that

<div class="math-display">
$$
\text{col}_3(A) = \frac{1}{2}\,\text{col}_1(A) + \frac{1}{2}\,\text{col}_5(A)
$$
</div>

tells us that <span class="math-inline">\\(\begin{bmatrix} 1/2 \\\\ 0 \\\\ -1 \\\\ 0 \\\\ 1/2 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ 0 \\\\ -2 \\\\ 0 \\\\ 1 \end{bmatrix}\\)</span> are also in <span class="math-inline">\\(\text{nullsp}(A)\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> Fill in the blanks: <span class="math-inline">\\(\text{nullsp}(A^T)\\)</span> is a \_\_(i)\_\_-dimensional subspace of \_\_(ii)\_\_.

| <span class="math-inline">\\(i\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(2\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(3\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(4\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(5\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(n-2\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(n-1\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(n\\)</span> |
|:---|:---|:---|:---|:---|:---|:---|:---|
| <span class="math-inline">\\(ii\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\mathbb{R}^2\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\mathbb{R}^3\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\mathbb{R}^4\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\mathbb{R}^5\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\mathbb{R}^{n-2}\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\mathbb{R}^{n-1}\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\mathbb{R}^n\\)</span> |

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\mathbb{R}^2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\mathbb{R}^3\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\mathbb{R}^4\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\mathbb{R}^5\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\mathbb{R}^{n-2}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\mathbb{R}^{n-1}\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(\mathbb{R}^n\\)</span></span></div>

Since <span class="math-inline">\\(\text{rank}(A)=2\\)</span> and <span class="math-inline">\\(\text{rank}(A) = \text{rank}(A^T)\\)</span>, we also have <span class="math-inline">\\(\text{rank}(A^T)=2\\)</span>. The matrix <span class="math-inline">\\(A^T\\)</span> has <span class="math-inline">\\(n\\)</span> columns, so rank-nullity gives

<div class="math-display">
$$
\dim(\text{nullsp}(A^T)) = \text{\# columns in }A^T - \text{rank}(A^T) = n - 2
$$
</div>

 Also, <span class="math-inline">\\(\text{nullsp}(A^T)\\)</span> is a subspace of <span class="math-inline">\\(\mathbb{R}^n\\)</span>, because vectors in <span class="math-inline">\\(\text{nullsp}(A^T)\\)</span> must have one entry for each column of <span class="math-inline">\\(A^T\\)</span> (row of <span class="math-inline">\\(A\\)</span>).
</details>

</div>
</div>

</div>
