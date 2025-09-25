# Natural Language

## Goal

$R$ is antisymmetric $\iff R \cap R^{-1} \subseteq I_A$

## Proof

  - ($\Rightarrow$) If $R$ is antisymmetric, then $(a, b) \in R \cap R^{-1}$ implies $(a, b) \in R$ and $(b, a) \in R$, so $a = b$. Hence, $(a, b) \in I_A$, proving $R \cap R^{-1} \subseteq I_A$.

  - ($\Leftarrow$) If $R \cap R^{-1} \subseteq I_A$, then whenever $(a, b) \in R$ and $(b, a) \in R$, we have $(a, b) \in I_A$, so $a = b$. Thus, $R$ is antisymmetric.