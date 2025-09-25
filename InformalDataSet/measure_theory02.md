# Natural Language

2.85  *Egorov’s Theorem*

Suppose $(X,S,\mu)$ is a measure space with $\mu(X)<\infty$. Suppose $f_1, f_2, \ldots$ is a sequence of $S$-measurable functions from $X$ to $\mathbf{R}$ that converges pointwise on $X$ to a function $f : X \to \mathbf{R}$. Then for every $\varepsilon > 0$, there exists a set $E \in S$ such that $\mu(X \setminus E) < \varepsilon$ and $f_1, f_2, \ldots$ converges uniformly to $f$ on $E$.

**Proof** Suppose $\varepsilon > 0$. Temporarily fix $n \in \mathbf{Z}^+$. The definition of pointwise convergence implies that

$$
\bigcup_{m=1}^\infty \bigcap_{k=m}^\infty \{x \in X : |f_k(x) - f(x)| < \frac{1}{n}\} = X.
\tag{2.86}
$$

For $m \in \mathbf{Z}^+$, let

$$
A_{m,n} = \bigcap_{k=m}^\infty \{x \in X : |f_k(x) - f(x)| < \frac{1}{n}\}.
$$

Then clearly $A_{1,n} \subset A_{2,n} \subset \cdots$ is an increasing sequence of sets and 2.86 can be rewritten as

$$
\bigcup_{m=1}^\infty A_{m,n} = X.
$$

The equation above implies (by 2.59) that $\lim_{m \to \infty} \mu(A_{m,n}) = \mu(X)$. Thus there exists $m_n \in \mathbf{Z}^+$ such that

$$
\mu(X) - \mu(A_{m_n,n}) < \frac{\varepsilon}{2^n}.
\tag{2.87}
$$

Now let

$$
E = \bigcap_{n=1}^\infty A_{m_n,n}.
$$

Then

$$
\mu(X \setminus E) = \mu \left(X \setminus \bigcap_{n=1}^\infty A_{m_n,n}\right)
= \mu \left(\bigcup_{n=1}^\infty (X \setminus A_{m_n,n})\right)
\leq \sum_{n=1}^\infty \mu(X \setminus A_{m_n,n})
< \varepsilon,
$$

where the last inequality follows from 2.87.

To complete the proof, we must verify that $f_1, f_2, \ldots$ converges uniformly to $f$ on $E$. To do this, suppose $\varepsilon' > 0$. Let $n \in \mathbf{Z}^+$ be such that $\frac{1}{n} < \varepsilon'$. Then $E \subset A_{m_n,n}$, which implies that

$$
|f_k(x) - f(x)| < \frac{1}{n} < \varepsilon'
$$

for all $k \geq m_n$ and all $x \in E$. Hence $f_1, f_2, \ldots$ does indeed converge uniformly to $f$ on $E$.
