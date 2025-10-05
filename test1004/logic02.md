**1.9 Lemma.** *Suppose that* $\Phi$ *is consistent and negation complete and that it contains witnesses. Then the following holds for all* $\varphi$ *and* $\psi$:
(a) $\Phi \vdash \neg \varphi$ *iff not* $\Phi \vdash \varphi$.
(b) $\Phi \vdash (\varphi \lor \psi)$ *if and only if* $\Phi \vdash \varphi$ *or* $\Phi \vdash \psi$.
(c) $\Phi \vdash \exists x \varphi$ *if and only if there is a term* $t$ *with* $\Phi \vdash \varphi \frac{t}{x}$.

*Proof.* (a) Since $\Phi$ is negation complete, we have $\Phi \vdash \varphi$ or $\Phi \vdash \neg \varphi$; and since $\Phi$ is consistent, $\Phi \vdash \neg \varphi$ iff not $\Phi \vdash \varphi$.

(b) First let $\Phi \vdash (\varphi \lor \psi)$. If not $\Phi \vdash \varphi$, then $\Phi \vdash \neg \varphi$ (since $\Phi$ is negation complete), and IV.3.4 gives $\Phi \vdash \psi$. The other direction follows immediately by the $\lor$-rules ($\lor$S) for the succedent.

(c) Let $\Phi \vdash \exists x \varphi$. Since $\Phi$ contains witnesses, there is a term $t$ with $\Phi \vdash (\exists x \varphi \to \varphi \frac{t}{x})$; using Modus ponens, IV.3.5, we get $\Phi \vdash \varphi \frac{t}{x}$. Conversely let $\Phi \vdash \varphi \frac{t}{x}$ for a term $t$. Then the rule ($\exists$S) of the $\exists$-introduction in the succedent gives $\Phi \vdash \exists x \varphi$.
