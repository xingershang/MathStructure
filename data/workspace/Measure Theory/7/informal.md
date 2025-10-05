The next result guarantees that there is a smallest $\sigma$-algebra on a set $X$ containing a given set $\mathcal{A}$ of subsets of $X$.

2.27  *smallest $\sigma$-algebra containing a collection of subsets*

Suppose $X$ is a set and $\mathcal{A}$ is a set of subsets of $X$. Then the intersection of all $\sigma$-algebras on $X$ that contain $\mathcal{A}$ is a $\sigma$-algebra on $X$.

**Proof** There is at least one $\sigma$-algebra on $X$ that contains $\mathcal{A}$ because the $\sigma$-algebra consisting of all subsets of $X$ contains $\mathcal{A}$.

Let $S$ be the intersection of all $\sigma$-algebras on $X$ that contain $\mathcal{A}$. Then $\emptyset \in S$ because $\emptyset$ is an element of each $\sigma$-algebra on $X$ that contains $\mathcal{A}$.

Suppose $E \in S$. Thus $E$ is in every $\sigma$-algebra on $X$ that contains $\mathcal{A}$. Thus $X \setminus E$ is in every $\sigma$-algebra on $X$ that contains $\mathcal{A}$. Hence $X \setminus E \in S$.

Suppose $E_1, E_2, \ldots$ is a sequence of elements of $S$. Thus each $E_k$ is in every $\sigma$-algebra on $X$ that contains $\mathcal{A}$. Thus $\bigcup_{k=1}^\infty E_k$ is in every $\sigma$-algebra on $X$ that contains $\mathcal{A}$. Hence $\bigcup_{k=1}^\infty E_k \in S$, which completes the proof that $S$ is a $\sigma$-algebra on $X$.
