## Goal

Every bounded sequence of real numbers contains a convergent subsequence.

**Proof.** Let $E$ be the set of values of the bounded sequence $\{x_n\}$. If $E$ is finite, there exists a point $x \in E$ and a sequence $n_1 < n_2 < \cdots$ of indices such that $x_{n_1} = x_{n_2} = \cdots = x$. The subsequence $\{x_{n_k}\}$ is constant and hence converges.

If $E$ is infinite, then by the Bolzano–Weierstrass principle it has a limit point $x$. Since $x$ is a limit point of $E$, one can choose $n_1 \in \mathbb{N}$ such that $|x_{n_1} - x| < 1$. If $n_k \in \mathbb{N}$ have been chosen so that $|x_{n_k} - x| < \frac{1}{k}$, then, because $x$ is a limit point of $E$, there exists $n_{k+1} \in \mathbb{N}$ such that $n_k < n_{k+1}$ and $|x_{n_{k+1}} - x| < \frac{1}{k+1}$.

Since $\lim_{k \to \infty} \frac{1}{k} = 0$, the sequence $x_{n_1}, x_{n_2}, \ldots, x_{n_k}, \ldots$ so constructed converges to $x$.