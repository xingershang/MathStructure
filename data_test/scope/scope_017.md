[Show: "f takes on any value between its maximum value M and its minimum value m on [a,b]"]
{
    [Fix: {a, b, f} st "f(x) is continuous on [a,b]"]
    {
        [Define: "M" as ""M = max{ f(x) | x ∈ [a,b] }""]
        [Define: "m" as ""m = min{ f(x) | x ∈ [a,b] }""]
        [Have: "there exist ξ,η ∈ [a,b] such that f(ξ)=m, f(η)=M" by "Extreme Value Theorem"]
        [Fix: {ξ, η} st {"ξ,η ∈ [a,b]"; "f(ξ)=m"; "f(η)=M"}]
        {
            [Assume: "ξ < η"]
            {
                [Fix: {C} st "m < C < M"]
                {
                    [Define: "φ" as ""φ(x) = f(x) - C""]
                    [Have: "φ(x) is continuous on [ξ,η]"]
                    [Have: {"φ(ξ)=f(ξ)-C<0"; "φ(η)=f(η)-C>0"}]
                    [Have: "there exists ζ ∈ (ξ,η) such that φ(ζ)=0" by "Intermediate Value Theorem"]
                    [Fix: {ζ} st {"ζ ∈ (ξ,η)"; "φ(ζ)=0"}]
                    {
                        [Have: "f(ζ)=C"]
                    }
                }
            }
        }
    }
}