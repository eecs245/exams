---
number: 1
title: Getting Started
heading_suffix: : Getting Started <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>
points: 12
flags: []
has_solution: true
images: []
---

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> Let <span class="math-inline">\\(A = \begin{bmatrix} 2 &amp; 4 \\\\ -3 &amp; -7 \end{bmatrix}\\)</span>. Find <span class="math-inline">\\(\text{det}(A)\\)</span>, the determinant of <span class="math-inline">\\(A\\)</span>. Give your answer as an integer.

<span class="math-inline">\\(\text{det}(A) = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>

<details markdown="1"><summary>Solution</summary>

The determinant of a <span class="math-inline">\\(2 \times 2\\)</span> matrix <span class="math-inline">\\(\begin{bmatrix} a &amp; b \\\\ c &amp; d \end{bmatrix}\\)</span> is <span class="math-inline">\\(ad - bc\\)</span>. So,

<div class="math-display">
$$
\text{det}(A) = (2)(-7) - (4)(-3) = -14 + 12 = \boxed{-2}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> Using <span class="math-inline">\\(A\\)</span> from part **a)**, find <span class="math-inline">\\(A^{-1}\\)</span>, the inverse of <span class="math-inline">\\(A\\)</span>. Fully simplify your answer, i.e. don't leave any constants out front.

<span class="math-inline">\\(A^{-1} = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>

<details markdown="1"><summary>Solution</summary>

The inverse of a <span class="math-inline">\\(2 \times 2\\)</span> matrix <span class="math-inline">\\(\begin{bmatrix} a &amp; b \\\\ c &amp; d \end{bmatrix}\\)</span> is <span class="math-inline">\\(\frac{1}{ad - bc} \begin{bmatrix} d &amp; -b \\\\ -c &amp; a \end{bmatrix}\\)</span>. So,

<div class="math-display">
$$
A^{-1} = \frac{1}{(-2)} \begin{bmatrix} -7 & -4 \\\\ 3 & 2 \end{bmatrix} = \boxed{\begin{bmatrix} 7/2 & 2 \\\\ -3/2 & -1 \end{bmatrix}}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">2 pts</span> Let <span class="math-inline">\\(B = \begin{bmatrix} -1 &amp; 2 &amp; -1 \\\\ 3 &amp; 3 &amp; 2 \\\\ 0 &amp; 0 &amp; 1 \end{bmatrix}\\)</span>. What is the **first column** of <span class="math-inline">\\(B^{-1}\\)</span>, the inverse of <span class="math-inline">\\(B\\)</span>?

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} -1 \\\\ 0 \\\\ 0 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} -1 \\\\ 1/2 \\\\ -1 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} -1 \\\\1/3 \\\\ 1 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} -1/3 \\\\ 1/3 \\\\ 0 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} 1/3 \\\\ -1/3 \\\\ 0 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(B\\)</span> is not invertible</span></div>

<details markdown="1"><summary>Solution</summary>

<span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(B\\)</span> is not invertible

<span class="math-inline">\\(\boxed{\begin{bmatrix} -1/3 \\\\ 1/3 \\\\ 0\end{bmatrix}}\\)</span>.

Remember, <span class="math-inline">\\(B^{-1}\\)</span> is the matrix that satisfies <span class="math-inline">\\(B B^{-1} = I\\)</span>. Inverting <span class="math-inline">\\(B\\)</span> is not necessary: instead, all one needs to look for is the vector <span class="math-inline">\\(\vec v\\)</span> such that <span class="math-inline">\\(B \vec v = \begin{bmatrix} 1 \\\\ 0 \\\\ 0 \end{bmatrix}\\)</span>, since <span class="math-inline">\\(B\\)</span> multiplied by <span class="math-inline">\\(B^{-1}\\)</span>'s first column should give the first column of <span class="math-inline">\\(I\\)</span>.

And indeed, <span class="math-inline">\\(B \begin{bmatrix} -1/3 \\\\ 1/3 \\\\ 0 \end{bmatrix} = \begin{bmatrix} 1 \\\\ 0 \\\\ 0 \end{bmatrix}\\)</span>. So, you could have solved this just by guessing and checking each of the options.

If we asked this as an open-ended question instead, we'd be searching for the vector <span class="math-inline">\\(\begin{bmatrix} x \\\\ y \\\\ z \end{bmatrix}\\)</span> such that

<div class="math-display">
$$
\begin{bmatrix} -1 & 2 & -1 \\\\ 3 & 3 & 2 \\\\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} x \\\\ y \\\\ z \end{bmatrix} = \begin{bmatrix} 1 \\\\ 0 \\\\ 0 \end{bmatrix}
$$
</div>

From here, there are two ways to solve for <span class="math-inline">\\(\begin{bmatrix} x \\\\ y \\\\ z \end{bmatrix}\\)</span>.

-   You could solve the system of equations directly.

-   Or, you could notice that <span class="math-inline">\\(\begin{bmatrix} x \\\\ y \\\\ z \end{bmatrix}\\)</span> must be orthogonal to both the second row and third row of <span class="math-inline">\\(B\\)</span>, which means that its in the same direction as the cross product of the second and third rows. If you compute the cross product of the last two rows, you get

<div class="math-display">
$$
\begin{bmatrix} 3(1) - 2(0) \\\\ 2(0) - 3(1) \\\\ 3(0) - 3(0) \end{bmatrix} = \begin{bmatrix} 3 \\\\ -3 \\\\ 0 \end{bmatrix}
$$
</div>

 which means that <span class="math-inline">\\(\begin{bmatrix} x \\\\ y \\\\ z \end{bmatrix} = c \begin{bmatrix} 3 \\\\ -3 \\\\ 0 \end{bmatrix}\\)</span> for some constant <span class="math-inline">\\(c\\)</span>. To find <span class="math-inline">\\(c\\)</span>, solve for the <span class="math-inline">\\(c\\)</span> such that the dot product of <span class="math-inline">\\(c \begin{bmatrix} 3 \\\\ -3 \\\\ 0 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\begin{bmatrix} -1 \\\\ 2 \\\\ -1 \end{bmatrix}\\)</span> (the first row of <span class="math-inline">\\(B\\)</span>) is 1. This gives <span class="math-inline">\\(c = -1/9\\)</span>, which means that <span class="math-inline">\\(\begin{bmatrix} x \\\\ y \\\\ z \end{bmatrix} = -1/9 \begin{bmatrix} 3 \\\\ -3 \\\\ 0 \end{bmatrix} = \begin{bmatrix} -1/3 \\\\ 1/3 \\\\ 0 \end{bmatrix}\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> This part is independent of the previous parts (i.e. don't use the specific <span class="math-inline">\\(A\\)</span> or <span class="math-inline">\\(B\\)</span> from above).

**Select all** true statements below.

<span class="mc-square" aria-hidden="true"></span> If <span class="math-inline">\\(A\\)</span> and <span class="math-inline">\\(B\\)</span> are both matrices such that <span class="math-inline">\\(AB = I\\)</span>, then <span class="math-inline">\\(A\\)</span> and <span class="math-inline">\\(B\\)</span> are both invertible.

<span class="mc-square" aria-hidden="true"></span> If <span class="math-inline">\\(A\\)</span> and <span class="math-inline">\\(B\\)</span> are both invertible matrices, then <span class="math-inline">\\((A^TB)^{-1} = \left( (B^{-1})^T A^{-1} \right)^T\\)</span>.

<span class="mc-square" aria-hidden="true"></span> If <span class="math-inline">\\(A\\)</span> is an invertible matrix, then <span class="math-inline">\\(\text{rank}(A) = \text{rank}(A^{-1})\\)</span>.

<span class="mc-square" aria-hidden="true"></span> If <span class="math-inline">\\(A\\)</span>, <span class="math-inline">\\(B\\)</span>, and <span class="math-inline">\\(C\\)</span> are all symmetric matrices, then <span class="math-inline">\\(AB + C\\)</span> is also symmetric.

<details markdown="1"><summary>Solution</summary>

<span class="mc-square" aria-hidden="true"></span> If <span class="math-inline">\\(A\\)</span>, <span class="math-inline">\\(B\\)</span>, and <span class="math-inline">\\(C\\)</span> are all symmetric matrices, then <span class="math-inline">\\(AB + C\\)</span> is also symmetric.

Only Option 3 is true. Let's look at each statement one by one.

**(i)** **If <span class="math-inline">\\(A\\)</span> and <span class="math-inline">\\(B\\)</span> are both matrices such that <span class="math-inline">\\(AB = I\\)</span>, then <span class="math-inline">\\(A\\)</span> and <span class="math-inline">\\(B\\)</span> are both invertible.** This is <span class="math-inline">\\(\boxed{\text{False}}\\)</span>, because it's possible for <span class="math-inline">\\(AB = I\\)</span> to be true for two non-square matrices <span class="math-inline">\\(A\\)</span> and <span class="math-inline">\\(B\\)</span>, meaning they can't be invertible. For example, suppose <span class="math-inline">\\(B = \begin{bmatrix} 1 &amp; 0 \\\\ 0 &amp; 1 \\\\ 0 &amp; 0\end{bmatrix}\\)</span> and <span class="math-inline">\\(A = B^T = \begin{bmatrix} 1 &amp; 0 &amp; 0 \\\\ 0 &amp; 1 &amp; 0 \end{bmatrix}\\)</span>. Then,

<div class="math-display">
$$
AB = B^TB = \begin{bmatrix} 1 & 0 & 0 \\\\ 0 & 1 & 0 \end{bmatrix} \begin{bmatrix} 1 & 0 \\\\ 0 & 1 \\\\ 0 & 0 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\\\ 0 & 1  \end{bmatrix} = I
$$
</div>

**(ii)** **If <span class="math-inline">\\(A\\)</span> and <span class="math-inline">\\(B\\)</span> are both invertible matrices, then <span class="math-inline">\\((A^TB)^{-1} = \left( (B^{-1})^T A^{-1} \right)^T\\)</span>.** This is <span class="math-inline">\\(\boxed{\text{False}}\\)</span>:

-   If we expand the right-hand side, we get

<div class="math-display">
$$
((B^{-1})^T A^{-1})^T = \underbrace{(A^{-1})^T ((B^{-1})^T)^T}_{\text{reverse order of product when taking transpose}} = (A^{-1})^T (B^{-1})
$$
</div>

-   This is not the same as <span class="math-inline">\\((A^TB)^{-1}\\)</span>, which is <span class="math-inline">\\((A^TB)^{-1} = B^{-1}(A^T)^{-1}\\)</span>. Note that <span class="math-inline">\\((A^{-1})^T = (A^T)^{-1}\\)</span>, but the reason these two expressions aren't the same is because order matters for matrix multiplication --- it's not commutative.

**(iii)** **If <span class="math-inline">\\(A\\)</span> is an invertible matrix, then <span class="math-inline">\\(\text{rank}(A) = \text{rank}(A^{-1})\\)</span>.** This is <span class="math-inline">\\(\boxed{\text{True}}\\)</span>. If <span class="math-inline">\\(A\\)</span> is invertible, then <span class="math-inline">\\(\text{rank}(A) = n\\)</span>. Then, <span class="math-inline">\\(A^{-1}\\)</span> is also invertible (its inverse is <span class="math-inline">\\(A\\)</span>), so it must have a rank of <span class="math-inline">\\(n\\)</span> as well.

**(iv)** **If <span class="math-inline">\\(A\\)</span>, <span class="math-inline">\\(B\\)</span>, and <span class="math-inline">\\(C\\)</span> are all symmetric matrices, then <span class="math-inline">\\(AB + C\\)</span> is also symmetric.** This is <span class="math-inline">\\(\boxed{\text{False}}\\)</span>. Recall, what makes a matrix <span class="math-inline">\\(A\\)</span> symmetric is that <span class="math-inline">\\(A = A^T\\)</span>. Let's take the transpose of <span class="math-inline">\\(AB + C\\)</span> and see if we end up getting back <span class="math-inline">\\(AB + C\\)</span>:

<div class="math-display">
$$
(AB + C)^T = (AB)^T + C^T = B^TA^T + C^T = BA + C
$$
</div>

<span class="math-inline">\\(AB + C\\)</span> is only symmetric if <span class="math-inline">\\(AB + C = BA + C\\)</span>, i.e. if <span class="math-inline">\\(AB = BA\\)</span>, which is not true in general, even if <span class="math-inline">\\(A\\)</span> and <span class="math-inline">\\(B\\)</span> are both symmetric.
</details>

</div>
</div>

</div>
