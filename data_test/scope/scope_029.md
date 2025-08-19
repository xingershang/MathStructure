[Assume: ]
{
    [Assume: "n! \mid \prod_{p<q\le n}(p+q)"]
    {
        [Fix: {p_1, ..., p_m} st "2=p_1<p_2<\dots<p_m\le n 为不超过 n 的所有质数"]
        {
            [Have: "每个质数 p_i 都整除 n!" by "p_i\le n"]
            [Have: "存在 i<j 使得 p_m \mid p_i+p_j" by "p_m\mid \prod_{p<q\le n}(p+q)"]
            [Have: "0<\dfrac{p_i+p_j}{p_m}<2"]
            [Have: "p_m=p_i+p_j,\; m\ge 3,\; p_i=2,\; p_m=2+p_j=2+p_{m-1}" by "上一式取值位于 (0,2)"]
            [Have: "存在 k<l 使得 p_{m-1}\mid p_k+p_l" by "p_{m-1}\mid \prod_{p<q\le n}(p+q)"]
            [Have: "0<\dfrac{p_k+p_l}{p_{m-1}}<3"]
            [Have: "要么 p_m-1=p_k+p_l, 要么 2p_{m-1}=p_k+p_l" by "值位于 (0,3)"]
            [Have: "若 p_m-1=p_k+p_l, 则 p_m-1=2+p_{m-2}"]
            [Have: "若 2p_{m-1}=p_k+p_l, 则 p_{m-1}=p_l+2=p_{m-2}+2"]
            [Have: {"无论哪种情况, p_{m-2}>2 且 3\mid p_{m-2}(=3)\text{ 或 }p_{m-1}=p_{m-2}+2\text{ 或 }p_m=p_{m-2}+4"; "因此 p_{m-2}=3,\; p_m=7,\; 7\le n<11"}]
        }
        [Have: {"7! \mid \prod_{p<q\le 7}(p+q)"; "8! \nmid \prod_{p<q\le 8}(p+q)"; "9!,10! 亦不整除相应乘积"} by "直接计算"]
        [Have: "故仅当 n=7 时有 n! \mid \prod_{p<q\le n}(p+q)"]
    }
}