# Natural Language

**1.4.5 Third Isomorphism Theorem** If $N$ and $H$ are normal subgroups of $G$, with $N$ contained in $H$, then

$$G / H \cong (G / N) / (H / N),$$

a “cancellation law”.

*Proof.* This will follow directly from the first isomorphism theorem if we can find an epimorphism of $G / N$ onto $G / H$ with kernel $H / N$, and there is a natural candidate: $f(aN) = aH$. To check that $f$ is well-defined, note that if $aN = bN$ then $a^{-1} b \in N \subseteq H$, so $aH = bH$. Since $a$ is an arbitrary element of $G$, $f$ is surjective, and by definition of coset multiplication, $f$ is a homomorphism. But the kernel of $f$ is

$$\{aN : aH = H\} = \{aN : a \in H\} = H / N.$$ ♣