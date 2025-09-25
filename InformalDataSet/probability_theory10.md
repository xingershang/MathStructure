# Natural Language

**Theorem 9.23** (Martingale Convergence Theorem). Let $\{X_n, \mathcal{F}_n, n=0,1,2,\ldots\}$ be a submartingale. Suppose that $\sup_n E\{|X_n|\} < \infty$. Then there exists a finite random variable $X_\infty$ such that

$$
\lim_{n \to \infty} X_n = X_\infty \quad a.s.
$$

**Proof.** First let us show that $\liminf_{n \to \infty} X_n = \limsup_{n \to \infty} X_n$ a.s. If this is not true, then $\liminf_n X_n < \limsup_n X_n$ with positive probability. Fix $\omega$ for which $\liminf_n X_n(\omega) < \limsup_n X_n(\omega)$. (Once we have fixed $\omega$, we are just dealing with a sequence of real numbers.) Then there exist rational $a < b$ for which $\liminf_n X_n(\omega) < a < b < \limsup_n X_n(\omega)$. Then there exist infinitely many $n$ for which $X_n < a$, and infinitely many $n$ for which $X_n > b$. But for this to happen, the process must cross $[a,b]$ infinitely often. Thus, $\nu_\infty(a,b)(\omega) = \infty$.

By the upcrossing inequality,

$$
E\{\nu_\infty(a,b)\} \leq \frac{\sup_N E\{(X_N - a)^+\}}{b - a} \leq \frac{\sup_N E\{|X_N|\} + |a|}{b - a},
$$

and this is finite by hypothesis. Thus, $P\{\nu_\infty(a,b) = \infty\} = 0$. This is true simultaneously for each of the countable number of rational pairs $a < b$, and it follows that the set of $\omega$ for which $\liminf_n X_n(\omega) < \limsup_n X_n(\omega)$ has probability zero. In short, $P\{\liminf_n X_n = \limsup_n X_n\} = 1$, so the limit exists almost surely. Thus, $X_\infty \overset{\text{def}}{=} \lim_n X_n = \liminf_n X_n = \limsup_n X_n$ exists. A priori it might be infinite. However, by Fatou's Lemma,

$$
E\{|X_\infty|\} \leq \liminf_{n \to \infty} E\{|X_n|\} < \infty.
$$

Thus, $X_\infty$ is finite a.s.  □
