---
number: 11
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">10 pts</span>
points: 10
flags: []
has_solution: true
images: [tikz-c9b7fae1abbb.svg]
---

The state diagram below describes a Markov chain with three states. <span class="math-inline">\\(a\\)</span> and <span class="math-inline">\\(b\\)</span> are both constants between 0 and 1.

![image](imgs/tikz-c9b7fae1abbb.svg)

Suppose that in the long run, <span class="math-inline">\\(\displaystyle\frac{25}{60}\\)</span> of the time is spent in state 1, <span class="math-inline">\\(\displaystyle\frac{21}{60}\\)</span> of the time is spent in state 2, and <span class="math-inline">\\(\displaystyle\frac{14}{60}\\)</span> of the time is spent in state 3.

Find the values of <span class="math-inline">\\(a\\)</span> and <span class="math-inline">\\(b\\)</span>. Show your work, and write your final answers in the boxes provided. Your answers should be numbers with no variables.

<details markdown="1"><summary>Solution</summary>

As discussed in [Chapter 9.3](https://notes.eecs245.org/eigenvalues-and-eigenvectors/markov-chains-adjacency-matrices/), a steady-state distribution is an eigenvector of the adjacency matrix with eigenvalue <span class="math-inline">\\(1\\)</span>, with the additional constraint that its entries sum to <span class="math-inline">\\(1\\)</span>. We are given that the steady-state distribution is

<div class="math-display">
$$
\vec x
=
\begin{bmatrix}
25/60\\\\
21/60\\\\
14/60
\end{bmatrix}
$$
</div>

 which already sums to <span class="math-inline">\\(1\\)</span>. The adjacency matrix for this Markov chain is

<div class="math-display">
$$
A=
\begin{bmatrix}
1-a & 1-b & 0\\\\
a & 0 & 1\\\\
0 & b & 0
\end{bmatrix}
$$
</div>

 So we need to choose <span class="math-inline">\\(a\\)</span> and <span class="math-inline">\\(b\\)</span> so that <span class="math-inline">\\(A\vec x=1\vec x=\vec x\\)</span>. This gives

<div class="math-display">
$$
\begin{bmatrix}
1-a & 1-b & 0\\\\
a & 0 & 1\\\\
0 & b & 0
\end{bmatrix}
\begin{bmatrix}
25/60\\\\
21/60\\\\
14/60
\end{bmatrix}
=
\begin{bmatrix}
25/60\\\\
21/60\\\\
14/60
\end{bmatrix}
$$
</div>

 or equivalently,

<div class="math-display">
$$
\begin{cases}
(1-a)\frac{25}{60}+(1-b)\frac{21}{60}=\frac{25}{60}\\\\
a\frac{25}{60}+\frac{14}{60}=\frac{21}{60}\\\\
b\frac{21}{60}=\frac{14}{60}
\end{cases}
$$
</div>

 The second equation gives

<div class="math-display">
$$
a\frac{25}{60}=\frac{7}{60}
\qquad\Rightarrow\qquad
a=\frac{7}{25}
$$
</div>

 The third equation gives

<div class="math-display">
$$
b=\frac{14}{21}=\frac{2}{3}
$$
</div>

 These values also satisfy the first equation, since

<div class="math-display">
$$
(1-\frac{7}{25})\frac{25}{60}+(1-\frac{2}{3})\frac{21}{60}
=
\frac{18}{60}+\frac{7}{60}
=
\frac{25}{60}
$$
</div>

</details>
