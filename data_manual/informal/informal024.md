## Goal

$A \times \bigcup B = \bigcup \{A \times X \mid X \in B\}$

## Proof

  - ($\subseteq$): Let $(a, x) \in A \times \bigcup B$. By definition, $x \in \bigcup B$, so there exists $X \in B$ such that $x \in X$. Therefore, $(a, x) \in A \times X$. Since $A \times X$ is part of the union $\bigcup \{A \times X \mid X \in B\}$, we conclude $(a, x) \in \bigcup \{A \times X \mid X \in B\}$.

  - ($\supseteq$): Let $(a, x) \in \bigcup \{A \times X \mid X \in B\}$. Then there exists $X \in B$ such that $(a, x) \in A \times X$. By definition of Cartesian product, $a \in A$ and $x \in X$. Since $X \in B$, we have $x \in \bigcup B$. Thus, $(a, x) \in A \times \bigcup B$.

Hence, $A \times \bigcup B = \bigcup \{A \times X \mid X \in B\}$.
