## Comprehensive Examples

### Example 1: Cauchy Convergence Theorem

**(Reference)** As detailed in the "Accurate Node-Type Identification Principle" section, this proof is an excellent example of handling "Actions as Reasons", quantifier scoping (`Fix`, `Obtain`), and making logical clarifications explicit. Please refer back to its full text and structure as an important example to study.

### Example 2: Schröder-Bernstein's Theorem

**Natural language text:**
"""
**Theorem 4** (Schröder-Bernstein's Theorem). If $f: A \to B$ and $g: B \to A$ are both injections, then there is a bijection from $A$ into $B$.
**Proof.**
Suppose $f: A \to B, g: B \to A$ are injections. Let’s construct the bijection $h$ from $A$ into $B$.
$$C_0 = \{ a \in A \mid \forall b \in B. \, g(b) \neq a \}$$
$$D_0 = \{ f(a) \mid a \in C_0 \}$$
$$C_1 = \{ a \in A \setminus C_0 \mid \forall b \in B \setminus D_0. \, g(b) \neq a \}$$
We can prove that $C_1 = \{ g(b) \mid b \in D_0 \}$ also.
$$D_1 = \{ f(a) \mid a \in C_1 \}$$
So that we can define
$$C_{n+1} = \{ a \in A \setminus \bigcup_{i=0}^{n} C_i \mid \forall b \in B \setminus \bigcup_{i=0}^{n} D_i. \, g(b) \neq a \}$$
$$D_{n+1} = \{ f(a) \mid a \in C_{n+1} \}$$
And similarly, we can prove that $C_{n+1} = \{ g(b) \mid b \in D_n \}$.
In the end, we can define
$$h(a) := \begin{cases} 
f(a), & \text{if} \, a \in \bigcup_{i=0}^{\infty} C_i \\
b, \, \text{such that} \, g(b) = a, & \text{if} \, a \in A \setminus \bigcup_{i=0}^{\infty} C_i 
\end{cases}$$
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
"""

```json
[
    {
        "type": "Hint",
        "text": "Theorem 4 (Schröder-Bernstein's Theorem)"
    },
    {
        "type": "Fix",
        "variable": ["$A$", "$B$"],
        "condition": ["$A$, $B$ are sets"],
        "scope": [
            {
                "type": "Fix",
                "variable": ["$f$", "$g$"],
                "condition": ["$f: A \\to B$ is an injection", "$g: B \\to A$ is an injection"],
                "scope": [
                    {
                        "type": "Show",
                        "proposition": ["there is a bijection from $A$ into $B$"],
                        "method": null,
                        "scope": [
                            {
                                "type": "Define",
                                "term": "$C_0$",
                                "definition": "$C_0=\\{ a \\in A \\mid \\forall b \\in B, g(b) \\neq a \\}$"
                            },
                            {
                                "type": "Define",
                                "term": "$D_0$",
                                "definition": "$D_0=\\{ f(a) \\mid a \\in C_0 \\}$"
                            },
                            {
                                "type": "Define",
                                "term": "$C_1$",
                                "definition": "$C_1=\\{ a \\in A \\setminus C_0 \\mid \\forall b \\in B \\setminus D_0, g(b) \\neq a \\}$"
                            },
                            {
                                "type": "Have",
                                "claim": ["$C_1 = \\{ g(b) \\mid b \\in D_0 \\}$"],
                                "reason": null
                            },
                            {
                                "type": "Define",
                                "term": "$D_1$",
                                "definition": "$D_1=\\{ f(a) \\mid a \\in C_1 \\}$"
                            },
                            {
                                "type": "Define",
                                "term": "set sequence $\\{C_{n}\\}$",
                                "definition": "$\\forall n>1,C_{n+1}=\\{ a \\in A \\setminus \\bigcup_{i=0}^{n} C_i \\mid \\forall b \\in B \\setminus \\bigcup_{i=0}^{n} D_i, g(b) \\neq a \\}$"
                            },
                            {
                                "type": "Define",
                                "term": "set sequence $\\{D_{n}\\}$",
                                "definition": "$\\forall n>1,D_{n+1}=\\{ f(a) \\mid a \\in C_{n+1} \\}$"
                            },
                            {
                                "type": "Have",
                                "claim": ["$\\forall n \\in \\N, C_{n+1} = \\{ g(b) \\mid b \\in D_n \\}$"],
                                "reason": ["similarly"]
                            },
                            {
                                "type": "Define",
                                "term": "$h$",
                                "definition": "function $h: A \\to B$ such that for any $a \\in A$, $h(a) := \\begin{cases} f(a), & \\text{if } a \\in \\bigcup_{i=0}^{\\infty} C_i \\\\ b, \\text{ such that } g(b) = a, & \\text{if } a \\in A \\setminus \\bigcup_{i=0}^{\\infty} C_i \\end{cases}$"
                            },
                            {
                                "type": "Have",
                                "claim": ["$\\forall n$, the restriction of $f$ to $C_n$ is a bijection onto $D_n$"],
                                "reason": null
                            },
                            {
                                "type": "Define",
                                "term": "$C$",
                                "definition": "$A \\setminus \\bigcup_{i=0}^{\\infty} C_i$"
                            },
                            {
                                "type": "Define",
                                "term": "$D$",
                                "definition": "$B \\setminus \\bigcup_{i=0}^{\\infty} D_i$"
                            },
                            {
                                "type": "SufficesToProve",
                                "sufficient_proposition": [
                                    "$\\forall d \\in D, \\exists c \\in C, g(d) = c$",
                                    "$\\forall c \\in C, \\exists d \\in D, g(d) = c$"
                                ],
                                "reason": null
                            },
                            {
                                "type": "Show",
                                "proposition": ["$\\forall d \\in D, \\exists c \\in C, g(d) = c$"],
                                "method": null,
                                "scope": [
                                    {
                                        "type": "Fix",
                                        "variable": ["$d$"],
                                        "condition": ["$d \\in D$"],
                                        "scope": [
                                            {
                                                "type": "Obtain",
                                                "obtained_variable": ["$c$"],
                                                "condition": ["$c \\in A$", "$g(d) = c$"],
                                                "reason": ["$g$ is a function from $B$ into $A$"]
                                            },
                                            {
                                                "type": "Show",
                                                "proposition": ["$\\forall n, c \\notin C_n$"],
                                                "method": ["contradiction"],
                                                "scope": [
                                                    {
                                                        "type": "Fix",
                                                        "variable": ["$n$"],
                                                        "condition": ["$n \\in \\N$"],
                                                        "scope": [
                                                            {
                                                                "type": "Assume",
                                                                "assumption": ["$c \\in C_n$"],
                                                                "scope": [
                                                                    {
                                                                        "type": "Assume",
                                                                        "assumption": ["$n=0$"],
                                                                        "scope": [
                                                                            {
                                                                                "type": "Have",
                                                                                "claim": ["contradiction"],
                                                                                "reason": null
                                                                            }
                                                                        ]
                                                                    },
                                                                    {
                                                                        "type": "Assume",
                                                                        "assumption": ["$n=m+1$ for some $m \\in \\N$"],
                                                                        "scope": [
                                                                            {
                                                                                "type": "Have",
                                                                                "claim": ["$c \\in C_{m+1} \\implies d \\in D_m$"],
                                                                                "reason": null
                                                                            },
                                                                            {
                                                                                "type": "Have",
                                                                                "claim": ["contradiction"],
                                                                                "reason": null
                                                                            }
                                                                        ]
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "type": "Have",
                                                "claim": ["$c \\in C$"],
                                                "reason": null
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "type": "Show",
                                "proposition": ["$\\forall c \\in C, \\exists d \\in D, g(d) = c$"],
                                "method": null,
                                "scope": [
                                    {
                                        "type": "Fix",
                                        "variable": ["$c$"],
                                        "condition": ["$c \\in C$"],
                                        "scope": [
                                            {
                                                "type": "Obtain",
                                                "obtained_variable": ["$d$"],
                                                "condition": ["$d \\in B$", "$g(d) = c$"],
                                                "reason": ["otherwise $c \\in C_0$, contradiction"]
                                            },
                                            {
                                                "type": "Show",
                                                "proposition": ["$\\forall n, d \\notin D_n$"],
                                                "method": ["contradiction"],
                                                "scope": [
                                                    {
                                                        "type": "Fix",
                                                        "variable": ["$n$"],
                                                        "condition": ["$n \\in \\N$"],
                                                        "scope": [
                                                            {
                                                                "type": "Assume",
                                                                "assumption": ["$d \\in D_n$"],
                                                                "scope": [
                                                                    {
                                                                        "type": "Have",
                                                                        "claim": ["$c \\in C_{n+1}$"],
                                                                        "reason": null
                                                                    },
                                                                    {
                                                                        "type": "Have",
                                                                        "claim": ["contradiction"],
                                                                        "reason": null
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "type": "Have",
                                                "claim": ["$d \\in D$"],
                                                "reason": null
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        ]
    }
]
```