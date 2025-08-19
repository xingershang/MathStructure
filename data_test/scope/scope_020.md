[Assume: "T = { x \mid x \in \mathbb{Q}, x>0, x^2<2 }"]
{
    [Show: "T has no least upper bound in \mathbb{Q}"]
    {
        [Assume: "T has a least upper bound in \mathbb{Q}"]
        {
            [Fix: {m, n} st {"m,n\in\mathbb{N}^*"; "m,n \text{ are coprime}"; "\sup T = \dfrac{n}{m}"}]
            {
                [Have: "1 < \left(\dfrac{n}{m}\right)^2 < 3"]
                [Have: "The square of a rational number cannot be 2"]
                [Hint: "There are two possible cases"]
                [Assume: "1 < \left(\dfrac{n}{m}\right)^2 < 2"]
                {
                    [Define: "t" as "{"\dfrac{n^2}{m^2} = 2 - t"; "0 < t < 1"}"]
                    [Define: "r" as ""r = \dfrac{n}{6m}""]
                    [Have: {"n + r > 0"; "\dfrac{n+r}{m} \in \mathbb{Q}"}]
                    [Have: {"\dfrac{n^2}{3m^2} t < \dfrac{2}{3}"; "\dfrac{2n}{m} - r < \dfrac{n}{18} t"}]
                    [Have: "\left(\dfrac{n+r}{m}\right)^2 = 2 - t + \dfrac{2n}{m} r + r^2 < 2"]
                    [Have: "\dfrac{n+r}{m} \in T"]
                    [Have: "This contradicts that \dfrac{n}{m} is the least upper bound of T"]
                }
                [Assume: "2 < \left(\dfrac{n}{m}\right)^2 < 3"]
                {
                    [Define: "t" as "{"\dfrac{n^2}{m^2} = 2 + t"; "0 < t < 1"}"]
                    [Define: "r" as ""r = \dfrac{n}{6m}""]
                    [Have: {"n - r > 0"; "\dfrac{n-r}{m} \in \mathbb{Q}"}]
                    [Have: "\dfrac{2n}{m} - r < \dfrac{n^2}{3m^2} t < 1"]
                    [Have: "\left(\dfrac{n-r}{m}\right)^2 = 2 + t - \dfrac{2n}{m} r + r^2 > 2"]
                    [Have: "\dfrac{n-r}{m} \in T"]
                    [Have: "This contradicts that \dfrac{n}{m} is the least upper bound of T"]
                }
            }
        }
        [Have: "Therefore, T has no least upper bound in \mathbb{Q}"]
    }
}