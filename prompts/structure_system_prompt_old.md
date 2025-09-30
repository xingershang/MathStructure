# The Structure of Mathematical Natural Language Texts

## Definition of Structure

### Node Types

The basic units of the structure of mathematical natural language are 11 different types of nodes. They are introduced sequentially below:

#### Show Node: `[Show] {P} using {Q}`

- Meaning: We will now prove proposition P, with the hint for the proof method being Q. P can be a list.
- Explanation: The Show node corresponds to the overall proof goal, subgoals in a proof text, sub-proof goals in general text, etc.
- Example 1: "Below we prove that the set $S$ is not empty" - `[Show] {The set $S$ is not empty} using {}`
- Example 2: "We use induction to prove $\forall n\in \N,f(n)\geq g(n)$" - `[Show] {$\forall n\in \N,f(n)\geq g(n)$} using {induction}`
- Example 3: "We prove $k\neq 0$. By contradiction, ..." - `[Show] {$k \neq 0$} using {contradiction}`

#### Assume Node: `[Assume] {P}`

-   Meaning: Assume proposition P holds. P can be a list.
-   Explanation: The premises of the overall proof goal, temporary assumptions introduced during the proof, or the conditions for each case in a "case analysis" all correspond to Assume nodes. (For situations introducing a new variable, although natural language might use the word "let", it generally needs to be identified as a Fix node, see Example 3. Care must be taken to distinguish between Assume and Fix nodes.)
-   Example 1: "Assume $a>0$" ($a$ has already been introduced above) - `[Assume] {$a>0$}`
-   Example 2: "Case 1: $n$ is even" - `[Assume] {$n$ is even}`
-   Example 3: "Let $\varepsilon > 0$" ($\varepsilon$ is a newly introduced variable) - `[Fix] {$\varepsilon$} such that {$\varepsilon > 0$}`

#### Have Node: `[Have] {P} by {Q}`

-   Meaning: Derive assertion P, where the basis for deriving this assertion is Q. Both P and Q can be lists. Q can be empty.
-   Explanation: Q can be a theorem name, a previously proven conclusion, or a natural language hint. If the natural language text does not state a reason, then Q is empty.
-   Example 1: "Therefore, $x>0$" - `[Have] {$x>0$} by {}`
-   Example 2: "By Lemma 1.2, $A$ is a closed set" - `[Have] {$A$ is a closed set} by {Lemma 1.2}`
-   Example 3: "Combining equations (1) and (2), we get $a=c$" - `[Have] {$a=c$} by {equation (1)}; {equation (2)}`

#### Fix Node: `[Fix] {var_list} such that {P}`

-   Meaning: Fix the variable list `var_list`, these variables satisfy proposition P. var_list is a list of variables; P can be a single proposition or a list of propositions.
-   Explanation: The Fix node introduces one or a list of new variables satisfying specific conditions. It corresponds to expressions in natural language like "for any ...", "for all ...", "given ...", "let ...", etc. Logically, it is equivalent to the universal quantifier (`∀`). Note the distinction between Fix and Assume nodes.
-   Example 1: "For any $\varepsilon > 0$" - `[Fix] {$\varepsilon$} such that {$\varepsilon > 0$}`
-   Example 2: "Let $x, y$ be arbitrary real numbers" - `[Fix] {$x$, $y$} such that {$x, y$ are real numbers}`

#### Obtain Node: `[Obtain] {var_list} such that {P} by {Q}`

-   Meaning: Derive the existence of the variable list `var_list`, these variables satisfy proposition P, and the basis for the existence is Q. var_list is a list of variables; P and Q can both be lists. Q can be empty.
-   Explanation: Logically, the Obtain node corresponds to the existential quantifier (`∃`); it asserts that variables satisfying specific properties exist. The `by` part indicates the source of existence, similar to the Have node; Q can be a theorem name, some already obtained assertion, or a natural language hint.
-   Example 1: "By the Mean Value Theorem, there exists $\xi \in (a,b)$ such that $f'(\xi)=0$" - `[Obtain] {$\xi$} such that {$\xi \in (a,b)$};{$f'(\xi)=0$} by {Mean Value Theorem}`
-   Example 2: "So there exists an integer $k$ such that $n=2k$" - `[Obtain] {$k$} such that {$k$ is an integer};{$n=2k$} by {}`

#### SufficeToProve Node: `[SufficeToProve] {P} by {Q}`

-   Meaning: To prove the current proof goal, it suffices to prove P, with the reason being Q. Both P and Q can be lists. Q can be empty.
-   Explanation: SufficeToProve is a transformation of the current proof goal during the proof process. The current proof goal could be the overall goal of the proof text or some subgoal, depending on the specific meaning of the original text. It corresponds to expressions like "it suffices to prove", "we only need to prove".
-   Example 1: "It suffices to prove $\forall x \in A, x \in B$" - `[SufficeToProve] {$\forall x \in A, x \in B$} by {}`
-   Example 2: "Since $A\subseteq B$, it suffices to prove $\forall x \in B, f(x)=0$" - `[SufficeToProve] {$\forall x \in B, f(x)=0$} by {$A \subseteq B$}`

#### LogicChain Node: `[LogicChain] {P1} {symbol1} {reason1} {P2} {symbol2} {reason2} {P3} ... {Pn}`

-   Meaning: Represents a logical derivation chain. The chain consists of propositions {Pk}, logical symbols {symbolk}, and reasoning reasons {reasonk} alternating. If the natural language does not state a reason, the reason is empty.
-   Explanation: Used to represent long strings of logical derivations in natural language. If all symbols are forward implications (left implies right), then LogicChain is equivalent to a series of Have nodes. However, if the derivation involves backward implications, or a mix of forward, backward, and bidirectional implications, it is generally represented by a LogicChain node.
-   Example 1: "$\begin{aligned}P_1&\iff P_2&(reason1) \\ &\implies P_3&(reason2)\\&\implies P_4\end{aligned}$" - `[LogicChain] {P_1} {<=>} {reason1} {P2} {=>} {reason2} {P3} {=>} {} {P4}`
-   Example 2: "to have $|{x}_{n} - 1| < \varepsilon$, it suffices to have $\frac{1}{n + 1} < \varepsilon$, i.e., $n > \frac{1}{\varepsilon} - 1$. " - `[LogicChain] {$|{x}_{n} - 1| < \varepsilon$} {⇐} {} {$\frac{1}{n + 1} < \varepsilon$} {⇔} {} {$n > \frac{1}{\varepsilon} - 1$}`

#### CalculationChain Node: `[CalculationChain] {E1} {symbol1} {reason1} ... {En}`

- Meaning: Represents a calculation chain. Similar to LogicChain, the chain consists of expressions, relation symbols, and derivation reasons alternating. Reasons can be empty.

- Explanation: Similar to LogicChain, CalculationChain is used to represent consecutive calculation steps, such as long chains of equalities or estimation processes.

- Example 1: "

  $|a_n b_n + \cdots + a_{n+k} b_{n+k}| = |B_n a_n + B_{n+1} (a_{n+1} - a_n) + \cdots + B_{n+k} (a_{n+k} - a_{n+k-1}) + B_{n+k+1} a_{n+k}|$ (Lemma)

  $\leq |B_n a_n| + |B_{n+1} (a_{n+1} - a_n)| + \cdots + |B_{n+k} (a_{n+k} - a_{n+k-1})| + |B_{n+k+1} a_{n+k}|$ (Triangle Inequality for Complex Numbers)

  $\leq M \epsilon + M \epsilon$

  $= 3M \epsilon$"

  `[CalculationChain] {$|a_n b_n + \cdots + a_{n+k} b_{n+k}|$} {$=$} {Lemma} {$|B_n a_n + B_{n+1} (a_{n+1} - a_n) + \cdots + B_{n+k} (a_{n+k} - a_{n+k-1}) + B_{n+k+1} a_{n+k}|$} {$\leq$} {Triangle Inequality for Complex Numbers} {$|B_n a_n| + |B_{n+1} (a_{n+1} - a_n)| + \cdots + |B_{n+k} (a_{n+k} - a_{n+k-1})| + |B_{n+k+1} a_{n+k}|$} {$\leq$} {} {$M \epsilon + M \epsilon$} {$=$} {} {$3M \epsilon$}`

#### Find Node: `[Find] {P} such that {Q}`

-   Meaning: Solve for P that satisfies Q, where P is a variable or expression.
-   Explanation: The Find node is used to represent a "problem-solving" task. For example, tasks like "compute the value of ...", "simplify the expression", "solve the equation ...", or "find all sets satisfying ...". Its purpose is not to "prove" a proposition, but to "find" an object satisfying specific conditions. For tasks like simplification or evaluating an expression, Q is empty.
-   Example 1: "Find the solutions to the equation $x^2 -3x+ 4 = 0$" - `[Find] {$x$} such that {$x^2 - 3x + 4 = 0$}`
-   Example 2: "Below we compute the integral $\int_0^1 x dx$" - `[Find] {$\int_0^1 x dx$} such that {}`

#### Define Node: `[Define] {A} as {B}`

-   Meaning: Define a "variable/symbol/concept" A, whose meaning is B. Neither A nor B can be lists.
-   Explanation: Used to introduce new variables, symbols, or concepts.
-   Example 1: "Let $M = \sup_{x \in S} f(x)$" - `[Define] {$M$} as {$\sup_{x \in S} f(x)$}`
-   Example 2: "We call $G$ an Abelian group if $G$ is a group and its operation is commutative" - `[Define] {$G$ is an Abelian group} as {$G$ is a group and its operation is commutative}`

#### Hint Node: `[Hint] {P}`

-   Meaning: Represents a natural language annotation. P can be any natural language text.
-   Explanation: Natural language texts often contain explanatory, annotative text that does not have specific mathematical meaning. For example, transitional text, author's comments, emphasis on the importance of a conclusion, or an intuitive overview of the upcoming proof steps or calculation steps.
-   Example 1: "Thus we can obtain the answer" - `[Hint] {Thus we can obtain the answer}`
-   Example 2: "The idea of this proof is very clever" - `[Hint] {The idea of this proof is very clever}`
-   Example 3: "Next we use a skillful technique to prove this conclusion; a more natural proof method will be introduced in Chapter 4" - `[Hint] {Next we use a skillful technique to prove this conclusion; a more natural proof method will be introduced in Chapter 4}`

### Scope

The four node types Show, Assume, Fix, and Find have a scope, while the other nodes do not have a scope. For nodes with a scope, their scope contains a substructure (defined identically to the outer structure, and scopes can be nested multiple levels).

The content within the scope of these four nodes is generally:

- The scope of a Show node contains the proof for that proof goal;
- The scope of an Assume node corresponds to the text content that acknowledges the assumption holds;
- The scope of a Fix node contains text content about the newly introduced variables;
- The scope of a Find node is the specific process of solving;

# JSON SCHEMA

In your task, you will need to represent the structure in a pre-defined json format. The definition of the format is as following:

{fill_in_json_schema}

# Schematics

As a schematic, we use the node followed by braces to represent the scope. For example:

Natural language text:

If $A \subseteq B$, then $\mathcal{P}(A) \subseteq \mathcal{P}(B)$:

Pf: Let $X \in \mathcal{P}(A)$. By definition of power set, $X \subseteq A$. Since $A \subseteq B$, it follows that $X \subseteq B$. Therefore, $X \in \mathcal{P}(B)$. Hence, every element of $\mathcal{P}(A)$ is also in $\mathcal{P}(B)$, so $\mathcal{P}(A) \subseteq \mathcal{P}(B)$. Qed.

Structure schematic:

[Fix] {A,B} such that {$A \subseteq B$}
{
	[Show] {$\mathcal{P}(A) \subseteq \mathcal{P}(B)$}
	{
		[Fix] {X} such that {$X \in \mathcal{P}(A)$}
		{
			[Have] {$X \subseteq A$} by {definition of power set}
			[Have] {$X \subseteq B$} by {$A \subseteq B$}
			[Have] {$X \in \mathcal{P}(B)$}
		}
		[Have] {every element of $\mathcal{P}(A)$ is also in $\mathcal{P}(B)$}
		[Have] {$\mathcal{P}(A) \subseteq \mathcal{P}(B)$}
	}
}

Natural language text:

$A \times \bigcup B = \bigcup \{A \times X \mid X \in B\}$

($\subseteq$): Let $(a, x) \in A \times \bigcup B$. By definition, $x \in \bigcup B$, so there exists $X \in B$ such that $x \in X$. Therefore, $(a, x) \in A \times X$. Since $A \times X$ is part of the union $\bigcup \{A \times X \mid X \in B\}$, we conclude $(a, x) \in \bigcup \{A \times X \mid X \in B\}$.

($\supseteq$): Let $(a, x) \in \bigcup \{A \times X \mid X \in B\}$. Then there exists $X \in B$ such that $(a, x) \in A \times X$. By definition of Cartesian product, $a \in A$ and $x \in X$. Since $X \in B$, we have $x \in \bigcup B$. Thus, $(a, x) \in A \times \bigcup B$.

Hence, $A \times \bigcup B = \bigcup \{A \times X \mid X \in B\}$.

Structure:

[Fix] {$A,B$} such that {$A,B$ are sets}
{
	[Show] {$A \times \bigcup B = \bigcup \{A \times X \mid X \in B\}$}
	{
		[Show] {$A \times \bigcup B \subseteq \bigcup \{A \times X \mid X \in B\}$}
		{
			[Fix] {$a,x$} such that {$(a, x) \in A \times \bigcup B$}
			{
				[Have] {$x \in \bigcup B$} by {definition}
				[Obtain] {$X$} such that {$X \in B$}; {$x \in X$}
				[Have] {$(a, x) \in A \times X$}
				[Have] {$(a, x) \in \bigcup \{A \times X \mid X \in B\}$} by {$A \times X$ is part of the union $\bigcup \{A \times X \mid X \in B\}$}
			}
		}
		[Show] {$\bigcup \{A \times X \mid X \in B\} \subseteq A \times \bigcup B$}
		{
			[Fix] {$a, x$} such that {$(a, x) \in \bigcup \{A \times X \mid X \in B\}$}
			{
				[Obtain] {$X$} such that {$X \in B$}; {$(a, x) \in A \times X$}
				[Have] {$a \in A$}; {$x \in X$} by {definition of Cartesian product}
				[Have] {$x \in \bigcup B$} by {$X \in B$}
				[Have] {$(a, x) \in A \times \bigcup B$}
			}
		}
		[Have] {$A \times \bigcup B = \bigcup \{A \times X \mid X \in B\}$}
	}
}

## How to Extract Structure

Given a piece of natural language text, a good structure extraction should satisfy: exactly preserving all the information of the natural language, while being logically clear and semantically unambiguous. However, due to the "ambiguity of natural language", we cannot use a precise algorithm to determine whether a structure perfectly corresponds to the natural language text. Usually, the structure corresponding to a natural language text is not unique; there may be multiple "good structures". Below we establish a series of criteria for "good structures".

### Information Equivalence

The structure should exactly preserve the information of the natural language text; it should not omit information, nor should it arbitrarily add information.

For example, the correct node extraction for the natural language text "We have $f(1)>0$." is [Have] {$f(1)>0$}. For this proposition, it should not be extracted as [Have] {$f(1)>0$} by {the definition of $f$}, even though "by definition of $f$" is indeed the reason for deriving $f(1)>0$ in this text. However, since this information is inferred by the reader and is not present in the original text, it should not be arbitrarily added during structure extraction.

Similarly, the correct node extraction for "By definition of power set, $X \subseteq A$" is [Have] {$X \subseteq A$} by {definition of power set}. If written as [Have] {$X \subseteq A$}, it omits the hint information "definition of power set" that was originally present in the text.

In short, structure extraction should not omit information, and generally does not need to supplement information on its own. However, "not allowing to supplement information on its own" does not mean "can only copy the original text verbatim". When the expression of the natural language itself is logically less strict or semantically less clear (for example, quantifier handling, variability of variables, etc., which we will detail in the following sections), we need to make "clarifications" during structure extraction. This is a clarification of the information the natural language "attempts to convey", not "adding extra information".

### Variable Introduction

The four nodes Fix, Obtain, Find, Define have the function of "introducing variables". Here, the definition of "introduction" is as follows:

- For the node [Fix] {x1, ..., xn} such that {P}, the variables x1, ..., xn are introduced within the scope of this node;
- For the node [Obtain] {x1, ..., xn} such that {P} by {Q}, the variables x1, ..., xn are introduced within the scope where the Obtain node is located, specifically in the range after this Obtain node;
- For the node [Find] {x1, ..., xn} such that {P}, the variables x1, ..., xn are introduced within the scope of this node;
- For the node [Define] {x} as {P}, the variable x is introduced within the scope where the Define node is located, specifically in the range after this Define node;

A good structure needs to satisfy the "No Free Variables Principle": every "free variable" appearing in the mathematical proposition of each node must have been introduced.

> The definition of "free variable" is the traditional logical definition. For example, in $\forall x, x+a=y$, $a$ and $y$ are free variables, and $x$ is a bound variable.
>
> Note that it is the "mathematical proposition of the node" that cannot have free variables. There is no such requirement for natural language hints or narrative reasoning. For example, [Have] {$\forall x,x^2>0$} by {$x$ squared is non-negative} does not violate the no free variables requirement, because the reasoning hint "$x$ squared is non-negative" is not a mathematical proposition, so naturally there is no concept of free variables.

### Quantifier Handling

The biggest difference between natural language and traditional logic is: the handling of quantifiers $\forall,\exists$ in natural language is ambiguous. Quantifiers in natural language are often omitted. Even when not omitted, quantifiers in natural language often span multiple lines.

Let's look at the following example:

> Theorem 2.4.7 (Cauchy Convergence): A sequence $\{x_n\}$ converges if and only if $\{x_n\}$ is a Cauchy sequence.
>
> Proof: First, we prove the necessity.
> Assume $\{x_n\}$ converges to $a$.
> By definition, for any $\varepsilon > 0$, there exists $N$ such that for all $n, m > N$: $|x_n - a| < \frac{\varepsilon}{2}, \quad |x_m - a| < \frac{\varepsilon}{2}$.
> Thus, $|x_n - x_m| \leq |x_n - a| + |x_m - a| < \varepsilon$.
>
> Next, we prove the sufficiency.
> First, we show that a Cauchy sequence must be bounded.
> Take $\varepsilon_0 = 1$. Since $\{x_n\}$ is a Cauchy sequence, there exists $N_0$ such that for all $n > N_0$: $|x_n - x_{N_0 + 1}| < 1$.
> Let $M = \max \{|x_1|, |x_2|, \ldots, |x_{N_0}|, |x_{N_0 + 1}| + 1\}$.
> Then for all $n$, we have $|x_n| \leq M$.
>By the Bolzano-Weierstrass theorem, there exists a convergent subsequence in $\{x_n\}$: $\lim_{k \to \infty} x_{n_k} = \xi$.
> Since $\{x_n\}$ is a Cauchy sequence, for any $\varepsilon > 0$, there exists $N$ such that for all $n, m > N$: $|x_n - x_m| < \frac{\varepsilon}{2}$.
> In the above inequality, take $x_m = x_{n_k}$, where $k$ is sufficiently large such that $n_k > N$, and let $k \to \infty$. Then we obtain $|x_n - \xi| \leq \frac{\varepsilon}{2}$.
> Thus, $|x_n - \xi| < \varepsilon$.
> This shows that the sequence $\{x_n\}$ converges.
> The proof is complete.

Let's extract the structure of the passage "By definition, for any $\varepsilon > 0$, there exists $N$ such that for all $n, m > N$: $|x_n - a| < \frac{\varepsilon}{2}, \quad |x_m - a| < \frac{\varepsilon}{2}$. Thus, $|x_n - x_m| \leq |x_n - a| + |x_m - a| < \varepsilon$." (assuming the outer structure has already introduced $x, a$).

First, writing it like this is incorrect:

[Have] {for any $\varepsilon > 0$, there exists $N$ such that for all $n, m > N$: $|x_n - a| < \frac{\varepsilon}{2}, \quad |x_m - a| < \frac{\varepsilon}{2}$} by {definition}
[Have] {$|x_n - x_m| \leq |x_n - a| + |x_m - a| < \varepsilon$}

The first Have node does not violate the variable introduction requirement because, from the perspective of the proposition "for any $\varepsilon > 0$, there exists $N$ such that for all $n, m > N$: $|x_n - a| < \frac{\varepsilon}{2}, \quad |x_m - a| < \frac{\varepsilon}{2}$", $\varepsilon, N, n, m$ are all bound variables, so this node does not have any unbound free variables. However, in the second Have node, $n, m, \varepsilon$ are all unbound free variables.

To eliminate the free variables in the second node, it can be rewritten as:

[Have] {for any $\varepsilon > 0$, there exists $N$ such that for all $n, m > N$: $|x_n - a| < \frac{\varepsilon}{2}, \quad |x_m - a| < \frac{\varepsilon}{2}$} by {definition}
[Have] {for any $\varepsilon > 0$, there exists $N$ such that for all $n, m > N$: $|x_n - x_m| \leq |x_n - a| + |x_m - a| < \varepsilon$}

By repeating the quantifier introduction method from the first Have node, we successfully eliminated the unbound free variables and made the semantics match the original text. However, doing this seems repetitive and cumbersome because we keep repeating the quantifier introduction. A better approach is to split the first Have node into Fix and Obtain nodes:

[Fix] {$\varepsilon$} such that {$\varepsilon>0$}
{
	[Obtain] {$N$} such that {$\forall n, m > N$：$|x_n - a| < \frac{\varepsilon}{2}, \quad |x_m - a| < \frac{\varepsilon}{2}$} by {definition}
	[Fix] {$n$,$m$} such that {$n>N$, $m>N$}
	{
		[Have] {$|x_n - x_m| \leq |x_n - a| + |x_m - a| < \varepsilon$}	
	}
}

To summarize, we see that the following two structures are equivalent:

- [Have] {$\forall x, P(x)\implies Q(x)$}
- [Fix] {x} such that {P(x)}
  {
		[Have] {Q(x)}
  }

The following two structures are also equivalent:

- [Have] {$\exists x, P(x)$}
- [Obtain] {x} such that {P(x)}

To avoid a large amount of supplementing quantifiers inside Have nodes, splitting Have nodes containing quantifiers into Fix and Obtain nodes is usually beneficial for simplifying the structure.

Below we completely write out the structure of the Cauchy Convergence Theorem text above:

[Hint] {Theorem 2.4.7 (Cauchy Convergence)}
[Fix] {$x$} such that {$\{x_n\}$ is a real sequence}
{
	[Show] {sequence $\{x_n\}$ converges if and only if $\{x_n\}$ is a Cauchy sequence.}
	{
		[Show] {sequence $\{x_n\}$ converges implies $\{x_n\}$ is a Cauchy sequence.}
		{
			[Fix] {$a$} such that { $\{x_n\}$ converges to $a$}
			{
				[Fix] {$\varepsilon$} such that {$\varepsilon>0$}
				{
					[Obtain] {$N$} such that {$\forall n, m > N$：$|x_n - a| < \frac{\varepsilon}{2}, \quad |x_m - a| < \frac{\varepsilon}{2}$} by {definition}
					[Fix] {$n$,$m$} such that {$n>N$, $m>N$}
					{
						[Have] {$|x_n - x_m| \leq |x_n - a| + |x_m - a| < \varepsilon$}	
					}
				}
			}
		}
		[Show] { $\{x_n\}$ is a Cauchy sequence implies sequence $\{x_n\}$ converges}
		{
			[Show] {Cauchy sequence $\{x_n\}$ is bounded}
			{
				[Obtain] {$N_0$} such that {$\forall n > N_0$：$|x_n - x_{N_0 + 1}| < 1$} by {take $\varepsilon_0 = 1$};{$\{x_n\}$ is a cauchy sequence}
				[Define] {$M$} as {$M = \max \{|x_1|, |x_2|, \ldots, |x_{N_0}|, |x_{N_0 + 1}| + 1\}$}
				[Have] {$\forall n, |x_n| \leq M$}
			}
			[Obtain] {$\{x_{n_k}\}$};{$\xi$} such that {$\{x_{n_k}\}$ is a subsequence of $\{x_n\}$};{$\lim_{k \to \infty} x_{n_k} = \xi$} by {Bolzano-Weierstrass theorem}
			[Fix] {$\varepsilon$} such that {$\varepsilon>0$}
			{
				[Obtain] {$N$} such that {$\forall n, m > N$：$|x_n - x_m| < \frac{\varepsilon}{2}$} by {$\{x_n\}$ is a Cauchy sequence}
				[Fix] {$n$} such that {$n>N$}
				{
					[Have] {$|x_n - \xi| \leq \frac{\varepsilon}{2}$} by {take $x_m = x_{n_k}$ in the inequality $|x_n - x_m| < \frac{\varepsilon}{2}$, where $k$ is sufficiently large such that $n_k > N$, and let $k \to \infty$}
					[Have] {$|x_n - \xi| < \varepsilon$}
				}
			}
			[Have] {$\{x_n\}$ converges}
		}
	}
}

Regarding some other key points in this example, brief explanations are given below:

- The theorem's name and number appear at the beginning of the text; this is information without specific mathematical meaning, so it is written at the beginning using a Hint node;
- The proof, from start to finish, discusses a fixed sequence $x$, so the outermost layer uses a Fix node to fix $x$;
- The sentence "By the Bolzano-Weierstrass theorem, there exists a convergent subsequence in $\{x_n\}$: $\lim_{k \to \infty} x_{n_k} = \xi$." establishes the existence of a "subsequence", not the usual "existence of some variable". For existence, we still use an Obtain node, but the object obtained is a subsequence. [Obtain] {$\{x_{n_k}\}$};{$\xi$} such that {$\{x_{n_k}\}$ is a subsequence of $\{x_n\}$};{$\lim_{k \to \infty} x_{n_k} = \xi$} by {Bolzano-Weierstrass theorem}. In fact, obtaining a subsequence essentially means obtaining a mapping from $\N$ to $\N$, so through this Obtain node, we introduce the mapping $n$, which can continue to be used within the following scope. From this example, we can see that variable introduction can sometimes be "implicit"; the object obtained by Obtain can be an expression, and the introduction of this expression implies the introduction of some variable. Of course, strictly writing it as [Obtain] {$n$};{$\xi$} such that {$n:\N\to\N$}; {$\{x_{n_k}\}$ is a subsequence of $\{x_n\}$};{$\lim_{k \to \infty} x_{n_k} = \xi$} by {Bolzano-Weierstrass theorem} is also considered a correct structure extraction.

### Natural Language Actions

We need to distinguish between "variable introduction" and "natural language actions". The former has a clear mathematical meaning, while the latter is merely a natural language prompt. For example, in the Cauchy convergence theorem example from the previous section, there are two instances involving "actions":

"Take $\varepsilon_0 = 1$. Since $\{x_n\}$ is a Cauchy sequence, there exists $N_0$ such that for all $n > N_0$: $|x_n - x_{N_0 + 1}| < 1$.". We note that $\varepsilon_0$ is not a variable that truly plays a role in the proof process; in fact, the variable $\varepsilon_0$ only appears this once and never appears again in any assertion. The reason the variable $\varepsilon$ is mentioned here is because the definition of a Cauchy sequence contains the quantifier $\forall \varepsilon>0, ...$, and the natural language here intends to express "specifically take $\varepsilon=1$ in the definition of a Cauchy sequence, we obtain...". Therefore, the phrase "Take $\varepsilon_0 = 1$" here is merely a suggestive statement, used to show us how we arrive at the assertion "there exists $N_0$ such that for all $n > N_0$: $|x_n - x_{N_0 + 1}| < 1$.". So the correct structure extraction for this sentence is [Obtain] {$N_0$} such that {$\forall n > N_0$：$|x_n - x_{N_0 + 1}| < 1$} by {take $\varepsilon_0 = 1$};{$\{x_n\}$ is a cauchy sequence}

"In the above inequality, take $x_m = x_{n_k}$, where $k$ is sufficiently large such that $n_k > N$, and let $k \to \infty$. Then we obtain $|x_n - \xi| \leq \frac{\varepsilon}{2}$." Similar to "Take $\varepsilon_0 = 1$", the series of actions "take $x_m = x_{n_k}$, where $k$ is sufficiently large such that $n_k > N$, and let $k \to \infty$" in this sentence is showing us what method we use to obtain the assertion $|x_n - \xi| \leq \frac{\varepsilon}{2}$, so this series of actions should all be considered as suggestive statements. [Have] {$|x_n - \xi| \leq \frac{\varepsilon}{2}$} by {take $x_m = x_{n_k}$ in the inequality $|x_n - x_m| < \frac{\varepsilon}{2}$, where $k$ is sufficiently large such that $n_k > N$, and let $k \to \infty$}.

Let's look at another example of a functional equation:

> We need to find all functions $ f: \mathbb{R} \rightarrow \mathbb{R} $ such that for all $ x, y \in \mathbb{R} $, $ f(x + y) - f(x - y) = f(x)f(y). $
> Solution
> First, interchange $ x $ and $ y $ in the original equation:
> $ f(y + x) - f(y - x) = f(y)f(x). $
> Thus, we have:
> $ f(y + x) - f(y - x) = f(x + y) - f(x - y). $
> This implies:
> $ f(y - x) = f(x - y). $
> Let $ y = 0 $, then:
> $ f(-x) = f(x). $
> So $ f $ is an even function.
> Now, in the original equation, replace $ y $ with $ -y $:
> $ f(x + (-y)) - f(x - (-y)) = f(x)f(-y), $
> which simplifies to:
> $ f(x - y) - f(x + y) = f(x)f(-y). $
> Since $ f $ is even, $ f(-y) = f(y) $, so:
> $ f(x - y) - f(x + y) = f(x)f(y). $
> But from the original equation,
> $ f(x + y) - f(x - y) = f(x)f(y). $
> Adding these two equations:
> $ [f(x + y) - f(x - y)] + [f(x - y) - f(x + y)] = f(x)f(y) + f(x)f(y), $
> which gives:
> $ 0 = 2f(x)f(y). $
> Therefore, for all $ x, y \in \mathbb{R} $,
> $ f(x)f(y) = 0. $
> In particular, let $ y = x $:
> $ f(x)^2 = 0 \quad \Rightarrow \quad f(x) = 0. $
> Thus, the only function satisfying the condition is the zero function.
> In conclusion, the only solution is:
> $ \boxed{f(x) = 0} $

Actions like "Let $y=0$", "replace $y=-y$", "let $y=x$", etc., that appear in this example are all suggestive statements, not assertions or assumptions. For example, for "let $y=x$", the correct structure extraction is: [Have] {$\forall x \in \mathbb{R}, f(x)^2 = 0$} by {Let $y = x$}

Below we write out the complete structure corresponding to this functional equation example. (We will come back to this example later when we discuss the variability of natural language variables.)

[Find] {f} such that {$f: \mathbb{R} \rightarrow \mathbb{R}$}; {$\forall x, y \in \mathbb{R}, f(x + y) - f(x - y) = f(x)f(y)$}
{
	[Have] {$\forall x, y \in \mathbb{R}, f(y + x) - f(y - x) = f(y)f(x)$} by {interchanging $x$ and $y$ in $f(x + y) - f(x - y) = f(x)f(y)$}
	[Have] {$\forall x,y\in\R,f(y + x) - f(y - x) = f(x + y) - f(x - y)$}
	[Have] {$\forall x, y \in \mathbb{R}, f(y - x) = f(x - y)$}
	[Have] {$\forall x \in \mathbb{R}, f(-x) = f(x)$} by {Letting y = 0 in $\forall x, y \in \mathbb{R}, f(y - x) = f(x - y)$}
	[Have] {$f$ is an even function}
	[Have] {$\forall x,y\in\R, f(x + (-y)) - f(x - (-y)) = f(x)f(-y)$} by {replacing $y$ with $-y$ in $f(x + y) - f(x - y) = f(x)f(y)$}
	[Have] {$\forall x, y \in \mathbb{R},  f(x - y) - f(x + y) = f(x)f(-y). $} by {simplify}
	[Have] {$\forall x,y\in\R, f(x - y) - f(x + y) = f(x)f(y). $} by {$ f $ is even};{$ f(-y) = f(y) $}
	[Have] {$\forall x,y\in\R,  f(x + y) - f(x - y) = f(x)f(y). $} by {this is the original equation}
	[Have] {$\forall x, y \in \mathbb{R},  [f(x + y) - f(x - y)] + [f(x - y) - f(x + y)] = f(x)f(y) + f(x)f(y), $} by {Adding the equation $f(x + y) - f(x - y) = f(x)f(y)$ and the equation $f(x - y) - f(x + y) = f(x)f(y)$}
	[Have] {$\forall x,y\in\R, 0 = 2f(x)f(y)$}
	[Have] {$\forall x, y \in \mathbb{R}, f(x)f(y) = 0$}
	[Have] {$\forall x \in \mathbb{R}, f(x)^2 = 0$} by {Letting $y = x$}
	[Have] {$\forall x \in \mathbb{R}, f(x) = 0$}
	[Have] {The only solution is the function $f(x) = 0$ for all $x \in \mathbb{R}$}
}

### Natural Language Reference

In the Cauchy convergence theorem example, when extracting the structure, we specifically supplemented the "In the above inequality" in the prompt to "in the inequality $|x_n - x_m| < \frac{\varepsilon}{2}$". In the functional equation example, when extracting the structure, we specifically supplemented the "the original equation" in the prompt to "$\forall x, y \in \mathbb{R}, f(x + y) - f(x - y) = f(x)f(y)$".

We summarize this practice as: a good structure should specify the references in natural language.

Similar situations include: natural language texts assign formula numbers, e.g., $f(x)=0\quad (1)$, $g(x)=1\quad (2)$; and then reference these numbers in narratives, e.g., "Combining equations (1) and (2) yields...". For such cases, we handle them as follows: in the nodes asserting $f(x)=0, g(x)=1$, do not retain the $(1)(2)$ labels; when referencing labels in narratives, complete the specific expressions or propositions corresponding to the labels. Specifically:

[Have] {$f(x)=0$}
[Have] {$g(x)=0$}
...
[Have] {...} by {Combining the equations $f(x)=0$ and $g(x)=0$}

### Variability of Variables in Natural Language

Consider the previous functional equation example. In the natural language argumentation process, $\forall x,y$ is not repeatedly mentioned; instead, equations with free variables like $f(y + x) - f(y - x) = f(y)f(x)$ are simply written. In the structure provided earlier, we supplemented $\forall x,y\in\R$ inside each Have node, thereby eliminating the free variables.

Similarly aiming to eliminate free variables, could we do it like this:

[Find] {$f$} such that {$f: \mathbb{R} \rightarrow \mathbb{R}$}; {$\forall x, y \in \mathbb{R}, f(x + y) - f(x - y) = f(x)f(y)$}
{
	[Fix] {$x,y$} such that {$x,y\in\R$}
	{
		[Have] {$f(y + x) - f(y - x) = f(y)f(x)$} by {interchanging $x$ and $y$ in $f(x + y) - f(x - y) = f(x)f(y)$}
		[Have] {$f(y + x) - f(y - x) = f(x + y) - f(x - y)$}
		[Have] {$f(y - x) = f(x - y)$}
		...

It can be found that writing this way is logically incorrect. In the derivation process of the functional equation, it is not the case that for fixed $x,y$, $f(y + x) - f(y - x) = f(y)f(x)$ is derived from $f(x + y) - f(x - y) = f(x)f(y)$; rather, $\forall x, y \in \mathbb{R}, f(y + x) - f(y - x) = f(y)f(x)$ is derived from $\forall x, y \in \mathbb{R}, f(x + y) - f(x - y) = f(x)f(y)$. These two are mathematically fundamentally different! In natural language, the variables $x,y$ here vary arbitrarily within the real numbers, they are not fixed. Therefore, when extracting the structure, we must absolutely not write Fix {x,y} at the outer level and then perform derivations inside; instead, we should reiterate $\forall x,y$ with each assertion.

Let's look at another example of solving an indefinite integral using the method of undetermined coefficients:

>  Find the integral $\displaystyle\int \frac{4x^3 - 13x^2 + 3x + 8}{(x+1)(x-2)(x-1)^2}  dx$.
> First, decompose the integrand into a sum of simple fractions. Let:
> $\displaystyle\frac{4x^3 - 13x^2 + 3x + 8}{(x+1)(x-2)(x-1)^2} = \frac{A}{x+1} + \frac{B}{x-2} + \frac{C}{x-1} + \frac{D}{(x-1)^2}.$
> After combining the right-hand side over a common denominator, the numerators on both sides must be equal, so:
> $4x^3 - 13x^2 + 3x + 8 = A(x-2)(x-1)^2 + B(x+1)(x-1)^2 +$
> $C(x+1)(x-2)(x-1) + D(x+1)(x-2).$
> Let $x = -1$, we get $A = 1$;
> Let $x = 2$, we get $B = -2$;
> Let $x = 1$, we get $D = -1$;
> Differentiate both sides then let $x = 1$, we get $C = 5$;
> Thus:
> $\displaystyle\int \frac{4x^3 - 13x^2 + 3x + 8}{(x+1)(x-2)(x-1)^2}  dx = \int \left[ \frac{1}{x+1} - \frac{2}{x-2} + \frac{5}{x-1} - \frac{1}{(x-1)^2} \right]  dx$
> $= \ln |(x+1)(x-1)^5| - \ln |(x-2)^2| + \frac{1}{x-1} + C.$

In this example, deriving $4x^3 - 13x^2 + 3x + 8 = A(x-2)(x-1)^2 + B(x+1)(x-1)^2 + C(x+1)(x-2)(x-1) + D(x+1)(x-2)$ from $\frac{4x^3 - 13x^2 + 3x + 8}{(x+1)(x-2)(x-1)^2} = \frac{A}{x+1} + \frac{B}{x-2} + \frac{C}{x-1} + \frac{D}{(x-1)^2}$ is not for some fixed $x$; it is based on "$\frac{4x^3 - 13x^2 + 3x + 8}{(x+1)(x-2)(x-1)^2}$ and $\frac{A}{x+1} + \frac{B}{x-2} + \frac{C}{x-1} + \frac{D}{(x-1)^2}$ are two identical rational functions", leading to the conclusion that $4x^3 - 13x^2 + 3x + 8$ and $A(x-2)(x-1)^2 + B(x+1)(x-1)^2 + C(x+1)(x-2)(x-1) + D(x+1)(x-2)$ are two identical polynomials. This shows that $x$ is a varying quantity, not a fixed one. Therefore, Fix {x} should not be used at the outer level during the derivation; instead, $\forall x$ should be supplemented in each line.

When supplementing $\forall x$, $\forall x, \frac{4x^3 - 13x^2 + 3x + 8}{(x+1)(x-2)(x-1)^2} = \frac{A}{x+1} + \frac{B}{x-2} + \frac{C}{x-1} + \frac{D}{(x-1)^2}$ is actually more precisely $\forall x\in \R\setminus\{1,-1,2\}, \frac{4x^3 - 13x^2 + 3x + 8}{(x+1)(x-2)(x-1)^2} = \frac{A}{x+1} + \frac{B}{x-2} + \frac{C}{x-1} + \frac{D}{(x-1)^2}$, because the denominator cannot be zero. However, the latter formulation involves reasoning at the arithmetic level, which is too cumbersome for the purpose of structure extraction. Therefore, we do not mandate writing it in the latter form; instead, we allow simply writing $\forall x$, used to address the issue of free occurrence and variability of $x$. The reason for this design is also because sometimes the range of variation of the variable is not easy to represent precisely.

$\ln |(x+1)(x-1)^5| - \ln |(x-2)^2| + \frac{1}{x-1} + C$ is actually a family of functions; we need to ensure that both variables $x$ and $C$ are properly handled in the final structure; they cannot be free variables. Logically, the strict expression here should be $\{\lambda x.(\ln |(x+1)(x-1)^5| - \ln |(x-2)^2| + \frac{1}{x-1} + C)\mid C\in \R\}$. But writing this is too cumbersome; we directly use a "descriptive phrase" to eliminate the free variable property of $x$ and $C$, writing it as {function family $\ln |(x+1)(x-1)^5| - \ln |(x-2)^2| + \frac{1}{x-1} + C$}

The final structure is:

[Find] {$\int \frac{4x^3 - 13x^2 + 3x + 8}{(x+1)(x-2)(x-1)^2}  dx$}
{
	[Hint] {First, decompose the integrand into a sum of simple fractions.}
	[Find] {$A, B, C, D$} such that {$\forall x, \frac{4x^3 - 13x^2 + 3x + 8}{(x+1)(x-2)(x-1)^2} = \frac{A}{x+1} + \frac{B}{x-2} + \frac{C}{x-1} + \frac{D}{(x-1)^2}$}
	{
		[Have] {$\forall x, 4x^3 - 13x^2 + 3x + 8 = A(x-2)(x-1)^2 + B(x+1)(x-1)^2 + C(x+1)(x-2)(x-1) + D(x+1)(x-2)$} by {combining the right-hand side over a common denominator, the numerators on both sides must be equal}
		[Have] {$A = 1$} by {Let $x = -1$}
		[Have] {$B = -2$} by {Let $x = 2$}
		[Have] {$D = -1$} by {Let $x = 1$}
		[Have] {$C = 5$} by {Differentiate both sides then let $x = 1$}
	}
	[CalculationChain] {$\int \frac{4x^3 - 13x^2 + 3x + 8}{(x+1)(x-2)(x-1)^2}  dx$} {=} {} {$\int \left[ \frac{1}{x+1} - \frac{2}{x-2} + \frac{5}{x-1} - \frac{1}{(x-1)^2} \right]  dx$} {=} {} {function family $\ln |(x+1)(x-1)^5| - \ln |(x-2)^2| + \frac{1}{x-1} + C$}
}

> This example involves the method of undetermined coefficients. The essence of the method of undetermined coefficients is to "solve" for the set parameters, so the Find node is used.

The above observation tells us: Although both "writing Fix in the outer layer" and "supplementing forall inside the node" can achieve the purpose of "eliminating free variables", the semantics produced by these two approaches are completely different! In structure extraction, a most critical task is to accurately judge the "variability" of natural language variables, and then use the correct method to eliminate free variables.

The above discussions are all aimed at independently varying variables. However, many times there are situations where the changes of different variables are interrelated. And the dependency relationship between variable changes is essentially a function. But because natural language is ambiguous, this functional relationship is not explicitly written out, which creates another key difficulty in the structure extraction process. Often, to ensure the "no free variables" principle, the implicit functional relationship must be supplemented.

Let's look at an example of the mean value theorem for integrals:

>  Suppose $f(x)$ is continuous on $[0,1]$ , prove that: $\lim_{h \to 0^+} \int_0^1 \frac{h}{h^2 + x^2} f(x) dx = \frac{\pi}{2} f(0)$
>
> Pf:
> $\int_0^1 \frac{h}{h^2 + x^2} f(x) dx = \int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx + \int_{h^{1/4}}^1 \frac{hf(x)}{h^2 + x^2} dx$
> Let $I_1 = \int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx$, $I_2 = \int_{h^{1/4}}^1 \frac{hf(x)}{h^2 + x^2} dx$
> where $I_1 = \int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx = f(\xi) \int_0^{h^{1/4}} \frac{h}{h^2 + x^2} dx \quad (0 \leq \xi \leq h^{1/4})$
> $= f(\xi) \arctan \frac{x}{h} \Big|_0^{h^{1/4}} = f(\xi) \arctan \frac{1}{h^{3/4}} \to f(0)\dfrac{\pi}{2} \quad (h \to 0^+)$
> $|I_2| = \left| \int_{h^{1/4}}^1 \frac{h}{h^2 + x^2} f(x) dx \right| \leq M \int_{h^{1/4}}^1 \frac{h}{h^2 + x^2} dx(\quad |f(x)|\leq M\quad)$
> $= M \left( \arctan \frac{1}{h} - \arctan \frac{1}{h^{3/4}} \right) \to 0 \quad (h \to 0^+)$
> Hence $h\to 0^+$时$I_1+I_2\to f(0)\dfrac{\pi}{2}$
> Qed.

First, in this proof process, is $h$ fixed or variable? Note the $h\to 0^+$ below. In the original text, according to $I_1=f(\xi)\arctan \frac{1}{h^{3/4}}$, let $h\to 0^+$ at this point, thus obtaining the limit value of $I_1$. If this entire process is said for a fixed $h$, then we must first exit the scope of Fix {h} to be able to discuss $h\to 0^+$. However, after discussing the limit value of $I_1$, the original text begins to discuss the limit value of $I_2$. If $I_2$ is defined for that fixed $h$, then after exiting the scope of Fix {h}, the definition of $I_2$ becomes invalid. But natural language does not re-narrate the definition of $I_2$, which shows that it is more reasonable to understand $h$ as "variable" in this example. For this reason, we need to supplement $\forall h$ inside the node. (If we want to be more precise, we can see that the range of variation of $h$ is some right neighborhood of $0$. Through simple observation, we can set this neighborhood as $(0,1/2)$.)

Since $h$ is variable, then $I_1,I_2$ are quantities defined with respect to the variable $h$, they are quantities that change with $h$. Therefore, $I_1,I_2$ are no longer real numbers, but functions of $h$. Therefore, the correct structure extraction is [Define] {$I_1$} as {$\forall h\in(0,1/2)$, $I_1(h)=\int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx$}, not [Define] {$I_1$} as {$I_1=\int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx$}. Similarly, $\xi$ is also a function of $h$.

Final structure:

[Fix] {$f$} such that {$f:\R \to \R$};{ $f(x)$ is continuous on $[0,1]$ }
{
	[Show] {$\lim\limits_{h \to 0^+} \int_0^1 \frac{h}{h^2 + x^2} f(x) dx = \frac{\pi}{2} f(0)$}
	{
		[Have] {$\forall h\in (0,1/2)$, $\int_0^1 \frac{h}{h^2 + x^2} f(x) dx = \int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx + \int_{h^{1/4}}^1 \frac{hf(x)}{h^2 + x^2} dx$}
		[Define] {$I_1$} as {$\forall h\in (0,1/2)$, $I_1(h)=\int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx$}
		[Define] {$I_2$} as {$\forall h\in (0,1/2)$, $I_2(h)=\int_{h^{1/4}}^1 \frac{hf(x)}{h^2 + x^2} dx$}
		[Obtain] {$\xi$} such that {$\xi:\R\to \R\land \forall h\in (0,1/2),\xi(h)\in [0, h^{1/4}]$ $\land$ $\forall h\in (0,1/2),I_1(h) = \int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx = f(\xi(h)) \int_0^{h^{1/4}} \frac{h}{h^2 + x^2} dx$}
		[Have] {$\forall h\in (0,1/2),f(\xi(h)) \int_0^{h^{1/4}} \frac{h}{h^2 + x^2} dx = f(\xi(h)) \arctan \frac{x}{h} \Big|_0^{h^{1/4}} = f(\xi(h)) \arctan \frac{1}{h^{3/4}}$}
		[Have] {$\lim\limits_{h \to 0^+} f(\xi(h)) \arctan \frac{1}{h^{3/4}} = f(0)\dfrac{\pi}{2}$}
		[Obtain] {$M$} such that {$M \in \R$};{$\forall x \in [0,1],|f(x)|\leq M$}
		[Have] {$\forall h\in (0,1/2),|I_2(h)| = \left| \int_{h^{1/4}}^1 \frac{h}{h^2 + x^2} f(x) dx \right| \leq M \int_{h^{1/4}}^1 \frac{h}{h^2 + x^2} dx$}]
		[Have] {$\forall h\in (0,1/2),M \int_{h^{1/4}}^1 \frac{h}{h^2 + x^2} dx = M \left( \arctan \frac{1}{h} - \arctan \frac{1}{h^{3/4}} \right)$}
		[Have] {$\lim\limits_{h \to 0^+} M \left( \arctan \frac{1}{h} - \arctan \frac{1}{h^{3/4}} \right) = 0$}
		[Have] {$\lim\limits_{h \to 0^+} (I_1(h) + I_2(h)) = f(0)\dfrac{\pi}{2}$}
	}
}

> The two limit calculations in this example appear on the surface to be suitable for identification as CalculationChain, but because the calculation process involves obtaining variables such as $\xi,M$, identifying them as CalculationChain would violate the "no free variables" principle. So they are still split apart and identified as multiple nodes.

Summary: Variables in natural language are divided into two types: "fixed" and "variable". For fixed variables, usually use outer Fix to eliminate free variables; for variable variables, usually use the method of supplementing forall inside the node to eliminate free variables. To extract the correct structure, the variability of variables must be accurately identified.

### Common Structures

#### Sufficient Condition Derivation

>  Let ${x}_{n} = \frac{n}{n + 1} \quad (n = 1,2,\cdots)$. Prove: $\lim_{n \to \infty} {x}_{n} = 1$.
> Proof:
> $|{x}_{n} - 1| = \frac{1}{n + 1}$.
> For any $\varepsilon > 0$, to have $|{x}_{n} - 1| < \varepsilon$, it suffices to have $\frac{1}{n + 1} < \varepsilon$, i.e., $n > \frac{1}{\varepsilon} - 1$.
> We may take $N = N(\varepsilon) = \left\lfloor \frac{1}{\varepsilon} \right\rfloor$. Then when $n > N$, $|{x}_{n} - 1| < \varepsilon$.
> Therefore, $\lim_{n \to \infty} {x}_{n} = 1$.

In this example, the part "to have $|{x}_{n} - 1| < \varepsilon$, it suffices to have $\frac{1}{n + 1} < \varepsilon$, i.e., $n > \frac{1}{\varepsilon} - 1$. " is doing a mixed logical derivation of sufficient condition derivation and equivalent derivation. We generally use the LogicChain node to represent this structure:

[Define] {$x$} as {$\forall n\in \N^*, {x}_{n} = \frac{n}{n + 1}$}
[Show] {$\lim_{n \to \infty} {x}_{n} = 1$}
{
	[Have] {$\forall n \in \N^*, |{x}_{n} - 1| = \frac{1}{n + 1}$}
	[Fix] {$\varepsilon$} such that {$\varepsilon>0$}
	{
		[Fix] {$n$} such that {$n \in \N^*$}
		{
			[LogicChain] {$|{x}_{n} - 1| < \varepsilon$} {⇐} {} {$\frac{1}{n + 1} < \varepsilon$} {⇔} {} {$n > \frac{1}{\varepsilon} - 1$}
		}
		[Define] {$N$} such that {$N=\left\lfloor \frac{1}{\varepsilon} \right\rfloor$}
		[Have] {$\forall n > N$, $|{x}_{n} - 1| < \varepsilon$}
	}
	[Have] {$\lim_{n \to \infty} {x}_{n} = 1$}
}

#### Case Analysis

The basic structure for case analysis is:

[Assume] {Case 1}
{
	...
}
[Assume] {Case 2}
{
	...
}
...
[Assume] {Case n}
{
	...
}

> $\lim_{n \to \infty} \sqrt[n]{a} = 1(a>0)$
**Proof:**
(1) When $a = 1$, the equality obviously holds.
(2) When $a > 1$, since $(1 + \varepsilon)^{n} > 1 + n\varepsilon$ (for $n > 1, \varepsilon > 0$), then for sufficiently large $n$, we can ensure $1 + n\varepsilon > a$, i.e., $(1 + \varepsilon)^{n} > a$. In fact, it suffices to take $N = \left\lceil \frac{a - 1}{\varepsilon} \right\rceil$; when $n > N$, this is guaranteed. Therefore, $1 < \sqrt[n]{a} < 1 + \varepsilon$, and when $n > N$, we have $|\sqrt[n]{a} - 1| < \varepsilon$, which implies $\lim_{n \to \infty} \sqrt[n]{a} = 1$.
(3) When $0 < a < 1$, let $a = \frac{1}{a'}$, where $a' > 1$. Then, as $n \to \infty$, $\sqrt[n]{a} = \frac{1}{\sqrt[n]{a'}} \to 1$.

The correct structure for this example is as follows:

[Fix] {$a$} such that {$a > 0$}
{
	[Show] {$\lim_{n \to \infty} \sqrt[n]{a} = 1$}
	{
		[Assume] {$a = 1$}
		{
			[Have] {$\lim_{n \to \infty} \sqrt[n]{a} = 1$}
		}
		[Assume] {$a > 1$}
		{
			[Fix] {$\varepsilon$} such that {$\varepsilon > 0$}
			{
				[Define] {$N$} as {$\left\lceil \frac{a - 1}{\varepsilon} \right\rceil$}
				[Fix] {$n$} such that {$n > N$; $n>1$}
				{
					[Have] {$1+n\varepsilon > a$}
					[Have] {$(1+\varepsilon)^n > a$}
					[Have] {$1 < \sqrt[n]{a} < 1 + \varepsilon$}
					[Have] {$|\sqrt[n]{a} - 1| < \varepsilon$}
				}
			}
			[Have] {$\lim_{n \to \infty} \sqrt[n]{a} = 1$}
		}
		[Assume] {$0 < a < 1$}
		{
			[Define] {$a'$} as {$a=\frac{1}{a'}$}
			[Have] {$a' > 1$}
			[Have] {$\lim_{n \to \infty} \sqrt[n]{a} = \lim_{n \to \infty} \frac{1}{\sqrt[n]{a'} }= 1$}
		}
	}
}

> There exist irrational numbers $a$ and $b$ such that $a^b$ is rational.
> Pf:
> The number $\sqrt{2}^{\sqrt{2}}$ must either be rational or irrational.
> If $\sqrt{2}^{\sqrt{2}}$ is rational, then let $a = \sqrt{2}$ (irrational) and $b = \sqrt{2}$ (irrational). The result $a^b$ is rational by assumption.
> If $\sqrt{2}^{\sqrt{2}}$ is irrational, then let $a = \sqrt{2}^{\sqrt{2}}$ and $b = \sqrt{2}$. Both are irrational. We have $a^b  =\left( \sqrt{2}^{\sqrt{2}} \right)^{\sqrt{2}} = \sqrt{2}^{(\sqrt{2} \times \sqrt{2})} = \sqrt{2}^2 = 2$, which is rational.
> the claim is proven.

The final structure is as follows:

[Show] {There exist irrational numbers $a$ and $b$ such that $a^b$ is rational}
{
	[Have] {The number $\sqrt{2}^{\sqrt{2}}$ is either rational or irrational}
	[Assume] {$\sqrt{2}^{\sqrt{2}}$ is rational}
	{
		[Define] {$a$} as {$\sqrt{2}$}
		[Define] {$b$} as {$\sqrt{2}$}
		[Have] {$a$ is irrational and $b$ is irrational}
		[Have] {$a^b$ is rational} by {the assumption that $\sqrt{2}^{\sqrt{2}}$ is rational}
	}
	[Assume] {$\sqrt{2}^{\sqrt{2}}$ is irrational}
	{
		[Define] {$a$} as {$\sqrt{2}^{\sqrt{2}}$}
		[Define] {$b$} as {$\sqrt{2}$}
		[Have] {$a,b$ are both irrational}
		[CalculationChain] {$a^b$} {=} {} {$\left( \sqrt{2}^{\sqrt{2}} \right)^{\sqrt{2}}$} {=} {} {$\sqrt{2}^{(\sqrt{2} \times \sqrt{2})}$} {=} {} {$\sqrt{2}^2$} {=} {} {2}
		[Have] {$a^b$ is rational}
	}
	[Have] {The claim is proven}
}

#### Proof by Contradiction

The basic structure for proof by contradiction is:

[Show] {P} using {contradiction}
{
	[Assume] {not P}
	{
		...
		[Have] {contradiction}
	}
}

> Let $ T = \{ x \mid x \in \mathbb{Q} \text{ and } x > 0, x^2 < 2 \} $. Prove that $ T $ has no least upper bound in $ \mathbb{Q} $.
>
> **Proof**: By contradiction, suppose $ T $ has a least upper bound in $ \mathbb{Q} $. Let $ \sup T = \frac{n}{m} $ (where $ m, n \in \mathbb{N}^* $ and $ m, n $ are coprime). Then it is obvious that $1 < \left( \frac{n}{m} \right)^2 < 3$
>
> Since the square of a rational number cannot be 2, there are only two possible cases:
>
> 1. $ 1 < \left( \frac{n}{m} \right)^2 < 2 $.
>
>    Let $ \frac{n^2}{m^2} = 2 - t $, where $ 0 < t < 1 $. Let $ r = \frac{n}{6m} $, then it is obvious that $ n + r > 0 $, $ \frac{n + r}{m} \in \mathbb{Q} $. Since
>
>    $
>    \frac{n^2}{3m^2} t < \frac{2}{3}, \quad \frac{2n}{m} - r < \frac{n}{18} t,
>    $
>
>    we get
>
>    $
>    \left( \frac{n + r}{m} \right)^2 = \frac{n^2}{m^2} + \frac{2n}{m} r + r^2 = 2 - t + \frac{2n}{m} r + r^2 < 2.
>    $
>
>    This implies $ \frac{n + r}{m} \in T $, contradicting the assumption that $ \frac{n}{m} $ is the least upper bound of $ T $.
>
> 2. $ 2 < \left( \frac{n}{m} \right)^2 < 3 $.
>
>    Let $ \frac{n^2}{m^2} = 2 + t $, where $ 0 < t < 1 $. Let $ r = \frac{n}{6m} $, then it is obvious that $ n - r > 0 $, $ \frac{n - r}{m} \in \mathbb{Q} $. Since
>
>    $
>    \frac{2n}{m} - r < \frac{n^2}{3m^2} t < 1,
>    $
>
>    we get
>
>    $
>    \left( \frac{n - r}{m} \right)^2 = \frac{n^2}{m^2} - \frac{2n}{m} r + r^2 = 2 + t - \frac{2n}{m} r + r^2 > 2.
>    $
>
>    This implies $ \frac{n - r}{m} \in T $, contradicting the assumption that $ \frac{n}{m} $ is the least upper bound of $ T $.
>
> Therefore, we conclude that $ T $ has no least upper bound in $ \mathbb{Q} $.

[Define] {T} as {$\{ x \mid x \in \mathbb{Q} \text{ and } x > 0, x^2 < 2 \}$}
[Show] {$T$ has no least upper bound in $\mathbb{Q}$} using {contradiction}
{
	[Assume] {$T$ has a least upper bound in $\mathbb{Q}$}
	{
		[Obtain] {n, m} such that {$\sup T = \frac{n}{m}$}; {$m, n \in \mathbb{N}^*$}; {$m, n$ are coprime}
		[Have] {$1 < \left( \frac{n}{m} \right)^2 < 3$}
		[Have] {The square of a rational number cannot be 2}
		[Hint] {There are only two possible cases:}
		[Assume] {$1 < \left( \frac{n}{m} \right)^2 < 2$}
		{
			[Define] {t} as {$\frac{n^2}{m^2}=2-t$}
			[Have] {$0 < t < 1$}
			[Define] {r} as {$r=\frac{n}{6m}$}
			[Have] {$n + r > 0$}
			[Have] {$\frac{n + r}{m} \in \mathbb{Q}$}
			[Have] {$\frac{n^2}{3m^2} t < \frac{2}{3}$}; {$\frac{2n}{m} - r < \frac{n}{18} t$}
			[CalculationChain] {$\left( \frac{n + r}{m} \right)^2$} {=} {} {$\frac{n^2}{m^2} + \frac{2n}{m} r + r^2$} {=} {} {$2 - t + \frac{2n}{m} r + r^2$} {<} {} {2}
			[Have] {$\frac{n + r}{m} \in T$}
			[Have] {contradiction} by {$\frac{n}{m}$ is the least upper bound of $T$}
		}
		[Assume] {$2 < \left( \frac{n}{m} \right)^2 < 3$}
		{
			[Define] {t} as {$\frac{n^2}{m^2} = 2+t$}
			[Have] {$0 < t < 1$}
			[Define] {r} as {$r=\frac{n}{6m}$}
			[Have] {$n - r > 0$}
			[Have] {$\frac{n - r}{m} \in \mathbb{Q}$}
			[Have] {$\frac{2n}{m} - r < \frac{n^2}{3m^2} t < 1$}
			[CalculationChain] {$\left( \frac{n - r}{m} \right)^2$} {=} {} {$\frac{n^2}{m^2} - \frac{2n}{m} r + r^2$} {=} {} {$2 + t - \frac{2n}{m} r + r^2$} {>} {} {2}
			[Have] {$\frac{n - r}{m}$ $\in$ $T$}
			[Have] {contradiction} by {$\frac{n}{m}$ is the least upper bound of $T$}
		}
	}
	[Have] {$T$ has no least upper bound in $\mathbb{Q}$}
}

#### Mathematical Induction

The basic structure for mathematical induction is:

[Show] {$\forall n$, ...} using {mathematical induction}
{
	[Have] {(Base Case)} or [Show] {(Base Case)} ...
	[Fix] {$n$(or $k$)} such that {(Induction Hypothesis)}
	{
		...
	}
}

The expressions of mathematical induction in natural language are diverse. However, for ease of processing, we prefer to uniformly treat mathematical induction as the two formats above (for this purpose, slight modifications to the original text are usually necessary, and we believe such modifications should be allowed here).

Example 1:

> $1 + 2 + \cdots + n = \frac{n(n + 1)}{2}$.
> Proof:
> We prove by mathematical induction.
> When $n = 1$, the equality holds.
> Assume the equality holds for $n = k$.
> Then for $n = k + 1$, we have
> $1 + 2 + \cdots + k + (k + 1) = \frac{k(k + 1)}{2} + k + 1 = \frac{(k + 1)[(k + 1) + 1]}{2}$.
> Thus, the equality also holds for $n = k + 1$.
> Therefore, for any positive integer $n$, we have $1 + 2 + \cdots + n = \frac{n(n + 1)}{2}$.

The structure is as follows:

[Show] {$\forall n \in \N^*, 1 + 2 + \cdots + n = \frac{n(n + 1)}{2}$} using {mathematical induction}
{
	[Have] {When $n = 1$, $1 + 2 + \cdots + n = \frac{n(n + 1)}{2}$ holds}
	[Fix] {$k$} such that {$1 + 2 + \cdots + n = \frac{n(n + 1)}{2}$ holds for $n=k$}
	{
		[Have] {$1 + 2 + \cdots + k + (k + 1) = \frac{k(k + 1)}{2} + k + 1 = \frac{(k + 1)[(k + 1) + 1]}{2}$}
		[Have] {$1 + 2 + \cdots + n = \frac{n(n + 1)}{2}$ holds for $n = k + 1$}
	}
}
[Have] {for any positive integer $n$, $1 + 2 + \cdots + n = \frac{n(n + 1)}{2}$}

> This example does not violate the "No Free Variables" principle because in the expression "$1 + 2 + \cdots + n = \frac{n(n + 1)}{2}$ holds for $n=k$", $n$ is not a free variable but a temporary variable used for substitution. Note that we are not substituting $n=k$ into $1 + 2 + \cdots + n = \frac{n(n + 1)}{2}$, but rather keeping the whole expression "$1 + 2 + \cdots + n = \frac{n(n + 1)}{2}$ holds for $n=k$". Because when the proposition is complex, the substitution operation may not be trivial, so we follow the "Information Equivalence" principle and retain the original expression.

Example 2:

> $1 + 2 + \cdots + n = \frac{n(n + 1)}{2}$.
> Proof:
> We prove by mathematical induction.
> When $n = 1$, the equality holds.
> Assume the equality holds for $n$.
> Then
> $1 + 2 + \cdots + n + (n + 1) = \frac{n(n + 1)}{2} + n + 1 = \frac{(n + 1)[(n + 1) + 1]}{2}$.
> Thus, the equality also holds for $n + 1$.
> Therefore, for any positive integer $n$, we have $1 + 2 + \cdots + n = \frac{n(n + 1)}{2}$.

The structure is as follows:

[Show] {$\forall n \in \N^*, 1 + 2 + \cdots + n = \frac{n(n + 1)}{2}$} using {mathematical induction}
{
	[Have] {When $n = 1$, $1 + 2 + \cdots + n = \frac{n(n + 1)}{2}$ holds}
	[Fix] {$n$} such that {$1 + 2 + \cdots + n = \frac{n(n + 1)}{2}$}
	{
		[Have] {$1 + 2 + \cdots + n + (n + 1) = \frac{n(n + 1)}{2} + n + 1 = \frac{(n + 1)[(n + 1) + 1]}{2}$}
		[Have] {$1 + 2 + \cdots + n+(n+1) = \frac{(n+1)((n+1) + 1)}{2}$}
	}
}
[Have] {for any positive integer $n$, $1 + 2 + \cdots + n = \frac{n(n + 1)}{2}$}

> In this type of induction expression that does not introduce a variable $k$ for induction, we need to substitute for "the equality also holds for $n + 1$", but this does not require extra calculation because the expression after substitution has already been obtained in the previous step.

#### Comprehensive Examples

> **Theorem 4** (Schröder-Bernstein's Theorem). If $f: A \to B$ and $g: B \to A$ are both injections, then there is a bijection from $A$ into $B$.
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
> - $\forall d \in D. \exists c \in C. g(d) = c$.
  As $g$ is an injection from $B$ into $A$, $\exists c \in A, g(d) = c$.
  Let prove $c \notin C_n$.
  Suppose $c \in C_n$.
  	- $n = 0$, Obviously contradiction.
  	- $n = m + 1$, $c \in C_{m+1} \Rightarrow d \in D_m$, contradiction.
  Therefore, $c \in C$.
> - $\forall c \in C. \exists d \in D. g(d) = c$.
  $\exists d \in B. g(d) = c$. Otherwise, $c \in C_0$, contradiction.
  Let’s prove $d \notin D_n$.
  Suppose $d \in D_n$, so that $c \in C_{n+1}$, contradiction.
  Therefore, $d \in D$.
  Qed.

This examples involves constructive proving, inductive definition, case analysis and proof by contradiction.

[Hint] {Theorem 4 (Schröder-Bernstein's Theorem)}
[Fix] {$A, B$} such that {$A, B$ are sets}
{
	[Fix] {$f, g$} such that {$f: A \to B$ is an injection}; {$g: B \to A$ is an injection}
	{
		[Show] {there is a bijection from $A$ into $B$}
		{
			[Define] {$C_0$} as {$\{ a \in A \mid \forall b \in B, g(b) \neq a \}$}
			[Define] {$D_0$} as {$\{ f(a) \mid a \in C_0 \}$}
			[Define] {$C_1$} as {$\{ a \in A \setminus C_0 \mid \forall b \in B \setminus D_0, g(b) \neq a \}$}
			[Have] {$C_1 = \{ g(b) \mid b \in D_0 \}$}
			[Define] {$D_1$} as {$\{ f(a) \mid a \in C_1 \}$}
			[Define] {set sequence $\{C_{n}\}$} as {$\forall n>1,C_{n+1}=\{ a \in A \setminus \bigcup_{i=0}^{n} C_i \mid \forall b \in B \setminus \bigcup_{i=0}^{n} D_i, g(b) \neq a \}$}
			[Define] {set sequence $\{D_{n}\}$} as {$\forall n>1,D_{n+1}=\{ f(a) \mid a \in C_{n+1} \}$}
			[Have] {$\forall n \in \N, C_{n+1} = \{ g(b) \mid b \in D_n \}$} by {similarly}
			[Define] {$h$} as {function $h: A \to B$ such that for any $a \in A$, $h(a) := \begin{cases} f(a), & \text{if } a \in \bigcup_{i=0}^{\infty} C_i \\ b, \text{ such that } g(b) = a, & \text{if } a \in A \setminus \bigcup_{i=0}^{\infty} C_i \end{cases}$}
			[Have] {$\forall n$, the restriction of $f$ to $C_n$ is a bijection onto $D_n$}
			[Define] {$C$} as {$A \setminus \bigcup_{i=0}^{\infty} C_i$}
			[Define] {$D$} as {$B \setminus \bigcup_{i=0}^{\infty} D_i$}
			[SufficeToProve] {$\forall d \in D. \, \exists c \in C. \, g(d) = c$};{$\forall c \in C. \, \exists d \in D. \, g(d) = c$.}
			[Show] {$\forall d \in D. \, \exists c \in C. \, g(d) = c$}
			{
				[Fix] {$d$} such that {$d \in D$}
				{
					[Obtain] {$c$} such that {$c \in A$}; {$g(d) = c$} by {$g$ is a function from $B$ into $A$}
					[Show] {$\forall n,c \notin C_n$} using {contradiction}
					{
						[Fix] {$n$} such that $n \in \N$
						{
							[Assume] {$c \in C_n$}
							{
								[Assume] {$n=0$}
								{
									[Have] {contradiction}
								}
								[Assume] {$n=m+1$ for some $m \in \N$}
								{
									[Have] {$c \in C_{m+1}\implies d \in D_m$}
									[Have] {contradiction}
								}
							}
						}
					}
					[Have] {$c \in C$}
				}
				[Show] {$\forall c \in C, \exists d \in D, g(d) = c$}
				{
					[Fix] {$c$} such that {$c \in C$}
					{
						[Obtain] {$d$} such that {$d \in B$}; {$g(d) = c$} by {otherwise $c \in C_0$, contradiction}
						[Show] {$\forall n,d \notin D_n$} using {contradiction}
						{
							[Fix] {$n$} such that $n \in \N$
							{
								[Assume] {$d \in D_n$}
								{
									[Have] {$c \in C_{n+1}$}
									[Have] {contradiction}
								}
							}
						}
						[Have] {$d \in D$}
					}
				}
			}
		}
	}
}

Here's another comprehensive example in Group Theory:

> **Theorem**
>
> Let $G$ be a group which acts on a finite set $X$.
>
> Let $x \in X$.
>
> Let $\text{Orb}(x)$ denote the orbit of $x$.
>
> Let $\text{Stab}(x)$ denote the stabilizer of $x$ by $G$.
>
> Let $[G : \text{Stab}(x)]$ denote the index of $\text{Stab}(x)$ in $G$.
>
> Then:
>
> $$|\text{Orb}(x)| = [G : \text{Stab}(x)] = \frac{|G|}{|\text{Stab}(x)|}$$
>
> **Proof**
>
> Let us define the mapping:
>
> $a : G \to \text{Orb}(x)$
>
> such that:
>
> $a(g) = g * x$
>
> where $*$ denotes the group action.
>
> It is clear that $a$ is surjective, because from the definition $x$ was acted on by all the elements of $G$.
>
> Next, from Stabilizer is Subgroup: Corollary:
>
> $a(g) = a(h) \iff g^{-1}h \in \text{Stab}(x)$
>
> This means:
>
> $g \equiv h \pmod{\text{Stab}(x)}$
>
> Thus there is a well-defined bijection:
>
> $G / \text{Stab}(x) \to \text{Orb}(x)$
>
> given by:
>
> $g \text{Stab}(x) \mapsto g * x$
>
> So $\text{Orb}(x)$ has the same number of elements as $G / \text{Stab}(x)$.
>
> That is:
>
> $|\text{Orb}(x)| = [G : \text{Stab}(x)]$
>
> The result follows.

[Hint] {Theorem}
[Fix] {$G$, $X$} such that {$G$ is a group}; {$X$ is a finite set}; {$G$ acts on $X$}
{
	[Fix] {$x$} such that {$x \in X$}
	{
		[Define] {$\text{Orb}(x)$} as {the orbit of $x$}
		[Define] {$\text{Stab}(x)$} as {the stabilizer of $x$ by $G$}
		[Define] {$[G : \text{Stab}(x)]$} as {the index of $\text{Stab}(x)$ in $G$}
		[Show] {$|\text{Orb}(x)| = [G : \text{Stab}(x)] = \frac{|G|}{|\text{Stab}(x)|}$}
		{
			[Define] {$a$} as {the mapping $a: G \to \text{Orb}(x)$ such that $\forall g\in G,a(g) = g * x$, where $*$ denotes the group action}
			[Have] {$a$ is surjective} by {the definition x was acted on by all the elements of $G$}
			[Fix] {g,h} such that {$g, h \in G$}
			{
				[Have] {$a(g) = a(h) \iff g^{-1}h \in \text{Stab}(x)$} by {Stabilizer is Subgroup: Corollary}
				[Have] {$g^{-1}h \in \text{Stab}(x) \iff g \equiv h \pmod{\text{Stab}(x)}$}
			}
			[Have] {there is a well-defined bijection from $G / \text{Stab}(x)$ to $\text{Orb}(x)$ given by $g \text{Stab}(x) \mapsto g * x$}
			[Have] {$\text{Orb}(x)$ has the same number of elements as $G / \text{Stab}(x)$}
			[Have] {$|\text{Orb}(x)| = [G : \text{Stab}(x)]$}
			[Hint] {The result follows.}
		}
	}
}