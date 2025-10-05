**2.3.7 Chinese Remainder Theorem** Let $R$ be an arbitrary ring, and let $I_1, \ldots, I_n$ be ideals in $R$ that are relatively prime in pairs, that is, $I_i + I_j = R$ for all $i \neq j$.

(1) If $a_1 = 1$ (the multiplicative identity of $R$) and $a_j = 0$ (the zero element of $R$) for $j = 2, \ldots, n$, then there is an element $a \in R$ such that $a \equiv a_i \mod I_i$ for all $i = 1, \ldots, n$. More generally,

(2) If $a_1, \ldots, a_n$ are arbitrary elements of $R$, there is an element $a \in R$ such that $a \equiv a_i \mod I_i$ for all $i = 1, \ldots, n$.

(3) If $b$ is another element of $R$ such that $b \equiv a_i \mod I_i$ for all $i = 1, \ldots, n$, then $b \equiv a \mod I_1 \cap I_2 \cap \ldots \cap I_n$. Conversely, if $b \equiv a \mod \cap_{i=1}^n I_i$, then $b \equiv a_i \mod I_i$ for all $i$.

(4) $R / \cap_{i=1}^n I_i$ is isomorphic to the direct product $\prod_{i=1}^n R / I_i$.

*Proof.*  
(1) If $j > 1$ we have $I_1 + I_j = R$, so there exist elements $b_j \in I_1$ and $c_j \in I_j$ such that $b_j + c_j = 1$; thus

$$\prod_{j=2}^n (b_j + c_j) = 1.$$

Expand the left side and observe that any product containing at least one $b_j$ belongs to $I_1$, while $c_2 \cdots c_n$ belongs to $\prod_{j=2}^n I_j$, the collection of all finite sums of products $x_2 \cdots x_n$ with $x_j \in I_j$. Thus we have elements $b \in I_1$ and $a \in \prod_{j=2}^n I_j$ (a subset of each $I_j$) with $b + a = 1$. Consequently, $a \equiv 1 \mod I_1$ and $a \equiv 0 \mod I_j$ for $j > 1$, as desired.

(2) By the argument of part (1), for each $i$ we can find $c_i$ with $c_i \equiv 1 \mod I_i$ and $c_i \equiv 0 \mod I_j, j \neq i$. If $a = a_1 c_1 + \cdots + a_n c_n$, then $a$ has the desired properties. To see this, write $a - a_i = a - a_i c_i + a_i (c_i - 1)$, and note that $a - a_i c_i$ is the sum of the $a_j c_j, j \neq i$, and is therefore congruent to $0 \mod I_i$.

(3) We have $b \equiv a_i \mod I_i$ for all $i$ iff $b - a \equiv 0 \mod I_i$ for all $i$, that is, iff $b - a \in \cap_{i=1}^n I_i$, and the result follows.

(4) Define $f : R \to \prod_{i=1}^n R / I_i$ by $f(a) = (a + I_1, \ldots, a + I_n)$. If $a_1, \ldots, a_n \in R$, then by part (2) there is an element $a \in R$ such that $a \equiv a_i \mod I_i$ for all $i$. But then $f(a) = (a_1 + I_1, \ldots, a_n + I_n)$, proving that $f$ is surjective. Since the kernel of $f$ is the intersection of the ideals $I_j$, the result follows from the first isomorphism theorem for rings. ♣