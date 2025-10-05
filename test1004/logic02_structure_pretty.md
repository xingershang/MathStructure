[Hint] {1.9 Lemma.}
[Fix] {$\Phi$} such that {$\Phi$ is consistent; $\Phi$ is negation complete; $\Phi$ contains witnesses}
{
    [Show] {For all formulas $\varphi$, $\Phi \vdash \neg \varphi$ iff not $\Phi \vdash \varphi$.; For all formulas $\varphi$ and $\psi$, $\Phi \vdash (\varphi \lor \psi)$ if and only if $\Phi \vdash \varphi$ or $\Phi \vdash \psi$.; For all formulas $\varphi$ with free variable $x$, $\Phi \vdash \exists x \varphi$ if and only if there is a term $t$ with $\Phi \vdash \varphi \frac{t}{x}$.}
    {
        [Show] {For all formulas $\varphi$, $\Phi \vdash \neg \varphi$ iff not $\Phi \vdash \varphi$.}
        {
            [Fix] {$\varphi$} such that {$\varphi$ is a formula}
            {
                [Have] {$\Phi \vdash \varphi$ or $\Phi \vdash \neg \varphi$} by {$\Phi$ is negation complete}
                [Have] {$\Phi \vdash \neg \varphi$ iff not $\Phi \vdash \varphi$} by {$\Phi$ is consistent}
            }
        }
        [Show] {For all formulas $\varphi$ and $\psi$, $\Phi \vdash (\varphi \lor \psi)$ if and only if $\Phi \vdash \varphi$ or $\Phi \vdash \psi$.}
        {
            [Fix] {$\varphi$; $\psi$} such that {$\varphi$ and $\psi$ are formulas}
            {
                [Show] {$\Phi \vdash (\varphi \lor \psi) \implies (\Phi \vdash \varphi \text{ or } \Phi \vdash \psi)$}
                {
                    [Assume] {$\Phi \vdash (\varphi \lor \psi)$}
                    {
                        [Assume] {not $\Phi \vdash \varphi$}
                        {
                            [Have] {$\Phi \vdash \neg \varphi$} by {$\Phi$ is negation complete}
                            [Have] {$\Phi \vdash \psi$} by {IV.3.4}
                        }
                    }
                }
                [Show] {$(\Phi \vdash \varphi \text{ or } \Phi \vdash \psi) \implies \Phi \vdash (\varphi \lor \psi)$}
                {
                    [Assume] {$\Phi \vdash \varphi$ or $\Phi \vdash \psi$}
                    {
                        [Have] {$(\Phi \vdash \varphi \lor \psi)$} by {the $\lor$-rules ($\lor$S) for the succedent}
                    }
                }
            }
        }
        [Show] {For all formulas $\varphi$ with free variable $x$, $\Phi \vdash \exists x \varphi$ if and only if there is a term $t$ with $\Phi \vdash \varphi \frac{t}{x}$.}
        {
            [Show] {($\Phi \vdash \exists x \varphi$) implies (there is a term $t$ with $\Phi \vdash \varphi \frac{t}{x}$)}
            {
                [Assume] {$\Phi \vdash \exists x \varphi$}
                {
                    [Obtain] {$t$} such that {$t$ is a term; $\Phi \vdash (\exists x \varphi \to \varphi \frac{t}{x})$} by {$\Phi$ contains witnesses}
                    [Have] {$\Phi \vdash \varphi \frac{t}{x}$} by {Modus ponens; IV.3.5}
                }
            }
            [Show] {(there is a term $t$ with $\Phi \vdash \varphi \frac{t}{x}$) implies ($\Phi \vdash \exists x \varphi$)}
            {
                [Assume] {there is a term $t$ with $\Phi \vdash \varphi \frac{t}{x}$}
                {
                    [Have] {$\Phi \vdash \exists x \varphi$} by {the rule ($\exists$S) of the $\exists$-introduction in the succedent}
                }
            }
        }
    }
}