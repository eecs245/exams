---
number: 4
title: Mission Impossible
heading_suffix: : Mission Impossible <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">12 pts</span>
points: 12
flags: []
has_solution: true
images: []
---

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Suppose <span class="math-inline">\\(\vec u, \vec v \in \mathbb{R}^n\\)</span> are **non-zero** vectors, and suppose that

<div class="math-display">
$$
| \vec u \cdot \vec v | = \lVert \vec u \rVert \lVert \vec v \rVert
$$
</div>

For each statement below, determine whether it is impossible, possible, or guaranteed to be true, given the above assumptions. **Select exactly one option from each row**. The first statement has been done for you as an example.

|  | **statement** | **impossible?** | **possible?** | **guaranteed?** |
|:--:|:---|:--:|:--:|:--:|
| <span class="math-inline">\\(i\\)</span> | <span class="math-inline">\\(\lVert \vec u \rVert = 5\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> |
| <span class="math-inline">\\(ii\\)</span> | <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> are orthogonal | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> |
| <span class="math-inline">\\(iii\\)</span> | <span class="math-inline">\\(\lVert \vec u - \vec v \rVert = 0\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> |
| <span class="math-inline">\\(iv\\)</span> | <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> span a 1-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^n\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> |
| <span class="math-inline">\\(v\\)</span> | <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> span a 2-dimensional subspace of <span class="math-inline">\\(\mathbb{R}^n\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> |
| <span class="math-inline">\\(vi\\)</span> | <span class="math-inline">\\(\lVert \vec u + \vec v \rVert = \lVert \vec u \rVert + \lVert \vec v \rVert\\)</span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> | <span class="mc-bubble" aria-hidden="true"></span> |

<details markdown="1"><summary>Solution</summary>

Remember that for **any** two vectors <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span>,

<div class="math-display">
$$
\vec u \cdot \vec v = \lVert \vec u \rVert \lVert \vec v \rVert \cos \theta
$$
</div>

The fact that we're told that

<div class="math-display">
$$
| \vec u \cdot \vec v | = \lVert \vec u \rVert \lVert \vec v \rVert
$$
</div>

tells us that <span class="math-inline">\\(\cos \theta = 1\\)</span> or <span class="math-inline">\\(\cos \theta = -1\\)</span>, which means that the angle between <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> is <span class="math-inline">\\(0^\circ\\)</span> or <span class="math-inline">\\(180^\circ\\)</span>, which means that <span class="math-inline">\\(\vec u\\)</span> and <span class="math-inline">\\(\vec v\\)</span> are scalar multiples of each other. (They may point in the same or opposite directions.) This is the key insight to assessing each of the statements.
</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Suppose <span class="math-inline">\\(\vec w, \vec z \in \mathbb{R}^n\\)</span>. Given that <span class="math-inline">\\(\lVert \vec w \rVert = \lVert \vec z \rVert = \lVert \vec w - \vec z \rVert = 1\\)</span>, find <span class="math-inline">\\(\lVert \vec w + \vec z \rVert\\)</span>. Show your work, and <span class="math-inline">\\(\boxed{\text{circle}}\\)</span> your final answer, which should be a number with no variables.

<details markdown="1"><summary>Solution</summary>

<span class="math-inline">\\(\lVert \vec w + \vec z \rVert = \sqrt{3}\\)</span>.

We're asked to find <span class="math-inline">\\(\lVert \vec w + \vec z \rVert\\)</span>. To do so, let's expand out <span class="math-inline">\\(\lVert \vec w + \vec z \rVert^2\\)</span> as we've done in the past, and see how to utilize what we were given.

<div class="math-display">
$$
\begin{align*}
\lVert \vec w + \vec z \rVert^2 &= (\vec w + \vec z) \cdot (\vec w + \vec z) \\\\
&= \vec w \cdot \vec w + 2 \vec w \cdot \vec z + \vec z \cdot \vec z \\\\
&= \lVert \vec w \rVert^2 + 2 \vec w \cdot \vec z + \lVert \vec z \rVert^2 \\\\
&= 1 + 2 \vec w \cdot \vec z + 1 \\\\
&= 2 + 2 \vec w \cdot \vec z
\end{align*}
$$
</div>

Above, we've plugged in <span class="math-inline">\\(\lVert \vec w \rVert^2 = 1\\)</span> and <span class="math-inline">\\(\lVert \vec z \rVert^2 = 1\\)</span>. We need to know <span class="math-inline">\\(\vec w \cdot \vec z\\)</span>, which we don't yet know.

But, we have enough information to find it, if we expand out <span class="math-inline">\\(\lVert \vec w - \vec z \rVert^2\\)</span>, which we were told is equal to 1.

<div class="math-display">
$$
\begin{align*}
\lVert \vec w - \vec z \rVert^2 &= (\vec w - \vec z) \cdot (\vec w - \vec z) \\\\
1 &= \vec w \cdot \vec w - 2 \vec w \cdot \vec z + \vec z \cdot \vec z \\\\
1 &= \lVert \vec w \rVert^2 - 2 \vec w \cdot \vec z + \lVert \vec z \rVert^2 \\\\
1 &= 1 - 2 \vec w \cdot \vec z + 1 \\\\
1 &= 2 - 2 \vec w \cdot \vec z
\end{align*}
$$
</div>

Solving the above gives us <span class="math-inline">\\(\vec w \cdot \vec z = \frac{1}{2}\\)</span>. This gives

<div class="math-display">
$$
\lVert \vec w + \vec z \rVert^2 = 2 + 2 \vec w \cdot \vec z = 2 + 2 \cdot \frac{1}{2} = 3
$$
</div>

And so,

<div class="math-display">
$$
\lVert \vec w + \vec z \rVert = \sqrt{3}
$$
</div>

</details>

</div>
</div>

</div>
