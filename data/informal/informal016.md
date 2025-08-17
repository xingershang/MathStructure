假设 $f(x)$ 在 $[0,1]$ 上连续，证明: $\lim_{h \to 0^+} \int_0^1 \frac{h}{h^2 + x^2} f(x) dx = \frac{\pi}{2} f(0)$

**证 ** （拟合法）因 $\lim_{h \to 0} \int_0^1 \frac{h}{h^2 + x^2} dx = \frac{\pi}{2}$，故极限值可改写为
$$
\frac{\pi}{2} f(0) = \lim_{h \to 0} \int_0^1 \frac{h}{h^2 + x^2} f(0) dx.
$$

问题归结为证明：$\lim_{h \to 0} \int_0^1 \frac{h}{h^2 + x^2} [f(x) - f(0)] dx = 0.$ 但是

$$
\int_0^1 \frac{h}{h^2 + x^2} [f(x) - f(0)] dx = \left( \int_0^\delta + \int_\delta^1 \right) \frac{h}{h^2 + x^2} [f(x) - f(0)] dx.
$$

因为 $f(x)$ 在 $x = 0$ 处连续，所以 $\forall \varepsilon > 0$，当 $\delta > 0$ 充分小时，在 $[0, \delta]$ 上，$|f(x) - f(0)| < \frac{\varepsilon}{\pi}$。从而

$$
\left| \int_0^\delta \frac{h}{h^2 + x^2} [f(x) - f(0)] dx \right| \\
\leq \int_0^\delta \frac{h|f(x)-f(0)|}{h^2 + x^2} \cdot dx \leq \frac{\varepsilon}{\pi} \cdot \int_{0}^{\delta}\frac{h}{h^2+x^2}dx \\
= \frac{\varepsilon}{\pi} \arctan \frac{\delta}{h} \leq \frac{\varepsilon}{\pi} \cdot \frac{\pi}{2} = \frac{\varepsilon}{2}.
$$

再将 $\delta$ 固定，这时第二个积分

$$
\left| \int_\delta^1 \frac{h}{h^2 + x^2} [f(x) - f(0)] dx \right| \leq h \int_\delta^1 \frac{1}{x^2} |f(x) - f(0)| dx \equiv h \cdot M_0.
$$

故当 $0 < h < \frac{\epsilon}{2M_0}$ 时，$\left| \int_0^1 \frac{h}{h^2 + x^2} [f(x) - f(0)] dx \right| < \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon.$ 证毕。