---
number: 5
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">11 pts</span> <span class="badge" data-flag="mt2-redemption" style="background-color: #9A3324; color: #FFFFFF; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">MT2 Redemption</span>
points: 11
flags: [mt2-redemption]
has_solution: true
images: []
---

Suppose <span class="math-inline">\\(A\\)</span> is a <span class="math-inline">\\(6 \times 5\\)</span> matrix such that

<div class="math-display">
$$
\text{nullsp}(A)
=
\text{span}\left(
\left\{
\begin{bmatrix}1\\\\0\\\\1\\\\0\\\\0\end{bmatrix},
\begin{bmatrix}0\\\\1\\\\1\\\\0\\\\0\end{bmatrix},
\begin{bmatrix}0\\\\0\\\\0\\\\1\\\\1\end{bmatrix}
\right\}
\right)
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Find <span class="math-inline">\\(\text{rank}(A)\\)</span> and <span class="math-inline">\\(\dim(\text{nullsp}(A^T))\\)</span>. Give your answers as integers with no variables.

<span class="math-inline">\\(\text{rank}(A) = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;  \dim(\text{nullsp}(A^T)) = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>

<details markdown="1"><summary>Solution</summary>

Recall, the rank-nullity theorem states that for any matrix <span class="math-inline">\\(A\\)</span>,

<div class="math-display">
$$
\text{rank}(A) + \dim(\text{nullsp}(A)) = \text{number of columns of } A
$$
</div>

The null space has dimension <span class="math-inline">\\(3\\)</span>, since the given basis has <span class="math-inline">\\(3\\)</span> vectors. Because <span class="math-inline">\\(A\\)</span> has <span class="math-inline">\\(5\\)</span> columns, rank-nullity gives

<div class="math-display">
$$
\text{rank}(A) + 3 = 5
\implies \text{rank}(A) = \boxed{2}
$$
</div>

 Also, <span class="math-inline">\\(A^T\\)</span> has <span class="math-inline">\\(6\\)</span> columns and <span class="math-inline">\\(\text{rank}(A^T)=\text{rank}(A)=2\\)</span>, so rank-nullity gives

<div class="math-display">
$$
\dim(\text{nullsp}(A^T)) = 6-2 = \boxed{4}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> Which of the following **could NOT** be the first row of <span class="math-inline">\\(A\\)</span>?

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} 2 &amp; 2 &amp; -2 &amp; 3 &amp; -3 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} 1 &amp; 1 &amp; -1 &amp; 4 &amp; -4 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} 2 &amp; 0 &amp; -2 &amp; 5 &amp; -5 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} 3 &amp; 3 &amp; -3 &amp; -2 &amp; 2 \end{bmatrix}\\)</span></span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} 2 &amp; 2 &amp; -2 &amp; 3 &amp; -3 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} 1 &amp; 1 &amp; -1 &amp; 4 &amp; -4 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} 2 &amp; 0 &amp; -2 &amp; 5 &amp; -5 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} 3 &amp; 3 &amp; -3 &amp; -2 &amp; 2 \end{bmatrix}\\)</span></span></div>

A key fact is that the row space and null space of a matrix are orthogonal complements, as discussed in [Chapter 5.4](https://notes.eecs245.org/matrices/null-space-rank-nullity/#example-orthogonal-complements) (and the linked video). What this means is that every row of <span class="math-inline">\\(A\\)</span> is orthogonal to every vector in <span class="math-inline">\\(\text{nullsp}(A)\\)</span>.

So a row

<div class="math-display">
$$
\begin{bmatrix} a & b & c & d & e \end{bmatrix}
$$
</div>

 must satisfy

<div class="math-display">
$$
a+c = 0,
\qquad
b+c = 0,
\qquad
d+e = 0
$$
</div>

Equivalently, every row of <span class="math-inline">\\(A\\)</span> must have the form

<div class="math-display">
$$
\begin{bmatrix} a & a & -a & d & -d \end{bmatrix}
$$
</div>

The first, second, and fourth options all have this form. The third option,

<div class="math-display">
$$
\begin{bmatrix} 2 & 0 & -2 & 5 & -5 \end{bmatrix}
$$
</div>

 does not. For instance, it is not orthogonal to

<div class="math-display">
$$
\begin{bmatrix}0\\\\1\\\\1\\\\0\\\\0\end{bmatrix}
\in \text{nullsp}(A)
$$
</div>

 since

<div class="math-display">
$$
\begin{bmatrix} 2 & 0 & -2 & 5 & -5 \end{bmatrix}
\begin{bmatrix}0\\\\1\\\\1\\\\0\\\\0\end{bmatrix}
= -2 \neq 0
$$
</div>

So the correct answer is the **third** option, <span class="math-inline">\\(\boxed{\begin{bmatrix} 2 &amp; 0 &amp; -2 &amp; 5 &amp; -5 \end{bmatrix}}\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Let <span class="math-inline">\\(\vec a^{(1)}, \vec a^{(2)}, \vec a^{(3)}, \vec a^{(4)}, \vec a^{(5)} \in \mathbb{R}^6\\)</span> be the columns of <span class="math-inline">\\(A\\)</span>.

Below, select **one possible set** of columns of <span class="math-inline">\\(A\\)</span> that form a basis for <span class="math-inline">\\(\text{colsp}(A)\\)</span>. You should select the fewest possible number of columns needed to span <span class="math-inline">\\(\text{colsp}(A)\\)</span>.

<div class="math-display">
$$
\begin{array}{c|c}
\text{Column} & \text{Include in your basis?} \\\\ \hline
\vec a^{(1)} & \square  \quad  \\\\
\vec a^{(2)} & \square  \quad  \\\\
\vec a^{(3)} & \square  \quad  \\\\
\vec a^{(4)} & \square  \quad  \\\\
\vec a^{(5)} & \square  \quad
\end{array}
$$
</div>

<details markdown="1"><summary>Solution</summary>

<span class="mc-square" aria-hidden="true"></span>

The vector

<div class="math-display">
$$
\begin{bmatrix}1\\\\0\\\\1\\\\0\\\\0\end{bmatrix}
\in \text{nullsp}(A)
$$
</div>

 tells us

<div class="math-display">
$$
\vec a^{(1)}+\vec a^{(3)}=\vec 0 \implies \vec a^{(3)} = -\vec a^{(1)}
$$
</div>

 and the vector

<div class="math-display">
$$
\begin{bmatrix}0\\\\1\\\\1\\\\0\\\\0\end{bmatrix}
\in \text{nullsp}(A)
$$
</div>

 tells us

<div class="math-display">
$$
\vec a^{(2)}+\vec a^{(3)}=\vec 0 \implies \vec a^{(3)} = -\vec a^{(2)}
$$
</div>

 So <span class="math-inline">\\(\vec a^{(1)}\\)</span>, <span class="math-inline">\\(\vec a^{(2)}\\)</span>, and <span class="math-inline">\\(\vec a^{(3)}\\)</span> all lie on the same line and are scalar multiples of each other. Similarly,

<div class="math-display">
$$
\begin{bmatrix}0\\\\0\\\\0\\\\1\\\\1\end{bmatrix}
\in \text{nullsp}(A)
$$
</div>

 tells us

<div class="math-display">
$$
\vec a^{(4)}+\vec a^{(5)}=\vec 0 \implies \vec a^{(5)} = -\vec a^{(4)}
$$
</div>

 Since <span class="math-inline">\\(\text{rank}(A)=2\\)</span>, the column space is 2-dimensional. A basis for the column space comes from picking one of <span class="math-inline">\\(\lbrace \vec a^{(1)}, \vec a^{(2)}, \vec a^{(3)} \rbrace\\)</span> and one of <span class="math-inline">\\(\lbrace \vec a^{(4)}, \vec a^{(5)} \rbrace\\)</span>. There are therefore 6 possible options; one of them is

<div class="math-display">
$$
\boxed{\{\vec a^{(1)}, \vec a^{(4)}\}}
$$
</div>

</details>

</div>
</div>

</div>
