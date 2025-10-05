Prove there exists at least one “smallest inductive set” if there exists at least one inductive set. **Hint:** you can use the conclusions above.

Proof. Suppose there exists an inductive set $u$. Let

$$
N = \bigcap_{\substack{X \text{ is inductive}}} X.
$$

$N$ is indeed a set because $N \subseteq u$. We prove that $N$ is the smallest inductive set.  
For each inductive set $X$, $\varnothing \in X$. Thus $\varnothing \in N$. For each $x \in N$, $x \in X$ for all inductive set $X$, which implies that $x \cup \{x\} \in X$ for all inductive set $X$, which implies that $x \cup \{x\} \in N$. Hence $N$ is inductive. For any inductive set $X$, $X \subseteq N$ by definition. Hence $N$ is *the* smallest inductive set.