---
number: 10
title: 
heading_suffix:  <span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">14 pts</span>
points: 14
flags: []
has_solution: true
images: [tikz-4049c66dfd05.svg, tikz-d6c2facf0597.svg]
---

The state diagram below describes a Markov chain with four states.

![image](imgs/tikz-4049c66dfd05.svg)

<div class="assignment-parts" markdown="1">
<div class="assignment-part" markdown="1">
<div class="assignment-part-label">a)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Find the adjacency matrix <span class="math-inline">\\(A\\)</span> for this Markov chain.

<span class="math-inline">\\(A =\\)</span> \_\_\_\_\_\_

<details markdown="1"><summary>Solution</summary>

Column <span class="math-inline">\\(j\\)</span> contains the probabilities of transitioning from state <span class="math-inline">\\(j\\)</span> to all other states; columns must sum to <span class="math-inline">\\(1\\)</span>. Reading from the diagram, the first two columns come from the left "connected component" (made up of states <span class="math-inline">\\(1\\)</span> and <span class="math-inline">\\(2\\)</span>), and the last two columns come from the right connected component. So

<div class="math-display">
$$
\boxed{
A =
\begin{bmatrix}
1/4 & 1/2 & 0 & 0\\\\
3/4 & 1/2 & 0 & 0\\\\
0 & 0 & 2/3 & 1/5\\\\
0 & 0 & 1/3 & 4/5
\end{bmatrix}}
$$
</div>

</details>

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">b)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">6 pts</span> Suppose the chain starts in **state <span class="math-inline">\\(\mathbf{1}\\)</span>**. Fill each box with the **long-run fraction** of time spent in each state. Your answers should be numbers with no variables, and should sum to <span class="math-inline">\\(1\\)</span>.

State 1: \_\_\_\_\_\_ State 2: \_\_\_\_\_\_ State 3: \_\_\_\_\_\_ State 4: \_\_\_\_\_\_

<details markdown="1"><summary>Solution</summary>

As we know from [Chapter 9.3](https://notes.eecs245.org/eigenvalues-and-eigenvectors/markov-chains-adjacency-matrices/), the long-run fraction of time spent in each state is described by the eigenvector of the adjacency matrix corresponding to eigenvalue <span class="math-inline">\\(1\\)</span> (and whose components sum to <span class="math-inline">\\(1\\)</span>).

What is tricky about this particular adjacency matrix is that it has **two linearly independent eigenvectors, both for the eigenvalue <span class="math-inline">\\(1\\)</span>.** Why? Note that the Markov chain has two isolated islands, and its impossible to transition between them. So if we ever start in states <span class="math-inline">\\(1\\)</span> or <span class="math-inline">\\(2\\)</span>, in the long run, we will only spend time in states <span class="math-inline">\\(1\\)</span> and <span class="math-inline">\\(2\\)</span>. Similarly, if we start in states <span class="math-inline">\\(3\\)</span> or <span class="math-inline">\\(4\\)</span>, in the long run, we will only spend time in states <span class="math-inline">\\(3\\)</span> and <span class="math-inline">\\(4\\)</span>.

This means that we can simplify the problem by just looking at the <span class="math-inline">\\(2 \times 2\\)</span> matrix in the top right of <span class="math-inline">\\(A\\)</span> corresponding to the left island (states <span class="math-inline">\\(1\\)</span> and <span class="math-inline">\\(2\\)</span>). This matrix is

<div class="math-display">
$$
A_{\text{left}} = \begin{bmatrix}
1/4 & 1/2 \\\\
3/4 & 1/2
\end{bmatrix}
$$
</div>

All we need to do now is find the eigenvector of <span class="math-inline">\\(A&#95;{\text{left}}\\)</span> corresponding to eigenvalue <span class="math-inline">\\(1\\)</span>. If such an eigenvector is of the form <span class="math-inline">\\(\begin{bmatrix} a \\\\ b \end{bmatrix}\\)</span>, then

<div class="math-display">
$$
\begin{bmatrix} 1/4 & 1/2 \\\\ 3/4 & 1/2 \end{bmatrix} \begin{bmatrix} a \\\\ b \end{bmatrix} = 1 \begin{bmatrix} a \\\\ b \end{bmatrix}
$$
</div>

The first row gives us

<div class="math-display">
$$
\frac{1}{4}a + \frac{1}{2} b = a \implies \frac{1}{2} b = \frac{3}{4}a \implies b = \frac{3}{2}a
$$
</div>

So, if <span class="math-inline">\\(a = 2\\)</span>, then <span class="math-inline">\\(b = 3\\)</span>. But, the steady-state distribution must have components that sum to <span class="math-inline">\\(1\\)</span>, so as probabilities, we're looking at <span class="math-inline">\\(2/5\\)</span> and <span class="math-inline">\\(3/5\\)</span>.

Not only is <span class="math-inline">\\(\begin{bmatrix} 2/5 \\\\ 3/5 \end{bmatrix}\\)</span> an eigenvector of <span class="math-inline">\\(A&#95;{\text{left}}\\)</span> corresponding to eigenvalue <span class="math-inline">\\(1\\)</span>, but

<div class="math-display">
$$
\begin{bmatrix} 2/5 \\\\ 3/5 \\\\ 0 \\\\ 0 \end{bmatrix}
$$
</div>

is an eigenvector of the full matrix <span class="math-inline">\\(A\\)</span> corresponding to eigenvalue <span class="math-inline">\\(1\\)</span>! The 0's in the latter two components effectively "ignore" states <span class="math-inline">\\(3\\)</span> and <span class="math-inline">\\(4\\)</span>, representing the assumption that we start in state <span class="math-inline">\\(1\\)</span>.

So, if we start in state <span class="math-inline">\\(1\\)</span>,

<div class="math-display">
$$
\boxed{\text{State 1: } \frac{2}{5},\quad \text{State 2: } \frac{3}{5},\quad \text{State 3: } 0,\quad \text{State 4: } 0}
$$
</div>

In case you're curious, the other linearly independent eigenvector of <span class="math-inline">\\(A\\)</span> corresponding to eigenvalue <span class="math-inline">\\(1\\)</span> is

<div class="math-display">
$$
\begin{bmatrix} 0 \\\\ 0 \\\\ 3/8 \\\\ 5/8 \end{bmatrix}
$$
</div>

There's a section in [Chapter 9.4](https://notes.eecs245.org/eigenvalues-and-eigenvectors/multiplicities-diagonalization/#example-another-diagonalizable-matrix) about block diagonal matrices that is relevant here.
</details>

Now, consider a **modified** version of the Markov chain. Changes have been emphasized in **bold**.

![image](imgs/tikz-d6c2facf0597.svg)

</div>
</div>

<div class="assignment-part" markdown="1">
<div class="assignment-part-label">c)</div>
<div class="assignment-part-content" markdown="1">
<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">4 pts</span> Consider the statement: "'If we start in \_\_\_\_, the long-run fraction of time spent in each state is the same as in the original chain.''

Which of the following could be placed in the blank to make the statement true? **Select all** that apply.

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> state 1</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> state 2</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> state 3</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> state 4</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> none of these are valid</span></div>

<details markdown="1"><summary>Solution</summary>

<div class="mc-options" markdown="span"><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> state 1</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> state 2</span><span class="mc-option"><span class="mc-square mc-correct" aria-hidden="true"></span> state 3</span><span class="mc-option"><span class="mc-square mc-correct" aria-hidden="true"></span> state 4</span><span class="mc-option"><span class="mc-square" aria-hidden="true"></span> none of these are valid</span></div>

In the modified chain, starting in state <span class="math-inline">\\(1\\)</span> or state <span class="math-inline">\\(2\\)</span> eventually leads to the right connected component, because there is now a positive-probability path from state <span class="math-inline">\\(2\\)</span> to state <span class="math-inline">\\(3\\)</span>. This changes the long-run fractions compared to the original chain. The long-run fraction of time spent in states <span class="math-inline">\\(1\\)</span> and <span class="math-inline">\\(2\\)</span> now will be <span class="math-inline">\\(0\\)</span>.

Starting in state <span class="math-inline">\\(3\\)</span> or state <span class="math-inline">\\(4\\)</span>, the chain stays in the right connected component, and that component has not changed. There is no way to go from state <span class="math-inline">\\(3\\)</span> to <span class="math-inline">\\(2\\)</span> or <span class="math-inline">\\(1\\)</span>. So, the long-run fractions are the same as in the original chain; <span class="math-inline">\\(3/8\\)</span> for state <span class="math-inline">\\(3\\)</span> and <span class="math-inline">\\(5/8\\)</span> for state <span class="math-inline">\\(4\\)</span>, and <span class="math-inline">\\(0\\)</span> for states <span class="math-inline">\\(1\\)</span> and <span class="math-inline">\\(2\\)</span>.

The correct choices are

<div class="math-display">
$$
\boxed{\text{state 3 and state 4}}
$$
</div>

</details>

</div>
</div>

</div>
