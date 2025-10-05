## Goal

The function $ f(x) = x^2 $ is not uniformly continuous on $[0, +\infty)$, but it is uniformly continuous on $[0, A]$ for any finite positive number $ A $.

**Proof**: Let $ x_n' = \sqrt{n+1} $ and $ x_n'' = \sqrt{n} $ (where $ n = 1, 2, 3, \ldots $). Then

$$
\lim_{n \to \infty} (x_n' - x_n'') = \lim_{n \to \infty} (\sqrt{n+1} - \sqrt{n}) = 0,
$$

but

$$
\lim_{n \to \infty} (f(x_n') - f(x_n'')) = 1.
$$

By Example 3.4.5, we know that $ f(x) $ is not uniformly continuous on $[0, +\infty)$.

When the interval is restricted to $[0, A]$, we have

$$
|x'^2 - x''^2| = |(x' + x'')(x' - x'')| \leq 2A |x' - x''|.
$$

For any given $ \epsilon > 0 $, we can take $ \delta = \frac{\epsilon}{2A} > 0 $. For any $ x', x'' \in [0, A] $, as long as $ |x' - x''| < \delta $, it follows that

$$
|x'^2 - x''^2| < \epsilon.
$$

Therefore, $ f(x) = x^2 $ is uniformly continuous on $[0, A]$.

**Q.E.D.**