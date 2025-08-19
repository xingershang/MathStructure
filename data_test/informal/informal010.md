## Goal

$$
\lim_{n \to \infty} \frac{q^n}{n!} = 0;
$$

here $q$ is any real number, $n \in \mathbb{N}$, and $n! := 1 \cdot 2 \cdot \ldots \cdot n$.

**Proof.** If $q = 0$, the assertion is obvious. Further, since $\left|\frac{q^n}{n!}\right| = \frac{|q|^n}{n!}$, it suffices to prove the assertion for $q > 0$. Reasoning as in Example 11, we remark that $x_{n+1} = \frac{q}{n+1} x_n$. Since the set of natural numbers is not bounded above, there exists an index $N$ such that $0 < \frac{q}{n+1} < 1$ for all $n > N$. Then for $n > N$ we shall have $x_{n+1} < x_n$, and since the terms of the sequence are positive, one can now guarantee that the limit $\lim_{n \to \infty} x_n = x$ exists. But then

$$
x = \lim_{n \to \infty} x_{n+1} = \lim_{n \to \infty} \frac{q}{n+1} x_n = \frac{q}{\lim_{n \to \infty} (n + 1)} \cdot \lim_{n \to \infty} x_n = 0 \cdot x = 0.
$$