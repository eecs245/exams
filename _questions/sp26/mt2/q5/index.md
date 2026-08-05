---
number: 5
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">19 pts</span>
points: 19
flags: []
has_solution: true
images: []
---

Suppose we're given a dataset with <span class="math-inline">\\(n = 5\\)</span> rows, and we use it to fit a multiple linear regression model with two features and an intercept term.

<div class="math-display">
$$
h(\vec x_i) = w_0 + w_1 x_i^{(1)} + w_2 x_i^{(2)}
$$
</div>

 Let <span class="math-inline">\\(X\\)</span> be the corresponding <span class="math-inline">\\(5 \times 3\\)</span> design matrix and <span class="math-inline">\\(\vec y \in \mathbb{R}^5\\)</span> be the corresponding observation vector. Suppose the matrix <span class="math-inline">\\(P\\)</span> that projects onto the column space of <span class="math-inline">\\(X\\)</span> is

<div class="math-display">
$$
P = \begin{bmatrix} 1/4 & 1/4 & 1/4 & 1/4 & 0 \\\\ 1/4 & 1/4 & 1/4 & 1/4 & 0 \\\\ 1/4 & 1/4 & 1/4 & 1/4 & 0 \\\\ 1/4 & 1/4 & 1/4 & 1/4 & 0 \\\\ 0 & 0 & 0 & 0 & 1 \end{bmatrix}
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> **In parts a) and b) only**, suppose the projection of <span class="math-inline">\\(\vec y\\)</span> onto <span class="math-inline">\\(\text{colsp}(X)\\)</span> is <span class="math-inline">\\(\vec p = \begin{bmatrix} 3 \\\\ 3 \\\\ 3 \\\\ 3 \\\\ 3 \end{bmatrix}\\)</span>. There are infinitely many such vectors <span class="math-inline">\\(\vec y\\)</span>. State one possible vector <span class="math-inline">\\(\vec y\\)</span> **whose five components are all different**. Give your answer as a vector with no variables.

one possible vector <span class="math-inline">\\(\vec y =\\)</span> \_\_\_\_\_\_

<details markdown="1"><summary>Solution</summary>

For any vector <span class="math-inline">\\(\vec y\\)</span>, multiplying by <span class="math-inline">\\(P\\)</span> averages the first four components of <span class="math-inline">\\(\vec y\\)</span> and leaves the fifth component unchanged:

<div class="math-display">
$$
P\vec y =
\begin{bmatrix}
\displaystyle \frac{y_1+y_2+y_3+y_4}{4} \\\\ \\\\
\displaystyle \frac{y_1+y_2+y_3+y_4}{4} \\\\ \\\\
\displaystyle \frac{y_1+y_2+y_3+y_4}{4} \\\\ \\\\
\displaystyle \frac{y_1+y_2+y_3+y_4}{4} \\\\ \\\\
\displaystyle y_5
\end{bmatrix}
$$
</div>

 We want this to equal <span class="math-inline">\\(\begin{bmatrix} 3 \\\\ 3 \\\\ 3 \\\\ 3 \\\\ 3 \end{bmatrix}\\)</span>, so the first four components of <span class="math-inline">\\(\vec y\\)</span> need to have average 3, and the fifth component needs to be 3.

One possible choice is

<div class="math-display">
$$
\vec y =
\begin{bmatrix}
0 \\\\
1 \\\\
5 \\\\
6 \\\\
3
\end{bmatrix}
$$
</div>

 The first four components have average 3, and all five components are different. There are infinitely many possible answers, though.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> Let <span class="math-inline">\\(\vec y\\)</span> and <span class="math-inline">\\(\vec p \\)</span> be as defined in part (a). True or false: <span class="math-inline">\\(X^T (\vec p - \vec y) = \vec 0\\)</span>.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

This is true. If <span class="math-inline">\\(\vec p\\)</span> is the projection of <span class="math-inline">\\(\vec y\\)</span> onto <span class="math-inline">\\(\text{colsp}(X)\\)</span>, then the error vector <span class="math-inline">\\(\vec y - \vec p\\)</span> is orthogonal to every vector in <span class="math-inline">\\(\text{colsp}(X)\\)</span>. This is how we arrived at the normal equations, <span class="math-inline">\\(X^TX \vec w = X^T \vec y\\)</span>. Here, this means

<div class="math-display">
$$
X^T(\vec y - \vec p) = \vec 0
$$
</div>

 Multiplying by <span class="math-inline">\\(-1\\)</span> gives

<div class="math-display">
$$
X^T(\vec p - \vec y) = \vec 0
$$
</div>

</details>

For the rest of the problem, suppose that both <span class="math-inline">\\(\vec w^{\ast} = \begin{bmatrix} 2 \\\\ 3 \\\\ 1 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec w' = \begin{bmatrix} 3 \\\\ 1 \\\\ 0 \end{bmatrix}\\)</span> are both optimal parameter vectors that minimize mean squared error.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Which of these vectors are in <span class="math-inline">\\(\text{nullsp}(X)\\)</span>? **Select all** that apply.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} 2 \\\\ 3 \\\\ 1 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} 5 \\\\ 4 \\\\ 1 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ -2 \\\\ -1 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} 4 \\\\ 6 \\\\ 2 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} -2 \\\\ 4 \\\\ 2 \end{bmatrix}\\)</span></span></div>

<details markdown="1"><summary>Solution</summary>

<span class="mc-square mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} -2 \\\\ 4 \\\\ 2 \end{bmatrix}\\)</span>

If two parameter vectors are both solutions to the normal equation, their difference is in <span class="math-inline">\\(\text{nullsp}(X)\\)</span>. So,

<div class="math-display">
$$
\vec w' - \vec w^*
=
\begin{bmatrix} 3 \\\\ 1 \\\\ 0 \end{bmatrix}
-
\begin{bmatrix} 2 \\\\ 3 \\\\ 1 \end{bmatrix}
=
\begin{bmatrix} 1 \\\\ -2 \\\\ -1 \end{bmatrix}
\in \text{nullsp}(X)
$$
</div>

Where did this come from? The fact that <span class="math-inline">\\(\vec w'\\)</span> and <span class="math-inline">\\(\vec w^{\ast}\\)</span> are both optimal parameter vectors means that they both result in the same projection of <span class="math-inline">\\(\vec y\\)</span> onto <span class="math-inline">\\(\text{colsp}(X)\\)</span>, so

<div class="math-display">
$$
X \vec w^* = X \vec w'
$$
</div>

But, this means <span class="math-inline">\\(X(\vec w' - \vec w^{\ast}) = \vec 0\\)</span>, which says that <span class="math-inline">\\(\vec w' - \vec w^{\ast}\\)</span> is in <span class="math-inline">\\(\text{nullsp}(X)\\)</span>.

Also, <span class="math-inline">\\(P\\)</span> projects onto <span class="math-inline">\\(\text{colsp}(X)\\)</span>, and <span class="math-inline">\\(P\\)</span> has rank 2. Therefore <span class="math-inline">\\(\text{rank}(X)=2\\)</span> (the logic behind this is described [here](https://notes.eecs245.org/linear-transformations-and-projections/complete-solution/#example-is-p-invertible)). Since <span class="math-inline">\\(X\\)</span> has 3 columns, the rank-nullity theorem gives

<div class="math-display">
$$
\dim(\text{nullsp}(X)) = 3 - 2 = 1
$$
</div>

 So <span class="math-inline">\\(\text{nullsp}(X)\\)</span> is exactly

<div class="math-display">
$$
\text{nullsp}(X) =
\text{span}\left( \left\{ \begin{bmatrix} 1 \\\\ -2 \\\\ -1 \end{bmatrix} \right\} \right)
$$
</div>

 Among the listed choices, the vectors in this span are <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ -2 \\\\ -1 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\begin{bmatrix} -2 \\\\ 4 \\\\ 2 \end{bmatrix}\\)</span>.

The rank-nullity logic wasn't strictly necessary to answer the question; I've included it here for completeness, as it fully justifies why none of the other listed vectors are in <span class="math-inline">\\(\text{nullsp}(X)\\)</span>.
</details>

**The information stated below, above part **d)**, is the same as the information stated on the previous page. It's provided for your convenience.**

Recall, <span class="math-inline">\\(X\\)</span> is a <span class="math-inline">\\(5 \times 3\\)</span> design matrix for the model

<div class="math-display">
$$
h(\vec x_i) = w_0 + w_1 x_i^{(1)} + w_2 x_i^{(2)}
$$
</div>

 Additionally, <span class="math-inline">\\(\vec y \in \mathbb{R}^5\\)</span> is an observation vector, both <span class="math-inline">\\(\vec w^{\ast} = \begin{bmatrix} 2 \\\\ 3 \\\\ 1 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec w' = \begin{bmatrix} 3 \\\\ 1 \\\\ 0 \end{bmatrix}\\)</span> are both optimal parameter vectors that minimize mean squared error, and the matrix <span class="math-inline">\\(P\\)</span> that projects onto the column space of <span class="math-inline">\\(X\\)</span> is

<div class="math-display">
$$
P = \begin{bmatrix} 1/4 & 1/4 & 1/4 & 1/4 & 0 \\\\ 1/4 & 1/4 & 1/4 & 1/4 & 0 \\\\ 1/4 & 1/4 & 1/4 & 1/4 & 0 \\\\ 1/4 & 1/4 & 1/4 & 1/4 & 0 \\\\ 0 & 0 & 0 & 0 & 1 \end{bmatrix}
$$
</div>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">8 pts</span> Find one possible design matrix <span class="math-inline">\\(X\\)</span>, consistent with all of the information above. Show your work, and <span class="math-inline">\\(\boxed{\text{circle}}\\)</span> your final answer, which should be a matrix with no variables.

<details markdown="1"><summary>Solution</summary>

Since <span class="math-inline">\\(P\\)</span> projects onto <span class="math-inline">\\(\text{colsp}(X)\\)</span>, we need <span class="math-inline">\\(\text{colsp}(X) = \text{colsp}(P)\\)</span>. Notice that the result <span class="math-inline">\\(P \vec y\\)</span> for any vector <span class="math-inline">\\(\vec y \in \mathbb{R}^5\\)</span> will have equal first four components (resulting from averaging the original first four components of <span class="math-inline">\\(\vec y\\)</span>) and the fifth component will be unchanged. If we think of the space of possible values of <span class="math-inline">\\(P \vec y\\)</span>, we realize that any <span class="math-inline">\\(P \vec y\\)</span> is of the form

<div class="math-display">
$$
\begin{bmatrix} a \\\\ a \\\\ a \\\\ a \\\\ b \end{bmatrix} = a \begin{bmatrix} 1 \\\\ 1 \\\\ 1 \\\\ 1 \\\\ 0 \end{bmatrix} + b \begin{bmatrix} 0 \\\\ 0 \\\\ 0 \\\\ 0 \\\\ 1 \end{bmatrix}
$$
</div>

This means

<div class="math-display">
$$
\text{colsp}(X) = \text{span}\left( \left\{ \begin{bmatrix} 1 \\\\ 1 \\\\ 1 \\\\ 1 \\\\ 0 \end{bmatrix}, \begin{bmatrix} 0 \\\\ 0 \\\\ 0 \\\\ 0 \\\\ 1 \end{bmatrix} \right\} \right)
$$
</div>

Now, the problem boils down to finding a design matrix <span class="math-inline">\\(X\\)</span> with the above column space, that also meets the other requirements. Here are the other relevant requirements:

**(i)** Since the model has an intercept term, the first column of <span class="math-inline">\\(X\\)</span> should be <span class="math-inline">\\(\vec 1 = \begin{bmatrix} 1 \\\\ 1 \\\\ 1 \\\\ 1 \\\\ 1 \end{bmatrix}\\)</span>.

**(ii)** From part **c)**, we need <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ -2 \\\\ -1 \end{bmatrix} \in \text{nullsp}(X)\\)</span>.

If the columns of <span class="math-inline">\\(X\\)</span> are <span class="math-inline">\\(\vec x^{(0)}\\)</span>, <span class="math-inline">\\(\vec x^{(1)}\\)</span>, and <span class="math-inline">\\(\vec x^{(2)}\\)</span> (we're told <span class="math-inline">\\(X\\)</span> has 3 columns), the first requirement states

<div class="math-display">
$$
\vec x^{(0)} = \begin{bmatrix} 1 \\\\ 1 \\\\ 1 \\\\ 1 \\\\ 1 \end{bmatrix}
$$
</div>

The second requirement states

<div class="math-display">
$$
\underbrace{\begin{bmatrix} | & | & | \\\\ \vec x^{(0)} & \vec x^{(1)} & \vec x^{(2)} \\\\ | & | & | \end{bmatrix}}_{X} \begin{bmatrix} 1 \\\\ -2 \\\\ -1 \end{bmatrix} = \vec 0
$$
</div>

or, in other words, <span class="math-inline">\\(\vec x^{(0)} - 2\vec x^{(1)} - \vec x^{(2)} = \vec 0\\)</span>.

To guarantee <span class="math-inline">\\(\text{colsp}(X)\\)</span> is the span we set out before,

<div class="math-display">
$$
\text{colsp}(X) = \text{span} \left( \left\{ \begin{bmatrix} 1 \\\\ 1 \\\\ 1 \\\\ 1 \\\\ 1 \end{bmatrix}, \begin{bmatrix} 1 \\\\ 1 \\\\ 1 \\\\ 1 \\\\ 0 \end{bmatrix}\right\} \right)
$$
</div>

let's just pick <span class="math-inline">\\(\vec x^{(1)} = \begin{bmatrix} 1 \\\\ 1 \\\\ 1 \\\\ 1 \\\\ 0 \end{bmatrix}\\)</span>. Since <span class="math-inline">\\(\vec x^{(0)} - \vec x^{(1)} = \begin{bmatrix} 0 \\\\ 0 \\\\ 0 \\\\ 0 \\\\ 1 \end{bmatrix}\\)</span>, we have accomplished the goal of finding a design matrix <span class="math-inline">\\(X\\)</span> with the desired column space. With our choices of <span class="math-inline">\\(\vec x^{(0)}\\)</span> and <span class="math-inline">\\(\vec x^{(1)}\\)</span> out of the way, <span class="math-inline">\\(\vec x^{(2)}\\)</span> is fully determined for us:

<div class="math-display">
$$
\vec x^{(0)} - 2 \vec x^{(1)} - \vec x^{(2)} = \vec 0 \implies \vec x^{(2)} = \vec x^{(0)} - 2 \vec x^{(1)} = \begin{bmatrix} 1 \\\\ 1 \\\\ 1 \\\\ 1 \\\\ 1 \end{bmatrix} - 2 \begin{bmatrix} 1 \\\\ 1 \\\\ 1 \\\\ 1 \\\\ 0 \end{bmatrix} = \begin{bmatrix} -1 \\\\ -1 \\\\ -1 \\\\ -1 \\\\ 1 \end{bmatrix}
$$
</div>

Therefore, one possible design matrix is

<div class="math-display">
$$
X =
\begin{bmatrix}
1 & 1 & -1 \\\\
1 & 1 & -1 \\\\
1 & 1 & -1 \\\\
1 & 1 & -1 \\\\
1 & 0 & 1
\end{bmatrix}
$$
</div>

This design matrix has a column space of <span class="math-inline">\\(\text{span} \left( \left\lbrace \begin{bmatrix} 1 \\\\ 1 \\\\ 1 \\\\ 1 \\\\ 1 \end{bmatrix}, \begin{bmatrix} 1 \\\\ 1 \\\\ 1 \\\\ 1 \\\\ 0 \end{bmatrix}\right\rbrace \right)\\)</span>, which is the same as the column space of <span class="math-inline">\\(P\\)</span>. It also has the required null space, which is why it would be wrong to just pick, say,

<div class="math-display">
$$
\begin{bmatrix} 1 & 1 & 0 \\\\ 1 & 1 & 0 \\\\ 1 & 1 & 0 \\\\ 1 & 1 & 0 \\\\ 0 & 0 & 1 \end{bmatrix}
$$
</div>

--- the above matrix has a null space spanned by <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ -1 \\\\ -1 \end{bmatrix}\\)</span>, not <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ -2 \\\\ -1 \end{bmatrix}\\)</span>.
</details>

</div>
</div>

</div>
