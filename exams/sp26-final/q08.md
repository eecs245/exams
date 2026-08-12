---
number: 8
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span> <span class="badge" data-flag="mt2-redemption" style="background-color: #9A3324; color: #FFFFFF; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">MT2 Redemption</span>
points: 12
flags: [mt2-redemption]
has_solution: true
images: []
---

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
