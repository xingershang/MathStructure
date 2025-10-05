4.6 Coincidence Lemma. Let $\mathfrak{I}_1 = (\mathcal{A}_1, \beta_1)$ be an $S_1$-interpretation and $\mathfrak{I}_2 = (\mathcal{A}_2, \beta_2)$ be an $S_2$-interpretation, both with the same domain, i.e. $A_1 = A_2$. Put $S := S_1 \cap S_2$.

(a) Let $t$ be an $S$-term. If $\mathfrak{I}_1$ and $\mathfrak{I}_2$ agree on the $S$-symbols occurring in $t$ and on the variables occurring in $t$, then $\mathfrak{I}_1(t) = \mathfrak{I}_2(t)$. (Note: $\mathfrak{I}_1$ and $\mathfrak{I}_2$ agree on $k \in S$ or on $x$ if $k^{\mathcal{A}_1} = k^{\mathcal{A}_2}$ or $\beta_1(x) = \beta_2(x)$, respectively.)

(b) Let $\varphi$ be an $S$-formula. If $\mathfrak{I}_1$ and $\mathfrak{I}_2$ agree on the $S$-symbols and on the variables occurring free in $\varphi$, then $\mathfrak{I}_1 \models \varphi$ iff $\mathfrak{I}_2 \models \varphi$.

**Proof.** (a) We use induction on $S$-terms.

$t = x$: By hypothesis, $\beta_1(x) = \beta_2(x)$ and therefore

$$\mathfrak{I}_1(x) = \beta_1(x) = \beta_2(x) = \mathfrak{I}_2(x).$$

$t = c$: Similarly.

$t = f t_1 \ldots t_n$ ($f \in S$ $n$-ary and $t_1, \ldots, t_n \in T^S$):

$$\mathfrak{I}_1(f t_1 \ldots t_n) = f^{\mathcal{A}_1}(\mathfrak{I}_1(t_1), \ldots, \mathfrak{I}_1(t_n))$$

$$= f^{\mathcal{A}_1}(\mathfrak{I}_2(t_1), \ldots, \mathfrak{I}_2(t_n)) \quad \text{(by induction hypothesis)}$$

$$= f^{\mathcal{A}_2}(\mathfrak{I}_2(t_1), \ldots, \mathfrak{I}_2(t_n)) \quad \text{(by hypothesis, } f^{\mathcal{A}_1} = f^{\mathcal{A}_2})$$

$$= \mathfrak{I}_2(f t_1 \ldots t_n).$$

(b) We use induction on $S$-formulas.

$\varphi = R t_1 \ldots t_n$ ($R \in S$ $n$-ary, $t_1, \ldots, t_n \in T^S$):

$$\mathfrak{I}_1 \models R t_1 \ldots t_n \iff R^{\mathcal{A}_1} \mathfrak{I}_1(t_1) \ldots \mathfrak{I}_1(t_n)$$

$$\iff R^{\mathcal{A}_1} \mathfrak{I}_2(t_1) \ldots \mathfrak{I}_2(t_n) \quad \text{(by (a))}$$

$$\iff R^{\mathcal{A}_2} \mathfrak{I}_2(t_1) \ldots \mathfrak{I}_2(t_n) \quad \text{(by hypothesis, } R^{\mathcal{A}_1} = R^{\mathcal{A}_2})$$

$$\iff \mathfrak{I}_2 \models R t_1 \ldots t_n.$$

$\varphi = t_1 \equiv t_2$: Similarly.

$\varphi = \neg \psi$: $\mathfrak{I}_1 \models \neg \psi$

iff not $\mathfrak{I}_1 \models \psi$

iff not $\mathfrak{I}_2 \models \psi$ (by induction hypothesis)

iff $\mathfrak{I}_2 \models \neg \psi$.

$\varphi = (\psi \lor \chi)$: Similarly.

$\varphi = \exists x \psi$: $\mathfrak{I}_1 \models \exists x \psi$

iff there is an $a \in A_1$ such that $\mathfrak{I}_1 \frac{a}{x} \models \psi$

iff there is an $a \in A_2 (= A_1)$ such that $\mathfrak{I}_2 \frac{a}{x} \models \psi$

(by induction hypothesis applied to $\psi$, $\mathfrak{I}_1 \frac{a}{x}$ and $\mathfrak{I}_2 \frac{a}{x}$; note that, because $\operatorname{free}(\psi) \subset \operatorname{free}(\varphi) \cup \{x\}$, the interpretations $\mathfrak{I}_1 \frac{a}{x}$ and $\mathfrak{I}_2 \frac{a}{x}$ agree on all symbols occurring in $\psi$ and all variables occurring free in $\psi$)

iff $\mathfrak{I}_2 \models \exists x \psi$.
