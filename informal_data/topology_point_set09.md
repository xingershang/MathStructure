# Natural Language

**Theorem 21.6 (Uniform limit theorem).** Let $f_n : X \to Y$ be a sequence of continuous functions from the topological space $X$ to the metric space $Y$. If $(f_n)$ converges uniformly to $f$, then $f$ is continuous.

*Proof.* Let $V$ be open in $Y$; let $x_0$ be a point of $f^{-1}(V)$. We wish to find a neighborhood $U$ of $x_0$ such that $f(U) \subset V$.

Let $y_0 = f(x_0)$. First choose $\epsilon$ so that the $\epsilon$-ball $B(y_0, \epsilon)$ is contained in $V$. Then, using uniform convergence, choose $N$ so that for all $n \geq N$ and all $x \in X$,

$$d(f_n(x), f(x)) < \epsilon / 3.$$

Finally, using continuity of $f_N$, choose a neighborhood $U$ of $x_0$ such that $f_N$ carries $U$ into the $\epsilon / 3$ ball in $Y$ centered at $f_N(x_0)$.

We claim that $f$ carries $U$ into $B(y_0, \epsilon)$ and hence into $V$, as desired. For this purpose, note that if $x \in U$, then

$$d(f(x), f_N(x)) < \epsilon / 3 \quad \text{(by choice of $N$)},$$

$$d(f_N(x), f_N(x_0)) < \epsilon / 3 \quad \text{(by choice of $U$)},$$

$$d(f_N(x_0), f(x_0)) < \epsilon / 3 \quad \text{(by choice of $N$)}.$$

Adding and using the triangle inequality, we see that $d(f(x), f(x_0)) < \epsilon$, as desired. ■
