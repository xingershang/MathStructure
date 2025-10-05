To prove Theorem 10, which states that if $ R $ is an equivalence relation on $ A $ and $ a, b \in A $, then $ aRb $ if and only if $[a]_R = [b]_R$, we need to show both directions of the implication.

### Proof:

1. **Assume $ aRb $. We need to show that $[a]_R = [b]_R$.**

   - **Show $[a]_R \subseteq [b]_R$:**
     Let $ c \in [a]_R $. By definition, $ aRc $. Since $ R $ is symmetric and $ aRb $, we have $ bRa $. By transitivity, $ bRa $ and $ aRc $ imply $ bRc $. Therefore, $ c \in [b]_R $.

   - **Show $[b]_R \subseteq [a]_R$:**
     Let $ c \in [b]_R $. By definition, $ bRc $. Since $ aRb $ and $ R $ is transitive, $ aRb $ and $ bRc $ imply $ aRc $. Therefore, $ c \in [a]_R $.

   Since both $[a]_R \subseteq [b]_R$ and $[b]_R \subseteq [a]_R$ hold, we conclude that $[a]_R = [b]_R$.

2. **Assume $[a]_R = [b]_R$. We need to show that $ aRb $.**

   - Since $[a]_R = [b]_R$, and $ a \in [a]_R $ (because $ R $ is reflexive, $ aRa $), it follows that $ a \in [b]_R $. By definition of $[b]_R$, this means $ bRa $.

   - Since $ R $ is symmetric, $ bRa $ implies $ aRb $.

Therefore, we have shown both directions: $ aRb $ implies $[a]_R = [b]_R$, and $[a]_R = [b]_R$ implies $ aRb $. This completes the proof of Theorem 10.