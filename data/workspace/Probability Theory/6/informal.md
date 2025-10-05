**Theorem 5.1** (Weak Law of Large Numbers). Let $X_1, X_2, \ldots$ be a sequence of independent, mean zero random variables. Suppose the variance of $X_i$ is less than or equal to $\sigma^2$. Then

$$
\lim_{n \to \infty} \frac{1}{n} S_n = 0 \quad \text{in probability}.
$$

**Proof.** 
$$
E \left\{ \left(\frac{1}{n} \sum_{i=1}^n X_i \right)^2 \right\} = \frac{1}{n^2} \sum_{i=1}^n E\{X_i^2\} \leq \frac{1}{n^2} n \sigma^2 = \frac{\sigma^2}{n}.
$$

Thus by Chebyshev's inequality, if $\epsilon > 0$, then

$$
P \left\{ \frac{1}{n} |S_n| \geq \epsilon \right\} \leq \frac{\sigma^2}{n \epsilon^2} \longrightarrow 0.
$$

Thus $\lim_{n \to \infty} \frac{1}{n} S_n = 0$ in probability, as claimed.  □
