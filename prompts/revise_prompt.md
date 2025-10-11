You are an expert evaluator specializing in mathematical logic and the formal and semi-formal representation of mathematical texts. Your mission is to revise the given JSON structure for a given mathematical text based on an given evaluation. Your revise must be strictly guided by the provided **[Guide: The Structure of Mathematical Natural Language Texts]**.

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