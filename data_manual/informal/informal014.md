对于正实数数列$\{x_n\}$和任意正整数$n$，请证明：

$$
\prod\limits_{i=1}^{n}\left( {1 + {x}_{i}}\right)\geq  1 + \sum\limits_{i=1}^{n}{x}_{i},
$$

Pf:

我们使用数学归纳法证明。

归纳基础：当 $n = 1$ 时，$1+x_1=1+x_1$，成立.

归纳步骤：设对于任意的正整数$k$，成立$\prod\limits_{i=1}^{k}\left( {1 + {x}_{i}}\right)\geq  1 + \sum\limits_{i=1}^{k}{x}_{i}$。下面证明$\prod\limits_{i=1}^{k+1}\left( {1 + {x}_{i}}\right)\geq  1 + \sum\limits_{i=1}^{k+1}{x}_{i}$。由于 $\forall 1\leq i \leq n,{x}_{i}>0$,所以, $1 + {x}_{i} > 0$。 因而,有

$$
\prod\limits_{i=1}^{k+1}\left( {1 + {x}_{i}}\right)\geq   (1 + \sum\limits_{i=1}^{k}{x}_{i})(1+x_{k+1})
$$

$$
=(1 + \sum\limits_{i=1}^{k+1}{x}_{i})+\sum\limits_{i=1}^{k}(x_i x_{k+1})
$$

由于 ${x}_{i}{x}_{j} \geq  0$。所以,

$$
\prod\limits_{i=1}^{k+1}\left( {1 + {x}_{i}}\right)\geq 1 + \sum\limits_{i=1}^{k+1}{x}_{i}
$$

归纳证明结束。

于是,对于任何正整数 $n$ ,有

所以

$$
\prod\limits_{i=1}^{n}\left( {1 + {x}_{i}}\right)\geq  1 + \sum\limits_{i=1}^{n}{x}_{i},
$$

Qed.