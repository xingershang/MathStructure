# Natural Language

## Goal

Let $R$ be a Equivalence Relation on $\R$. Define $S_2= \left\{ ([a]_R, [b]_R) \mid \exists a' \in [a]_R, b' \in [b]_R, a' - b' = \frac{1}{2} \right\} \cup \{([a]_R, [a]_R) \mid a \in \mathbb{R} \}$. Prove that $S_2$ is an Equivalence Relation.

## Proof

**Reflexivity:** For all $[a]_R$, $([a]_R, [a]_R) \in S_2$ by definition.

**Symmetry:** If $([a]_R, [b]_R) \in S_2$, there exist $a' \in [a]_R, b' \in [b]_R$ with $a' - b' = \frac{1}{2}$. Let $b'' = b' + 1 \in [b]_R$. Then $b'' - a' = \frac{1}{2}$, so $([b]_R, [a]_R) \in S_2$.

**Transitivity:** Suppose $([a]_R, [b]_R) \in S_2$ and $([b]_R, [c]_R) \in S_2$. Then:

1. $\exists a' \in [a]_R, b_1 \in [b]_R$ with $a' - b_1 = \frac{1}{2}$.
2. $\exists b_2 \in [b]_R, c' \in [c]_R$ with $b_2 - c' = \frac{1}{2}$.

Since $b_1, b_2 \in [b]_R$, $b_1 - b_2 = k \in \mathbb{Z}$. Let $c'' = c' + k \in [c]_R$. Then:

$$
a' - c'' = (a' - b_1) + (b_1 - c'') = \frac{1}{2} + (b_1 - (c' + k)) = \frac{1}{2} - \frac{1}{2} = 0 \implies [a]_R = [c]_R.
$$

Thus, $([a]_R, [c]_R) \in S_2$.
