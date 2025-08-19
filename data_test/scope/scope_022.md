[Show: {"$\lim_{x\to x_0}f(x)=A$"; "$\lim_{x\to x_0}g(x)=B$"; "$A>B$"}]
{
    [Show: "存在 $\delta>0$ ，使得当 $0<|x-x_0|<\delta$ 时 $f(x)>g(x)$"]
    {
        [Define: "$\epsilon_0$" as ""$\epsilon_0=\dfrac{A-B}{2}$""]
        [Have: "$\epsilon_0>0$"]
        [Have: "存在 $\delta_1>0$ ，当 $0<|x-x_0|<\delta_1$ 时有 $|f(x)-A|<\epsilon_0$" by "$\lim_{x\to x_0}f(x)=A$"]
        [Have: "当 $0<|x-x_0|<\delta_1$ 时 $f(x)>(A+B)/2$" by "$|f(x)-A|<\epsilon_0$"]
        [Have: "存在 $\delta_2>0$ ，当 $0<|x-x_0|<\delta_2$ 时有 $|g(x)-B|<\epsilon_0$" by "$\lim_{x\to x_0}g(x)=B$"]
        [Have: "当 $0<|x-x_0|<\delta_2$ 时 $g(x)<(A+B)/2$" by "$|g(x)-B|<\epsilon_0$"]
        [Define: "$\delta$" as ""$\delta=\min\{\delta_1,\delta_2\}$""]
        [Have: "当 $0<|x-x_0|<\delta$ 时 $g(x)<(A+B)/2<f(x)$"]
        [Have: "当 $0<|x-x_0|<\delta$ 时 $f(x)>g(x)$"]
    }
}