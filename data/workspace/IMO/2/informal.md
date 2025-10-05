## Goal

Let $k\geqslant2$ be an integer. Prove that the smallest integer $n\geqslant k+1$ with the property that "there exists a set of $n$ distinct real numbers such that each of its elements can be written as a sum of $k$ other distinct elements of the set" is $n=k+4$.

## Proof

First we show that $n\geqslant k+ 4$. Suppose that there exists such a set with $n$ numbers and denote them by $a_1<a_2<\cdots<a_n$.

Note that in order to express $a_1$ as a sum of $k$ distinct elements of the set, we must have $a_1\geqslant a_2+\cdots+a_{k+1}$ and, similarly for $a_n$, we must have $a_{n-k}+\cdots+a_{n-1}\geqslant a_n.$ We also know $\mathop{\text{that }}n\geqslant k+1.$

If $n=k+1$ then we have $a_1\geqslant a_2+\cdots+a_{k+1}>a_1+\cdots+a_k\geqslant a_{k+1}$, which gives a contradiction.

If $n= k+ 2$ then we have $a_1\geqslant a_2+ \cdots + a_{k+ 1}\geqslant a_{k+ 2}$, that again gives a contradiction. 

If $n= k+ 3$ then we have $a_1\geqslant a_2+ \cdots + a_{k+ 1}$ and $a_3+ \cdots + a_{k+ 2}\geqslant a_{k+ 3}.$ Adding the two inequalities we get $a_1+a_{k+2}\geqslant a_2+a_{k+3}$, again a contradiction.

It remains to give an example of a set with $k+4$ elements satisfying the condition of the problem. We start with the case when $k=2l$ and $l\geqslant1.$ In that case, denote by $A_i=\{-i,i\}$ and take the set $A_1\cup\cdots\cup A_{l+2}$, which has exactly $k+4=2l+4$ elements. We are left to show that this set satisfes the required condition.

Note that if a number $i$ can be expressed in the desired way, then so can $-i$ by negating the expression. Therefore, we consider only $1\leqslant i\leqslant l+2$.

If $i<l+2$, we sum the numbers from some $l-1$ sets $A_j$ with $j\neq1,i+1$, and the numbers $i+1$ and $-1$.

For $i= l+ 2$, we sum the numbers from some $l- 1$ sets $A_{j}$ with $j\neq 1, l+ 1$, and the numbers $l+1$ and $1$.

It remains to a give a construction for odd $k=2l+1$ with $l\geqslant1$ (since $k\geqslant2).$ To that end, we modify the construction for $k=2l$ by adding 0 to the previous set.

This is a valid set as $0$ can be added to each constructed expression, and $0$ can be expressed as follows: take the numbers $1,2,-3$ and all the numbers from the remaining $l-1$ sets $A_4,A_5,\cdots,A_{l+2}.$

$Qed.$