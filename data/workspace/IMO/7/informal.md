## Goal

Let $b, n > 1$ be integers. Suppose that for each $k > 1$ there exists an integer $a_k$ such that $b - a_k^n$ is divisible by $k$. Prove that $b = A^n$ for some integer $A$.

## Proof

Let the prime factorization of $b$ be $b = p_1^{\alpha_1} \cdots p_s^{\alpha_s}$, where $p_1, \ldots, p_s$ are distinct primes. Our goal is to show that all exponents $\alpha_i$ are divisible by $n$, then we can set $A = p_1^{\alpha_1/n} \cdots p_s^{\alpha_s/n}$.

Apply the condition for $k = b^2$. The number $b - a_k^n$ is divisible by $b^2$ and hence, for each $1 \leq i \leq s$, it is divisible by $p_i^{2\alpha_i} > p_i^{\alpha_i}$ as well. Therefore

$$
a_k^n \equiv b \equiv 0 \pmod{p_i^{\alpha_i}}
$$

and

$$
a_k^n \not\equiv b \not\equiv 0 \pmod{p_i^{\alpha_i + 1}},
$$

which implies that the largest power of $p_i$ dividing $a_k^n$ is $p_i^{\alpha_i}$. Since $a_k^n$ is a complete $n$th power, this implies that $\alpha_i$ is divisible by $n$.

$Qed.$