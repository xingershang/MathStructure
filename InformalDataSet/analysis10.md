# Natural Language

## Goal

Let $\{x_n\}$ and $\{y_n\}$ be numerical sequences. Prove that if $\lim_{n \to \infty} x_n = A$ and $\lim_{n \to \infty} y_n = B$, then $\lim_{n \to \infty} \frac{x_n}{y_n} = \frac{A}{B}$, provided $y_n \neq 0$ $(n = 1, 2, \ldots)$ and $B \neq 0$.

$Proof.$

We use the estimate

$$
\left| \frac{A}{B} - \frac{x_n}{y_n} \right| \leq \frac{|x_n| \Delta(y_n) + |y_n| \Delta(x_n)}{y_n^2} \cdot \frac{1}{1 - \delta(y_n)},
$$

where $\delta(y_n) = \frac{\Delta(y_n)}{|y_n|}$.

For a given $\varepsilon > 0$ we find numbers $N'$ and $N''$ such that

$$
\forall n > N' \left( \Delta(x_n) < \min \left\{ 1, \frac{\varepsilon |B|}{8} \right\} \right),
$$

$$
\forall n > N'' \left( \Delta(y_n) < \min \left\{ \frac{|B|}{4}, \frac{\varepsilon \cdot B^2}{16(|A| + 1)} \right\} \right).
$$

Then for $n > \max\{N', N''\}$ we shall have

$$
|x_n| < |A| + \Delta(x_n) < |A| + 1,
$$

$$
|y_n| > |B| - \Delta(y_n) > |B| - \frac{|B|}{4} > \frac{|B|}{2},
$$

$$
\frac{1}{|y_n|} < \frac{2}{|B|},
$$

$$
0 < \delta(y_n) = \frac{\Delta(y_n)}{|y_n|} < \frac{|B| / 4}{|B| / 2} = \frac{1}{2},
$$

$$
1 - \delta(y_n) > \frac{1}{2},
$$

and therefore

$$
|x_n| \cdot \frac{1}{y_n^2} \Delta(y_n) < (|A| + 1) \cdot \frac{4}{B^2} \cdot \frac{\varepsilon \cdot B^2}{16(|A| + 1)} = \frac{\varepsilon}{4},
$$

$$
\left| \frac{1}{y_n} \right| \Delta(x_n) < \frac{2}{|B|} \cdot \frac{\varepsilon |B|}{8} = \frac{\varepsilon}{4},
$$

$$
0 < \frac{1}{1 - \delta(y_n)} < 2,
$$

and consequently

$$
\left| \frac{A}{B} - \frac{x_n}{y_n} \right| < \varepsilon \text{ when } n > N.
$$

$Qed.$