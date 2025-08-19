[Fix: {α} st "$\alpha>-1$"]
{
    [Fix: {n} st "$n\in\mathbb{N}$"]
    {
        [Show: "$(1+\alpha)^n\ge 1+n\alpha$"]
        {
            [Have: "$(1+\alpha)^1\ge 1+1\alpha$" by "$n=1$"]
            [Assume: "$(1+\alpha)^n\ge 1+n\alpha$"]
            {
                [Show: "$(1+\alpha)^{n+1}\ge 1+(n+1)\alpha$"]
                {
                    [Have: "$(1+\alpha)^{n+1}=(1+\alpha)(1+\alpha)^n\ge(1+\alpha)(1+n\alpha)=1+(n+1)\alpha+n\alpha^2\ge 1+(n+1)\alpha$" by "计算"]
                }
            }
            [Have: "对所有$n\in\mathbb{N}$, $(1+\alpha)^n\ge 1+n\alpha$" by "数学归纳法"]
        }
        [Have: "若$\alpha\neq 0$且$n>1$则严格不等式成立" by "同上计算"]
    }
}