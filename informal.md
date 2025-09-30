2.19 *linear dependence lemma*

Suppose $v_1, ..., v_m$ is a linearly dependent list in $V$. Then there exists $k \in \{1, 2, ..., m\}$ such that

$$v_k \in \operatorname{span}(v_1, ..., v_{k-1}).$$

Furthermore, if $k$ satisfies the condition above and the $k^{th}$ term is removed from $v_1, ..., v_m$, then the span of the remaining list equals $\operatorname{span}(v_1, ..., v_m)$.

**Proof** Because the list $v_1, ..., v_m$ is linearly dependent, there exist numbers $a_1, ..., a_m \in \mathbf{F}$, not all 0, such that

$$a_1 v_1 + \cdots + a_m v_m = 0.$$

Let $k$ be the largest element of $\{1, ..., m\}$ such that $a_k \neq 0$. Then

$$v_k = -\frac{a_1}{a_k} v_1 - \cdots - \frac{a_{k-1}}{a_k} v_{k-1},$$

which proves that $v_k \in \operatorname{span}(v_1, ..., v_{k-1})$, as desired.

Now suppose $k$ is any element of $\{1, ..., m\}$ such that $v_k \in \operatorname{span}(v_1, ..., v_{k-1})$. Let $b_1, ..., b_{k-1} \in \mathbf{F}$ be such that

2.20  
$$v_k = b_1 v_1 + \cdots + b_{k-1} v_{k-1}.$$

Suppose $u \in \operatorname{span}(v_1, ..., v_m)$. Then there exist $c_1, ..., c_m \in \mathbf{F}$ such that

$$u = c_1 v_1 + \cdots + c_m v_m.$$

In the equation above, we can replace $v_k$ with the right side of 2.20, which shows that $u$ is in the span of the list obtained by removing the $k^{th}$ term from $v_1, ..., v_m$. Thus removing the $k^{th}$ term of the list $v_1, ..., v_m$ does not change the span of the list.

