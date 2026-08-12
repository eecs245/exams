---
number: 10
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>
points: 12
flags: []
has_solution: true
images: []
---

Consider the adjacency matrix <span class="math-inline">\\(A = \begin{bmatrix} 0.4 &amp; 0 &amp; 0.5 \\\\ 0.4 &amp; 0 &amp; 0.5 \\\\ a &amp; b &amp; c \end{bmatrix}\\)</span> for a Markov chain with three states, where <span class="math-inline">\\(a, b, c \in \mathbb{R}\\)</span> are some constants.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Find <span class="math-inline">\\(a\\)</span>, <span class="math-inline">\\(b\\)</span>, and <span class="math-inline">\\(c\\)</span> such that <span class="math-inline">\\(A\\)</span> is a valid adjacency matrix. Give your answers as numbers with no variables.

<span class="math-inline">\\(a = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;, \qquad b = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;, \qquad c = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>

<details markdown="1"><summary>Solution</summary>

For a valid adjacency matrix, each column must sum to 1, since the columns describe the transition probabilities **out of** a given state. So,

<div class="math-display">
$$
\begin{align*}
0.4 + 0.4 + a &= 1 \implies a = 0.2 \\\\
0 + 0 + b &= 1 \implies b = 1 \\\\
0.5 + 0.5 + c &= 1 \implies c = 0
\end{align*}
$$
</div>

Therefore,

<div class="math-display">
$$
\boxed{a = 0.2, \qquad b = 1, \qquad c = 0}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Suppose <span class="math-inline">\\(\vec x^{\ast} \in \mathbb{R}^3\\)</span> is a vector containing the long-run fraction of time spent in each state. Which of the following vectors is <span class="math-inline">\\(\vec x^{\ast}\\)</span> and why?

1.  <span class="math-inline">\\(\vec x^{\ast}\\)</span> is
<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \begin{bmatrix} 1/3 \\\\ 1/3 \\\\ 1/3 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \begin{bmatrix} 4/9 \\\\ 0 \\\\ 5/9 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \begin{bmatrix} 5/16 \\\\ 5/16 \\\\ 6/16 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \begin{bmatrix} 5/16 \\\\ 6/16 \\\\ 5/16 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(\displaystyle \begin{bmatrix} 3/16 \\\\ 3/16 \\\\ 10/16 \end{bmatrix}\\)</span></span></div>

2.  because <span class="math-inline">\\(\vec x^{\ast}\\)</span> is the eigenvector of <span class="math-inline">\\(A\\)</span> corresponding to the eigenvalue



<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(-1\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(0\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(0.4\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1.8\\)</span></span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(-1\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(0\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(0.4\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(1\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(1.8\\)</span></span></div>

The long-run fraction of time spent in each state is the stationary distribution, so it must satisfy

<div class="math-display">
$$
A\vec x^* = \vec x^*
$$
</div>

 That means <span class="math-inline">\\(\vec x^{\ast}\\)</span> is an eigenvector corresponding to eigenvalue 1.

Using the matrix from part **a)**,

<div class="math-display">
$$
A = \begin{bmatrix} 0.4 & 0 & 0.5 \\\\ 0.4 & 0 & 0.5 \\\\ 0.2 & 1 & 0 \end{bmatrix}
$$
</div>

 we can check that

<div class="math-display">
$$
A\begin{bmatrix} 5/16 \\\\ 5/16 \\\\ 6/16 \end{bmatrix}
=
\begin{bmatrix} 5/16 \\\\ 5/16 \\\\ 6/16 \end{bmatrix}
$$
</div>

 So the correct choices are

<div class="math-display">
$$
\boxed{\begin{bmatrix} 5/16 \\\\ 5/16 \\\\ 6/16 \end{bmatrix}}
\qquad \text{and} \qquad
\boxed{1}
$$
</div>

</details>

</div>
</div>

</div>
