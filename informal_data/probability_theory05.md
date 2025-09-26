# Natural Language

**Theorem 4.9** (Borel-Cantelli Lemma). Let $\Lambda_1, \Lambda_2, \ldots$ be a sequence of events. Suppose that $\sum_{n=1}^\infty P\{\Lambda_n\} < \infty$. Then

$$
P\{\limsup_n \Lambda_n\} = 0.
$$

Conversely, if the $\Lambda_n$ are independent, there are only two possibilities:

$$
P\{\limsup_n \Lambda_n\} = \begin{cases}
0 & \iff \sum_{n=1}^\infty P\{\Lambda_n\} < \infty, \\
1 & \iff \sum_{n=1}^\infty P\{\Lambda_n\} = \infty.
\end{cases}
$$

**Proof.** The lim sup of the $\Lambda_n$ can be written as $\lim_{m \to \infty} \bigcup_{n=m}^\infty \Lambda_n$. Notice that the union decreases as $m$ increases, so

$$
P\{\limsup_n \Lambda_n\} = \lim_{m \to \infty} P\left\{\bigcup_{n=m}^\infty \Lambda_n\right\}
\leq \lim_{m \to \infty} \sum_{n=m}^\infty P\{\Lambda_n\}.
$$

But this is the tail of a convergent series (the series $\sum_n P\{\Lambda_n\}$ converges by hypothesis) so it converges to zero.

For the converse, consider

$$
P\{\limsup_n \Lambda_n\} = 1 - P\{\liminf_n \Lambda_n^c\}
= 1 - \lim_{m \to \infty} P\left\{\bigcap_{n=m}^\infty \Lambda_n^c\right\}
= 1 - \lim_{m \to \infty} \prod_{n=m}^\infty P\{\Lambda_n^c\}.
$$

But if $0 < x_n < 1$, $\prod_n (1 - x_n)$ is either zero or strictly positive according to whether $\sum_n x_n = \infty$ or $\sum_n x_n < \infty$, respectively. If the sum is finite, $\lim_{m \to \infty} \prod_{n=m}^\infty (1 - x_n) = 1$. Thus, the probability of the lim sup equals

$$
1 - \lim_{m \to \infty} \prod_{n=m}^\infty (1 - P\{\Lambda_n\}) = \begin{cases}
1 & \text{if } \sum_n P\{\Lambda_n\} = \infty, \\
0 & \text{if } \sum_n P\{\Lambda_n\} < \infty.
\end{cases}
$$

□
