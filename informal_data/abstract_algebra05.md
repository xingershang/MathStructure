# Natural Language

**1.4.1 Factor Theorem** Any homomorphism $f$ whose kernel $K$ contains $N$ can be factored through $G/N$. In other words, in Figure 1.4.1 there is a unique homomorphism $\overline{f} : G/N \to H$ such that $\overline{f} \circ \pi = f$. Furthermore,  
(i) $\overline{f}$ is an epimorphism if and only if $f$ is an epimorphism;  
(ii) $\overline{f}$ is a monomorphism if and only if $K = N$;  
(iii) $\overline{f}$ is an isomorphism if and only if $f$ is an epimorphism and $K = N$.  

*Proof.* If the diagram is to commute, then $\overline{f}(aN)$ must be $f(a)$, and it follows that $\overline{f}$, if it exists, is unique. The definition of $\overline{f}$ that we have just given makes sense, because if $aN = bN$, then $a^{-1}b \in N \subseteq K$, so $f(a^{-1}b) = 1$, and therefore $f(a) = f(b)$. Since

$$\overline{f}(aNbN) = \overline{f}(abN) = f(ab) = f(a) f(b) = \overline{f}(aN) \overline{f}(bN),$$

$\overline{f}$ is a homomorphism. By construction, $\overline{f}$ has the same image as $f$, proving (i). Now the kernel of $\overline{f}$ is

$$\{aN : f(a) = 1\} = \{aN : a \in K\} = K/N.$$

By (1.3.13), a homomorphism is injective, i.e., a monomorphism, if and only if its kernel is trivial. Thus $\overline{f}$ is a monomorphism if and only if $K/N$ consists only of the identity element $N$. This means that if $a$ is any element of $K$, then the coset $aN$ coincides with $N$, which forces $a$ to belong to $N$. Thus $\overline{f}$ is a monomorphism if and only if $K = N$, proving (ii). Finally, (iii) follows immediately from (i) and (ii). ♣