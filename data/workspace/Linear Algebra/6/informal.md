3.56 *column–row factorization*

Suppose $A$ is an $m$-by-$n$ matrix with entries in $\mathbf{F}$ and column rank $c \geq 1$. Then there exist an $m$-by-$c$ matrix $C$ and a $c$-by-$n$ matrix $R$, both with entries in $\mathbf{F}$, such that $A = CR$.

**Proof** Each column of $A$ is an $m$-by-1 matrix. The list $A_{\cdot,1}, ..., A_{\cdot,n}$ of columns of $A$ can be reduced to a basis of the span of the columns of $A$ (by 2.30). This basis has length $c$, by the definition of the column rank. The $c$ columns in this basis can be put together to form an $m$-by-$c$ matrix $C$.

If $k \in \{1, ..., n\}$, then column $k$ of $A$ is a linear combination of the columns of $C$. Make the coefficients of this linear combination into column $k$ of a $c$-by-$n$ matrix that we call $R$. Then $A = CR$, as follows from 3.51(a).
