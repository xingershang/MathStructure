# Natural Language

## Goal

Let $a, b, c$ be positive real numbers such that $ab + bc + ca \leq 3abc$. Prove that
$$
\sqrt{\frac{a^2 + b^2}{a + b}} + \sqrt{\frac{b^2 + c^2}{b + c}} + \sqrt{\frac{c^2 + a^2}{c + a}} + 3 \leq \sqrt{2} \left( \sqrt{a + b} + \sqrt{b + c} + \sqrt{c + a} \right).
$$

## Proof

Starting with the terms of the right-hand side, the quadratic-arithmetic-mean inequality yields
$$
\sqrt{2} \sqrt{a + b} = 2 \sqrt{\frac{ab}{a + b}} \sqrt{\frac{1}{2} \left( 2 + \frac{a^2 + b^2}{ab} \right)}
$$

$$
\geq 2 \sqrt{\frac{ab}{a + b}} \cdot \frac{1}{2} \left( \sqrt{2} + \sqrt{\frac{a^2 + b^2}{ab}} \right) = \sqrt{\frac{2ab}{a + b}} + \sqrt{\frac{a^2 + b^2}{a + b}}.
$$

and, analogously,

$$
\sqrt{2} \sqrt{b + c} \geq \sqrt{\frac{2bc}{b + c}} + \sqrt{\frac{b^2 + c^2}{b + c}},
$$

$$
\sqrt{2} \sqrt{c + a} \geq \sqrt{\frac{2ca}{c + a}} + \sqrt{\frac{c^2 + a^2}{c + a}}.
$$

Applying the inequality between the arithmetic mean and the squared harmonic mean will finish the proof:

$$
\sqrt{\frac{2ab}{a + b}} + \sqrt{\frac{2bc}{b + c}} + \sqrt{\frac{2ca}{c + a}} \geq 3 \cdot \sqrt{\frac{3}{\frac{a + b}{2ab} + \frac{b + c}{2bc} + \frac{c + a}{2ca}}} = 3 \cdot \sqrt{\frac{3ab}{ab + bc + ca}} \geq 3.
$$

