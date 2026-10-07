Suppose <span class="math-inline">\\(\vec v&#95;1,\vec v&#95;2\in\mathbb R^2\\)</span> satisfy

<div class="math-display">
$$
\vec v_1=\begin{bmatrix}18\\\\-24\end{bmatrix},\qquad
\lVert\vec v_2\rVert=6,\qquad
\vec v_1\cdot\vec v_2=0
$$
</div>

 Let

<div class="math-display">
$$
\vec x=\begin{bmatrix}10\\\\-5\end{bmatrix}
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge badge-points">5 pts</span> Find <span class="math-inline">\\(\vec p\\)</span>, the projection of <span class="math-inline">\\(\vec x\\)</span> onto <span class="math-inline">\\(\vec v&#95;1\\)</span>. Give your answer as a vector with two components and no variables.

<details markdown="1"><summary>Solution</summary>

Since <span class="math-inline">\\(\vec v&#95;1=6\begin{bmatrix}3\\\\-4\end{bmatrix}\\)</span>, projecting onto <span class="math-inline">\\(\vec v&#95;1\\)</span> is equivalent to projecting onto <span class="math-inline">\\(\begin{bmatrix}3\\\\-4\end{bmatrix}\\)</span>. So,

<div class="math-display">
$$
\vec p=\frac{(10)(3)+(-5)(-4)}{3^2+(-4)^2}\begin{bmatrix}3\\\\-4\end{bmatrix}
=\frac{50}{25}\begin{bmatrix}3\\\\-4\end{bmatrix}
=\boxed{\begin{bmatrix}6\\\\-8\end{bmatrix}}
$$
</div>

 Equivalently, using <span class="math-inline">\\(\vec v&#95;1\\)</span> directly gives the coefficient <span class="math-inline">\\(300/900=1/3\\)</span>.

![image](imgs/tikz-25490f820b29.svg)
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge badge-points">7 pts</span> Suppose that the first component of <span class="math-inline">\\(\vec v&#95;2\\)</span> is positive. Write <span class="math-inline">\\(\vec x\\)</span> as a linear combination of <span class="math-inline">\\(\vec v&#95;1\\)</span> and <span class="math-inline">\\(\vec v&#95;2\\)</span> by filling in the two boxes below.

<div class="math-display">
$$
\vec x=\_\_\_\_\_\_\vec v_1+\_\_\_\_\_\_\vec v_2
$$
</div>

<details markdown="1"><summary>Solution</summary>

A vector perpendicular to <span class="math-inline">\\(\begin{bmatrix}3\\\\-4\end{bmatrix}\\)</span> with positive first component has direction <span class="math-inline">\\(\begin{bmatrix}4\\\\3\end{bmatrix}\\)</span>. This direction vector has length <span class="math-inline">\\(5\\)</span>, so

<div class="math-display">
$$
\vec v_2=\frac65\begin{bmatrix}4\\\\3\end{bmatrix}
$$
</div>

 From part **a)**, <span class="math-inline">\\(\vec p=\frac13\vec v&#95;1\\)</span>. The remaining component is

<div class="math-display">
$$
\vec x-\vec p=\begin{bmatrix}10\\\\-5\end{bmatrix}-\begin{bmatrix}6\\\\-8\end{bmatrix}
=\begin{bmatrix}4\\\\3\end{bmatrix}=\frac56\vec v_2
$$
</div>

 Therefore,

<div class="math-display">
$$
\boxed{\vec x=\frac13\vec v_1+\frac56\vec v_2}
$$
</div>

![image](imgs/tikz-8d44ebc79c95.svg)
</details>

</div>
</div>

</div>
