# Natural Language

2.25 *finite-dimensional subspaces*

Every subspace of a finite-dimensional vector space is finite-dimensional.

**Proof** Suppose $V$ is finite-dimensional and $U$ is a subspace of $V$. We need to prove that $U$ is finite-dimensional. We do this through the following multistep construction.

**Step 1**  
If $U = \{0\}$, then $U$ is finite-dimensional and we are done. If $U \neq \{0\}$, then choose a nonzero vector $u_1 \in U$.

**Step k**  
If $U = \operatorname{span}(u_1, ..., u_{k-1})$, then $U$ is finite-dimensional and we are done. If $U \neq \operatorname{span}(u_1, ..., u_{k-1})$, then choose a vector $u_k \in U$ such that

$$u_k \notin \operatorname{span}(u_1, ..., u_{k-1}).$$

After each step, as long as the process continues, we have constructed a list of vectors such that no vector in this list is in the span of the previous vectors. Thus after each step we have constructed a linearly independent list, by the linear dependence lemma (2.19). This linearly independent list cannot be longer than any spanning list of $V$ (by 2.22). Thus the process eventually terminates, which means that $U$ is finite-dimensional.
