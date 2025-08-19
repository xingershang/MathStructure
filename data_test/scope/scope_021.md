[Show: "$\lim\limits_{n\to\infty}\dfrac{n}{n+3}=1$"]
{
    [Define: "$x_n$" as """$x_n=\dfrac{n}{n+3}$"""]
    [Fix: {$\varepsilon$} st "$\varepsilon>0$"]
    {
        [Have: "$\left|\dfrac{n}{n+3}-1\right|=\left|\dfrac{n-(n+3)}{n+3}\right|=\left|\dfrac{-3}{n+3}\right|=\dfrac{3}{n+3}$"]
        [ToHave: "$\left|\dfrac{n}{n+3}-1\right|<\varepsilon$"]
        {
            [OnlyNeeds: "$\dfrac{3}{n+3}<\varepsilon$"]
            [OnlyNeeds: "$n>\dfrac{3}{\varepsilon}-3$" by "化不等式得"]
        }
        [Find: {$N$} st "$N=\left\lceil\dfrac{3}{\varepsilon}\right\rceil-3$"]
        {
            [Have: "当 $n>N$ 时，$\left|\dfrac{n}{n+3}-1\right|=\dfrac{3}{n+3}<\varepsilon$" by "$n>N\Rightarrow n>\dfrac{3}{\varepsilon}-3$"]
            [Have: "$\lim\limits_{n\to\infty}\dfrac{n}{n+3}=1$" by "极限定义"]
        }
    }
}