# Natural Language

2.58  *countable subadditivity*

Suppose $(X,S,\mu)$ is a measure space and $E_1, E_2, \ldots \in S$. Then

$$
\mu \left( \bigcup_{k=1}^\infty E_k \right) \leq \sum_{k=1}^\infty \mu(E_k).
$$

**Proof** Let $D_1 = \varnothing$ and $D_k = E_1 \cup \cdots \cup E_{k-1}$ for $k \geq 2$. Then

$$
E_1 \setminus D_1, E_2 \setminus D_2, E_3 \setminus D_3, \ldots
$$

is a disjoint sequence of subsets of $X$ whose union equals $\bigcup_{k=1}^\infty E_k$. Thus

$$
\mu \left( \bigcup_{k=1}^\infty E_k \right) = \mu \left( \bigcup_{k=1}^\infty (E_k \setminus D_k) \right)
= \sum_{k=1}^\infty \mu(E_k \setminus D_k)
\leq \sum_{k=1}^\infty \mu(E_k),
$$

where the second line above follows from the countable additivity of $\mu$ and the last line above follows from 2.57(a).
