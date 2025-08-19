## Goal

$$
\lim_{n \to \infty} \sqrt[n]{a} = 1 \text{ for any } a > 0.
$$

**Proof.** Assume first that $a \geq 1$. For any $\epsilon > 0$ there exists $N \in \mathbb{N}$ such that $1 \leq a < (1 + \epsilon)^n$ for all $n > N$, and we then have $1 \leq \sqrt[n]{a} < 1 + \epsilon$ for all $n > N$, which says $\lim_{n \to \infty} \sqrt[n]{a} = 1$.

For $0 < a < 1$, we have $1 < \frac{1}{a}$, and then

$$
\lim_{n \to \infty} \sqrt[n]{a} = \lim_{n \to \infty} \frac{1}{\sqrt[n]{\frac{1}{a}}} = \frac{1}{\lim_{n \to \infty} \sqrt[n]{\frac{1}{a}}} = 1.
$$