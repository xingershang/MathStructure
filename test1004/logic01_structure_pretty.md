[Hint] {4.6 Coincidence Lemma}
[Fix] {$\mathfrak{I}_1$; $\mathfrak{I}_2$} such that {$\mathfrak{I}_1 = (\mathcal{A}_1, \beta_1)$ is an $S_1$-interpretation; $\mathfrak{I}_2 = (\mathcal{A}_2, \beta_2)$ is an $S_2$-interpretation; $A_1 = A_2$}
{
    [Define] {$S$} as {$S := S_1 \cap S_2$}
    [Show] {Let $t$ be an $S$-term. If $\mathfrak{I}_1$ and $\mathfrak{I}_2$ agree on the $S$-symbols occurring in $t$ and on the variables occurring in $t$, then $\mathfrak{I}_1(t) = \mathfrak{I}_2(t)$.}
    {
        [Hint] {We use induction on S-terms.}
        [Assume] {t = x for some variable x}
        {
            [Have] {$\beta_1(x) = \beta_2(x)$} by {hypothesis}
            [CalculationChain] {$\mathfrak{I}_1(x)$}
        }
        [Assume] {t = c for some constant c}
        {
            [Have] {$c^{\mathcal{A}_1} = c^{\mathcal{A}_2}$} by {hypothesis}
            [CalculationChain] {$\mathfrak{I}_1(c)$}
        }
        [Assume] {t = f t_1 \ldots t_n for some n-ary function symbol f and S-terms t_1, ..., t_n}
        {
            [CalculationChain] {$\mathfrak{I}_1(f t_1 \ldots t_n)$}
        }
    }
    [Show] {Let $\varphi$ be an $S$-formula. If $\mathfrak{I}_1$ and $\mathfrak{I}_2$ agree on the $S$-symbols and on the variables occurring free in $\varphi$, then $\mathfrak{I}_1 \models \varphi$ iff $\mathfrak{I}_2 \models \varphi$.}
    {
        [Hint] {We use induction on $S$-formulas.}
        [Assume] {$\varphi = R t_1 \ldots t_n$ for some n-ary relation symbol $R \in S$ and S-terms $t_1, \ldots, t_n$}
        {
            [LogicChain] {$\mathfrak{I}_1 \models R t_1 \ldots t_n$}
        }
        [Assume] {$\varphi = t_1 \equiv t_2$}
        {
            [Hint] {Similarly.}
        }
        [Assume] {$\varphi = \neg \psi$}
        {
            [LogicChain] {$\mathfrak{I}_1 \models \neg \psi$}
        }
        [Assume] {$\varphi = (\psi \lor \chi)$}
        {
            [Hint] {Similarly.}
        }
        [Assume] {$\varphi = \exists x \psi$}
        {
            [LogicChain] {$\mathfrak{I}_1 \models \exists x \psi$}
        }
    }
}