Let

<div class="math-display">
$$
A=\begin{bmatrix}
0&0&1&0\\\\
1&0&0&0\\\\
0&1&0&0\\\\
0&0&0&-1
\end{bmatrix},\qquad
\vec v=\begin{bmatrix}1\\\\2\\\\3\\\\4\end{bmatrix}
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge badge-points">2 pts</span> Find <span class="math-inline">\\(A\vec v\\)</span>.

<details markdown="1"><summary>Solution</summary>

Multiplying by <span class="math-inline">\\(A\\)</span> cycles the first three components and negates the fourth:

<div class="math-display">
$$
A\begin{bmatrix}v_1\\\\v_2\\\\v_3\\\\v_4\end{bmatrix}
=\begin{bmatrix}v_3\\\\v_1\\\\v_2\\\\-v_4\end{bmatrix}
\quad\Longrightarrow\quad
\boxed{A\vec v=\begin{bmatrix}3\\\\1\\\\2\\\\-4\end{bmatrix}}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge badge-points">2 pts</span> What is the smallest positive integer <span class="math-inline">\\(k\\)</span> such that <span class="math-inline">\\(A^k=I\\)</span>?

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 2</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 3</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 4</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 6</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 8</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 12</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 2</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 3</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 4</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> 6</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 8</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 12</span></div>

The first three components return to their original positions after a multiple of <span class="math-inline">\\(3\\)</span> applications of <span class="math-inline">\\(A\\)</span>. The fourth returns to its original sign after an even number of applications. The smallest positive integer divisible by both <span class="math-inline">\\(3\\)</span> and <span class="math-inline">\\(2\\)</span> is <span class="math-inline">\\(\boxed{k=6}\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge badge-points">6 pts</span> Give one basis for <span class="math-inline">\\(\text{nullsp}(A-I)\\)</span>.

<details markdown="1"><summary>Solution</summary>

A vector is in <span class="math-inline">\\(\text{nullsp}(A-I)\\)</span> exactly when <span class="math-inline">\\(A\vec x=\vec x\\)</span>. Componentwise,

<div class="math-display">
$$
x_3=x_1,\qquad x_1=x_2,\qquad x_2=x_3,\qquad -x_4=x_4
$$
</div>

 Thus, <span class="math-inline">\\(x&#95;1=x&#95;2=x&#95;3\\)</span> and <span class="math-inline">\\(x&#95;4=0\\)</span>. Every vector in the null space is a multiple of <span class="math-inline">\\(\begin{bmatrix}1\\\\1\\\\1\\\\0\end{bmatrix}\\)</span>, so one basis is

<div class="math-display">
$$
\boxed{\left\{\begin{bmatrix}1\\\\1\\\\1\\\\0\end{bmatrix}\right\}}
$$
</div>

</details>

Recall,

<div class="math-display">
$$
A=\begin{bmatrix}
0&0&1&0\\\\
1&0&0&0\\\\
0&1&0&0\\\\
0&0&0&-1
\end{bmatrix}
$$
</div>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge badge-points">6 pts</span> Applying <span class="math-inline">\\(A\\)</span> to a vector <span class="math-inline">\\(\vec x\\)</span> changes its components by the amounts shown below:

<div class="math-display">
$$
A\vec x-\vec x=\begin{bmatrix}m\\\\-3\\\\5\\\\2\end{bmatrix}
$$
</div>

<ol class="roman">
<li markdown="1">
(4 pts) Find <span class="math-inline">\\(m\\)</span>. Your answer should be a number with no variables.

<details markdown="1"><summary>Solution</summary>

   Applying <span class="math-inline">\\(A\\)</span> rearranges the first three components, so their sum does not change. Their changes must therefore sum to zero:

<div class="math-display">
$$
m+(-3)+5=0\quad\Longrightarrow\quad\boxed{m=-2}
$$
</div>

</details>
</li>
<li markdown="1">
(2 pts) For this value of <span class="math-inline">\\(m\\)</span>, how many vectors <span class="math-inline">\\(\vec x\\)</span> satisfy <span class="math-inline">\\(A\vec x-\vec x=\begin{bmatrix}m\\\\-3\\\\5\\\\2\end{bmatrix}\\)</span>?

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 0</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 1</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 2</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 3</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 4</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> Infinitely many</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 0</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 1</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 2</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 3</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> 4</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> Infinitely many</span></div>

   There are **infinitely many** solutions. One particular solution is <span class="math-inline">\\(\begin{bmatrix}0\\\\3\\\\-2\\\\-1\end{bmatrix}\\)</span>. Adding any vector in <span class="math-inline">\\(\text{nullsp}(A-I)\\)</span> preserves the product with <span class="math-inline">\\(A-I\\)</span>, giving

<div class="math-display">
$$
\vec x=\begin{bmatrix}0\\\\3\\\\-2\\\\-1\end{bmatrix}
    +t\begin{bmatrix}1\\\\1\\\\1\\\\0\end{bmatrix},\qquad t\in\mathbb R
$$
</div>

</details>
</li>
</ol>

</div>
</div>

</div>
