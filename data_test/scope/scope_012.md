[Hint: "定义序列"]
[Define: "y_n" as ""$y_n=\left(1+\frac{1}{n}\right)^{n+1}$""]
[Show: "序列 $y_n$ 单调递减"]
{
    [Fix: {n} st "$n\ge 2$"]
    {
        [Hint: "利用伯努利不等式计算比值"]
        [Have: "$\displaystyle\frac{y_{n-1}}{y_n}=\left(1+\frac{1}{n^2-1}\right)^n\cdot\frac{n}{n+1}$"]
        [Have: "$\left(1+\frac{1}{n^2-1}\right)^n\ge 1+\frac{n}{n^2-1}$" by "Bernoulli 不等式"]
        [Have: "$\displaystyle\frac{y_{n-1}}{y_n}\ge \left(1+\frac{n}{n^2-1}\right)\cdot\frac{n}{n+1}$" by "前两式"]
        [Have: "$\left(1+\frac{n}{n^2-1}\right)\cdot\frac{n}{n+1}>\left(1+\frac{1}{n}\right)\cdot\frac{n}{n+1}$" by "$\frac{n}{n^2-1}>\frac{1}{n}$"]
        [Have: "$\left(1+\frac{1}{n}\right)\cdot\frac{n}{n+1}=1$"]
        [Have: "$\displaystyle\frac{y_{n-1}}{y_n}>1$" by "以上不等式"]
        [Have: "$y_{n-1}>y_n$" by "两边同乘 $y_n>0$"]
    }
    [Have: "序列 $y_n$ 单调递减" by "$\forall n\ge 2,\;y_{n-1}>y_n$"]
}