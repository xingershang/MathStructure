**Theorem**

Let ⟨$a_n(z)$⟩ and ⟨$b_n(z)$⟩ be sequences of complex functions on a compact set $K$. Let ⟨$a_n(z)$⟩ be such that:

- ⟨$a_n(z)$⟩ is bounded in $K$

- $\sum |a_n(z) - a_{n+1}(z)|$ is convergent with a sum which is bounded in $K$

- $\sum b_n(z)$ is uniformly convergent in $K$.

Then $\sum a_n(z) b_n(z)$ is uniformly convergent on $K$.

---

First we modify the statement of Abel's Lemma

**Lemma**

Suppose $\sum b_k$ converges. Let $B_k = b_k + b_{k+1} + b_{k+2} + \cdots$

Then:

$a_n b_n + \cdots + a_{n+k} b_{n+k} = B_n a_n + B_{n+1} (a_{n+1} - a_n) + \cdots + B_{n+k} (a_{n+k} - a_{n+k-1}) - B_{n+k+1} a_{n+k}$

**Proof of lemma**

$a_n b_n + \cdots + a_{n+k} b_{n+k} = a_n (B_n - B_{n+1}) + \cdots + a_{n+k} (B_{n+k} - B_{n+k+1})$

$= B_n a_n + B_{n+1} (a_{n+1} - a_n) + \cdots + B_{n+k} (a_{n+k} - a_{n+k-1}) - B_{n+k+1} a_{n+k}$

□

**Proof of theorem**

We show that $\sum_{j=n}^{n+k} a_j(z) b_j(z)$ is uniformly small if $n$ is large enough.

Using the notation of the lemma, since $B_n(z) \to 0$ uniformly, let $n$ be so large that $|B_N(z)| \leq \epsilon$ in $K$ for all $N \geq n$.

Since ⟨$a_n(z)$⟩ is uniformly bounded in $K$, let $|a_n(z)| \leq M$ for all $z \in K$.

Since $\sum |a_n(z) - a_{n+1}(z)|$ is convergent with a sum which is bounded in $K$, let $n$ be so large that:

$\forall k \in \mathbb{N} : |a_{n+1} - a_n| + \cdots + |a_{n+k} - a_{n+k-1}| \leq \epsilon$ for all $z \in K$

then we have:

$\forall z \in K : |B_{n+1} (a_{n+1} - a_n)| + \cdots + |B_{n+k} (a_{n+k} - a_{n+k-1})| \leq M \epsilon$

Therefore:

$|a_n b_n + \cdots + a_{n+k} b_{n+k}| = |B_n a_n + B_{n+1} (a_{n+1} - a_n) + \cdots + B_{n+k} (a_{n+k} - a_{n+k-1}) + B_{n+k+1} a_{n+k}|$ (Lemma)

$\leq |B_n a_n| + |B_{n+1} (a_{n+1} - a_n)| + \cdots + |B_{n+k} (a_{n+k} - a_{n+k-1})| + |B_{n+k+1} a_{n+k}|$ (Triangle Inequality for Complex Numbers)                            

$\leq M \epsilon + M \epsilon$

$= 3M \epsilon$

Therefore, $\sum a_n(z) b_n(z)$ is uniformly convergent on $K$. 

■
