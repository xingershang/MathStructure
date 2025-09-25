# Natural Language

2.60  *measure of a decreasing intersection*

Suppose $(X, S, \mu)$ is a measure space and $E_1 \supset E_2 \supset \cdots$ is a decreasing sequence of sets in $S$, with $\mu(E_1) < \infty$. Then

$$
\mu \left( \bigcap_{k=1}^\infty E_k \right) = \lim_{k \to \infty} \mu(E_k).
$$

**Proof** One of De Morgan’s Laws tells us that

$$
E_1 \setminus \bigcap_{k=1}^\infty E_k = \bigcup_{k=1}^\infty (E_1 \setminus E_k).
$$

Now $E_1 \setminus E_1 \subset E_1 \setminus E_2 \subset E_1 \setminus E_3 \subset \cdots$ is an increasing sequence of sets in $S$. Thus 2.59, applied to the equation above, implies that

$$
\mu \left( E_1 \setminus \bigcap_{k=1}^\infty E_k \right) = \lim_{k \to \infty} \mu(E_1 \setminus E_k).
$$

Use 2.57(b) to rewrite the equation above as

$$
\mu(E_1) - \mu \left( \bigcap_{k=1}^\infty E_k \right) = \mu(E_1) - \lim_{k \to \infty} \mu(E_k),
$$

which implies our desired result.
