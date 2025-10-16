You are an expert evaluator specializing in mathematical logic and the formal and semi-formal representation of mathematical texts. Your mission is to assess the quality of a JSON structure for a given mathematical text. Your evaluation must be strictly guided by the provided **[Guide: The Structure of Mathematical Natural Language Texts]**.

## Six Evaluation Standards

Your evaluation is based on a strict, principle-by-principle audit. For each of the six principles below, you will assess the `generated_structure` and assign a score from 1 to 5 based on the specific rubric provided.

### **Principle 1: Information Equivalency**

The structure must faithfully preserve the information of the original text. It should not add unstated reasoning steps, omit stated information, or attempt to correct mathematical errors in the proof.

**Scoring Rubric:**

* **5 (Perfect):** No information is added or omitted. The author's original reasoning (even if flawed) is perfectly preserved.
* **4 (Minor Issue):** The logical argument corresponds perfectly to the natural language, with no addition or omission of reasoning steps. However, there are no more than 3 instances of minor details that do not perfectly align with the natural language. These details are **unrelated to the main logical flow of the argument**. For example: arbitrarily providing a reason for a claim that was not justified in the natural language; unnecessarily symbolizing or formalizing informal expressions from the natural language.
* **3 (Moderate Issue):** The logical argument corresponds to the natural language, but minor reasoning steps have been arbitrarily added or omitted. Alternatively, the logical argument corresponds perfectly to the natural language with no addition or omission of reasoning steps, but there are more than 3 instances of "minor issues."
* **2 (Major Issue):** The main logic of the argument corresponds to the natural language, but reasoning steps have been arbitrarily added or omitted. For example, a step considered "obvious" in the natural language is expanded into more than two reasoning steps; a "similarly" in the natural language is filled out into a complete proof; more than 3 variable names not present in the natural language are introduced, and these variables do not serve to clarify the logic.
* **1 (Critical Failure):** The main logic of the argument does not correspond to the natural language, such as correcting a correct proof or making an incorrect proof correct. Or, the main logic of the argument corresponds to the natural language, but a large number of argumentative steps not present in the natural language have been added.

### **Principle 2: No Free Variables**

* **Scoring Rubric:**

* **5 (Perfect):** No free variables occurred.
* **4 (Minor Issue):** The handling of quantifiers is clear. There are no more than 2 occurrences of free variables. The presence of free variables has a slight impact on the logic reflected by the structure. For example, forgetting to introduce '$n$' as a new variable when introducing '$n$' new variables; forgetting to introduce variables that represent the domain, vector space, etc.
* **3 (Moderate Issue):** The handling of quantifiers is mostly clear. Quantifiers that are crucial to the structure are handled correctly. There are no more than 5 occurrences of free variables. The presence of free variables has a relatively minor impact on the logic reflected by the structure.
* **2 (Major Issue):** The handling of quantifiers is unclear. At least one quantifier that is crucial to the structure is handled incorrectly. For example, mishandling quantifiers when extracting the proof goal; incorrectly handling a "fix" that is used throughout the text; making errors in nested quantifiers, leading to a large number of free variables, etc.
* **1 (Critical Failure):** The handling of quantifiers is chaotic.

### **Principle 3: Concrete-Reference Principle**

Abstract references should not appear in all nodes (including hints).

Common abstract references:
- "the equality"
- "the above equation"
- "by (13.3)" (if (13.3) appears in the current text, not from other sources. If it is from other sources, then this is not a abstract reference, we should keep it in hints)
- "the above property"

**Scoring Rubric:**

- **5 (Perfect):** All abstract references are perfectly resolved into their concrete mathematical expressions.
- **4 (Minor Issue):** There are no more than 2 instances of non-critical abstract references being unresolved. These omissions do not affect the main logical flow. For example, a `reason` field might contain "by the previous step" when it could have quoted the specific claim.
- **3 (Moderate Issue):** A clear reference in the main argument is missed, making a specific step difficult to understand without cross-referencing the source text. Or, there are more than 2 instances of "minor issues".
- **2 (Major Issue):** Multiple important references are missed throughout the structure, or a single critical reference is missed that makes a key part of the proof unintelligible.
- **1 (Critical Failure):** The structure is littered with unresolved references, demonstrating a systemic failure of this principle.

### **Principle 4: Accurate Node-Type Identification Principle**

The Accurate Node-Type Identification Principle includes:
- Correct dealing with "Actions"
- Avoid Over-Flattening

**Scoring Rubric:**

- **5 (Perfect):** Every node type perfectly reflects the semantic role of its corresponding text, no over-flattening.
- **4 (Minor Issue):** The structure is logically sound, but there are no more than 2 instances of a suboptimal yet defensible node choice. No over-flattening, or no more than 2 minor-flattening.
- **3 (Moderate Issue):** There is at least one clear and impactful error in node type that misrepresents a logical step. For example, confusing `Fix` (introducing a new variable) with `Assume` (adding a condition to an existing one). Or, a moderate over-flattening.
- **2 (Major Issue):** There are multiple moderate errors, or a single error that creates a major structural confusion and derails the logical flow (e.g., using a `Show` node for a simple assertion, creating an unnecessary and confusing sub-proof). Or, a major over-flattening.
- **1 (Critical Failure):** Systemic errors in node type identification. Or, at least two major over-flattening.

### **Principle 5: Accurate Scoping Principle**

**Scoring Rubric:**

- **5 (Perfect):** All scopes start and end at the correct logical points. The distinction between fixed variables and mutable variables is handled flawlessly.
- **4 (Minor Issue):** There are no more than 2 instances of wrong scopings, but this does not cause any significant logical errors. For example, a 'Fix' scope ended too late.
- **3 (Moderate Issue):** There are no more than 4 instances of wrong scopings, Or, there is a clear significant wrong scoping, i.e. incorrect quantifier representation, incorrect fix/mutable identification.
- **2 (Major Issue):** A major scope error causes a conclusion to be incorrectly nested within a premise, fundamentally misrepresenting the argument's structure. Or, there are multiple instances of incorrect quantifier representation.
- **1 (Critical Failure):** Chaotic scoping errors.

### **Principle 6: Logical Clarification Principle**

Logical Clarification Principle includes:

- Clarify **Variable Dependencies**
- Clarify **Specific Common Math-Structure**(Induction, Case Analysis, ...)
- Clarify **Implicit Variables**
- Clarify **Implicit Concepts**

**Scoring Rubric:**

- **5 (Perfect):** All necessary logical clarifications are made perfectly and correctly. 
- **4 (Minor Issue):** No more than 2 minor clarification was missed. But the logic(variable type/domain, variable dependency, implicit variables, etc) was still obvious from the context.
- **3 (Moderate Issue):** A clear and necessary clarification was missed, and this mistake cause some difficulty in understanding the statement.
- **2 (Major Issue):** Multiple necessary clarifications were missed, leaving the structure ambiguous or logically incomplete in key areas.
- **1 (Critical Failure):** A complete failure to perform necessary logical clarifications.

## Output Format

Your entire output **MUST** be a single, valid JSON object. The structure of this JSON object is defined as follows:

```json
{
  "evaluation": {
    "InformationEquivalency": {
      "issues": "<thinking...>",
      "score": <Integer from 1-5>
    },
    "NoFreeVariables": {
      "issues": "<thinking...>",
      "score": <Integer from 1-5>
    },
    "ConcreteReference": {
      "issues": "<thinking...>",
      "score": <Integer from 1-5>
    },
    "AccurateNodeType": {
      "issues": "<thinking...>",
      "score": <Integer from 1-5>
    },
    "AccurateScoping": {
      "issues": "<thinking...>",
      "score": <Integer from 1-5>
    },
    "LogicalClarification": {
      "issues": "<thinking...>",
      "score": <Integer from 1-5>
    }
  }
}
```

## Examples

### Example 1

**Natural language text:**
"""
If $A \subseteq B$, then $\mathcal{P}(A) \subseteq \mathcal{P}(B)$:

Pf: Let $X \in \mathcal{P}(A)$. By definition of power set, $X \subseteq A$. We have $A \subseteq B$. It follows that $X \subseteq B$. Therefore, $X \in \mathcal{P}(B)$. Hence, every element of $\mathcal{P}(A)$ is also in $\mathcal{P}(B)$, so $\mathcal{P}(A) \subseteq \mathcal{P}(B)$. Qed.
"""

**Structure:**
```json
{
  "structure": [
    {
      "type": "Fix",
      "variable": ["$A$", "$B$"],
      "condition": ["$A \\subseteq B$"],
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

**Evaluation:**
```json
{
  "evaluation": {
    "InformationEquivalency": {
      "issues": "The structure perfectly preserves all the logical steps and reasons provided in the original text. No information has been added or omitted.",
      "score": 5
    },
    "NoFreeVariables": {
      "issues": "The structure correctly uses 'Fix' nodes to introduce and bind variables A, B, and X. There are no free variables at any level of the structure.",
      "score": 5
    },
    "ConcreteReference": {
      "issues": "The source text is direct and does not contain abstract references, so this principle is trivially satisfied.",
      "score": 5
    },
    "AccurateNodeType": {
      "issues": "The node types are perfectly chosen. The use of 'Fix' to handle premises and arbitrary elements, and 'Have' for deductive steps, accurately reflects the logical flow of the proof.",
      "score": 5
    },
    "AccurateScoping": {
      "issues": "The scoping is perfect. Crucially, the final two 'Have' nodes, which summarize the conclusion of the proof, are correctly placed outside the scope of the 'Fix' node for the variable X, as they no longer depend on that specific variable.",
      "score": 5
    },
    "LogicalClarification": {
      "issues": "There is one minor missed clarification. The outermost 'Fix' node introduces variables A and B with the condition '$A \\subseteq B$'. While contextually obvious, it should have been explicitly clarified that A and B are sets, as per the guide's examples.",
      "score": 4
    }
  }
}
```

### Example 2

**Natural language text:**
"""
If there exists $ r > 0 $ such that for $ 0 < |x - x_0| < r $, we have $ g(x) \leq f(x) \leq h(x) $, and $ \lim_{x \to x_0} g(x) = \lim_{x \to x_0} h(x) = A $, then $ \lim_{x \to x_0} f(x) = A $.

**Proof**: For any $ \epsilon > 0 $, since $ \lim_{x \to x_0} h(x) = A $, there exists $ \delta_1 > 0 $ such that for all $ x $ satisfying $ 0 < |x - x_0| < \delta_1 $,

$$
|h(x) - A| < \epsilon \implies h(x) < A + \epsilon.
$$

Since $ \lim_{x \to x_0} g(x) = A $, there exists $ \delta_2 > 0 $ such that for all $ x $ satisfying $ 0 < |x - x_0| < \delta_2 $,

$$
|g(x) - A| < \epsilon \implies A - \epsilon < g(x).
$$

Let $ \delta = \min \{ \delta_1, \delta_2, r \} $. Then for $ 0 < |x - x_0| < \delta $,

$$
A - \epsilon < g(x) \leq f(x) \leq h(x) < A + \epsilon.
$$

Thus, $ \lim_{x \to x_0} f(x) = A $.

**Q.E.D.**
"""

**Structure:**
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
        "r"
      ],
      "condition": [
        "$f, g, h$ are real-valued functions",
        "$x_0, A, r$ are real numbers",
        "$\\lim_{x \\to x_0} g(x) = A$",
        "$\\lim_{x \\to x_0} h(x) = A$",
        "for all $x$ such that $0 < |x - x_0| < r$, we have $g(x) \\leq f(x) \\leq h(x)$"
      ],
      "scope": [
        {
          "type": "Show",
          "proposition": [
            "$\\lim_{x \\to x_0} f(x) = A$"
          ],
          "method": null,
          "scope": [
            {
              "type": "Fix",
              "variable": [
                "$\\epsilon$"
              ],
              "condition": [
                "$\\epsilon > 0$"
              ],
              "scope": [
                {
                  "type": "Obtain",
                  "obtained_variable": [
                    "$\\delta_1$"
                  ],
                  "condition": [
                    "$\\delta_1 > 0$",
                    "for all $x$ satisfying $0 < |x - x_0| < \\delta_1$, $h(x) < A + \\epsilon$"
                  ],
                  "reason": [
                    "$\\lim_{x \\to x_0} h(x) = A$"
                  ]
                },
                {
                  "type": "Obtain",
                  "obtained_variable": [
                    "$\\delta_2$"
                  ],
                  "condition": [
                    "$\\delta_2 > 0$",
                    "for all $x$ satisfying $0 < |x - x_0| < \\delta_2$, $A - \\epsilon < g(x)$"
                  ],
                  "reason": [
                    "$\\lim_{x \\to x_0} g(x) = A$"
                  ]
                },
                {
                  "type": "Define",
                  "term": "$\\delta$",
                  "definition": "$\\delta = \\min \\{ \\delta_1, \\delta_2, r \\}$"
                },
                {
                  "type": "Fix",
                  "variable": [
                    "$x$"
                  ],
                  "condition": [
                    "$0 < |x - x_0| < \\delta$"
                  ],
                  "scope": [
                    {
                      "type": "Have",
                      "claim": [
                        "$A - \\epsilon < g(x) \\leq f(x) \\leq h(x) < A + \\epsilon$"
                      ],
                      "reason": null
                    }
                  ]
                },
                {
                  "type": "Have",
                  "claim": [
                    "$\\lim_{x \\to x_0} f(x) = A$"
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
```

**Evaluation:**
```json
{
  "evaluation": {
    "InformationEquivalency": {
      "issues": "The structure omits the intermediate reasoning step present in the text, namely that `|h(x) - A| < epsilon` implies `h(x) < A + epsilon` (and similarly for `g(x)`). It directly states the conclusion of this implication as the condition in the `Obtain` nodes, thus losing a minor but explicit part of the original argument. This happens for both the `h(x)` and `g(x)` parts of the proof.",
      "score": 3
    },
    "NoFreeVariables": {
      "issues": "All variables used in the structure are properly introduced by a `Fix`, `Obtain`, or `Define` node before use. There are no free variables.",
      "score": 5
    },
    "ConcreteReference": {
      "issues": "The original text does not contain any abstract references, so this principle is trivially satisfied.",
      "score": 5
    },
    "AccurateNodeType": {
      "issues": "The node types (`Fix`, `Show`, `Obtain`, `Define`, `Have`) are all used correctly and accurately reflect the semantic intent of each step in the proof (e.g., introducing universal quantifiers, stating goals, introducing existential quantifiers, making assertions).",
      "score": 5
    },
    "AccurateScoping": {
      "issues": "There are two major scoping errors. First, the variable `r` is incorrectly placed in the top-level `Fix` node. The theorem statement specifies 'there exists `r > 0`', but the structure models it as 'for all `r`', which fundamentally changes the premise. This is a critical error in quantifier representation. Second, the final conclusion `lim f(x) = A` is incorrectly placed inside the scope of `Fix epsilon`, even though the conclusion no longer depends on the specific `epsilon` chosen for the proof.",
      "score": 2
    },
    "LogicalClarification": {
      "issues": "The structure correctly applies this principle by adding the types for the variables in the top-level `Fix` node (e.g., '$f, g, h$ are real-valued functions'), which is a necessary clarification not explicitly stated line-by-line in the original text. No other clarifications were necessary.",
      "score": 5
    }
  }
}
```

### Example 3

**Natural language text:**
"""
Prove that there exist infinitely many positive integers $n$ such that $n^2 + 1$ has a prime divisor greater than $2n + \sqrt{10n}$.

Pf.

Let $p \equiv 1 \pmod{8}$ be a prime. The congruence $x^2 \equiv -1 \pmod{p}$ has two solutions in $[1, p-1]$ whose sum is $p$. If $n$ is the smaller one of them then $p$ divides $n^2 + 1$ and $n \leq (p-1)/2$. We show that $p > 2n + \sqrt{10n}$.

Let $n = (p-1)/2 - \ell$ where $\ell \geq 0$. Then $n^2 \equiv -1 \pmod{p}$ gives

$$
\left(\frac{p-1}{2} - \ell\right)^2 \equiv -1 \pmod{p}
$$

or

$$
(2\ell + 1)^2 + 4 \equiv 0 \pmod{p}.
$$

Thus $(2\ell + 1)^2 + 4 = rp$ for some $r \geq 0$. As $(2\ell + 1)^2 \equiv 1 \pmod{8} \equiv p \pmod{8}$, we have $r \equiv 5 \pmod{8}$, so that $r \geq 5$. Hence $(2\ell + 1)^2 + 4 \geq 5p$, implying $\ell \geq (\sqrt{5p - 4} - 1)/2$. Set $\sqrt{5p - 4} = u$ for clarity; then $\ell \geq (u - 1)/2$. Therefore

$$
n = \frac{p-1}{2} - \ell \leq \frac{1}{2} (p - u).
$$

Combined with $p = (u^2 + 4)/5$, this leads to $u^2 - 5u - 10n + 4 \geq 0$. Solving this quadratic inequality with respect to $u \geq 0$ gives $u \geq (5 + \sqrt{40n + 9})/2$. So the estimate $n \leq (p - u)/2$ leads to

$$
p \geq 2n + u \geq 2n + \frac{1}{2}(5 + \sqrt{40n + 9}) > 2n + \sqrt{10n}.
$$

Since there are infinitely many primes of the form $8k + 1$, it follows easily that there are also infinitely many $n$ with the stated property.
"""

**Structure:**
```json
{
  "structure": [
    {
      "type": "Show",
      "proposition": [
        "There exist infinitely many positive integers $n$ such that $n^2 + 1$ has a prime divisor greater than $2n + \\sqrt{10n}$."
      ],
      "method": null,
      "scope": [
        {
          "type": "Fix",
          "variable": [
            "$p$"
          ],
          "condition": [
            "$p$ is a prime",
            "$p \\equiv 1 \\pmod{8}$"
          ],
          "scope": [
            {
              "type": "Obtain",
              "obtained_variable": [
                "$n$"
              ],
              "condition": [
                "$n$ is the smaller solution in $[1, p-1]$ to the congruence $x^2 \\equiv -1 \\pmod{p}$",
                "$p$ divides $n^2 + 1$",
                "$n \\leq (p-1)/2$"
              ],
              "reason": null
            },
            {
              "type": "Show",
              "proposition": [
                "$p > 2n + \\sqrt{10n}$"
              ],
              "method": null,
              "scope": [
                {
                  "type": "Define",
                  "term": "$\\ell$",
                  "definition": "$\\ell = (p-1)/2 - n$"
                },
                {
                  "type": "Have",
                  "claim": [
                    "$\\ell \\geq 0$"
                  ],
                  "reason": [
                    "$n \\leq (p-1)/2$"
                  ]
                },
                {
                  "type": "Obtain",
                  "obtained_variable": [
                    "$r$"
                  ],
                  "condition": [
                    "$r \\geq 0$",
                    "$(2\\ell + 1)^2 + 4 = rp$"
                  ],
                  "reason": [
                    "From $n^2 \\equiv -1 \\pmod{p}$ and the definition of $\\ell$, we have $(2\\ell + 1)^2 + 4 \\equiv 0 \\pmod{p}$"
                  ]
                },
                {
                  "type": "Have",
                  "claim": [
                    "$r \\equiv 5 \\pmod{8}$",
                    "$r \\geq 5$"
                  ],
                  "reason": [
                    "$(2\\ell + 1)^2 \\equiv 1 \\pmod{8}$",
                    "$p \\equiv 1 \\pmod{8}$",
                    "$(2\\ell + 1)^2 + 4 = rp$"
                  ]
                },
                {
                  "type": "Have",
                  "claim": [
                    "$(2\\ell + 1)^2 + 4 \\geq 5p$",
                    "$\\ell \\geq (\\sqrt{5p - 4} - 1)/2$"
                  ],
                  "reason": [
                    "$r \\geq 5$"
                  ]
                },
                {
                  "type": "Define",
                  "term": "$u$",
                  "definition": "$u = \\sqrt{5p - 4}$"
                },
                {
                  "type": "Have",
                  "claim": [
                    "$\\ell \\geq (u - 1)/2$"
                  ],
                  "reason": null
                },
                {
                  "type": "CalculationChain",
                  "initial_expression": [
                    "$n$"
                  ],
                  "step": [
                    {
                      "operator": "=",
                      "expression": [
                        "\\frac{p-1}{2} - \\ell"
                      ],
                      "reason": null
                    },
                    {
                      "operator": "\\leq",
                      "expression": [
                        "\\frac{1}{2} (p - u)"
                      ],
                      "reason": null
                    }
                  ]
                },
                {
                  "type": "Have",
                  "claim": [
                    "$u^2 - 5u - 10n + 4 \\geq 0$"
                  ],
                  "reason": [
                    "Combined with $p = (u^2 + 4)/5$"
                  ]
                },
                {
                  "type": "Have",
                  "claim": [
                    "$u \\geq (5 + \\sqrt{40n + 9})/2$"
                  ],
                  "reason": [
                    "Solving the quadratic inequality $u^2 - 5u - 10n + 4 \\geq 0$ with respect to $u \\geq 0$"
                  ]
                },
                {
                  "type": "CalculationChain",
                  "initial_expression": [
                    "$p$"
                  ],
                  "step": [
                    {
                      "operator": "\\geq",
                      "expression": [
                        "$2n + u$"
                      ],
                      "reason": [
                        "the estimate $n \\leq (p - u)/2$"
                      ]
                    },
                    {
                      "operator": "\\geq",
                      "expression": [
                        "$2n + \\frac{1}{2}(5 + \\sqrt{40n + 9})$"
                      ],
                      "reason": [
                        "$u \\geq (5 + \\sqrt{40n + 9})/2$"
                      ]
                    },
                    {
                      "operator": ">",
                      "expression": [
                        "$2n + \\sqrt{10n}$"
                      ],
                      "reason": null
                    }
                  ]
                }
              ]
            },
            {
              "type": "Have",
              "claim": [
                "there are also infinitely many $n$ with the stated property"
              ],
              "reason": [
                "there are infinitely many primes of the form $8k + 1$"
              ]
            }
          ]
        }
      ]
    }
  ]
}
```

**Evaluation:**
```json
{
    "evaluation": {
        "InformationEquivalency": {
            "issues": "There are two instances of over-flattening the logical structure. First, the `Obtain` node for `r` collapses the derivation of `(2l+1)^2+4≡0(mod p)` into its `reason` field, instead of presenting it as a preceding `Have` node. Second, the `Have` node for `r >= 5` incorrectly lists `r ≡ 5 (mod 8)` as a parallel conclusion, when it should be a separate, preceding `Have` node, as the former is a direct consequence of the latter.",
            "score": 3
        },
        "NoFreeVariables": {
            "issues": "All variables (`p`, `n`, `l`, `r`, `u`) are properly introduced via `Fix`, `Obtain`, or `Define` nodes before they are used. There are no free variables at any level of the structure.",
            "score": 5
        },
        "ConcreteReference": {
            "issues": "The original text does not contain abstract references, so this principle is trivially satisfied.",
            "score": 5
        },
        "AccurateNodeType": {
            "issues": "The choice of nodes is generally correct. However, there is a moderate error in the first `Obtain` node for `n`. The text states 'If n is..., then p divides... and n <= ...'. This causal flow is not preserved. The structure incorrectly combines the definition of `n` and its consequences into a single `Obtain` node's `condition` field, which is a form of over-flattening.",
            "score": 3
        },
        "AccurateScoping": {
            "issues": "There is a major scoping error. The final `Have` node, 'there are also infinitely many n with the stated property', is a global conclusion that generalizes from the argument about a single `p`. It should be placed **outside** the `Fix {p}` scope, as its reasoning no longer depends on that specific, fixed prime. Placing it inside the `Fix {p}` scope is a fundamental misrepresentation of the proof's logical hierarchy.",
            "score": 2
        },
        "LogicalClarification": {
            "issues": "The structure does a good job of clarifying the logic in some places (e.g., separating the definition of `l` and the claim `l >= 0`). However, it misses the crucial clarification needed for the final `Have` node. It should have added a concrete reference for 'the stated property' by using the 'Define-and-Refer' pattern, which was not done.",
            "score": 3
        }
    }
}
```

## Your Task

**Natural language text:**
"""
{Natural_Language_Text}
"""

**Structure:**
```json
{Json_Structure}
```

**Evaluation:**
(you don't need to output "```json" and "```". You simply output the json content.)