【90】证明: 若单调数列的某一子数列收敛, 则此单调数列本身是收敛的.

证 不失一般性,假设数列 $\left\{  {x}_{n}\right\}$ 单调增加,其一子数列 $\left\{  {x}_{{p}_{n}}\right\}$ 收敛于 $a$ . 则对于任给的 $\varepsilon  > 0$ ,存在正整数 $N$ ,使当 $k > N$ 时, $\left| {{x}_{{p}_{k}} - a}\right|  < \varepsilon$ ,令 ${N}^{\prime } = {p}_{N + 1}$ . 设 $n > {N}^{\prime }$ ,由于 ${p}_{1} < {p}_{2} < {p}_{3} < \cdots  \rightarrow   + \infty$ ,故必有 ${p}_{k}\left( {k > N}\right)$ 使 ${p}_{k} \leq  n < {p}_{k + 1}$ . 由上知

$$
\left| {{x}_{{p}_{k}} - a}\right|  < \varepsilon ,\;\left| {{x}_{{p}_{k + 1}} - a}\right|  < \varepsilon .
$$

而 ${x}_{{p}_{k}} \leq  {x}_{n} \leq  {x}_{{p}_{k + 1}}$ (因 ${x}_{n}$ 递增),故必 $\left| {{x}_{n} - a}\right|  < \varepsilon$ . 由此可知 $\mathop{\lim }\limits_{{n \rightarrow  \infty }}{x}_{n} = a$ ,即 $\left\{  {x}_{n}\right\}$ 是收敛的.