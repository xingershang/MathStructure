[Hint] {Theorem}
[Fix] {$G$; $X$} such that {$G$ is a group; $X$ is a finite set; $G$ acts on $X$}
{
    [Fix] {$x$} such that {$x \in X$}
    {
        [Define] {$\text{Orb}(x)$} as {the orbit of $x$}
        [Define] {$\text{Stab}(x)$} as {the stabilizer of $x$ by $G$}
        [Define] {$[G : \text{Stab}(x)]$} as {the index of $\text{Stab}(x)$ in $G$}
        [Show] {$|\text{Orb}(x)| = [G : \text{Stab}(x)] = \frac{|G|}{|\text{Stab}(x)|}$}
        {
            [Define] {$a$} as {the mapping $a: G \to \text{Orb}(x)$ such that $a(g) = g * x$}
            [Have] {$a$ is surjective} by {from the definition $x$ was acted on by all the elements of $G$}
            [Have] {$\forall g, h \in G, a(g) = a(h) \iff g^{-1}h \in \text{Stab}(x)$} by {Stabilizer is Subgroup: Corollary}
            [Have] {$\forall g, h \in G, a(g) = a(h) \iff g \equiv h \pmod{\text{Stab}(x)}$} by {This means}
            [Obtain] {a well-defined bijection $f$} such that {$f: G / \text{Stab}(x) \to \text{Orb}(x)$; The bijection is given by $g \text{Stab}(x) \mapsto g * x$} by {$\forall g, h \in G, a(g) = a(h) \iff g \equiv h \pmod{\text{Stab}(x)}$}
            [Have] {$\text{Orb}(x)$ has the same number of elements as $G / \text{Stab}(x)$} by {the existence of a well-defined bijection from $G / \text{Stab}(x)$ to $\text{Orb}(x)$}
            [Have] {$|\text{Orb}(x)| = [G : \text{Stab}(x)]$}
            [Have] {$|\text{Orb}(x)| = [G : \text{Stab}(x)] = \frac{|G|}{|\text{Stab}(x)|}$} by {The result follows}
        }
    }
}