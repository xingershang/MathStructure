[Hint: "A sequence $x_n$ is defined"]
[Define: "x_n" as "{"$x_1 = 1$"; "$x_{2k} = -x_k$"; "$x_{2k-1} = (-1)^{k+1}x_k$  for all  $k\ge 1$"}"]
[Show: "对所有 $n\ge 1,\;x_1+\cdots +x_n\ge 0"]
{
    [Hint: "We start with some observations."]
    [Have: {"$x_{4k-3}=x_{2k-1}=-x_{4k-2}$"; "$x_{4k-1}=x_{4k}=-x_{2k}=x_k$"} by "definition of $x_i$"]
    [Define: "S_n" as ""$S_n=\sum_{i=1}^{n}x_i$""]
    [Have: "$S_{4k}=2S_k$"]
    [Have: "$S_{4k+2}=S_{4k}$"]
    [Have: "$S_n\equiv n \; (\mathrm{mod}\,2)$"]
    [Hint: "We prove by induction on $k$ that $S_i\ge 0$ for all $i\le 4k$."]
    [Have: "$S_1=1,\;S_2=0,\;S_3=1,\;S_4=2\;(\text{so }S_i\ge 0\text{ for }i\le 4)$" by "direct calculation"]
    [Assume: "$S_i\ge 0$ for all $i\le 4k$ (induction hypothesis)"]
    {
        [Have: "$S_{4k+4}=2S_{k+1}\ge 0" by "$S_{4k}=2S_k$ pattern"]
        [Have: "$S_{4k+2}=S_{4k}\ge 0"]
        [Have: "$S_{4k+3}=\dfrac{S_{4k+2}+S_{4k+4}}{2}\ge 0"]
        [Hint: "It remains to check $S_{4k+1}\ge 0$."]
        [Assume: "$k$ is odd"]
        {
            [Have: "$S_{4k}=2S_k\ge 2\Rightarrow S_{4k+1}=S_{4k}+x_{4k+1}\ge 1"]
        }
        [Assume: "$k$ is even"]
        {
            [Have: "$x_{4k+1}=x_{k+1},\;S_{4k+1}=S_k+S_{k+1}\ge 0"]
        }
    }
    [Hint: "Induction complete; thus $S_n\ge 0$ for all $n$."]
}