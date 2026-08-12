---
number: 1
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span> <span class="badge" data-flag="mt1-redemption" style="background-color: #9A3324; color: #FFFFFF; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">MT1 Redemption</span>
points: 12
flags: [mt1-redemption]
has_solution: true
images: []
---

Suppose we'd like to find the optimal constant prediction, <span class="math-inline">\\(w^{\ast}\\)</span>, for the constant model <span class="math-inline">\\(h(x&#95;i) = w\\)</span>, given the following dataset of <span class="math-inline">\\(n = 4\\)</span> values.

<div class="math-display">
$$
y_1 = 3, \quad y_2 = 6, \quad y_3 = 6, \quad y_4 = 13
$$
</div>

 In each part, choose from the options below.

<div class="math-display">
$$
\begin{array}{l@{\hspace{1.75cm}}l}
A = 3 & E = 7 \\\\[1.5ex]
B = \dfrac{4}{\frac{1}{3} + \frac{1}{6} + \frac{1}{6} + \frac{1}{13}} \approx 5.37 & F = \sqrt{\dfrac{3^2 + 6^2 + 6^2 + 13^2}{4}} \approx 7.90 \\\\[3ex]
C = 6 & G = 8 \\\\[1.5ex]
D = \left( 3 \cdot 6 \cdot 6 \cdot 13 \right)^{1/4} \approx 6.12 & H = 13 \\\\
\end{array}
$$
</div>

1.  (3 pts) What value of <span class="math-inline">\\(w^{\ast}\\)</span> minimizes <span class="math-inline">\\(R(w) = \displaystyle \frac{1}{4} \sum&#95;{i=1}^4 (y&#95;i - w)^2\\)</span>?

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(A\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(B\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(C\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(D\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(E\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(F\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(G\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(H\\)</span></span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(A\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(B\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(C\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(D\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(E\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(F\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(G\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(H\\)</span></span></div>

   For (i), the minimizer of mean squared error is the mean, so

<div class="math-display">
$$
w^* = \frac{3+6+6+13}{4} = \boxed{7}
$$
</div>

</details>

2.  (3 pts) What value of <span class="math-inline">\\(w^{\ast}\\)</span> minimizes <span class="math-inline">\\(R(w) = \displaystyle \lim&#95;{p \to \infty} \displaystyle \frac{1}{4} \sum&#95;{i=1}^4 |y&#95;i - w|^p\\)</span>?

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(A\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(B\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(C\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(D\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(E\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(F\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(G\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(H\\)</span></span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(A\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(B\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(C\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(D\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(E\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(F\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(G\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(H\\)</span></span></div>

   For (ii), as <span class="math-inline">\\(p \to \infty\\)</span>, the largest value of <span class="math-inline">\\(|y&#95;i-w|\\)</span> dominates. So we should put <span class="math-inline">\\(w\\)</span> halfway between the smallest and largest data values, as discussed in [Chapter 1.4](https://notes.eecs245.org/introduction-to-supervised-learning/comparing-loss-functions/#beyond-absolute-and-squared-loss).

<div class="math-display">
$$
w^* = \frac{3+13}{2} = \boxed{8}
$$
</div>

</details>

3.  (3 pts) What value of <span class="math-inline">\\(w^{\ast}\\)</span> minimizes <span class="math-inline">\\(R(w) = \displaystyle \frac{1}{4} \sum&#95;{i=1}^4 (\log(y&#95;i) - \log(w))^2\\)</span>?

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(A\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(B\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(C\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(D\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(E\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(F\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(G\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(H\\)</span></span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(A\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(B\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(C\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(D\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(E\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(F\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(G\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(H\\)</span></span></div>

   For (iii), let <span class="math-inline">\\(u=\log(w)\\)</span>. The problem is now asking for the best constant prediction for the transformed values <span class="math-inline">\\(\log(y&#95;i)\\)</span>, so

<div class="math-display">
$$
u^* = \frac{\log(3)+\log(6)+\log(6)+\log(13) = \log(3 \cdot 6 \cdot 6 \cdot 13)}{4}
$$
</div>

 Exponentiating gives

<div class="math-display">
$$
w^* = e^{u^*} = \boxed{(3 \cdot 6 \cdot 6 \cdot 13)^{1/4}}
$$
</div>

 This was also a homework problem.
</details>

4.  (3 pts) The slope of the graph of <span class="math-inline">\\(R(w) = \displaystyle\frac{1}{4} \sum&#95;{i = 1}^4 |y&#95;i - w|\\)</span> at <span class="math-inline">\\(w = \alpha\\)</span> is <span class="math-inline">\\(-1/2\\)</span>. Among the options above, which could be <span class="math-inline">\\(\alpha\\)</span>?

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(A\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(B\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(C\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(D\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(E\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(F\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(G\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(H\\)</span></span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(A\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\(B\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(C\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(D\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(E\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(F\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(G\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(H\\)</span></span></div>

   For (iv), the slope of mean absolute error at any <span class="math-inline">\\(w\\)</span> that is not a data point is



<div class="math-display">
$$
\frac{\text{\# left of } w - \text{\# right of } w}{n}
$$
</div>

   Here, in order to achieve a slope of <span class="math-inline">\\(-1/2\\)</span>, we need to have 1 data point to the left of <span class="math-inline">\\(w\\)</span> and 3 to the right, since <span class="math-inline">\\(\frac{1-3}{4} = -1/2\\)</span>. This means we need <span class="math-inline">\\(w\\)</span> to be between <span class="math-inline">\\(3\\)</span> and <span class="math-inline">\\(6\\)</span>, **exclusive**. The only value in this interval is <span class="math-inline">\\(B\\)</span>,



<div class="math-display">
$$
\boxed{\dfrac{4}{\frac{1}{3}+\frac{1}{6}+\frac{1}{6}+\frac{1}{13}} \approx 5.37}
$$
</div>

</details>
