## Goal

If $ u = g(x) $ is continuous at $ x_0 $ and $ g(x_0) = u_0 $, and $ y = f(u) $ is continuous at $ u_0 $, then the composite function $ y = f(g(x)) $ is continuous at $ x_0 $.

**Proof**: For any given $ \epsilon > 0 $, since $ \lim_{u \to u_0} f(u) = f(u_0) $, there exists $ \eta > 0 $ such that when $ |u - u_0| < \eta $, we have

$$
|f(u) - f(u_0)| < \epsilon.
$$

For this $ \eta > 0 $, since $ \lim_{x \to x_0} g(x) = g(x_0) = u_0 $, there exists $ \delta > 0 $ such that when $ |x - x_0| < \delta $, we have

$$
|g(x) - u_0| < \eta.
$$

Therefore, when $ |x - x_0| < \delta $, we have

$$
|f(g(x)) - f(g(x_0))| = |f(g(x)) - f(u_0)| < \epsilon,
$$

which means

$$
\lim_{x \to x_0} f(g(x)) = f(g(x_0)).
$$

**Q.E.D.**