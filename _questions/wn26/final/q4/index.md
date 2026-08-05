---
number: 4
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> <span class="badge" data-flag="mt1-redemption" style="background-color: #9A3324; color: #FFFFFF; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">MT1 Redemption</span>
points: 4
flags: [mt1-redemption]
has_solution: true
images: []
---

Let

<div class="math-display">
$$
S =
\left\{
\begin{bmatrix}
x_1\\\\x_2\\\\x_3\\\\x_4\\\\x_5\\\\x_6
\end{bmatrix}
\in \mathbb{R}^6
:
x_1+x_2+x_3=0
\text{ and }
x_4=x_5
\right\}
$$
</div>

Find <span class="math-inline">\\(\dim(S)\\)</span>. Give your answer as an integer with no variables.

<span class="math-inline">\\(\dim(S)=\&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>

<details markdown="1"><summary>Solution</summary>

There are <span class="math-inline">\\(6\\)</span> variables total. The condition

<div class="math-display">
$$
x_1+x_2+x_3=0
$$
</div>

 removes one degree of flexibility, and the condition

<div class="math-display">
$$
x_4=x_5
$$
</div>

 removes one flexibility. So

<div class="math-display">
$$
\dim(S) = 6-2 = \boxed{4}
$$
</div>

Another way to think about it is to think of what a basis for <span class="math-inline">\\(S\\)</span> looks like. Every vector in <span class="math-inline">\\(S\\)</span> is of the form

<div class="math-display">
$$
\begin{bmatrix} a \\\\ b \\\\ -a-b \\\\ c \\\\ c \\\\ d \end{bmatrix}
$$
</div>

where <span class="math-inline">\\(a, b, c, d\\)</span> are real numbers. <span class="math-inline">\\(a\\)</span> and <span class="math-inline">\\(b\\)</span> (components 1 and 2) can both be anything, but component 3 is automatically determined once <span class="math-inline">\\(a\\)</span> and <span class="math-inline">\\(b\\)</span> are chosen. Similarly, <span class="math-inline">\\(c\\)</span> and <span class="math-inline">\\(d\\)</span> (components 4 and 6) can both be anything, but once component 4 is chosen, component 5 is automatically determined.

<span class="math-inline">\\(S\\)</span> is the set of all vectors that fit the template above. But

<div class="math-display">
$$
\begin{bmatrix} a \\\\ b \\\\ -a-b \\\\ c \\\\ c \\\\ d \end{bmatrix} = a \begin{bmatrix} 1 \\\\ 0 \\\\ -1 \\\\ 0 \\\\ 0 \\\\ 0 \end{bmatrix} + b \begin{bmatrix} 0 \\\\ 1 \\\\ -1 \\\\ 0 \\\\ 0 \\\\ 0 \end{bmatrix} + c \begin{bmatrix} 0 \\\\ 0 \\\\ 0 \\\\ 1 \\\\ 1 \\\\ 0 \end{bmatrix} + d \begin{bmatrix} 0 \\\\ 0 \\\\ 0 \\\\ 0 \\\\ 0 \\\\ 1 \end{bmatrix}
$$
</div>

So, <span class="math-inline">\\(S = \text{span}\left(\left\lbrace \begin{bmatrix} 1 \\\\ 0 \\\\ -1 \\\\ 0 \\\\ 0 \\\\ 0 \end{bmatrix}, \begin{bmatrix} 0 \\\\ 1 \\\\ -1 \\\\ 0 \\\\ 0 \\\\ 0 \end{bmatrix}, \begin{bmatrix} 0 \\\\ 0 \\\\ 0 \\\\ 1 \\\\ 1 \\\\ 0 \end{bmatrix}, \begin{bmatrix} 0 \\\\ 0 \\\\ 0 \\\\ 0 \\\\ 0 \\\\ 1 \end{bmatrix} \right\rbrace\right)\\)</span>. This is a 4-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^6\\)</span>, so <span class="math-inline">\\(\dim(S) = 4\\)</span>.
</details>
