设 $\{x_n\}$是实数上的数列，满足$\forall n\geq 1,{x}_{n} = \frac{n}{n + 1}$。请证明：$\mathop{\lim }\limits_{{n \rightarrow  \infty }}{x}_{n} = 1$。

Pf: 

我们有 $\forall n\geq 1, \left| {{x}_{n} - 1}\right|  = \frac{1}{n + 1}$.

对于任意的 $\varepsilon  > 0$ , 我们可以取$N  = \left\lbrack  \frac{1}{\varepsilon }\right\rbrack$。我们证明$\forall n>N,|x_n-1|<\varepsilon$。只需证$\frac{1}{n + 1} < \varepsilon$。只需证 $n > \frac{1}{\varepsilon } - 1$。我们有$n>\left\lbrack  \frac{1}{\varepsilon }\right\rbrack$，得证。

所以, $\mathop{\lim }\limits_{{n \rightarrow  \infty }}{x}_{n} = 1$ .

Qed.