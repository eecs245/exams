---
number: 2
title: Space Jam
heading_suffix: : Space Jam <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">20 pts</span>
points: 20
flags: []
has_solution: true
images: []
---

Let <span class="math-inline">\\(X = \begin{bmatrix} 1 &amp; -4 &amp; 2 &amp; 2 &amp; 0 \\\\ 0 &amp; 0 &amp; -3 &amp; 3 &amp; 0 \\\\ 1 &amp; -4 &amp; 4 &amp; 0 &amp; 0 \\\\ 0 &amp; 0 &amp; 0 &amp; 0 &amp; 1 \end{bmatrix}\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
(4.5 pts) Determine the values of each of the following. Give your answers as integers.

<div class="math-display">
$$
\begin{array}{lllll}
\text{dim}(\text{colsp}(X)) = &\_\_\_\_\_\_ \qquad \qquad  & \text{dim}(\text{nullsp}(X)) = &\_\_\_\_\_\_ \\\\ \\\\
\text{dim}(\text{colsp}(X^T)) = &\_\_\_\_\_\_ \qquad \qquad  & \text{dim}(\text{nullsp}(X^T)) = &\_\_\_\_\_\_ \\\\
\end{array}
$$
</div>

<details markdown="1"><summary>Solution</summary>

Recall, the rank-nullity theorem states that for any matrix <span class="math-inline">\\(X\\)</span>,

<div class="math-display">
$$
\text{rank}(X) + \text{dim}(\text{nullsp}(X)) = \text{number of columns of } X
$$
</div>

where <span class="math-inline">\\(\text{rank}(X) = \text{dim}(\text{colsp}(X)) = \text{dim}(\text{colsp}(X^T))\\)</span>.

<span class="math-inline">\\(X\\)</span> has **3** linearly independent columns: columns 1, 4, and 5. These three columns can be used to create the other two columns:

-   Column 2 = <span class="math-inline">\\(\begin{bmatrix} -4 \\\\ 0 \\\\ -4 \\\\ 0 \end{bmatrix} = -4 \begin{bmatrix} 1 \\\\ 0 \\\\ 1 \\\\ 0 \end{bmatrix} = (-4) \cdot \text{column 1}\\)</span>

-   Column 3 = <span class="math-inline">\\(\begin{bmatrix} 2 \\\\ -3 \\\\ 4 \\\\ 0 \end{bmatrix} = 4 \begin{bmatrix} 1 \\\\ 0 \\\\ 1 \\\\ 0 \end{bmatrix} - \begin{bmatrix} 2 \\\\ 3\\\\ 0 \\\\ 0 \end{bmatrix} = 4 \cdot \text{column 1} - \text{column 4}\\)</span>

So, <span class="math-inline">\\(\text{rank}(X) = 3\\)</span>, meaning <span class="math-inline">\\(\text{dim}(\text{colsp}(X)) = \boxed{3}\\)</span> and <span class="math-inline">\\(\text{dim}(\text{colsp}(X^T)) = \boxed{3}\\)</span> also.

Since <span class="math-inline">\\(\text{rank}(X) + \text{dim}(\text{nullsp}(X)) = \text{number of columns of } X\\)</span>, we have <span class="math-inline">\\(\text{dim}(\text{nullsp}(X)) = 5 - 3 = \boxed{2}\\)</span>.

And finally, since <span class="math-inline">\\(\text{rank}(X^T) + \text{dim}(\text{nullsp}(X^T)) = \text{number of columns of } X^T\\)</span>, we have <span class="math-inline">\\(\text{dim}(\text{nullsp}(X^T)) = 5 - 4 = \boxed{1}\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(3.5 pts) Suppose <span class="math-inline">\\(\vec y \in \mathbb{R}^4\\)</span>. How many solutions <span class="math-inline">\\(\vec v \in \mathbb{R}^5\\)</span> are there to the system of equations <span class="math-inline">\\(X \vec v = \vec y\\)</span>? **Select all** possibilities, since the answer may depend on <span class="math-inline">\\(\vec y\\)</span>.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 0</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 1</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 2</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 3</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 4</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 5</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> Infinitely many</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-square mc-correct" aria-hidden="true"></span> 0</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 1</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 2</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 3</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 4</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> 5</span><span class="mc-option"><span class="mc-square mc-correct" aria-hidden="true"></span> Infinitely many</span></div>

When solving <span class="math-inline">\\(X \vec v = \vec y\\)</span> for <span class="math-inline">\\(\vec v\\)</span>, there are two possible cases.

-   <span class="math-inline">\\(\vec y \notin \text{colsp}(X)\\)</span>: This is possible because <span class="math-inline">\\(\text{dim}(\text{colsp}(X))=3\\)</span>, so the columns don't span all of <span class="math-inline">\\(\mathbb{R}^4\\)</span>. In this case, <span class="math-inline">\\(\vec v\\)</span> has no solutions.

-   <span class="math-inline">\\(\vec y \in \text{colsp}(X)\\)</span>: The columns of <span class="math-inline">\\(X\\)</span> aren't linearly independent, so there are infinitely many ways to write <span class="math-inline">\\(\vec y\\)</span> as a linear combination of the columns of <span class="math-inline">\\(X\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> For some <span class="math-inline">\\(\vec y \in \mathbb{R}^4\\)</span>, the vector <span class="math-inline">\\(\vec w' = \begin{bmatrix} 8 \\\\ 0 \\\\ 0 \\\\ 3 \\\\ 11 \end{bmatrix}\\)</span> is such that <span class="math-inline">\\(X \vec w'\\)</span> is the vector in <span class="math-inline">\\(\text{colsp}(X)\\)</span> that is closest to <span class="math-inline">\\(\vec y\\)</span>. State **one other** vector <span class="math-inline">\\(\vec \beta\\)</span> such that <span class="math-inline">\\(X \vec \beta = X \vec w'\\)</span>. Show your work, and <span class="math-inline">\\(\boxed{\text{circle}}\\)</span> your final answer, which should be a vector with five entries and no variables.

<details markdown="1"><summary>Solution</summary>

There's two ways to approach this problem. The first is adding a vector in <span class="math-inline">\\(\text{nullsp}(X)\\)</span> to <span class="math-inline">\\(\vec w'\\)</span>. Why does this work? Let <span class="math-inline">\\(\vec \beta = \vec w' + \vec n\\)</span>, where <span class="math-inline">\\(X\vec n = \vec 0\\)</span>:

<div class="math-display">
$$
\begin{align*}
X\vec \beta &= X(\vec w' + \vec n)
\\\\&=X(\vec w' + \vec n)
\\\\&=X\vec w' + X\vec n
\\\\&=X\vec w' = \vec y
\end{align*}
$$
</div>

So, all we have to do is find a vector in the null space of

<div class="math-display">
$$
X = \begin{bmatrix} 1 & -4 & 2 & 2 & 0 \\\\ 0 & 0 & -3 & 3 & 0 \\\\ 1 & -4 & 4 & 0 & 0 \\\\ 0 & 0 & 0 & 0 & 1 \end{bmatrix}
$$
</div>

One such vector is <span class="math-inline">\\(\vec n = \begin{bmatrix} 0 \\\\ 1 \\\\ 1 \\\\ 1 \\\\ 0 \end{bmatrix}\\)</span>, since <span class="math-inline">\\(X\vec n = \begin{bmatrix} -4 \\\\ 0 \\\\ -4 \\\\ 0 \end{bmatrix} + \begin{bmatrix} 2 \\\\ -3 \\\\ 4 \\\\ 0 \end{bmatrix} + \begin{bmatrix} 2 \\\\ 3 \\\\ 0 \\\\ 0 \end{bmatrix} = \vec 0\\)</span>

This leaves us with <span class="math-inline">\\(\vec \beta=\vec w' + \vec n = \begin{bmatrix} 8 \\\\ 0 \\\\ 0 \\\\ 3 \\\\ 11 \end{bmatrix} + \begin{bmatrix} 0 \\\\ 1 \\\\ 1 \\\\ 1 \\\\ 0 \end{bmatrix} = \boxed{\begin{bmatrix} 8 \\\\ 1 \\\\ 1 \\\\ 4 \\\\ 11 \end{bmatrix}}\\)</span>.

The other way is to "tweak" <span class="math-inline">\\(\vec w'\\)</span> using the relationships we know about in the columns of <span class="math-inline">\\(X\\)</span>. Since <span class="math-inline">\\(\text{column 2} = -4 \cdot \text{column 1}\\)</span>, and <span class="math-inline">\\(\vec w' = \begin{bmatrix} 8 \\\\ 0 \\\\ 0 \\\\ 3 \\\\ 11 \end{bmatrix}\\)</span>, an easy swap is to change <span class="math-inline">\\(w&#95;0\\)</span> from <span class="math-inline">\\(8\\)</span> to <span class="math-inline">\\(0\\)</span> and <span class="math-inline">\\(w&#95;1\\)</span> from 0 to <span class="math-inline">\\(-2\\)</span>:

<div class="math-display">
$$
8 \cdot \begin{bmatrix} 1 \\\\ 0 \\\\ 1 \\\\ 0 \end{bmatrix} = -2 \cdot \begin{bmatrix} -4 \\\\ 0 \\\\ -4 \\\\ 0 \end{bmatrix}
$$
</div>

Doing this gives <span class="math-inline">\\(\vec \beta = \boxed{\begin{bmatrix} 0 \\\\ -2 \\\\ 0 \\\\ 3 \\\\ 11 \end{bmatrix}}\\)</span>.
</details>

Recall, <span class="math-inline">\\(X = \begin{bmatrix} 1 &amp; -4 &amp; 2 &amp; 2 &amp; 0 \\\\ 0 &amp; 0 &amp; -3 &amp; 3 &amp; 0 \\\\ 1 &amp; -4 &amp; 4 &amp; 0 &amp; 0 \\\\ 0 &amp; 0 &amp; 0 &amp; 0 &amp; 1 \end{bmatrix}\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Find a basis for <span class="math-inline">\\(\text{nullsp}(X^T)\\)</span> (**not** <span class="math-inline">\\(\text{nullsp}(X)\\)</span>). Show your work, and <span class="math-inline">\\(\boxed{\text{circle}}\\)</span> your final answer, which should be a list of vectors.

<details markdown="1"><summary>Solution</summary>

<div class="math-display">
$$
X^T=
\begin{bmatrix}
1 & 0 & 1 & 0 \\\\
-4 & 0 & -4 & 0 \\\\
2 & -3 & 4 & 0 \\\\
2 & 3 & 0 & 0 \\\\
0 & 0 & 0 & 1
\end{bmatrix}
$$
</div>

 From the rank-nullity theorem, we know that our basis will have exactly one vector, so our goal is to find a non-zero vector where <span class="math-inline">\\(X^T \vec n = \vec 0\\)</span>.

<span class="math-inline">\\(\text{Column 3}=\text{Column 1} - \frac{2}{3}\cdot \text{Column 2}\\)</span>, so one possible basis is <span class="math-inline">\\(\left\lbrace \begin{bmatrix} 1 \\\\ -\frac{2}{3} \\\\ -1 \\\\ 0\end{bmatrix}\right\rbrace\\)</span>.
</details>

</div>
</div>

</div>
