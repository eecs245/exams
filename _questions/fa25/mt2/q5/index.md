---
number: 5
title: Ortho\...dontist?
heading_suffix: : Ortho\...dontist? <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>
points: 12
flags: []
has_solution: true
images: []
---

Let <span class="math-inline">\\(A = \begin{bmatrix} 1 &amp; 0 \\\\ 1 &amp; 4 \\\\ 1 &amp; 4 \\\\ 1 &amp; 4 \end{bmatrix}\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Find a matrix <span class="math-inline">\\(Q\\)</span> such that <span class="math-inline">\\(\text{colsp}(Q) = \text{colsp}(A)\\)</span> and <span class="math-inline">\\(Q^TQ = I\\)</span>. Show your work and <span class="math-inline">\\(\boxed{\text{circle}}\\)</span> your final answer, which should be a matrix with two columns and no variables. <em>Hint: One of the columns may involve square roots.</em>

<details markdown="1"><summary>Solution</summary>

Since we want <span class="math-inline">\\(Q^TQ = I\\)</span>, we're looking for a matrix <span class="math-inline">\\(Q\\)</span> with two columns that are orthogonal to each other and are both unit vectors.

The "standard" way to answer this part is to use the Gram-Schmidt process, first introduced in Homework 7, Problem 4. But, since <span class="math-inline">\\(A\\)</span> only has two columns, it's okay if you forgot about the specifics, and instead realized the core of Gram-Schmidt, which takes advantage of the fact that **the error when projecting <span class="math-inline">\\(\vec u\\)</span> onto <span class="math-inline">\\(\vec v\\)</span> is orthogonal to <span class="math-inline">\\(\vec v\\)</span>**.

Let

<div class="math-display">
$$
\vec v = \begin{bmatrix} 1 \\\\ 1 \\\\ 1 \\\\ 1 \end{bmatrix}
\qquad
\vec u = \begin{bmatrix} 0 \\\\ 4 \\\\ 4 \\\\ 4 \end{bmatrix}
$$
</div>

Then the projection of <span class="math-inline">\\(\vec u\\)</span> onto <span class="math-inline">\\(\vec v\\)</span> is

<div class="math-display">
$$
\vec p = \frac{\vec u \cdot \vec v}{\vec v \cdot \vec v}\vec v
= \frac{0\cdot 1 + 4\cdot 1 + 4\cdot 1 + 4\cdot 1}{1^2+1^2+1^2+1^2}
\begin{bmatrix} 1 \\\\ 1 \\\\ 1 \\\\ 1 \end{bmatrix}
= \frac{12}{4}
\begin{bmatrix} 1 \\\\ 1 \\\\ 1 \\\\ 1 \end{bmatrix}
= 3
\begin{bmatrix} 1 \\\\ 1 \\\\ 1 \\\\ 1 \end{bmatrix}
$$
</div>

So the error vector is

<div class="math-display">
$$
\vec e = \vec u - \vec p
=
\begin{bmatrix} 0 \\\\ 4 \\\\ 4 \\\\ 4 \end{bmatrix}
-
\begin{bmatrix} 3 \\\\ 3 \\\\ 3 \\\\ 3 \end{bmatrix}
=
\begin{bmatrix} -3 \\\\ 1 \\\\ 1 \\\\ 1 \end{bmatrix}
$$
</div>

This vector <span class="math-inline">\\(\vec e\\)</span> is orthogonal to <span class="math-inline">\\(\vec v\\)</span>, and together <span class="math-inline">\\(\vec v\\)</span> and <span class="math-inline">\\(\vec e\\)</span> have the same span as <span class="math-inline">\\(\text{colsp}(A)\\)</span>. To make the columns orthonormal, we normalize both vectors:

<div class="math-display">
$$
\|\vec v\| = \sqrt{1^2+1^2+1^2+1^2} = 2
\qquad
\|\vec e\| = \sqrt{(-3)^2+1^2+1^2+1^2} = \sqrt{12}
$$
</div>

Therefore, one valid matrix <span class="math-inline">\\(Q\\)</span> is

<div class="math-display">
$$
\boxed{
Q=
\begin{bmatrix}
1/2 & -3/\sqrt{12} \\\\
1/2 & 1/\sqrt{12} \\\\
1/2 & 1/\sqrt{12} \\\\
1/2 & 1/\sqrt{12}
\end{bmatrix}
}
$$
</div>

Another common solution is to observe that the vectors

<div class="math-display">
$$
\begin{bmatrix} 1 \\\\ 0 \\\\ 0 \\\\ 0 \end{bmatrix}
\qquad \text{and} \qquad
\begin{bmatrix} 0 \\\\ 1 \\\\ 1 \\\\ 1 \end{bmatrix}
$$
</div>

 are orthogonal to each other and span <span class="math-inline">\\(\text{colsp}(A)\\)</span>. Normalizing these two vectors gives another valid answer:

<div class="math-display">
$$
\boxed{
\begin{bmatrix}
1 & 0 \\\\
0 & 1/\sqrt{3} \\\\
0 & 1/\sqrt{3} \\\\
0 & 1/\sqrt{3}
\end{bmatrix}
}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">2 pts</span> True or False: The matrix <span class="math-inline">\\(Q\\)</span> you found above is an orthogonal matrix.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> False</span></div>

No matter how you find <span class="math-inline">\\(Q\\)</span> in part **a)**, the answer is false, because <span class="math-inline">\\(Q\\)</span> is not a square matrix, so it cannot be orthogonal!

For <span class="math-inline">\\(Q\\)</span> to be orthogonal, we'd need **both** <span class="math-inline">\\(Q^TQ = I\\)</span> **and** <span class="math-inline">\\(QQ^T = I\\)</span>. Since <span class="math-inline">\\(Q\\)</span> is not square, these can't both be true at the same time (the dimensions don't match, since the former would be <span class="math-inline">\\(2 \times 2\\)</span> while the latter would be <span class="math-inline">\\(4 \times 4\\)</span>).
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Let <span class="math-inline">\\(R = \begin{bmatrix} r&#95;1 &amp; \boxed{r&#95;2} \\\\ \boxed{r&#95;3} &amp; r&#95;4 \end{bmatrix}\\)</span> be a <span class="math-inline">\\(2 \times 2\\)</span> matrix such that <span class="math-inline">\\(A = QR\\)</span>, where <span class="math-inline">\\(Q\\)</span> is the matrix you found above.

Find <span class="math-inline">\\(r&#95;2\\)</span> and <span class="math-inline">\\(r&#95;3\\)</span>. Give your answers as scalars without variables.

<span class="math-inline">\\(r&#95;2 = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;, \qquad r&#95;3 = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>

<details markdown="1"><summary>Solution</summary>

**We ended up giving full credit to everyone for this problem, since there's no unique answer, and it's difficult to answer this correctly if you found an invalid <span class="math-inline">\\(Q\\)</span>.**

The main idea being assessed here, taken from Homework 7, Problem 4, is that if <span class="math-inline">\\(Q\\)</span> is a matrix such that <span class="math-inline">\\(\text{colsp}(Q) = \text{colsp}(A)\\)</span> and <span class="math-inline">\\(Q^T Q = I\\)</span>, then

<div class="math-display">
$$
A = QR \implies Q^TA = Q^TQR \implies R = Q^TA
$$
</div>

As we saw in that homework problem, **if you use Gram-Schmidt to find <span class="math-inline">\\(Q\\)</span>**, <span class="math-inline">\\(R\\)</span> is an **upper triangular** matrix, meaning that <span class="math-inline">\\(r&#95;3 = 0\\)</span>. (We won't elaborate on this here: read the solutions to Homework 7, Problem 4.)

For two different <span class="math-inline">\\(Q\\)</span>'s, we'll find the corresponding <span class="math-inline">\\(R\\)</span>'s to give you some sample possible answers.

-   For

<div class="math-display">
$$
Q =
        \begin{bmatrix}
        1/2 & -3/\sqrt{12} \\\\
        1/2 & 1/\sqrt{12} \\\\
        1/2 & 1/\sqrt{12} \\\\
        1/2 & 1/\sqrt{12}
        \end{bmatrix}
$$
</div>

 **which did result from Gram-Schmidt**,

<div class="math-display">
$$
R = Q^TA
        =
        \begin{bmatrix}
        2 & 6 \\\\
        0 & 12/\sqrt{12}
        \end{bmatrix}
        =
        \begin{bmatrix}
        2 & 6 \\\\
        0 & \sqrt{12}
        \end{bmatrix}
$$
</div>

 This <span class="math-inline">\\(R\\)</span> **is** upper triangular.

-   For

<div class="math-display">
$$
Q =
        \begin{bmatrix}
        1 & 0 \\\\
        0 & 1/\sqrt{3} \\\\
        0 & 1/\sqrt{3} \\\\
        0 & 1/\sqrt{3}
        \end{bmatrix}
$$
</div>

 **which did not result from Gram-Schmidt**,

<div class="math-display">
$$
R = Q^TA
        =
        \begin{bmatrix}
        1 & 0 \\\\
        \sqrt{3} & 4\sqrt{3}
        \end{bmatrix}
$$
</div>

 This <span class="math-inline">\\(R\\)</span> **is not** upper triangular.
</details>

</div>
</div>

</div>
