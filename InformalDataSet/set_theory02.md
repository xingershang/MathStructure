# Natural Language

## Goal

$A \times \bigcup B = \bigcup \{A \times X \mid X \in B\}$

## Proof

  - ($\subseteq$): Let $(a, x) \in A \times \bigcup B$. By definition, $x \in \bigcup B$, so there exists $X \in B$ such that $x \in X$. Therefore, $(a, x) \in A \times X$. Since $A \times X$ is part of the union $\bigcup \{A \times X \mid X \in B\}$, we conclude $(a, x) \in \bigcup \{A \times X \mid X \in B\}$.

  - ($\supseteq$): Let $(a, x) \in \bigcup \{A \times X \mid X \in B\}$. Then there exists $X \in B$ such that $(a, x) \in A \times X$. By definition of Cartesian product, $a \in A$ and $x \in X$. Since $X \in B$, we have $x \in \bigcup B$. Thus, $(a, x) \in A \times \bigcup B$.

Hence, $A \times \bigcup B = \bigcup \{A \times X \mid X \in B\}$.

# Structure

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