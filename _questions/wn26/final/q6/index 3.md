---
number: 6
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span> <span class="badge" data-flag="mt2-redemption" style="background-color: #9A3324; color: #FFFFFF; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">MT2 Redemption</span>
points: 12
flags: [mt2-redemption]
has_solution: true
images: []
---

Suppose <span class="math-inline">\\(X\\)</span> is an <span class="math-inline">\\(n \times 3\\)</span> matrix, where <span class="math-inline">\\(n &gt; 2\\)</span>, with columns <span class="math-inline">\\(\vec x^{(1)}\\)</span>, <span class="math-inline">\\(\vec x^{(2)}\\)</span>, and <span class="math-inline">\\(\vec x^{(3)}\\)</span>. Furthermore, suppose that <span class="math-inline">\\(X = QR\\)</span>, where 

<div class="math-display">
$$
Q =
\begin{bmatrix}
\vert & \vert \\\\
\vec q^{(1)} & \vec q^{(2)} \\\\
\vert & \vert
\end{bmatrix}
$$
</div>

 is an <span class="math-inline">\\(n \times 2\\)</span> matrix with orthonormal columns, and 

<div class="math-display">
$$
R =
\begin{bmatrix}
2 & 0 & 2\\\\
0 & 1 & -1
\end{bmatrix}
$$
</div>

Lastly, suppose <span class="math-inline">\\(\vec y \in \mathbb{R}^n\\)</span> and <span class="math-inline">\\(Q^T \vec y = \begin{bmatrix} -2 \\\\ 10 \end{bmatrix}\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Let <span class="math-inline">\\(\vec p\\)</span> be the projection of <span class="math-inline">\\(\vec y\\)</span> onto <span class="math-inline">\\(\text{colsp}(X)\\)</span>. Write <span class="math-inline">\\(\vec p\\)</span> as a linear combination of the columns of <span class="math-inline">\\(X\\)</span>. Fill in each box with a number with no variables. If there are multiple correct answers, you only need to provide one.

<span class="math-inline">\\(\vec p = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;  \vec x^{(1)} + \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;  \vec x^{(2)} + \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;  \vec x^{(3)}\\)</span>

<details markdown="1"><summary>Solution</summary>

The columns of <span class="math-inline">\\(Q\\)</span> are a basis for <span class="math-inline">\\(\text{colsp}(X)\\)</span> (since <span class="math-inline">\\(X = QR\\)</span> writes every column of <span class="math-inline">\\(X\\)</span> as a linear combination of the columns of <span class="math-inline">\\(Q\\)</span>). So, the general strategy is to first write <span class="math-inline">\\(\vec p\\)</span> as a linear combination of the columns of <span class="math-inline">\\(Q\\)</span>, and then use the information in <span class="math-inline">\\(R\\)</span> to write that as a linear combination of the columns of <span class="math-inline">\\(X\\)</span>.

If <span class="math-inline">\\(X\\)</span> is a full rank matrix, then the projection of <span class="math-inline">\\(\vec y\\)</span> onto <span class="math-inline">\\(\text{colsp}(X)\\)</span> is

<div class="math-display">
$$
X (X^TX)^{-1}X^T \vec y
$$
</div>

<span class="math-inline">\\(X\\)</span> isn't full rank here, but <span class="math-inline">\\(Q\\)</span> is, and that is the matrix whose columns we're writing <span class="math-inline">\\(\vec p\\)</span> as a linear combination of to begin with. So, we have

<div class="math-display">
$$
\vec p = Q (Q^TQ)^{-1}Q^T \vec y
$$
</div>

But, since <span class="math-inline">\\(Q\\)</span>'s columns are orthonormal, <span class="math-inline">\\(Q^TQ = I\\)</span>, so

<div class="math-display">
$$
\vec p = Q (Q^TQ)^{-1} Q^T \vec y = Q I Q^T \vec y = Q Q^T \vec y = Q \begin{bmatrix} -2 \\\\ 10 \end{bmatrix} = -2 \vec q^{(1)}+10 \vec q^{(2)}
$$
</div>

Good, so now we have <span class="math-inline">\\(\vec p\\)</span> as a linear combination of the columns of <span class="math-inline">\\(Q\\)</span>. How do the columns of <span class="math-inline">\\(X\\)</span> relate to the columns of <span class="math-inline">\\(Q\\)</span>? <span class="math-inline">\\(R = \begin{bmatrix} 2 &amp; 0 &amp; 2\\\\0 &amp; 1 &amp; -1 \end{bmatrix}\\)</span> tells us that 

<div class="math-display">
$$
\vec x^{(1)} = 2\vec q^{(1)},
\qquad
\vec x^{(2)} = \vec q^{(2)},
\qquad
\vec x^{(3)} = 2\vec q^{(1)}-\vec q^{(2)}
$$
</div>

 So, one possible answer comes from 

<div class="math-display">
$$
\vec p = \boxed{-\vec x^{(1)}+10\vec x^{(2)}+0\vec x^{(3)}}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Let <span class="math-inline">\\(\vec w^{\ast}\\)</span> be a minimizer of

<div class="math-display">
$$
R_\text{sq}(w) = \frac{1}{n}\lVert \vec y - X \vec w \rVert^2
$$
</div>

 Fill in the blanks to describe the set of all possible values of <span class="math-inline">\\(\vec w^{\ast}\\)</span>. Each blank should contain a vector with no variables.

<span class="math-inline">\\(\text{set of all possible } \vec w^{\ast} = \left\lbrace \&#95;\&#95;\&#95;\&#95;\&#95;\&#95; + t  \&#95;\&#95;\&#95;\&#95;\&#95;\&#95; : t \in \mathbb{R} \right\rbrace\\)</span>.

<details markdown="1"><summary>Solution</summary>

From the previous part, we know one possible minimizer is

<div class="math-display">
$$
\vec w^* = \begin{bmatrix}-1\\\\10\\\\0\end{bmatrix}
$$
</div>

As discussed in [Chapter 6.4](https://notes.eecs245.org/linear-transformations-and-projections/complete-solution/#finding-all-solutions), the full sete of minimizers results from taking one particular solution and adding any vector in <span class="math-inline">\\(\text{nullsp}(X)\\)</span>. So, all we need to do is find a basis for <span class="math-inline">\\(\text{nullsp}(X)\\)</span>.

Note that <span class="math-inline">\\(X\\)</span> has two linearly independent columns (<span class="math-inline">\\(\vec x^{(1)}\\)</span> and <span class="math-inline">\\(\vec x^{(2)}\\)</span>), with a third column defined by

<div class="math-display">
$$
\vec x^{(3)} = 2 \vec q^{(1)}-\vec q^{(2)} = \vec x^{(1)} - \vec x^{(2)}
$$
</div>

**Before continuing to read these solutions, make sure you understand why the statement above is true!**

Rearranging the above equation gives

<div class="math-display">
$$
\vec x^{(1)} - \vec x^{(2)} - \vec x^{(3)} = \vec 0
$$
</div>

The coefficients on the three vectors in the linear combination above are <span class="math-inline">\\(1\\)</span>, <span class="math-inline">\\(-1\\)</span>, and <span class="math-inline">\\(-1\\)</span>. So, <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ -1 \\\\ -1 \end{bmatrix}\\)</span> is in <span class="math-inline">\\(\text{nullsp}(X)\\)</span>. Not only that, but it's a basis for <span class="math-inline">\\(\text{nullsp}(X)\\)</span>, since <span class="math-inline">\\(\text{rank}(X) = 2\\)</span> and thus <span class="math-inline">\\(\text{dim}(\text{nullsp}(X)) = 3-2 = 1\\)</span> (meaning any one vector in <span class="math-inline">\\(\text{nullsp}(X)\\)</span> is a basis for it). Another commonly chosen basis for <span class="math-inline">\\(\text{nullsp}(X)\\)</span> was <span class="math-inline">\\(\begin{bmatrix} -1 \\\\ 1 \\\\ 1 \end{bmatrix}\\)</span>.

So, the full set of minimizers is

<div class="math-display">
$$
\boxed{\left\{ \begin{bmatrix}-1\\\\10\\\\0\end{bmatrix} + t \begin{bmatrix}1\\\\-1\\\\-1\end{bmatrix} : t \in \mathbb{R} \right\}}
$$
</div>

</details>

</div>
</div>

</div>
