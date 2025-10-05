Let $\{x_n\}$ be a sequence of real numbers defined by $x_n = n^{(-1)^n}$ for all $n \geq 1$. Prove that $\{x_n\}$ is unbounded and that $\lim\limits_{n \to \infty} x_n = \infty$ does not hold.

**Proof:**

First, for every positive integer $k$, we have:
- $x_{2k} = 2k$
- $x_{2k-1} = \frac{1}{2k-1}$

**(1) Proof that $\{x_n\}$ is unbounded:**

Consider the subsequence $y_k = x_{2k}$. We show that $\{y_k\}$ is unbounded. For any given $M > 0$, choose $k_0 = \lceil M/2 \rceil$. Then for all $k \geq k_0$, we have:
\[
y_k = x_{2k} = 2k \geq 2k_0 \geq M.
\]
Thus, $\{y_k\}$ is unbounded. Since $\{y_k\}$ is a subsequence of $\{x_n\}$, it follows that $\{x_n\}$ is unbounded.

**(2) Proof that $\lim\limits_{n \to \infty} x_n = \infty$ does not hold:**

Consider two subsequences:
- $y_k = x_{2k}$ with $\lim\limits_{k \to \infty} y_k = \lim\limits_{k \to \infty} 2k = +\infty$
- $z_k = x_{2k-1}$ with $\lim\limits_{k \to \infty} z_k = \lim\limits_{k \to \infty} \frac{1}{2k-1} = 0$

Since the subsequence $\{z_k\}$ converges to $0$ (not $\infty$), the limit $\lim\limits_{n \to \infty} x_n = \infty$ cannot hold.

**Q.E.D.**