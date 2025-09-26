# Natural Language

**Theorem 18.4 (Maps into products).** Let $f : A \to X \times Y$ be given by the equation

$$f(a) = (f_1(a), f_2(a)).$$

Then $f$ is continuous if and only if the functions

$$f_1 : A \to X \quad \text{and} \quad f_2 : A \to Y$$

are continuous.

The maps $f_1$ and $f_2$ are called the *coordinate functions* of $f$.

*Proof.* Let $\pi_1 : X \times Y \to X$ and $\pi_2 : X \times Y \to Y$ be projections onto the first and second factors, respectively. These maps are continuous. For $\pi_1^{-1}(U) = U \times Y$ and $\pi_2^{-1}(V) = X \times V$, and these sets are open if $U$ and $V$ are open. Note that for each $a \in A$,

$$f_1(a) = \pi_1(f(a)) \quad \text{and} \quad f_2(a) = \pi_2(f(a)).$$

If the function $f$ is continuous, then $f_1$ and $f_2$ are composites of continuous functions and therefore continuous. Conversely, suppose that $f_1$ and $f_2$ are continuous. We show that for each basis element $U \times V$ for the topology of $X \times Y$, its inverse image $f^{-1}(U \times V)$ is open. A point $a$ is in $f^{-1}(U \times V)$ if and only if $f(a) \in U \times V$, that is, if and only if $f_1(a) \in U$ and $f_2(a) \in V$. Therefore,

$$f^{-1}(U \times V) = f_1^{-1}(U) \cap f_2^{-1}(V).$$

Since both of the sets $f_1^{-1}(U)$ and $f_2^{-1}(V)$ are open, so is their intersection. ■

