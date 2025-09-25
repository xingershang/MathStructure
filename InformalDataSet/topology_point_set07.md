# Natural Language

**Theorem 18.3 (The pasting lemma).** Let $X = A \cup B$, where $A$ and $B$ are closed in $X$. Let $f : A \to Y$ and $g : B \to Y$ be continuous. If $f(x) = g(x)$ for every $x \in A \cap B$, then $f$ and $g$ combine to give a continuous function $h : X \to Y$, defined by setting $h(x) = f(x)$ if $x \in A$, and $h(x) = g(x)$ if $x \in B$.

*Proof.* Let $C$ be a closed subset of $Y$. Now

$$h^{-1}(C) = f^{-1}(C) \cup g^{-1}(C),$$

by elementary set theory. Since $f$ is continuous, $f^{-1}(C)$ is closed in $A$ and, therefore, closed in $X$. Similarly, $g^{-1}(C)$ is closed in $B$ and therefore closed in $X$. Their union $h^{-1}(C)$ is thus closed in $X$. ■
