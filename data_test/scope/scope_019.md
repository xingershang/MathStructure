[Assume: ]
{
    [Show: "$\displaystyle \frac{a_1+\cdots+a_n}{n}\ge \sqrt[n]{a_1a_2\cdots a_n}\ge n\Bigl(\frac1{a_1}+\cdots+\frac1{a_n}\Bigr)^{-1}$，且当且仅当 $a_1=a_2=\cdots=a_n$ 时取等号"]
    {
        [Hint: "首先证明左边的不等式"]
        [Show: "$\displaystyle \frac{a_1+\cdots+a_n}{n}\ge \sqrt[n]{a_1a_2\cdots a_n}$"]
        {
            [Have: "当 $n=1,2$ 时，上式显然成立"]
            [Have: "当 $n=2^k\;(k\in\mathbb N^*)$ 时，不等式成立" by "$\displaystyle \frac{a+b}{2}\ge\sqrt{ab}$ 的迭代应用"]
            [Fix: {l} st "$2^{l-1}<n<2^{l}$"]
            {
                [Define: "\bar a" as ""$\bar a=\sqrt[n]{a_1a_2\cdots a_n}$""]
                [Hint: "补上 $(2^l-n)$ 个 $\bar a$ 以得到 $2^l$ 个正整数"]
                [Have: "$\displaystyle \frac1{2^{l}}\bigl(a_1+\cdots+a_n+(2^{l}-n)\bar a\bigr)\ge \bar a$" by "将不等式应用于这 $2^{l}$ 个正整数"]
                [Have: "$\displaystyle \frac{a_1+\cdots+a_n}{n}\ge \sqrt[n]{a_1a_2\cdots a_n}$" by "整理上式"]
            }
        }
        [Have: "$\displaystyle \sqrt[n]{a_1a_2\cdots a_n}\ge n\Bigl(\frac1{a_1}+\cdots+\frac1{a_n}\Bigr)^{-1}$" by "把结论应用于 $\frac1{a_1},\frac1{a_2},\ldots,\frac1{a_n}$"]
    }
}