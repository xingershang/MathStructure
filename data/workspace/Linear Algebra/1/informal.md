2.6 *span is the smallest containing subspace*

The span of a list of vectors in $V$ is the smallest subspace of $V$ containing all vectors in the list.

**Proof** Suppose $v_1, ..., v_m$ is a list of vectors in $V$.  
First we show that $\operatorname{span}(v_1, ..., v_m)$ is a subspace of $V$. The additive identity is in $\operatorname{span}(v_1, ..., v_m)$ because

$$0 = 0v_1 + \cdots + 0v_m.$$

Also, $\operatorname{span}(v_1, ..., v_m)$ is closed under addition because

$$(a_1 v_1 + \cdots + a_m v_m) + (c_1 v_1 + \cdots + c_m v_m) = (a_1 + c_1) v_1 + \cdots + (a_m + c_m) v_m.$$

Furthermore, $\operatorname{span}(v_1, ..., v_m)$ is closed under scalar multiplication because

$$\lambda (a_1 v_1 + \cdots + a_m v_m) = \lambda a_1 v_1 + \cdots + \lambda a_m v_m.$$

Thus $\operatorname{span}(v_1, ..., v_m)$ is a subspace of $V$ (by 1.34).  
Each $v_k$ is a linear combination of $v_1, ..., v_m$ (to show this, set $a_k = 1$ and let the other $a$'s in 2.2 equal 0). Thus $\operatorname{span}(v_1, ..., v_m)$ contains each $v_k$. Conversely, because subspaces are closed under scalar multiplication and addition, every subspace of $V$ that contains each $v_k$ contains $\operatorname{span}(v_1, ..., v_m)$. Thus $\operatorname{span}(v_1, ..., v_m)$ is the smallest subspace of $V$ containing all the vectors $v_1, ..., v_m$.
