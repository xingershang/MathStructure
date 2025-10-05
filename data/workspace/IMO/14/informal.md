## Goal

A sequence $x_1, x_2, \ldots$ is defined by $x_1 = 1$ and $x_{2k} = -x_k, x_{2k-1} = (-1)^{k+1} x_k$ for all $k \geq 1$. Prove that $x_1 + x_2 + \cdots + x_n \geq 0$ for all $n \geq 1$.

## Proof

We start with some observations. First, from the definition of $x_i$ it follows that for each positive integer $k$ we have
$$
x_{4k-3} = x_{2k-1} = -x_{4k-2} \quad \text{and} \quad x_{4k-1} = x_{4k} = -x_{2k} = x_k.
$$

Hence, denoting $S_n = \sum_{i=1}^n x_i$, we have

$$
S_{4k} = \sum_{i=1}^k ((x_{4k-3} + x_{4k-2}) + (x_{4k-1} + x_{4k})) = \sum_{i=1}^k (0 + 2x_k) = 2S_k,
$$

$$
S_{4k+2} = S_{4k} + (x_{4k+1} + x_{4k+2}) = S_{4k}.
$$

Observe also that $S_n = \sum_{i=1}^n x_i \equiv \sum_{i=1}^n 1 = n \ (\text{mod} \ 2)$.

Now we prove by induction on $k$ that $S_i \geq 0$ for all $i \leq 4k$. The base case is valid since $x_1 = x_3 = x_4 = 1, x_2 = -1$. For the induction step, assume that $S_i \geq 0$ for all $i \leq 4k$. Using the relations (1)-(3), we obtain

$$
S_{4k+4} = 2S_{k+1} \geq 0, \quad S_{4k+2} = S_{4k} \geq 0, \quad S_{4k+3} = S_{4k+2} + x_{4k+3} = \frac{S_{4k+2} + S_{4k+4}}{2} \geq 0.
$$

So, we are left to prove that $S_{4k+1} \geq 0$. If $k$ is odd, then $S_{4k} = 2S_k \geq 0$; since $k$ is odd, $S_k$ is odd as well, so we have $S_{4k} \geq 2$ and hence $S_{4k+1} = S_{4k} + x_{4k+1} \geq 1$.

Conversely, if $k$ is even, then we have $x_{4k+1} = x_{2k+1} = x_{k+1}$, hence $S_{4k+1} = S_{4k} + x_{4k+1} = 2S_k + x_{k+1} = S_k + S_{k+1} \geq 0$. The step is proved.