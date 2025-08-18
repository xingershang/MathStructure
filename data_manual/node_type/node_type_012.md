[Fix: {p} such that "$p > 0$"]
[Find: "反常积分$\int_0^{+\infty} te^{-pt} dt$"]
[Have: "$\int_0^{+\infty} te^{-pt} dt = \left[ \int te^{-pt} dt \right]_0^{+\infty} = \left[ -\frac{1}{p} \int t d(e^{-pt}) \right]_0^{+\infty}$= \left[ -\frac{t}{p} e^{-pt} + \frac{1}{p} \int e^{-pt} dt \right]_0^{+\infty}= \left[ -\frac{t}{p} e^{-pt} \right]_0^{+\infty} - \left[ \frac{1}{p^2} e^{-pt} \right]_0^{+\infty}= -\frac{1}{p} \lim_{t \to +\infty} te^{-pt} - 0 - \frac{1}{p^2} (0 - 1) = \frac{1}{p^2}"]
[Hint: "注意，上式中的极限 $\lim_{t \to +\infty} te^{-pt}$ 是未定式，可用洛必达法则确定。"]