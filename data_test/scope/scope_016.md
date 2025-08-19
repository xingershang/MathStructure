[Show: "f(x)=x^2"]
{
    [Show: {"f is not uniformly continuous on [0,+∞)"; "f is uniformly continuous on [0,A] for any finite positive number A"}]
    {
        [Define: "x_n'" as ""x_n' = \sqrt{n+1}\;(n=1,2,3,\ldots)""]
        [Define: "x_n''" as ""x_n'' = \sqrt{n}\;(n=1,2,3,\ldots)""]
        [Have: "lim_{n\to\infty}(x_n' - x_n'') = 0"]
        [Have: "lim_{n\to\infty}(f(x_n') - f(x_n'')) = 1"]
        [Have: "f is not uniformly continuous on [0,+∞)" by "Example 3.4.5 and the two limits above"]
        [Fix: {A} st "A>0\;\text{finite}"]
        {
            [Show: "f is uniformly continuous on [0,A]"]
            {
                [Have: "|x'^2 - x''^2| = |(x' + x'')(x' - x'')| \le 2A |x' - x''|"]
                [Fix: {ε} st "ε>0"]
                {
                    [Define: "δ" as ""δ = ε / (2A)""]
                    [Have: "如果 x',x''∈[0,A] 且 |x'-x''|<δ, 则 |x'^2 - x''^2|<ε"]
                    [Have: "f is uniformly continuous on [0,A]" by "definition of uniform continuity and the inequality above"]
                }
            }
        }
    }
}