**Theorem 4** (Schröder-Bernstein's Theorem). If $f: A \to B$ and $g: B \to A$ are both injections, then there is a bijection from $A$ into $B$.

**Proof.**

Suppose $f: A \to B, g: B \to A$ are injections. Let’s construct the bijection $h$ from $A$ into $B$.

$$
C_0 = \{ a \in A \mid \forall b \in B. \, g(b) \neq a \}
$$

$$
D_0 = \{ f(a) \mid a \in C_0 \}
$$

$$
C_1 = \{ a \in A \setminus C_0 \mid \forall b \in B \setminus D_0. \, g(b) \neq a \}. \, \text{We can prove that} \, C_1 = \{ g(b) \mid b \in D_0 \} \, \text{also}.
$$

$$
D_1 = \{ f(a) \mid a \in C_1 \}
$$

So that we can define

$$
C_{n+1} = \{ a \in A \setminus \bigcup_{i=0}^{n} C_i \mid \forall b \in B \setminus \bigcup_{i=0}^{n} D_i. \, g(b) \neq a \}
$$

$$
D_{n+1} = \{ f(a) \mid a \in C_{n+1} \}
$$

And similarly, we can prove that $C_{n+1} = \{ g(b) \mid b \in D_n \}$.

In the end, we can define

$$
h(a) := \begin{cases} 
f(a), & \text{if} \, a \in \bigcup_{i=0}^{\infty} C_i \\
b, \, \text{such that} \, g(b) = a, & \text{if} \, a \in A \setminus \bigcup_{i=0}^{\infty} C_i 
\end{cases}
$$

Obviously, the $f$ part is a bijection from $C_n$ into $D_n$.

So we just need to prove that the $g$ part is a bijection from $D := B \setminus \bigcup_{i=0}^{\infty} D_i$ into $C := A \setminus \bigcup_{i=0}^{\infty} C_i$.

Thus, it is suffice to prove: (1) $\forall d \in D. \, \exists c \in C. \, g(d) = c$ and (2) $\forall c \in C. \, \exists d \in D. \, g(d) = c$.

- $\forall d \in D. \exists c \in C. g(d) = c$.

  As $g$ is an injection from $B$ into $A$, $\exists c \in A, g(d) = c$.

  Let prove $c \notin C_n$.

  Suppose $c \in C_n$.

  - $n = 0$, Obviously contradiction.
  - $n = m + 1$, $c \in C_{m+1} \Rightarrow d \in D_m$, contradiction.

  Therefore, $c \in C$.

- $\forall c \in C. \exists d \in D. g(d) = c$.

  $\exists d \in B. g(d) = c$. Otherwise, $c \in C_0$, contradiction.

  Let’s prove $d \notin D_n$.

  Suppose $d \in D_n$, so that $c \in C_{n+1}$, contradiction.

  Therefore, $d \in D$.

Qed.
