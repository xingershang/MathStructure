# Natural Language

## Goal

Let $(a_{n})_{n\geqslant1}$ be a sequence of positive real numbers with the property that $(a_{n+1})^2+a_na_{n+2}\leqslant a_n+a_{n+2}$ for all positive integers $n$. Prove that $a_{2022}\leqslant1$.

## Proof

We begin by observing that $(a_{n+1})^{2}-1\leqslant a_{n}+a_{n+2}-a_{n}a_{n+2}-1$, which is equivalent to $$(a_{n+1})^2-1\leqslant(1-a_n)(a_{n+2}-1).$$ Suppose now that there exists a positive integer $n$ such that $a_{n+1}>1$ and $a_{n+2}>1$. Since $( a_{n+ 1}) ^{2}- 1$ $\leqslant$ $( 1- a_{n}) ( a_{n+ 2}- 1)$ ,we deduce that $0 < 1- a_{n} < 1 < 1 + a_{n+ 2}$ ，thus $(a_{n+1})^{2}-1<(a_{n+2}+1)(a_{n+2}-1)=(a_{n+2})^{2}-1$.

On the other hand, $(a_{n+2})^{2}-1\leqslant(1-a_{n+3})(a_{n+1}-1)$$<(1+a_{n+1})(a_{n+1}-1)=(a_{n+1})^{2}-1$, a contradiction. We have shown that we cannot have two consecutive terms,except maybe $a_1$ and $a_2$ ,strictly greater than 1.

Finally, suppose $a_{2022}>1$. This implies that $a_{2021}\leqslant1$ and $a_{2023}\leqslant1$ . Therefore $0<(a_{2022})^{2}-1\leqslant(1-a_{2021})(a_{2023}-1)\leqslant0$, a contradiction. We conclude that $a_{2022}\leqslant 1$.

$Qed.$