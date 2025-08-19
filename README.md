# Math Proof Structure Extraction  

## Step 1. Node Type Identification  

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

## Step 2. Scope Identification  

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