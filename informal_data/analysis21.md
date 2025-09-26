# Natural Language

## Goal

The function $ f(x) = \sin x $ is continuous on $(-\infty, +\infty)$.

**Proof**: Let $ x_0 \in (-\infty, +\infty) $ be an arbitrary point. Since

$$
|\sin x - \sin x_0| = 2 \left| \cos \frac{x + x_0}{2} \sin \frac{x - x_0}{2} \right| \leq |x - x_0|,
$$

for any given $ \epsilon > 0 $, take $ \delta = \epsilon $. When $ |x - x_0| < \delta $, we have

$$
|\sin x - \sin x_0| \leq |x - x_0| < \epsilon.
$$

Therefore, $ f(x) = \sin x $ is continuous on $(-\infty, +\infty)$.

**Q.E.D.**