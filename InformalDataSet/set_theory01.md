# Natural Language

## Goal

$A = \bigcup \mathcal{P}(A)$

## Proof

  - ($\subseteq$): Let $x \in A$. The singleton set $\{x\}$ is a subset of $A$, so $\{x\} \in \mathcal{P}(A)$. Therefore, $x \in \bigcup \mathcal{P}(A)$ since $x \in \{x\}$ and $\{x\}$ is in $\mathcal{P}(A)$.

  - ($\supseteq$): Let $x \in \bigcup \mathcal{P}(A)$. By definition, there exists some $Y \in \mathcal{P}(A)$ such that $x \in Y$. Since $Y \in \mathcal{P}(A)$, we know $Y \subseteq A$. Therefore, $x \in A$.

Hence, $A = \bigcup \mathcal{P}(A)$.

