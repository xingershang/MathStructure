[Show: {"$(a_n)_{n\geqslant1}$ 是正实数序列"; "对所有正整数 $n$ 有 $(a_{n+1})^2+a_na_{n+2}\leqslant a_n+a_{n+2}$"}]
{
    [Show: "$a_{2022}\leqslant1$"]
    {
        [Have: "$(a_{n+1})^{2}-1\leqslant a_{n}+a_{n+2}-a_{n}a_{n+2}-1"]
        [Have: "$(a_{n+1})^{2}-1\leqslant(1-a_n)(a_{n+2}-1)" by "等价变形"]
        [Assume: "存在正整数 $n$ 使得 $a_{n+1}>1$ 且 $a_{n+2}>1$"]
        {
            [Have: "$0<1-a_n<1<1+a_{n+2}$" by "$(a_{n+1})^{2}-1\leqslant(1-a_n)(a_{n+2}-1)$"]
            [Have: "$(a_{n+1})^{2}-1<(a_{n+2}+1)(a_{n+2}-1)=(a_{n+2})^{2}-1"]
            [Have: "$(a_{n+2})^{2}-1\leqslant(1-a_{n+3})(a_{n+1}-1)<(1+a_{n+1})(a_{n+1}-1)=(a_{n+1})^{2}-1"]
            [Have: "出现矛盾" by "上一组不等式互相冲突"]
        }
        [Have: "除 $a_1,a_2$ 外, 不存在两个连续项都严格大于 1" by "由矛盾得出"]
        [Assume: "$a_{2022}>1$"]
        {
            [Have: "$a_{2021}\leqslant1$ 且 $a_{2023}\leqslant1$" by "不能有两个连续项大于1"]
            [Have: "$0<(a_{2022})^{2}-1\leqslant(1-a_{2021})(a_{2023}-1)\leqslant0$"]
            [Have: "矛盾"]
        }
        [Have: "$a_{2022}\leqslant1$"]
    }
}