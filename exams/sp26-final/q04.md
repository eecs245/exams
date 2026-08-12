---
number: 4
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">5 pts</span> <span class="badge" data-flag="mt1-redemption" style="background-color: #9A3324; color: #FFFFFF; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">MT1 Redemption</span>
points: 5
flags: [mt1-redemption]
has_solution: true
images: []
---

Suppose <span class="math-inline">\\(S = \left\lbrace \begin{bmatrix} x&#95;1 \\\\ x&#95;2 \\\\ x&#95;3 \\\\ x&#95;4 \end{bmatrix} : x&#95;1 + x&#95;2 + 2x&#95;3 = 0 \text{ and } x&#95;3 = x&#95;4 \right\rbrace\\)</span>. State one basis for <span class="math-inline">\\(S\\)</span>. Your answer should be a list of vectors with no variables.

<span class="math-inline">\\(\text{one basis for } S =\\)</span> \_\_\_\_\_\_

<details markdown="1"><summary>Solution</summary>

The condition <span class="math-inline">\\(x&#95;3=x&#95;4\\)</span> means we can write <span class="math-inline">\\(x&#95;3=x&#95;4=b\\)</span>. The other condition gives

<div class="math-display">
$$
x_1+x_2+2b=0
$$
</div>

 so <span class="math-inline">\\(x&#95;1=-x&#95;2-2b\\)</span>. Let <span class="math-inline">\\(x&#95;2=a\\)</span>. Then every vector in <span class="math-inline">\\(S\\)</span> can be written as

<div class="math-display">
$$
\begin{bmatrix}
x_1\\\\x_2\\\\x_3\\\\x_4
\end{bmatrix}
=
\begin{bmatrix}
-a-2b\\\\a\\\\b\\\\b
\end{bmatrix}
=
a\begin{bmatrix}-1\\\\1\\\\0\\\\0\end{bmatrix}
+b\begin{bmatrix}-2\\\\0\\\\1\\\\1\end{bmatrix}
$$
</div>

 So, one basis for <span class="math-inline">\\(S\\)</span> is

<div class="math-display">
$$
\left\{
\begin{bmatrix}-1\\\\1\\\\0\\\\0\end{bmatrix},
\begin{bmatrix}-2\\\\0\\\\1\\\\1\end{bmatrix}
\right\}
$$
</div>

Another way to think about this: since <span class="math-inline">\\(\dim(S)=2\\)</span> (the subspace has two "degrees of freedom", or free variables), any two linearly independent vectors in <span class="math-inline">\\(S\\)</span> span all of <span class="math-inline">\\(S\\)</span> (see [Chapter 4.3](https://notes.eecs245.org/linear-independence/vector-spaces-basis-dimension/)). So, we could just play with the numbers until we end up with two vectors that are not scalar multiples of each other that both satisfy the conditions of inclusion in <span class="math-inline">\\(S\\)</span>. For instance,

<div class="math-display">
$$
\left\{\begin{bmatrix}-1\\\\1\\\\0\\\\0\end{bmatrix},\begin{bmatrix}-3 \\\\ 1 \\\\ 1 \\\\ 1\end{bmatrix}\right\}
$$
</div>

 is also a valid basis.
</details>
