## Goal

Let $a, b, c$ be positive real numbers such that $\frac{1}{a} + \frac{1}{b} + \frac{1}{c} = a + b + c$. Prove that

$$
\frac{1}{(2a + b + c)^2} + \frac{1}{(2b + c + a)^2} + \frac{1}{(2c + a + b)^2} \leq \frac{3}{16}.
$$

## Proof

For positive real numbers $x, y, z$, from the arithmetic-geometric-mean inequality,

$$
2x + y + z = (x + y) + (x + z) \geq 2\sqrt{(x + y)(x + z)},
$$

we obtain

$$
\frac{1}{(2x + y + z)^2} \leq \frac{1}{4(x + y)(x + z)}.
$$

Applying this to the left-hand side terms of the inequality to prove, we get
$$
\frac{1}{(2a + b + c)^2} + \frac{1}{(2b + c + a)^2} + \frac{1}{(2c + a + b)^2}
$$

$$
\leq \frac{1}{4(a + b)(a + c)} + \frac{1}{4(b + c)(b + a)} + \frac{1}{4(c + a)(c + b)}
$$

$$
= \frac{(b + c) + (c + a) + (a + b)}{4(a + b)(b + c)(c + a)} = \frac{a + b + c}{2(a + b)(b + c)(c + a)}\tag{1}
$$

A second application of the inequality of the arithmetic-geometric mean yields

$$
a^2b + a^2c + b^2a + b^2c + c^2a + c^2b \geq 6abc,
$$

or, equivalently,

$$
9(a + b)(b + c)(c + a) \geq 8(a + b + c)(ab + bc + ca). \tag{2}
$$

The supposition $\frac{1}{a} + \frac{1}{b} + \frac{1}{c} = a + b + c$ can be written as
$$
ab + bc + ca = abc(a + b + c). \tag{3}
$$

Applying the arithmetic-geometric-mean inequality $x^2y^2 + x^2z^2 \geq 2x^2yz$ thrice, we get

$$
a^2b^2 + b^2c^2 + c^2a^2 \geq a^2bc + ab^2c + abc^2,
$$

which is equivalent to

$$
(ab + bc + ca)^2 \geq 3abc(a + b + c). \tag{4}
$$

Combining (1), (2), (3), and (4), we will finish the proof:
$$
\frac{a + b + c}{2(a + b)(b + c)(c + a)} = \frac{(a + b + c)(ab + bc + ca)}{2(a + b)(b + c)(c + a)} \cdot \frac{ab + bc + ca}{abc(a + b + c)} = \frac{abc(a + b + c)}{(ab + bc + ca)^2}
$$

$$
\leq \frac{9}{2} \cdot \frac{1}{8} \cdot \frac{1}{3} = \frac{3}{16}.
$$
