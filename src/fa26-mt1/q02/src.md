Consider a dataset of seven values <span class="math-inline">\\(y&#95;1,y&#95;2,\ldots,y&#95;7\\)</span>, listed in **non-decreasing** order:

<div class="math-display">
$$
y_1,\ y_2,\ 47,\ 60,\ 60,\ 81,\ y_7
$$
</div>

 Suppose that the mean of <span class="math-inline">\\(y&#95;1,\ldots,y&#95;6\\)</span> --- that is, **not including <span class="math-inline">\\(\mathbf{y&#95;7}\\)</span>** --- is <span class="math-inline">\\(50\\)</span>. Furthermore, suppose

-   <span class="math-inline">\\(\displaystyle f(w)=\frac17\sum&#95;{i=1}^7|y&#95;i-w|\\)</span>, and <span class="math-inline">\\(\alpha^{\ast}\\)</span> is the value of <span class="math-inline">\\(w\\)</span> that minimizes <span class="math-inline">\\(f(w)\\)</span>.

-   <span class="math-inline">\\(\displaystyle g(w)=\frac17\sum&#95;{i=1}^7(y&#95;i-w)^2\\)</span>, and <span class="math-inline">\\(\beta^{\ast}\\)</span> is the value of <span class="math-inline">\\(w\\)</span> that minimizes <span class="math-inline">\\(g(w)\\)</span>.

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge badge-points">2 pts</span> What is the value of <span class="math-inline">\\(\alpha^{\ast}\\)</span>? Give your answer as a number with no variables.

<span class="math-inline">\\(\alpha^{\ast}=\&#95;\&#95;\&#95;\&#95;\&#95;\&#95;\\)</span>

<details markdown="1"><summary>Solution</summary>

Mean absolute error is minimized by the median. Since there are seven ordered values, the median is the fourth value, so <span class="math-inline">\\(\boxed{\alpha^{\ast}=60}\\)</span>. The fact that <span class="math-inline">\\(60\\)</span> is repeated does not change this result: the middle (fourth) value is still <span class="math-inline">\\(60\\)</span>, so the median is still <span class="math-inline">\\(60\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge badge-points">5 pts</span> What is the largest possible value of <span class="math-inline">\\(y&#95;7\\)</span> such that <span class="math-inline">\\(\alpha^{\ast}\geq\beta^{\ast}\\)</span>? Give your answer as a number with no variables.

<details markdown="1"><summary>Solution</summary>

Mean squared error is minimized by the mean. The first six values sum to <span class="math-inline">\\(6\cdot50=300\\)</span>, so

<div class="math-display">
$$
\beta^*=\frac{300+y_7}{7}
$$
</div>

 Using <span class="math-inline">\\(\alpha^{\ast}=60\\)</span>, the required condition becomes

<div class="math-display">
$$
60\geq\frac{300+y_7}{7}
\quad\Longleftrightarrow\quad
420\geq300+y_7
\quad\Longleftrightarrow\quad
y_7\leq120
$$
</div>

 The value <span class="math-inline">\\(120\\)</span> is consistent with the ordering, so the largest possible value is <span class="math-inline">\\(\boxed{120}\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge badge-points">7 pts</span> Consider the same seven values, listed in **non-decreasing** order:

<div class="math-display">
$$
y_1,\ y_2,\ 47,\ 60,\ 60,\ 81,\ y_7
$$
</div>

 Recall,

<div class="math-display">
$$
f(w)=\frac17\sum_{i=1}^7|y_i-w|
$$
</div>

 For this part, do not assume that <span class="math-inline">\\(\alpha^{\ast}\geq\beta^{\ast}\\)</span>.

Suppose that <span class="math-inline">\\(f(59)=30\\)</span>. What is <span class="math-inline">\\(f(65)\\)</span>? Give your answer as a number with no variables. <em>Hint: Consider the slopes of <span class="math-inline">\\(f(w)\\)</span> between <span class="math-inline">\\(w=59\\)</span> and <span class="math-inline">\\(w=65\\)</span>.</em>

<details markdown="1"><summary>Solution</summary>

For any value of <span class="math-inline">\\(w\\)</span> that is not equal to a <span class="math-inline">\\(y&#95;i\\)</span>, the slope of mean absolute error, <span class="math-inline">\\(f(w)\\)</span>, is

<div class="math-display">
$$
\frac{\text{d}}{\text{d}w}f(w)
=\frac{\text{# of points left of }w-\text{# of points right of }w}{7}
$$
</div>

 For <span class="math-inline">\\(59&lt;w&lt;60\\)</span>, there are three values to the left and four to the right, so the slope is <span class="math-inline">\\(-1/7\\)</span>. For <span class="math-inline">\\(60&lt;w&lt;65\\)</span>, there are five to the left and two to the right, so the slope is <span class="math-inline">\\(3/7\\)</span>. Both copies of <span class="math-inline">\\(60\\)</span> count.

<div class="math-display">
$$
\begin{align*}
f(60)&=30+(60-59)\left(-\frac17\right)=\frac{209}{7}\\\\
f(65)&=f(60)+(65-60)\left(\frac37\right)
=\frac{209}{7}+\frac{15}{7}=\boxed{32}
\end{align*}
$$
</div>

![image](imgs/tikz-c525583657df.svg)
</details>

</div>
</div>

</div>
