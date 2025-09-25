# Natural Language

## Goal

If there exists $ r > 0 $ such that for $ 0 < |x - x_0| < r $, we have $ g(x) \leq f(x) \leq h(x) $, and $ \lim_{x \to x_0} g(x) = \lim_{x \to x_0} h(x) = A $, then $ \lim_{x \to x_0} f(x) = A $.

**Proof**: For any $ \epsilon > 0 $, since $ \lim_{x \to x_0} h(x) = A $, there exists $ \delta_1 > 0 $ such that for all $ x $ satisfying $ 0 < |x - x_0| < \delta_1 $,

$$
|h(x) - A| < \epsilon \implies h(x) < A + \epsilon.
$$

Since $ \lim_{x \to x_0} g(x) = A $, there exists $ \delta_2 > 0 $ such that for all $ x $ satisfying $ 0 < |x - x_0| < \delta_2 $,

$$
|g(x) - A| < \epsilon \implies A - \epsilon < g(x).
$$

Let $ \delta = \min \{ \delta_1, \delta_2, r \} $. Then for $ 0 < |x - x_0| < \delta $,

$$
A - \epsilon < g(x) \leq f(x) \leq h(x) < A + \epsilon.
$$

Thus, $ \lim_{x \to x_0} f(x) = A $.

**Q.E.D.**