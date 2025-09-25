# Natural Language

## Goal

Prove that the sequence $y_n = \left(1 + \frac{1}{n}\right)^{n+1}$ is decreasing.

**Proof.** Let $n \geq 2$. Using Bernoulli's inequality, we find that
$$
\frac{y_{n-1}}{y_n} = \frac{\left(1 + \frac{1}{n-1}\right)^n}{\left(1 + \frac{1}{n}\right)^{n+1}} = \frac{n2^n}{(n^2 - 1)^n} \cdot \frac{n}{n + 1} = \left(1 + \frac{1}{n^2 - 1}\right)^n \cdot \frac{n}{n + 1} \geq
$$

$$
\left(1 + \frac{n}{n^2 - 1}\right) \cdot \frac{n}{n + 1} > \left(1 + \frac{1}{n}\right) \cdot \frac{n}{n + 1} = 1.
$$

This finishes the proof.

