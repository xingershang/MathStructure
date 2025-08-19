## Goal

Prove that for all positive integers $n>2$, 

$$
n!\mid \left(\prod\limits_{p<q\leqslant n,}(p+q)\right)
$$

this only holds for $n=7.$

## Proof

Assume that $n$ satisfies $n!\mid \prod\limits_{p<q\leq n}(p+q)$ and let $2=p_1<p_2<\cdots<p_m\leq n$ be the primes in $1,2,\cdots,n$. Each such prime divides $n!$. In particular, $p_m\mid p_i+p_j$ for some $p_i<p_j\leqslant n.$ But

$$0<\frac{p_i+p_j}{p_m}<\frac{p_m+p_m}{p_m}=2,$$

so $p_m=p_i+p_j$ which implies $m\geqslant3,p_i=2$ and $p_m=2+p_j=2+p_{m-1}.$

Similarly, $p_{m-1}\mid p_{k}+p_{l}$ for some $p_{k}<p_{l}\leqslant n.$ But

$$0<\dfrac{p_l+p_k}{p_{m-1}}\leqslant\dfrac{p_m+p_{m-1}}{p_{m-1}}=\dfrac{2p_{m-1}+2}{p_{m-1}}<3,$$

so either $p_m-1=p_l+p_k$ or $2p_{m-1}=p_l+p_k.$ As above, the former case gives $p_m-1=2+p_{m-2}.$ If $2p_{m-1}=p_{l}+p_{k}$,then $p_{m-1}<p_{k}$, so $k=m$ and

$$2p_{m-1}=p_l+p_{m-1}+2\Rightarrow p_{m-1}=p_l+2=p_{m-2}+2.$$

Either way, $p_{m-2} > 2$ and 3 divides one of $p_{m-2}, p_{m-1} = p_{m-2} + 2$ and $p_m = p_{m-2} + 4$. This implies $p_{m-2} = 3$ and thus $p_m = 7$, giving $7 \leq n < 11$.

Finally, a quick computation shows that $7! \mid \prod_{p < q \leq 7} (p + q)$ but $8! \nmid \prod_{p < q \leq 7} (p + q)$, so neither does $9!$ and $10!$.

$Qed.$