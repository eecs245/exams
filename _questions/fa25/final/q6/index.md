---
number: 6
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> <span class="badge" data-flag="mt2-redemption" style="background-color: #9A3324; color: #FFFFFF; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">MT2 Redemption</span>
points: 4
flags: [mt2-redemption]
has_solution: true
images: []
---

Suppose <span class="math-inline">\\(A\\)</span> and <span class="math-inline">\\(B\\)</span> are both (not necessarily symmetric!) <span class="math-inline">\\(n \times n\\)</span> matrices. Which of the following is <span class="math-inline">\\(\nabla f(\vec x)\\)</span>, the gradient of

<div class="math-display">
$$
f(\vec x) = (A \vec x)^T (B \vec x)
$$
</div>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(2AB \vec x\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(A^TB \vec x\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(2A^TB \vec x\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(2B^TA \vec x\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\((A^TB + B^TA) \vec x\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\((A^TB - B^TA) \vec x\\)</span></span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(2AB \vec x\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(A^TB \vec x\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(2A^TB \vec x\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\(2B^TA \vec x\\)</span></span><span class="mc-option"><span class="mc-bubble mc-correct" aria-hidden="true"></span> <span class="math-inline">\\((A^TB + B^TA) \vec x\\)</span></span><span class="mc-option"><span class="mc-bubble" aria-hidden="true"></span> <span class="math-inline">\\((A^TB - B^TA) \vec x\\)</span></span></div>

We can rewrite the function as

<div class="math-display">
$$
f(\vec x) = (A\vec x)^T(B\vec x) = \vec x^T A^T B \vec x
$$
</div>

 If <span class="math-inline">\\(M\\)</span> is any matrix, then

<div class="math-display">
$$
\nabla(\vec x^T M \vec x) = (M + M^T)\vec x
$$
</div>

 Here, <span class="math-inline">\\(M = A^TB\\)</span>, so

<div class="math-display">
$$
\nabla f(\vec x) = \left(A^TB + (A^TB)^T\right)\vec x = \boxed{(A^TB + B^TA)\vec x}
$$
</div>

</details>
