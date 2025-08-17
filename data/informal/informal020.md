Let $\{x_n\}$ and $\{y_n\}$ be numerical sequences. Prove that if $\lim_{n \to \infty} x_n = A$ and $\lim_{n \to \infty} y_n = B$, then $\lim_{n \to \infty} (x_n + y_n) = A + B$.

$Proof.$

Denote $|A - x_n| = \Delta(x_n)$, $|B - y_n| = \Delta(y_n)$. Then we have

$$
|(A + B) - (x_n + y_n)| \leq \Delta(x_n) + \Delta(y_n).
$$

Suppose $\varepsilon > 0$ is given. Since $\lim_{n \to \infty} x_n = A$, there exists $N'$ such that $\Delta(x_n) < \varepsilon / 2$ for all $n > N'$. Similarly, since $\lim_{n \to \infty} y_n = B$, there exists $N''$ such that $\Delta(y_n) < \varepsilon / 2$ for all $n > N''$. Then for $n > \max\{N', N''\}$ we shall have

$$
|(A + B) - (x_n + y_n)| < \varepsilon,
$$

which, by definition of limit, gives us $\lim_{n \to \infty} (x_n + y_n) = A + B$.

$Qed.$