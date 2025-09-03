# Math Proof Structure Extraction  

## Step 1. Cut Scentences

Text in the informal_proof.md will be cut into sentences using a one-shot LLM call.

## Step 2. Rewrite

Each sentences will be rewrite by a LLM with thinking tokens, adding missing informations, quantifiers and so on.

## Step 3. Node Type Identification  

The structure of an arbitrary math proof is first regarded as a typed sequence of nodes.  

We define 10 node types in total, as follows:  

- **[Show: "P"]** – Next, we prove proposition P.  
- **[Assume: "P"]** – Assume proposition P holds.  
- **[Have: "P" by "Q"]** – Based on a list of "theorems/proven propositions/natural language hints" Q, we conclude that proposition P holds.  
- **[Fix: {var_list} such that "P"]** – Fix a variable list {var_list} such that these variables satisfy proposition P.  
- **[SufficeToProve: "P" by "Q"]** – To prove the current goal, it suffices to prove proposition P, with the justification Q.  
- **[ToHave: "P"]** – To ensure that... holds, used in conjunction with OnlyNeeds (P can be a list).  
- **[OnlyNeeds: "P" by "Q"]** – It only requires... to hold, following ToHave (P and Q can be lists).  
- **[Find: {var_list} such that "P"]** – Find a variable list {var_list} that satisfies proposition P (P can be a list).  
- **[Define: "A" as "B"]** – Define a "symbol/concept" A, whose meaning is B (A and B cannot be lists).  
- **[Hint: "string"]** – A natural language annotation.  

For a given natural language mathematical text (stored in `display/informal_proof.md`), we input it along with a prompt into a LLM. The model outputs a structured JSON result (located in `output_node_type.json` in the `display` folder). This result is parsed and printed in a pretty-printed format in `pretty_output_node_type.md` in the `display` folder.  

## Step 4. Scope Identification  

Based on the typed node sequence obtained in Step 1, we next determine the "scope" of each node.  

The nodes **Show, Assume, Fix, ToHave, Find** have scopes. In the pretty-printed output, we use curly braces to denote scopes.  

- The scope of **Show P** contains the complete proof of proposition P.  
- The scope of **Assume P** contains the proof passage that implicitly assumes P.  
- The scope of **Fix** is similar to **Assume**, containing the proof passage where the variables introduced by **Fix** are used.  
- The scope of **ToHave** includes all subsequent backward reasoning (**OnlyNeeds**).  
- The scope of **Find** covers the entire solving process.  

During Step 2, the pretty-printed node sequence from Step 1(node_type.json) is input along with another prompt into the LLM, which outputs a structured result with scope(scope.json). This result is parsed and printed in a pretty-printed format(scope.md).

# Current Version

The current version of this project uses OpenAI-o3 as the LLM.

# Test Log

Test0819: 40 proofs from Analysis and IMO. (see `data_test`)

# Example

## Example 1

### Original Text

假设 $f(x)$ 在 $[0,1]$ 上连续，证明: $\lim_{h \to 0^+} \int_0^1 \frac{h}{h^2 + x^2} f(x) dx = \frac{\pi}{2} f(0)$

Pf:

$\int_0^1 \frac{h}{h^2 + x^2} f(x) dx = \int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx + \int_{h^{1/4}}^1 \frac{hf(x)}{h^2 + x^2} dx$

令$I_1 = \int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx$, $I_2 = \int_{h^{1/4}}^1 \frac{hf(x)}{h^2 + x^2} dx$

其中

$I_1 = \int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx = f(\xi) \int_0^{h^{1/4}} \frac{h}{h^2 + x^2} dx \quad (0 \leq \xi \leq h^{1/4})$

$= f(\xi) \arctan \frac{x}{h} \Big|_0^{h^{1/4}} = f(\xi) \arctan \frac{1}{h^{3/4}} \to f(0)\dfrac{\pi}{2} \quad (h \to 0^+)$

$|I_2| = \left| \int_{h^{1/4}}^1 \frac{h}{h^2 + x^2} f(x) dx \right| \leq M \int_{h^{1/4}}^1 \frac{h}{h^2 + x^2} dx(\quad |f(x)|\leq M\quad)$

$= M \left( \arctan \frac{1}{h} - \arctan \frac{1}{h^{3/4}} \right) \to 0 \quad (h \to 0^+)$

因此$h\to 0^+$时$I_1+I_2\to f(0)\dfrac{\pi}{2}$

Qed.

### After Step 1 Cut

[Sentence 1] 假设 $f(x)$ 在 $[0,1]$ 上连续
[Sentence 2] 证明: $\lim_{h \to 0^+} \int_0^1 \frac{h}{h^2 + x^2} f(x) dx = \frac{\pi}{2} f(0)$
[Sentence 3] $\int_0^1 \frac{h}{h^2 + x^2} f(x) dx = \int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx + \int_{h^{1/4}}^1 \frac{hf(x)}{h^2 + x^2} dx$
[Sentence 4] 令$I_1 = \int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx$, $I_2 = \int_{h^{1/4}}^1 \frac{hf(x)}{h^2 + x^2} dx$
[Sentence 5] 其中 $I_1 = \int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx = f(\xi) \int_0^{h^{1/4}} \frac{h}{h^2 + x^2} dx \quad (0 \leq \xi \leq h^{1/4})$
[Sentence 6] $= f(\xi) \arctan \frac{x}{h} \Big|_0^{h^{1/4}} = f(\xi) \arctan \frac{1}{h^{3/4}} \to f(0)\dfrac{\pi}{2} \quad (h \to 0^+)$
[Sentence 7] $|I_2| = \left| \int_{h^{1/4}}^1 \frac{h}{h^2 + x^2} f(x) dx \right| \leq M \int_{h^{1/4}}^1 \frac{h}{h^2 + x^2} dx(\quad |f(x)|\leq M\quad)$
[Sentence 8] $= M \left( \arctan \frac{1}{h} - \arctan \frac{1}{h^{3/4}} \right) \to 0 \quad (h \to 0^+)$
[Sentence 9] 因此$h\to 0^+$时$I_1+I_2\to f(0)\dfrac{\pi}{2}$

### After Step 2 Rewrite

[Sentence 1] $\forall f:\R \to \R$，假设$f$在$[0,1]$上连续
[Sentence 2] 证明: $\lim_{h \to 0^+} \int_0^1 \frac{h}{h^2 + x^2} f(x) dx = \frac{\pi}{2} f(0)$
[Sentence 3] ∀h ∈ (0,1/2)，$\int_0^1 \frac{h}{h^2 + x^2} f(x) dx = \int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx + \int_{h^{1/4}}^1 \frac{hf(x)}{h^2 + x^2} dx$
[Sentence 4] 令$I_1 = \int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx$
[Sentence 5] 令$I_2 = \int_{h^{1/4}}^1 \frac{hf(x)}{h^2 + x^2} dx$
[Sentence 6] 其中 $I_1 = \int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx$
[Sentence 7] $\exists \xi \in [0, h^{1/4}]$，$\int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx = f(\xi) \int_0^{h^{1/4}} \frac{h}{h^2 + x^2} dx$
[Sentence 8] $f(\xi) \int_0^{h^{1/4}} \frac{h}{h^2 + x^2} dx = f(\xi) \arctan \frac{x}{h} \Big|_0^{h^{1/4}} = f(\xi) \arctan \frac{1}{h^{3/4}}$
[Sentence 9] $\lim\limits_{h \to 0^+} f(\xi) \arctan \frac{1}{h^{3/4}} = f(0)\dfrac{\pi}{2}$
[Sentence 10] ∃M ∈ ℝ, ∀x ∈ [0,1], |f(x)| ≤ M，并且∀h ∈ (0,1/2)，$|I_2| = \left| \int_{h^{1/4}}^1 \frac{h}{h^2 + x^2} f(x) dx \right| \leq M \int_{h^{1/4}}^1 \frac{h}{h^2 + x^2} dx$
[Sentence 11] $M \int_{h^{1/4}}^1 \frac{h}{h^2 + x^2} dx = M \left( \arctan \frac{1}{h} - \arctan \frac{1}{h^{3/4}} \right)$
[Sentence 12] $\lim\limits_{h \to 0^+} M \left( \arctan \frac{1}{h} - \arctan \frac{1}{h^{3/4}} \right) = 0$
[Sentence 13] 因此，$\lim\limits_{h \to 0^+} (I_1 + I_2) = f(0)\dfrac{\pi}{2}$