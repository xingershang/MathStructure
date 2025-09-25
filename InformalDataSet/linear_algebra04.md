# Natural Language

The next result says that we can check whether a linear map is injective by checking whether 0 is the only vector that gets mapped to 0. As a simple application of this result, we see that of the linear maps whose null spaces we computed in 3.12, only multiplication by $x^2$ is injective (except that the zero map is injective in the special case $V = \{0\}$).

3.15 *injectivity* $\iff$ *null space equals* $\{0\}$

Let $T \in \mathcal{L}(V, W)$. Then $T$ is injective if and only if $\operatorname{null} T = \{0\}$.

**Proof** First suppose $T$ is injective. We want to prove that $\operatorname{null} T = \{0\}$. We already know that $\{0\} \subseteq \operatorname{null} T$ (by 3.10). To prove the inclusion in the other direction, suppose $v \in \operatorname{null} T$. Then

$$T(v) = 0 = T(0).$$

Because $T$ is injective, the equation above implies that $v = 0$. Thus we can conclude that $\operatorname{null} T = \{0\}$, as desired.

To prove the implication in the other direction, now suppose $\operatorname{null} T = \{0\}$. We want to prove that $T$ is injective. To do this, suppose $u, v \in V$ and $Tu = Tv$. Then

$$0 = Tu - Tv = T(u - v).$$

Thus $u - v$ is in $\operatorname{null} T$, which equals $\{0\}$. Hence $u - v = 0$, which implies that $u = v$. Hence $T$ is injective, as desired.
