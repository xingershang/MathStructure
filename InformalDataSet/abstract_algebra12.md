# Natural Language

**2.6.8 Theorem** Every principal ideal domain is a unique factorization domain. For short, PID implies UFD.

*Proof.* If $<a_1> \subseteq <a_2> \subseteq \ldots$, let $I = \cup_i <a_i>$. Then $I$ is an ideal, necessarily principal by hypothesis. If $I = <b>$ then $b$ belongs to some $<a_n>$, so $I \subseteq <a_n>$. Thus if $i \geq n$ we have $<a_i> \subseteq I \subseteq <a_n> \subseteq <a_i>$. Therefore $<a_i> = <a_n>$ for all $i \geq n$, so that $R$ satisfies the acc on principal ideals.

Now suppose that $a$ is irreducible. Then $<a>$ is a proper ideal, for if $<a> = R$ then $1 \in <a>$, so that $a$ is a unit. By the acc on principal ideals, $<a>$ is contained in a maximal ideal $I$. (Note that we need not appeal to the general result (2.4.2), which uses Zorn’s lemma.) If $I = <b>$ then $b$ divides the irreducible element $a$, and $b$ is not a unit since $I$ is proper. Thus $a$ and $b$ are associates, so $<a> = <b> = I$. But $I$, a maximal ideal, is prime by (2.4.6), hence $a$ is prime. The result follows from (2.6.6). ♣