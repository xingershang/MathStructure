[Show: "there exists N in ℕ such that for all n > N, x_n < y_n"]
{
    [Fix: {x, y, A, B} st {"{x_n} convergent and \lim_{n\to\infty} x_n = A"; "{y_n} convergent and \lim_{n\to\infty} y_n = B"}]
    {
        [Assume: "A < B"]
        {
            [Fix: {C} st "A < C < B"]
            {
                [Fix: {N'} st "∀ n > N', |x_n - A| < C - A"]
                {
                    [Have: "for all n > N', x_n < C" by "|x_n - A| < C - A"]
                    [Fix: {N''} st "∀ n > N'', |y_n - B| < B - C"]
                    {
                        [Have: "for all n > N'', y_n > C" by "|y_n - B| < B - C"]
                        [Define: "N" as ""N = \max\{N', N''\}""]
                        [Have: "for all n > N, x_n < y_n" by {"n > N implies n > N' and n > N''"; "x_n < C"; "y_n > C"}]
                    }
                }
            }
        }
    }
}