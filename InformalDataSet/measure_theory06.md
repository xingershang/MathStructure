# Natural Language

Now we come to some easy but important properties of $\sigma$-algebras.

2.25  *$\sigma$-algebras are closed under countable intersection*

Suppose $S$ is a $\sigma$-algebra on a set $X$. Then

(a) $X \in S$;

(b) if $D, E \in S$, then $D \cup E \in S$ and $D \cap E \in S$ and $D \setminus E \in S$;

(c) if $E_1, E_2, \ldots$ is a sequence of elements of $S$, then $\bigcap_{k=1}^\infty E_k \in S$.

**Proof** Because $\emptyset \in S$ and $X = X \setminus \emptyset$, the first two bullet points in the definition of $\sigma$-algebra (2.23) imply that $X \in S$, proving (a).

Suppose $D, E \in S$. Then $D \cup E$ is the union of the sequence $D, E, \emptyset, \emptyset, \ldots$ of elements of $S$. Thus the third bullet point in the definition of $\sigma$-algebra (2.23) implies that $D \cup E \in S$.

De Morgan’s Laws tell us that

$$
X \setminus (D \cap E) = (X \setminus D) \cup (X \setminus E).
$$

If $D, E \in S$, then the right side of the equation above is in $S$; hence $X \setminus (D \cap E) \in S$; thus the complement in $X$ of $X \setminus (D \cap E)$ is in $S$; in other words, $D \cap E \in S$.

Because $D \setminus E = D \cap (X \setminus E)$, we see that if $D, E \in S$, then $D \setminus E \in S$, completing the proof of (b).

Finally, suppose $E_1, E_2, \ldots$ is a sequence of elements of $S$. De Morgan’s Laws tell us that

$$
X \setminus \bigcap_{k=1}^\infty E_k = \bigcup_{k=1}^\infty (X \setminus E_k).
$$

The right side of the equation above is in $S$. Hence the left side is in $S$, which implies that $X \setminus \left( X \setminus \bigcap_{k=1}^\infty E_k \right) \in S$. In other words, $\bigcap_{k=1}^\infty E_k \in S$, proving (c).

