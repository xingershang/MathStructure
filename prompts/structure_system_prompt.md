# The Structure of Mathematical Natural Language Texts

## Definition of Structure

### Node Types

The basic units of the structure of mathematical natural language are 11 different types of nodes:

#### 'Show' Node

- Semantics: "We will now prove proposition P, with hint Q".
- JSON:
```json
{
	"type": "Show",
	"proposition": [...],
	"method": [...]
}
```
- Explanation: The Show node corresponds to the overall proof goal, or subgoals in a proof text or in a problem solving text. Here, the hint Q is an indication for the proof method, for example 'induction'.

Example 1:
"Below we prove that the set $S$ is not empty and the set $T$ is not empty"

```json
{
	"type": "Show",
	"proposition": ["the set $S$ is not empty", "the set $T$ is not empty"],
	"method": null
}
```

Example 2:
"We use induction to prove $\forall n\in \N,f(n)\geq g(n)$ using theorem 3.1"

```json
{
	"type": "Show",
	"proposition": ["$\\forall n \\in \\N,f(n) \\geq g(n)$"],
	"method": ["induction", "theorem 3.1"]
}
```

Example 3:
"We show that $k\neq 0$. We prove by contradiction, ..."

```json
{
	"type": "Show",
	"proposition": ["$k \neq 0$"],
	"method": ["contradiction"]
}
```

#### 'Assume' Node

- Semantics: "Assume proposition P holds."
- JSON:
  ```json
  {
      "type": "Assume",
      "assumption": [...]
  }
  ```
- Explanation: 'Assume' nodes are used in the premises of the overall proof goal, or temporary assumptions introduced in the middle of the text, e.g. the conditions for each case in a "case analysis". (For situations that introduces new variables, although natural language might use the words "assume" or "let" or "suppose", it generally needs to be identified as a 'Fix' node, which will be introduced later(see Example 3). 'Assume' nodes only applies to situations that a assumption has been made, but NO NEW VARIABLES HAVE BEEN INTRODUCED in the text environment. Care must be taken to distinguish between Assume and Fix nodes!!!)

Example 1:
"Assume $a > 0$ and $a \in \mathbb{Q}$" (when $a$ has already been introduced above)

```json
{
    "type": "Assume",
    "assumption": ["$a > 0$", "$a \\in \\mathbb{Q}$"]
}
```

Example 2:
"Case 1: $n$ is even"

```json
{
    "type": "Assume",
    "assumption": ["$n$ is even"]
}
```

Example 3:
"Let $\varepsilon > 0$" ($\varepsilon$ is a newly introduced variable - This should be a Fix node.)

```json
{
    "type": "Fix",
    "variable": ["$\\varepsilon$"],
    "condition": ["$\\varepsilon > 0$"]
}
```

#### 'Fix' Node

- Semantics: "Fix a variable list `variables`, these variables satisfy proposition P."
- JSON:
  ```json
  {
      "type": "Fix",
      "variable": [...],
      "condition": [...]
  }
  ```
- Explanation: The Fix node introduces one or a list of new variables satisfying specific conditions. It corresponds to expressions in natural language like "for any ...", "for all ...", "given ...", "let ...", etc. Logically, it is equivalent to the universal quantifier (`∀`). Again, note the distinction between Fix and Assume nodes!

Example 1:
"For any $\varepsilon > 0$" ($\varepsilon$ is a newly introduced variable)

```json
{
    "type": "Fix",
    "variable": ["$\\varepsilon$"],
    "condition": ["$\\varepsilon > 0$"]
}
```

Example 2:
"Let $x, y$ be arbitrary real numbers"

```json
{
    "type": "Fix",
    "variable": ["$x$", "$y$"],
    "condition": ["$x, y$ are real numbers"]
}
```
(always use LaTeX expression to write variables)

Example 3:
"Let $x_1, ..., x_n$, $y_1, ..., y_n$ be arbitrary real numbers"

```json
{
    "type": "Fix",
    "variable": ["$x_1, ..., x_n$","$y_1, ..., y_n$"],
    "condition": ["$x_1, ..., x_n$, $y_1, ..., y_n$ are real numbers"]
}
```
(remark: when variables are written with '...', we put them in one string)

#### 'Have' Node

- Semantics: "claim P, the reasons for this assertion is Q."
- JSON:
  ```json
  {
      "type": "Have",
      "claim": [...],
      "reason": [...]
  }
  ```
- Explanation: A reason can be a theorem name, a previously proven conclusion(in natural language), or a natural language hint. If the original claim in the given text did not state a reason, then the "reason" should be empty.

Example 1:
"Therefore, $x>0$"

```json
{
    "type": "Have",
    "claim": ["$x>0$"],
    "reason": null
}
```

Example 2:
"By Lemma 1.2 and Lemma 1.3, $A$ is a closed set"

```json
{
    "type": "Have",
    "claim": ["$A$ is a closed set"],
    "reason": ["Lemma 1.2", "Lemma 1.3"]
}
```

#### 'Obtain' Node

- Semantics: "Claim the existence of the variable list `obtained_variable`, these variables satisfy the "condition", by "reason"."
- JSON:
  ```json
  {
      "type": "Obtain",
      "obtained_variable": [...],
      "condition": [...],
      "reason": [...]
  }
  ```
- Explanation: Logically, the Obtain node corresponds to the existential quantifier (`∃`); it asserts that variables satisfying specific properties exist. The `reason` part indicates the reason for the claim, similar to the 'Have' node.

Example 1:
"By the Mean Value Theorem, there exists $\xi \in (a,b)$ such that $f'(\xi)=0$"

```json
{
    "type": "Obtain",
    "obtained_variable": ["$\\xi$"],
    "condition": ["$\\xi \\in (a,b)$", "$f'(\\xi)=0$"],
    "reason": ["the Mean Value Theorem"]
}
```

Example 2:
"So there exists an integer $k$ such that $n=2k$"

```json
{
    "type": "Obtain",
    "obtained_variable": ["$k$"],
    "condition": ["$k$ is an integer", "$n=2k$"],
    "reason": null
}
```

Example 3:
"By the Bolzano-Weierstrass theorem, there exists a convergent subsequence in $\{x_n\}$: $\lim_{k \to \infty} x_{n_k} = \xi$."

```json
{
    "type": "Obtain",
    "obtained_variable": ["$\\{x_{n_k}\\}$", "$\\xi$"],
    "condition": ["$\\{x_{n_k}\\}$ is a subsequence of $\\{x_n\\}$", "$\\lim_{k \to \\infty} x_{n_k} = \\xi$"],
    "reason": ["Bolzano-Weierstrass theorem"]
}
```
In fact, "obtaining a subsequence" essentially means "obtaining a mapping $n:\mathbb{N}$ to $\mathbb{N}$". But sometimes it is difficult to extract the exact new variable we have newly obtained. Instead, we allow putting the full expression in "obtained_variable", and the introduction of this expression implicitly entails the introduction of a certain variable.

#### 'SufficesToProve' Node

- Semantics: "claim that to prove the current proof goal, it suffices to prove "sufficient_proposition", with the reason being "reason"."
- JSON:
  ```json
  {
      "type": "SufficesToProve",
      "sufficient_proposition": [...],
      "reason": [...]
  }
  ```
- Explanation: SufficesToProve is a transformation of the current proof goal during the proof process. The current proof goal could be the overall goal of the proof text or some subgoal, depending on the current context. It corresponds to natural language expressions like "it suffices to prove", "we only need to prove"...

Example 1:
"It suffices to prove $x \in A$ and $x \in B$"

```json
{
    "type": "SufficesToProve",
    "sufficient_proposition": ["$x \\in A$", "$x \\in B$"],
    "reason": null
}
```

Example 2:
"Since $A\subseteq B$, it suffices to prove $\forall x \in B, f(x)=0$"

```json
{
    "type": "SufficesToProve",
    "sufficient_proposition": ["$\\forall x \\in B, f(x)=0$"],
    "reason": ["$A \\subseteq B$"]
}
```

#### 'LogicChain' Node

- Semantics: "A logical derivation chain. The chain consists of an initial proposition and a sequence of steps, each with an operator, a resulting proposition, and an optional reason."
- JSON:
  ```json
  {
      "type": "LogicChain",
      "initial_proposition": [...],
      "step": [
          {
              "operator": "...",
              "proposition": [...],
              "reason": [...]
          },
          ...
      ]
  }
  ```
- Explanation: Used to represent long strings of logical derivations in natural language. If all symbols are forward implications (left implies right), then LogicChain is equivalent to a series of Have nodes. However, if the derivation involves backward implications, or a mix of forward, backward, and bidirectional implications, it is generally represented by a LogicChain node.

Example 1:
"$\begin{aligned}P_1&\iff P_2&(reason1) \\ &\implies P_3&(reason2)\\&\implies P_4\end{aligned}$"

```json
{
    "type": "LogicChain",
    "initial_proposition": ["$P_1$"],
    "step": [
        {
            "operator": "<=>",
            "proposition": ["$P_2$"],
            "reason": ["reason1"]
        },
        {
            "operator": "=>",
            "proposition": ["$P_3$"],
            "reason": ["reason2"]
        },
        {
            "operator": "=>",
            "proposition": ["$P_4$"],
            "reason": null
        }
    ]
}
```

Example 2:
"to have $|{x}_{n} - 1| < \varepsilon$, it suffices to have $\frac{1}{n + 1} < \varepsilon$, i.e., $n > \frac{1}{\varepsilon} - 1$."

```json
{
    "type": "LogicChain",
    "initial_proposition": ["$|{x}_{n} - 1| < \\varepsilon$"],
    "step": [
        {
            "operator": "⇐",
            "proposition": ["$\\frac{1}{n + 1} < \\varepsilon$"],
            "reason": null
        },
        {
            "operator": "⇔",
            "proposition": ["$n > \\frac{1}{\\varepsilon} - 1$"],
            "reason": null
        }
    ]
}
```

#### 'CalculationChain' Node

- Semantics: "Represents a calculation chain. The chain consists of an initial expression and a sequence of steps, each with an operator, a resulting expression, and an optional reason."
- JSON:
  ```json
  {
      "type": "CalculationChain",
      "initial_expression": [...],
      "step": [
          {
              "operator": "...",
              "expression": [...],
              "reason": [...]
          },
          ...
      ]
  }
  ```
- Explanation: Similar to LogicChain, CalculationChain is used to represent consecutive calculation steps, such as long chains of equalities or estimation processes.

Example 1:
"
$|a_n b_n + \cdots + a_{n+k} b_{n+k}| = |B_n a_n + B_{n+1} (a_{n+1} - a_n) + \cdots + B_{n+k} (a_{n+k} - a_{n+k-1}) + B_{n+k+1} a_{n+k}|$ (Lemma)
$\leq |B_n a_n| + |B_{n+1} (a_{n+1} - a_n)| + \cdots + |B_{n+k} (a_{n+k} - a_{n+k-1})| + |B_{n+k+1} a_{n+k}|$ (Triangle Inequality for Complex Numbers)
$\leq M \epsilon + M \epsilon$
$= 3M \epsilon$
"

```json
{
    "type": "CalculationChain",
    "initial_expression": ["$|a_n b_n + \\cdots + a_{n+k} b_{n+k}|$"],
    "step": [
        {
            "operator": "=",
            "expression": ["$|B_n a_n + B_{n+1} (a_{n+1} - a_n) + \\cdots + B_{n+k} (a_{n+k} - a_{n+k-1}) + B_{n+k+1} a_{n+k}|$"],
            "reason": ["Lemma"]
        },
        {
            "operator": "<=",
            "expression": ["$|B_n a_n| + |B_{n+1} (a_{n+1} - a_n)| + \\cdots + |B_{n+k} (a_{n+k} - a_{n+k-1})| + |B_{n+k+1} a_{n+k}|$"],
            "reason": ["Triangle Inequality for Complex Numbers"]
        },
        {
            "operator": "<=",
            "expression": ["$M \\epsilon + M \\epsilon$"],
            "reason": null
        },
        {
            "operator": "=",
            "expression": ["$3M \\epsilon$"],
            "reason": null
        }
    ]
}
```

#### 'Find' Node

- Semantics: "To find out(solve) the target, which satisfies certain condition(optional)"
- JSON:
  ```json
  {
      "type": "Find",
      "target": [...],
      "condition": [...]
  }
  ```
- Explanation: The Find node is used to represent a "problem-solving" task. For example, tasks like "compute the value of ...", "simplify the expression", "solve the equation ...", or "find all sets satisfying ...". Its purpose is not to "prove" a proposition, but to "find" an object satisfying specific conditions. **The target can be variables or expressions. For tasks like simplification or evaluating an expression, "condition" should be empty.** 

Example 1:
"Find the solutions to the equation $x^2 -3x+ 4 = 0$"

```json
{
    "type": "Find",
    "target": ["$x$"],
    "condition": ["$x^2 - 3x + 4 = 0$"]
}
```

Example 2:
"Now we compute the integral $\int_0^1 x dx$"

```json
{
    "type": "Find",
    "target": ["$\\int_0^1 x dx$"],
    "condition": null
}
```

#### 'Define' Node

- Semantics: "Define a 'variable/symbol/concept' "term", whose meaning is "definition"."
- JSON:
  ```json
  {
      "type": "Define",
      "term": "...",
      "definition": "..."
  }
  ```
- Explanation: Used to define new variables, symbols, or concepts.

Example 1:
"Let $M = \sup_{x \in S} f(x)$"

```json
{
    "type": "Define",
    "term": "$M$",
    "definition": "$M = \\sup_{x \\in S} f(x)$"
}
```

Example 2:
"We call $G$ an Abelian group if $G$ is a group and its operation is commutative"

```json
{
    "type": "Define",
    "term": "Abelian group",
    "definition": "$G$ is an Abelian group if $G$ is a group and its operation is commutative"
}
```

#### 'Hint' Node

- Semantics: "a natural language annotation."
- JSON:
  ```json
  {
      "type": "Hint",
      "text": "..."
  }
  ```
- Explanation: Natural language texts often contain explanatory, annotative text that **does not have specific mathematical meaning**. For example, transitional text, author's comments, emphasis on the importance of a conclusion, or an intuitive overview of the upcoming proof steps or calculation steps.

Example 1:
"Thus we can obtain the answer"

```json
{
    "type": "Hint",
    "text": "Thus we can obtain the answer"
}
```

Example 2:
"The idea of this proof is very clever"

```json
{
    "type": "Hint",
    "text": "The idea of this proof is very clever"
}
```

Example 3:
"Next we use a skillful technique to prove this conclusion; a more natural proof method will be introduced in Chapter 4"

```json
{
    "type": "Hint",
    "text": "Next we use a skillful technique to prove this conclusion; a more natural proof method will be introduced in Chapter 4"
}
```

### Scope

Now we define the scope of a node.

Only four types of node have a scope: 'Show', 'Assume', 'Fix', and 'Find'. Other types of nodes do not.

In the scope of a node is another structure defined exactly the same as the outer structure. Hnece, a structure is a nested multi-level node sequences.

The content within the scope of these four nodes is generally:

- Show: The scope of a Show node contains the proof for that proof goal;
- Assume: The scope of an Assume node corresponds to the text content that acknowledges the assumption holds;
- Fix: The scope of a Fix node contains text content about the newly introduced variables;
- Find: The scope of a Find node is the specific process of finding or solving;

## How to Extract Structure

Given a piece of natural language text, due to the ambiguity of natural language, we cannot use a precise algorithm to extract the corresponding structure. We cannot precisely define whether a structure is the correct corresponding structure or not, either. However, we can summarize some key characteristics of a "good corresponding structure" as follows:

- Information Equivalency Principle
- No Free Variables Principle
- Concrete-Reference Principle
- Accurate Node-Type Identification Principle
- Accurate Scoping Principle
- Logical Clarification Principle

### Information Equivalency Principle

The structure should exactly preserve the information of the natural language text. It should not omit given information, nor should it arbitrarily add redundant information.

There are two basic principles:

- **DO NOT** add or omit "reasoning steps" or "reasons for the claim"
- **DO** add type or domain for the variables
- **DO NOT** try to correct a wrong proof

#### Example 1

**Natural language text**
"Since $(x-1)(x-3)=0$, we have $x=1$ or $x=3$."

**Structure with information equivalency**
```json
{
    "type": "Have",
    "claim": ["$x=1$ or $x=3$"],
    "reason": ["$(x-1)(x-3)=0$"]
}
```

**Structure with redundant information**
```json
{
    "type": "Have",
    "claim": ["$x-1=0$ or $x-3=0$"],
    "reason": ["$(x-1)(x-3)=0$"]
},
{
    "type": "Have",
    "claim": ["$x=1$ or $x=3$"],
    "reason": null
}
```

In this example, even though the middle reasoning step "$x-1=0$ or $x-3=0$" is correct, but this information was imagined by the reader and was not presented in the original text, it should not be arbitrarily added during structure extraction.

#### Example 2

**Natural language text**
"Therefore, $X \in \mathcal{P}(B)$."

**Structure with information equivalency**
```json
{
    "type": "Have",
    "claim": ["$X \\in \\mathcal{P}(B)$"],
    "reason": null
}
```

**Structure with redundant information**
```json
{
    "type": "Have",
    "claim": ["$X \\in \\mathcal{P}(B)$"],
    "reason": ["definition of power set"]
}
```

In this example, even though "by the definition of power set" is indeed the reason for deriving $X \\in \\mathcal{P}(B)$, since this information is inferred by the reader and is not present in the original text, it should not be arbitrarily added during structure extraction.

#### Example 3

**Natural language text**
"By definition of power set, $X \subseteq A$."

**Structure with information equivalency**
```json
{
    "type": "Have",
    "claim": ["$X \\subseteq A$"],
    "reason": ["definition of power set"]
}
```

**Structure with omitted information**
```json
{
    "type": "Have",
    "claim": ["$X \\subseteq A$"],
    "reason": null
}
```

In this example, since the original text has given the hint information "definition of power set", we should preserve this piece of information.

#### Example 4

**Natural language text**
"""
$A \times \bigcup B = \bigcup \{A \times X \mid X \in B\}$

($\subseteq$): Let $(a, x) \in A \times \bigcup B$. By definition, $x \in \bigcup B$, so there exists $X \in B$ such that $x \in X$. Therefore, $(a, x) \in A \times X$. Since $A \times X$ is part of the union $\bigcup \{A \times X \mid X \in B\}$, we conclude $(a, x) \in \bigcup \{A \times X \mid X \in B\}$.

($\supseteq$): Let $(a, x) \in \bigcup \{A \times X \mid X \in B\}$. Then there exists $X \in B$ such that $(a, x) \in A \times X$. By definition of Cartesian product, $a \in A$ and $x \in X$. Since $X \in B$, we have $x \in \bigcup B$. Thus, $(a, x) \in A \times \bigcup B$.

Hence, $A \times \bigcup B = \bigcup \{A \times X \mid X \in B\}$.
"""

**Structure with information equivalency**
```json
{
  "structure": [
    {
      "type": "Fix",
      "variable": ["$A$","$B$"],
      "condition": ["$A$,$B$ are sets"],
      "scope": [
        {
          "type": "Show",
          "proposition": ["$A \\times \\bigcup B = \\bigcup \\{A \\times X \\mid X \\in B\\}$"],
          "method": null,
          "scope": [
            {
              "type": "Show",
              "proposition": ["$A \\times \\bigcup B \\subseteq \\bigcup \\{A \\times X \\mid X \\in B\\}$"],
              "method": null,
              "scope": [
                {
                  "type": "Fix",
                  "variable": ["$a$","$x$"],
                  "condition": ["$(a, x) \\in A \\times \\bigcup B$"],
                  "scope": [
                    {
                      "type": "Have",
                      "claim": ["$x \\in \\bigcup B$"],
                      "reason": ["definition"]
                    },
                    {
                      "type": "Obtain",
                      "obtained_variable": ["$X$"],
                      "condition": ["$X \\in B$", "$x \\in X$"],
                      "reason": null
                    },
                    {
                      "type": "Have",
                      "claim": ["$(a, x) \\in A \\times X$"],
                      "reason": null
                    },
                    {
                      "type": "Have",
                      "claim": ["$(a, x) \\in \\bigcup \\{A \\times X \\mid X \\in B\\}$"],
                      "reason": ["$A \\times X$ is part of the union $\\bigcup \\{A \\times X \\mid X \\in B\\}$"]
                    }
                  ]
                }
              ]
            },
            {
              "type": "Show",
              "proposition": ["$\\bigcup \\{A \\times X \\mid X \\in B\\} \\subseteq A \\times \\bigcup B$"],
              "method": null,
              "scope": [
                {
                  "type": "Fix",
                  "variable": ["$a$", "$x$"],
                  "condition": ["$(a, x) \\in \\bigcup \\{A \\times X \\mid X \\in B\\}$"],
                  "scope": [
                    {
                      "type": "Obtain",
                      "obtained_variable": ["$X$"],
                      "condition": ["$X \\in B$", "$(a, x) \\in A \\times X$"],
                      "reason": null
                    },
                    {
                      "type": "Have",
                      "claim": ["$a \\in A$", "$x \\in X$"],
                      "reason": ["definition of Cartesian product"]
                    },
                    {
                      "type": "Have",
                      "claim": ["$x \\in \\bigcup B$"],
                      "reason": ["$X \\in B$"]
                    },
                    {
                      "type": "Have",
                      "claim": ["$(a, x) \\in A \\times \\bigcup B$"],
                      "reason": null
                    }
                  ]
                }
              ]
            },
            {
              "type": "Have",
              "claim": ["$A \\times \\bigcup B = \\bigcup \\{A \\times X \\mid X \\in B\\}$"],
              "reason": null
            }
          ]
        }
      ]
    }
  ]
}
```

In this example, despite that in the original text, there's no written out information about "$A$,$B$ are sets", but the correct structure extraction should clarify this condition. We should always clarify the type/domain of the newly introduced variables (when we can).

We should keep in mind that "do not add redundant information" does not mean "only copy the original text"! The type/domain of a variable is not redundant information, it is a piece of information that the natural language "attempts to convey", but did not "write out".

#### Example 5

**Natural language text**
"""
A, B are sets. Proof that if $A \subseteq B$, $\mathcal{P}(A) \subseteq \mathcal{P}(B)$.
Let $n,m$ be integers. Let $A = \{a_1, a_2, \dots, a_n\}$, $B = \{b_1, b_2, \dots, b_m\}$. Since $A \subseteq B$, we have $n \leq m$. $\forall i \in [n], \exists j \in [m] s.t. a_i=b_j$. Hence $\mathcal{P}(A) \subseteq \mathcal{P}(B)$.
"""

**Structure with information equivalency**
```json
{
  "structure": [
    {
      "type": "Fix",
      "variable": ["$A$","$B$"],
      "condition": ["$A, B$ are sets","$A \\subseteq B$"],
      "scope": [
        {
          "type": "Show",
          "proposition": ["$A \\subseteq B \\implies \\mathcal{P}(A) \\subseteq \\mathcal{P}(B)$"],
          "method": null,
          "scope": [
            {
              "type": "Fix",
              "variable": ["$n$","$m$"],
              "condition": ["$n,m$ are integers"],
              "scope": [
                {
                  "type": "Fix",
                  "variable": ["$a_1, ..., a_n$","$b_1, ..., b_m$"],
                  "condition": ["$A = \\{a_1, a_2, \\dots, a_n\\}$","$B = \\{b_1, b_2, \\dots, b_m\\}$"],
                  "scope": [
                    {
                      "type": "Have",
                      "claim": ["$n \\leq m$"],
                      "reason": ["$A \\subseteq B$"]
                    },
                    {
                      "type": "Have",
                      "claim": ["$\\forall i \\in [n], \\exists j \\in [m] s.t. a_i=b_j$"],
                      "reason": null
                    }
                  ]
                }
              ]
            },
            {
              "type": "Have",
              "claim": ["$\\mathcal{P}(A) \\subseteq \\mathcal{P}(B)$"],
              "reason": null
            }
          ]
        }
      ]
    }
  ]
}
```

While this proof is complete wrong(because $A,B$ are not necessarily finite sets), we should still extract the structure in the way of the original text, instead of modifying it into a correct proof.

### No Free Variables Principle

A logically sound mathematical text does not contain variables that appear without being properly "introduced". In formal logic, such variables are called "free variables". We apply this concept to our structure extraction and establish a fundamental principle for a "good structure": the No Free Variables Principle.

For a single natural language proposition, the definition is as follows (which is identical to the definition in formal logic):

- A proposition of the form "for all x, P" contains the free variables of P, **minus the variable x**.
- A proposition of the form "there exists x, P" contains the free variables of P, **minus the variable x**.
- A "temporary variable" used as a binder in a proposition is NOT considered as a free variable.

The free variables for each node type are defined as follows:

- Show(proposition, method, scope): The free variables are the union of the free variables from the `proposition` and the `scope`. The `method` field is a hint and its variables are not considered.
- Assume(assumption, scope): The free variables are the union of the free variables from the `assumption` and the `scope`.
- Have(claim, reason): The free variables are those from the `claim` proposition. The `reason` field is a hint and its variables are not considered.
- SufficesToProve(sufficient_proposition, reason): The free variables are those from the `sufficient_proposition`. The `reason` field is a hint and its variables are not considered.
- LogicChain: The free variables are the union of the free variables from the propositions in each step.
- CalculationChain: The free variables are the union of the free variables from the expressions in each step.
- Hint: Contains no free variables.

(Pay special attention to the definitions for the following variable-binding nodes)

- Fix(variable, condition, scope): The free variables are the free variables of the `scope` and `condition`, **with the variables in the `variable` list removed from both**.
- Obtain(obtained_variable, condition, reason): The free variables of the `Obtain` node itself are the free variables of the `condition` proposition, **with the `obtained_variable` list removed**; Furthermore, the `obtained_variable`s are considered **not free** for all **subsequent nodes within the same scope** as the `Obtain` node. (As always, the `reason` field is a hint and its variables are not considered.)
- Find(target, condition, scope): The free variables are the free variables of the `scope` and `condition`, **with the variables in the `target` list removed from both**.
- Define(term, definition): The free variables of the `Define` node itself are the free variables of the `definition`, **with the `term` removed**. Furthermore, the `term` is considered **not free** for all **subsequent nodes within the same scope** as the `Define` node.

The No Free Variables Principle: A good structure must have no free variables **overall at the top level.**

#### Example 1

```json
{
    "type": "Have",
    "claim": ["$\\forall x, x^2 > 0$"],
    "reason": ["$x$'s square is non-negative"]
}
```

This node does not violate the No Free Variables Principle. The proposition "`$\forall x, x^2 > 0$`" contains no free variables because `x` is bound by the quantifier `$\forall$`. The variable `x` appearing in the `reason` field is not considered a formal mathematical free variable under this principle.

#### Example 2

**Natural language text:** (Assume the variables for the sequence `$x_n$` and the limit `$a$` have been introduced by an outer scope)
"""
By definition, for any $\varepsilon > 0$, there exists $N$ such that for all $n, m > N$: $|x_n - a| < \frac{\varepsilon}{2}, \quad |x_m - a| < \frac{\varepsilon}{2}$. Thus, $|x_n - x_m| \leq |x_n - a| + |x_m - a| < \varepsilon$.
"""

**Structure 1**
```json
[
    {
        "type": "Have",
        "claim": ["for any $\\varepsilon > 0$, there exists $N$ such that for all $n, m > N$: $|x_n - a| < \\frac{\\varepsilon}{2}, \\quad |x_m - a| < \\frac{\\varepsilon}{2}$"],
        "reason": ["definition"]
    },
    {
        "type": "Have",
        "claim": ["$|x_n - x_m| \\leq |x_n - a| + |x_m - a| < \\varepsilon$"],
        "reason": null
    }
]
```
This structure violates the No Free Variables principle. The first `Have` node is valid because the natural language quantifiers ("for any", "there exists") bind the variables `$\varepsilon, N, n, m$` within that proposition. However, in the second `Have` node, the variables `$\varepsilon, n, m$` are all free variables, as they have not been introduced into its scope.

**Structure 2**
```json
[
    {
        "type": "Have",
        "claim": ["for any $\\varepsilon > 0$, there exists $N$ such that for all $n, m > N$: $|x_n - a| < \\frac{\\varepsilon}{2}, \\quad |x_m - a| < \\frac{\\varepsilon}{2}$"],
        "reason": ["definition"]
    },
    {
        "type": "Have",
        "claim": ["for any $\\varepsilon > 0$, there exists $N$ such that for all $n, m > N$: $|x_n - x_m| \\leq |x_n - a| + |x_m - a| < \\varepsilon$"],
        "reason": null
    }
]
```
This structure does not violates the No Free Variables principle. By repeating the quantifiers from the first node, the variables in the second `Have` node are properly bound, eliminating the free variables.

**Structure 3**
```json
{
    "type": "Fix",
    "variable": ["$\\varepsilon$"],
    "condition": ["$\\varepsilon>0$"],
    "scope": [
        {
            "type": "Obtain",
            "obtained_variable": ["$N$"],
            "condition": ["$\\forall n, m > N, |x_n - a| < \\frac{\\varepsilon}{2} \\text{ and } |x_m - a| < \\frac{\\varepsilon}{2}$"],
            "reason": ["definition"]
        },
        {
            "type": "Fix",
            "variable": ["$n$", "$m$"],
            "condition": ["$n>N$", "$m>N$"],
            "scope": [
                {
                    "type": "Have",
                    "claim": ["$|x_n - x_m| \\leq |x_n - a| + |x_m - a| < \\varepsilon$"],
                    "reason": null
                }
            ]
        }
    ]
}
```
This structure also does not violates the No Free Variables principle. Compared to Structure 2, it achieves the goal of eliminating free variables by breaking down the natural language quantifiers into `Fix` and `Obtain` nodes.
While both Structure 2 and Structure 3 does not violates the No Free Variables principle, **Structure 3 is generally preferred**. The reason for this preference will be detailed in the upcoming "Accurate Scoping Principle".

#### Example 3

**Natural language text:**
"When $n = 1$, $1 + 2 + \cdots + n = \frac{n(n + 1)}{2}$ holds"

**Correct Structure**
```json
{
	"type": "Have",
	"claim": ["When $n = 1$, $1 + 2 + \\cdots + n = \\frac{n(n + 1)}{2}$ holds"],
	"reason": null
}
```

In this example, although there's no expressions like "forall" or "exists" in the natural language text, but we know that $n$ is just a binder, used as a temporary variable, not a free variable.

### Concrete-Reference Principle

Propositions and hints in natural language often contain **abstract references**. For example, phrases like "this fact", "that equation", "those theorems", etc. Mathematical texts might also label propositions or expressions with numbers, such as $f(x)=0\quad (1)$ and $g(x)=1\quad (2)$, and then refer to these labels, for instance, "Combining (1) and (2), we get...".

We refer to these phenomena as **"abstract references"**. A good structure must resolve these abstract references into **concrete references**. We call this the Concrete-Reference Principle.

#### Example 1

**Natural language text:**
```
...
Hence we have $\forall x \in \R, f(x)=g(-x)$.
By the above equation, we have $f(1)=g(-1)$.
...
```

**Correct Structure:**
```json
[
  {
    "type": "Have",
    "claim": ["$\\forall x \\in \\R, f(x)=g(-x)$"],
    "reason": null
  },
  {
    "type": "Have",
    "claim": ["$f(1)=g(-1)$"],
    "reason": ["$\\forall x \\in \\R, f(x)=g(-x)$"]
  }
]
```

In this example, the abstract reference "the above equation" has been replaced with the concrete mathematical expression it refers to: "$\\forall x \in \\R, f(x)=g(-x)$".

#### Example 2

**Natural language text:**
```
$1 + 2 + \cdots + n = \frac{n(n + 1)}{2}$.
Proof: 
We prove by mathematical induction. 
When $n = 1$, the equality holds.
...
```

**Correct Structure:**
```json
{
    "type": "Show",
    "proposition": ["$\\forall n \\in \\N^*, 1 + 2 + \\cdots + n = \\frac{n(n + 1)}{2}$"],
    "method": ["mathematical induction"],
    "scope": [
        {
			"type": "Have",
			"claim": ["When $n = 1$, the equality $1 + 2 + \\cdots + n = \\frac{n(n + 1)}{2}$ holds"],
			"reason": null
        },
		...
    ]
}
```

In this example, the abstract reference "the equality" is replaced with the concrete equation it refers to: "$1 + 2 + \cdots + n = \frac{n(n + 1)}{2}$".

Note two other important points in this example:

1.  We added the quantifier `$\forall n \in \N^*$` to the main proof goal to eliminate the free variable `n`, following the **No Free Variables Principle**.
2.  We did **not** simplify the statement "When $n = 1$, the equality holds" by substituting `n=1` to get `$1=1$` or `$1=\frac{1\times 2}{2}$`. Instead, we preserved the original phrasing while resolving the reference. This follows the **Information Equivalency Principle**, as we do not add unstated simplification steps. In many cases, substitution might not be trivial, so we must not add information that wasn't explicitly written.

#### Example 3

**Natural language text:**
```
$f(x)=0\quad (1)$
$g(x)=1\quad (2)$
...
Combining equations (1) and (2), we get $f(x)+g(x)=1$.
...
```

**Correct Structure:**
```json
[
    {
        "type": "Have",
        "claim": ["$f(x)=0$"],
        "reason": null
    },
    {
        "type": "Have",
        "claim": ["$g(x)=1$"],
        "reason": null
    },
	...
    {
        "type": "Have",
        "claim": ["$f(x)+g(x)=1$"],
        "reason": ["By combining the equations $f(x)=0$ and $g(x)=1$"]
    },
	...
]
```

For references to numbered labels, we handle them as follows: in the nodes that assert the original propositions (`$f(x)=0$`), we do not store the labels `(1)` and `(2)`. When these labels are later referenced in a reason, we replace the reference with the full proposition that the label points to.

### Accurate Node-Type Identification Principle

A good structure must correctly identify the node type for each node.

In most cases, determining the node type is straightforward by literal interpretation. For example, if the natural language says "Now we prove...", it corresponds to a `Show` node; if it says "It suffices to prove...", it corresponds to a `SufficesToProve` node.

However, identifying the node type can be very error-prone when dealing with natural language "Actions", which cannot be judged literally. A good structure must correctly identify the node type corresponding to these "Actions". This is explained in detail below:

In natural language, sentences like "Let $a > 0$", "When $a > 0$", "Let $a=1$", or "Let $a=b$" can correspond to an `Assume` node, a `Fix` node, a `Define` node, or they might not correspond to a standalone node at all but rather be part of a hint or reason. The correct choice depends on the context. Generally:

  * If **`a` is a newly introduced variable** and the subsequent text discusses arguments under a certain condition on `a` (e.g., $a>0$), use a **`Fix`** node.
  * If **`a` is a pre-existing variable** and the text is making a deduction under a new, temporary condition (common in case analysis), use an **`Assume`** node.
  * If **`a` is a newly introduced variable** that is assigned a specific, determined value, use a **`Define`** node.
  * If the action performed on `a` has no independent logical significance and serves only as a **hint for how a conclusion is reached**, include the action as part of the **`reason`** field in the relevant node.

#### Example 1

**Natural language text:**
"""
$\lim_{n \to \infty} \sqrt[n]{a} = 1$ (for $a>0$)
**Proof:** 
(1) When $a = 1$, the equality obviously holds. 
(2) When $a > 1$, for any $\varepsilon>0$, let $N = \left\lceil \frac{a - 1}{\varepsilon} \right\rceil$, then for any $n > N$, we have $|\sqrt[n]{a} - 1| < \varepsilon$, which implies $\lim_{n \to \infty} \sqrt[n]{a} = 1$. 
(3) When $0 < a < 1$, let $a' = \frac{1}{a}$. Then $a' > 1$. Then, as $n \to \infty$, $\sqrt[n]{a} = \frac{1}{\sqrt[n]{a'}} \to 1$. 
"""

In this example, the entire proof is for a fixed positive real number `a`, so a `Fix` node is used at the outermost level. Within the scope of the main `Show` node, a case analysis is performed based on the range of `a`. Each case makes an assumption about the pre-existing variable `a`, so `Assume` nodes are used for each case. "let $N = \left\lceil \frac{a - 1}{\varepsilon} \right\rceil$" and "let $a' = \frac{1}{a}$" both introduce new variables with specific values, so `Define` nodes are used. "for any $\varepsilon>0$" and "for any $n > N$" both introduce new variables under certain conditions for further discussion, corresponding to `Fix` nodes.

**Correct Structure:**
```json
{
    "type": "Fix",
    "variable": ["$a$"],
    "condition": ["$a > 0$"],
    "scope": [
        {
            "type": "Show",
            "proposition": ["$\\lim_{n \\to \\infty} \\sqrt[n]{a} = 1$"],
            "method": null,
            "scope": [
                {
                    "type": "Assume",
                    "assumption": ["$a = 1$"],
                    "scope": [
                        {
                            "type": "Have",
                            "claim": ["$\\lim_{n \\to \\infty} \\sqrt[n]{a} = 1$"],
                            "reason": null
                        }
                    ]
                },
                {
                    "type": "Assume",
                    "assumption": ["$a > 1$"],
                    "scope": [
                        {
                            "type": "Fix",
                            "variable": ["$\\varepsilon$"],
                            "condition": ["$\\varepsilon > 0$"],
                            "scope": [
                                {
                                    "type": "Define",
                                    "term": "$N$",
                                    "definition": "$N = \\lceil \\frac{a - 1}{\\varepsilon} \\rceil$"
                                },
                                {
                                    "type": "Fix",
                                    "variable": ["$n$"],
                                    "condition": ["$n > N$"],
                                    "scope": [
                                        {
                                            "type": "Have",
                                            "claim": ["$|\\sqrt[n]{a} - 1| < \\varepsilon$"],
                                            "reason": null
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "type": "Have",
                            "claim": ["$\\lim_{n \\to \\infty} \\sqrt[n]{a} = 1$"],
                            "reason": null
                        }
                    ]
                },
                {
                    "type": "Assume",
                    "assumption": ["$0 < a < 1$"],
                    "scope": [
                        {
                            "type": "Define",
                            "term": "$a'$",
                            "definition": "$a' = \\frac{1}{a}$"
                        },
                        {
                            "type": "Have",
                            "claim": ["$a' > 1$"],
                            "reason": null
                        },
                        {
                            "type": "Have",
                            "claim": ["as $n \\to \\infty$, $\\sqrt[n]{a} = \\frac{1}{\\sqrt[n]{a'}} \\to 1$"],
                            "reason": null
                        }
                    ]
                }
            ]
        }
    ]
}
```

#### Example 2

**Natural language text:**
"""
Let ${x}_{n} = \frac{n}{n + 1} \quad (n = 1,2,\cdots)$. Prove: $\lim_{n \to \infty} {x}_{n} = 1$.
Proof: 
$|{x}_{n} - 1| = \frac{1}{n + 1}$. 
For any $\varepsilon > 0$, to have $|{x}_{n} - 1| < \varepsilon$, it suffices to have $\frac{1}{n + 1} < \varepsilon$, i.e., $n > \frac{1}{\varepsilon} - 1$. 
We may take $N = N(\varepsilon) = \left\lfloor \frac{1}{\varepsilon} \right\rfloor$. Then when $n > N$, $|{x}_{n} - 1| < \varepsilon$. 
Therefore, $\lim_{n \to \infty} {x}_{n} = 1$.
"""

In this example, "Let $x_n=\frac{n}{n+1}$" defines the sequence $x$ at the outermost level, so a `Define` node is used. (it is also logically correct to use a `Fix` node for $x$ satisfying $\forall n\in \N^*, {x}_{n} = \frac{n}{n + 1}$ and place the rest of the proof in its scope.)

The phrase "to have..., it suffices to have..., i.e., ..." represents a logical derivation mixing sufficient conditions and equivalences. We use a `LogicChain` node to represent this. To eliminate the free variable $n$ in this chain, we wrap the `LogicChain` node within a `Fix` node for $n$.

The text "We may take $N = N(\varepsilon) = \left\lfloor \frac{1}{\varepsilon} \right\rfloor$" explicitly notes that $N$ is a function of $\varepsilon$. Since we can place the `Define` node for $N$ inside the scope of $\varepsilon$, this dependency is correctly captured, making the logic sound whether $N$ is considered a function or a value.

**Correct Structure:**
```json
[
    {
        "type": "Define",
        "term": "$x$",
        "definition": "$\\forall n\\in \\N^*, {x}_{n} = \\frac{n}{n + 1}$"
    },
    {
        "type": "Show",
        "proposition": ["$\\lim_{n \\to \\infty} {x}_{n} = 1$"],
        "method": null,
        "scope": [
            {
                "type": "Have",
                "claim": ["$\\forall n \\in \\N^*, |{x}_{n} - 1| = \\frac{1}{n + 1}$"],
                "reason": null
            },
            {
                "type": "Fix",
                "variable": ["$\\varepsilon$"],
                "condition": ["$\\varepsilon>0$"],
                "scope": [
                    {
                        "type": "Fix",
                        "variable": ["$n$"],
                        "condition": ["$n \\in \\N^*$"],
                        "scope": [
                            {
                                "type": "LogicChain",
                                "initial_proposition": ["$|{x}_{n} - 1| < \\varepsilon$"],
                                "steps": [
                                    {
                                        "operator": "⇐",
                                        "proposition": ["$\\frac{1}{n + 1} < \\varepsilon$"],
                                        "reason": null
                                    },
                                    {
                                        "operator": "⇔",
                                        "proposition": ["$n > \\frac{1}{\\varepsilon} - 1$"],
                                        "reason": null
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "Define",
                        "term": "$N$",
                        "definition": "$N=\\lfloor \\frac{1}{\\varepsilon} \\rfloor$"
                    },
                    {
                        "type": "Have",
                        "claim": ["$\\forall n > N, |{x}_{n} - 1| < \\varepsilon$"],
                        "reason": null
                    }
                ]
            },
            {
                "type": "Have",
                "claim": ["$\\lim_{n \\to \\infty} {x}_{n} = 1$"],
                "reason": null
            }
        ]
    }
]
```

#### Example 3

**Natural language text:**
"""
Theorem 2.4.7 (Cauchy Convergence): A sequence $\{x_n\}$ converges if and only if $\{x_n\}$ is a Cauchy sequence.

Proof: First, we prove the necessity.
Assume $\{x_n\}$ converges to $a$.
By definition, for any $\varepsilon > 0$, there exists $N$ such that for all $n, m > N$: $|x_n - a| < \frac{\varepsilon}{2}, \quad |x_m - a| < \frac{\varepsilon}{2}$.
Thus, $|x_n - x_m| \leq |x_n - a| + |x_m - a| < \varepsilon$.

Next, we prove the sufficiency.
First, we show that a Cauchy sequence must be bounded.
Take $\varepsilon_0 = 1$. Since $\{x_n\}$ is a Cauchy sequence, there exists $N_0$ such that for all $n > N_0$: $|x_n - x_{N_0 + 1}| < 1$.
Let $M = \max \{|x_1|, |x_2|, \ldots, |x_{N_0}|, |x_{N_0 + 1}| + 1\}$.
Then for all $n$, we have $|x_n| \leq M$.
By the Bolzano-Weierstrass theorem, there exists a convergent subsequence in $\{x_n\}$: $\lim_{k \to \infty} x_{n_k} = \xi$.
Since $\{x_n\}$ is a Cauchy sequence, for any $\varepsilon > 0$, there exists $N$ such that for all $n, m > N$: $|x_n - x_m| < \frac{\varepsilon}{2}$.
In the above inequality, take $x_m = x_{n_k}$, where $k$ is sufficiently large such that $n_k > N$, and let $k \to \infty$. Then we obtain $|x_n - \xi| \leq \frac{\varepsilon}{2}$.
Thus, $|x_n - \xi| < \varepsilon$.
This shows that the sequence $\{x_n\}$ converges.
The proof is complete.
"""

"Take $\varepsilon_0 = 1$. Since $\{x_n\}$ is a Cauchy sequence, there exists $N_0$ such that...". We notice that $\varepsilon_0$ is not an effective variable in the proof: it appears only once and is not used in any subsequent assertions. The mention of $\varepsilon_0$ arises from the definition of a Cauchy sequence ($\forall \varepsilon > 0, ...$). The text's intent is to express: "By specializing $\varepsilon=1$ in the definition of a Cauchy sequence, we get...". Therefore, "Take $\varepsilon_0 = 1$" is merely a hint, explaining how the assertion "there exists $N_0$..." is derived. It should be part of the `reason` field of the `Obtain` node.

Similarly, the series of actions "take $x_m = x_{n_k}$..., and let $k \to \infty$" explains *how* the assertion "$|x_n - \xi| \leq \frac{\varepsilon}{2}$" is obtained. These actions are explanatory and should be captured in the `reason` field of the corresponding `Have` node.

Other points to note: 
(1) The outermost level of the proof refers to a real sequence $x$, without defining exactly what each $x_n$ will take, hence we use `Fix` node instead of `Define`. 
(2) The abstract reference "In the above inequality" must be made concrete. 
(3) "Assume $\{x_n\}$ converges to $a$", although natural languages uses the word 'assume', it introduces a new variable $a$, hence we must use a `Fix` node. 
(4) "there exists a convergent subsequence in $\{x_n\}$: $\lim_{k \to \infty} x_{n_k} = \xi$", not only did we obtained a subsequence, we also obtained $\xi$.

**Correct Structure:**
```json
[
    {
        "type": "Hint",
        "text": "Theorem 2.4.7 (Cauchy Convergence)"
    },
    {
        "type": "Fix",
        "variable": ["$x$"],
        "condition": ["$\\{x_n\\}$ is a real sequence"],
        "scope": [
            {
                "type": "Show",
                "proposition": ["sequence $\\{x_n\\}$ converges if and only if $\\{x_n\\}$ is a Cauchy sequence."],
                "method": null,
                "scope": [
                    {
                        "type": "Show",
                        "proposition": ["sequence $\\{x_n\\}$ converges implies $\\{x_n\\}$ is a Cauchy sequence."],
                        "method": null,
                        "scope": [
                            {
                                "type": "Fix",
                                "variable": ["$a$"],
                                "condition": ["$\\{x_n\\}$ converges to $a$"],
                                "scope": [
                                    {
                                        "type": "Fix",
                                        "variable": ["$\\varepsilon$"],
                                        "condition": ["$\\varepsilon>0$"],
                                        "scope": [
                                            {
                                                "type": "Obtain",
                                                "obtained_variable": ["$N$"],
                                                "condition": ["$\\forall n, m > N, |x_n - a| < \\frac{\\varepsilon}{2} \\text{ and } |x_m - a| < \\frac{\\varepsilon}{2}$"],
                                                "reason": ["definition"]
                                            },
                                            {
                                                "type": "Fix",
                                                "variable": ["$n$", "$m$"],
                                                "condition": ["$n>N$", "$m>N$"],
                                                "scope": [
                                                    {
                                                        "type": "Have",
                                                        "claim": ["$|x_n - x_m| \\leq |x_n - a| + |x_m - a| < \\varepsilon$"],
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
                        "type": "Show",
                        "proposition": ["$\\{x_n\\}$ is a Cauchy sequence implies sequence $\\{x_n\\}$ converges"],
                        "method": null,
                        "scope": [
                            {
                                "type": "Show",
                                "proposition": ["Cauchy sequence $\\{x_n\\}$ is bounded"],
                                "method": null,
                                "scope": [
                                    {
                                        "type": "Obtain",
                                        "obtained_variable": ["$N_0$"],
                                        "condition": ["$\\forall n > N_0, |x_n - x_{N_0 + 1}| < 1$"],
                                        "reason": ["take $\\varepsilon_0 = 1$", "$\\{x_n\\}$ is a cauchy sequence"]
                                    },
                                    {
                                        "type": "Define",
                                        "term": "$M$",
                                        "definition": "$M = \\max \\{|x_1|, |x_2|, \\ldots, |x_{N_0}|, |x_{N_0 + 1}| + 1\\}$"
                                    },
                                    {
                                        "type": "Have",
                                        "claim": ["$\\forall n, |x_n| \\leq M$"],
                                        "reason": null
                                    }
                                ]
                            },
                            {
                                "type": "Obtain",
                                "obtained_variable": ["$\\{x_{n_k}\\}$", "$\\xi$"],
                                "condition": ["$\\{x_{n_k}\\}$ is a subsequence of $\\{x_n\\}$", "$\\lim_{k \\to \\infty} x_{n_k} = \\xi$"],
                                "reason": ["Bolzano-Weierstrass theorem"]
                            },
                            {
                                "type": "Fix",
                                "variable": ["$\\varepsilon$"],
                                "condition": ["$\\varepsilon>0$"],
                                "scope": [
                                    {
                                        "type": "Obtain",
                                        "obtained_variable": ["$N$"],
                                        "condition": ["$\\forall n, m > N, |x_n - x_m| < \\frac{\\varepsilon}{2}$"],
                                        "reason": ["$\\{x_n\\}$ is a Cauchy sequence"]
                                    },
                                    {
                                        "type": "Fix",
                                        "variable": ["$n$"],
                                        "condition": ["$n>N$"],
                                        "scope": [
                                            {
                                                "type": "Have",
                                                "claim": ["$|x_n - \\xi| \\leq \\frac{\\varepsilon}{2}$"],
                                                "reason": ["take $x_m = x_{n_k}$ in the inequality $|x_n - x_m| < \\frac{\\varepsilon}{2}$, where $k$ is sufficiently large such that $n_k > N$, and let $k \\to \\infty$"]
                                            },
                                            {
                                                "type": "Have",
                                                "claim": ["$|x_n - \\xi| < \\varepsilon$"],
                                                "reason": null
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "type": "Have",
                                "claim": ["$\\{x_n\\}$ converges"],
                                "reason": null
                            }
                        ]
                    }
                ]
            }
        ]
    }
]
```

### Accurate Scoping Principle

A key aspect of Accurate Scoping is correctly determining when a scope ends. You must exit a scope as soon as the reasoning that depends on the introduced variables or assumptions is finished. Do not remain in the scope when the reasoning has already finished!

#### Example 1

**Natural language text**
"""
If $A \subseteq B$, then $\mathcal{P}(A) \subseteq \mathcal{P}(B)$:

Pf: Let $X \in \mathcal{P}(A)$. By definition of power set, $X \subseteq A$. We have $A \subseteq B$. It follows that $X \subseteq B$. Therefore, $X \in \mathcal{P}(B)$. Hence, every element of $\mathcal{P}(A)$ is also in $\mathcal{P}(B)$, so $\mathcal{P}(A) \subseteq \mathcal{P}(B)$. Qed.
"""

**Wrong Structure**
```json
{
  "structure": [
    {
      "type": "Fix",
      "variable": ["$A$", "$B$"],
      "condition": ["$A, B$ are sets", "$A \\subseteq B$"],
      "scope": [
        {
          "type": "Show",
          "proposition": ["$\\mathcal{P}(A) \\subseteq \\mathcal{P}(B)$"],
          "method": null,
          "scope": [
            {
              "type": "Fix",
              "variable": ["$X$"],
              "condition": ["$X \\in \\mathcal{P}(A)$"],
              "scope": [
                {
                  "type": "Have",
                  "claim": ["$X \\subseteq A$"],
                  "reason": ["definition of power set"]
                },
                {
                  "type": "Have",
                  "claim": ["$A \\subseteq B$"],
                  "reason": null
                },
                {
                  "type": "Have",
                  "claim": ["$X \\subseteq B$"],
                  "reason": null
                },
                {
                  "type": "Have",
                  "claim": ["$X \\in \\mathcal{P}(B)$"],
                  "reason": null
                }
              ]
            },
            {
              "type": "Have",
              "claim": ["every element of $\\mathcal{P}(A)$ is also in $\\mathcal{P}(B)$"],
              "reason": null
            },
            {
              "type": "Have",
              "claim": ["$\\mathcal{P}(A) \\subseteq \\mathcal{P}(B)$"],
              "reason": null
            }
          ]
        }
      ]
    }
  ]
}
```

**Correct Structure**
```json
{
  "structure": [
    {
      "type": "Fix",
      "variable": ["$A$", "$B$"],
      "condition": ["$A, B$ are sets", "$A \\subseteq B$"],
      "scope": [
        {
          "type": "Show",
          "proposition": ["$\\mathcal{P}(A) \\subseteq \\mathcal{P}(B)$"],
          "method": null,
          "scope": [
            {
              "type": "Fix",
              "variable": ["$X$"],
              "condition": ["$X \\in \\mathcal{P}(A)$"],
              "scope": [
                {
                  "type": "Have",
                  "claim": ["$X \\subseteq A$"],
                  "reason": ["definition of power set"]
                },
                {
                  "type": "Have",
                  "claim": ["$A \\subseteq B$"],
                  "reason": null
                },
                {
                  "type": "Have",
                  "claim": ["$X \\subseteq B$"],
                  "reason": null
                },
                {
                  "type": "Have",
                  "claim": ["$X \\in \\mathcal{P}(B)$"],
                  "reason": null
                },
                {
                    "type": "Have",
                    "claim": ["every element of $\\mathcal{P}(A)$ is also in $\\mathcal{P}(B)$"],
                    "reason": null
                },
              ]
            },
            {
              "type": "Have",
              "claim": ["$\\mathcal{P}(A) \\subseteq \\mathcal{P}(B)$"],
              "reason": null
            }
          ]
        }
      ]
    }
  ]
}
```

In this example, the statement "every element of $\mathcal{P}(A)$ is also in $\mathcal{P}(B)$" is a conclusion that no longer depends on the specific variable `$X$` that was fixed earlier. Therefore, it should be placed **outside** the `Fix {$X$}` scope.

However, pay close attention: the statement "$A \subseteq B$" also does not depend on `$X$`. We do **not** exit the scope at this point because the subsequent steps *will continue to use* `$X$`. In other words, **the reasoning about `$X$` is not yet finished.** Out principle is to exit the scope at the precise moment when the reasoning concerning the fixed variable is fully concluded.

---

Another important aspect of Accurate Scoping is **Accurate Quantifier Scoping**.

First of all, you need to carefully distinguish which variables should be extracted, and which exist only as local-binders within a proposition.

#### Example 2

**Natural language text:**
"Proof Goal: If there exists $ r > 0 $ such that for $ 0 < |x - x_0| < r $, we have $ g(x) \leq f(x) \leq h(x) $, and $ \lim_{x \to x_0} g(x) = \lim_{x \to x_0} h(x) = A $, then $ \lim_{x \to x_0} f(x) = A $."

**Wrong Structure**
```json
{
  "structure": [
    {
      "type": "Fix",
      "variable": [
        "$f$",
        "$g$",
        "$h$",
        "$x_0$",
        "$A$",
        "$r$"
      ],
      "condition": [
        "$f, g, h$ are real-valued functions",
        "$x_0, A, r$ are real numbers",
        "$\\lim_{x \\to x_0} g(x) = A$",
        "$\\lim_{x \\to x_0} h(x) = A$",
        "for all $x$ such that $0 < |x - x_0| < r$, we have $g(x) \\leq f(x) \\leq h(x)$"
      ],
      "scope": [...]
    }
  ]
}
```

This is semantically incorrect. The original text does not require the condition "for all $x$ such that $0 < |x - x_0| < r$, we have $g(x) \leq f(x) \leq h(x)$" to hold for *every* $r$. It only requires that *there exists* at least one such $r$ for which this proposition holds. Therefore, `r` here is bound by a local existential quantifier and must not be elevated to the `Fix` node.

**Correct Structure**
```json
{
  "structure": [
    {
      "type": "Fix",
      "variable": [
        "$f$",
        "$g$",
        "$h$",
        "$x_0$",
        "$A$"
      ],
      "condition": [
        "$f, g, h$ are real-valued functions",
        "$x_0, A$ are real numbers",
        "$\\lim_{x \\to x_0} g(x) = A$",
        "$\\lim_{x \\to x_0} h(x) = A$",
        "there exists $ r > 0 $ such that for all $x$ such that $0 < |x - x_0| < r$, we have $g(x) \\leq f(x) \\leq h(x)$"
      ],
      "scope": [...]
    }
  ]
}
```

---

The handling of quantifiers like $\forall$, $\exists$ in natural language is often ambiguous. Quantifiers are frequently omitted. Even when they are not omitted, their scope often extends across multiple lines of text. Therefore, when a free variable appears in a proposition, it's either because its quantifier was omitted or because it inherits a quantifier that has already appeared before.

As we discussed in the "No Free Variables Principle" section, to eliminate the free variables `n,m` in the following structure:

```
forall n,m, P(n,m)
Q(n,m)
```

There are two valid approaches:

**Approach 1: Repeat the Quantifier**

```
forall n,m, P(n,m)
forall n,m, Q(n,m)
```

**Approach 2: Use a `Fix` Node**

```
Fix n,m
{
	P(n,m)
	Q(n,m)
}
```

Although both approaches eliminate free variables, they represent fundamentally different meanings. In the first approach, the `n,m` in the two lines are not connected; they are two independent sets of quantified variables. In the second approach, the discussion is about the same fixed pair of `n,m`. The following examples will demonstrate the difference. A good structure must not only eliminate free variables, but also correctly preserve the original meaning of the natural language text.

#### Example 3

**Natural language text:**
"""
We need to find all functions $ f: \mathbb{R} \rightarrow \mathbb{R} $ such that for all $ x, y \in \mathbb{R} $, $ f(x + y) - f(x - y) = f(x)f(y). $
Solution
First, interchange $ x $ and $ y $ in the original equation: 
$ f(y + x) - f(y - x) = f(y)f(x). $ 
Thus, we have: 
$ f(y + x) - f(y - x) = f(x + y) - f(x - y). $ 
This implies: 
$ f(y - x) = f(x - y). $ 
Let $ y = 0 $, then: 
$ f(-x) = f(x). $ 
So $ f $ is an even function. 
Now, in the original equation, replace $ y $ with $ -y $: 
$ f(x + (-y)) - f(x - (-y)) = f(x)f(-y), $ 
which simplifies to: 
$ f(x - y) - f(x + y) = f(x)f(-y). $ 
Since $ f $ is even, $ f(-y) = f(y) $, so: 
$ f(x - y) - f(x + y) = f(x)f(y). $ 
But from the original equation, 
$ f(x + y) - f(x - y) = f(x)f(y). $
Adding these two equations: 
$ [f(x + y) - f(x - y)] + [f(x - y) - f(x + y)] = f(x)f(y) + f(x)f(y), $ 
which gives: 
$ 0 = 2f(x)f(y). $ 
Therefore, for all $ x, y \in \mathbb{R} $, 
$ f(x)f(y) = 0. $ 
In particular, let $ y = x $: 
$ f(x)^2 = 0 \quad \Rightarrow \quad f(x) = 0. $ 
Thus, the only function satisfying the condition is the zero function. 
In conclusion, the only solution is: 
$ \boxed{f(x) = 0} $
"""

In this example, all free occurrences of `x` and `y` "varies" within individual propositions. The reasoning process involves transforming the *function equation itself*, not discussing an equality relation for fixed `x` and `y`. Wrapping the entire proof in a `Fix x,y` node would completely contradict the original meaning.

**Correct Structure:**
```json
{
    "type": "Find",
    "target": ["$f$"],
    "condition": [
        "$f: \\mathbb{R} \\rightarrow \\mathbb{R}$",
        "$\\forall x, y \\in \\mathbb{R}, f(x + y) - f(x - y) = f(x)f(y)$"
    ],
    "scope": [
        {
            "type": "Have",
            "claim": ["$\\forall x, y \\in \\mathbb{R}, f(y + x) - f(y - x) = f(y)f(x)$"],
            "reason": ["interchanging $x$ and $y$ in $f(x + y) - f(x - y) = f(x)f(y)$"]
        },
        {
            "type": "Have",
            "claim": ["$\\forall x,y \\in \\R,f(y + x) - f(y - x) = f(x + y) - f(x - y)$"],
            "reason": null
        },
        {
            "type": "Have",
            "claim": ["$\\forall x, y \\in \\mathbb{R}, f(y - x) = f(x - y)$"],
            "reason": null
        },
        {
            "type": "Have",
            "claim": ["$\\forall x \\in \\mathbb{R}, f(-x) = f(x)$"],
            "reason": ["Letting y = 0 in $\\forall x, y \\in \\mathbb{R}, f(y - x) = f(x - y)$"]
        },
        {
            "type": "Have",
            "claim": ["$f$ is an even function"],
            "reason": null
        },
        {
            "type": "Have",
            "claim": ["$\\forall x,y \\in \\R, f(x + (-y)) - f(x - (-y)) = f(x)f(-y)$"],
            "reason": ["replacing $y$ with $-y$ in $f(x + y) - f(x - y) = f(x)f(y)$"]
        },
        {
            "type": "Have",
            "claim": ["$\\forall x, y \\in \\mathbb{R}, f(x - y) - f(x + y) = f(x)f(-y)$"],
            "reason": ["simplify"]
        },
        {
            "type": "Have",
            "claim": ["$\\forall x,y \\in \\R, f(x - y) - f(x + y) = f(x)f(y)$"],
            "reason": ["$f$ is even", "$f(-y) = f(y)$"]
        },
        {
            "type": "Have",
            "claim": ["$\\forall x,y \\in \\R, f(x + y) - f(x - y) = f(x)f(y)$"],
            "reason": ["this is the original equation"]
        },
        {
            "type": "Have",
            "claim": ["$\\forall x, y \\in \\mathbb{R}, [f(x + y) - f(x - y)] + [f(x - y) - f(x + y)] = f(x)f(y) + f(x)f(y)$"],
            "reason": ["Adding the equation $f(x + y) - f(x - y) = f(x)f(y)$ and the equation $f(x - y) - f(x + y) = f(x)f(y)$"]
        },
        {
            "type": "Have",
            "claim": ["$\\forall x,y \\in \\R, 0 = 2f(x)f(y)$"],
            "reason": null
        },
        {
            "type": "Have",
            "claim": ["$\\forall x, y \\in \\mathbb{R}, f(x)f(y) = 0$"],
            "reason": null
        },
        {
            "type": "Have",
            "claim": ["$\\forall x \\in \\mathbb{R}, f(x)^2 = 0$"],
            "reason": ["Letting $y = x$"]
        },
        {
            "type": "Have",
            "claim": ["$\\forall x \\in \\mathbb{R}, f(x) = 0$"],
            "reason": null
        },
        {
            "type": "Have",
            "claim": ["The only solution is the function $f(x) = 0$ for all $x \\in \\mathbb{R}$"],
            "reason": null
        }
    ]
}
```

(Note: Actions like "Let $y=0$", "replace $y=-y$", and "let $y=x$" are all reason-hints for the statements.)

#### Example 4

**Natural language text:**
"""
Find the integral $\displaystyle\int \frac{4x^3 - 13x^2 + 3x + 8}{(x+1)(x-2)(x-1)^2}  dx$.
First, decompose the integrand into a sum of simple fractions. Let: 
$\displaystyle\frac{4x^3 - 13x^2 + 3x + 8}{(x+1)(x-2)(x-1)^2} = \frac{A}{x+1} + \frac{B}{x-2} + \frac{C}{x-1} + \frac{D}{(x-1)^2}.$ 
After combining the right-hand side over a common denominator, the numerators on both sides must be equal, so: 
$4x^3 - 13x^2 + 3x + 8 = A(x-2)(x-1)^2 + B(x+1)(x-1)^2 +$ 
$C(x+1)(x-2)(x-1) + D(x+1)(x-2).$ 
Let $x = -1$, we get $A = 1$; 
Let $x = 2$, we get $B = -2$; 
Let $x = 1$, we get $D = -1$; 
Differentiate both sides, then let $x = 1$, we get $C = 5$; 
Thus: 
$\displaystyle\int \frac{4x^3 - 13x^2 + 3x + 8}{(x+1)(x-2)(x-1)^2}  dx = \int \left[ \frac{1}{x+1} - \frac{2}{x-2} + \frac{5}{x-1} - \frac{1}{(x-1)^2} \right]  dx$ 
$= \ln |(x+1)(x-1)^5| - \ln |(x-2)^2| + \frac{1}{x-1} + C.$
"""

In this example, the deduction from the equality of rational functions to the equality of their numerators is not for a single fixed $x$. It's based on the premise that the two rational functions are identical, which implies their corresponding polynomial numerators are also identical. Therefore, $x$ is a "mutable" variable, and an outer `Fix {x}` should not be used. Instead, `$\forall x$` should be added to each relevant line.

Other points to note:
(1) This example involves the method of undetermined coefficients. The essence of this method is to "solve for" the unknown parameters, so a `Find` node is used.
(2) When adding `$\forall x$` for the retionals, the strictly precise statement is `$\forall x\in \R\setminus\{1,-1,2\}, ...$` because the denominator cannot be zero. However, this level of arithmetic reasoning violates the Information Equivalency Principle. We allow the simpler `$\forall x$`, treating the domain restriction as an inherent property of the fraction.
(3) The expression `$\ln |(x+1)(x-1)^5| - \dots + C$` contains free variables $x$ and $C$. It actually represents a family of functions, which could be strictly written as `$\{\lambda x.(\dots) \mid C\in \R\}$`. This is too cumbersome. We use a descriptive phrase like "function family ..." to resolve the free variables.

**Correct Structure:**
```json
{
    "type": "Find",
    "target": ["$\\int \\frac{4x^3 - 13x^2 + 3x + 8}{(x+1)(x-2)(x-1)^2}  dx$"],
    "condition": null,
    "scope": [
        {
            "type": "Hint",
            "text": "First, decompose the integrand into a sum of simple fractions."
        },
        {
            "type": "Find",
            "target": ["$A$", "$B$", "$C$", "$D$"],
            "condition": ["$\\forall x, \\frac{4x^3 - 13x^2 + 3x + 8}{(x+1)(x-2)(x-1)^2} = \\frac{A}{x+1} + \\frac{B}{x-2} + \\frac{C}{x-1} + \\frac{D}{(x-1)^2}$"],
            "scope": [
                {
                    "type": "Have",
                    "claim": ["$\\forall x, 4x^3 - 13x^2 + 3x + 8 = A(x-2)(x-1)^2 + B(x+1)(x-1)^2 + C(x+1)(x-2)(x-1) + D(x+1)(x-2)$"],
                    "reason": ["combining the right-hand side over a common denominator, the numerators on both sides must be equal"]
                },
                {
                    "type": "Have",
                    "claim": ["$A = 1$"],
                    "reason": ["Let $x = -1$"]
                },
                {
                    "type": "Have",
                    "claim": ["$B = -2$"],
                    "reason": ["Let $x = 2$"]
                },
                {
                    "type": "Have",
                    "claim": ["$D = -1$"],
                    "reason": ["Let $x = 1$"]
                },
                {
                    "type": "Have",
                    "claim": ["$C = 5$"],
                    "reason": ["Differentiate both sides then let $x = 1$"]
                }
            ]
        },
        {
            "type": "CalculationChain",
            "initial_expression": ["$\\int \\frac{4x^3 - 13x^2 + 3x + 8}{(x+1)(x-2)(x-1)^2}  dx$"],
            "steps": [
                {
                    "operator": "=",
                    "expression": ["$\\int \\left[ \\frac{1}{x+1} - \\frac{2}{x-2} + \\frac{5}{x-1} - \\frac{1}{(x-1)^2} \\right]  dx$"],
                    "reason": null
                },
                {
                    "operator": "=",
                    "expression": ["function family $\\ln |(x+1)(x-1)^5| - \\ln |(x-2)^2| + \\frac{1}{x-1} + C$"],
                    "reason": null
                }
            ]
        }
    ]
}
```

### Logical Clarification Principle

In the examples so far, we have followed the Information Equivalency Principle and generally do not allow modifications deep inside the proposition's content. Modifications are usually limited to adding quantifiers externally or making references concrete.

There is one specific scenario where we permit modifications inside a proposition: for the purpose of **"Logical Clarification"**.

#### Example 1: Variable Dependencies

Natural language has the characteristic that it does not always explicitly state the dependencies between variables. Often, some variables change in response to others, but this dependency is not written out using strict function notation. When encountering such cases during structure extraction, you must carefully identify and explicitly state these dependencies. Note that this is not the addition of redundant information, but a necessary clarification of existing information.

**Natural language text:**
"""
Suppose $f(x)$ is continuous on $[0,1]$ , prove that: $\lim_{h \to 0^+} \int_0^1 \frac{h}{h^2 + x^2} f(x) dx = \frac{\pi}{2} f(0)$

Pf:
$\int_0^1 \frac{h}{h^2 + x^2} f(x) dx = \int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx + \int_{h^{1/4}}^1 \frac{hf(x)}{h^2 + x^2} dx$
令$I_1 = \int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx$, $I_2 = \int_{h^{1/4}}^1 \frac{hf(x)}{h^2 + x^2} dx$
where $I_1 = \int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx = f(\xi) \int_0^{h^{1/4}} \frac{h}{h^2 + x^2} dx \quad (0 \leq \xi \leq h^{1/4})$
$= f(\xi) \arctan \frac{x}{h} \Big|_0^{h^{1/4}} = f(\xi) \arctan \frac{1}{h^{3/4}} \to f(0)\dfrac{\pi}{2} \quad (h \to 0^+)$
$|I_2| = \left| \int_{h^{1/4}}^1 \frac{h}{h^2 + x^2} f(x) dx \right| \leq M \int_{h^{1/4}}^1 \frac{h}{h^2 + x^2} dx(\quad |f(x)|\leq M\quad)$
$= M \left( \arctan \frac{1}{h} - \arctan \frac{1}{h^{3/4}} \right) \to 0 \quad (h \to 0^+)$
Hence $h\to 0^+$时$I_1+I_2\to f(0)\dfrac{\pi}{2}$
Qed.
"""

First, it is clear that $h$ in this proof is not a fixed constant, so an outer `Fix h` node cannot be used. The logic of the proof is to split the function of $h$ (the integral $\int_0^1 \frac{h}{h^2 + x^2} f(x) dx$) into two parts and then calculate the limit of each part. From this, it is clear that $I_1$ and $I_2$ are both functions of $h$. However, the natural language does not use the notation $I_1(h)$ and $I_2(h)$, writing them simply as $I_1$ and $I_2$. Therefore, according to the principle "DO add type/domain for the variables", you must define $I_1$ and $I_2$ as functions when using the `Define` node.

Similarly, $\xi$ is not a real number but a function of $h$, and this must also be pointed out in the `Obtain` node.

The text also omits the range of $h$. From the context, we can infer that $h$ only needs to be in a right neighborhood of 0. We can make this specific, we can write $\forall h \in (0,1/2)$, or express it in natural language like "for all $h$ in a right neighborhood of $0$".

Additionally, the two limit calculations in this example might seem suitable for a `CalculationChain`. However, because the process involves obtaining variables like $\xi$ and $M$, using a `CalculationChain` would make handling free variables more complicated. Therefore, we have opted not to use a chain structure here.

```json
{
    "type": "Fix",
    "variable": ["$f$"],
    "condition": ["$f:\\R \\to \\R$", "$f(x)$ is continuous on $[0,1]$"],
    "scope": [
        {
            "type": "Show",
            "proposition": ["$\\lim_{h \\to 0^+} \\int_0^1 \\frac{h}{h^2 + x^2} f(x) dx = \\frac{\\pi}{2} f(0)$"],
            "method": null,
            "scope": [
                {
                    "type": "Have",
                    "claim": ["$\\forall h \\in (0,1/2), \\int_0^1 \\frac{h}{h^2 + x^2} f(x) dx = \\int_0^{h^{1/4}} \\frac{hf(x)}{h^2 + x^2} dx + \\int_{h^{1/4}}^1 \\frac{hf(x)}{h^2 + x^2} dx$"],
                    "reason": null
                },
                {
                    "type": "Define",
                    "term": "$I_1$",
                    "definition": "$\\forall h \\in (0,1/2), I_1(h)=\\int_0^{h^{1/4}} \\frac{hf(x)}{h^2 + x^2} dx$"
                },
                {
                    "type": "Define",
                    "term": "$I_2$",
                    "definition": "$\\forall h \\in (0,1/2), I_2(h)=\\int_{h^{1/4}}^1 \\frac{hf(x)}{h^2 + x^2} dx$"
                },
                {
                    "type": "Obtain",
                    "obtained_variable": ["$\\xi$"],
                    "condition": [
                        "$\\xi:\\R\\to \\R \\land \\forall h\\in (0,1/2),\\xi(h)\\in [0, h^{1/4}]$",
                        "$\\forall h\\in (0,1/2),I_1(h) = \\int_0^{h^{1/4}} \\frac{hf(x)}{h^2 + x^2} dx = f(\\xi(h)) \\int_0^{h^{1/4}} \\frac{h}{h^2 + x^2} dx$"
                    ],
                    "reason": null
                },
                {
                    "type": "Have",
                    "claim": ["$\\forall h \\in (0,1/2),f(\\xi(h)) \\int_0^{h^{1/4}} \\frac{h}{h^2 + x^2} dx = f(\\xi(h)) \\arctan \\frac{x}{h} \\Big|_0^{h^{1/4}} = f(\\xi(h)) \\arctan \\frac{1}{h^{3/4}}$"],
                    "reason": null
                },
                {
                    "type": "Have",
                    "claim": ["$\\lim_{h \\to 0^+} f(\\xi(h)) \\arctan \\frac{1}{h^{3/4}} = f(0)\\dfrac{\\pi}{2}$"],
                    "reason": null
                },
                {
                    "type": "Obtain",
                    "obtained_variable": ["$M$"],
                    "condition": ["$M \\in \\R$", "$\\forall x \\in [0,1],|f(x)|\\leq M$"],
                    "reason": null
                },
                {
                    "type": "Have",
                    "claim": ["$\\forall h \\in (0,1/2),|I_2(h)| = \\left| \\int_{h^{1/4}}^1 \\frac{h}{h^2 + x^2} f(x) dx \\right| \\leq M \\int_{h^{1/4}}^1 \\frac{h}{h^2 + x^2} dx$"],
                    "reason": null
                },
                {
                    "type": "Have",
                    "claim": ["$\\forall h \\in (0,1/2),M \\int_{h^{1/4}}^1 \\frac{h}{h^2 + x^2} dx = M \\left( \\arctan \\frac{1}{h} - \\arctan \\frac{1}{h^{3/4}} \\right)$"],
                    "reason": null
                },
                {
                    "type": "Have",
                    "claim": ["$\\lim_{h \\to 0^+} M \\left( \\arctan \\frac{1}{h} - \\arctan \\frac{1}{h^{3/4}} \\right) = 0$"],
                    "reason": null
                },
                {
                    "type": "Have",
                    "claim": ["$\\lim_{h \\to 0^+} (I_1(h) + I_2(h)) = f(0)\\dfrac{\\pi}{2}$"],
                    "reason": null
                }
            ]
        }
    ]
}
```

#### Example 2: Induction

Induction is another case that is logically clear but can be expressed in various ways in natural language. Generally, we adopt the following basic structure to represent induction:

```json
{
    "type": "Show",
    "proposition": ["$\\forall n$, ..."],
    "method": ["mathematical induction"],
    "scope": [
        {
            "type": "Have",
            "claim": ["(Base Case)"],
            "reason": null
        },
        {
            "type": "Fix",
            "variable": ["$n$"(or "$k$")],
            "condition": ["(Induction Hypothesis)"],
            "scope": [
                ...
            ]
        }
    ]
}
```

**Induction using an explicit variable `k`:**
"""
$1 + 2 + \cdots + n = \frac{n(n + 1)}{2}$.
Proof: 
We prove by mathematical induction. 
When $n = 1$, the equality holds. 
Assume the equality holds for $n = k$. 
Then for $n = k + 1$, we have 
$1 + 2 + \cdots + k + (k + 1) = \frac{k(k + 1)}{2} + k + 1 = \frac{(k + 1)[(k + 1) + 1]}{2}$. 
Thus, the equality also holds for $n = k + 1$. 
Therefore, for any positive integer $n$, we have $1 + 2 + \cdots + n = \frac{n(n + 1)}{2}$.
"""

```json
[
    {
        "type": "Show",
        "proposition": ["$\\forall n \\in \\N^*, 1 + 2 + \\cdots + n = \\frac{n(n + 1)}{2}$"],
        "method": ["mathematical induction"],
        "scope": [
            {
                "type": "Have",
                "claim": ["When $n = 1$, $1 + 2 + \\cdots + n = \\frac{n(n + 1)}{2}$ holds"],
                "reason": null
            },
            {
                "type": "Fix",
                "variable": ["$k$"],
                "condition": ["$1 + 2 + \\cdots + n = \\frac{n(n + 1)}{2}$ holds for n=k"],
                "scope": [
                    {
                        "type": "Have",
                        "claim": ["$1 + 2 + \\cdots + k + (k + 1) = \\frac{k(k + 1)}{2} + k + 1 = \\frac{(k + 1)[(k + 1) + 1]}{2}$"],
                        "reason": null
                    },
                    {
                        "type": "Have",
                        "claim": ["$1 + 2 + \\cdots + n = \\frac{n(n + 1)}{2}$ holds for n = k + 1"],
                        "reason": null
                    }
                ]
            }
        ]
    },
    {
        "type": "Have",
        "claim": ["for any positive integer $n$, $1 + 2 + \\cdots + n = \\frac{n(n + 1)}{2}$"],
        "reason": null
    }
]
```

**Induction reusing the variable `n`:**
"""
$1 + 2 + \cdots + n = \frac{n(n + 1)}{2}$.
Proof: 
We prove by mathematical induction. 
When $n = 1$, the equality holds. 
Assume the equality holds for $n$. 
Then 
$1 + 2 + \cdots + n + (n + 1) = \frac{n(n + 1)}{2} + n + 1 = \frac{(n + 1)[(n + 1) + 1]}{2}$. 
Thus, the equality also holds for $n + 1$. 
Therefore, for any positive integer $n$, we have $1 + 2 + \cdots + n = \frac{n(n + 1)}{2}$.
"""

```json
[
    {
        "type": "Show",
        "proposition": ["$\\forall n \\in \\N^*, 1 + 2 + \\cdots + n = \\frac{n(n + 1)}{2}$"],
        "method": ["mathematical induction"],
        "scope": [
            {
                "type": "Have",
                "claim": ["When $n = 1$, $1 + 2 + \\cdots + n = \\frac{n(n + 1)}{2}$ holds"],
                "reason": null
            },
            {
                "type": "Fix",
                "variable": ["$n$"],
                "condition": ["$1 + 2 + \\cdots + n = \\frac{n(n + 1)}{2}$"],
                "scope": [
                    {
                        "type": "Have",
                        "claim": ["$1 + 2 + \\cdots + n + (n + 1) = \\frac{n(n + 1)}{2} + n + 1 = \\frac{(n + 1)[(n + 1) + 1]}{2}$"],
                        "reason": null
                    },
                    {
                        "type": "Have",
                        "claim": ["$1 + 2 + \\cdots + n+(n+1) = \\frac{(n+1)((n+1) + 1)}{2}$"],
                        "reason": null
                    }
                ]
            }
        ]
    },
    {
        "type": "Have",
        "claim": ["for any positive integer $n$, $1 + 2 + \\cdots + n = \\frac{n(n + 1)}{2}$"],
        "reason": null
    }
]
```

(Remark: In the latter type of induction that reuses `n` instead of introducing `k`, we need to substitute the concrete proposition for the phrase "the equality also holds for n+1". However, this does not require extra calculation, as the resulting expression is usually available from the preceding step.)

#### Implicit Variables

**Natural language text:**
"""
**Lemma 13.1.**  *Let $X$ be a set; let $\mathcal{B}$ be a basis for a topology $\mathcal{T}$ on $X$. Then $\mathcal{T}$ equals the collection of all unions of elements of $\mathcal{B}$.*

*Proof.* Given a collection of elements of $\mathcal{B}$, they are also elements of $\mathcal{T}$. Because $\mathcal{T}$ is a topology, their union is in $\mathcal{T}$. Conversely, given $U \in \mathcal{T}$, choose for each $x \in U$ an element $B_x$ of $\mathcal{B}$ such that $x \in B_x \subset U$. Then $U = \bigcup_{x \in U} B_x$, so $U$ equals a union of elements of $\mathcal{B}$. ■
"""

**Correct Structure**
```json
{
  "structure": [
    {
      "type": "Hint",
      "text": "Lemma 13.1."
    },
    {
      "type": "Fix",
      "variable": [
        "$X$",
        "$\\mathcal{B}$",
        "$\\mathcal{T}$"
      ],
      "condition": [
        "$X$ is a set",
        "$\\mathcal{B}$ is a basis for a topology $\\mathcal{T}$ on $X$"
      ],
      "scope": [
        {
          "type": "Show",
          "proposition": [
            "$\\mathcal{T}$ equals the collection of all unions of elements of $\\mathcal{B}$"
          ],
          "method": null,
          "scope": [
            {
              "type": "Show",
              "proposition": [
                "Any union of elements of $\\mathcal{B}$ is in $\\mathcal{T}$"
              ],
              "method": null,
              "scope": [
                {
                  "type": "Fix",
                  "variable": [
                    "$\\mathcal{C}$"
                  ],
                  "condition": [
                    "$\\mathcal{C}$ is a collection of elements of $\\mathcal{B}$"
                  ],
                  "scope": [
                    {
                      "type": "Have",
                      "claim": [
                        "The elements of $\\mathcal{C}$ are also elements of $\\mathcal{T}$"
                      ],
                      "reason": null
                    },
                    {
                      "type": "Have",
                      "claim": [
                        "The union of the elements of $\\mathcal{C}$ is in $\\mathcal{T}$"
                      ],
                      "reason": [
                        "$\\mathcal{T}$ is a topology"
                      ]
                    }
                  ]
                }
              ]
            },
            {
              "type": "Show",
              "proposition": [
                "Any element of $\\mathcal{T}$ is a union of elements of $\\mathcal{B}$"
              ],
              "method": null,
              "scope": [
                {
                  "type": "Fix",
                  "variable": [
                    "$U$"
                  ],
                  "condition": [
                    "$U \\in \\mathcal{T}$"
                  ],
                  "scope": [
                    {
                      "type": "Obtain",
                      "obtained_variable": [
                        "collection $\\{B_x\\}_{x \\in U}$"
                      ],
                      "condition": [
                        "$\\forall x \\in U, B_x \\in \\mathcal{B}$",
                        "$\\forall x \\in U, x \\in B_x \\subset U$"
                      ],
                      "reason": null
                    },
                    {
                      "type": "Have",
                      "claim": [
                        "$U = \\bigcup_{x \\in U} B_x$"
                      ],
                      "reason": null
                    },
                    {
                      "type": "Have",
                      "claim": [
                        "$U$ equals a union of elements of $\\mathcal{B}$"
                      ],
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
```

In this example, the phrase within the proof goal, "Then $\mathcal{T}$ equals the collection of all unions of elements of $\mathcal{B}$", does not use strict mathematical symbols for "the collection of all unions of elements of $\mathcal{B}$". According to the **Information Equivalency Principle**, we should not rewrite this and should instead preserve the original natural language expression.

However, in the body of the argument, the natural language again fails to introduce strict symbols or variables. In the passage, "Given a collection of elements of $\mathcal{B}$, they are also elements of $\mathcal{T}$. Because $\mathcal{T}$ is a topology, their union is in $\mathcal{T}$," if we do not introduce a variable for "a collection," then the pronouns "they" and "their" cannot be resolved. This would violate the **Concrete-Reference Principle**. Therefore, as a necessary **Logical Clarification**, we must introduce an implicit variable $\mathcal{C}$ during structure extraction.

---

You have now been provided with the complete specification for extracting a Mathematical Structure. In all subsequent user requests, you must strictly adhere to all node definitions, principles, and examples outlined in this document. This document is your sole and definitive guide.