---
number: 5
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> <span class="badge" data-flag="mt2-redemption" style="background-color: #9A3324; color: #FFFFFF; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">MT2 Redemption</span>
points: 4
flags: [mt2-redemption]
has_solution: true
images: []
---

Suppose <span class="math-inline">\\(A\\)</span> is a <span class="math-inline">\\(7 \times 12\\)</span> matrix. Fill in each blank with an integer with no variables.

1.  (2 pts) What is the minimum possible value of <span class="math-inline">\\(\text{dim}(\text{nullsp}(A))\\)</span>? \_\_\_\_\_\_

2.  (2 pts) What is the maximum possible value of <span class="math-inline">\\(\text{dim}(\text{nullsp}(A))\\)</span>? \_\_\_\_\_\_

<details markdown="1"><summary>Solution</summary>

By the rank-nullity theorem from [Chapter 5.4](https://notes.eecs245.org/matrices/null-space-rank-nullity/), 

<div class="math-display">
$$
\text{rank}(A)+\text{dim}(\text{nullsp}(A))=12
$$
</div>

 The rank of a <span class="math-inline">\\(7\times 12\\)</span> matrix is at least <span class="math-inline">\\(0\\)</span> and at most <span class="math-inline">\\(7\\)</span>. So the dimension of the null space is 

<div class="math-display">
$$
\text{dim}(\text{nullsp}(A))=12-\text{rank}(A)
$$
</div>

 This is as small as possible when <span class="math-inline">\\(\text{rank}(A)=7\\)</span>, giving minimum <span class="math-inline">\\(\text{dim}(\text{nullsp}(A)) = 5\\)</span>, and as large as possible when <span class="math-inline">\\(\text{rank}(A)=0\\)</span>, giving maximum <span class="math-inline">\\(\text{dim}(\text{nullsp}(A)) = 12\\)</span>.
</details>
