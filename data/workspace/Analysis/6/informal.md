## Goal

If a function $ f(x) $ is continuous on the interval $[a, b]$ and $ f(a) \cdot f(b) < 0 $, then there exists a $ \xi \in (a, b) $ such that $ f(\xi) = 0 $.

**Proof**: Without loss of generality, assume $ f(a) < 0 $ and $ f(b) > 0 $. Define the set $ V $ as:

$$
V = \{ x \mid f(x) < 0, x \in [a, b] \}.
$$

Clearly, the set $ V $ is bounded and non-empty, so it must have a supremum. Let

$$
\xi = \sup V.
$$

We will show that $ \xi \in (a, b) $ and $ f(\xi) = 0 $.

Due to the continuity of $ f(x) $ and the fact that $ f(a) < 0 $, there exists $ \delta_1 > 0 $ such that for all $ x \in [a, a + \delta_1] $, $ f(x) < 0 $. Similarly, since $ f(b) > 0 $, there exists $ \delta_2 > 0 $ such that for all $ x \in [b - \delta_2, b] $, $ f(x) > 0 $. Therefore, we have

$$
a + \delta_1 \leq \xi \leq b - \delta_2,
$$

which implies $ \xi \in (a, b) $.

Take $ x_n \in V $ for $ n = 1, 2, \ldots $ such that $ x_n \to \xi $ as $ n \to \infty $. Since $ f(x_n) < 0 $, we have

$$
f(\xi) = \lim_{n \to \infty} f(x_n) \leq 0.
$$

If $ f(\xi) < 0 $, due to the continuity of $ f(x) $ at $ \xi $, there exists $ \delta > 0 $ such that for all $ x \in (\xi - \delta, \xi + \delta) $,

$$
f(x) < 0,
$$

which contradicts the fact that $ \xi = \sup V $. Therefore, it must be that

$$
f(\xi) = 0.
$$

**Q.E.D.**