# Natural Language

**3.1.3 Theorem** Let $f$ be a nonconstant polynomial over the field $F$. Then there is an extension $E/F$ and an element $\alpha \in E$ such that $f(\alpha) = 0$.

*Proof.* Since $f$ can be factored into irreducibles, we may assume without loss of generality that $f$ itself is irreducible. The ideal $I = <f(X)>$ in $F[X]$ is prime (see (2.6.1)), in fact maximal (see (2.6.9)). Thus $E = F[X]/I$ is a field by (2.4.3). We have a problem at this point because $F$ need not be a subset of $E$, but we can place an isomorphic copy of $F$ inside $E$ via the homomorphism $h : a \to a + I$; by (3.1.2), $h$ is a monomorphism, so we may identify $F$ with a subfield of $E$. Now let $\alpha = X + I$; if $f(X) = a_0 + a_1 X + \cdots + a_n X^n$, then

$$
\begin{aligned}
f(\alpha) &= (a_0 + I) + a_1 (X + I) + \cdots + a_n (X + I)^n \\
&= (a_0 + a_1 X + \cdots + a_n X^n) + I \\
&= f(X) + I
\end{aligned}
$$

which is zero in $E$. ♣