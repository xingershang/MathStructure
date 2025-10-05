**1.4.4 Second Isomorphism Theorem** If $H$ and $N$ are subgroups of $G$, with $N$ normal in $G$, then

$$H / (H \cap N) \cong HN / N.$$

Note that we write $HN / N$ rather than $H / N$, since $N$ need not be a subgroup of $H$.

*Proof.* Let $\pi$ be the canonical epimorphism from $G$ to $G / N$, and let $\pi_0$ be the restriction of $\pi$ to $H$. Then the kernel of $\pi_0$ is $H \cap N$, so by the first isomorphism theorem, $H / (H \cap N)$ is isomorphic to the image of $\pi_0$, which is $\{hN : h \in H\} = HN / N$. (To justify the last equality, note that for any $n \in N$ we have $hnN = hN$.) ♣