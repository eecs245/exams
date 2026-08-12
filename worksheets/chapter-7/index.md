---
layout: minimal
title: "Chapter 7: Regression Using Linear Algebra"
description: "Practice problems for Chapter 7: Regression Using Linear Algebra."
nav_exclude: true
hide_footer_hr: true
---

{% raw %}

<script>
window.MathJax = {
  tex: {inlineMath: [['$', '$'], ['\\(', '\\)']]}
};
</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js" async></script>

<style>
.main-content p {
  margin-bottom: 1.15em;
}
.assignment-pdf-button {
  font-size: 0.95rem;
  padding: 0.35rem 0.65rem;
}
.assignment-actions {
  align-items: center;
  display: flex;
  flex-wrap: wrap;
  gap: 0.55rem;
  margin: 0 0 1rem;
}
.math-display,
mjx-container[jax="CHTML"][display="true"] {
  max-width: 100%;
  overflow-x: auto;
  overflow-y: hidden;
}
.math-display {
  padding-bottom: 0.2rem;
}
.math-display mjx-container[jax="CHTML"][display="true"] {
  padding-bottom: 0.2rem;
}
.answer-blank {
  border-bottom: 1px solid currentColor;
  display: inline-block;
  min-width: 8rem;
  height: 1em;
  vertical-align: baseline;
}
.assignment-parts {
  margin: 1rem 0;
}
.assignment-part {
  column-gap: 0.55rem;
  display: grid;
  grid-template-columns: 1.4rem minmax(0, 1fr);
  margin-bottom: 1.05rem;
}
.assignment-part-label {
  font-weight: 600;
  text-align: right;
}
.assignment-part-content > :first-child {
  margin-top: 0;
}
.mc-options {
  display: flex;
  flex-wrap: wrap;
  gap: 0.9rem 1.6rem;
  margin: 0.9rem 0 1.1rem;
}
.mc-option {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  white-space: nowrap;
}
.mc-bubble,
.mc-square {
  display: inline-block;
  flex: 0 0 auto;
  height: 0.95em;
  width: 0.95em;
  vertical-align: -0.12em;
}
.mc-bubble {
  border: 1.5px solid currentColor;
  border-radius: 50%;
}
.mc-square {
  border: 1.5px solid currentColor;
}
.mc-correct {
  background: currentColor;
}
.main-content table {
  font-size: 0.9rem;
  width: auto;
  max-width: 100%;
}
.main-content table th,
.main-content table td {
  padding: 0.35rem 0.5rem;
  white-space: nowrap;
}
</style>

<style>
.worksheet-source { font-size: 0.8rem; color: #57606a; margin: -0.4rem 0 0.8rem; }
.worksheet-source a { color: #0066cc; }
</style>

<style>
#main-header,
.site-header,
.aux-nav,
.main-header,
.side-bar {
  display: none !important;
}
body { padding-top: 0 !important; }
.main-content-wrap { margin-top: 0 !important; }
.exam-breadcrumb { font-size: 0.85rem; margin-bottom: 0.75rem; }
.exam-breadcrumb a { color: #0066cc; text-decoration: none; }
.exam-breadcrumb a:hover { text-decoration: underline; }
</style>
<nav class="exam-breadcrumb" aria-label="Breadcrumb">
<a href="/">← Back</a>
</nav>

# Chapter 7: Regression Using Linear Algebra

*Topics: regression using linear algebra, design matrices*

*Problems below are collected from past exams; each links back to its full exam. Solutions are in the dropdowns.*

## Problems

- [FA25 MT2 · Problem 4](#fa25-mt2--problem-4-poly-wants-a-cracker-18-pts)
- [FA25 Final · Problem 8](#fa25-final--problem-8-6-pts-mt2-redemption)
- [WN26 MT2 · Problem 6](#wn26-mt2--problem-6-20-pts)
- [WN26 Final · Problem 7](#wn26-final--problem-7-8-pts-mt2-redemption)
- [SP26 MT2 · Problem 5](#sp26-mt2--problem-5-19-pts)
- [SP26 Final · Problem 8](#sp26-final--problem-8-12-pts-mt2-redemption)

---

## FA25 MT2 · Problem 4: Poly Wants a Cracker <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">18 pts</span>

<p class="worksheet-source">From <a href="/exams/fa25-mt2/">FA25 MT2</a></p>

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

---

## FA25 Final · Problem 8 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> <span class="badge" data-flag="mt2-redemption" style="background-color: #9A3324; color: #FFFFFF; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">MT2 Redemption</span>

<p class="worksheet-source">From <a href="/exams/fa25-final/">FA25 Final</a></p>

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

---

## WN26 MT2 · Problem 6 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">20 pts</span>

<p class="worksheet-source">From <a href="/exams/wn26-mt2/">WN26 MT2</a></p>

Suppose we'd like to fit a multiple linear regression model **without** an intercept term to **predict the number of fans in attendance at a Michigan football home game** given various features.

For each row in the dataset, the corresponding feature vector is <span class="math-inline">\\(\vec x&#95;i = \begin{bmatrix} \text{tempF}&#95;i \\\\ \text{tempC}&#95;i \\\\ \text{night}&#95;i \\\\ \text{day}&#95;i \end{bmatrix}\\)</span>, where:

-   <span class="math-inline">\\(\text{tempF}&#95;i\\)</span> is the temperature, in degrees **Fahrenheit**, at kickoff for game <span class="math-inline">\\(i\\)</span>

-   <span class="math-inline">\\(\text{tempC}&#95;i\\)</span> is the temperature, in degrees **Celsius**, at kickoff for game <span class="math-inline">\\(i\\)</span>

-   <span class="math-inline">\\(\text{night}&#95;i\\)</span> is 1 if game <span class="math-inline">\\(i\\)</span> is a night game and 0 otherwise

-   <span class="math-inline">\\(\text{day}&#95;i\\)</span> is 0 if game <span class="math-inline">\\(i\\)</span> is a night game and 1 otherwise

**Important**: Note that

<div class="math-display">
$$
\text{tempC}_i = \frac{5}{9} (\text{tempF}_i - 32)
$$
</div>

So, our model is of the form

<div class="math-display">
$$
h(\vec x_i) = w_1 \cdot \text{tempF}_i + w_2 \cdot \text{tempC}_i + w_3 \cdot \text{night}_i + w_4 \cdot \text{day}_i
$$
</div>

 We find optimal model parameters, <span class="math-inline">\\(\vec w^{\ast} = \begin{bmatrix} w&#95;1^{\ast} \\\\ w&#95;2^{\ast} \\\\ w&#95;3^{\ast} \\\\ w&#95;4^{\ast} \end{bmatrix}\\)</span>, by solving the normal equation.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> The first two rows of the dataset have the following information:

-   Game 1: 77 degrees Fahrenheit, 25 degrees Celsius, not night game, 102,111 fans

-   Game 2: 59 degrees Fahrenheit, 15 degrees Celsius, night game, 101,982 fans

Write the first two rows of the design matrix, <span class="math-inline">\\(X\\)</span>. Your answer should be a matrix with two rows and no variables.

<span class="math-inline">\\(X = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>

<details markdown="1"><summary>Solution</summary>

Each row of the design matrix is just the feature vector for that game:

<div class="math-display">
$$
\vec x_i = \begin{bmatrix} \text{tempF}_i \\\\ \text{tempC}_i \\\\ \text{night}_i \\\\ \text{day}_i \end{bmatrix}
$$
</div>

So,

<div class="math-display">
$$
\text{Game 1}: \begin{bmatrix} 77 & 25 & 0 & 1 \end{bmatrix}
\qquad
\text{Game 2}: \begin{bmatrix} 59 & 15 & 1 & 0 \end{bmatrix}
$$
</div>

Therefore, the first two rows of <span class="math-inline">\\(X\\)</span> are

<div class="math-display">
$$
X = \begin{bmatrix}
77 & 25 & 0 & 1 \\\\
59 & 15 & 1 & 0
\end{bmatrix}
$$
</div>

</details>

Recall, our model is of the form

<div class="math-display">
$$
h(\vec x_i) = w_1 \cdot \text{tempF}_i + w_2 \cdot \text{tempC}_i + w_3 \cdot \text{night}_i + w_4 \cdot \text{day}_i
$$
</div>

where <span class="math-inline">\\(\text{tempC}&#95;i = \frac{5}{9} (\text{tempF}&#95;i - 32)\\)</span>.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Suppose <span class="math-inline">\\(\vec w'\\)</span> is one solution to the normal equation for this model. Which option describes the **complete set** of solutions to the normal equation?

|     |     |
|:----|:----|
|     |     |

<details markdown="1"><summary>Solution</summary>

If we add any vector in <span class="math-inline">\\(\text{nullsp}(X)\\)</span> to one solution of the normal equation, we get another solution. So we just need to find a non-zero vector in <span class="math-inline">\\(\text{nullsp}(X)\\)</span>.

For any row of <span class="math-inline">\\(X\\)</span>, the following two statements must be true:

<div class="math-display">
$$
\begin{align*}
\text{tempC}_i &= \frac{5}{9}(\text{tempF}_i - 32) \\\\
\text{night}_i + \text{day}_i &= 1
\end{align*}
$$
</div>

The idea is to use this information to find a linear combination of <span class="math-inline">\\(X\\)</span>'s columns that equals the zero vector.

Using the first equation, we have

<div class="math-display">
$$
\text{tempF}_i - \frac{9}{5}\text{tempC}_i - 32 = 0
$$
</div>

In order to write this as a linear combination of <span class="math-inline">\\(X\\)</span>'s columns, the 32 needs to come from a vector that is "constant" across all rows. Fortunately, that's true of the sum of the night and day columns, since <span class="math-inline">\\(\text{night}&#95;i + \text{day}&#95;i = 1\\)</span> for all rows. So, this means

<div class="math-display">
$$
\begin{align*}
\text{tempF}_i - \frac{9}{5}\text{tempC}_i - 32(\text{night}_i + \text{day}_i) &= 0 \\\\
\text{tempF}_i - \frac{9}{5}\text{tempC}_i - 32 \text{night}_i - 32 \text{day}_i &= 0 \\\\
\end{align*}
$$
</div>

Meaning that

<div class="math-display">
$$
\begin{bmatrix} 1 \\\\ -9/5 \\\\ -32 \\\\ -32 \end{bmatrix} \in \text{nullsp}(X)
$$
</div>

Therefore, if <span class="math-inline">\\(\vec w'\\)</span> is one solution, the complete set of solutions is

<div class="math-display">
$$
\left \{ \vec w' + t\begin{bmatrix} 1 \\\\ -9/5 \\\\ -32 \\\\ -32 \end{bmatrix} \: , \: t \in \mathbb{R} \right \}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> First, assume <span class="math-inline">\\(h(\vec x&#95;i)\\)</span> is the model at the top of the page.

1.  What is the **largest possible** rank of the design matrix, <span class="math-inline">\\(X\\)</span>? (Note that we're asking about the full design matrix, not just its first two rows.)

   <span class="math-inline">\\(\text{largest possible value of }\text{rank}(X) = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>

2.  True or False: The sum of the errors of the model's predictions is 0.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

3.  True or False: The sum of the errors of the model's predictions **on just the rows of the dataset corresponding to night games** is 0.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

Let <span class="math-inline">\\(\vec e = \vec y - X \vec w^{\ast}\\)</span> be the error vector. Since <span class="math-inline">\\(\vec w^{\ast}\\)</span> satisfies the normal equation, <span class="math-inline">\\(\vec e\\)</span> is orthogonal to every column of <span class="math-inline">\\(X\\)</span>, and to every linear combination of those columns.

**(i)** The largest possible rank of <span class="math-inline">\\(X\\)</span> is 3, which happens when the tempF, tempC, and night columns are linearly independent. When the day column is added, the columns become linearly dependent. (Equivalently, the tempF, night, and day columns are linearly independent, but linearly dependent with the tempC column.)

**(ii)** This is true. Even though there is no explicit intercept term (and thus, no column of all ones), the all-ones vector is still in <span class="math-inline">\\(\text{colsp}(X)\\)</span>, because the night and day columns add up to 1 for each row.

<div class="math-display">
$$
\vec 1 = \text{night column} + \text{day column}
$$
</div>

 Since <span class="math-inline">\\(\vec e\\)</span> is orthogonal to every vector in <span class="math-inline">\\(\text{colsp}(X)\\)</span>, it is orthogonal to <span class="math-inline">\\(\vec 1\\)</span>, so

<div class="math-display">
$$
\begin{align*}
\vec 1^T \vec e &= \sum_{i=1}^n e_i = 0
\end{align*}
$$
</div>

**(iii)** This is also true. The night indicator is itself a column of <span class="math-inline">\\(X\\)</span>, so

<div class="math-display">
$$
\vec e \cdot (\text{night column}) = \vec e \cdot \begin{bmatrix} 0 \\\\ 1 \\\\ \vdots \end{bmatrix} = e_2 + ... = 0
$$
</div>

 But this dot product is exactly the sum of the errors for just the night games, because the night column has 1s on night rows and 0s elsewhere.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Now, suppose we remove the <span class="math-inline">\\(\textbf{day}&#95;i\\)</span> feature from our model, meaning our model is

<div class="math-display">
$$
h(\vec x_i) = w_1 \cdot \text{tempF}_i + w_2 \cdot \text{tempC}_i + w_3 \cdot \text{night}_i
$$
</div>

1.  After removing the day column, what is the **largest possible** rank of the **new** design matrix?

   <span class="math-inline">\\(\text{largest possible value of }\text{rank}(\text{new design matrix}) = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>

2.  True or False: The sum of the errors of the new model's predictions is 0.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

3.  True or False: The sum of the errors of the new model's predictions **on just the rows of the dataset corresponding to night games** is 0.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

Let <span class="math-inline">\\(\vec e&#95;{\text{new}}\\)</span> be the error vector for the new model.

**(i)** After removing the day column, the new design matrix has 3 columns, and there is no longer a forced linear dependence among them. So the largest possible rank is still 3. What's new now is that <span class="math-inline">\\(X\\)</span>'s columns are all linearly independent, meaning there is a unique solution to the normal equation.

**(ii)** This is false. The normal equations still tell us that <span class="math-inline">\\(\vec e&#95;{\text{new}}\\)</span> is orthogonal to each column of the new design matrix, but there is no guarantee that the all-ones vector is in the column space anymore. So the errors are not guaranteed to sum to 0.

**(iii)** This is true. The night indicator column is still present in the new design matrix, so <span class="math-inline">\\(\vec e&#95;{\text{new}}\\)</span> is orthogonal to that column. Therefore, the sum of the errors over the night-game rows is still 0.
</details>

</div>
</div>

</div>

---

## WN26 Final · Problem 7 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">8 pts</span> <span class="badge" data-flag="mt2-redemption" style="background-color: #9A3324; color: #FFFFFF; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">MT2 Redemption</span>

<p class="worksheet-source">From <a href="/exams/wn26-final/">WN26 Final</a></p>

Suppose we'd like to fit a multiple linear regression model **without an intercept term** to predict an apartment's monthly rent (in hundreds of dollars) using various features.

For apartment <span class="math-inline">\\(i\\)</span>, the corresponding feature vector is <span class="math-inline">\\(\vec x&#95;i = \begin{bmatrix} \text{bedrooms}&#95;i &amp; K&#95;i &amp; C&#95;i &amp; N&#95;i \end{bmatrix}^T\\)</span>, where <span class="math-inline">\\(\text{bedrooms}&#95;i\\)</span> is the number of bedrooms in apartment <span class="math-inline">\\(i\\)</span>, and <span class="math-inline">\\(K&#95;i\\)</span>, <span class="math-inline">\\(C&#95;i\\)</span>, and <span class="math-inline">\\(N&#95;i\\)</span> are one hot encoded features for the Kerrytown, Central Campus, and North Campus neighborhoods, respectively.

The model is fit by minimizing mean squared error. **All rows of the dataset are shown to the right.** The model's predictions, <span class="math-inline">\\(h(x&#95;i)\\)</span>, are shown, along with the true rents, <span class="math-inline">\\(y&#95;i\\)</span>. Several values are missing.

<div class="math-display">
$$
\boxed{\renewcommand{\arraystretch}{1.3}
\begin{array}{c|c|c|c}
\text{bedrooms}_i & \text{neighborhood}_i & y_i & h(x_i) \\\\
\hline
4 & \text{K} & 17 & \boxed{(i)} \\\\
1 & \text{C} & \boxed{(ii)} & 9 \\\\
3 & \text{C} & 15 & 13 \\\\
2 & \text{C} & 10 & 11 \\\\
1 & \text{N} & 9 & \boxed{(iii)} \\\\
4 & \text{N} & 13 & \boxed{(iv)}
\end{array}
\renewcommand{\arraystretch}{1}}
$$
</div>

For instance, the first row of the design matrix

is <span class="math-inline">\\(\begin{bmatrix} 4 &amp; 1 &amp; 0 &amp; 0 \end{bmatrix}\\)</span>.

Find all four missing values in the table. Show your work, and write your final answers in the boxes provided. Your answers should be integers with no variables. <em>Hint: Think about orthogonality.</em>

<details markdown="1"><summary>Solution</summary>

For clarity, let's start by writing out the full design matrix <span class="math-inline">\\(X\\)</span>.

<div class="math-display">
$$
X = \begin{bmatrix}
  4 & 1 & 0 & 0 \\\\
  1 & 0 & 1 & 0 \\\\
  3 & 0 & 1 & 0 \\\\
  2 & 0 & 1 & 0 \\\\
  1 & 0 & 0 & 1 \\\\
  4 & 0 & 0 & 1 \end{bmatrix}
$$
</div>

Let <span class="math-inline">\\(e&#95;i = y&#95;i-h(x&#95;i)\\)</span> refer to the error for apartment <span class="math-inline">\\(i\\)</span>. Since the model is fit by minimizing mean squared error, the vector

<div class="math-display">
$$
\vec e = \begin{bmatrix} e_1 \\\\ e_2 \\\\ e_3 \\\\ e_4 \\\\ e_5 \\\\ e_6 \end{bmatrix} = \begin{bmatrix} y_1 - h(x_1) \\\\ y_2 - h(x_2) \\\\ y_3 - h(x_3) \\\\ y_4 - h(x_4) \\\\ y_5 - h(x_5) \\\\ y_6 - h(x_6) \end{bmatrix} = \begin{bmatrix} 17 - (i) \\\\ (ii) - 9 \\\\ 15 - 13 \\\\ 10 - 11 \\\\ 9 - (iii) \\\\ 13 - (iv) \end{bmatrix}
$$
</div>

 is orthogonal to every column of <span class="math-inline">\\(X\\)</span>.

-   First, let's take the dot product of the error vector with the second column of <span class="math-inline">\\(X\\)</span>, the one hot encoded column for Kerrytown. We know this dot product must be <span class="math-inline">\\(0\\)</span>.

<div class="math-display">
$$
\begin{bmatrix} 1 \\\\ 0 \\\\ 0 \\\\ 0 \\\\ 0 \\\\ 0 \end{bmatrix} \cdot \begin{bmatrix} 17 - (i) \\\\ (ii) - 9 \\\\ 15 - 13 \\\\ 10 - 11 \\\\ 9 - (iii) \\\\ 13 - (iv) \end{bmatrix} = 0 \implies 17 - (i) = 0 \implies \boxed{(i) = 17}
$$
</div>

 Intuitively, this says that the errors for Kerrytown apartments must sum to <span class="math-inline">\\(0\\)</span>. Since there is only one Kerrytown apartment, this means that its prediction must be correct.

-   Similarly, if we take the dot product of the error vector with the third column of <span class="math-inline">\\(X\\)</span>, this tells us that the errors for the Central Campus apartments must sum to <span class="math-inline">\\(0\\)</span>.

<div class="math-display">
$$
((ii) - 9) + (15 - 13) + (10 - 11) = 0 \implies (ii) - 9 + 2 - 1 = 0 \implies \boxed{(ii) = 8}
$$
</div>

-   Things are a little more complicated for (iii) and (iv): it's true that

<div class="math-display">
$$
(9 - (iii)) + (13 - (iv)) = 0 \implies (iii) + (iv) = 22
$$
</div>

 but this is not enough information to determine the values of (iii) and (iv). To get another equation, we can set the dot product of the error vector with the first column of <span class="math-inline">\\(X\\)</span> to <span class="math-inline">\\(0\\)</span>.



<div class="math-display">
$$
\begin{align*}
    \begin{bmatrix} 4 \\\\ 1 \\\\ 3 \\\\ 2 \\\\ 1 \\\\ 4 \end{bmatrix} \cdot \begin{bmatrix} 17 - \mathbf{17} \\\\ \mathbf{8} - 9 \\\\ 15 - 13 \\\\ 10 - 11 \\\\ 9 - (iii) \\\\ 13 - (iv) \end{bmatrix} &= 0 \\\\
    -1 + 3 \cdot 2 + 2 \cdot (-1) + 1 \cdot (9 - (iii)) + 4 \cdot (13 - (iv)) &= 0 \\\\
    (iii) + 4(iv) &= 64
    \end{align*}
$$
</div>

   So,

<div class="math-display">
$$
\left( (iii) + 4(iv) \right) - \left( (iii) + (iv) \right) = 64 - 22 \implies 3(iv) = 42 \implies \boxed{(iv) = 14}
$$
</div>

 and thus

<div class="math-display">
$$
(iii) + 14 = 22 \implies \boxed{(iii) = 8}
$$
</div>

To summarize,

<div class="math-display">
$$
\boxed{(i)=17,\qquad (ii)=8,\qquad (iii)=8,\qquad (iv)=14}
$$
</div>

</details>

---

## SP26 MT2 · Problem 5 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">19 pts</span>

<p class="worksheet-source">From <a href="/exams/sp26-mt2/">SP26 MT2</a></p>

Suppose we're given a dataset with <span class="math-inline">\\(n = 5\\)</span> rows, and we use it to fit a multiple linear regression model with two features and an intercept term.

<div class="math-display">
$$
h(\vec x_i) = w_0 + w_1 x_i^{(1)} + w_2 x_i^{(2)}
$$
</div>

 Let <span class="math-inline">\\(X\\)</span> be the corresponding <span class="math-inline">\\(5 \times 3\\)</span> design matrix and <span class="math-inline">\\(\vec y \in \mathbb{R}^5\\)</span> be the corresponding observation vector. Suppose the matrix <span class="math-inline">\\(P\\)</span> that projects onto the column space of <span class="math-inline">\\(X\\)</span> is

<div class="math-display">
$$
P = \begin{bmatrix} 1/4 & 1/4 & 1/4 & 1/4 & 0 \\\\ 1/4 & 1/4 & 1/4 & 1/4 & 0 \\\\ 1/4 & 1/4 & 1/4 & 1/4 & 0 \\\\ 1/4 & 1/4 & 1/4 & 1/4 & 0 \\\\ 0 & 0 & 0 & 0 & 1 \end{bmatrix}
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> **In parts a) and b) only**, suppose the projection of <span class="math-inline">\\(\vec y\\)</span> onto <span class="math-inline">\\(\text{colsp}(X)\\)</span> is <span class="math-inline">\\(\vec p = \begin{bmatrix} 3 \\\\ 3 \\\\ 3 \\\\ 3 \\\\ 3 \end{bmatrix}\\)</span>. There are infinitely many such vectors <span class="math-inline">\\(\vec y\\)</span>. State one possible vector <span class="math-inline">\\(\vec y\\)</span> **whose five components are all different**. Give your answer as a vector with no variables.

one possible vector <span class="math-inline">\\(\vec y =\\)</span> \_\_\_\_\_\_

<details markdown="1"><summary>Solution</summary>

For any vector <span class="math-inline">\\(\vec y\\)</span>, multiplying by <span class="math-inline">\\(P\\)</span> averages the first four components of <span class="math-inline">\\(\vec y\\)</span> and leaves the fifth component unchanged:

<div class="math-display">
$$
P\vec y =
\begin{bmatrix}
\displaystyle \frac{y_1+y_2+y_3+y_4}{4} \\\\ \\\\
\displaystyle \frac{y_1+y_2+y_3+y_4}{4} \\\\ \\\\
\displaystyle \frac{y_1+y_2+y_3+y_4}{4} \\\\ \\\\
\displaystyle \frac{y_1+y_2+y_3+y_4}{4} \\\\ \\\\
\displaystyle y_5
\end{bmatrix}
$$
</div>

 We want this to equal <span class="math-inline">\\(\begin{bmatrix} 3 \\\\ 3 \\\\ 3 \\\\ 3 \\\\ 3 \end{bmatrix}\\)</span>, so the first four components of <span class="math-inline">\\(\vec y\\)</span> need to have average 3, and the fifth component needs to be 3.

One possible choice is

<div class="math-display">
$$
\vec y =
\begin{bmatrix}
0 \\\\
1 \\\\
5 \\\\
6 \\\\
3
\end{bmatrix}
$$
</div>

 The first four components have average 3, and all five components are different. There are infinitely many possible answers, though.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">3 pts</span> Let <span class="math-inline">\\(\vec y\\)</span> and <span class="math-inline">\\(\vec p \\)</span> be as defined in part (a). True or false: <span class="math-inline">\\(X^T (\vec p - \vec y) = \vec 0\\)</span>.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> True</span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> False</span></div>

This is true. If <span class="math-inline">\\(\vec p\\)</span> is the projection of <span class="math-inline">\\(\vec y\\)</span> onto <span class="math-inline">\\(\text{colsp}(X)\\)</span>, then the error vector <span class="math-inline">\\(\vec y - \vec p\\)</span> is orthogonal to every vector in <span class="math-inline">\\(\text{colsp}(X)\\)</span>. This is how we arrived at the normal equations, <span class="math-inline">\\(X^TX \vec w = X^T \vec y\\)</span>. Here, this means

<div class="math-display">
$$
X^T(\vec y - \vec p) = \vec 0
$$
</div>

 Multiplying by <span class="math-inline">\\(-1\\)</span> gives

<div class="math-display">
$$
X^T(\vec p - \vec y) = \vec 0
$$
</div>

</details>

For the rest of the problem, suppose that both <span class="math-inline">\\(\vec w^{\ast} = \begin{bmatrix} 2 \\\\ 3 \\\\ 1 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec w' = \begin{bmatrix} 3 \\\\ 1 \\\\ 0 \end{bmatrix}\\)</span> are both optimal parameter vectors that minimize mean squared error.

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Which of these vectors are in <span class="math-inline">\\(\text{nullsp}(X)\\)</span>? **Select all** that apply.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} 2 \\\\ 3 \\\\ 1 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} 5 \\\\ 4 \\\\ 1 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ -2 \\\\ -1 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} 4 \\\\ 6 \\\\ 2 \end{bmatrix}\\)</span></span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} -2 \\\\ 4 \\\\ 2 \end{bmatrix}\\)</span></span></div>

<details markdown="1"><summary>Solution</summary>

<span class="mc-square mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(\begin{bmatrix} -2 \\\\ 4 \\\\ 2 \end{bmatrix}\\)</span>

If two parameter vectors are both solutions to the normal equation, their difference is in <span class="math-inline">\\(\text{nullsp}(X)\\)</span>. So,

<div class="math-display">
$$
\vec w' - \vec w^*
=
\begin{bmatrix} 3 \\\\ 1 \\\\ 0 \end{bmatrix}
-
\begin{bmatrix} 2 \\\\ 3 \\\\ 1 \end{bmatrix}
=
\begin{bmatrix} 1 \\\\ -2 \\\\ -1 \end{bmatrix}
\in \text{nullsp}(X)
$$
</div>

Where did this come from? The fact that <span class="math-inline">\\(\vec w'\\)</span> and <span class="math-inline">\\(\vec w^{\ast}\\)</span> are both optimal parameter vectors means that they both result in the same projection of <span class="math-inline">\\(\vec y\\)</span> onto <span class="math-inline">\\(\text{colsp}(X)\\)</span>, so

<div class="math-display">
$$
X \vec w^* = X \vec w'
$$
</div>

But, this means <span class="math-inline">\\(X(\vec w' - \vec w^{\ast}) = \vec 0\\)</span>, which says that <span class="math-inline">\\(\vec w' - \vec w^{\ast}\\)</span> is in <span class="math-inline">\\(\text{nullsp}(X)\\)</span>.

Also, <span class="math-inline">\\(P\\)</span> projects onto <span class="math-inline">\\(\text{colsp}(X)\\)</span>, and <span class="math-inline">\\(P\\)</span> has rank 2. Therefore <span class="math-inline">\\(\text{rank}(X)=2\\)</span> (the logic behind this is described [here](https://notes.eecs245.org/linear-transformations-and-projections/complete-solution/#example-is-p-invertible)). Since <span class="math-inline">\\(X\\)</span> has 3 columns, the rank-nullity theorem gives

<div class="math-display">
$$
\dim(\text{nullsp}(X)) = 3 - 2 = 1
$$
</div>

 So <span class="math-inline">\\(\text{nullsp}(X)\\)</span> is exactly

<div class="math-display">
$$
\text{nullsp}(X) =
\text{span}\left( \left\{ \begin{bmatrix} 1 \\\\ -2 \\\\ -1 \end{bmatrix} \right\} \right)
$$
</div>

 Among the listed choices, the vectors in this span are <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ -2 \\\\ -1 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\begin{bmatrix} -2 \\\\ 4 \\\\ 2 \end{bmatrix}\\)</span>.

The rank-nullity logic wasn't strictly necessary to answer the question; I've included it here for completeness, as it fully justifies why none of the other listed vectors are in <span class="math-inline">\\(\text{nullsp}(X)\\)</span>.
</details>

**The information stated below, above part **d)**, is the same as the information stated on the previous page. It's provided for your convenience.**

Recall, <span class="math-inline">\\(X\\)</span> is a <span class="math-inline">\\(5 \times 3\\)</span> design matrix for the model

<div class="math-display">
$$
h(\vec x_i) = w_0 + w_1 x_i^{(1)} + w_2 x_i^{(2)}
$$
</div>

 Additionally, <span class="math-inline">\\(\vec y \in \mathbb{R}^5\\)</span> is an observation vector, both <span class="math-inline">\\(\vec w^{\ast} = \begin{bmatrix} 2 \\\\ 3 \\\\ 1 \end{bmatrix}\\)</span> and <span class="math-inline">\\(\vec w' = \begin{bmatrix} 3 \\\\ 1 \\\\ 0 \end{bmatrix}\\)</span> are both optimal parameter vectors that minimize mean squared error, and the matrix <span class="math-inline">\\(P\\)</span> that projects onto the column space of <span class="math-inline">\\(X\\)</span> is

<div class="math-display">
$$
P = \begin{bmatrix} 1/4 & 1/4 & 1/4 & 1/4 & 0 \\\\ 1/4 & 1/4 & 1/4 & 1/4 & 0 \\\\ 1/4 & 1/4 & 1/4 & 1/4 & 0 \\\\ 1/4 & 1/4 & 1/4 & 1/4 & 0 \\\\ 0 & 0 & 0 & 0 & 1 \end{bmatrix}
$$
</div>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">d)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">8 pts</span> Find one possible design matrix <span class="math-inline">\\(X\\)</span>, consistent with all of the information above. Show your work, and <span class="math-inline">\\(\boxed{\text{circle}}\\)</span> your final answer, which should be a matrix with no variables.

<details markdown="1"><summary>Solution</summary>

Since <span class="math-inline">\\(P\\)</span> projects onto <span class="math-inline">\\(\text{colsp}(X)\\)</span>, we need <span class="math-inline">\\(\text{colsp}(X) = \text{colsp}(P)\\)</span>. Notice that the result <span class="math-inline">\\(P \vec y\\)</span> for any vector <span class="math-inline">\\(\vec y \in \mathbb{R}^5\\)</span> will have equal first four components (resulting from averaging the original first four components of <span class="math-inline">\\(\vec y\\)</span>) and the fifth component will be unchanged. If we think of the space of possible values of <span class="math-inline">\\(P \vec y\\)</span>, we realize that any <span class="math-inline">\\(P \vec y\\)</span> is of the form

<div class="math-display">
$$
\begin{bmatrix} a \\\\ a \\\\ a \\\\ a \\\\ b \end{bmatrix} = a \begin{bmatrix} 1 \\\\ 1 \\\\ 1 \\\\ 1 \\\\ 0 \end{bmatrix} + b \begin{bmatrix} 0 \\\\ 0 \\\\ 0 \\\\ 0 \\\\ 1 \end{bmatrix}
$$
</div>

This means

<div class="math-display">
$$
\text{colsp}(X) = \text{span}\left( \left\{ \begin{bmatrix} 1 \\\\ 1 \\\\ 1 \\\\ 1 \\\\ 0 \end{bmatrix}, \begin{bmatrix} 0 \\\\ 0 \\\\ 0 \\\\ 0 \\\\ 1 \end{bmatrix} \right\} \right)
$$
</div>

Now, the problem boils down to finding a design matrix <span class="math-inline">\\(X\\)</span> with the above column space, that also meets the other requirements. Here are the other relevant requirements:

**(i)** Since the model has an intercept term, the first column of <span class="math-inline">\\(X\\)</span> should be <span class="math-inline">\\(\vec 1 = \begin{bmatrix} 1 \\\\ 1 \\\\ 1 \\\\ 1 \\\\ 1 \end{bmatrix}\\)</span>.

**(ii)** From part **c)**, we need <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ -2 \\\\ -1 \end{bmatrix} \in \text{nullsp}(X)\\)</span>.

If the columns of <span class="math-inline">\\(X\\)</span> are <span class="math-inline">\\(\vec x^{(0)}\\)</span>, <span class="math-inline">\\(\vec x^{(1)}\\)</span>, and <span class="math-inline">\\(\vec x^{(2)}\\)</span> (we're told <span class="math-inline">\\(X\\)</span> has 3 columns), the first requirement states

<div class="math-display">
$$
\vec x^{(0)} = \begin{bmatrix} 1 \\\\ 1 \\\\ 1 \\\\ 1 \\\\ 1 \end{bmatrix}
$$
</div>

The second requirement states

<div class="math-display">
$$
\underbrace{\begin{bmatrix} | & | & | \\\\ \vec x^{(0)} & \vec x^{(1)} & \vec x^{(2)} \\\\ | & | & | \end{bmatrix}}_{X} \begin{bmatrix} 1 \\\\ -2 \\\\ -1 \end{bmatrix} = \vec 0
$$
</div>

or, in other words, <span class="math-inline">\\(\vec x^{(0)} - 2\vec x^{(1)} - \vec x^{(2)} = \vec 0\\)</span>.

To guarantee <span class="math-inline">\\(\text{colsp}(X)\\)</span> is the span we set out before,

<div class="math-display">
$$
\text{colsp}(X) = \text{span} \left( \left\{ \begin{bmatrix} 1 \\\\ 1 \\\\ 1 \\\\ 1 \\\\ 1 \end{bmatrix}, \begin{bmatrix} 1 \\\\ 1 \\\\ 1 \\\\ 1 \\\\ 0 \end{bmatrix}\right\} \right)
$$
</div>

let's just pick <span class="math-inline">\\(\vec x^{(1)} = \begin{bmatrix} 1 \\\\ 1 \\\\ 1 \\\\ 1 \\\\ 0 \end{bmatrix}\\)</span>. Since <span class="math-inline">\\(\vec x^{(0)} - \vec x^{(1)} = \begin{bmatrix} 0 \\\\ 0 \\\\ 0 \\\\ 0 \\\\ 1 \end{bmatrix}\\)</span>, we have accomplished the goal of finding a design matrix <span class="math-inline">\\(X\\)</span> with the desired column space. With our choices of <span class="math-inline">\\(\vec x^{(0)}\\)</span> and <span class="math-inline">\\(\vec x^{(1)}\\)</span> out of the way, <span class="math-inline">\\(\vec x^{(2)}\\)</span> is fully determined for us:

<div class="math-display">
$$
\vec x^{(0)} - 2 \vec x^{(1)} - \vec x^{(2)} = \vec 0 \implies \vec x^{(2)} = \vec x^{(0)} - 2 \vec x^{(1)} = \begin{bmatrix} 1 \\\\ 1 \\\\ 1 \\\\ 1 \\\\ 1 \end{bmatrix} - 2 \begin{bmatrix} 1 \\\\ 1 \\\\ 1 \\\\ 1 \\\\ 0 \end{bmatrix} = \begin{bmatrix} -1 \\\\ -1 \\\\ -1 \\\\ -1 \\\\ 1 \end{bmatrix}
$$
</div>

Therefore, one possible design matrix is

<div class="math-display">
$$
X =
\begin{bmatrix}
1 & 1 & -1 \\\\
1 & 1 & -1 \\\\
1 & 1 & -1 \\\\
1 & 1 & -1 \\\\
1 & 0 & 1
\end{bmatrix}
$$
</div>

This design matrix has a column space of <span class="math-inline">\\(\text{span} \left( \left\lbrace \begin{bmatrix} 1 \\\\ 1 \\\\ 1 \\\\ 1 \\\\ 1 \end{bmatrix}, \begin{bmatrix} 1 \\\\ 1 \\\\ 1 \\\\ 1 \\\\ 0 \end{bmatrix}\right\rbrace \right)\\)</span>, which is the same as the column space of <span class="math-inline">\\(P\\)</span>. It also has the required null space, which is why it would be wrong to just pick, say,

<div class="math-display">
$$
\begin{bmatrix} 1 & 1 & 0 \\\\ 1 & 1 & 0 \\\\ 1 & 1 & 0 \\\\ 1 & 1 & 0 \\\\ 0 & 0 & 1 \end{bmatrix}
$$
</div>

--- the above matrix has a null space spanned by <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ -1 \\\\ -1 \end{bmatrix}\\)</span>, not <span class="math-inline">\\(\begin{bmatrix} 1 \\\\ -2 \\\\ -1 \end{bmatrix}\\)</span>.
</details>

</div>
</div>

</div>

---

## SP26 Final · Problem 8 <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span> <span class="badge" data-flag="mt2-redemption" style="background-color: #9A3324; color: #FFFFFF; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">MT2 Redemption</span>

<p class="worksheet-source">From <a href="/exams/sp26-final/">SP26 Final</a></p>

Suppose we'd like to fit a multiple linear regression model to predict <span class="math-inline">\\(\texttt{cost}&#95;i\\)</span>, the cost in dollars of parking in an Ann Arbor parking garage, using <span class="math-inline">\\(\texttt{hours}&#95;i\\)</span>, the number of hours parked.

For each row <span class="math-inline">\\(i\\)</span>, the corresponding augmented feature vector is <span class="math-inline">\\(\text{Aug}(\vec x&#95;i) = \begin{bmatrix} 1 &amp; \texttt{hours}&#95;i &amp; \max(0,\texttt{hours}&#95;i-2) \end{bmatrix}^T\\)</span> so the model is of the form

<div class="math-display">
$$
h(\vec x_i)
=
w_0 + w_1 \texttt{hours}_i + w_2 \max(0, \texttt{hours}_i - 2)
$$
</div>

 The model is fit by minimizing mean squared error.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Suppose the dataset has four rows, and the number of hours parked in those rows is

<span class="math-inline">\\(3\\)</span>, <span class="math-inline">\\(0\\)</span>, <span class="math-inline">\\(5\\)</span>, and <span class="math-inline">\\(1\\)</span>, respectively. Write the first four rows of the design matrix <span class="math-inline">\\(X\\)</span>. Your answer should be a matrix with four rows and no variables.

<span class="math-inline">\\(X =\\)</span> \_\_\_\_\_\_

<details markdown="1"><summary>Solution</summary>

Each row is the transpose of the augmented feature vector

<div class="math-display">
$$
\begin{bmatrix}
1\\\\
\texttt{hours}_i\\\\
\max(0,\texttt{hours}_i-2)
\end{bmatrix}
$$
</div>

 For <span class="math-inline">\\(\texttt{hours}&#95;i=3,0,5,1\\)</span>, the values of <span class="math-inline">\\(\max(0,\texttt{hours}&#95;i-2)\\)</span> are <span class="math-inline">\\(1,0,3,0\\)</span>, respectively. So,

<div class="math-display">
$$
X=
\begin{bmatrix}
1&3&1\\\\
1&0&0\\\\
1&5&3\\\\
1&1&0
\end{bmatrix}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">2 pts</span> Give a one-sentence English explanation of the meaning of <span class="math-inline">\\(w&#95;2\\)</span>.

<details markdown="1"><summary>Solution</summary>

The coefficient <span class="math-inline">\\(w&#95;2\\)</span> is the change in the hourly slope after 2 hours; after the first 2 hours, each additional hour changes the predicted cost by <span class="math-inline">\\(w&#95;1+w&#95;2\\)</span> dollars instead of <span class="math-inline">\\(w&#95;1\\)</span> dollars.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Once again, suppose the dataset has four rows. In each of the following subparts, we provide the number of hours parked in the dataset. Find the rank of the design matrix <span class="math-inline">\\(X\\)</span> in each case. Fill in each blank with an integer with no variables.

1.  (2 pts) <span class="math-inline">\\(3\\)</span>, <span class="math-inline">\\(0\\)</span>, <span class="math-inline">\\(5\\)</span>, and <span class="math-inline">\\(1\\)</span> <span class="math-inline">\\(\text{rank}(X) = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>

2.  (2 pts) <span class="math-inline">\\(2\\)</span>, <span class="math-inline">\\(0\\)</span>, <span class="math-inline">\\(2\\)</span>, and <span class="math-inline">\\(1\\)</span> <span class="math-inline">\\(\text{rank}(X) = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>

3.  (2 pts) <span class="math-inline">\\(3\\)</span>, <span class="math-inline">\\(4\\)</span>, <span class="math-inline">\\(5\\)</span>, and <span class="math-inline">\\(6\\)</span> <span class="math-inline">\\(\text{rank}(X) = \&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>

<details markdown="1"><summary>Solution</summary>

This feature engineering setup is an example of the multiple linear regression design matrices from [Chapter 7.2](https://notes.eecs245.org/regression-using-linear-algebra/multiple-linear-regression/).

**(i)** The design matrix is

<div class="math-display">
$$
\begin{bmatrix}
    1&3&1\\\\
    1&0&0\\\\
    1&5&3\\\\
    1&1&0
    \end{bmatrix}
$$
</div>

 The three columns are linearly independent, so <span class="math-inline">\\(\text{rank}(X)=3\\)</span>.

**(ii)** The design matrix is

<div class="math-display">
$$
\begin{bmatrix}
    1&2&0\\\\
    1&0&0\\\\
    1&2&0\\\\
    1&1&0
    \end{bmatrix}
$$
</div>

 The third column is all zero, while the first two columns are linearly independent. So <span class="math-inline">\\(\text{rank}(X)=2\\)</span>.

**(iii)** If all hour values are greater than <span class="math-inline">\\(2\\)</span>, then

<div class="math-display">
$$
\max(0,\texttt{hours}_i-2)=\texttt{hours}_i-2
$$
</div>

 This means column 2 is equal to <span class="math-inline">\\(2\\)</span> times column 1 plus column 3:

<div class="math-display">
$$
\text{column 2}=2(\text{column 1})+\text{column 3}
$$
</div>

 So the rank is at most <span class="math-inline">\\(2\\)</span>. Since the hour values are not all the same, columns 1 and 3 are linearly independent, and <span class="math-inline">\\(\text{rank}(X)=2\\)</span>.
</details>

</div>
</div>

</div>

---

{% endraw %}
