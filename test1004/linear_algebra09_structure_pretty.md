[Hint] {3.132 matrix of T' is transpose of matrix of T}
[Fix] {$V$; $W$; $T$; $v_1, ..., v_n$; $\varphi_1, ..., \varphi_n$; $w_1, ..., w_m$; $\psi_1, ..., \psi_m$} such that {$V$ and $W$ are finite-dimensional vector spaces; $T \in \mathcal{L}(V,W)$; $v_1, ..., v_n$ is a basis of $V$; $\varphi_1, ..., \varphi_n$ is the dual basis of $v_1, ..., v_n$; $w_1, ..., w_m$ is a basis of $W$; $\psi_1, ..., \psi_m$ is the dual basis of $w_1, ..., w_m$}
{
    [Show] {$\mathcal{M}(T') = (\mathcal{M}(T))^{t}$}
    {
        [Define] {$A$} as {$A = \mathcal{M}(T)$}
        [Define] {$C$} as {$C = \mathcal{M}(T')$}
        [Fix] {$j$; $k$} such that {$1 \leq j \leq m$; $1 \leq k \leq n$}
        {
            [Have] {$T'(\psi_j) = \sum_{r=1}^n C_{r,j} \varphi_r$} by {the definition of $\mathcal{M}(T')$}
            [CalculationChain] {$(\psi_j \circ T)(v_k)$}
            [CalculationChain] {$(\psi_j \circ T)(v_k)$}
            [Have] {$C_{k,j} = A_{j,k}$} by {Comparing the last line of the last two sets of equations}
        }
        [Have] {$C = A^{t}$}
        [Have] {$\mathcal{M}(T') = (\mathcal{M}(T))^{t}$}
    }
}