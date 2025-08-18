设 $|q| < 1$，证明等比数列  $x_n=q^{n-1}$ 的极限是 0。
证  
$\forall \varepsilon > 0$（设 $\varepsilon < 1$），因为  $|x_n - 0| = |q^{n-1} - 0| = |q|^{n-1},$ 
要使 $|x_n - 0| < \varepsilon$，只要  $|q|^{n-1} < \varepsilon.$
取自然对数，得  $(n-1) \ln |q| < \ln \varepsilon.$
因 $|q| < 1$，$\ln |q| < 0$，故  $n > 1 + \frac{\ln \varepsilon}{\ln |q|}.$
取  $N = \left\lceil 1 + \frac{\ln \varepsilon}{\ln |q|} \right\rceil,$
则当 $n > N$ 时，就有  $|q^{n-1} - 0| < \varepsilon,$
即  $\lim_{n \to \infty} q^{n-1} = 0.$