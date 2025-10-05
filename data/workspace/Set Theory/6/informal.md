## Goal

If $R$ is an equivalence relation on $A$ and $a, b \in A$, then $aRb$ if and only if $[a]_R = [b]_R$.

## Proof

(⇒) Assume $aRb$. We show $[a]_R = [b]_R$ by mutual inclusion.

- $[a]_R \subseteq [b]_R$: Let $c \in [a]_R$. By definition, $cRa$. Since $R$ is symmetric, $aRb$ implies $bRa$. By transitivity of $R$, $cRa$ and $aRb$ yield $cRb$. Hence, $c \in [b]_R$.

- $[b]_R \subseteq [a]_R$: Let $d \in [b]_R$. By definition, $dRb$. From $aRb$ and symmetry, $bRa$. By transitivity, $dRb$ and $bRa$ imply $dRa$. Hence, $d \in [a]_R$.

Thus, $[a]_R = [b]_R$.

(⇐) Assume $[a]_R = [b]_R$. Since $R$ is reflexive, $a \in [a]_R$. Therefore, $a \in [b]_R$, which by definition means $aRb$.

Hence, $aRb$ if and only if $[a]_R = [b]_R$. 

Qed.