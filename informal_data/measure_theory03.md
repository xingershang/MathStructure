# Natural Language

3.7  *integral of a simple function*

Suppose $(X,S,\mu)$ is a measure space, $E_1, \ldots, E_n$ are disjoint sets in $S$, and $c_1, \ldots, c_n \in [0, \infty]$. Then

$$
\int \left(\sum_{k=1}^n c_k \chi_{E_k} \right) d\mu = \sum_{k=1}^n c_k \mu(E_k).
$$

**Proof** Without loss of generality, we can assume that $E_1, \ldots, E_n$ is an $S$-partition of $X$ [by replacing $n$ by $n+1$ and setting $E_{n+1} = X \setminus (E_1 \cup \ldots \cup E_n)$ and $c_{n+1} = 0$].

If $P$ is the $S$-partition $E_1, \ldots, E_n$ of $X$, then $\mathcal{L} \left(\sum_{k=1}^n c_k \chi_{E_k}, P \right) = \sum_{k=1}^n c_k \mu(E_k)$. Thus

$$
\int \left(\sum_{k=1}^n c_k \chi_{E_k} \right) d\mu \geq \sum_{k=1}^n c_k \mu(E_k).
$$

To prove the inequality in the other direction, suppose that $P$ is an $S$-partition $A_1, \ldots, A_m$ of $X$. Then

$$
\mathcal{L} \left(\sum_{k=1}^n c_k \chi_{E_k}, P \right) = \sum_{j=1}^m \mu(A_j) \min_{\{i : A_j \cap E_i \neq \varnothing\}} c_i
= \sum_{j=1}^m \sum_{k=1}^n \mu(A_j \cap E_k) \min_{\{i : A_j \cap E_i \neq \varnothing\}} c_i
\leq \sum_{j=1}^m \sum_{k=1}^n \mu(A_j \cap E_k) c_k
= \sum_{k=1}^n c_k \sum_{j=1}^m \mu(A_j \cap E_k)
= \sum_{k=1}^n c_k \mu(E_k).
$$

The inequality above implies that $\int \left(\sum_{k=1}^n c_k \chi_{E_k} \right) d\mu \leq \sum_{k=1}^n c_k \mu(E_k)$, completing the proof.
