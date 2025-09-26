# Natural Language

**Example 2** Compute the improper integral $\int_0^{+\infty} te^{-pt} dt$, where $p$ is a constant and $p > 0$.

**Solution**

$\int_0^{+\infty} te^{-pt} dt = \left[ \int te^{-pt} dt \right]_0^{+\infty} = \left[ -\frac{1}{p} \int t d(e^{-pt}) \right]_0^{+\infty}$

$= \left[ -\frac{t}{p} e^{-pt} + \frac{1}{p} \int e^{-pt} dt \right]_0^{+\infty}$

$= \left[ -\frac{t}{p} e^{-pt} \right]_0^{+\infty} - \left[ \frac{1}{p^2} e^{-pt} \right]_0^{+\infty}$

$= -\frac{1}{p} \lim_{t \to +\infty} te^{-pt} - 0 - \frac{1}{p^2} (0 - 1) = \frac{1}{p^2}$

Note: The limit $\lim_{t \to +\infty} te^{-pt}$ in the above expression is an indeterminate form, which can be determined using L'Hôpital's rule.