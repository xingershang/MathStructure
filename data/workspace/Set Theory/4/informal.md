## Goal

$R \circ (S \cup T) = (R \circ S) \cup (R \circ T)$

## Proof

- Let $(x, z) \in R \circ (S \cup T)$. Then there exists $y$ such that $(x, y) \in R$ and $(y, z) \in S \cup T$. If $(y, z) \in S$, then $(x, z) \in R \circ S$; if $(y, z) \in T$, then $(x, z) \in R \circ T$. Thus, $(x, z) \in (R \circ S) \cup (R \circ T)$, so $R \circ (S \cup T) \subseteq (R \circ S) \cup (R \circ T)$.

- Conversely, let $(x, z) \in (R \circ S) \cup (R \circ T)$. If $(x, z) \in R \circ S$, there exists $y$ with $(x, y) \in R$ and $(y, z) \in S \subseteq S \cup T$, so $(x, z) \in R \circ (S \cup T)$. Similarly for $R \circ T$. Hence, $(R \circ S) \cup (R \circ T) \subseteq R \circ (S \cup T)$.

- Therefore, $R \circ (S \cup T) = (R \circ S) \cup (R \circ T)$.