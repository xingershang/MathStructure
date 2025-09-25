# Natural Language

5.22 *existence, uniqueness, and degree of minimal polynomial*

Suppose $V$ is finite-dimensional and $T \in \mathcal{L}(V)$. Then there is a unique monic polynomial $p \in \mathcal{P}(\mathbf{F})$ of smallest degree such that $p(T) = 0$. Furthermore, $\deg p \leq \dim V$.

**Proof** If $\dim V = 0$, then $I$ is the zero operator on $V$ and thus we take $p$ to be the constant polynomial 1.

Now use induction on $\dim V$. Thus assume that $\dim V > 0$ and that the desired result is true for all operators on all complex vector spaces of smaller dimension. Let $v \in V$ be such that $v \neq 0$. The list $v, Tv, ..., T^{\dim V} v$ has length $1 + \dim V$ and thus is linearly dependent. By the linear dependence lemma (2.19), there is a smallest positive integer $m \leq \dim V$ such that $T^m v$ is a linear combination of $v, Tv, ..., T^{m-1} v$. Thus there exist scalars $c_0, c_1, c_2, ..., c_{m-1} \in \mathbf{F}$ such that

5.23
$$c_0 v + c_1 T v + \cdots + c_{m-1} T^{m-1} v + T^m v = 0.$$

Define a monic polynomial $q \in \mathcal{P}_m(\mathbf{F})$ by

$$q(z) = c_0 + c_1 z + \cdots + c_{m-1} z^{m-1} + z^m.$$

Then 5.23 implies that $q(T) v = 0$.

If $k$ is a nonnegative integer, then

$$q(T)(T^k v) = T^k (q(T) v) = T^k(0) = 0.$$

The linear dependence lemma (2.19) shows that $v, Tv, ..., T^{m-1} v$ is linearly independent. Thus the equation above implies that $\dim \operatorname{null} q(T) \geq m$. Hence

$$\dim \operatorname{range} q(T) = \dim V - \dim \operatorname{null} q(T) \leq \dim V - m.$$

Because $\operatorname{range} q(T)$ is invariant under $T$ (by 5.18), we can apply our induction hypothesis to the operator $T|_{\operatorname{range} q(T)}$ on the vector space $\operatorname{range} q(T)$. Thus there is a monic polynomial $s \in \mathcal{P}(\mathbf{F})$ with

$$\deg s \leq \dim V - m \quad \text{and} \quad s(T|_{\operatorname{range} q(T)}) = 0.$$

Hence for all $v \in V$ we have

$$(sq)(T)(v) = s(T)(q(T) v) = 0$$

because $q(T) v \in \operatorname{range} q(T)$ and $s(T)|_{\operatorname{range} q(T)} = s(T|_{\operatorname{range} q(T)}) = 0$. Thus $sq$ is a monic polynomial such that $\deg sq \leq \dim V$ and $(sq)(T) = 0$.

The paragraph above shows that there is a monic polynomial of degree at most $\dim V$ that when applied to $T$ gives the 0 operator. Thus there is a monic polynomial of smallest degree with this property, completing the existence part of this result.

Let $p \in \mathcal{P}(\mathbf{F})$ be a monic polynomial of smallest degree such that $p(T) = 0$. To prove the uniqueness part of the result, suppose $r \in \mathcal{P}(\mathbf{F})$ is a monic polynomial of the same degree as $p$ and $r(T) = 0$. Then $(p - r)(T) = 0$ and also $\deg(p - r) < \deg p$. If $p - r$ were not equal to 0, then we could divide $p - r$ by the coefficient of the highest-order term in $p - r$ to get a monic polynomial (of smaller degree than $p$) that when applied to $T$ gives the 0 operator. Thus $p - r = 0$, as desired.
