# Natural Language

2.39  *condition for measurable function*

Suppose $(X, S)$ is a measurable space and $f : X \to \mathbf{R}$ is a function such that

$$
f^{-1}((a, \infty)) \in S
$$

for all $a \in \mathbf{R}$. Then $f$ is an $S$-measurable function.

**Proof** Let

$$
\mathcal{T} = \{ A \subset \mathbf{R} : f^{-1}(A) \in S \}.
$$

We want to show that every Borel subset of $\mathbf{R}$ is in $\mathcal{T}$. To do this, we will first show that $\mathcal{T}$ is a $\sigma$-algebra on $\mathbf{R}$.

Certainly $\emptyset \in \mathcal{T}$, because $f^{-1}(\emptyset) = \emptyset \in S$.

If $A \in \mathcal{T}$, then $f^{-1}(A) \in S$; hence

$$
f^{-1}(\mathbf{R} \setminus A) = X \setminus f^{-1}(A) \in S
$$

by 2.33(a), and thus $\mathbf{R} \setminus A \in \mathcal{T}$. In other words, $\mathcal{T}$ is closed under complementation.

If $A_1, A_2, \ldots \in \mathcal{T}$, then $f^{-1}(A_1), f^{-1}(A_2), \ldots \in S$; hence

$$
f^{-1}\left(\bigcup_{k=1}^\infty A_k \right) = \bigcup_{k=1}^\infty f^{-1}(A_k) \in S
$$

by 2.33(b), and thus $\bigcup_{k=1}^\infty A_k \in \mathcal{T}$. In other words, $\mathcal{T}$ is closed under countable unions. Thus $\mathcal{T}$ is a $\sigma$-algebra on $\mathbf{R}$.

By hypothesis, $\mathcal{T}$ contains $\{(a, \infty) : a \in \mathbf{R}\}$. Because $\mathcal{T}$ is closed under complementation, $\mathcal{T}$ also contains $\{(-\infty, b] : b \in \mathbf{R}\}$. Because the $\sigma$-algebra $\mathcal{T}$ is closed under finite intersections (by 2.25), we see that $\mathcal{T}$ contains $\{(a,b) : a,b \in \mathbf{R}\}$. Because $(a,b) = \bigcup_{k=1}^\infty (a, b-\frac{1}{k}]$ and $(-\infty,b) = \bigcup_{k=1}^\infty (-k, b-\frac{1}{k}]$ and $\mathcal{T}$ is closed under countable unions, we can conclude that $\mathcal{T}$ contains every open subset of $\mathbf{R}$.

Thus the $\sigma$-algebra $\mathcal{T}$ contains the smallest $\sigma$-algebra on $\mathbf{R}$ that contains all open subsets of $\mathbf{R}$. In other words, $\mathcal{T}$ contains every Borel subset of $\mathbf{R}$. Thus $f$ is an $S$-measurable function.
