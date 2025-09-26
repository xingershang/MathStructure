# Natural Language

2.48  *limit of $S$-measurable functions*

Suppose $(X, S)$ is a measurable space and $f_1, f_2, \ldots$ is a sequence of $S$-measurable functions from $X$ to $\mathbf{R}$. Suppose $\lim_{k \to \infty} f_k(x)$ exists for each $x \in X$. Define $f : X \to \mathbf{R}$ by

$$
f(x) = \lim_{k \to \infty} f_k(x).
$$

Then $f$ is an $S$-measurable function.

**Proof** Suppose $a \in \mathbf{R}$. We will show that

2.49
$$
f^{-1}((a, \infty)) = \bigcup_{j=1}^\infty \bigcup_{m=1}^\infty \bigcap_{k=m}^\infty f_k^{-1} \left( \left(a + \frac{1}{j}, \infty \right) \right),
$$

which implies that $f^{-1}((a, \infty)) \in S$.

To prove 2.49, first suppose $x \in f^{-1}((a, \infty))$. Thus there exists $j \in \mathbf{Z}^+$ such that $f(x) > a + \frac{1}{j}$. The definition of limit now implies that there exists $m \in \mathbf{Z}^+$ such that $f_k(x) > a + \frac{1}{j}$ for all $k \geq m$. Thus $x$ is in the right side of 2.49, proving that the left side of 2.49 is contained in the right side.

To prove the inclusion in the other direction, suppose $x$ is in the right side of 2.49. Thus there exist $j, m \in \mathbf{Z}^+$ such that $f_k(x) > a + \frac{1}{j}$ for all $k \geq m$. Taking the limit as $k \to \infty$, we see that $f(x) \geq a + \frac{1}{j} > a$. Thus $x$ is in the left side of 2.49, completing the proof of 2.49. Thus $f$ is an $S$-measurable function.

