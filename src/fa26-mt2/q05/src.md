Let

<div class="math-display">
$$
X=\begin{bmatrix}1&4\\\\2&3\\\\2&4\\\\0&2\end{bmatrix},\qquad
\vec q_1=\frac13\begin{bmatrix}1\\\\2\\\\2\\\\0\end{bmatrix}
$$
</div>

 We would like to find **orthogonal** unit vectors <span class="math-inline">\\(\vec q&#95;1,\vec q&#95;2\in\mathbb R^4\\)</span> such that

<div class="math-display">
$$
\text{span}(\{\vec q_1,\vec q_2\})=\text{colsp}(X)
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge badge-points">6 pts</span> Find one possible <span class="math-inline">\\(\vec q&#95;2\\)</span>.

<details markdown="1"><summary>Solution</summary>

Let <span class="math-inline">\\(\vec x&#95;2\\)</span> be the second column of <span class="math-inline">\\(X\\)</span>. Remove its component in the direction of <span class="math-inline">\\(\vec q&#95;1\\)</span>:

<div class="math-display">
$$
\vec q_1\cdot\vec x_2=\frac{4+6+8}{3}=6
$$
</div>



<div class="math-display">
$$
\vec u_2=\vec x_2-6\vec q_1
=\begin{bmatrix}4\\\\3\\\\4\\\\2\end{bmatrix}
-\begin{bmatrix}2\\\\4\\\\4\\\\0\end{bmatrix}
=\begin{bmatrix}2\\\\-1\\\\0\\\\2\end{bmatrix}
$$
</div>

 Since <span class="math-inline">\\(\|\vec u&#95;2\|=\sqrt{4+1+4}=3\\)</span>, one answer is

<div class="math-display">
$$
\boxed{\vec q_2=\frac13\begin{bmatrix}2\\\\-1\\\\0\\\\2\end{bmatrix}}
$$
</div>

 This is a unit vector orthogonal to <span class="math-inline">\\(\vec q&#95;1\\)</span>. The first column of <span class="math-inline">\\(X\\)</span> is <span class="math-inline">\\(3\vec q&#95;1\\)</span>, and its second column is <span class="math-inline">\\(6\vec q&#95;1+3\vec q&#95;2\\)</span>, so the two unit vectors span <span class="math-inline">\\(\text{colsp}(X)\\)</span>. The negative of this <span class="math-inline">\\(\vec q&#95;2\\)</span> is also valid.
</details>

For the remaining parts, suppose <span class="math-inline">\\(Q\\)</span> has orthonormal columns <span class="math-inline">\\(\vec q&#95;1,\vec q&#95;2\in\mathbb R^4\\)</span>. You do not need your answer to part (a). Let

<div class="math-display">
$$
Q=\begin{bmatrix}|&|\\\\\vec q_1&\vec q_2\\\\|&|\end{bmatrix},\qquad
Z=\begin{bmatrix}|&|\\\\\vec q_1+\vec q_2&\vec q_1-\vec q_2\\\\|&|\end{bmatrix}
$$
</div>

 and suppose <span class="math-inline">\\(\vec y\in\mathbb R^4\\)</span> satisfies

<div class="math-display">
$$
Q^T\vec y=\begin{bmatrix}3\\\\1\end{bmatrix}
$$
</div>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge badge-points">2 pts</span> Is <span class="math-inline">\\(\vec y\in\text{colsp}(Q)\\)</span>?

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Yes</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> No</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Impossible to tell</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Yes</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> No</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> Impossible to tell</span></div>

**Impossible to tell.** The vector <span class="math-inline">\\(\vec y&#95;0=3\vec q&#95;1+\vec q&#95;2\\)</span> is in <span class="math-inline">\\(\text{colsp}(Q)\\)</span> and has the specified product with <span class="math-inline">\\(Q^T\\)</span>.

There are also nonzero vectors <span class="math-inline">\\(\vec r\\)</span> orthogonal to <span class="math-inline">\\(\text{colsp}(Q)\\)</span>, since this is a two-dimensional subspace of <span class="math-inline">\\(\mathbb R^4\\)</span>. Then <span class="math-inline">\\(\vec y&#95;0+\vec r\\)</span> is outside <span class="math-inline">\\(\text{colsp}(Q)\\)</span> but has the same product with <span class="math-inline">\\(Q^T\\)</span>, because <span class="math-inline">\\(Q^T\vec r=\vec0\\)</span>. Both possibilities are consistent with the information given.
</details>

Recall that <span class="math-inline">\\(Q\\)</span> has orthonormal columns, and

<div class="math-display">
$$
Z=\begin{bmatrix}|&|\\\\\vec q_1+\vec q_2&\vec q_1-\vec q_2\\\\|&|\end{bmatrix},\qquad
Q^T\vec y=\begin{bmatrix}3\\\\1\end{bmatrix}
$$
</div>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge badge-points">4 pts</span> Which choice gives both the vector <span class="math-inline">\\(\vec w^\ast\\)</span> that minimizes <span class="math-inline">\\(\|\vec y-Z\vec w\|^2\\)</span> and the resulting projection, <span class="math-inline">\\(\vec p=Z\vec w^\ast\\)</span>?

<span class="mc-bubble" aria-hidden="true"></span> A. <span class="math-inline">\\(\vec w^\ast=\begin{bmatrix}3\\\\1\end{bmatrix},\quad \vec p=3\vec q&#95;1+\vec q&#95;2\\)</span>

<span class="mc-bubble" aria-hidden="true"></span> B. <span class="math-inline">\\(\vec w^\ast=\begin{bmatrix}2\\\\1\end{bmatrix},\quad \vec p=3\vec q&#95;1+\vec q&#95;2\\)</span>

<span class="mc-bubble" aria-hidden="true"></span> C. <span class="math-inline">\\(\vec w^\ast=\begin{bmatrix}3\\\\1\end{bmatrix},\quad \vec p=4\vec q&#95;1+2\vec q&#95;2\\)</span>

<span class="mc-bubble" aria-hidden="true"></span> D. <span class="math-inline">\\(\vec w^\ast=\begin{bmatrix}2\\\\1\end{bmatrix},\quad \vec p=2\vec q&#95;1+\vec q&#95;2\\)</span>

<span class="mc-bubble" aria-hidden="true"></span> E. <span class="math-inline">\\(\vec w^\ast=\begin{bmatrix}1\\\\2\end{bmatrix},\quad \vec p=3\vec q&#95;1+\vec q&#95;2\\)</span>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> A. <span class="math-inline">\\(\vec w^\ast=\begin{bmatrix}3\\\\1\end{bmatrix},\quad \vec p=3\vec q&#95;1+\vec q&#95;2\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> B. <span class="math-inline">\\(\vec w^\ast=\begin{bmatrix}2\\\\1\end{bmatrix},\quad \vec p=3\vec q&#95;1+\vec q&#95;2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> C. <span class="math-inline">\\(\vec w^\ast=\begin{bmatrix}3\\\\1\end{bmatrix},\quad \vec p=4\vec q&#95;1+2\vec q&#95;2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> D. <span class="math-inline">\\(\vec w^\ast=\begin{bmatrix}2\\\\1\end{bmatrix},\quad \vec p=2\vec q&#95;1+\vec q&#95;2\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> E. <span class="math-inline">\\(\vec w^\ast=\begin{bmatrix}1\\\\2\end{bmatrix},\quad \vec p=3\vec q&#95;1+\vec q&#95;2\\)</span></span></div>

**B.** Adding and subtracting the columns of <span class="math-inline">\\(Z\\)</span> recovers <span class="math-inline">\\(2\vec q&#95;1\\)</span> and <span class="math-inline">\\(2\vec q&#95;2\\)</span>, so <span class="math-inline">\\(Z\\)</span> and <span class="math-inline">\\(Q\\)</span> have the same column space. Hence,

<div class="math-display">
$$
\boxed{\vec p=QQ^T\vec y=3\vec q_1+\vec q_2}
$$
</div>

 But <span class="math-inline">\\(Z\vec w=(w&#95;1+w&#95;2)\vec q&#95;1+(w&#95;1-w&#95;2)\vec q&#95;2\\)</span>. Independence of <span class="math-inline">\\(\vec q&#95;1,\vec q&#95;2\\)</span> therefore requires

<div class="math-display">
$$
w_1^\ast+w_2^\ast=3,\qquad w_1^\ast-w_2^\ast=1
\quad\Longrightarrow\quad
\boxed{\vec w^\ast=\begin{bmatrix}2\\\\1\end{bmatrix}}
$$
</div>

 <span class="math-inline">\\(Q^T\vec y\\)</span> gives coefficients in <span class="math-inline">\\(Q\\)</span>'s columns, while <span class="math-inline">\\(\vec w^\ast\\)</span> gives coefficients in <span class="math-inline">\\(Z\\)</span>'s columns.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge badge-points">4 pts</span> Identify whether each statement is true or false.

<ol class="roman">
<li markdown="1">
(2 pts) For every <span class="math-inline">\\(\vec x\in\mathbb R^2\\)</span>, <span class="math-inline">\\(Q^TQ\vec x=\vec x\\)</span>.
<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

**True.** Orthonormal columns give <span class="math-inline">\\(Q^TQ=I&#95;2\\)</span>, so <span class="math-inline">\\(Q^TQ\vec x=\vec x\\)</span> for every <span class="math-inline">\\(\vec x\in\mathbb R^2\\)</span>.
</details>
</li>
<li markdown="1">
(2 pts) <span class="math-inline">\\(QQ^T\\)</span> is invertible.
<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> False</span></div>

**False.** <span class="math-inline">\\(QQ^T\\)</span> is <span class="math-inline">\\(4\times4\\)</span>, and its columns lie in the two-dimensional space <span class="math-inline">\\(\text{colsp}(Q)\\)</span>. Its rank is at most <span class="math-inline">\\(2\\)</span>, so it is not invertible.
</details>
</li>
</ol>

</div>
</div>

</div>
