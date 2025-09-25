# Natural Language

**Theorem 3.5.** Let $X$ and $Y$ be independent random variables. If both $X$ and $Y$ are integrable, so is $XY$, and

(3.2)  
$$E\{XY\} = E\{X\} E\{Y\}.$$

**Proof.** Suppose first that $X$ and $Y$ are discrete with possible values $(x_i)$ and $(y_j)$, respectively. Then
$$
E\{|XY|\} = \sum_{i,j} |x_i| |y_j| P\{X = x_i, Y = y_j\}
$$

$$
= \sum_{i,j} |x_i| |y_j| P\{X = x_i\} P\{Y = y_j\}
$$

$$
= \sum_i |x_i| P\{X = x_i\} \sum_j |y_j| P\{Y = y_j\}
$$

$$
= E\{|X|\} E\{|Y|\},
$$

where the change of order in the summation is justified since the summands are positive. Both $X$ and $Y$ are integrable, so this is finite. Thus $XY$ is integrable. Now remove the absolute value signs. The series converges absolutely, so that the terms can be rearranged, and the same calculation (sans absolute value signs) gives (3.2).

Next, if $X$ and $Y$ are integrable, so are the dyadic approximations $\bar{X}_n$ and $\bar{Y}_n$, and, as $\bar{X}_n - X$ and $\bar{Y}_n - Y$ are both positive and less than $2^{-n}$,

$$
E\{| \bar{X}_n \bar{Y}_n - XY | \} \leq E\{| \bar{X}_n || \bar{Y}_n - Y | \} + E\{|Y| | \bar{X}_n - X | \}
$$

$$
\leq 2^{-n} \left(E\{|\bar{X}_n|\} + E\{|Y|\}\right)
$$

$$
\leq 2^{-n} \left(2 + E\{|\bar{X}_0|\} + E\{|\bar{Y}_0|\}\right) \to 0
$$

where we have used the facts that $|\bar{X}_n| \leq 1 + |\bar{X}_0|$ and $|Y| \leq 1 + |\bar{Y}_0|$. In particular, since $\bar{X}_n \bar{Y}_n$ is integrable, so is $XY$. Therefore

$$
E\{XY\} = \lim_n E\{\bar{X}_n \bar{Y}_n\} = \lim_n E\{\bar{X}_n\} E\{\bar{Y}_n\} = E\{X\} E\{Y\}.
$$

□