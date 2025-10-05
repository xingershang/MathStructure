[Hint] {Every bounded sequence of real numbers contains a convergent subsequence.}
[Fix] {$\{x_n\}$} such that {$\{x_n\}$ is a bounded sequence of real numbers}
{
    [Show] {$\{x_n\}$ contains a convergent subsequence}
    {
        [Define] {$E$} as {$E$ is the set of values of the sequence $\{x_n\}$}
        [Assume] {$E$ is finite}
        {
            [Obtain] {$x$; $\{x_{n_k}\}$} such that {$x \in E$; $\{x_{n_k}\}$ is a subsequence of $\{x_n\}$; $\forall k, x_{n_k} = x$}
            [Have] {The subsequence $\{x_{n_k}\}$ is constant}
            [Have] {The subsequence $\{x_{n_k}\}$ converges} by {The subsequence $\{x_{n_k}\}$ is constant}
        }
        [Assume] {$E$ is infinite}
        {
            [Obtain] {$x$} such that {$x$ is a limit point of $E$} by {the Bolzano–Weierstrass principle}
            [Obtain] {a subsequence $\{x_{n_k}\}$} such that {$\forall k \in \mathbb{N}, |x_{n_k} - x| < \frac{1}{k}$} by {$x$ is a limit point of $E$, allowing for an inductive construction of the subsequence.}
            [Have] {the sequence $\{x_{n_k}\}$ converges to $x$} by {$\lim_{k \to \infty} \frac{1}{k} = 0$; the sequence was constructed such that $\forall k, |x_{n_k} - x| < \frac{1}{k}$}
        }
    }
}