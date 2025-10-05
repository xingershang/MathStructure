## Goal

Let $n$ be a positive integer, and let $x$ and $y$ be positive real numbers such that $x^n + y^n = 1$. Prove that
$$
\left( \sum_{k=1}^n \frac{1 + x^{2k}}{1 + x^{4k}} \right) \left( \sum_{k=1}^n \frac{1 + y^{2k}}{1 + y^{4k}} \right) < \frac{1}{(1 - x)(1 - y)}.
$$

## Proof

For each real $t \in (0, 1)$,

$$
\frac{1 + t^2}{1 + t^4} = \frac{1}{t} - \frac{(1 - t)(1 - t^3)}{t(1 + t^4)} < \frac{1}{t}.
$$

Substituting $t = x^k$ and $t = y^k$,

$$
0 < \sum_{k=1}^n \frac{1 + x^{2k}}{1 + x^{4k}} < \sum_{k=1}^n \frac{1}{x^k} = \frac{1 - x^n}{x^n (1 - x)}
$$

and

$$
0 < \sum_{k=1}^n \frac{1 + y^{2k}}{1 + y^{4k}} < \sum_{k=1}^n \frac{1}{y^k} = \frac{1 - y^n}{y^n (1 - y)}.
$$

Since $1 - y^n = x^n$ and $1 - x^n = y^n$,

$$
\frac{1 - x^n}{x^n (1 - x)} = \frac{y^n}{x^n (1 - x)}, \quad \frac{1 - y^n}{y^n (1 - y)} = \frac{x^n}{y^n (1 - y)},
$$

and therefore

$$
\left( \sum_{k=1}^n \frac{1 + x^{2k}}{1 + x^{4k}} \right) \left( \sum_{k=1}^n \frac{1 + y^{2k}}{1 + y^{4k}} \right) < \frac{y^n}{x^n (1 - x)} \cdot \frac{x^n}{y^n (1 - y)} = \frac{1}{(1 - x)(1 - y)}.
$$
$Qed.$