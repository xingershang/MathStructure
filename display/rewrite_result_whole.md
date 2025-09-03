[Sentence 1] $\forall f:\R \to \R$，假设$f$在$[0,1]$上连续
[Sentence 2] 证明: $\lim_{h \to 0^+} \int_0^1 \frac{h}{h^2 + x^2} f(x) dx = \frac{\pi}{2} f(0)$
[Sentence 3] $\forall h \in (0,1/2)$，$\int_0^1 \frac{h}{h^2 + x^2} f(x) dx = \int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx + \int_{h^{1/4}}^1 \frac{hf(x)}{h^2 + x^2} dx$
[Sentence 4] $\forall h \in (0,1/2), I_1(h) = \int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx$
[Sentence 5] $\forall h \in (0,1/2), I_2(h) = \int_{h^{1/4}}^1 \frac{hf(x)}{h^2 + x^2} dx$
[Sentence 6] 其中$\forall h \in (0,1/2), I_1(h) = \int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx$
[Sentence 7] $\forall h \in (0,1/2), \exists \xi, (0 \leq \xi \leq h^{1/4}) \land \int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx = f(\xi) \int_0^{h^{1/4}} \frac{h}{h^2 + x^2} dx$
[Sentence 8] $\forall h \in (0,1/2), \exists \xi, (0 \leq \xi \leq h^{1/4}) \land f(\xi) \int_0^{h^{1/4}} \frac{h}{h^2 + x^2} dx = f(\xi) \arctan \frac{x}{h} \Big|_0^{h^{1/4}}$
[Sentence 9] $\forall h \in (0,1/2), \exists \xi, (0 \leq \xi \leq h^{1/4}) \land f(\xi) \arctan \frac{x}{h} \Big|_0^{h^{1/4}} = f(\xi) \arctan \frac{1}{h^{3/4}}$
[Sentence 10] $\lim\limits_{h \to 0^+} I_1(h) = f(0)\dfrac{\pi}{2}$
[Sentence 11] $\forall h \in (0,1/2), |I_2(h)| = \left| \int_{h^{1/4}}^1 \frac{h}{h^2 + x^2} f(x) dx \right|$
[Sentence 12] ∃ M ∈ ℝ, (∀ x ∈ [0,1], |f(x)| ≤ M) ∧ ∀ h ∈ (0,1/2), $\left| \int_{h^{1/4}}^1 \frac{h}{h^2 + x^2} f(x) dx \right| \leq M \int_{h^{1/4}}^1 \frac{h}{h^2 + x^2} dx$
[Sentence 13] ∃ M ∈ ℝ, (∀ x ∈ [0,1], |f(x)| ≤ M) ∧ ∀ h ∈ (0,1/2), $M \int_{h^{1/4}}^1 \frac{h}{h^2 + x^2} dx = M \left( \arctan \frac{1}{h} - \arctan \frac{1}{h^{3/4}} \right)$
[Sentence 14] $\lim\limits_{h \to 0^+} I_2(h) = 0$
[Sentence 15] $\lim\limits_{h \to 0^+} (I_1(h) + I_2(h)) = f(0)\dfrac{\pi}{2}$
[Sentence 16] Qed.
End.
