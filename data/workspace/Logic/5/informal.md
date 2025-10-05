**6.11 $\beta$-Function Lemma$^3$.** *There is a function $\beta: \mathbb{N}^3 \to \mathbb{N}$ with the following properties:*

(a) *For every sequence $(a_0, \ldots, a_r)$ over $\mathbb{N}$ there exist $t,p \in \mathbb{N}$ such that for all $i \le r$*  
$$\beta(t,p,i) = a_i.$$

(b) *$\beta$ is definable in $L^{S_{ar}}$, i.e. there exists an $S_{ar}$-formula $\varphi_\beta(v_0, v_1, v_2, v_3)$ such that for all $t,p,i,a \in \mathbb{N}$,*  
$$\mathbb{N} \models \varphi_\beta[t,p,i,a] \quad \text{iff} \quad \beta(t,p,i) = a.$$

*Proof.* Given $(a_0, \ldots, a_r)$, we choose a prime $p$ which is larger than $a_0, \ldots, a_r, r+1$ and set  
$$(*) \quad t := 1 \cdot p^0 + a_0 p^1 + 2 p^2 + a_1 p^3 + \ldots + (i+1) p^{2i} + a_i p^{2i+1} + \ldots + (r+1) p^{2r} + a_r p^{2r+1}.$$

By choice of $p$ the right-hand side is the $p$-adic representation of $t$.

First, we show that for all $i$, $0 \le i \le r$,  
$$(**) \quad a = a_i \quad \text{iff} \quad \text{there are } b_0, b_1, b_2 \text{ such that}$$  
(i) $t = b_0 + b_1 ((i+1) + a p + b_2 p^2)$,  
(ii) $a < p$,  
(iii) $b_0 < b_1$,  
(iv) $b_1 = p^{2m}$ for a suitable $m$.

The implication from left to right follows immediately from $(*)$ with  
$$b_0 := 1 \cdot p^0 + \ldots + a_{i-1} p^{2i-1},$$  
$$b_1 := p^{2i},$$  
$$b_2 := (i+2) + a_{i+1} p + \ldots + a_r p^{2(r-i)-1}.$$

Conversely, suppose (i) – (iv) hold for $b_0, b_1, b_2$ and let $b_1 = p^{2m}$. From (i) we obtain  
$$t = b_0 + (i+1) p^{2m} + a p^{2m+1} + b_2 p^{2m+2}.$$

Since $b_0 < p^{2m}$, $a < p$, and $i+1 < p$, and since the $p$-adic representation of $t$ is unique, a comparison with $(*)$ yields $m = i$ and $a = a_i$.

Obviously, (iv) from $(**)$ is equivalent to  
(iv)$'$ $b_1$ is a square and for all $d \neq 1$ with $d \mid b_1$ we have $p \nmid d$.

We define $\beta(t,p,i)$ to be the uniquely determined (and hence the smallest) $a$ for which the right-hand side of $(**)$ (with (iv)$'$ instead of (iv)) holds. We extend this definition to arbitrary triples of natural numbers by specifying:

Let $\beta(u,q,j)$ be the smallest $a$ such that there are $b_0, b_1, b_2$ with  
(i) $u = b_0 + b_1 ((j+1) + a q + b_2 q^2)$,  
(ii) $a < q$,  
(iii) $b_0 < b_1$,  
(iv)$'$ $b_1$ is a square, and for all $d \neq 1$ with $d \mid b_1$ we have $q \nmid d$.

If no such $a$ exists let $\beta(u,q,j) = 0$.

Then $\beta$ has the properties required in (a).

The definition of $\beta$ just given leads immediately to an $S_{ar}$-formula $\varphi_\beta(v_0, v_1, v_2, v_3)$ defining $\beta$. So (b) holds as well.  
$\square$

