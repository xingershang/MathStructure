## Goal

If a function $ f(x) $ is continuous on the closed interval $[a, b]$, then it takes on any value between its maximum value $ M = \max \{ f(x) \mid x \in [a, b] \} $ and its minimum value $ m = \min \{ f(x) \mid x \in [a, b] \} $.

**Proof**: By the Extreme Value Theorem, there exist $ \xi, \eta \in [a, b] $ such that
$$
f(\xi) = m, \quad f(\eta) = M.
$$

Without loss of generality, assume $ \xi < \eta $. For any intermediate value $ C $ such that $ m < C < M $, consider the auxiliary function

$$
\varphi(x) = f(x) - C.
$$

Since $ \varphi(x) $ is continuous on the interval $[ \xi, \eta ]$, $ \varphi(\xi) = f(\xi) - C < 0 $ and $ \varphi(\eta) = f(\eta) - C > 0 $. By the Intermediate Value Theorem, there must exist a $ \zeta \in (\xi, \eta) $ such that

$$
\varphi(\zeta) = 0,
$$

which means

$$
f(\zeta) = C.
$$

**Q.E.D.**