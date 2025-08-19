## Goal

Let $a_0, a_1, a_2, \ldots$ be a sequence of positive integers such that the greatest common divisor of any two consecutive terms is greater than the preceding term; in symbols, $\gcd(a_i, a_{i+1}) > a_{i-1}$. Prove that $a_n \geq 2^n$ for all $n \geq 0$.

## Prove

Since $a_i \geq \gcd(a_i, a_{i+1}) > a_{i-1}$, the sequence is strictly increasing. In particular $a_0 \geq 1$, $a_1 \geq 2$. For each $i \geq 1$ we also have $a_{i+1} - a_i \geq \gcd(a_i, a_{i+1}) > a_{i-1}$, and consequently $a_{i+1} \geq a_i + a_{i-1} + 1$. Hence $a_2 \geq 4$ and $a_3 \geq 7$. The equality $a_3 = 7$ would force equalities in the previous estimates, leading to $\gcd(a_2, a_3) = \gcd(4, 7) > a_1 = 2$, which is false. Thus $a_3 \geq 8$; the result is valid for $n = 0, 1, 2, 3$. These are the base cases for a proof by induction.

Take any $n \geq 3$ and assume that $a_i \geq 2^i$ for $i = 0, 1, \ldots, n$. We must show that $a_{n+1} \geq 2^{n+1}$. Let $\gcd(a_n, a_{n+1}) = d$. We know that $d > a_{n-1}$. The induction claim is reached immediately in the following cases:

- if $a_{n+1} \geq 4d$ then $a_{n+1} > 4a_{n-1} \geq 4 \cdot 2^{n-1} = 2^{n+1}$;
- if $a_n \geq 3d$ then $a_{n+1} \geq a_n + d \geq 4d > 4a_{n-1} \geq 4 \cdot 2^{n-1} = 2^{n+1}$;
- if $a_n = d$ then $a_{n+1} \geq a_n + d = 2a_n \geq 2 \cdot 2^n = 2^{n+1}$.

The only remaining possibility is that $a_n = 2d$ and $a_{n+1} = 3d$, which we assume for the sequel. So $a_{n+1} = \frac{3}{2}a_n$.

Let now $\gcd(a_{n-1}, a_n) = d'$; then $d' > a_{n-2}$. Write $a_n = md'$ ($m$ an integer). Keeping in mind that $d' \leq a_{n-1} < d$ and $a_n = 2d$, we get that $m \geq 3$. Also $a_{n-1} < d = \frac{1}{2}md'$, $a_{n+1} = \frac{3}{2}md'$. Again we single out the cases which imply the induction claim immediately:

- if $m \geq 6$ then $a_{n+1} = \frac{3}{2}md' \geq 9d' > 9a_{n-2} \geq 9 \cdot 2^{n-2} = 2^{n+1}$;
- if $3 \leq m \leq 4$ then $a_{n-1} < \frac{1}{2} \cdot 4d'$, and hence $a_{n-1} = d'$, $a_{n+1} = \frac{3}{2}ma_{n-1} \geq \frac{3}{2} \cdot 3a_{n-1} = \frac{9}{2} \cdot 2^{n-2} = 2^{n+1}$.

So we are left with the case $m = 5$, which means that $a_n = 5d'$, $a_{n+1} = \frac{15}{2}d'$, and $a_{n-1} < d = \frac{5}{2}d'$. The last relation implies that $a_{n-1}$ is either $d'$ or $2d'$. Anyway, $a_n \geq 2d'$.

The same pattern repeats once more. We denote $\gcd(a_{n-2}, a_{n-1}) = d''$, then $d'' > a_{n-3}$. Because $d''$ is a divisor of $a_{n-1}$, hence also of $2d'$, we may write $2d' = m'd''$ ($m'$ an integer). Since $d'' < a_{n-2} < d'$, we get $m' \geq 3$. Also, $a_{n-2} < d' = \frac{1}{2}m'd''$, $a_{n+1} = \frac{15}{4}m'd''$. As before, we consider the cases:

- if $m' \geq 5$ then $a_{n+1} = \frac{15}{4}m'd'' \geq \frac{75}{4}d'' > \frac{75}{4}a_{n-3} \geq \frac{75}{4} \cdot 2^{n-3} > 2^{n+1}$;
- if $3 \leq m' \leq 4$ then $a_{n-2} < \frac{1}{2} \cdot 4d''$, and hence $a_{n-2} = d''$, $a_{n+1} = \frac{15}{4}m'a_{n-2} = \frac{15}{4} \cdot 3a_{n-2} \geq \frac{45}{4} \cdot 2^{n-2} > 2^{n+1}$.

Both of them have produced the induction claim. But now there are no cases left. Induction is complete; the inequality $a_n \geq 2^n$ holds for all $n$.

$Qed.$
