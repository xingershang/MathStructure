[Fix] {$f$; $g$; $h$; $x_0$; $A$; $r$} such that {$f, g, h$ are real-valued functions; $x_0, A, r$ are real numbers; $r > 0$; for all $x$ such that $0 < |x - x_0| < r$, we have $g(x) \leq f(x) \leq h(x)$; $\lim_{x \to x_0} g(x) = A$; $\lim_{x \to x_0} h(x) = A$}
{
    [Show] {$\lim_{x \to x_0} f(x) = A$}
    {
        [Fix] {$\epsilon$} such that {$\epsilon > 0$}
        {
            [Obtain] {$\delta_1$} such that {$\delta_1 > 0$; for all $x$ satisfying $0 < |x - x_0| < \delta_1$, $h(x) < A + \epsilon$} by {$\lim_{x \to x_0} h(x) = A$}
            [Obtain] {$\delta_2$} such that {$\delta_2 > 0$; for all $x$ satisfying $0 < |x - x_0| < \delta_2$, $A - \epsilon < g(x)$} by {$\lim_{x \to x_0} g(x) = A$}
            [Define] {$\delta$} as {$\delta = \min \{ \delta_1, \delta_2, r \}$}
            [Fix] {$x$} such that {$0 < |x - x_0| < \delta$}
            {
                [Have] {$A - \epsilon < g(x) \leq f(x) \leq h(x) < A + \epsilon$}
            }
            [Have] {$\lim_{x \to x_0} f(x) = A$}
        }
    }
}