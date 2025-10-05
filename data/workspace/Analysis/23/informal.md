## Goal

Let $ T = \{ x \mid x \in \mathbb{Q} \text{ and } x > 0, x^2 < 2 \} $. Prove that $ T $ has no least upper bound in $ \mathbb{Q} $.

**Proof**: By contradiction, suppose $ T $ has a least upper bound in $ \mathbb{Q} $. Let $ \sup T = \frac{n}{m} $ (where $ m, n \in \mathbb{N}^* $ and $ m, n $ are coprime). Then it is obvious that

$$
1 < \left( \frac{n}{m} \right)^2 < 3.
$$

Since the square of a rational number cannot be 2, there are only two possible cases:

1. $ 1 < \left( \frac{n}{m} \right)^2 < 2 $.

    Let $ \frac{n^2}{m^2} = 2 - t $, where $ 0 < t < 1 $. Let $ r = \frac{n}{6m} $, then it is obvious that $ n + r > 0 $, $ \frac{n + r}{m} \in \mathbb{Q} $. Since

    $$
    \frac{n^2}{3m^2} t < \frac{2}{3}, \quad \frac{2n}{m} - r < \frac{n}{18} t,
    $$

    we get

    $$
    \left( \frac{n + r}{m} \right)^2 = \frac{n^2}{m^2} + \frac{2n}{m} r + r^2 = 2 - t + \frac{2n}{m} r + r^2 < 2.
    $$

    This implies $ \frac{n + r}{m} \in T $, contradicting the assumption that $ \frac{n}{m} $ is the least upper bound of $ T $.

2. $ 2 < \left( \frac{n}{m} \right)^2 < 3 $.

    Let $ \frac{n^2}{m^2} = 2 + t $, where $ 0 < t < 1 $. Let $ r = \frac{n}{6m} $, then it is obvious that $ n - r > 0 $, $ \frac{n - r}{m} \in \mathbb{Q} $. Since

    $$
    \frac{2n}{m} - r < \frac{n^2}{3m^2} t < 1,
    $$

    we get

    $$
    \left( \frac{n - r}{m} \right)^2 = \frac{n^2}{m^2} - \frac{2n}{m} r + r^2 = 2 + t - \frac{2n}{m} r + r^2 > 2.
    $$

    This implies $ \frac{n - r}{m} \in T $, contradicting the assumption that $ \frac{n}{m} $ is the least upper bound of $ T $.

Therefore, we conclude that $ T $ has no least upper bound in $ \mathbb{Q} $.

**Q.E.D.**