## Goal

Let $\{x_n\}$ and $\{y_n\}$ be numerical sequences. Prove that if $\lim_{n \to \infty} x_n = A$ and $\lim_{n \to \infty} y_n = B$, then $\lim_{n \to \infty} (x_n \cdot y_n) = A \cdot B$.

$Proof.$

We know that

$$
|(A \cdot B) - (x_n \cdot y_n)| \leq |x_n| \Delta(y_n) + |y_n| \Delta(x_n) + \Delta(x_n) \cdot \Delta(y_n).
$$

Given $\varepsilon > 0$ find numbers $N'$ and $N''$ such that

$$
\forall n > N' \left( \Delta(x_n) < \min \left\{ 1, \frac{\varepsilon}{3(|B| + 1)} \right\} \right),
$$

$$
\forall n > N'' \left( \Delta(y_n) < \min \left\{ 1, \frac{\varepsilon}{3(|A| + 1)} \right\} \right).
$$

Then for $n > N = \max\{N', N''\}$ we shall have

$$
|x_n| < |A| + \Delta(x_n) < |A| + 1,
$$

$$
|y_n| < |B| + \Delta(y_n) < |B| + 1,
$$

$$
\Delta(x_n) \cdot \Delta(y_n) < \min \left\{ 1, \frac{\varepsilon}{3} \right\} \cdot \min \left\{ 1, \frac{\varepsilon}{3} \right\} \leq \frac{\varepsilon}{3}.
$$

Hence for $n > N$ we have

$$
|x_n| \Delta(y_n) < (|A| + 1) \cdot \frac{\varepsilon}{3(|A| + 1)} < \frac{\varepsilon}{3},
$$

$$
|y_n| \Delta(x_n) < (|B| + 1) \cdot \frac{\varepsilon}{3(|B| + 1)} < \frac{\varepsilon}{3},
$$

$$
\Delta(x_n) \cdot \Delta(y_n) < \frac{\varepsilon}{3}.
$$

and therefore $|AB - x_n y_n| < \varepsilon$ for $n > N$.

$Qed.$