# Natural Language

## Goal

Let $\{x_n\}$ and $\{y_n\}$ be two convergent sequences with $\lim_{n \to \infty} x_n = A$ and $\lim_{n \to \infty} y_n = B$. Prove that if $A < B$, then there exists an index $N \in \mathbb{N}$ such that $x_n < y_n$ for all $n > N$.

$Proof.$

Choose a number $C$ such that $A < C < B$. By definition of limit, we can find numbers $N'$ and $N''$ such that $|x_n - A| < C - A$ for all $n > N'$ and $|y_n - B| < B - C$ for all $n > N''$. Then for $n > N = \max\{N', N''\}$ we shall have $x_n < A + C - A = C = B - (B - C) < y_n$.

$Qed.$

