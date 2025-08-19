[Show: "$x_n \leq y_n \leq z_n$ for all $n > N \in \mathbb{N}$"]
[Assume: "$\lim_{n \to \infty} x_n = \lim_{n \to \infty} z_n = A$"]
{
    [Show: "$\lim_{n \to \infty} y_n = A$"]
    {
        [Fix: {$\varepsilon$} st "$\varepsilon > 0$"]
        {
            [Have: "There exists $N'$ such that $A-\varepsilon < x_n$ for all $n > N'$" by "$\lim_{n \to \infty} x_n = A$"]
            [Have: "There exists $N''$ such that $z_n < A+\varepsilon$ for all $n > N''$" by "$\lim_{n \to \infty} z_n = A$"]
            [Define: "N" as ""$N=\max\{N',N''\}$""]
            [Have: "For all $n > N$, $A-\varepsilon < x_n \leq y_n \leq z_n < A+\varepsilon$" by {"$x_n \leq y_n \leq z_n$"; "previous bounds on $x_n$ and $z_n$"}]
            [Have: "$|y_n - A| < \varepsilon$" by "previous inequality"]
            [Have: "$\lim_{n \to \infty} y_n = A$" by "definition of limit"]
        }
    }
}