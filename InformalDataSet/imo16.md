# Natural Language

## Goal

Given six positive numbers $a, b, c, d, e, f$ such that $a < b < c < d < e < f$. Let $a + c + e = S$ and $b + d + f = T$. Prove that

$$
2ST > \sqrt{3(S + T)} (S(bd + bf + df) + T(ac + ae + ce)).
$$

## Proof

We define also $\sigma = ac + ce + ae, \tau = bd + bf + df$. The idea of the solution is to interpret (1) as a natural inequality on the roots of an appropriate polynomial.

Actually, consider the polynomial

$$
P(x) = (b + d + f)(x - a)(x - c)(x - e) + (a + c + e)(x - b)(x - d)(x - f)
$$

$$
= T(x^3 - Sx^2 + \sigma x - ace) + S(x^3 - Tx^2 + \tau x - bdf).
$$

Surely, $P$ is cubic with leading coefficient $S + T > 0$. Moreover, we have

$$
P(a) = S(a - b)(a - d)(a - f) < 0, \quad P(c) = S(c - b)(c - d)(c - f) > 0,
$$

$$
P(e) = S(e - b)(e - d)(e - f) < 0, \quad P(f) = T(f - a)(f - c)(f - e) > 0.
$$

Hence, each of the intervals $(a, c), (c, e), (e, f)$ contains at least one root of $P(x)$. Since there are at most three roots at all, we obtain that there is exactly one root in each interval (denote them by $\alpha \in (a, c), \beta \in (c, e), \gamma \in (e, f)$). Moreover, the polynomial $P$ can be factorized as

$$
P(x) = (T + S)(x - \alpha)(x - \beta)(x - \gamma).
$$

Equating the coefficients in the two representations (2) and (3) of $P(x)$ provides

$$
\alpha + \beta + \gamma = \frac{2TS}{T + S}, \quad \alpha \beta + \alpha \gamma + \beta \gamma = \frac{S \tau + T \sigma}{T + S}.
$$

Now, since the numbers $\alpha, \beta, \gamma$ are distinct, we have

$$
0 < (\alpha - \beta)^2 + (\alpha - \gamma)^2 + (\beta - \gamma)^2 = 2(\alpha + \beta + \gamma)^2 - 6(\alpha \beta + \alpha \gamma + \beta \gamma),
$$

which implies

$$
\frac{4S^2 T^2}{(T + S)^2} = (\alpha + \beta + \gamma)^2 > 3(\alpha \beta + \alpha \gamma + \beta \gamma) = \frac{3(S \tau + T \sigma)}{T + S},
$$

or

$$
4S^2 T^2 > 3(T + S)(T \sigma + S \tau),
$$

which is exactly what we need.