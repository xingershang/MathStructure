**1.4.6 Correspondence Theorem** If $N$ is a normal subgroup of $G$, then the map $\psi : H \to H / N$ sets up a one-to-one correspondence between subgroups of $G$ containing $N$ and subgroups of $G / N$. The inverse of $\psi$ is the map $\tau : Q \to \pi^{-1}(Q)$, where $\pi$ is the canonical epimorphism of $G$ onto $G / N$. Furthermore,

(i) $H_1 \leq H_2$ if and only if $H_1 / N \leq H_2 / N$, and in this case,

$$[H_2 : H_1] = [H_2 / N : H_1 / N]$$

(ii) $H$ is a normal subgroup of $G$ if and only if $H / N$ is a normal subgroup of $G / N$. More generally,  
(iii) $H_1$ is a normal subgroup of $H_2$ if and only if $H_1 / N$ is a normal subgroup of $H_2 / N$, and in this case, $H_2 / H_1 \cong (H_2 / N) / (H_1 / N)$.

*Proof.* We have established that $\psi$ is a bijection with inverse $\tau$. If $H_1 \leq H_2$, we have $H_1 / N \leq H_2 / N$ immediately, and the converse follows from the above proof that $\psi$ is injective. To prove the last statement of (i), let $\eta$ map the left coset $aH_1$, $a \in H_2$, to the left coset $(aN)(H_1 / N)$. Then $\eta$ is a well-defined and injective map of

$$aH_1 = bH_1 \quad \text{iff} \quad a^{-1} b \in H_1$$
$$\text{iff} \quad (aN)^{-1}(bN) = a^{-1} b N \in H_1 / N$$
$$\text{iff} \quad (aN)(H_1 / N) = (bN)(H_1 / N);$$

$\eta$ is surjective because $a$ ranges over all of $H_2$.  
To prove (ii), assume that $H \triangleleft G$; then for any $a \in G$ we have

$$(aN)(H / N)(aN)^{-1} = (aHa^{-1}) / N = H / N$$

so that $H / N \triangleleft G / N$. Conversely, suppose that $H / N$ is normal in $G / N$. Consider the homomorphism $a \to (aN)(H / N)$, the composition of the canonical map of $G$ onto $G / N$ and the canonical map of $G / N$ onto $(G / N) / (H / N)$. The element $a$ will belong to the kernel of this map if and only if $(aN)(H / N) = H / N$, which happens if and only if $aN \in H / N$, that is, $aN = hN$ for some $h \in H$. But since $N$ is contained in $H$, this statement is equivalent to $a \in H$. Thus $H$ is the kernel of a homomorphism, and is therefore a normal subgroup of $G$.  

Finally, the proof of (ii) also establishes the first part of (iii); just replace $H$ by $H_1$ and $G$ by $H_2$. The second part of (iii) follows from the third isomorphism theorem (with the same replacement). ♣