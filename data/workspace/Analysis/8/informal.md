$\int {x}^{2}\sqrt{{a}^{2} + {x}^{2}}\mathrm{\;d}x$ .

Solution

 $\int {x}^{2}\sqrt{{a}^{2} + {x}^{2}}\mathrm{\;d}x = \frac{1}{2}\int x{\left( {a}^{2} + {x}^{2}\right) }^{\frac{1}{2}}\mathrm{\;d}\left( {{a}^{2} + {x}^{2}}\right)  = \frac{1}{3}\int x\mathrm{\;d}\left\lbrack  {\left( {a}^{2} + {x}^{2}\right) }^{\frac{3}{2}}\right\rbrack$
$$
= \frac{1}{3}x{\left( {a}^{2} + {x}^{2}\right) }^{\frac{3}{2}} - \frac{1}{3}\int {\left( {a}^{2} + {x}^{2}\right) }^{\frac{3}{2}}\mathrm{\;d}x
$$

$$
= \frac{1}{3}x\left( {{a}^{2} + {x}^{2}}\right) \sqrt{{a}^{2} + {x}^{2}} - \frac{{a}^{2}}{3}\int \sqrt{{a}^{2} + {x}^{2}}\mathrm{\;d}x - \frac{1}{3}\int {x}^{2}\sqrt{{a}^{2} + {x}^{2}}\mathrm{\;d}x.
$$

Hence $\int {x}^{2}\sqrt{{a}^{2} + {x}^{2}}\mathrm{\;d}x = \frac{3}{4}\left\lbrack  {\frac{1}{3}x\left( {{a}^{2} + {x}^{2}}\right) \sqrt{{a}^{2} + {x}^{2}} - \frac{{a}^{2}}{3}\int \sqrt{{a}^{2} + {x}^{2}}\mathrm{\;d}x}\right\rbrack$

$$
= \frac{1}{4}x\left( {{a}^{2} + {x}^{2}}\right) \sqrt{{a}^{2} + {x}^{2}} - \frac{{a}^{2}}{4}{\left\lbrack  \frac{x}{2}\sqrt{{a}^{2} + {x}^{2}} + \frac{{a}^{2}}{2}\ln \left( x + \sqrt{{a}^{2} + {x}^{2}}\right) \right\rbrack  } + C
$$

$$
= \frac{x\left( {2{x}^{2} + {a}^{2}}\right) }{8}\sqrt{{a}^{2} + {x}^{2}} - \frac{{a}^{4}}{8}\ln \left( {x + \sqrt{{x}^{2} + {a}^{2}}}\right)  + C.
$$