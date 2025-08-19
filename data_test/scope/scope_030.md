[Show: ]
{
    [Show: " \left(\sum_{k=1}^{n}\frac{1+x^{2k}}{1+x^{4k}}\right)\left(\sum_{k=1}^{n}\frac{1+y^{2k}}{1+y^{4k}}\right)<\frac{1}{(1-x)(1-y)} "]
    {
        [Fix: {t} st "0<t<1"]
        {
            [Have: " \frac{1+t^2}{1+t^4}=\frac{1}{t}-\frac{(1-t)(1-t^3)}{t(1+t^4)}<\frac{1}{t} "]
            [Have: " \frac{1+x^{2k}}{1+x^{4k}}<\frac{1}{x^{k}}\;(1\le k\le n)" by "令 t=x^{k} 于上式"]
            [Have: "0<\sum_{k=1}^{n}\frac{1+x^{2k}}{1+x^{4k}}<\sum_{k=1}^{n}\frac{1}{x^{k}}=\frac{1-x^{n}}{x^{n}(1-x)}" by "对 k 求和"]
            [Have: " \frac{1+y^{2k}}{1+y^{4k}}<\frac{1}{y^{k}}\;(1\le k\le n)" by "令 t=y^{k} 于上式"]
            [Have: "0<\sum_{k=1}^{n}\frac{1+y^{2k}}{1+y^{4k}}<\sum_{k=1}^{n}\frac{1}{y^{k}}=\frac{1-y^{n}}{y^{n}(1-y)}" by "对 k 求和"]
        }
        [Have: {"1-y^{n}=x^{n}"; "1-x^{n}=y^{n}"} by "x^{n}+y^{n}=1"]
        [Have: {" \frac{1-x^{n}}{x^{n}(1-x)}=\frac{y^{n}}{x^{n}(1-x)} "; " \frac{1-y^{n}}{y^{n}(1-y)}=\frac{x^{n}}{y^{n}(1-y)} "} by "上一命题"]
        [Have: " \left(\sum_{k=1}^{n}\frac{1+x^{2k}}{1+x^{4k}}\right)\left(\sum_{k=1}^{n}\frac{1+y^{2k}}{1+y^{4k}}\right)<\frac{y^{n}}{x^{n}(1-x)}\cdot\frac{x^{n}}{y^{n}(1-y)}=\frac{1}{(1-x)(1-y)} " by "组合前述不等式"]
    }
}