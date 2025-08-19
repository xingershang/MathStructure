[Show: "$\exists\,\xi\in(a,b),\;f(\xi)=0$"]
{
    [Fix: {f, a, b} st {"$f$ 在 $[a,b]$ 上连续"; "$f(a)\,f(b)<0$"}]
    {
        [Assume: {"$f(a)<0$"; "$f(b)>0$"}]
        {
            [Define: "V" as ""$V=\{x\in[a,b]\mid f(x)<0\}$""]
            [Have: "$V$ 非空且有界" by "显然"]
            [Define: "\xi" as ""$\xi=\sup V$""]
            [Have: "存在 $\delta_1>0$ 使得 $\forall x\in[a,a+\delta_1],\;f(x)<0$" by "$f$ 在 $a$ 处连续且 $f(a)<0$"]
            [Have: "存在 $\delta_2>0$ 使得 $\forall x\in[b-\delta_2,b],\;f(x)>0$" by "$f$ 在 $b$ 处连续且 $f(b)>0$"]
            [Have: "$a+\delta_1\le \xi\le b-\delta_2$" by "上两式及 $\xi=\sup V$"]
            [Have: "$\xi\in(a,b)$" by "$a+\delta_1\le\xi\le b-\delta_2$"]
            [Fix: {x_n} st {"$x_n\in V$"; "$x_n\to\xi$"}]
            {
                [Have: "$f(\xi)=\lim_{n\to\infty}f(x_n)\le 0$" by "$f$ 连续于 $\xi$；$f(x_n)<0$"]
                [Assume: "$f(\xi)<0$"]
                {
                    [Have: "存在 $\delta>0$ 使得 $\forall x\in(\xi-\delta,\xi+\delta),\;f(x)<0$" by "$f$ 连续且 $f(\xi)<0$"]
                    [Have: "与 $\xi=\sup V$ 矛盾"]
                }
            }
            [Have: "$f(\xi)=0$" by "反证法得到"]
        }
    }
}