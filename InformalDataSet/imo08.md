# Natural Language

## Goal

Let $k$ be a positive integer. Prove that the number $(4k^2 - 1)^2$ has a positive divisor of the form $8kn - 1$ if and only if $k$ is even.

## Proof

The statement follows from the following fact.

$Lemma.$ For arbitrary positive integers $x$ and $y$, the number $4xy - 1$ divides $(4x^2 - 1)^2$ if and only if $x = y$.

**Proof.** If $x = y$ then $4xy - 1 = 4x^2 - 1$ obviously divides $(4x^2 - 1)^2$ so it is sufficient to consider the opposite direction.

Call a pair $(x, y)$ of positive integers **bad** if $4xy - 1$ divides $(4x^2 - 1)^2$ but $x \neq y$. In order to prove that bad pairs do not exist, we present two properties of them which provide an infinite descent.

**Property (i).** If $(x, y)$ is a bad pair and $x < y$ then there exists a positive integer $z < x$ such that $(x, z)$ is also bad.

Let $r = \frac{(4x^2 - 1)^2}{4xy - 1}$. Then

$$
r = -r \cdot (-1) \equiv -r(4xy - 1) = -(4x^2 - 1)^2 \equiv -1 \pmod{4x}
$$

and $r = 4xz - 1$ with some positive integer $z$. From $x < y$ we obtain that

$$
4xz - 1 = \frac{(4x^2 - 1)^2}{4xy - 1} < 4x^2 - 1
$$

and therefore $z < x$. By the construction, the number $4xz - 1$ is a divisor of $(4x^2 - 1)^2$ so $(x, z)$ is a bad pair.

**Property (ii).** If $(x, y)$ is a bad pair then $(y, x)$ is also bad.

Since $1 = 1^2 \equiv (4xy)^2 \pmod{4xy - 1}$, we have

$$
(4y^2 - 1)^2 \equiv (4y^2 - (4xy)^2)^2 = 16y^4(4x^2 - 1)^2 \equiv 0 \pmod{4xy - 1}.
$$

Hence, the number $4xy - 1$ divides $(4y^2 - 1)^2$ as well.

Now suppose that there exists at least one bad pair. Take a bad pair $(x, y)$ such that $2x + y$ attains its smallest possible value. If $x < y$ then property (i) provides a bad pair $(x, z)$ with $z < y$ and thus $2x + z < 2x + y$. Otherwise, if $y < x$, property (ii) yields that pair $(y, x)$ is also bad while $2y + x < 2x + y$. Both cases contradict the assumption that $2x + y$​ is minimal; the Lemma is proved.

**Qed.**

To prove the problem statement, apply the Lemma for $x = k$ and $y = 2n$; the number $8kn - 1$ divides $(4k^2 - 1)^2$ if and only if $k = 2n$. Hence, there is no such $n$ if $k$ is odd and $n = k/2$ is the only solution if $k$ is even.

$Qed.$