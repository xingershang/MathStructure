# Natural Language

**4.2 Lemma.** *For two $S$-structures $\mathfrak{A}$ and $\mathfrak{B}$,*  
$$\mathfrak{B} \equiv \mathfrak{A} \quad \text{iff} \quad \mathfrak{B} \models \mathrm{Th}(\mathfrak{A}).$$

*Proof.* If $\mathfrak{B} \equiv \mathfrak{A}$ then, since $\mathfrak{A} \models \mathrm{Th}(\mathfrak{A})$, also $\mathfrak{B} \models \mathrm{Th}(\mathfrak{A})$. Conversely, if $\mathfrak{B} \models \mathrm{Th}(\mathfrak{A})$ then, given an $S$-sentence $\varphi$, we examine the two possibilities:  
(i) If $\mathfrak{A} \models \varphi$ then $\varphi \in \mathrm{Th}(\mathfrak{A})$ and hence $\mathfrak{B} \models \varphi$.  
(ii) If not $\mathfrak{A} \models \varphi$ then $\neg \varphi \in \mathrm{Th}(\mathfrak{A})$; thus $\mathfrak{B} \models \neg \varphi$ and therefore not $\mathfrak{B} \models \varphi$.  
$\square$
