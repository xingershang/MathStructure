**Theorem 9.7** (Doob Decomposition). Let $\{X_n, \mathcal{F}_n, n=0,1,2,\ldots\}$ be a submartingale. Then there exists a martingale $\{M_n, \mathcal{F}_n, n=0,1,2,\ldots\}$ and a process $\{A_n, n=0,1,2,\ldots\}$ such that for $n=0,1,2,\ldots$

1. $A_n \leq A_{n+1}$ a.e.,
2. $A_0 = 0$ and $A_n$ is $\mathcal{F}_{n-1}$-measurable, $n=1,2,3,\ldots$,
3. $X_n = M_n + A_n, n=0,1,2,\ldots$.

**Proof.** Let $d_n = E\{X_{n+1} - X_n \mid \mathcal{F}_n\}$. Then $d_n \geq 0$ by the submartingale inequality, and $d_n$ is $\mathcal{F}_n$-measurable. Define $A_0 = 0$, $M_0 = X_0$, and

$$
A_n \overset{\text{def}}{=} d_1 + \cdots + d_{n-1}, \quad M_n \overset{\text{def}}{=} X_n - A_n, \quad n=1,2,3,\ldots.
$$

It is clear that (i), (ii) and (iii) hold. We must verify that $M_n$ is a martingale. It is adapted. Calculate

$$
E\{M_{n+1} \mid \mathcal{F}_n\} = E\{X_{n+1} - A_{n+1} \mid \mathcal{F}_n\} = E\{X_{n+1} - X_n + \underbrace{X_n - A_n}_{M_n} - (A_{n+1} - A_n) \mid \mathcal{F}_n\}
$$

which is

$$
= d_n + M_n - \underbrace{(A_{n+1} - A_n)}_{d_n} = M_n.
$$

Thus, $M_n$ is indeed a martingale.  □
