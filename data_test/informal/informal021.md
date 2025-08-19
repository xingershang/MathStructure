## Goal

Prove that the limit of the sequence $ \left\{ \frac{n}{n+3} \right\} $ is 1.

**Proof**: For any given $ \epsilon > 0 $, we need to show that
$$
\left| \frac{n}{n+3} - 1 \right| < \epsilon.
$$

We have

$$
\left| \frac{n}{n+3} - 1 \right| = \left| \frac{n - (n+3)}{n+3} \right| = \left| \frac{-3}{n+3} \right| = \frac{3}{n+3}.
$$

To make $ \frac{3}{n+3} < \epsilon $, we need $ n > \frac{3}{\epsilon} - 3 $. We can choose any integer $ N $ greater than $ \frac{3}{\epsilon} - 3 $, for example, $ N = \left\lceil \frac{3}{\epsilon} \right\rceil - 3 $, where $ \left\lceil x \right\rceil $ denotes the ceiling of $ x $.

Therefore, for $ n > N $, we have $ n > \frac{3}{\epsilon} - 3 $, and thus

$$
\left| \frac{n}{n+3} - 1 \right| = \frac{3}{n+3} < \epsilon.
$$

Hence, the limit of the sequence $ \left\{ \frac{n}{n+3} \right\} $ is 1.

**Q.E.D.**