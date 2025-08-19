[Fix: {x, y, A, B} st {"$\{x_n\},\{y_n\}$ are numerical sequences"; "$\lim_{n\to\infty} x_n = A$"; "$\lim_{n\to\infty} y_n = B$"; "$y_n\neq 0\;(n=1,2,\ldots)$"; "$B\neq 0$"}]
{
    [Show: "$\lim_{n \to \infty} \frac{x_n}{y_n} = \frac{A}{B}$"]
    {
        [Define: "\\Delta(x_n)" as """$\Delta(x_n)=|A - x_n|$"""]
        [Define: "\\Delta(y_n)" as """$\Delta(y_n)=|B - y_n|$"""]
        [Define: "\\delta(y_n)" as """$\delta(y_n)=\frac{\Delta(y_n)}{|y_n|}$"""]
        [Have: "$\left| \frac{A}{B} - \frac{x_n}{y_n} \right| \leq \frac{|x_n| \Delta(y_n) + |y_n| \Delta(x_n)}{y_n^2} \cdot \frac{1}{1 - \delta(y_n)}$"]
        [Fix: {\varepsilon} st "$\varepsilon > 0$"]
        {
            [Have: "there exists $N'$ such that $\Delta(x_n) < \min\{1, \frac{\varepsilon |B|}{8}\}$ for all $n > N'$" by "$\lim_{n\to\infty} x_n=A$"]
            [Have: "there exists $N''$ such that $\Delta(y_n) < \min\{\frac{|B|}{4}, \frac{\varepsilon B^2}{16(|A| + 1)}\}$ for all $n > N''$" by "$\lim_{n\to\infty} y_n=B$"]
            [Define: "N" as """$N = \max\{N', N''\}$"""]
            [Fix: {n} st "$n > N$"]
            {
                [Have: "$|x_n| < |A| + \Delta(x_n) < |A| + 1$"]
                [Have: "$|y_n| > |B| - \Delta(y_n) > \frac{|B|}{2}$"]
                [Have: "$\frac{1}{|y_n|} < \frac{2}{|B|}$"]
                [Have: "$0 < \delta(y_n) < \frac{1}{2}$"]
                [Have: "$1 - \delta(y_n) > \frac{1}{2}$"]
                [Have: "$|x_n| \cdot \frac{1}{y_n^2} \Delta(y_n) < (|A| + 1) \cdot \frac{4}{B^2} \cdot \frac{\varepsilon B^2}{16(|A| + 1)} = \frac{\varepsilon}{4}$"]
                [Have: "$\left| \frac{1}{y_n} \right| \Delta(x_n) < \frac{2}{|B|} \cdot \frac{\varepsilon |B|}{8} = \frac{\varepsilon}{4}$"]
                [Have: "$0 < \frac{1}{1 - \delta(y_n)} < 2$"]
                [Have: "$\left| \frac{A}{B} - \frac{x_n}{y_n} \right| < \varepsilon$"]
            }
        }
        [Have: "$\lim_{n \to \infty} \frac{x_n}{y_n} = \frac{A}{B}$" by "definition of limit"]
    }
}