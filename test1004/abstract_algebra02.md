**Theorem**

Let $G$ be a group which acts on a finite set $X$.

Let $x \in X$.

Let $\text{Orb}(x)$ denote the orbit of $x$.

Let $\text{Stab}(x)$ denote the stabilizer of $x$ by $G$.

Let $[G : \text{Stab}(x)]$ denote the index of $\text{Stab}(x)$ in $G$.

Then:

$$|\text{Orb}(x)| = [G : \text{Stab}(x)] = \frac{|G|}{|\text{Stab}(x)|}$$

**Proof**

Let us define the mapping:

$a : G \to \text{Orb}(x)$

such that:

$a(g) = g * x$

where $*$ denotes the group action.

It is clear that $a$ is surjective, because from the definition $x$ was acted on by all the elements of $G$.

Next, from Stabilizer is Subgroup: Corollary:

$a(g) = a(h) \iff g^{-1}h \in \text{Stab}(x)$

This means:

$g \equiv h \pmod{\text{Stab}(x)}$

Thus there is a well-defined bijection:

$G / \text{Stab}(x) \to \text{Orb}(x)$

given by:

$g \text{Stab}(x) \mapsto g * x$

So $\text{Orb}(x)$ has the same number of elements as $G / \text{Stab}(x)$.

That is:

$|\text{Orb}(x)| = [G : \text{Stab}(x)]$

The result follows.

# Structure

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