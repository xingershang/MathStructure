[Assume: {"\{x_n\} and \{y_n\} are numerical sequences"; "\displaystyle\lim_{n \to \infty} x_n = A"; "\displaystyle\lim_{n \to \infty} y_n = B"}]
{
    [Show: "\displaystyle\lim_{n \to \infty} (x_n + y_n) = A + B"]
    {
        [Define: "$\Delta(x_n)$" as ""$|A - x_n| = \Delta(x_n)$""]
        [Define: "$\Delta(y_n)$" as ""$|B - y_n| = \Delta(y_n)$""]
        [Have: "$|(A + B) - (x_n + y_n)| \leq \Delta(x_n) + \Delta(y_n)$"]
        [Fix: {\varepsilon} st "$\varepsilon > 0$"]
        {
            [Have: "there exists $N'$ such that \Delta(x_n) < \varepsilon / 2 for all $n > N'$" by "$\displaystyle\lim_{n \to \infty} x_n = A$"]
            [Have: "there exists $N''$ such that \Delta(y_n) < \varepsilon / 2 for all $n > N''$" by "$\displaystyle\lim_{n \to \infty} y_n = B$"]
            [Have: "for $n > \max\{N', N''\}$, $|(A + B) - (x_n + y_n)| < \varepsilon$"]
            [Have: "$\displaystyle\lim_{n \to \infty} (x_n + y_n) = A + B$" by "definition of limit"]
        }
    }
}