Throughout this problem, let

<div class="math-display">
$$
\vec x_1=\begin{bmatrix}12\\\\-2\\\\6\end{bmatrix},\qquad
\vec x_2=\begin{bmatrix}3\\\\0\\\\3\end{bmatrix},\qquad
P=\operatorname{span}(\{\vec x_1,\vec x_2\})
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge badge-points">5 pts</span> Find an equation for the plane <span class="math-inline">\\(P\\)</span> of the form <span class="math-inline">\\(Ax+By+Cz+d=0\\)</span>. Simplify your answer so that <span class="math-inline">\\(A=1\\)</span>.

<details markdown="1"><summary>Solution</summary>

Because <span class="math-inline">\\(P\\)</span> is a span, it contains the origin, so <span class="math-inline">\\(d=0\\)</span>. With <span class="math-inline">\\(A=1\\)</span>, the equation is <span class="math-inline">\\(x+By+Cz=0\\)</span>. Substituting the two spanning vectors gives

<div class="math-display">
$$
12-2B+6C=0,\qquad 3+3C=0
$$
</div>

 The second equation gives <span class="math-inline">\\(C=-1\\)</span>, and then the first gives <span class="math-inline">\\(B=3\\)</span>. Thus,

<div class="math-display">
$$
\boxed{x+3y-z=0}
$$
</div>

 Both vectors lie in this plane and are linearly independent, so they span the entire plane.
</details>

For part **b)**, suppose that <span class="math-inline">\\(\vec x&#95;3,\vec x&#95;4\in\mathbb R^3\\)</span> and that <span class="math-inline">\\(\operatorname{span}(\lbrace \vec x&#95;1,\vec x&#95;2,\vec x&#95;3,\vec x&#95;4\rbrace )\\)</span> is a **plane** in <span class="math-inline">\\(\mathbb R^3\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge badge-points">5 pts</span> For each statement below, determine whether it is impossible, possible (but **not** guaranteed), or guaranteed to be true, given the above assumptions. The first statement has been done for you as an example.

|  | **statement** | **impossible?** | **possible?** | **guaranteed?** |
|:--:|:---|:--:|:--:|:--:|
| <span class="math-inline">\\(i\\)</span> | <span class="math-inline">\\(\lVert \vec x&#95;3 \rVert = 5\\)</span>. | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble mc-correct" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> |
| <span class="math-inline">\\(ii\\)</span> | <span class="math-inline">\\(\vec x&#95;3\\)</span> and <span class="math-inline">\\(\vec x&#95;4\\)</span> are scalar multiples of one another. | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> |
| <span class="math-inline">\\(iii\\)</span> | <span class="math-inline">\\(\vec x&#95;4 = \vec 0\\)</span>. | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> |
| <span class="math-inline">\\(iv\\)</span> | The vectors <span class="math-inline">\\(\vec x&#95;1, \vec x&#95;2, \vec x&#95;3\\)</span> are linearly independent. | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> |
| <span class="math-inline">\\(v\\)</span> | span(<span class="math-inline">\\(\lbrace \vec x&#95;3, \vec x&#95;4\rbrace \\)</span>) <span class="math-inline">\\(= P\\)</span>. | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> |
| <span class="math-inline">\\(vi\\)</span> | <span class="math-inline">\\(\lbrace \vec x&#95;1, \vec x&#95;2\rbrace \\)</span> is a basis for <span class="math-inline">\\(P\\)</span>. | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> |

<details markdown="1"><summary>Solution</summary>

The span of all four vectors contains <span class="math-inline">\\(P\\)</span> and is a plane, so it must equal <span class="math-inline">\\(P\\)</span>. Thus, <span class="math-inline">\\(\vec x&#95;3\\)</span> and <span class="math-inline">\\(\vec x&#95;4\\)</span> both lie in <span class="math-inline">\\(P\\)</span>.

<ol class="roman">
<li markdown="1">
**Possible.** A vector in <span class="math-inline">\\(P\\)</span> can have length <span class="math-inline">\\(5\\)</span>, but it doesn't need to.
</li>
<li markdown="1">
**Possible.** For example, choose <span class="math-inline">\\(\vec x&#95;3=\vec x&#95;1\\)</span> and <span class="math-inline">\\(\vec x&#95;4=2\vec x&#95;1\\)</span>. They don't need to be scalar multiples: we could instead choose <span class="math-inline">\\(\vec x&#95;3=\vec x&#95;1\\)</span> and <span class="math-inline">\\(\vec x&#95;4=\vec x&#95;2\\)</span>.
</li>
<li markdown="1">
**Possible.** We may choose <span class="math-inline">\\(\vec x&#95;4=\vec0\\)</span> because the first two vectors already span <span class="math-inline">\\(P\\)</span>.
</li>
<li markdown="1">
**Impossible.** Three vectors in a two-dimensional space cannot be linearly independent.
</li>
<li markdown="1">
**Possible.** Choosing <span class="math-inline">\\(\vec x&#95;3=\vec x&#95;1\\)</span> and <span class="math-inline">\\(\vec x&#95;4=\vec x&#95;2\\)</span> works. Choosing both to be zero shows that this is not guaranteed.
</li>
<li markdown="1">
**Guaranteed.** By definition, <span class="math-inline">\\(\vec x&#95;1\\)</span> and <span class="math-inline">\\(\vec x&#95;2\\)</span> span <span class="math-inline">\\(P\\)</span>, and they are not scalar multiples of one another, so they form a basis.
</li>
</ol>

</details>

Recall,

<div class="math-display">
$$
\vec x_1=\begin{bmatrix}12\\\\-2\\\\6\end{bmatrix},\qquad
\vec x_2=\begin{bmatrix}3\\\\0\\\\3\end{bmatrix},\qquad
P=\operatorname{span}(\{\vec x_1,\vec x_2\})
$$
</div>

Additionally, suppose that <span class="math-inline">\\(\vec x&#95;3,\vec x&#95;4\in\mathbb R^3\\)</span> and that <span class="math-inline">\\(\operatorname{span}(\lbrace \vec x&#95;1,\vec x&#95;2,\vec x&#95;3,\vec x&#95;4\rbrace )\\)</span> is a **plane** in <span class="math-inline">\\(\mathbb R^3\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge badge-points">4 pts</span> Give one nonzero vector orthogonal to <span class="math-inline">\\(3\vec x&#95;1-7\vec x&#95;2+12\vec x&#95;3-\vec x&#95;4\\)</span>. Your answer should have no variables. Briefly justify it.

<details markdown="1"><summary>Solution</summary>

From part **a)**, <span class="math-inline">\\(\vec n=\begin{bmatrix}1\\\\3\\\\-1\end{bmatrix}\\)</span> is normal to <span class="math-inline">\\(P\\)</span>. All four vectors lie in <span class="math-inline">\\(P\\)</span>, so <span class="math-inline">\\(\vec n\cdot\vec x&#95;i=0\\)</span> for <span class="math-inline">\\(i=1,2,3,4\\)</span>. By distributivity,

<div class="math-display">
$$
\vec n\cdot(3\vec x_1-7\vec x_2+12\vec x_3-\vec x_4)=0
$$
</div>

 Thus, one valid answer is <span class="math-inline">\\(\boxed{\begin{bmatrix}1\\\\3\\\\-1\end{bmatrix}}\\)</span>. Any nonzero scalar multiple of this vector also works.
</details>

For part **d)**, suppose that <span class="math-inline">\\(\vec x&#95;3,\vec x&#95;4\in\mathbb R^3\\)</span> but that <span class="math-inline">\\(\operatorname{span}(\lbrace \vec x&#95;1,\vec x&#95;2,\vec x&#95;3,\vec x&#95;4\rbrace ) = \mathbb R^3\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge badge-points">5 pts</span> Which statements are **impossible**? Select all that apply.

<span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\vec x&#95;3\\)</span> and <span class="math-inline">\\(\vec x&#95;4\\)</span> are on <span class="math-inline">\\(P\\)</span>.

<span class="mc-square" aria-hidden="true"></span> The vectors <span class="math-inline">\\(\vec x&#95;3,\vec x&#95;4\\)</span> are linearly independent.

<span class="mc-square" aria-hidden="true"></span> The vectors <span class="math-inline">\\(\vec x&#95;1,\vec x&#95;2,\vec x&#95;3,\vec x&#95;4\\)</span> are linearly independent.

<span class="mc-square" aria-hidden="true"></span> There is a nonzero vector orthogonal to all four vectors.

<span class="mc-square" aria-hidden="true"></span> Every subset containing exactly three of the four vectors is a basis for <span class="math-inline">\\(\mathbb R^3\\)</span>.

<details markdown="1"><summary>Solution</summary>

<span class="mc-square" aria-hidden="true"></span> Every subset containing exactly three of the four vectors is a basis for <span class="math-inline">\\(\mathbb R^3\\)</span>.

Select **options 1, 3, and 4**.

<ol>
<li markdown="1">
**Impossible.** If both additional vectors were on <span class="math-inline">\\(P\\)</span>, all four vectors would span only <span class="math-inline">\\(P\\)</span>, not <span class="math-inline">\\(\mathbb R^3\\)</span>.
</li>
<li markdown="1">
**Possible.** Choose <span class="math-inline">\\(\vec x&#95;3\\)</span> outside <span class="math-inline">\\(P\\)</span> and <span class="math-inline">\\(\vec x&#95;4=\vec x&#95;1\\)</span>. These two vectors are independent, and all four span <span class="math-inline">\\(\mathbb R^3\\)</span>.
</li>
<li markdown="1">
**Impossible.** Four vectors in <span class="math-inline">\\(\mathbb R^3\\)</span> are always linearly dependent.
</li>
<li markdown="1">
**Impossible.** A vector orthogonal to all four is orthogonal to their entire span, <span class="math-inline">\\(\mathbb R^3\\)</span>. In particular, it is orthogonal to itself and must be zero.
</li>
<li markdown="1">
**Possible.** Choose <span class="math-inline">\\(\vec x&#95;3\\)</span> outside <span class="math-inline">\\(P\\)</span> and <span class="math-inline">\\(\vec x&#95;4=\vec x&#95;1+\vec x&#95;2+\vec x&#95;3\\)</span>. The first three vectors form a basis. Replacing any one with their sum still gives a basis, since the omitted vector can be recovered by subtracting the other two from the sum.
</li>
</ol>

</details>

</div>
</div>

</div>
