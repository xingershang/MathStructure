# Natural Language

The setting for the next result is the assumption that we have a basis $v_1, ..., v_n$ of $V$, along with its dual basis $\varphi_1, ..., \varphi_n$ of $V'$. We also have a basis $w_1, ..., w_m$ of $W$, along with its dual basis $\psi_1, ..., \psi_m$ of $W'$. Thus $\mathcal{M}(T)$ is computed with respect to the bases just mentioned of $V$ and $W$, and $\mathcal{M}(T')$ is computed with respect to the dual bases just mentioned of $W'$ and $V'$. Using these bases gives the following pretty result.

3.132 *matrix of $T'$ is transpose of matrix of $T$*

Suppose $V$ and $W$ are finite-dimensional and $T \in \mathcal{L}(V,W)$. Then

$$\mathcal{M}(T') = (\mathcal{M}(T))^{t}.$$

**Proof** Let $A = \mathcal{M}(T)$ and $C = \mathcal{M}(T')$. Suppose $1 \leq j \leq m$ and $1 \leq k \leq n$. From the definition of $\mathcal{M}(T')$ we have

$$T'(\psi_j) = \sum_{r=1}^n C_{r,j} \varphi_r.$$

The left side of the equation above equals $\psi_j \circ T$. Thus applying both sides of the equation above to $v_k$ gives

$$(\psi_j \circ T)(v_k) = \sum_{r=1}^n C_{r,j} \varphi_r(v_k) = C_{k,j}.$$

We also have

$$(\psi_j \circ T)(v_k) = \psi_j(T v_k) = \psi_j \left( \sum_{r=1}^m A_{r,k} w_r \right) = \sum_{r=1}^m A_{r,k} \psi_j(w_r) = A_{j,k}.$$

Comparing the last line of the last two sets of equations, we have $C_{k,j} = A_{j,k}$. Thus $C = A^{t}$. In other words, $\mathcal{M}(T') = (\mathcal{M}(T))^{t}$, as desired.


