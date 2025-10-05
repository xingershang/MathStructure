Theorem
Let $\phi : G_1 \to G_2$ be a group homomorphism.
Let $\ker(\phi)$ be the kernel of $\phi$.

Then:

$$\mathrm{Img}(\phi) \cong G_1 / \ker(\phi)$$

where $\cong$ denotes group isomorphism.

Proof
Let $K = \ker(\phi)$.
By Kernel is Normal Subgroup of Domain, $G_1 / K$ exists.
We need to establish that the mapping $\theta : G_1 / K \to G_2$ defined as:
$$\forall x \in G_1 : \theta(xK) = \phi(x)$$
is well-defined.
That is, we need to ensure that:
$$\forall x,y \in G_1 : xK = yK \implies \theta(xK) = \theta(yK)$$

Let $x,y \in G_1 : xK = yK$.
Then:

$xK = yK$
$\iff x^{-1} y \in K = \ker(\phi) \quad \text{(Left Cosets are Equal iff Product with Inverse in Subgroup)}$
$\iff \phi(x^{-1} y) = e_{G_2}$
$\iff (\phi(x))^{-1} \phi(y) = e_{G_2} $
$\iff \phi(x) = \phi(y)$

Thus we see that $\theta$ is well-defined.

We also note that:

$$\mathrm{Img}(\theta) = \{\theta(xK) : x \in G_1\}$$

So:

$$
\mathrm{Img}(\theta) = \{\theta(xK) : x \in G_1\} \\
= \{\phi(x) : x \in G_1\} \\
= \mathrm{Img}(\phi)
$$

We also note that $\theta$ is a homomorphism:

$$
\forall x,y \in G_1 : \quad \theta(xK yK) \\
= \theta(xyK) \\
= \phi(xy) \\
= \phi(x) \phi(y) \\
= \theta(xK) \theta(yK)
$$

Thus $\theta$ is a monomorphism whose image equals $\mathrm{Img}(\phi)$.

The result follows.

■