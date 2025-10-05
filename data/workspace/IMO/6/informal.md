## Goal

Let $a_1, a_2, \ldots, a_{100}$ be nonnegative real numbers such that $a_1^2 + a_2^2 + \cdots + a_{100}^2 = 1$. Prove that
$$
a_1^2 a_2 + a_2^2 a_3 + \cdots + a_{100}^2 a_1 < \frac{12}{25}.
$$

## Proof

Let $S = \sum_{k=1}^{100} a_k^2 a_{k+1}$. (As usual, we consider the indices modulo 100, e.g. we set $a_{101} = a_1$ and $a_{102} = a_2$.)

Applying the Cauchy-Schwarz inequality to sequences $(a_{k+1})$ and $(a_k^2 + 2a_k a_{k+1} a_{k+2})$, and then the AM-GM inequality to numbers $a_k^2 a_{k+1}$ and $a_k^2 a_{k+2}$,

$$
(3S)^2 = \left( \sum_{k=1}^{100} a_{k+1} (a_k^2 + 2a_k a_{k+1} a_{k+2}) \right)^2 \leq \left( \sum_{k=1}^{100} a_{k+1}^2 \right) \left( \sum_{k=1}^{100} (a_k^2 + 2a_k a_{k+1} a_{k+2})^2 \right)
$$

$$
= 1 \cdot \sum_{k=1}^{100} (a_k^4 + 4a_k^2 a_{k+1} a_k a_{k+2} + 4a_k^2 a_{k+1}^2) 
$$

$$
\leq \sum_{k=1}^{100} (a_k^4 + 2a_k^2 (a_k^2 + a_{k+2}^2) + 4a_k^2 a_{k+1}^2) = \sum_{k=1}^{100} (a_k^4 + 6a_k^2 a_{k+1}^2 + 2a_k^2 a_{k+2}^2).
$$

Applying the trivial estimates

$$
\sum_{k=1}^{100} (a_k^4 + 2a_k^2 a_{k+1}^2 + 2a_k^2 a_{k+2}^2) \leq \left( \sum_{k=1}^{100} a_k^2 \right)^2 
$$

and 

$$
\sum_{k=1}^{100} a_{2i-1}^2 a_{2i}^2 \leq \left( \sum_{i=1}^{50} a_{2i-1}^2 \right) \left( \sum_{j=1}^{50} a_{2j}^2 \right),
$$

we obtain that

$$
(3S)^2 \leq \left( \sum_{k=1}^{100} a_k^2 \right)^2 + 4 \left( \sum_{i=1}^{50} a_{2i-1}^2 \right) \left( \sum_{j=1}^{50} a_{2j}^2 \right) \leq 1 + \left( \sum_{i=1}^{50} a_{2i-1}^2 + \sum_{j=1}^{50} a_{2j}^2 \right)^2 = 2,
$$

hence

$$
S \leq \frac{\sqrt{2}}{3} \approx 0.4714 < \frac{12}{25} = 0.48.
$$

$Qed.$