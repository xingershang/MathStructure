# Natural Language

## Goal

Prove that the function $ f(x) = \sin x $ is continuous and uniformly continuous on $(-\infty, +\infty)$.

**Proof**: By the inequality
$$
| \sin x' - \sin x'' | = 2 \left| \cos \frac{x' + x''}{2} \sin \frac{x' - x''}{2} \right| \leq | x' - x'' |,
$$

for any given $ \epsilon > 0 $, take $ \delta = \epsilon $. Then for any two points $ x', x'' \in (-\infty, +\infty) $, as long as $ | x' - x'' | < \delta $, it follows that

$$
| \sin x' - \sin x'' | \leq | x' - x'' | < \delta = \epsilon.
$$

By definition, $ \sin x $ is uniformly continuous on $(-\infty, +\infty)$.

**Q.E.D.**