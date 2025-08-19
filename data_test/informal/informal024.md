## Goal

$ f(x) = \sqrt{x(1 - x)} $ is continuous on the closed interval $[0, 1]$.

**Proof**: Let $ x_0 \in (0, 1) $ be any point, and let $ \eta = \min \{x_0, 1 - x_0\} > 0 $. When $ |x - x_0| < \eta $ and $ x \in (0, 1) $, we have
$$
| \sqrt{x(1 - x)} - \sqrt{x_0(1 - x_0)} | = \frac{|(1 - x) - (1 - x_0)| |x - x_0|}{\sqrt{x(1 - x)} + \sqrt{x_0(1 - x_0)}} < \frac{1}{\sqrt{x_0(1 - x_0)}} |x - x_0|.
$$

For any given $ \epsilon > 0 $, let $ \delta = \min \{ \eta, \sqrt{x_0(1 - x_0)} \epsilon \} $. When $ |x - x_0| < \delta $, we have

$$
| \sqrt{x(1 - x)} - \sqrt{x_0(1 - x_0)} | < \frac{1}{\sqrt{x_0(1 - x_0)}} |x - x_0| < \epsilon.
$$

Therefore, $ f(x) = \sqrt{x(1 - x)} $ is continuous on $ (0, 1) $.

Now consider the endpoints. For any given $ \epsilon > 0 $, let $ \delta = \epsilon^2 $. When $ 0 \leq x < \delta $,

$$
| f(x) - f(0) | \leq \sqrt{x} < \epsilon.
$$

And when $ 1 - \delta < x \leq 1 $,

$$
| f(x) - f(1) | \leq \sqrt{1 - x} < \epsilon.
$$

This shows that $ f(x) $ is continuous at $ x = 0 $ from the right and at $ x = 1 $ from the left.

Thus, $ f(x) = \sqrt{x(1 - x)} $ is continuous on the closed interval $[0, 1]$.

**Q.E.D.**