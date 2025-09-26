# Natural Language

**Theorem 17.9.** *Let $X$ be a space satisfying the $T_1$ axiom; let $A$ be a subset of $X$. Then the point $x$ is a limit point of $A$ if and only if every neighborhood of $x$ contains infinitely many points of $A$.*

*Proof.* If every neighborhood of $x$ intersects $A$ in infinitely many points, it certainly intersects $A$ in some point other than $x$ itself, so that $x$ is a limit point of $A$.

Conversely, suppose that $x$ is a limit point of $A$, and suppose some neighborhood $U$ of $x$ intersects $A$ in only finitely many points. Then $U$ also intersects $A - \{x\}$ in finitely many points; let $\{x_1, \ldots, x_m\}$ be the points of $U \cap (A - \{x\})$. The set $X - \{x_1, \ldots, x_m\}$ is an open set of $X$, since the finite point set $\{x_1, \ldots, x_m\}$ is closed; then

$$U \cap (X - \{x_1, \ldots, x_m\})$$

is a neighborhood of $x$ that intersects the set $A - \{x\}$ not at all. This contradicts the assumption that $x$ is a limit point of $A$. ■


