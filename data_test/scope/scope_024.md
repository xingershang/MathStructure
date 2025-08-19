[Show: "$f(x)=\sqrt{x(1-x)}$ 在闭区间$[0,1]$上连续"]
{
    [Hint: "Proof"]
    [Fix: {x_0} st "$x_0\in(0,1)$"]
    {
        [Define: "\eta" as """$\eta=\min\{x_0,1-x_0\}>0$"""]
        [Fix: {x} st {"$x\in(0,1)$"; "$|x-x_0|<\eta$"}]
        {
            [Have: "$|\sqrt{x(1-x)}-\sqrt{x_0(1-x_0)}|=\dfrac{|(1-x)-(1-x_0)|\,|x-x_0|}{\sqrt{x(1-x)}+\sqrt{x_0(1-x_0)}}<\dfrac{1}{\sqrt{x_0(1-x_0)}}|x-x_0|"]
        }
        [Fix: {\epsilon} st "$\epsilon>0$"]
        {
            [Define: "\delta" as """$\delta=\min\{\eta,\sqrt{x_0(1-x_0)}\,\epsilon\}$"""]
            [Fix: {x} st "$|x-x_0|<\delta$"]
            {
                [Have: "$|\sqrt{x(1-x)}-\sqrt{x_0(1-x_0)}|<\dfrac{1}{\sqrt{x_0(1-x_0)}}|x-x_0|<\epsilon$" by {"前一步不等式"; "$|x-x_0|<\delta\le\sqrt{x_0(1-x_0)}\,\epsilon$"}]
            }
        }
    }
    [Have: "$f(x)$ 在$(0,1)$上连续"]
    [Hint: "Now consider the endpoints."]
    [Fix: {\epsilon} st "$\epsilon>0$"]
    {
        [Define: "\delta" as """$\delta=\epsilon^2$"""]
        [Fix: {x} st "$0\le x<\delta$"]
        {
            [Have: "$|f(x)-f(0)|\le\sqrt{x}<\epsilon$"]
        }
        [Fix: {x} st "$1-\delta<x\le1$"]
        {
            [Have: "$|f(x)-f(1)|\le\sqrt{1-x}<\epsilon$"]
        }
    }
    [Have: "$f(x)$ 在$x=0$右连续且在$x=1$左连续"]
    [Have: "$f(x)=\sqrt{x(1-x)}$ 在闭区间$[0,1]$上连续"]
}