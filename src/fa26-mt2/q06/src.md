Suppose we'd like to fit a multiple linear regression model to predict the daily electricity use of household <span class="math-inline">\\(i\\)</span>, <span class="math-inline">\\(y&#95;i\\)</span>, in kilowatt-hours.

For each household <span class="math-inline">\\(i\\)</span>, the feature vector is <span class="math-inline">\\(\vec x&#95;i=\begin{bmatrix}x&#95;i^{(1)}\\\\x&#95;i^{(2)}\end{bmatrix}\\)</span>, where:

-   <span class="math-inline">\\(x&#95;i^{(1)}\\)</span> is the number of residents.

-   <span class="math-inline">\\(x&#95;i^{(2)}\\)</span> is <span class="math-inline">\\(2\\)</span> if the household uses a heat pump and <span class="math-inline">\\(0\\)</span> if it uses gas heating.

Our model is

<div class="math-display">
$$
h(\vec x_i)=w_0+w_1x_i^{(1)}+w_2x_i^{(2)}
$$
</div>

 The dataset below has two unknown values, <span class="math-inline">\\(a\\)</span> and <span class="math-inline">\\(b\\)</span>.

| <span class="math-inline">\\(i\\)</span> | Residents (<span class="math-inline">\\(x&#95;i^{(1)}\\)</span>) | Heating source (<span class="math-inline">\\(x&#95;i^{(2)}\\)</span>) | Electricity use (<span class="math-inline">\\(y&#95;i\\)</span>) |
|:--:|:--:|:--:|:--:|
| 1 | 2 | <span class="math-inline">\\(a\\)</span> | 12 |
| 2 | 5 | 2 | 30 |
| 3 | 2 | 2 | 16 |
| 4 | 4 | 0 | <span class="math-inline">\\(b\\)</span> |
| 5 | 3 | 0 | 16 |

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge badge-points">4 pts</span> Write the design matrix <span class="math-inline">\\(X\\)</span>. Your answer should be a matrix in terms of <span class="math-inline">\\(a\\)</span> and constants.

<details markdown="1"><summary>Solution</summary>

The intercept contributes a column of ones, followed by the residents and heating-source features:

<div class="math-display">
$$
\boxed{X=\begin{bmatrix}1&2&a\\\\1&5&2\\\\1&2&2\\\\1&4&0\\\\1&3&0\end{bmatrix}}
$$
</div>

</details>

Recall, our model is <span class="math-inline">\\(h(\vec x&#95;i)=w&#95;0+w&#95;1x&#95;i^{(1)}+w&#95;2x&#95;i^{(2)}\\)</span>, where <span class="math-inline">\\(x&#95;i^{(1)}\\)</span> is the number of residents and <span class="math-inline">\\(x&#95;i^{(2)}\\)</span> is <span class="math-inline">\\(2\\)</span> for a heat pump and <span class="math-inline">\\(0\\)</span> for gas heating.

| <span class="math-inline">\\(i\\)</span> | Residents (<span class="math-inline">\\(x&#95;i^{(1)}\\)</span>) | Heating source (<span class="math-inline">\\(x&#95;i^{(2)}\\)</span>) | Electricity use (<span class="math-inline">\\(y&#95;i\\)</span>) |
|:--:|:--:|:--:|:--:|
| 1 | 2 | <span class="math-inline">\\(a\\)</span> | 12 |
| 2 | 5 | 2 | 30 |
| 3 | 2 | 2 | 16 |
| 4 | 4 | 0 | <span class="math-inline">\\(b\\)</span> |
| 5 | 3 | 0 | 16 |

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge badge-points">10 pts</span> The parameter vector that minimizes mean squared error is <span class="math-inline">\\(\vec w^\ast=\begin{bmatrix}3\\\\4\\\\3\end{bmatrix}\\)</span>.

Find <span class="math-inline">\\(a\\)</span> and <span class="math-inline">\\(b\\)</span>. Your answers should be numbers with no variables.

<em>Hint: What properties must the error vector satisfy?</em>

<details markdown="1"><summary>Solution</summary>

The predictions and errors are

<div class="math-display">
$$
X\vec w^\ast=\begin{bmatrix}11+3a\\\\29\\\\17\\\\19\\\\15\end{bmatrix},\qquad
\vec e=\vec y-X\vec w^\ast=\begin{bmatrix}1-3a\\\\1\\\\-1\\\\b-19\\\\1\end{bmatrix}
$$
</div>

 At a least-squares solution, <span class="math-inline">\\(\vec e\\)</span> is orthogonal to every column of <span class="math-inline">\\(X\\)</span>. Orthogonality to the intercept column gives

<div class="math-display">
$$
(1-3a)+1-1+(b-19)+1=0\quad\Longrightarrow\quad b-17-3a=0
$$
</div>

 Orthogonality to the residents column gives

<div class="math-display">
$$
2(1-3a)+5-2+4(b-19)+3=0\quad\Longrightarrow\quad4b-68-6a=0
$$
</div>

 Substituting <span class="math-inline">\\(b=17+3a\\)</span> into the second equation gives <span class="math-inline">\\(6a=0\\)</span>. Thus,

<div class="math-display">
$$
\boxed{a=0,\qquad b=17}
$$
</div>

 These values give <span class="math-inline">\\(\vec e=\begin{bmatrix}1\\\\1\\\\-1\\\\-2\\\\1\end{bmatrix}\\)</span>, which is also orthogonal to the heating-source column: <span class="math-inline">\\(2(1)+2(-1)=0\\)</span>. All the normal equations are satisfied.
</details>

</div>
</div>

</div>
