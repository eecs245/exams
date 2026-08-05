---
number: 8
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> <span class="badge" data-flag="mt2-redemption" style="background-color: #9A3324; color: #FFFFFF; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">MT2 Redemption</span>
points: 6
flags: [mt2-redemption]
has_solution: true
images: []
---

Suppose we fit a multiple linear regression model **with** an intercept term that predicts the `height` of a wolverine given its `weight` and `color`. The model is fit by minimizing mean squared error.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">2 pts</span> If we one hot encode the color feature **without** dropping any categories, the design matrix <span class="math-inline">\\(X\\)</span> has 6 columns.

How many unique `color`s are there? Give your answer as an integer with no variables.

There are <span class="math-inline">\\(\&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span> unique `color`s.

<details markdown="1"><summary>Solution</summary>

The 6 columns are:

-   1 intercept column

-   1 `weight` column

-   1 column for each color after one hot encoding without dropping any categories

So the number of unique colors is 

<div class="math-display">
$$
6 - 2 = \boxed{4}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Assume that not all wolverines in the dataset have the same `weight`, and that there is at least one wolverine with each color.

What impact would dropping one of the color categories' columns from the design matrix <span class="math-inline">\\(X\\)</span> have? **Select all that apply.**

<span class="mc-square" aria-hidden="true"></span> It would decrease the rank of <span class="math-inline">\\(X\\)</span>.

<span class="mc-square" aria-hidden="true"></span> It would guarantee that <span class="math-inline">\\(X\\)</span> invertible.

<span class="mc-square" aria-hidden="true"></span> It would guarantee that <span class="math-inline">\\(X^TX\\)</span> invertible.

<span class="mc-square" aria-hidden="true"></span> It would guarantee the existence of a unique optimal parameter vector <span class="math-inline">\\(\vec w^{\ast}\\)</span>.

<span class="mc-square" aria-hidden="true"></span> It would change <span class="math-inline">\\(\text{nullsp}(X)\\)</span>.

<span class="mc-square" aria-hidden="true"></span> It would change <span class="math-inline">\\(\text{colsp}(X)\\)</span>.

<details markdown="1"><summary>Solution</summary>

<span class="mc-square" aria-hidden="true"></span> It would change <span class="math-inline">\\(\text{colsp}(X)\\)</span>.

By dropping one of the color categories' columns from the design matrix <span class="math-inline">\\(X\\)</span>, we guarantee that the columns of <span class="math-inline">\\(X\\)</span> are linearly independent. As discussed in the course notes, when one hot encoding, the sum of all 4 color columns is equal to the intercept column (of all ones); by dropping one of the 4 color columns, we don't lose any information but remove the linear dependence. (The other assumptions in the problem help guarantee this, too --- for instance, if all of the wolverines in the dataset have the same `weight`, then the `weight` column is a scalar multiple of the intercept column.)

With that in mind, let's look at the options:

-   It would decrease the rank of <span class="math-inline">\\(X\\)</span>. **False**: <span class="math-inline">\\(\text{colsp}(X)\\)</span> doesn't change, so <span class="math-inline">\\(\text{rank}(X)\\)</span> doesn't change.

-   It would guarantee that <span class="math-inline">\\(X\\)</span> is invertible. **False**: <span class="math-inline">\\(X\\)</span> is not necessarily square!

-   It would guarantee that <span class="math-inline">\\(X^TX\\)</span> is invertible. **True**: If <span class="math-inline">\\(X\\)</span>'s columns are linearly independent, then <span class="math-inline">\\(X^TX\\)</span> is invertible, since <span class="math-inline">\\(\text{rank}(X) = \text{rank}(X^TX) = \text{\# columns in } X^TX\\)</span>.

-   It would gaurantee the existence of a unique optimal parameter vector <span class="math-inline">\\(\vec w^{\ast}\\)</span>. **True**: If <span class="math-inline">\\(X\\)</span>'s columns are linearly independent, there is a unique <span class="math-inline">\\(\vec w^{\ast}\\)</span>.

-   It would change <span class="math-inline">\\(\text{nullsp}(X)\\)</span>: **True**. With the redundant column, <span class="math-inline">\\(X\\)</span> has a non-trivial null space, but without it, <span class="math-inline">\\(X\\)</span>'s null space is <span class="math-inline">\\(\lbrace \vec 0 \rbrace\\)</span>.

-   It would change <span class="math-inline">\\(\text{colsp}(X)\\)</span>: **False**, as discussed above.
</details>

</div>
</div>

</div>
