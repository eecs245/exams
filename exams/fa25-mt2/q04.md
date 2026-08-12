---
number: 4
title: Poly Wants a Cracker
heading_suffix: : Poly Wants a Cracker <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">18 pts</span>
points: 18
flags: []
has_solution: true
images: []
---

Suppose we'd like to fit the model <span class="math-inline">\\(\boxed{h(x&#95;i) = w&#95;0 + w&#95;1 x&#95;i + w&#95;2 x&#95;i^2}\\)</span> by minimizing mean squared error. We use an observation vector <span class="math-inline">\\(\vec y \in \mathbb{R}^n\\)</span>, but instead of using the regular design matrix <span class="math-inline">\\(X\\)</span>,

<div class="math-display">
$$
X = \begin{bmatrix} 1 & x_1 & x_1^2 \\\\ 1 & x_2 & x_2^2 \\\\ \vdots & \vdots & \vdots \\\\ 1 & x_n & x_n^2 \end{bmatrix} = \begin{bmatrix} | & | & | \\\\ \vec x^{(0)} & \vec x^{(1)} & \vec x^{(2)} \\\\ | & | & | \end{bmatrix}
$$
</div>

we use the **centered** design matrix <span class="math-inline">\\(Z\\)</span> (where <span class="math-inline">\\(\bar{x} = \frac{1}{n} \sum&#95;{i=1}^n x&#95;i\\)</span> is the mean of the <span class="math-inline">\\(x\\)</span>'s).

<div class="math-display">
$$
Z = \begin{bmatrix} 1 & x_1 - \bar{x} & (x_1 - \bar{x})^2 \\\\ 1 & x_2 - \bar{x} & (x_2 - \bar{x})^2 \\\\ \vdots & \vdots & \vdots \\\\ 1 & x_n - \bar{x} & (x_n - \bar{x})^2 \end{bmatrix} = \begin{bmatrix} | & | & | \\\\ \vec z^{(0)} & \vec z^{(1)} & \vec z^{(2)} \\\\ | & | & | \end{bmatrix}
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> It turns out that <span class="math-inline">\\(\text{colsp}(Z) = \text{colsp}(X)\\)</span>. To show this, fill in the blanks below to express <span class="math-inline">\\(\vec z^{(2)}\\)</span> (the third column of <span class="math-inline">\\(Z\\)</span>) as a linear combination of <span class="math-inline">\\(X\\)</span>'s columns. Each box should be filled with an expression involving <span class="math-inline">\\(\bar{x}\\)</span>, <span class="math-inline">\\(n\\)</span>, and/or constants.

<div class="math-display">
$$
\vec z^{(2)} = \_\_\_\_\_\_ \: \begin{bmatrix} 1 \\\\ 1 \\\\ \vdots \\\\ 1 \end{bmatrix} + \_\_\_\_\_\_ \: \begin{bmatrix} x_1 \\\\ x_2 \\\\ \vdots \\\\ x_n \end{bmatrix} + \_\_\_\_\_\_ \: \begin{bmatrix} x_1^2 \\\\ x_2^2 \\\\ \vdots \\\\ x_n^2 \end{bmatrix}
$$
</div>

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(\vec z^{(2)}\\)</span> is the column made up of terms of the form <span class="math-inline">\\((x&#95;i - \bar x)^2\\)</span>. Note that

<div class="math-display">
$$
(x_i - \bar x)^2=x_i^2 -2\bar x x_i + \bar x^2 = ({\bar x}^2)(1) + (-2\bar x)(x_i) + (1)(x_i^2)
$$
</div>

which tells us that

<div class="math-display">
$$
\vec z^{(2)} = \bar{x}^2 \begin{bmatrix} 1 \\\\ 1 \\\\ \vdots \\\\ 1 \end{bmatrix} -2\bar{x} \begin{bmatrix} x_1 \\\\ x_2 \\\\ \vdots \\\\ x_n \end{bmatrix} + \begin{bmatrix} x_1^2 \\\\ x_2^2 \\\\ \vdots \\\\ x_n^2 \end{bmatrix}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
(6 pts) In this part only, assume that the values <span class="math-inline">\\(x&#95;1, x&#95;2, ..., x&#95;n\\)</span> are each either 1 or 0. For some specific values <span class="math-inline">\\(x&#95;1, x&#95;2, ..., x&#95;n\\)</span>, the matrix <span class="math-inline">\\(P\\)</span> that projects vectors in <span class="math-inline">\\(\mathbb{R}^n\\)</span> onto <span class="math-inline">\\(\text{colsp}(Z)\\)</span> is given by

<div class="math-display">
$$
P = \begin{bmatrix}
1/3 & 1/3 & 0      & 1/3 & 0      \\\\
1/3 & 1/3 & 0      & 1/3 & 0      \\\\
0      & 0      & 1/2    & 0      & 1/2    \\\\
1/3 & 1/3 & 0      & 1/3 & 0      \\\\
0      & 0      & 1/2    & 0      & 1/2
\end{bmatrix}
$$
</div>

1.  What is the rank of <span class="math-inline">\\(Z\\)</span>? Give your answer as an integer. <span class="math-inline">\\(\text{rank}(Z) = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>

2.  Which specific values of <span class="math-inline">\\(x&#95;1, x&#95;2, ..., x&#95;n\\)</span> result in <span class="math-inline">\\(P\\)</span> being the matrix above? Give your answer as a list of values, in the order <span class="math-inline">\\(x&#95;1\\)</span>, then <span class="math-inline">\\(x&#95;2\\)</span>, then <span class="math-inline">\\(x&#95;3\\)</span>, etc. (If there are multiple possible answers, just give one.)

<details markdown="1"><summary>Solution</summary>

First, <span class="math-inline">\\(\text{rank}(Z) = 2\\)</span>. We're told in part **a)** that <span class="math-inline">\\(\text{colsp}(Z) = \text{colsp}(X)\\)</span>, so <span class="math-inline">\\(\text{rank}(Z) = \text{rank}(X)\\)</span>. I find it easier to think in terms of <span class="math-inline">\\(X\\)</span> since the numbers are more straightforward.

**Remember, throughout this part, that each <span class="math-inline">\\(x&#95;i\\)</span> is either 1 or 0!** This means that the column <span class="math-inline">\\(\vec x^{(1)} = \begin{bmatrix} x&#95;1 \\\\ x&#95;2 \\\\ \vdots \\\\ x&#95;n \end{bmatrix}\\)</span> is made up of 1's and 0's, and the column <span class="math-inline">\\(\vec x^{(2)} = \begin{bmatrix} x&#95;1^2 \\\\ x&#95;2^2 \\\\ \vdots \\\\ x&#95;n^2 \end{bmatrix}\\)</span> is made up of 1's and 0's in the same positions, since <span class="math-inline">\\(1^2 = 1\\)</span> and <span class="math-inline">\\(0^2 = 0\\)</span>.

So, <span class="math-inline">\\(X\\)</span> only really has two unique columns, and its rank is 2. But since <span class="math-inline">\\(\text{rank}(Z) = \text{rank}(X)\\)</span>, we have <span class="math-inline">\\(\text{rank}(Z) = 2\\)</span>. <span class="math-inline">\\(Z\\)</span> doesn't have any repeated columns, but as we showed above, it's still the case that one of <span class="math-inline">\\(Z\\)</span>'s columns is a linear combination of the other two.

The only case in which <span class="math-inline">\\(\text{rank}(Z) = 1\\)</span> is if all of the <span class="math-inline">\\(x&#95;i\\)</span> are the same, but the matrix <span class="math-inline">\\(P\\)</span> tells us that that is not the case.

Let's now look at the matrix <span class="math-inline">\\(P\\)</span>. Notice that rows 1, 2, and 4 of <span class="math-inline">\\(P\\)</span> are identical, as are rows 3 and 5. Let's imagine some vector <span class="math-inline">\\(\vec y \in \mathbb{R}^5\\)</span>. What would multiplying <span class="math-inline">\\(P\\)</span> by <span class="math-inline">\\(\vec y\\)</span> give us?

<div class="math-display">
$$
P \vec y = \begin{bmatrix} 1/3 & 1/3 & 0      & 1/3 & 0      \\\\
1/3 & 1/3 & 0      & 1/3 & 0      \\\\
0      & 0      & 1/2    & 0      & 1/2    \\\\
1/3 & 1/3 & 0      & 1/3 & 0      \\\\
0      & 0      & 1/2    & 0      & 1/2
\end{bmatrix} \begin{bmatrix} y_1 \\\\ y_2 \\\\ y_3 \\\\ y_4 \\\\ y_5 \end{bmatrix} = \begin{bmatrix} \frac{1}{3}y_1 + \frac{1}{3}y_2 + \frac{1}{3}y_4 \\\\ \frac{1}{3}y_1 + \frac{1}{3}y_2 + \frac{1}{3}y_4 \\\\ \frac{1}{2}y_3 + \frac{1}{2}y_5 \\\\ \frac{1}{3}y_1 + \frac{1}{3}y_2 + \frac{1}{3}y_4 \\\\ \frac{1}{2}y_3 + \frac{1}{2}y_5 \end{bmatrix} = \begin{bmatrix} \text{mean of } y_1, y_2, y_4 \\\\ \text{mean of } y_1, y_2, y_4 \\\\ \text{mean of } y_3, y_5 \\\\ \text{mean of } y_1, y_2, y_4 \\\\ \text{mean of } y_3, y_5 \end{bmatrix}
$$
</div>

We know from Chapter 1 that the mean is the constant that minimizes mean squared error. Here, it appears that the prediction returned in <span class="math-inline">\\(\vec y\\)</span> is not always the same, but is one of two possibilities --- rows 1, 2, and 4 have the same prediction, and rows 3 and 5 have the same prediction. This hints to us that rows 1, 2, and 4 come from the same <span class="math-inline">\\(x&#95;i\\)</span> value, and rows 3 and 5 come from the same <span class="math-inline">\\(x&#95;i\\)</span> value, and the optimal prediction is some **conditional** mean. This resembles [Lab 9, Activity 2](https://eecs245.org/resources/labs/lab09/lab09-solutions.pdf#page=3), on one hot encoding with beef, chicken, and fish.

The above observation alone is enough information to answer the question. The two possible answers are <span class="math-inline">\\(\boxed{x&#95;1 = 1, x&#95;2 = 1, x&#95;3 = 0, x&#95;4 = 1, x&#95;5 = 0}\\)</span> and <span class="math-inline">\\(\boxed{x&#95;1 = 0, x&#95;2 = 0, x&#95;3 = 1, x&#95;4 = 0, x&#95;5 = 1}\\)</span>.

Let's dive deeper into the math to confirm this. Let's start with what <span class="math-inline">\\(X\\)</span> would have had to be. (We can work with <span class="math-inline">\\(X\\)</span> instead of <span class="math-inline">\\(Z\\)</span> since both have the same column spaces, so projecting onto either column space will give us the same result; <span class="math-inline">\\(X\\)</span> is just easier to work with.) And, let's drop <span class="math-inline">\\(\vec x^{(2)}\\)</span> from <span class="math-inline">\\(X\\)</span>, since including it will prevent <span class="math-inline">\\(X^TX\\)</span> from being invertible while not changing <span class="math-inline">\\(\text{colsp}(X)\\)</span>.

<div class="math-display">
$$
X = \begin{bmatrix} 1 & 1 \\\\ 1 & 1 \\\\ 1 & 0 \\\\ 1 & 1 \\\\ 1 & 0 \end{bmatrix}
$$
</div>

Note that I arbitrarily picked <span class="math-inline">\\(x&#95;1 = x&#95;2 = x&#95;4 = 1\\)</span> and <span class="math-inline">\\(x&#95;3 = x&#95;5 = 0\\)</span>, but we could reverse the 1's and 0's and <span class="math-inline">\\(P\\)</span> would turn out to be the same.

The formula for the projection matrix is <span class="math-inline">\\(P = X (X^TX)^{-1}X^T\\)</span>. I won't include all of the algebra here, but if you work out <span class="math-inline">\\(P = X (X^TX)^{-1}X^T\\)</span>, you'll find that <span class="math-inline">\\(P\\)</span> is indeed the matrix provided in the problem.

Here's one final interpretation of what's going on. Suppose the optimal parameters for this <span class="math-inline">\\(X\\)</span> and some <span class="math-inline">\\(\vec y\\)</span> are <span class="math-inline">\\(\vec w^{\ast} = \begin{bmatrix} w&#95;0^{\ast} \\\\ w&#95;1^{\ast} \end{bmatrix}\\)</span>, which would lead to a hypothesis function of

<div class="math-display">
$$
h(x_i) = w_0^* + w_1^* x_i
$$
</div>

This hypothesis function only returns one of two values:

-   If <span class="math-inline">\\(x&#95;i = 1\\)</span>, then <span class="math-inline">\\(h(1) = w&#95;0^{\ast} + w&#95;1^{\ast}\\)</span>

-   If <span class="math-inline">\\(x&#95;i = 0\\)</span>, then <span class="math-inline">\\(h(0) = w&#95;0^{\ast}\\)</span>

So, <span class="math-inline">\\(w&#95;0^{\ast}\\)</span> is the mean of the <span class="math-inline">\\(y\\)</span>'s when <span class="math-inline">\\(x&#95;i = 0\\)</span>, and <span class="math-inline">\\(w&#95;0^{\ast} + w&#95;1^{\ast}\\)</span> is the mean of the <span class="math-inline">\\(y\\)</span>'s when <span class="math-inline">\\(x&#95;i = 1\\)</span>. This is exactly what we see in the matrix <span class="math-inline">\\(P\\)</span>.
</details>

Recall, <span class="math-inline">\\(Z = \begin{bmatrix} 1 &amp; x&#95;1 - \bar{x} &amp; (x&#95;1 - \bar{x})^2 \\\\ 1 &amp; x&#95;2 - \bar{x} &amp; (x&#95;2 - \bar{x})^2 \\\\ \vdots &amp; \vdots &amp; \vdots \\\\ 1 &amp; x&#95;n - \bar{x} &amp; (x&#95;n - \bar{x})^2 \end{bmatrix} = \begin{bmatrix} | &amp; | &amp; | \\\\ \vec z^{(0)} &amp; \vec z^{(1)} &amp; \vec z^{(2)} \\\\ | &amp; | &amp; | \end{bmatrix}\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Let <span class="math-inline">\\(\vec \beta^{\ast} = \begin{bmatrix} \beta&#95;0^{\ast} \\\\ \beta&#95;1^{\ast} \\\\ \beta&#95;2^{\ast} \end{bmatrix}\\)</span> be a solution to the normal equations for <span class="math-inline">\\(Z\\)</span> and <span class="math-inline">\\(\vec y\\)</span>. Show that

<div class="math-display">
$$
\beta_0^* = \bar{y} - \beta_2^* \sigma_x^2
$$
</div>

where <span class="math-inline">\\(\sigma&#95;x^2 = \frac{1}{n} \sum&#95;{i=1}^n (x&#95;i - \bar{x})^2\\)</span> is the variance of the <span class="math-inline">\\(x\\)</span>'s, and <span class="math-inline">\\(\bar{y}\\)</span> is the mean of the <span class="math-inline">\\(y\\)</span>'s. <em>Hint: Use the fact that <span class="math-inline">\\(\sum&#95;{i = 1}^n (x&#95;i - \bar{x}) = 0\\)</span>. What is the error vector? Is it orthogonal to something useful?</em>

<details markdown="1"><summary>Solution</summary>

The error vector is <span class="math-inline">\\(\vec e = \vec y - Z\vec \beta^{\ast}\\)</span>. As we studied in depth, the error vector is orthogonal to every vector in <span class="math-inline">\\(\text{colsp}(Z)\\)</span>, i.e. every linear combination of the columns of <span class="math-inline">\\(Z\\)</span>. <span class="math-inline">\\(Z\\)</span> has a column of all 1's, so the error vector is orthogonal to that, too.

<div class="math-display">
$$
(\vec y - Z\vec \beta^*) \cdot \vec 1 = 0
$$
</div>

 We'll proceed by expanding <span class="math-inline">\\(Z \vec \beta^{\ast}\\)</span> and then plugging the result into the above. This will allow us to solve for <span class="math-inline">\\(\beta^{\ast}&#95;0\\)</span>.

<div class="math-display">
$$
\begin{align*}
Z\vec \beta^* &= \beta_0^*\vec z^{(0)} + \beta_1^*\vec z^{(1)} + \beta_2^*\vec z^{(2)}
\\\\ &= \beta_0^*\begin{bmatrix} 1 \\\\ 1 \\\\ \vdots \\\\ 1  \end{bmatrix} +  \beta_1^*\begin{bmatrix} x_1 - \bar x_1 \\\\ x_2 - \bar x_2 \\\\ \vdots \\\\ x_n - \bar x_n\end{bmatrix} + \beta_2^*\begin{bmatrix} (x_1 - \bar x_1)^2 \\\\ (x_2 - \bar x_2)^2 \\\\ \vdots \\\\ (x_n - \bar x_n)^2\end{bmatrix}
\\\\ &= \begin{bmatrix} \beta_0^* + \beta_1^*(x_1 - \bar x_1) + \beta_2^*(x_1 - \bar x_1)^2 \\\\ \beta_0^* + \beta_1^*(x_2 - \bar x_2)+ \beta_2^*(x_2 - \bar x_2)^2\\\\ \vdots \\\\ \beta_0^* + \beta_1^*(x_n - \bar x_n) + \beta_2^*(x_n - \bar x_n)^2\end{bmatrix}
\end{align*}
$$
</div>

<div class="math-display">
$$
\begin{align*}
(\vec y - Z\vec \beta^*) \cdot \vec 1 &= 0
\\\\ \sum_{i=1}^{n}\left[y_i - (Z\vec \beta^*)_i\right] &= 0
\\\\ \sum_{i=1}^{n}\left[y_i - \beta_0^* - \beta_1^*(x_i - \bar x_i) - \beta_2^*(x_i - \bar x_i)^2\right] &= 0
\\\\ \underbrace{\sum_{i=1}^{n}y_i}_{n \bar{y}} - \underbrace{\sum_{i=1}^{n}\beta_0^*}_{\text{sum of constant}} - \underbrace{\sum_{i=1}^{n}\beta_1^*(x_i - \bar x_i)}_{0} - \sum_{i=1}^{n}\beta_2^*(x_i - \bar x_i)^2 &= 0
\\\\ n\bar y - n\beta_0^* - n\beta_2^*\sigma_x^2 &= 0
\\\\ n\beta_0^* &= n\bar y - n\beta_2^*\sigma_x^2
\\\\ \beta_0^* &= \boxed{\bar y - \beta_2^*\sigma_x^2}
\end{align*}
$$
</div>

</details>

</div>
</div>

</div>
