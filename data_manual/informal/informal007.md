【819】求对于所有实数 $x$ 和 $y$ 都满足方程组:

$$
f\left( {x + y}\right)  = f\left( x\right) f\left( y\right)  - g\left( x\right) g\left( y\right) ,
$$

$$
g\left( {x + y}\right)  = f\left( x\right) g\left( y\right)  + f\left( y\right) g\left( x\right) ,
$$

以及规范条件

$$
f\left( 0\right)  = 1\text{ 和 }g\left( 0\right)  = 0
$$

的所有的有界连续函数 $f\left( x\right)$ 和 $g\left( x\right) \left( {-\infty  < x <  + \infty }\right)$ .

提示 考虑函数 $F\left( x\right)  = {f}^{2}\left( x\right)  + {g}^{2}\left( x\right)$ .

解 考虑函数 $F\left( x\right)  = {f}^{2}\left( x\right)  + {g}^{2}\left( x\right)$ ,则

$$
F\left( {x + y}\right)  = {f}^{2}\left( {x + y}\right)  + {g}^{2}\left( {x + y}\right)
$$

$$
= {\left\lbrack  f\left( x\right) f\left( y\right)  - g\left( x\right) g\left( y\right) \right\rbrack  }^{2} + {\left\lbrack  f\left( x\right) g\left( y\right)  + f\left( y\right) g\left( x\right) \right\rbrack  }^{2} = F\left( x\right) F\left( y\right) ,
$$

由于 $F\left( 0\right)  = 1$ 及 $F\left( x\right)  ≢ 0$ ,故

$$
F\left( x\right)  = {a}^{x}\;\left( {-\infty  < x <  + \infty }\right) ,
$$

式中 $a = F\left( 1\right)$ 为正的常数 ${}^{*)}$ .

由于 $f\left( x\right)$ 及 $g\left( x\right)$ 有界,故只能有 $a = 1$ . 因此,对于所有的实数 $x$ ,有 ${f}^{2}\left( x\right)  + {g}^{2}\left( x\right)  = 1$ . 因为

$$
0 = g\left( 0\right)  = g\left( {x - x}\right)  = f\left( x\right) g\left( {-x}\right)  + f\left( {-x}\right) g\left( x\right)
$$

及

$$
1 = f\left( 0\right)  = f\left( {x - x}\right)  = f\left( x\right) f\left( {-x}\right)  - g\left( {-x}\right) g\left( x\right) .
$$

上面二式分别乘以 $g\left( {-x}\right)$ 及 $f\left( {-x}\right)$ ,然后相加,得

$$
f\left( {-x}\right)  = f\left( x\right) \left\lbrack  {{f}^{2}\left( {-x}\right)  + {g}^{2}\left( {-x}\right) }\right\rbrack   = f\left( x\right) ;
$$

如果上面二式分别乘以 $f\left( {-x}\right)$ 及 $g\left( {-x}\right)$ ,然后相减,得

$$
g\left( {-x}\right)  =  - g\left( x\right) \left\lbrack  {{g}^{2}\left( {-x}\right)  + {f}^{2}\left( {-x}\right) }\right\rbrack   =  - g\left( x\right) .
$$

从而可得

$$
f\left( {x + y}\right)  + f\left( {x - y}\right)  = f\left( x\right) f\left( y\right)  - g\left( x\right) g\left( y\right)  + f\left( x\right) f\left( {-y}\right)  - g\left( x\right) g\left( {-y}\right)  = {2f}\left( x\right) f\left( y\right) .
$$

于是,考虑到 $f\left( x\right)$ 的有界性,可得

$$
f\left( x\right)  = \cos a{x}^{* * )},
$$

再由 ${f}^{2}\left( x\right)  + {g}^{2}\left( x\right)  = 1$ 可得

$$
g\left( x\right)  =  \pm  \sin {ax}.
$$