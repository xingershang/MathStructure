**Proposition 3.44.** Let $X$ and $Y$ have joint density $f_{XY}(x,y)$. Then $Z \equiv X + Y$ has a density $f_Z(z)$ given by

$$
f_Z(z) = \int_{-\infty}^\infty f_{XY}(x, z - x) \, dx = \int_{-\infty}^\infty f_{XY}(z - y, y) \, dy.
$$

**Proof.** $X + Y \leq z \iff (X,Y) \in \{(x,y) : x + y \leq z\}$. Then the density $F_{X+Y}$ is

$$
F_{X+Y}(z) = P\{X + Y \leq z\} = \iint_{\{u+v \leq z\}} f_{XY}(u,v) \, du \, dv.
$$

Let $x = u$, $y = u + v$, a transformation with Jacobian 1. Then this is

$$
= \iint_{\{(x,y): y \leq z\}} f_{XY}(x, y - x) \, dx \, dy = \int_{-\infty}^z \left[ \int_{-\infty}^\infty f_{XY}(x, y - x) \, dx \right] dy.
$$

But $F_{X+Y}(z) = \int_{-\infty}^z f_{X+Y}(y) \, dy$, so, comparing the two integrals for $F_{X+Y}$, we see that $f_{X+Y}(y)$ must equal the term in square brackets. Add $X$ and $Y$ in the opposite order to get the second formula.  □