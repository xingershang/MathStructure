[Show: {"$f(x)=\sin x$ 在 $(-\infty,+\infty)$ 上连续"; "$f(x)=\sin x$ 在 $(-\infty,+\infty)$ 上一致连续"}]
{
    [Define: "f" as ""$f(x)=\sin x$""]
    [Have: "$|\sin x' - \sin x''| = 2\left|\cos \dfrac{x'+x''}{2}\,\sin \dfrac{x'-x''}{2}\right| \le |x'-x''|"]
    [Fix: {\varepsilon} st "$\varepsilon>0$"]
    {
        [Define: "\delta" as ""$\delta=\varepsilon$""]
        [Fix: {x', x''} st "$x',x''\in(-\infty,+\infty)$"]
        {
            [Have: "如果 $|x'-x''|<\delta$，则 $|\sin x'-\sin x''|<\varepsilon$"]
        }
        [Have: "$\sin x$ 在 $(-\infty,+\infty)$ 上一致连续" by "定义"]
    }
}