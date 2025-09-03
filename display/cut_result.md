[Sentence 1] 假设 $f(x)$ 在 $[0,1]$ 上连续
[Sentence 2] 证明: $\lim_{h \to 0^+} \int_0^1 \frac{h}{h^2 + x^2} f(x) dx = \frac{\pi}{2} f(0)$
[Sentence 3] $\int_0^1 \frac{h}{h^2 + x^2} f(x) dx = \int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx + \int_{h^{1/4}}^1 \frac{hf(x)}{h^2 + x^2} dx$
[Sentence 4] 令$I_1 = \int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx$
[Sentence 5] 令$I_2 = \int_{h^{1/4}}^1 \frac{hf(x)}{h^2 + x^2} dx$
[Sentence 6] 其中$I_1 = \int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx$
[Sentence 7] $\int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx = f(\xi) \int_0^{h^{1/4}} \frac{h}{h^2 + x^2} dx \quad (0 \leq \xi \leq h^{1/4})$
[Sentence 8] $f(\xi) \int_0^{h^{1/4}} \frac{h}{h^2 + x^2} dx = f(\xi) \arctan \frac{x}{h} \Big|_0^{h^{1/4}}$
[Sentence 9] $f(\xi) \arctan \frac{x}{h} \Big|_0^{h^{1/4}} = f(\xi) \arctan \frac{1}{h^{3/4}}$
[Sentence 10] $f(\xi) \arctan \frac{1}{h^{3/4}} \to f(0)\dfrac{\pi}{2} \quad (h \to 0^+)$
[Sentence 11] $|I_2| = \left| \int_{h^{1/4}}^1 \frac{h}{h^2 + x^2} f(x) dx \right|$
[Sentence 12] $\left| \int_{h^{1/4}}^1 \frac{h}{h^2 + x^2} f(x) dx \right| \leq M \int_{h^{1/4}}^1 \frac{h}{h^2 + x^2} dx(\quad |f(x)|\leq M\quad)$
[Sentence 13] $M \int_{h^{1/4}}^1 \frac{h}{h^2 + x^2} dx = M \left( \arctan \frac{1}{h} - \arctan \frac{1}{h^{3/4}} \right)$
[Sentence 14] $M \left( \arctan \frac{1}{h} - \arctan \frac{1}{h^{3/4}} \right) \to 0 \quad (h \to 0^+)$
[Sentence 15] 因此$h\to 0^+$时$I_1+I_2\to f(0)\dfrac{\pi}{2}$
[Sentence 16] Qed.