Suppose <span class="math-inline">\\(a\\)</span>, <span class="math-inline">\\(b\\)</span>, and <span class="math-inline">\\(c\\)</span> are real numbers, and let

<div class="math-display">
$$
\vec u=\begin{bmatrix}a\\\\b\\\\c\end{bmatrix},\qquad
\vec v=\begin{bmatrix}b\\\\c\\\\a\end{bmatrix}
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge badge-points">5 pts</span> Use the Cauchy--Schwarz inequality to prove that the following holds for all real numbers <span class="math-inline">\\(a\\)</span>, <span class="math-inline">\\(b\\)</span>, and <span class="math-inline">\\(c\\)</span>:

<div class="math-display">
$$
|ab+bc+ca|\leq a^2+b^2+c^2
$$
</div>

<details markdown="1"><summary>Solution</summary>

The Cauchy--Schwarz inequality says that

<div class="math-display">
$$
|\vec u\cdot\vec v|\leq\lVert\vec u\rVert\lVert\vec v\rVert
$$
</div>

For the given vectors,

<div class="math-display">
$$
\vec u\cdot\vec v=ab+bc+ca,\qquad
\lVert\vec u\rVert=\lVert\vec v\rVert=\sqrt{a^2+b^2+c^2}
$$
</div>

 By the Cauchy--Schwarz inequality,

<div class="math-display">
$$
|ab+bc+ca|=|\vec u\cdot\vec v|
\leq\lVert\vec u\rVert\lVert\vec v\rVert
=\boxed{a^2+b^2+c^2}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge badge-points">6 pts</span> Now suppose that <span class="math-inline">\\(a+b+c=0\\)</span> and <span class="math-inline">\\(\vec u\neq\vec0\\)</span>. Find <span class="math-inline">\\(\theta\\)</span>, the angle between <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span>. Give your answer as the cosine inverse of a number (e.g. <span class="math-inline">\\(\cos^{-1}(3/4)\\)</span>). <em>Hint: <span class="math-inline">\\((a+b+c)^2=a^2+b^2+c^2+2ab+2bc+2ca\\)</span>.</em>

<details markdown="1"><summary>Solution</summary>

Using the hint and <span class="math-inline">\\(a+b+c=0\\)</span>,

<div class="math-display">
$$
0=(a+b+c)^2=a^2+b^2+c^2+2(ab+bc+ca)
$$
</div>

 Therefore,

<div class="math-display">
$$
ab+bc+ca=-\frac12(a^2+b^2+c^2)
$$
</div>

 Note that <span class="math-inline">\\(ab+bc+ca=\vec u\cdot\vec v\\)</span>, and

<div class="math-display">
$$
\lVert\vec u\rVert\lVert\vec v\rVert
=\sqrt{a^2+b^2+c^2}\sqrt{a^2+b^2+c^2}
=a^2+b^2+c^2
$$
</div>

 Part of the point of part **a)** was to get you to notice this!

Since <span class="math-inline">\\(\vec u\neq\vec0\\)</span>, the denominator below is positive. We have

<div class="math-display">
$$
\cos\theta=\frac{\vec u\cdot\vec v}{\lVert\vec u\rVert\lVert\vec v\rVert}
=\frac{ab+bc+ca}{a^2+b^2+c^2}=-\frac12
$$
</div>

 Thus, <span class="math-inline">\\(\boxed{\theta=\cos^{-1}(-1/2)}\\)</span>.
</details>

</div>
</div>

</div>
