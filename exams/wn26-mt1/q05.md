---
number: 5
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>
points: 12
flags: []
has_solution: true
images: []
---

Suppose <span class="math-inline">\\(\vec u, \vec v \in \mathbb{R}^n\\)</span>. Let <span class="math-inline">\\(\vec p\\)</span> be the projection of <span class="math-inline">\\(\vec u\\)</span> onto <span class="math-inline">\\(\vec v\\)</span>. Furthermore, we know that:

<div class="math-display">
$$
\underbrace{\lVert \vec v \rVert = 2}_{\text{length of } \vec v \: (\text{not } \vec u)} \qquad \lVert \vec p \rVert = 3
$$
</div>

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Find <span class="math-inline">\\(| \vec u \cdot \vec v |\\)</span>. Show your work and <span class="math-inline">\\(\boxed{\text{circle}}\\)</span> your final answer, which should be a number with no variables.

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(|\vec u \cdot \vec v| = 6\\)</span>.

Let's start with the formula for <span class="math-inline">\\(\vec p\\)</span>.

<div class="math-display">
$$
\vec p = \frac{\vec u \cdot \vec v}{\vec v \cdot \vec v} \vec v = \frac{\vec u \cdot \vec v}{\lVert \vec v \rVert^2} \vec v
$$
</div>

We know that <span class="math-inline">\\(\lVert \vec p \rVert = 3\\)</span>, so let's try and find the magnitude of <span class="math-inline">\\(\vec p\\)</span> in the formula above, which will allow us to learn more about <span class="math-inline">\\(\vec u \cdot \vec v\\)</span>.

The key to remember that <span class="math-inline">\\(\lVert k x \rVert = |k| \lVert x \rVert\\)</span> for any scalar <span class="math-inline">\\(k\\)</span> and vector <span class="math-inline">\\(x\\)</span>. The absolute value is necessary because the scalar <span class="math-inline">\\(k\\)</span> could be negative, but the length of a vector is always non-negative.

<div class="math-display">
$$
\lVert \vec p \rVert = \left| \frac{\vec u \cdot \vec v}{\lVert \vec v \rVert^2} \right| \lVert \vec v \rVert = \left| \frac{\vec u \cdot \vec v}{2^2} \right| 2 = \left| \frac{\vec u \cdot \vec v}{4} \right| 2 = \frac{\left| \vec u \cdot \vec v \right|}{2}
$$
</div>

So, we know that <span class="math-inline">\\(\frac{\left| \vec u \cdot \vec v \right|}{2} = 3\\)</span>, which means that <span class="math-inline">\\(\boxed{\left| \vec u \cdot \vec v \right| = 6}\\)</span>.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> For each pair of vectors, determine whether they are orthogonal, linearly dependent, or neither. Make sure to select **one bubble per row**.

|  | pair of vectors | orthogonal | linearly dependent | neither |
|:--:|:---|:--:|:--:|:--:|
| <span class="math-inline">\\(i\\)</span> | <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec u - \vec p\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> |
| <span class="math-inline">\\(ii\\)</span> | <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v - \vec p\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> |
| <span class="math-inline">\\(iii\\)</span> | <span class="math-inline">\\(\vec v\\)</span> and <span class="math-inline">\\(\vec u - \vec p\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> |
| <span class="math-inline">\\(iv\\)</span> | <span class="math-inline">\\(\vec v\\)</span> and <span class="math-inline">\\(\vec v - \vec p\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> |
| <span class="math-inline">\\(v\\)</span> | <span class="math-inline">\\(\vec p\\)</span> and <span class="math-inline">\\(\vec u - \vec p\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> |
| <span class="math-inline">\\(vi\\)</span> | <span class="math-inline">\\(\vec p\\)</span> and <span class="math-inline">\\(\vec v - \vec p\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> |

<details markdown="1"><summary>Solution</summary>

The key fact about orthogonality when it comes to projections is that the error vector --- here, <span class="math-inline">\\(\vec e = \vec u - \vec p\\)</span> --- is orthogonal to the vector we're projecting onto, <span class="math-inline">\\(\vec v\\)</span>.

This means that <span class="math-inline">\\(\vec v\\)</span> and <span class="math-inline">\\(\vec u - \vec p\\)</span> are orthogonal (iii). But, <span class="math-inline">\\(\vec p\\)</span> is a scalar multiple of <span class="math-inline">\\(\vec v\\)</span>, so <span class="math-inline">\\(\vec p\\)</span> and <span class="math-inline">\\(\vec u - \vec p\\)</span> are also orthogonal (v).

Remember that <span class="math-inline">\\(\vec p\\)</span> is a scalar multiple of <span class="math-inline">\\(\vec v\\)</span>, so <span class="math-inline">\\(\vec v - \vec p\\)</span> is a scalar multiple of <span class="math-inline">\\(\vec v\\)</span> too. So, <span class="math-inline">\\(\vec v\\)</span> and <span class="math-inline">\\(\vec v - \vec p\\)</span> are linearly dependent (iv), as are <span class="math-inline">\\(\vec p\\)</span> and <span class="math-inline">\\(\vec v - \vec p\\)</span> (vi).

Now, we need to address (i) and (ii), which ask about <span class="math-inline">\\(\vec u\\)</span>'s relation to <span class="math-inline">\\(\vec u - \vec p\\)</span> and <span class="math-inline">\\(\vec v - \vec p\\)</span>, respectively. <span class="math-inline">\\(\vec u - \vec p\\)</span> is the error vector of the projection, which in general is orthogonal to <span class="math-inline">\\(\vec v\\)</span> and neither orthogonal nor linearly dependent with <span class="math-inline">\\(\vec u\\)</span>.

The only possible "edge case" here is when <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> are orthogonal, in which case <span class="math-inline">\\(\vec p = \frac{\vec u \cdot \vec v}{\vec v \cdot \vec v} \vec v = \frac{0}{\vec v \cdot \vec v} \vec v = \vec 0\\)</span>, which would mean that <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v - \vec p\\)</span> are orthogonal and <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec u - \vec p\\)</span> are the same vector and thus linearly dependent. However, we know that <span class="math-inline">\\(\vec p \neq \vec 0\\)</span> since <span class="math-inline">\\(\lVert \vec p \rVert = 3 &gt; 0\\)</span>. So, this edge case doesn't apply to this problem, and therefore <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec u - \vec p\\)</span> are neither orthogonal nor linearly dependent (i), and same with <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v - \vec p\\)</span> (ii).
</details>

</div>
</div>

</div>
