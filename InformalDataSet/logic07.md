# Natural Language

**7.6 Lemma.** *Let $\Phi$ be consistent and suppose $\Phi$ allows representations. Then $\Phi^\vdash$ is not representable in $\Phi$.*

*Proof.* Suppose the assumptions of the lemma hold and let $\chi(v_0)$ represent $\Phi^\vdash$ in $\Phi$. By the consistency of $\Phi$ we get for an arbitrary $\alpha \in L^{S_{ar}}_0$,  
$$(1) \quad \Phi \vdash \neg \chi(\mathfrak{n}^\alpha) \quad \text{iff} \quad \text{not } \Phi \vdash \alpha.$$

For $\psi := \neg \chi$ we choose, by 7.5, a "fixed point" $\varphi \in L^{S_{ar}}_0$ such that  
$$(2) \quad \Phi \vdash \varphi \leftrightarrow \neg \chi(\mathfrak{n}^\varphi).$$

($\varphi$ says intuitively "I am not true.") But then  
$$\Phi \vdash \varphi \quad \text{iff} \quad \Phi \vdash \neg \chi(\mathfrak{n}^\varphi) \quad (\text{by } (2))$$  
$$\quad \text{iff} \quad \text{not } \Phi \vdash \varphi \quad (\text{by } (1)),$$  
a contradiction.  
$\square$
