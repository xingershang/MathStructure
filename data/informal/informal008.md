设 $\{x_n\}$ 是实数上的数列，满足 $\forall n \geq 1, x_n = n^{(-1)^n}$。请证明：$\{x_n\}$ 无界，且$\lim\limits_{n \to \infty} x_n=\infty$不成立。

Pf:

首先，我们有对于任意正整数 $k$，$x_{2k} = 2k$, $x_{2k-1}=\frac{1}{2k-1}$

(1) 下面证明 $\{x_n\}$ 无界：

考虑$\{x_n\}$的子列 $y_k=x_{2k}$。下面证明$\{y_n\}$无界。对于任意给定的 $M > 0$，存在 $k_0 = \lceil M/2 \rceil$，使得当 $k \geq k_0$ 时，$y_k=x_{2k} = 2k \geq 2k_0 \geq M$。因此，$\{y_n\}$ 无界。

因为$\{y_n\}$无界，因此 $\{x_n\}$ 无界。

(2) 证明 $\lim\limits_{n \to \infty} x_n=\infty$ 不成立：

考虑两个子列$y_k=x_{2k}$与$z_k=x_{2k-1}$，我们有 $\lim\limits_{k \to \infty} y_k = \lim\limits_{k \to \infty} x_{2k}=\lim\limits_{k \to \infty} 2k=+\infty$；又有 $\lim\limits_{k \to \infty} z_k=\lim\limits_{k \to \infty}x_{2k-1} =\lim\limits_{k \to \infty} \frac{1}{2k-1}= 0$。所以$\lim\limits_{n \to \infty} x_n=\infty$ 不成立。

Qed.