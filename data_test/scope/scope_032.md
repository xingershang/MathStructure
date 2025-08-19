[Fix: {b, n} st {"b,n>1 整数"; "对每个 k>1 , 存在整数 a_k 使得 k | (b-a_k^n)"}]
{
    [Show: "存在整数 A 使 b=A^n"]
    {
        [Fix: {p_1, \ldots , p_s,  \alpha_1, \ldots , \alpha_s} st {"b = p_1^{\alpha_1}\cdots p_s^{\alpha_s}"; "p_1,\ldots ,p_s 不同质数"}]
        {
            [Hint: "我们的目标是证明所有 \alpha_i 都能被 n 整除, 于是可设 A = p_1^{\alpha_1/n}\cdots p_s^{\alpha_s/n}"]
            [Fix: {k} st "k = b^2"]
            {
                [Fix: {a_k} st "b-a_k^n 可被 k 整除"]
                {
                    [Have: "b-a_k^n 可被 b^2 整除" by {"k=b^2"; "定义 a_k"}]
                    [Have: "对每个 i, b-a_k^n 可被 p_i^{2\alpha_i} 整除" by {"b-a_k^n 可被 b^2 整除"; "b = \prod p_i^{\alpha_i}"}]
                    [Have: "a_k^n \equiv b \equiv 0 \pmod{p_i^{\alpha_i}}" by {"p_i^{\alpha_i} | b"; "p_i^{2\alpha_i} | (b-a_k^n)"}]
                    [Have: "a_k^n \not\equiv 0 \pmod{p_i^{\alpha_i+1}}" by {"p_i^{\alpha_i+1} \nmid b"; "p_i^{2\alpha_i} > p_i^{\alpha_i}"}]
                    [Have: "a_k^n 的 p_i-指数为 \alpha_i" by "上两式同模比较"]
                    [Have: "\alpha_i 能被 n 整除" by "a_k^n 是 n 次幂"]
                }
            }
            [Have: "所有 \alpha_i 都能被 n 整除" by "对每个 i 都成立"]
            [Have: "b=A^n 对某个整数 A 成立" by "b 的质因数分解中各指数均被 n 整除"]
        }
    }
}