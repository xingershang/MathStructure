## Goal

For any $ n $ positive integers $ a_1, a_2, \ldots, a_n $, we have

$$
\frac{a_1 + a_2 + \cdots + a_n}{n} \geq \sqrt[n]{a_1 a_2 \cdots a_n} \geq n \left( \frac{1}{a_1} + \frac{1}{a_2} + \cdots + \frac{1}{a_n} \right)^{-1},
$$

with equality if and only if $ a_1 = a_2 = \cdots = a_n $.

**Proof**: First, we prove the inequality on the left-hand side

$$
\frac{a_1 + a_2 + \cdots + a_n}{n} \geq \sqrt[n]{a_1 a_2 \cdots a_n}.
$$

When $ n = 1, 2 $, the inequality is obviously true.

When $ n = 2^k (k \in \mathbb{N}^*) $, the inequality is the direct result of $ \frac{a + b}{2} \geq \sqrt{ab} $.

When $ n \neq 2^k $, take $ l \in \mathbb{N}^* $ such that $ 2^{l-1} < n < 2^l $. Let

$$
\sqrt[n]{a_1 a_2 \cdots a_n} = \bar{a}.
$$

Add $ (2^l - n) $ $ \bar{a} $'s to $ a_1, a_2, \ldots, a_n $ to make it $ 2^l $ positive integers. Applying the inequality to these $ 2^l $ positive integers, we get

$$
\frac{1}{2^l} \left[ a_1 + a_2 + \cdots + a_n + (2^l - n) \bar{a} \right] \geq (\bar{a})^{1/2^l} = \bar{a}.
$$

After rearranging, we have

$$
\frac{a_1 + a_2 + \cdots + a_n}{n} \geq \sqrt[n]{a_1 a_2 \cdots a_n}.
$$

For $ \frac{1}{a_1}, \frac{1}{a_2}, \ldots, \frac{1}{a_n} $, using the above conclusion, we obtain the inequality on the right-hand side.

**Q.E.D.**