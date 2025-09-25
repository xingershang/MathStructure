# Natural Language

**7.5 Fixed Point Theorem.** *Suppose $\Phi$ allows representations. Then, for every $\psi \in L^{S_{ar}}_1$, there is an $S_{ar}$-sentence $\varphi$ such that*  
$$\Phi \vdash \varphi \leftrightarrow \psi(\mathfrak{n}^\varphi).$$

Intuitively, $\varphi$ says: "I have the property $\psi$."

*Proof.* Let $F: \mathbb{N} \times \mathbb{N} \to \mathbb{N}$ be given by  
$$F(n,m) = \begin{cases} n^{\chi(m)}, & \text{if } n = n^\chi \text{ for some } \chi \in L^{S_{ar}}_1; \\ 0, & \text{otherwise}. \end{cases}$$

Clearly, $F$ is computable, and for $\chi \in L^{S_{ar}}_1$ we have  
$$F(n^\chi, m) = n^{\chi(m)}.$$

Since $\Phi$ allows representations, $F$ can be represented in $\Phi$ by a suitable $S_{ar}$-formula $\alpha(v_0, v_1, v_2)$. We write $x,y,z$ for $v_0, v_1, v_2$. For given $\psi \in L^{S_{ar}}_1$ we set  
$$\beta := \forall z (\alpha(x, x, z) \to \psi(z)), \quad \varphi := \forall z (\alpha(n^\beta, n^\beta, z) \to \psi(z)).$$

Since $\beta \in L^{S_{ar}}_1$ and $\varphi = \beta \mathfrak{n}^\beta_x$, we have $F(n^\beta, n^\beta) = n^\varphi$ and hence  
$$(1) \quad \Phi \vdash \alpha(n^\beta, n^\beta, n^\varphi).$$

Now we show the claim for $\varphi$ and $\psi$, i.e.  
$$\Phi \vdash \varphi \leftrightarrow \psi(n^\varphi).$$

For the direction from left to right, we have by definition of $\varphi$ that  
$$\Phi \cup \{\varphi\} \vdash \alpha(n^\beta, n^\beta, n^\varphi) \to \psi(n^\varphi),$$  
by (1) therefore $\Phi \vdash \varphi \to \psi(n^\varphi)$.

On the other hand, $\alpha$ represents the function $F$ in $\Phi$, in particular  
$$\Phi \vdash \exists^{=1} z \alpha(n^\beta, n^\beta, z);$$  
thus by (1)  
$$\Phi \vdash \forall z (\alpha(n^\beta, n^\beta, z) \to z \equiv n^\varphi)$$  
and therefore  
$$\Phi \vdash \psi(n^\varphi) \to \forall z (\alpha(n^\beta, n^\beta, z) \to \psi(z)),$$  
that is  
$$\Phi \vdash \psi(n^\varphi) \to \varphi.$$  
$\square$

