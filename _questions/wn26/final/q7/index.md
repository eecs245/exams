---
number: 7
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">8 pts</span> <span class="badge" data-flag="mt2-redemption" style="background-color: #9A3324; color: #FFFFFF; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">MT2 Redemption</span>
points: 8
flags: [mt2-redemption]
has_solution: true
images: []
---

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
