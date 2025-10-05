2.19 *linear dependence lemma*

Suppose $v_1, ..., v_m$ is a linearly dependent list in $V$. Then there exists $k \in \{1, 2, ..., m\}$ such that

$$v_k \in \operatorname{span}(v_1, ..., v_{k-1}).$$

Furthermore, if $k$ satisfies the condition above and the $k^{th}$ term is removed from $v_1, ..., v_m$, then the span of the remaining list equals $\operatorname{span}(v_1, ..., v_m)$.

**Proof** Because the list $v_1, ..., v_m$ is linearly dependent, there exist numbers $a_1, ..., a_m \in \mathbf{F}$, not all 0, such that

$$a_1 v_1 + \cdots + a_m v_m = 0.$$

Let $k$ be the largest element of $\{1, ..., m\}$ such that $a_k \neq 0$. Then

$$v_k = -\frac{a_1}{a_k} v_1 - \cdots - \frac{a_{k-1}}{a_k} v_{k-1},$$

which proves that $v_k \in \operatorname{span}(v_1, ..., v_{k-1})$, as desired.

Now suppose $k$ is any element of $\{1, ..., m\}$ such that $v_k \in \operatorname{span}(v_1, ..., v_{k-1})$. Let $b_1, ..., b_{k-1} \in \mathbf{F}$ be such that

2.20  
$$v_k = b_1 v_1 + \cdots + b_{k-1} v_{k-1}.$$

Suppose $u \in \operatorname{span}(v_1, ..., v_m)$. Then there exist $c_1, ..., c_m \in \mathbf{F}$ such that

$$u = c_1 v_1 + \cdots + c_m v_m.$$

In the equation above, we can replace $v_k$ with the right side of 2.20, which shows that $u$ is in the span of the list obtained by removing the $k^{th}$ term from $v_1, ..., v_m$. Thus removing the $k^{th}$ term of the list $v_1, ..., v_m$ does not change the span of the list.

# Structure

```json
{
  "structure": [
    {
      "type": "Hint",
      "text": "2.19 *linear dependence lemma*"
    },
    {
      "type": "Fix",
      "variable": [
        "$V$",
        "$m$",
        "$v_1, ..., v_m$"
      ],
      "condition": [
        "$V$ is a vector space",
        "$m \\in \\mathbb{N}^*$",
        "$v_1, ..., v_m$ is a list of vectors in $V$",
        "$v_1, ..., v_m$ is linearly dependent"
      ],
      "scope": [
        {
          "type": "Show",
          "proposition": [
            "$\\exists k \\in \\{1, ..., m\\}$ such that $v_k \\in \\operatorname{span}(v_1, ..., v_{k-1})$",
            "if $k$ satisfies $v_k \\in \\operatorname{span}(v_1, ..., v_{k-1})$ and the $k^{th}$ term is removed from $v_1, ..., v_m$, then the span of the remaining list equals $\\operatorname{span}(v_1, ..., v_m)$"
          ],
          "method": null,
          "scope": [
            {
              "type": "Show",
              "proposition": [
                "$\\exists k \\in \\{1, ..., m\\}$ such that $v_k \\in \\operatorname{span}(v_1, ..., v_{k-1})$"
              ],
              "method": null,
              "scope": [
                {
                  "type": "Obtain",
                  "obtained_variable": [
                    "$a_1, ..., a_m$"
                  ],
                  "condition": [
                    "$a_1, ..., a_m \\in \\mathbf{F}$",
                    "not all $a_i$ are 0",
                    "$a_1 v_1 + \\cdots + a_m v_m = 0$"
                  ],
                  "reason": [
                    "the list $v_1, ..., v_m$ is linearly dependent"
                  ]
                },
                {
                  "type": "Define",
                  "term": "$k$",
                  "definition": "$k$ is the largest element of $\\{1, ..., m\\}$ such that $a_k \\neq 0$"
                },
                {
                  "type": "Have",
                  "claim": [
                    "$v_k = -\\frac{a_1}{a_k} v_1 - \\cdots - \\frac{a_{k-1}}{a_k} v_{k-1}$"
                  ],
                  "reason": null
                },
                {
                  "type": "Have",
                  "claim": [
                    "$v_k \\in \\operatorname{span}(v_1, ..., v_{k-1})$"
                  ],
                  "reason": null
                }
              ]
            },
            {
              "type": "Show",
              "proposition": [
                "if $k$ satisfies $v_k \\in \\operatorname{span}(v_1, ..., v_{k-1})$ and the $k^{th}$ term is removed from $v_1, ..., v_m$, then the span of the remaining list equals $\\operatorname{span}(v_1, ..., v_m)$"
              ],
              "method": null,
              "scope": [
                {
                  "type": "Fix",
                  "variable": [
                    "$k$"
                  ],
                  "condition": [
                    "$k \\in \\{1, ..., m\\}$",
                    "$v_k \\in \\operatorname{span}(v_1, ..., v_{k-1})$"
                  ],
                  "scope": [
                    {
                      "type": "Obtain",
                      "obtained_variable": [
                        "$b_1, ..., b_{k-1}$"
                      ],
                      "condition": [
                        "$b_1, ..., b_{k-1} \\in \\mathbf{F}$",
                        "$v_k = b_1 v_1 + \\cdots + b_{k-1} v_{k-1}$"
                      ],
                      "reason": null
                    },
                    {
                      "type": "Fix",
                      "variable": [
                        "$u$"
                      ],
                      "condition": [
                        "$u \\in \\operatorname{span}(v_1, ..., v_m)$"
                      ],
                      "scope": [
                        {
                          "type": "Obtain",
                          "obtained_variable": [
                            "$c_1, ..., c_m$"
                          ],
                          "condition": [
                            "$c_1, ..., c_m \\in \\mathbf{F}$",
                            "$u = c_1 v_1 + \\cdots + c_m v_m$"
                          ],
                          "reason": null
                        },
                        {
                          "type": "Have",
                          "claim": [
                            "$u \\in \\operatorname{span}(v_1, ..., v_{k-1}, v_{k+1}, ..., v_m)$"
                          ],
                          "reason": [
                            "replace $v_k$ with $b_1 v_1 + \\cdots + b_{k-1} v_{k-1}$ in $u = c_1 v_1 + \\cdots + c_m v_m$"
                          ]
                        }
                      ]
                    },
                    {
                      "type": "Have",
                      "claim": [
                        "$\\operatorname{span}(v_1, ..., v_m) = \\operatorname{span}(v_1, ..., v_{k-1}, v_{k+1}, ..., v_m)$"
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

