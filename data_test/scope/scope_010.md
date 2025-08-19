[Fix: {q} st "q is any real number"]
{
    [Show: "lim_{n\to\infty} \dfrac{q^{n}}{n!}=0"]
    {
        [Assume: "q=0"]
        {
            [Have: "lim_{n\to\infty} \dfrac{q^{n}}{n!}=0" by "for n\ge 1, q^{n}=0"]
        }
        [Have: "\left|\dfrac{q^{n}}{n!}\right|=\dfrac{|q|^{n}}{n!}"]
        [Have: "It suffices to prove the assertion for q>0" by "previous equality"]
        [Assume: "q>0"]
        {
            [Define: "x_n" as ""x_{n}=\dfrac{q^{n}}{n!}""]
            [Have: "x_{n+1}=\dfrac{q}{n+1}\,x_{n}" by "algebraic calculation"]
            [Have: "There exists N\in\mathbb{N} such that 0<\dfrac{q}{n+1}<1\text{ for all }n>N" by "the natural numbers are unbounded above"]
            [Have: "For n>N,\;x_{n+1}<x_{n}" by "0<\dfrac{q}{n+1}<1"]
            [Have: "The limit \displaystyle\lim_{n\to\infty}x_{n}=x\text{ exists}" by "decreasing sequence bounded below by 0"]
            [Have: "x=\lim_{n\to\infty}x_{n+1}=\lim_{n\to\infty}\dfrac{q}{n+1}x_{n}=0\cdot x=0"]
            [Have: "lim_{n\to\infty} \dfrac{q^{n}}{n!}=0" by "x=0"]
        }
    }
}