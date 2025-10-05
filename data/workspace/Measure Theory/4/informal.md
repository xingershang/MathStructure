3.26  *Bounded Convergence Theorem*

Suppose $(X,S,\mu)$ is a measure space with $\mu(X) < \infty$. Suppose $f_1, f_2, \ldots$ is a sequence of $S$-measurable functions from $X$ to $\mathbf{R}$ that converges pointwise on $X$ to a function $f : X \to \mathbf{R}$. If there exists $c \in (0, \infty)$ such that

$$
|f_k(x)| \leq c
$$

for all $k \in \mathbf{Z}^+$ and all $x \in X$, then

$$
\lim_{k \to \infty} \int f_k \, d\mu = \int f \, d\mu.
$$

**Proof** The function $f$ is $S$-measurable by 2.48.

Suppose $c$ satisfies the hypothesis of this theorem. Let $\varepsilon > 0$. By Egorov’s Theorem (2.85), there exists $E \in S$ such that $\mu(X \setminus E) < \frac{\varepsilon}{4c}$ and $f_1, f_2, \ldots$ converges uniformly to $f$ on $E$. Now

$$
\left| \int f_k \, d\mu - \int f \, d\mu \right| = \left| \int_{X \setminus E} f_k \, d\mu - \int_{X \setminus E} f \, d\mu + \int_E (f_k - f) \, d\mu \right|
\leq \int_{X \setminus E} |f_k| \, d\mu + \int_{X \setminus E} |f| \, d\mu + \int_E |f_k - f| \, d\mu
< \frac{\varepsilon}{2} + \mu(E) \sup_E |f_k - f|,
$$

where the last inequality follows from 3.25. Because $f_1, f_2, \ldots$ converges uniformly to $f$ on $E$ and $\mu(E) < \infty$, the right side of the inequality above is less than $\varepsilon$ for $k$ sufficiently large, which completes the proof.
