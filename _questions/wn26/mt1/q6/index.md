---
number: 6
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">14 pts</span>
points: 14
flags: []
has_solution: true
images: []
---

Suppose <span class="math-inline">\\(\vec x&#95;1, \vec x&#95;2, \vec x&#95;3, \vec x&#95;4, \vec x&#95;5, \vec x&#95;6\\)</span> are 6 vectors in <span class="math-inline">\\(\mathbb{R}^9\\)</span> such that

<div class="math-display">
$$
S = \text{span}\left(\{\vec x_1, \vec x_2, \vec x_3, \vec x_4, \vec x_5, \vec x_6\}\right)
$$
</div>

 is a **4-dimensional** subspace of <span class="math-inline">\\(\mathbb{R}^9\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">2 pts</span> True or False: The set <span class="math-inline">\\(\lbrace\vec x&#95;1, \vec x&#95;2, \vec x&#95;3, \vec x&#95;4, \vec x&#95;5, \vec x&#95;6\rbrace\\)</span> is linearly independent.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> False</span></div>

This is false.

If these vectors were linearly independent, they would span a 6-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^9\\)</span>; since they only span a 4-dimensional subspace, they must be linearly dependent, and two of them are "redundant".
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Consider the statement:

"There exists a vector <span class="math-inline">\\(\vec b \in \mathbb{R}^9\\)</span> such that the number of ways to write <span class="math-inline">\\(\vec b\\)</span> as a linear combination of <span class="math-inline">\\(\vec x&#95;1, \ldots, \vec x&#95;6\\)</span> is ."

In each part below, a possible way to fill in the blank is given. Determine whether the statement that results from filling in the blank is **True** or **False**.

1.  zero

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

2.  exactly one

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

3.  exactly two

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

4.  infinite

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

-   **(True) zero ways**: <span class="math-inline">\\(S\\)</span>, the set of all linear combinations of <span class="math-inline">\\(\vec x&#95;1, \ldots, \vec x&#95;6\\)</span>, is a 4-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^9\\)</span>. Since <span class="math-inline">\\(S\\)</span> isn't all of <span class="math-inline">\\(\mathbb{R}^9\\)</span>, there are plenty of vectors <span class="math-inline">\\(\vec b \in \mathbb{R}^9\\)</span> that are not in <span class="math-inline">\\(S\\)</span>, and therefore can't be written as a linear combination of <span class="math-inline">\\(\vec x&#95;1, \ldots, \vec x&#95;6\\)</span>. So, it's true that there are some <span class="math-inline">\\(\vec b\\)</span>'s such that there are zero ways to write <span class="math-inline">\\(\vec b\\)</span> as a linear combination of <span class="math-inline">\\(\vec x&#95;1, \ldots, \vec x&#95;6\\)</span>.

-   **(False) exactly one way**: Linear combinations are only unique if the spanning vectors are linearly independent. Since <span class="math-inline">\\(\vec x&#95;1, \ldots, \vec x&#95;6\\)</span> are linearly dependent, there is a non-trivial linear combination of them that equals the zero vector, which could be added to any other existing linear combination that sums to <span class="math-inline">\\(\vec b\\)</span> to "invent" a new, different-looking linear combination that sums to <span class="math-inline">\\(\vec b\\)</span>. So, it's false that there is exactly one way to write <span class="math-inline">\\(\vec b\\)</span> as a linear combination of <span class="math-inline">\\(\vec x&#95;1, \ldots, \vec x&#95;6\\)</span> --- if there is one way, there are infinitely many.

-   **(False) exactly two ways**: Same logic as above. If this thinking is a bit confusing, see the solution to part **c)**.

-   **(True) infinite ways**: For any vector <span class="math-inline">\\(\vec b \in S\\)</span>, there are infinitely many ways to write <span class="math-inline">\\(\vec b\\)</span> as a linear combination of <span class="math-inline">\\(\vec x&#95;1, \ldots, \vec x&#95;6\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Suppose <span class="math-inline">\\(\vec b\\)</span> is some vector in <span class="math-inline">\\(S\\)</span> such that both of the following equations are true:

<div class="math-display">
$$

$$
</div>

\begin{aligned}
\vec b &= 4 \vec x_1 - 2 \vec x_2 + 6 \vec x_3

\vec b &= 3 \vec x_1 + 3 \vec x_3 - \vec x_5
\end{aligned}

<div class="math-display">
$$

$$
</div>

State **one** other linear combination of <span class="math-inline">\\(\vec x&#95;1, \ldots, \vec x&#95;6\\)</span> that is equal to <span class="math-inline">\\(\vec b\\)</span>. Fill in each box with a number with no variables.

<span class="math-inline">\\(\vec b = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;  \vec x&#95;1 + \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;  \vec x&#95;2 + \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;  \vec x&#95;3 + \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;  \vec x&#95;4 + \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;  \vec x&#95;5 + \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;  \vec x&#95;6\\)</span>

<details markdown="1"><summary>Solution</summary>

Arguably, answering part **c)** may have helped clarify the answer to part **b)**.

Let's try adding the two representation of <span class="math-inline">\\(\vec b\\)</span> together.

<div class="math-display">
$$

$$
</div>

\begin{aligned}
\vec b &= 4 \vec x_1 - 2 \vec x_2 + 6 \vec x_3

\vec b &= 3 \vec x_1 + 3 \vec x_3 - \vec x_5

\implies 2 \vec b &= 7 \vec x_1 - 2 \vec x_2 + 9 \vec x_3 - \vec x_5
\end{aligned}

<div class="math-display">
$$

$$
</div>

Dividing both sides by 2 gives us

<div class="math-display">
$$
\boxed{\vec b = \frac{7}{2} \vec x_1 - \vec x_2 + \frac{9}{2} \vec x_3 - \frac{1}{2} \vec x_5}
$$
</div>

This is not the only possible answer, but it's probably the easiest one. For example, you could repeat this process with one of the original two <span class="math-inline">\\(\vec b\\)</span>'s along with the new representation of <span class="math-inline">\\(\vec b\\)</span> to get another valid representation of <span class="math-inline">\\(\vec b\\)</span>.

You also could have subtracted the two representations of <span class="math-inline">\\(\vec b\\)</span> to get a linear combination of <span class="math-inline">\\(\vec x&#95;1, \ldots, \vec x&#95;6\\)</span> that equals the zero vector, which could be added to any other existing linear combination that sums to <span class="math-inline">\\(\vec b\\)</span> to "invent" a new, different-looking linear combination that sums to <span class="math-inline">\\(\vec b\\)</span> (as we said in the solution to part **b)**). If you did this, you'd find that

<div class="math-display">
$$
\vec 0 = \vec x_1 - 2 \vec x_2 + 3 \vec x_3 + \vec x_5
$$
</div>

This must mean that

<div class="math-display">
$$
\vec b + \vec 0 = (4 \vec x_1 - 2 \vec x_2 + 6 \vec x_3) + (\vec x_1 - 2 \vec x_2 + 3 \vec x_3 + \vec x_5) = 5 \vec x_1 - 4 \vec x_2 + 9 \vec x_3 + \vec x_5
$$
</div>

is another way to represent <span class="math-inline">\\(\vec b\\)</span> as a linear combination of <span class="math-inline">\\(\vec x&#95;1, \ldots, \vec x&#95;6\\)</span>,

and so is

<div class="math-display">
$$
\vec b + 245 (\vec 0) = (4 \vec x_1 - 2 \vec x_2 + 6 \vec x_3) + 245(\vec x_1 - 2 \vec x_2 + 3 \vec x_3 + \vec x_5)
$$
</div>

(for instance).
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Let <span class="math-inline">\\(T = \text{span}(\lbrace \vec x&#95;1, \vec x&#95;2, \vec x&#95;3 \rbrace)\\)</span> and <span class="math-inline">\\(U = \text{span}(\lbrace \vec x&#95;4, \vec x&#95;5, \vec x&#95;6 \rbrace)\\)</span>. Suppose <span class="math-inline">\\(W\\)</span> is the **intersection** of <span class="math-inline">\\(T\\)</span> and <span class="math-inline">\\(U\\)</span>, i.e. <span class="math-inline">\\(W = T \cap U\\)</span>. <span class="math-inline">\\(W\\)</span> is also a subspace of <span class="math-inline">\\(\mathbb{R}^9\\)</span>.

What are the smallest and largest possible values of <span class="math-inline">\\(\text{dim}(W)\\)</span>, the dimension of <span class="math-inline">\\(W\\)</span>? Give your answers as integers.

<span class="math-inline">\\(=\\)</span> \_\_\_\_\_\_ <span class="math-inline">\\(=\\)</span> \_\_\_\_\_\_

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(T\\)</span> and <span class="math-inline">\\(U\\)</span> are each individually at most 3-dimensional, since they are each spanned by 3 vectors. So, the intersection <span class="math-inline">\\(W\\)</span> must be at most 3-dimensional. This means the possible dimensions to consider are 3, 2, 1, or 0. Let's reason about them, starting with 3.

To give examples, we'll use the standard basis vectors <span class="math-inline">\\(\vec e&#95;1, \vec e&#95;2, \ldots, \vec e&#95;9\\)</span> of <span class="math-inline">\\(\mathbb{R}^9\\)</span>. In <span class="math-inline">\\(\mathbb{R}^2\\)</span>, <span class="math-inline">\\(\vec e&#95;1 = \begin{bmatrix} 1 \\\\ 0 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec e&#95;2 = \begin{bmatrix} 0 \\\\ 1 \end{bmatrix}\\)</span>, so (for instance) in <span class="math-inline">\\(\mathbb{R}^9\\)</span>,

<div class="math-display">
$$
\vec e_5 = \begin{bmatrix} 0 \\\\ 0 \\\\ 0 \\\\ 0 \\\\ 1 \\\\ 0 \\\\ 0 \\\\ 0 \\\\ 0 \end{bmatrix}
$$
</div>

-   Could <span class="math-inline">\\(\text{dim}(W) = 3\\)</span>? **No**. If <span class="math-inline">\\(\text{dim}(W) = 3\\)</span>, it would mean that <span class="math-inline">\\(T\\)</span> and <span class="math-inline">\\(U\\)</span> are both **the same** 3-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^9\\)</span>, and intersect everywhere. But if that were the case, then <span class="math-inline">\\(S = \text{span}(\lbrace \vec x&#95;1, \vec x&#95;2, \vec x&#95;3, \vec x&#95;4, \vec x&#95;5, \vec x&#95;6 \rbrace)\\)</span> would be a 3-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^9\\)</span>, which contradicts the problem statement that <span class="math-inline">\\(S\\)</span> is a 4-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^9\\)</span>. So, <span class="math-inline">\\(\text{dim}(W) &lt; 3\\)</span>, and the maximum possible value is something less than 3.

-   Could <span class="math-inline">\\(\text{dim}(W) = 2\\)</span>? **Yes**, and all smaller values are also possible. <span class="math-inline">\\(T\\)</span> and <span class="math-inline">\\(U\\)</span> could overlap in a 2-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^9\\)</span>, while each containing a direction that the other doesn't.

   For example, <span class="math-inline">\\(T\\)</span> could be the span of <span class="math-inline">\\(\lbrace\vec e&#95;1, \vec e&#95;2, \vec e&#95;3\rbrace\\)</span> and <span class="math-inline">\\(U\\)</span> could be the span of <span class="math-inline">\\(\lbrace\vec e&#95;2, \vec e&#95;3, \vec e&#95;4\rbrace\\)</span>. In this case, <span class="math-inline">\\(W\\)</span> would be the span of <span class="math-inline">\\(\lbrace\vec e&#95;2, \vec e&#95;3\rbrace\\)</span>, which is a 2-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^9\\)</span>.

-   Could <span class="math-inline">\\(\text{dim}(W) = 1\\)</span>? **Yes**. For example, <span class="math-inline">\\(T\\)</span> could be the span of <span class="math-inline">\\(\lbrace\vec e&#95;1, \vec e&#95;2\rbrace\\)</span> and <span class="math-inline">\\(U\\)</span> could be the span of <span class="math-inline">\\(\lbrace\vec e&#95;2, \vec e&#95;3, \vec e&#95;4 \rbrace\\)</span>. In this case, <span class="math-inline">\\(W\\)</span> would be the span of <span class="math-inline">\\(\lbrace\vec e&#95;2\rbrace\\)</span>, which is 1-dimensional, while <span class="math-inline">\\(S\\)</span> would still be 4-dimensional. (In this example, we said that <span class="math-inline">\\(T\\)</span> is the span of <span class="math-inline">\\(\vec e&#95;1\\)</span> and <span class="math-inline">\\(\vec e&#95;2\\)</span> though we defined it in the problem statement to be the span of three vectors. No problem --- just pick the third vector to be a linear combination of <span class="math-inline">\\(\vec e&#95;1\\)</span> and <span class="math-inline">\\(\vec e&#95;2\\)</span>. That is, <span class="math-inline">\\(\vec x&#95;1 = \vec e&#95;1\\)</span>, <span class="math-inline">\\(\vec x&#95;2 = \vec e&#95;2\\)</span>, and <span class="math-inline">\\(\vec x&#95;3 = \vec e&#95;1 + \vec e&#95;2\\)</span> would work as an example.)

-   Could <span class="math-inline">\\(\text{dim}(W) = 0\\)</span>? **Yes**. <span class="math-inline">\\(T\\)</span> and <span class="math-inline">\\(U\\)</span> could be two completely disjoint subspaces, except for <span class="math-inline">\\(\vec 0\\)</span>, which is in every subspace.

   For example, let <span class="math-inline">\\(\vec x&#95;1 = \vec e&#95;1\\)</span>, <span class="math-inline">\\(\vec x&#95;2 = \vec e&#95;2\\)</span>, <span class="math-inline">\\(\vec x&#95;3 = \vec e&#95;1 + \vec e&#95;2\\)</span>, which makes <span class="math-inline">\\(T\\)</span> a 2-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^9\\)</span>, and <span class="math-inline">\\(\vec x&#95;4 = \vec e&#95;3\\)</span>, <span class="math-inline">\\(\vec x&#95;5 = \vec e&#95;4\\)</span>, <span class="math-inline">\\(\vec x&#95;6 = \vec e&#95;3 + \vec e&#95;4\\)</span>, which makes <span class="math-inline">\\(U\\)</span> a 2-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^9\\)</span>. In this case, <span class="math-inline">\\(W\\)</span> would be the set <span class="math-inline">\\(\lbrace\vec 0\rbrace\\)</span>, while <span class="math-inline">\\(S\\)</span> would still be 4-dimensional.

So, the smallest possible value of <span class="math-inline">\\(\text{dim}(W)\\)</span> is <span class="math-inline">\\(\boxed{0}\\)</span>, and the largest possible value is <span class="math-inline">\\(\boxed{2}\\)</span>.
</details>

</div>
</div>

</div>
