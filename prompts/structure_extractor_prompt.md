You need to refine the top level structure in the first 'place_holder' node of the given JSON mathematical structure. Please complete the task according to the definition of the mathematical structure (which has been clearly defined in your system prompt).

# Requirements

You are given as an input: a structure that has been partially extracted but contains place_holders. 

Your task is to refine the structure at the first occurrence of a place_holder.

Note, the work you need to do only requires adding 2~5 nodes. If you believe that refining the entire content of the place_holder would not exceed 2~5 nodes, then please refine it entirely. Otherwise, please only refine the topmost 2~5 nodes, and still represent the remaining content with place_holder(and copy the corresponding natural language texts in the content of each place_holder node).

You need to think in the thinking field first, and then output the result in the structure field.

# JSON Format

{Json_Format}

# Examples

## Example 1

Input:

{
  "structure": [
    {
      "type": "place_holder",
      "content": "If $A \\subseteq B$, then $\\mathcal{P}(A) \\subseteq \\mathcal{P}(B)$:\n\nPf: Let $X \\in \\mathcal{P}(A)$. By definition of power set, $X \\subseteq A$. Since $A \\subseteq B$, it follows that $X \\subseteq B$. Therefore, $X \\in \\mathcal{P}(B)$. Hence, every element of $\\mathcal{P}(A)$ is also in $\\mathcal{P}(B)$, so $\\mathcal{P}(A) \\subseteq \\mathcal{P}(B)$. Qed."
    }
  ]
}

Output:

{
  "thinking": "The structure to be extracted is currently a single placeholder, and I need to parse its top-level structure. This is a proof text, and the proof goal is If $A \\subseteq B$, then $\\mathcal{P}(A) \\subseteq \\mathcal{P}(B)$. Here, A and B are free variables, so they need to be extracted at the outermost level using a Fix node, and then within the scope of Fix, use a Show node to represent the proof goal. The internal process of Show can be marked with a placeholder for this round.",
  "structure": [
    {
      "type": "fix",
      "var_list": ["A", "B"],
      "such_that": "$A \\subseteq B$",
      "scope": [
        {
          "type": "show",
          "content": "$\\mathcal{P}(A) \\subseteq \\mathcal{P}(B)$",
          "scope": [
            {
              "type": "place_holder",
              "content": "Let $X \\in \\mathcal{P}(A)$. By definition of power set, $X \\subseteq A$. Since $A \\subseteq B$, it follows that $X \\subseteq B$. Therefore, $X \\in \\mathcal{P}(B)$. Hence, every element of $\\mathcal{P}(A)$ is also in $\\mathcal{P}(B)$, so $\\mathcal{P}(A) \\subseteq \\mathcal{P}(B)$. Qed."
            }
          ]
        }
      ]
    }
  ]
}

## Example 2

Input:

{
  "structure": [
    {
      "type": "fix",
      "var_list": ["A", "B"],
      "such_that": "$A \\subseteq B$",
      "scope": [
        {
          "type": "show",
          "content": "$\\mathcal{P}(A) \\subseteq \\mathcal{P}(B)$",
          "scope": [
            {
              "type": "place_holder",
              "content": "Let $X \\in \\mathcal{P}(A)$. By definition of power set, $X \\subseteq A$. Since $A \\subseteq B$, it follows that $X \\subseteq B$. Therefore, $X \\in \\mathcal{P}(B)$. Hence, every element of $\\mathcal{P}(A)$ is also in $\\mathcal{P}(B)$, so $\\mathcal{P}(A) \\subseteq \\mathcal{P}(B)$. Qed."
            }
          ]
        }
      ]
    }
  ]
}

Output:

{
  "thinking": "The structure to be refined has already extracted the variables A, B, and the proof goal. I will next refine the main body of the proof. The proof primarily introduces a variable X to complete the discussion. It then draws two conclusions: Hence, every element of $\mathcal{P}(A)$ is also in $\mathcal{P}(B)$ and so $\mathcal{P}(A) \subseteq \mathcal{P}(B)$. Therefore, the overall structure consists of a Fix node for introducing X and two Have nodes. In this round, the placeholder inside the Fix node will be retained.",
  "structure": [
    {
      "type": "fix",
      "var_list": ["A", "B"],
      "such_that": "$A \\subseteq B$",
      "scope": [
        {
          "type": "show",
          "content": "$\\mathcal{P}(A) \\subseteq \\mathcal{P}(B)$",
          "scope": [
            {
              "type": "fix",
              "var_list": ["X"],
              "such_that": "$X \\in \\mathcal{P}(A)$",
              "scope": [
                {
                  "type": "place_holder",
                  "content": "By definition of power set, $X \\subseteq A$. Since $A \\subseteq B$, it follows that $X \\subseteq B$. Therefore, $X \\in \\mathcal{P}(B)$."
                }
              ]
            },
            {
              "type": "have",
              "content": "every element of $\\mathcal{P}(A)$ is also in $\\mathcal{P}(B)$"
            },
            {
              "type": "have",
              "content": "$\\mathcal{P}(A) \\subseteq \\mathcal{P}(B)$"
            }
          ]
        }
      ]
    }
  ]
}

## Example 3

Input:

{
  "structure": [
    {
      "type": "fix",
      "var_list": ["A", "B"],
      "such_that": "$A \\subseteq B$",
      "scope": [
        {
          "type": "show",
          "content": "$\\mathcal{P}(A) \\subseteq \\mathcal{P}(B)$",
          "scope": [
            {
              "type": "fix",
              "var_list": ["X"],
              "such_that": "$X \\in \\mathcal{P}(A)$",
              "scope": [
                {
                  "type": "place_holder",
                  "content": "By definition of power set, $X \\subseteq A$. Since $A \\subseteq B$, it follows that $X \\subseteq B$. Therefore, $X \\in \\mathcal{P}(B)$."
                }
              ]
            },
            {
              "type": "have",
              "content": "every element of $\\mathcal{P}(A)$ is also in $\\mathcal{P}(B)$"
            },
            {
              "type": "have",
              "content": "$\\mathcal{P}(A) \\subseteq \\mathcal{P}(B)$"
            }
          ]
        }
      ]
    }
  ]
}

Output:

{
  "thinking": "The given structure has mostly completed the extraction, and in the place_holders that need refinement, there are mainly three assertions, so writing three Have nodes is sufficient. Among them, the first assertion, "By definition of power set, $X \\subseteq A$", is a Have node with a reasoning basis. The second assertion, "Since $A \\subseteq B$, it follows that $X \\subseteq B$.", is also a Have node with a reasoning basis. The third assertion is "Therefore, $X \\in \\mathcal{P}(B)$" with its reasoning basis. At this point, all place_holders have been filled.",
  "structure": [
    {
      "type": "fix",
      "var_list": ["A", "B"],
      "such_that": "$A \\subseteq B$",
      "scope": [
        {
          "type": "show",
          "content": "$\\mathcal{P}(A) \\subseteq \\mathcal{P}(B)$",
          "scope": [
            {
              "type": "fix",
              "var_list": ["X"],
              "such_that": "$X \\in \\mathcal{P}(A)$",
              "scope": [
                {
                  "type": "have",
                  "content": "$X \\subseteq A$",
                  "by": "definition of power set"
                },
                {
                  "type": "have",
                  "content": "$X \\subseteq B$",
                  "by": "$A \\subseteq B$"
                },
                {
                  "type": "have",
                  "content": "$X \\in \\mathcal{P}(B)$"
                }
              ]
            },
            {
              "type": "have",
              "content": "every element of $\\mathcal{P}(A)$ is also in $\\mathcal{P}(B)$"
            },
            {
              "type": "have",
              "content": "$\\mathcal{P}(A) \\subseteq \\mathcal{P}(B)$"
            }
          ]
        }
      ]
    }
  ]
}

## Your Task

Input:

{Task_Input}

Output: