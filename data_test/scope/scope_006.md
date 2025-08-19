[Hint: "A sequence {x_n} is called a Cauchy sequence if for any ε>0 there exists N∈ℕ such that |x_m-x_n|<ε whenever m> N and n> N"]
[Show: "一个数列收敛当且仅当它是Cauchy数列"]
{
    [Assume: "$\lim_{n\to\infty}x_n=A$"]
    {
        [Fix: {\epsilon} st "$\epsilon>0$"]
        {
            [Have: "存在$N$使得当$n\ge N$时$|x_n-A|<\epsilon/2$" by "$\lim_{n\to\infty}x_n=A$"]
            [Have: "当$m> N,n> N$时$|x_m-x_n|\le |x_m-A|+|x_n-A|<\epsilon$" by "三角不等式"]
            [Have: "\{x_n\}是Cauchy数列" by "定义"]
        }
    }
    [Assume: "\{x_n\}是Cauchy数列"]
    {
        [Fix: {\epsilon} st "$\epsilon>0$"]
        {
            [Have: "存在$N$使得$m\ge N,k\ge N$时$|x_m-x_k|<\epsilon/3$" by "Cauchy性质"]
            [Have: "取$m=N$后,当$k>N$时,$x_N-\epsilon/3<x_k<x_N+\epsilon/3$" by "设$m=N$"]
            [Have: "\{x_n\}有界" by "上一步说明$\{x_n\}$从$N$以后被夹在有界区间内,前$N$项有限"]
            [Define: "$a_n$" as ""$a_n:=\inf_{k\ge n}x_k$""]
            [Define: "$b_n$" as ""$b_n:=\sup_{k\ge n}x_k$""]
            [Have: "$a_n\le a_{n+1}\le b_{n+1}\le b_n$" by "下确界上确界的单调性"]
            [Fix: {A} st "$A$属于所有闭区间$[a_n,b_n]$"]
            {
                [Have: "$a_n\le A\le b_n$对所有$n$成立" by "$A\in\bigcap[a_n,b_n]$"]
                [Have: "当$k\ge n$时$|A-x_k|\le b_n-a_n$" by "$x_k\in[a_n,b_n]$"]
                [Have: "当$n>N$时,$x_N-\epsilon/3\le a_n\le b_n\le x_N+\epsilon/3$" by "由第11步区间性质"]
                [Have: "当$n>N$时,$b_n-a_n\le 2\epsilon/3<\epsilon$" by "上一步"]
                [Have: "对任何$k>N$, $|A-x_k|<\epsilon$" by "步骤17和19"]
                [Have: "$\lim_{k\to\infty}x_k=A$" by "极限定义"]
            }
        }
        [Have: "因此, Cauchy数列必收敛, 与第一部分合起来得到收敛数列当且仅当它是Cauchy数列"]
    }
}