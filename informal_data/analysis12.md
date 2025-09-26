# Natural Language

## Goal

Suppose the sequences $\{x_n\}$, $\{y_n\}$, and $\{z_n\}$ are such that $x_n \leq y_n \leq z_n$ for all $n > N \in \mathbb{N}$. Prove that if the sequences $\{x_n\}$ and $\{z_n\}$ both converge to the same limit, then the sequence $\{y_n\}$ also converges to that limit.

$Proof.$

Suppose $\lim_{n \to \infty} x_n = \lim_{n \to \infty} z_n = A$. Given $\varepsilon > 0$ choose $N'$ and $N''$ such that $A - \varepsilon < x_n$ for all $n > N'$ and $z_n < A + \varepsilon$ for all $n > N''$. Then for $n > N = \max\{N', N''\}$ we shall have $A - \varepsilon < x_n \leq y_n \leq z_n < A + \varepsilon$, which says $|y_n - A| < \varepsilon$, that is $A = \lim_{n \to \infty} y_n$.

$Qed.$