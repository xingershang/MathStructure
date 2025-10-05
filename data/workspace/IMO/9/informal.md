## Goal

Let $a, b, c, d$ be positive real numbers such that

$$
abcd = 1 \quad \text{and} \quad a + b + c + d > \frac{a}{b} + \frac{b}{c} + \frac{c}{d} + \frac{d}{a}.
$$

Prove that

$$
a + b + c + d < \frac{b}{a} + \frac{c}{b} + \frac{d}{c} + \frac{a}{d}.
$$

## Proof

We show that if $abcd = 1$, the sum $a + b + c + d$ cannot exceed a certain weighted mean of the expressions $\frac{a}{b} + \frac{b}{c} + \frac{c}{d} + \frac{d}{a}$ and $\frac{b}{a} + \frac{c}{b} + \frac{d}{c} + \frac{a}{d}$.

By applying the AM-GM inequality to the numbers $\frac{a}{b}$, $\frac{b}{c}$, $\frac{c}{d}$, and $\frac{d}{a}$, we obtain

$$
a = \sqrt[4]{\frac{a^4}{abcd}} = \sqrt[4]{\frac{a}{b} \cdot \frac{b}{c} \cdot \frac{c}{d} \cdot \frac{d}{a}} \leq \frac{1}{4} \left( \frac{a}{b} + \frac{b}{c} + \frac{c}{d} + \frac{d}{a} \right).
$$

Analogously,

$$
b \leq \frac{1}{4} \left( \frac{b}{c} + \frac{c}{d} + \frac{d}{a} + \frac{a}{b} \right), \quad c \leq \frac{1}{4} \left( \frac{c}{d} + \frac{d}{a} + \frac{a}{b} + \frac{b}{c} \right), \quad \text{and} \quad d \leq \frac{1}{4} \left( \frac{d}{a} + \frac{a}{b} + \frac{b}{c} + \frac{c}{d} \right).
$$

Summing up these estimates yields

$$
a + b + c + d \leq \frac{3}{4} \left( \frac{a}{b} + \frac{b}{c} + \frac{c}{d} + \frac{d}{a} \right) + \frac{1}{4} \left( \frac{b}{a} + \frac{c}{b} + \frac{d}{c} + \frac{a}{d} \right).
$$

In particular, if $a + b + c + d > \frac{a}{b} + \frac{b}{c} + \frac{c}{d} + \frac{d}{a}$, then

$$
a + b + c + d < \frac{b}{a} + \frac{c}{b} + \frac{d}{c} + \frac{a}{d}.
$$

$Qed.$