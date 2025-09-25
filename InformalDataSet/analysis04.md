# Natural Language

Suppose $f(x)$ is continuous on $[0,1]$ , proof that $\lim_{h \to 0^+} \int_0^1 \frac{h}{h^2 + x^2} f(x) dx = \frac{\pi}{2} f(0)$

**Proof** (Fitting method) Since $\lim_{h \to 0} \int_0^1 \frac{h}{h^2 + x^2} dx = \frac{\pi}{2}$, the limit value can be rewritten as
$$
\frac{\pi}{2} f(0) = \lim_{h \to 0} \int_0^1 \frac{h}{h^2 + x^2} f(0) dx.
$$

The problem reduces to proving: $\lim_{h \to 0} \int_0^1 \frac{h}{h^2 + x^2} [f(x) - f(0)] dx = 0.$ However,

$$
\int_0^1 \frac{h}{h^2 + x^2} [f(x) - f(0)] dx = \left( \int_0^\delta + \int_\delta^1 \right) \frac{h}{h^2 + x^2} [f(x) - f(0)] dx.
$$

Because $f(x)$ is continuous at $x = 0$, so $\forall \varepsilon > 0$, when $\delta > 0$ is sufficiently small, on $[0, \delta]$, $|f(x) - f(0)| < \frac{\varepsilon}{\pi}$. Thus,

$$
\begin{aligned}
\left| \int_0^\delta \frac{h}{h^2 + x^2} [f(x) - f(0)] dx \right| &\leq \int_0^\delta \frac{h|f(x)-f(0)|}{h^2 + x^2} dx \\
&\leq \frac{\varepsilon}{\pi} \int_{0}^{\delta}\frac{h}{h^2+x^2}dx \\
&= \frac{\varepsilon}{\pi} \arctan \frac{\delta}{h} \leq \frac{\varepsilon}{\pi} \cdot \frac{\pi}{2} = \frac{\varepsilon}{2}.
\end{aligned}
$$

Now, fix this $\delta$. Then the second integral satisfies

$$
\left| \int_\delta^1 \frac{h}{h^2 + x^2} [f(x) - f(0)] dx \right| \leq h \int_\delta^1 \frac{1}{x^2} |f(x) - f(0)| dx \equiv h \cdot M_0.
$$

Therefore, when $0 < h < \frac{\epsilon}{2M_0}$, we have $\left| \int_0^1 \frac{h}{h^2 + x^2} [f(x) - f(0)] dx \right| < \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon.$ The proof is complete.