[Assume: {$\forall f:\R \to \R$，$f$在$[0,1]$上连续}] [@tag: 1]
[Show: {$\lim_{h \to 0^+} \int_0^1 \frac{h}{h^2 + x^2} f(x) dx = \frac{\pi}{2} f(0)$}] [@tag: 2]
[Have: {∀h ∈ (0,1/2)，$\int_0^1 \frac{h}{h^2 + x^2} f(x) dx = \int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx + \int_{h^{1/4}}^1 \frac{hf(x)}{h^2 + x^2} dx$}] [@tag: 3]
[Define: {$I_1$} as {$\int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx$}] [@tag: 3]
[Define: {$I_2$} as {$\int_{h^{1/4}}^1 \frac{hf(x)}{h^2 + x^2} dx$}] [@tag: 3]
[Hint: {其中 $I_1 = \int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx$}] [@tag: 3]
[Have: {$\exists \xi \in [0, h^{1/4}]$，$\int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx = f(\xi) \int_0^{h^{1/4}} \frac{h}{h^2 + x^2} dx$}] [@tag: 3]
[Have: {$f(\xi) \int_0^{h^{1/4}} \frac{h}{h^2 + x^2} dx = f(\xi) \arctan \frac{x}{h} \Big|_0^{h^{1/4}} = f(\xi) \arctan \frac{1}{h^{3/4}}$}] [@tag: 3]
[Have: {$\lim\limits_{h \to 0^+} f(\xi) \arctan \frac{1}{h^{3/4}} = f(0)\dfrac{\pi}{2}$}] [@tag: 3]
[Have: {∃M ∈ ℝ, ∀x ∈ [0,1], |f(x)| ≤ M，并且∀h ∈ (0,1/2)，$|I_2| = \left| \int_{h^{1/4}}^1 \frac{h}{h^2 + x^2} f(x) dx \right| \leq M \int_{h^{1/4}}^1 \frac{h}{h^2 + x^2} dx$}] [@tag: 3]
[Have: {$M \int_{h^{1/4}}^1 \frac{h}{h^2 + x^2} dx = M \left( \arctan \frac{1}{h} - \arctan \frac{1}{h^{3/4}} \right)$}] [@tag: 3]
[Have: {$\lim\limits_{h \to 0^+} M \left( \arctan \frac{1}{h} - \arctan \frac{1}{h^{3/4}} \right) = 0$}] [@tag: 3]
[Have: {因此，$\lim\limits_{h \to 0^+} (I_1 + I_2) = f(0)\dfrac{\pi}{2}$}] [@tag: 3]
End.


