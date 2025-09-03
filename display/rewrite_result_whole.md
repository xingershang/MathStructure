$\forall f:\R \to \R$，假设$f$在$[0,1]$上连续
证明: $\lim_{h \to 0^+} \int_0^1 \frac{h}{h^2 + x^2} f(x) dx = \frac{\pi}{2} f(0)$
∀h ∈ (0,1/2)，$\int_0^1 \frac{h}{h^2 + x^2} f(x) dx = \int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx + \int_{h^{1/4}}^1 \frac{hf(x)}{h^2 + x^2} dx$
令$I_1 = \int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx$
令$I_2 = \int_{h^{1/4}}^1 \frac{hf(x)}{h^2 + x^2} dx$
其中 $I_1 = \int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx$
$\exists \xi \in [0, h^{1/4}]$，$\int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx = f(\xi) \int_0^{h^{1/4}} \frac{h}{h^2 + x^2} dx$
$f(\xi) \int_0^{h^{1/4}} \frac{h}{h^2 + x^2} dx = f(\xi) \arctan \frac{x}{h} \Big|_0^{h^{1/4}} = f(\xi) \arctan \frac{1}{h^{3/4}}$
$\lim\limits_{h \to 0^+} f(\xi) \arctan \frac{1}{h^{3/4}} = f(0)\dfrac{\pi}{2}$
∃M ∈ ℝ, ∀x ∈ [0,1], |f(x)| ≤ M，并且∀h ∈ (0,1/2)，$|I_2| = \left| \int_{h^{1/4}}^1 \frac{h}{h^2 + x^2} f(x) dx \right| \leq M \int_{h^{1/4}}^1 \frac{h}{h^2 + x^2} dx$
$M \int_{h^{1/4}}^1 \frac{h}{h^2 + x^2} dx = M \left( \arctan \frac{1}{h} - \arctan \frac{1}{h^{3/4}} \right)$
$\lim\limits_{h \to 0^+} M \left( \arctan \frac{1}{h} - \arctan \frac{1}{h^{3/4}} \right) = 0$
因此，$\lim\limits_{h \to 0^+} (I_1 + I_2) = f(0)\dfrac{\pi}{2}$
End.
