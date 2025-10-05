3.31  *Dominated Convergence Theorem*

Suppose $(X,S,\mu)$ is a measure space, $f : X \to [-\infty, \infty]$ is $S$-measurable, and $f_1, f_2, \ldots$ are $S$-measurable functions from $X$ to $[-\infty, \infty]$ such that

$$
\lim_{k \to \infty} f_k(x) = f(x)
$$

for almost every $x \in X$. If there exists an $S$-measurable function $g : X \to [0, \infty]$ such that

$$
\int g \, d\mu < \infty \quad \text{and} \quad |f_k(x)| \leq g(x)
$$

for every $k \in \mathbf{Z}^+$ and almost every $x \in X$, then

$$
\lim_{k \to \infty} \int f_k \, d\mu = \int f \, d\mu.
$$

**Proof** Suppose $g : X \to [0, \infty]$ satisfies the hypotheses of this theorem. If $E \in S$, then

$$
\left| \int f_k \, d\mu - \int f \, d\mu \right| = \left| \int_{X \setminus E} f_k \, d\mu - \int_{X \setminus E} f \, d\mu + \int_E f_k \, d\mu - \int_E f \, d\mu \right|
\leq \left| \int_{X \setminus E} f_k \, d\mu \right| + \left| \int_{X \setminus E} f \, d\mu \right| + \left| \int_E f_k \, d\mu - \int_E f \, d\mu \right|
\leq 2 \int_{X \setminus E} g \, d\mu + \left| \int_E f_k \, d\mu - \int_E f \, d\mu \right|.
\tag{3.32}
$$

**Case 1:** Suppose $\mu(X) < \infty$.  
Let $\varepsilon > 0$. By 3.28, there exists $\delta > 0$ such that

$$
\int_B g \, d\mu < \frac{\varepsilon}{4}
\tag{3.33}
$$

for every set $B \in S$ such that $\mu(B) < \delta$. By Egorov’s Theorem (2.85), there exists a set $E \in S$ such that $\mu(X \setminus E) < \delta$ and $f_1, f_2, \ldots$ converges uniformly to $f$ on $E$. Now 3.32 and 3.33 imply that

$$
\left| \int f_k \, d\mu - \int f \, d\mu \right| < \frac{\varepsilon}{2} + \left| \int_E (f_k - f) \, d\mu \right|.
$$

Because $f_1, f_2, \ldots$ converges uniformly to $f$ on $E$ and $\mu(E) < \infty$, the last term on the right is less than $\frac{\varepsilon}{2}$ for all sufficiently large $k$. Thus $\lim_{k \to \infty} \int f_k \, d\mu = \int f \, d\mu$, completing the proof of case 1.

**Case 2:** Suppose $\mu(X) = \infty$.  
Let $\varepsilon > 0$. By 3.29, there exists $E \in S$ such that $\mu(E) < \infty$ and

$$
\int_{X \setminus E} g \, d\mu < \frac{\varepsilon}{4}.
$$

The inequality above and 3.32 imply that

$$
\left| \int f_k \, d\mu - \int f \, d\mu \right| < \frac{\varepsilon}{2} + \left| \int_E f_k \, d\mu - \int_E f \, d\mu \right|.
$$

By case 1 as applied to the sequence $f_1|_E, f_2|_E, \ldots$, the last term on the right is less than $\frac{\varepsilon}{2}$ for all sufficiently large $k$. Thus $\lim_{k \to \infty} \int f_k \, d\mu = \int f \, d\mu$, completing the proof of case 2.
