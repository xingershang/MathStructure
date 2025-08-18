证明: 对于所有实数 $x$ 和 $y$ 都满足方程

$$
f\left( {x + y}\right)  = f\left( x\right)  + f\left( y\right)  \tag{1}
$$

的唯一的连续函数 $f\left( x\right) \left( {-\infty  < x <  + \infty }\right)$ 是线性齐次函数:

$$
f\left( x\right)  = {ax},
$$

式中 $a = f\left( 1\right)$ 是任意的常数.

证 先证: 若 $f\left( x\right)$ 满足 (1),则对任何有理数 $c$ ,必有

$$
f\left( {cx}\right)  = {cf}\left( x\right) \;\left( {-\infty  < x <  + \infty }\right) .
$$

事实上,当 $m$ 与 $n$ 为正整数时,有

$$
f\left( {mx}\right)  = f\left( {x + \left( {m - 1}\right) x}\right)  = f\left( x\right)  + f\left( {\left( {m - 1}\right) x}\right)  = f\left( x\right)  + f\left( x\right)  + f\left( {\left( {m - 2}\right) x}\right)  = \cdots
$$

$$
= f\left( x\right)  + f\left( x\right)  + \cdots  + f\left( x\right)  = {mf}\left( x\right) \text{;}
$$

$$
f\left( x\right)  = f\left( {n \cdot  \frac{x}{n}}\right)  = {nf}\left( \frac{x}{n}\right) ,\;\text{ 故 }f\left( \frac{x}{n}\right)  = \frac{1}{n}f\left( x\right) .
$$

于是,

$$
f\left( {\frac{m}{n}x}\right)  = {mf}\left( \frac{x}{n}\right)  = \frac{m}{n}f\left( x\right) .
$$

又在 (1) 中令 $y = 0$ ,得 $f\left( x\right)  = f\left( x\right)  + f\left( 0\right)$ ,故 $f\left( 0\right)  = 0$ ; 又在 (1) 中令 $y =  - x$ ,并注意到已证的结果 $f\left( 0\right)  = 0$ , 得 $f\left( {-x}\right)  =  - f\left( x\right)$ . 于是,

$$
f\left( {-\frac{m}{n}x}\right)  =  - f\left( {\frac{m}{n}x}\right)  =  - \frac{m}{n}f\left( x\right) .
$$

故对任何有理数 $c$ ,有 $f\left( {cx}\right)  = {cf}\left( x\right) \left( {-\infty  < x <  + \infty }\right)$ . 下面,我们利用 $f\left( x\right)$ 的连续性证明对任何无理数 $c$ , 此式也成立. 事实上,设 $c$ 为无理数. 取一串有理数 ${c}_{n}$ ,使 ${c}_{n} \rightarrow  c\left( {n \rightarrow  \infty }\right)$ . 于是,

$$
f\left( {{c}_{n}x}\right)  = {c}_{n}f\left( x\right) \;\left( {n = 1,2,\cdots }\right) ,
$$

在此式两端令 $n \rightarrow  \infty$ 取极限,并注意到函数 $f$ 在点 ${cx}$ 连续,即得 $f\left( {cx}\right)  = {cf}\left( x\right)$ . 于是,对任何实数 $x$ 和 $c$ , 有 $f\left( {cx}\right)  = {cf}\left( x\right)$ . 由此可知,对任何实数 $x$ ,有

$$
f\left( x\right)  = f\left( {x \cdot  1}\right)  = {xf}\left( 1\right)  = {ax},
$$

其中 $a = f\left( 1\right)$ . 证毕.