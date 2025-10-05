We now use the Compactness Theorem to obtain variants of the Löwenheim-Skolem Theorem.

**2.2 Theorem.** *Let $\Phi$ be a set of formulas which is satisfiable over arbitrarily large finite domains (i.e. for every $n \in \mathbb{N}$ there is an interpretation satisfying $\Phi$ over a finite domain which contains at least $n$ elements). Then $\Phi$ is also satisfiable over an infinite domain.*

*Proof.* Let  
$$\Psi := \Phi \cup \{\varphi_{\ge n} \mid 2 \le n\}$$  
($\varphi_{\ge n}$ was introduced in III.6.3). Every interpretation which satisfies $\Psi$ is a model of $\Phi$ and has an infinite domain. Therefore we need only prove that $\Psi$ is satisfiable. By the Compactness Theorem it is sufficient to show that every finite subset $\Psi_0$ of $\Psi$ is satisfiable. For each such $\Psi_0$ there is an $n_0 \in \mathbb{N}$ such that  
$$(*) \quad \Psi_0 \subseteq \Phi \cup \{\varphi_{\ge n} \mid 2 \le n \le n_0\}.$$  
According to the hypothesis of the theorem there is an interpretation $\mathfrak{I}$ which satisfies $\Phi$ and whose domain contains at least $n_0$ elements. By $(*)$, $\mathfrak{I}$ is also a model of $\Psi_0$.  
$\square$
