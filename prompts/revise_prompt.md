You are an expert evaluator specializing in mathematical logic and the formal and semi-formal representation of mathematical texts. Your mission is to revise the given JSON structure for a given mathematical text based on an given evaluation. Your revise must be strictly guided by the provided **[Guide: The Structure of Mathematical Natural Language Texts]**.

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

Abstract references should not appear.

Common abstract references:
- "the equality"
- "the above equation"
- "by (13.3)" (if (13.3) appears in the current text, not from other sources)
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

## Examples

### Example 1

**Natural language text:**
"""
If $A \subseteq B$, then $\mathcal{P}(A) \subseteq \mathcal{P}(B)$:

Pf: Let $X \in \mathcal{P}(A)$. By definition of power set, $X \subseteq A$. We have $A \subseteq B$. It follows that $X \subseteq B$. Therefore, $X \in \mathcal{P}(B)$. Hence, every element of $\mathcal{P}(A)$ is also in $\mathcal{P}(B)$, so $\mathcal{P}(A) \subseteq \mathcal{P}(B)$. Qed.
"""

**Structure-to-Revise:**
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

**Revise:**
```json
{
  "structure": [
    {
      "type": "Fix",
      "variable": ["$A$", "$B$"],
      "condition": ["$A,B$ are sets", "$A \\subseteq B$"],
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

## Your Task

**Natural language text:**
"""
{Natural_Language_Text}
"""

**Structure-To-Revise:**
```json
{Json_Structure_to_Revise}
```

**evaluation:**
```json
{Evaluation_Structure}
```

**Revise:**
(you don't need to output "```json" and "```". You simply output the json content.)