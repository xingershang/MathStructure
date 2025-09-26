# Natural Language

**Theorem 18.2 (Rules for constructing continuous functions).** Let $X$, $Y$, and $Z$ be topological spaces.

(a) (Constant function) If $f : X \to Y$ maps all of $X$ into the single point $y_0$ of $Y$, then $f$ is continuous.

(b) (Inclusion) If $A$ is a subspace of $X$, the inclusion function $j : A \to X$ is continuous.

(c) (Composites) If $f : X \to Y$ and $g : Y \to Z$ are continuous, then the map $g \circ f : X \to Z$ is continuous.

(d) (Restricting the domain) If $f : X \to Y$ is continuous, and if $A$ is a subspace of $X$, then the restricted function $f|A : A \to Y$ is continuous.

(e) (Restricting or expanding the range) Let $f : X \to Y$ be continuous. If $Z$ is a subspace of $Y$ containing the image set $f(X)$, then the function $g : X \to Z$ obtained by restricting the range of $f$ is continuous. If $Z$ is a space having $Y$ as a subspace, then the function $h : X \to Z$ obtained by expanding the range of $f$ is continuous.

(f) (Local formulation of continuity) The map $f : X \to Y$ is continuous if $X$ can be written as the union of open sets $U_\alpha$ such that $f|U_\alpha$ is continuous for each $\alpha$.

*Proof.* (a) Let $f(x) = y_0$ for every $x$ in $X$. Let $V$ be open in $Y$. The set $f^{-1}(V)$ equals $X$ or $\emptyset$, depending on whether $V$ contains $y_0$ or not. In either case, it is open.

(b) If $U$ is open in $X$, then $j^{-1}(U) = U \cap A$, which is open in $A$ by definition of the subspace topology.

(c) If $U$ is open in $Z$, then $g^{-1}(U)$ is open in $Y$ and $f^{-1}(g^{-1}(U))$ is open in $X$. But

$$f^{-1}(g^{-1}(U)) = (g \circ f)^{-1}(U),$$

by elementary set theory.

(d) The function $f|A$ equals the composite of the inclusion map $j : A \to X$ and the map $f : X \to Y$, both of which are continuous.

(e) Let $f : X \to Y$ be continuous. If $f(X) \subset Z \subset Y$, we show that the function $g : X \to Z$ obtained from $f$ is continuous. Let $B$ be open in $Z$. Then $B = Z \cap U$ for some open set $U$ of $Y$. Because $Z$ contains the entire image set $f(X)$,

$$f^{-1}(U) = g^{-1}(B),$$

by elementary set theory. Since $f^{-1}(U)$ is open, so is $g^{-1}(B)$.

To show $h : X \to Z$ is continuous if $Z$ has $Y$ as a subspace, note that $h$ is the composite of the map $f : X \to Y$ and the inclusion map $j : Y \to Z$.

(f) By hypothesis, we can write $X$ as a union of open sets $U_\alpha$, such that $f|U_\alpha$ is continuous for each $\alpha$. Let $V$ be an open set in $Y$. Then

$$f^{-1}(V) \cap U_\alpha = (f|U_\alpha)^{-1}(V),$$

because both expressions represent the set of those points $x$ lying in $U_\alpha$ for which $f(x) \in V$. Since $f|U$ is continuous, this set is open in $U_\alpha$, and hence open in $X$. But

$$f^{-1}(V) = \bigcup_\alpha (f^{-1}(V) \cap U_\alpha),$$

so that $f^{-1}(V)$ is also open in $X$. ■



