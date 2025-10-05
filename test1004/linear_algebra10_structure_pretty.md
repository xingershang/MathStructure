[Fix] {$p$; $r$} such that {$p \in \mathcal{P}(\mathbf{F})$ is a monic polynomial of smallest degree such that $p(T) = 0$; $r \in \mathcal{P}(\mathbf{F})$ is a monic polynomial of the same degree as $p$ and $r(T) = 0$}
{
    [Have] {$(p - r)(T) = 0$; $\deg(p - r) < \deg p$}
    [Have] {$p - r = 0$} by {If $p - r$ were not equal to 0, then we could divide $p - r$ by the coefficient of the highest-order term in $p - r$ to get a monic polynomial (of smaller degree than $p$) that when applied to $T$ gives the 0 operator.}
    [Have] {$p = r$} by {$p - r = 0$}
}