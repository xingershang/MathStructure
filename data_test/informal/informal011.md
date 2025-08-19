## Goal
$$(1 + \alpha)^n \geq 1 + n\alpha \text{ for } n \in \mathbb{N} \text{ and } \alpha > -1.$$

**Proof.** The assertion is true for $n = 1$. If it holds for $n \in \mathbb{N}$, then it must also hold for $n + 1$, since we then have

$$
(1 + \alpha)^{n+1} = (1 + \alpha)(1 + \alpha)^n \geq (1 + \alpha)(1 + n\alpha) = 1 + (n + 1)\alpha + n\alpha^2 \geq 1 + (n + 1)\alpha.
$$

By the principle of induction the assertion is true for all $n \in \mathbb{N}$. Incidentally, the computation shows that strict inequality holds if $\alpha \neq 0$ and $n > 1$. 