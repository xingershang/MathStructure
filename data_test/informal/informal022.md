## Goal

If $ \lim_{x \to x_0} f(x) = A $, $ \lim_{x \to x_0} g(x) = B $, and $ A > B $, then there exists $ \delta > 0 $ such that for $ 0 < |x - x_0| < \delta $, we have $ f(x) > g(x) $.

**Proof**: Let $ \epsilon_0 = \frac{A - B}{2} > 0 $. Since $ \lim_{x \to x_0} f(x) = A $, there exists $ \delta_1 > 0 $ such that for all $ x $ satisfying $ 0 < |x - x_0| < \delta_1 $,

$$
|f(x) - A| < \epsilon_0 \implies f(x) > \frac{A + B}{2}.
$$

Since $ \lim_{x \to x_0} g(x) = B $, there exists $ \delta_2 > 0 $ such that for all $ x $ satisfying $ 0 < |x - x_0| < \delta_2 $,

$$
|g(x) - B| < \epsilon_0 \implies g(x) < \frac{A + B}{2}.
$$

Let $ \delta = \min \{ \delta_1, \delta_2 \} $. Then for $ 0 < |x - x_0| < \delta $,

$$
g(x) < \frac{A + B}{2} < f(x).
$$

Therefore, $ f(x) > g(x) $ for $ 0 < |x - x_0| < \delta $.

**Q.E.D.**