---
number: 7
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span> <span class="badge" data-flag="mt2-redemption" style="background-color: #9A3324; color: #FFFFFF; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">MT2 Redemption</span>
points: 12
flags: [mt2-redemption]
has_solution: true
images: []
---

Suppose <span class="math-inline">\\(X\\)</span> is an <span class="math-inline">\\(n \times d\\)</span> matrix with linearly independent columns, <span class="math-inline">\\(d&lt;n\\)</span>, and <span class="math-inline">\\(\vec y \in \mathbb{R}^n\\)</span>.

Furthermore, suppose <span class="math-inline">\\(P\\)</span> is the matrix that projects vectors in <span class="math-inline">\\(\mathbb{R}^n\\)</span> onto <span class="math-inline">\\(\text{colsp}(X)\\)</span>, and <span class="math-inline">\\(\vec p = P \vec y\\)</span> is the projection of <span class="math-inline">\\(\vec y\\)</span> onto <span class="math-inline">\\(\text{colsp}(X)\\)</span>.

Finally, let <span class="math-inline">\\(Q\\)</span> be an <span class="math-inline">\\(n \times n\\)</span> orthogonal matrix.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span>
1.  (2 pts) What is <span class="math-inline">\\(\text{det}(P)\\)</span>?
<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(-1\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(0\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(-1\\)</span> or <span class="math-inline">\\(1\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> None of these</span></div>

2.  (2 pts) What is <span class="math-inline">\\(\text{det}(Q)\\)</span>?
<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(-1\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(0\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(-1\\)</span> or <span class="math-inline">\\(1\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> None of these</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(-1\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(0\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(-1\\)</span> or <span class="math-inline">\\(1\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> None of these</span></div>

**(i)** Since <span class="math-inline">\\(P\\)</span> projects onto <span class="math-inline">\\(\text{colsp}(X)\\)</span> and <span class="math-inline">\\(d&lt;n\\)</span>, multiple vectors in <span class="math-inline">\\(\mathbb{R}^n\\)</span> will have the same projection onto <span class="math-inline">\\(\text{colsp}(X)\\)</span>. So <span class="math-inline">\\(P\\)</span> is not invertible, and therefore <span class="math-inline">\\(\det(P)=0\\)</span>.

**(ii)** Since <span class="math-inline">\\(Q\\)</span> is orthogonal, <span class="math-inline">\\(Q^TQ=I\\)</span>. Taking determinants gives

<div class="math-display">
$$
\det(Q^TQ)=\det(I)
$$
</div>

 so, since <span class="math-inline">\\(\det(I)=1\\)</span>, <span class="math-inline">\\(\text{det}(Q^T) = \det(Q)\\)</span>, and in general <span class="math-inline">\\(\text{det}(AB) = \det(A)\det(B)\\)</span> for square <span class="math-inline">\\(A\\)</span> and <span class="math-inline">\\(B\\)</span>, we have

<div class="math-display">
$$
\det(Q)^2=1
$$
</div>

 and therefore <span class="math-inline">\\(\det(Q)\\)</span> is either <span class="math-inline">\\(-1\\)</span> or <span class="math-inline">\\(1\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">2 pts</span> Which of the following vectors is orthogonal to <span class="math-inline">\\(\text{colsp}(X)\\)</span>?

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\vec y\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(P \vec y\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(Q \vec y\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\((I - P) \vec y\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\((I - Q) \vec y\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> None of these</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\vec y\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(P \vec y\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(Q \vec y\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\((I - P) \vec y\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\((I - Q) \vec y\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> None of these</span></div>

The vector <span class="math-inline">\\(P\vec{y}\\)</span> is the projection of <span class="math-inline">\\(\vec{y}\\)</span> onto <span class="math-inline">\\(\text{colsp}(X)\\)</span>, so the error vector

<div class="math-display">
$$
\vec y - \vec p = \vec{y}-P\vec{y}=(I-P)\vec{y}
$$
</div>

 is orthogonal to <span class="math-inline">\\(\text{colsp}(X)\\)</span>. This is the same projection geometry used in [Chapter 6.3](https://notes.eecs245.org/linear-transformations-and-projections/projecting-onto-column-space/); the novel thing here was the representation of the error vector as a linear combination of the columns of <span class="math-inline">\\(I-P\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Prove that the projection of <span class="math-inline">\\(Q \vec y\\)</span> onto <span class="math-inline">\\(\text{colsp}(QX)\\)</span> is <span class="math-inline">\\(Q \vec p\\)</span>. <em>Hint: Start by showing that the matrix that projects vectors in <span class="math-inline">\\(\mathbb{R}^n\\)</span> onto <span class="math-inline">\\(\text{colsp}(QX)\\)</span> is <span class="math-inline">\\(Q P Q^T\\)</span>.</em>

<details markdown="1"><summary>Solution</summary>

Since <span class="math-inline">\\(X\\)</span> has linearly independent columns, the matrix that projects onto <span class="math-inline">\\(\text{colsp}(X)\\)</span> is

<div class="math-display">
$$
P=X(X^TX)^{-1}X^T
$$
</div>

 Now, the matrix that projects onto <span class="math-inline">\\(\text{colsp}(QX)\\)</span> is

<div class="math-display">
$$
\begin{align*}
QX((QX)^T(QX))^{-1}(QX)^T
&=
QX(X^TQ^TQX)^{-1}X^TQ^T \\\\
&=
QX(X^TX)^{-1}X^TQ^T \\\\
&=
QPQ^T
\end{align*}
$$
</div>

using the fact that <span class="math-inline">\\(Q^TQ=I\\)</span>. Therefore, the projection of <span class="math-inline">\\(Q\vec{y}\\)</span> onto <span class="math-inline">\\(\text{colsp}(QX)\\)</span> is

<div class="math-display">
$$
(QPQ^T)(Q\vec{y})
=
QP(Q^TQ)\vec{y}
=
QP\vec{y}
=
Q\vec{p}
$$
</div>

Why does this happen? Think of <span class="math-inline">\\(Q\\)</span> as a rotation matrix. This is saying that if we:

**(i)** Rotate <span class="math-inline">\\(\vec y\\)</span> and rotate <span class="math-inline">\\(\text{colsp}(X)\\)</span>, and project the rotated <span class="math-inline">\\(\vec y\\)</span> onto the rotated <span class="math-inline">\\(\text{colsp}(X)\\)</span>, OR

**(ii)** Project the original <span class="math-inline">\\(\vec y\\)</span> onto the original <span class="math-inline">\\(\text{colsp}(X)\\)</span>, and then rotate the projected vector,

we end up with the same vector in either case.
</details>

</div>
</div>

</div>
