## Goal

Prove that there exist infinitely many positive integers $n$ such that $n^2 + 1$ has a prime divisor greater than $2n + \sqrt{10n}$.

## Proof

Let $p \equiv 1 \pmod{8}$ be a prime. The congruence $x^2 \equiv -1 \pmod{p}$ has two solutions in $[1, p-1]$ whose sum is $p$. If $n$ is the smaller one of them then $p$ divides $n^2 + 1$ and $n \leq (p-1)/2$. We show that $p > 2n + \sqrt{10n}$.

Let $n = (p-1)/2 - \ell$ where $\ell \geq 0$. Then $n^2 \equiv -1 \pmod{p}$ gives

$$
\left(\frac{p-1}{2} - \ell\right)^2 \equiv -1 \pmod{p}
$$

or

$$
(2\ell + 1)^2 + 4 \equiv 0 \pmod{p}.
$$

Thus $(2\ell + 1)^2 + 4 = rp$ for some $r \geq 0$. As $(2\ell + 1)^2 \equiv 1 \pmod{8} \equiv p \pmod{8}$, we have $r \equiv 5 \pmod{8}$, so that $r \geq 5$. Hence $(2\ell + 1)^2 + 4 \geq 5p$, implying $\ell \geq (\sqrt{5p - 4} - 1)/2$. Set $\sqrt{5p - 4} = u$ for clarity; then $\ell \geq (u - 1)/2$. Therefore

$$
n = \frac{p-1}{2} - \ell \leq \frac{1}{2} (p - u).
$$

Combined with $p = (u^2 + 4)/5$, this leads to $u^2 - 5u - 10n + 4 \geq 0$. Solving this quadratic inequality with respect to $u \geq 0$ gives $u \geq (5 + \sqrt{40n + 9})/2$. So the estimate $n \leq (p - u)/2$ leads to

$$
p \geq 2n + u \geq 2n + \frac{1}{2}(5 + \sqrt{40n + 9}) > 2n + \sqrt{10n}.
$$

Since there are infinitely many primes of the form $8k + 1$, it follows easily that there are also infinitely many $n$ with the stated property.