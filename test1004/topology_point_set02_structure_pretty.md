[Hint] {Lemma 13.1.}
[Fix] {$X$; $\mathcal{B}$; $\mathcal{T}$} such that {$X$ is a set; $\mathcal{B}$ is a basis for a topology $\mathcal{T}$ on $X$}
{
    [Show] {$\mathcal{T}$ equals the collection of all unions of elements of $\mathcal{B}$} using {set equality}
    {
        [Show] {Any union of elements of $\mathcal{B}$ is in $\mathcal{T}$}
        {
            [Fix] {$\mathcal{C}$} such that {$\mathcal{C}$ is a collection of elements of $\mathcal{B}$}
            {
                [Have] {The elements of $\mathcal{C}$ are also elements of $\mathcal{T}$}
                [Have] {The union of the elements of $\mathcal{C}$ is in $\mathcal{T}$} by {$\mathcal{T}$ is a topology}
            }
        }
        [Show] {Any element of $\mathcal{T}$ is a union of elements of $\mathcal{B}$}
        {
            [Fix] {$U$} such that {$U \in \mathcal{T}$}
            {
                [Obtain] {collection $\{B_x\}_{x \in U}$} such that {$\forall x \in U, B_x \in \mathcal{B}$; $\forall x \in U, x \in B_x \subset U$}
                [Have] {$U = \bigcup_{x \in U} B_x$}
                [Have] {$U$ equals a union of elements of $\mathcal{B}$}
            }
        }
    }
}