3.21 *fundamental theorem of linear maps*

Suppose $V$ is finite-dimensional and $T \in \mathcal{L}(V,W)$. Then range $T$ is finite-dimensional and

$$\dim V = \dim \operatorname{null} T + \dim \operatorname{range} T.$$

**Proof** Let $u_1, ..., u_m$ be a basis of null $T$; thus $\dim \operatorname{null} T = m$. The linearly independent list $u_1, ..., u_m$ can be extended to a basis

$$u_1, ..., u_m, v_1, ..., v_n$$

of $V$ (by 2.32). Thus $\dim V = m + n$. To complete the proof, we need to show that range $T$ is finite-dimensional and $\dim \operatorname{range} T = n$. We will do this by proving that $Tv_1, ..., Tv_n$ is a basis of range $T$.

Let $v \in V$. Because $u_1, ..., u_m, v_1, ..., v_n$ spans $V$, we can write

$$v = a_1 u_1 + \cdots + a_m u_m + b_1 v_1 + \cdots + b_n v_n,$$

where the $a$'s and $b$'s are in $\mathbf{F}$. Applying $T$ to both sides of this equation, we get

$$Tv = b_1 T v_1 + \cdots + b_n T v_n,$$

where the terms of the form $T u_k$ disappeared because each $u_k$ is in null $T$. The last equation implies that the list $Tv_1, ..., Tv_n$ spans range $T$. In particular, range $T$ is finite-dimensional.

To show $Tv_1, ..., Tv_n$ is linearly independent, suppose $c_1, ..., c_n \in \mathbf{F}$ and

$$c_1 T v_1 + \cdots + c_n T v_n = 0.$$

Then

$$T(c_1 v_1 + \cdots + c_n v_n) = 0.$$

Hence

$$c_1 v_1 + \cdots + c_n v_n \in \operatorname{null} T.$$

Because $u_1, ..., u_m$ spans null $T$, we can write

$$c_1 v_1 + \cdots + c_n v_n = d_1 u_1 + \cdots + d_m u_m,$$

where the $d$'s are in $\mathbf{F}$. This equation implies that all the $c$'s (and $d$'s) are 0 (because $u_1, ..., u_m, v_1, ..., v_n$ is linearly independent). Thus $Tv_1, ..., Tv_n$ is linearly independent and hence is a basis of range $T$, as desired.
