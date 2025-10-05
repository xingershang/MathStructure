[Hint] {Theorem}
[Fix] {$G_1$; $G_2$; $\phi$} such that {$G_1, G_2$ are groups; $\phi : G_1 \to G_2$ is a group homomorphism}
{
    [Define] {$\ker(\phi)$} as {$\ker(\phi)$ is the kernel of $\phi$}
    [Show] {$\mathrm{Img}(\phi) \cong G_1 / \ker(\phi)$}
    {
        [Define] {$K$} as {$K = \ker(\phi)$}
        [Have] {$G_1 / K$ exists} by {Kernel is Normal Subgroup of Domain}
        [Define] {$\theta$} as {the mapping $\theta : G_1 / K \to G_2$ such that $\forall x \in G_1, \theta(xK) = \phi(x)$}
        [Show] {$\theta$ is well-defined, i.e., $\forall x,y \in G_1 : xK = yK \implies \theta(xK) = \theta(yK)$}
        {
            [Fix] {$x$; $y$} such that {$x, y \in G_1$; $xK = yK$}
            {
                [LogicChain] {$xK = yK$}
                    ⇔ {$x^{-1} y \in K = \ker(\phi)$} by {Left Cosets are Equal iff Product with Inverse in Subgroup}
                    ⇔ {$\phi(x^{-1} y) = e_{G_2}$}
                    ⇔ {$(\phi(x))^{-1} \phi(y) = e_{G_2}$}
                    ⇔ {$\phi(x) = \phi(y)$}
            }
        }
        [Have] {$\theta$ is well-defined}
        [CalculationChain] {$\mathrm{Img}(\theta)$}
            = {\{\theta(xK) : x \in G_1\}}
            = {\{\phi(x) : x \in G_1\}}
            = {\mathrm{Img}(\phi)}
        [Show] {$\theta$ is a homomorphism}
        {
            [Fix] {x; y} such that {x, y \in G_1}
            {
                [CalculationChain] {\theta(xK yK)}
                    = {\theta(xyK)}
                    = {\phi(xy)}
                    = {\phi(x) \phi(y)}
                    = {\theta(xK) \theta(yK)}
            }
        }
        [Have] {$\theta$ is a monomorphism whose image equals $\mathrm{Img}(\phi)$}
    }
}