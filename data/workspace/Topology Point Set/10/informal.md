**Theorem 20.1.** Let $X$ be a metric space with metric $d$. Define $\bar{d} : X \times X \to \mathbb{R}$ by the equation

$$\bar{d}(x,y) = \min\{d(x,y), 1\}.$$

Then $\bar{d}$ is a metric that induces the same topology as $d$.

The metric $\bar{d}$ is called the *standard bounded metric* corresponding to $d$.

*Proof.* Checking the first two conditions for a metric is trivial. Let us check the triangle inequality:

$$\bar{d}(x,z) \leq \bar{d}(x,y) + \bar{d}(y,z).$$

Now if either $d(x,y) \geq 1$ or $d(y,z) \geq 1$, then the right side of this inequality is at least 1; since the left side is (by definition) at most 1, the inequality holds. It remains to consider the case in which $d(x,y) < 1$ and $d(y,z) < 1$. In this case, we have

$$d(x,z) \leq d(x,y) + d(y,z) = \bar{d}(x,y) + \bar{d}(y,z).$$

Since $\bar{d}(x,z) \leq d(x,z)$ by definition, the triangle inequality holds for $\bar{d}$.

Now we note that in any metric space, the collection of $\epsilon$-balls with $\epsilon < 1$ forms a basis for the metric topology, for every basis element containing $x$ contains such an $\epsilon$-ball centered at $x$. It follows that $d$ and $\bar{d}$ induce the same topology on $X$, because the collections of $\epsilon$-balls with $\epsilon < 1$ under these two metrics are the same collection. ■
