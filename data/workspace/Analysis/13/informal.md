## Goal

$\lim_{n \to \infty} \frac{n}{q^n} = 0$ if $q > 1$.

## Proof

Indeed, if $x_n = \frac{n}{q^n}$, then $x_{n+1} = \frac{n+1}{nq} x_n$ for $n \in \mathbb{N}$. Since $\lim_{n \to \infty} \frac{n+1}{nq} = \lim_{n \to \infty} \left( \frac{1 + \frac{1}{n}}{q} \right) = \lim_{n \to \infty} \left( 1 + \frac{1}{n} \right) \cdot \lim_{n \to \infty} \frac{1}{q} = 1 \cdot \frac{1}{q} = \frac{1}{q} < 1$, there exists an index $N$ such that $\frac{n+1}{nq} < 1$ for $n > N$. Thus we shall have $x_{n+1} < x_n$ for $n > N$, so that the sequence will be monotonically decreasing from index $N$ on. As one can see from the definition of a limit, a finite set of terms of a sequence has no effect on the convergence of a sequence or its limit, so that it now suffices to find the limit of the sequence $x_{N+1} > x_{N+2} > \cdots$.

The terms of this sequence are positive, that is, the sequence is bounded below. Therefore it has a limit.

Let $x = \lim_{n \to \infty} x_n$. It now follows from the relation $x_{n+1} = \frac{n+1}{nq} x_n$ that

$$
x = \lim_{n \to \infty} (x_{n+1}) = \lim_{n \to \infty} \left( \frac{n+1}{nq} x_n \right) = \lim_{n \to \infty} \frac{n+1}{nq} \cdot \lim_{n \to \infty} x_n = \frac{1}{q} x,
$$

from which we find $\left( 1 - \frac{1}{q} \right) x = 0$, and so $x = 0$.