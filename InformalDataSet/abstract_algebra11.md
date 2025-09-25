# Natural Language

**2.4.3 Theorem** Let $M$ be an ideal in the commutative ring $R$. Then $M$ is a maximal ideal if and only if $R/M$ is a field.

*Proof.* Suppose $M$ is maximal. We know that $R/M$ is a ring (see (2.2.4)); we need to find the multiplicative inverse of the element $a + M$ of $R/M$, where $a + M$ is not the zero element, i.e., $a \notin M$. Since $M$ is maximal, the ideal $Ra + M$, which contains $a$ and is therefore strictly larger than $M$, must be the ring $R$ itself. Consequently, the identity element $1$ belongs to $Ra + M$. If $1 = ra + m$ where $r \in R$ and $m \in M$, then

$$(r + M)(a + M) = ra + M = (1 - m) + M = 1 + M \text{ since } m \in M,$$

proving that $r + M$ is the multiplicative inverse of $a + M$.

Conversely, if $R/M$ is a field, then $M$ must be a proper ideal. If not, then $M = R$, so that $R/M$ contains only one element, contradicting the requirement that $1 \neq 0$ in $R/M$ (see (7) of (2.1.1)). By (2.2.6), the only ideals of $R/M$ are $\{0\}$ and $R/M$, so by the correspondence theorem (2.3.5), there are no ideals properly between $M$ and $R$. Therefore $M$ is a maximal ideal. ♣