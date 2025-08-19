## Goal

A sequence $\{x_n\}$ is called a **fundamental** or **Cauchy sequence** if for any $\epsilon > 0$ there exists an index $N \in \mathbb{N}$ such that $|x_m - x_n| < \epsilon$ whenever $n > N$ and $m > N$. Prove that a numerical sequence converges if and only if it is a Cauchy sequence.

**Proof.** Suppose $\lim_{n \to \infty} x_n = A$. Given $\epsilon > 0$, we find an index $N$ such that $|x_n - A| < \frac{\epsilon}{2}$ for $n \geq N$. Then if $m > N$ and $n > N$, we have $|x_m - x_n| \leq |x_m - A| + |x_n - A| < \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon$, and we have thus verified that the sequence is a Cauchy sequence.

Now let $\{x_k\}$ be a fundamental sequence. Given $\epsilon > 0$, we find an index $N$ such that $|x_m - x_k| < \frac{\epsilon}{3}$ when $m \geq N$ and $k \geq N$. Fixing $m = N$, we find that for any $k > N$

$$
x_N - \frac{\epsilon}{3} < x_k < x_N + \frac{\epsilon}{3},
$$

but since only a finite number of terms of the sequence have indices not larger than $N$, we have shown that a fundamental sequence is bounded.

For $n \in \mathbb{N}$ we now set $a_n := \inf_{k \geq n} x_k$, and $b_n := \sup_{k \geq n} x_k$.

It is clear from these definitions that $a_n \leq a_{n+1} \leq b_{n+1} \leq b_n$ (since the greatest lower bound does not decrease and the least upper bound does not increase when we pass to a smaller set). By the nested interval principle, there is a point $A$ common to all of the closed intervals $[a_n, b_n]$.

Since

$$
a_n \leq A \leq b_n
$$

for any $n \in \mathbb{N}$ and

$$
a_n = \inf_{k \geq n} x_k \leq x_k \leq \sup_{k \geq n} x_k = b_k
$$

for $k \geq n$, it follows that

$$
|A - x_k| \leq b_n - a_n. \quad (3.2)
$$

But it follows from Eq. (3.1) that

$$
x_N - \frac{\epsilon}{3} \leq \inf_{k \geq n} x_k = a_n \leq b_n = \sup_{k \geq n} x_k \leq x_N + \frac{\epsilon}{3}
$$

for $n > N$, and therefore

$$
b_n - a_n \leq \frac{2\epsilon}{3} < \epsilon \quad (3.3)
$$

for $n > m$. Comparing Eqs. (3.2) and (3.3), we find that

$$
|A - x_k| < \epsilon,
$$

for any $k > N$, and we have proved that $\lim_{k \to \infty} x_k = A$.