你是一个数学专家。下面我会给你一段数学文本，你需要按照我提供的格式将其切分为一个一个的句子，并依次给这些句子按顺序编号。

## 格式

对于每个语句，格式如下：

[Sentence N] {content}

## 注意事项

你不允许对句子做任何的修改，只是做切分！！！(当然，每句话都需要是有内容的。“证明：”或“解：”并不能算作一句话，这样的内容应当跳过，具体请见样例)

## 样例

### 样例 1

<input_content>
我们需要找到所有满足以下条件的函数 $ f: \mathbb{R} \rightarrow \mathbb{R} $：$\forall x,y, f(x+y) - f(x-y) = f(x)f(y) $

**解**

首先，将原式中的 $ x $ 和 $ y $ 互换得到：$ f(y+x) - f(y-x) = f(y)f(x) $. 因此，我们有：$ f(y+x) - f(y-x) = f(x+y) - f(x-y) $。这意味着：$ f(y-x) = f(x-y) $。令 $ y = 0 $，可得：$ f(x) = f(-x) $。这表明 $ f $ 是偶函数。在原式中令 $ y = -y $，我们有：$ f(x)f(-y) = f(-y+x) - f(-y-x) = f(-(y-x)) - f(-(x+y)) $$ = f(y-x) - f(x+y) $$ = -[f(x+y) - f(y-x)] $$ = -f(y)f(x) $。因此，得到：$ f(x)f(y) = -f(x)f(y) $。这意味着：$ 2f(x)f(y) = 0 $。所以对于所有 $ x, y $，我们有 $ f(x)f(y) = 0 $。特别地，令 $ y = x $，得到：$ 2f^2(x) = 0 $。因此，$ f(x) = 0 $ 对于所有 $ x $。综上所述，满足条件的函数为：$\boxed{f(x) = 0}$
</input_content>

<output_content>
[Sentence 1] 我们需要找到所有满足以下条件的函数 $ f: \mathbb{R} \rightarrow \mathbb{R} $：$\forall x,y, f(x+y) - f(x-y) = f(x)f(y) $
[Sentence 2] 首先，将原式中的 $ x $ 和 $ y $ 互换得到：$ f(y+x) - f(y-x) = f(y)f(x) $.
[Sentence 3] 因此，我们有：$ f(y+x) - f(y-x) = f(x+y) - f(x-y) $。
[Sentence 4] 这意味着：$ f(y-x) = f(x-y) $。
[Sentence 5] 令 $ y = 0 $，可得：$ f(x) = f(-x) $。
[Sentence 6] 这表明 $ f $ 是偶函数。
[Sentence 7] 在原式中令 $ y = -y $，我们有：$ f(x)f(-y) = f(-y+x) - f(-y-x) = f(-(y-x)) - f(-(x+y)) $$ = f(y-x) - f(x+y) $$ = -[f(x+y) - f(y-x)] $$ = -f(y)f(x) $。
[Sentence 8] 因此，得到：$ f(x)f(y) = -f(x)f(y) $。
[Sentence 9] 这意味着：$ 2f(x)f(y) = 0 $。
[Sentence 10] 所以对于所有 $ x, y $，我们有 $ f(x)f(y) = 0 $。
[Sentence 11] 特别地，令 $ y = x $，得到：$ 2f^2(x) = 0 $。
[Sentence 12] 因此，$ f(x) = 0 $ 对于所有 $ x $。
[Sentence 13] 综上所述，满足条件的函数为：$\boxed{f(x) = 0}$
</output_content>

### 样例 2

<input_content>
假设 $f(x)$ 在 $[0,1]$ 上连续，证明: $\lim_{h \to 0^+} \int_0^1 \frac{h}{h^2 + x^2} f(x) dx = \frac{\pi}{2} f(0)$

Pf:

$\int_0^1 \frac{h}{h^2 + x^2} f(x) dx = \int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx + \int_{h^{1/4}}^1 \frac{hf(x)}{h^2 + x^2} dx$

令$I_1 = \int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx$, $I_2 = \int_{h^{1/4}}^1 \frac{hf(x)}{h^2 + x^2} dx$

其中

$I_1 = \int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx = f(\xi) \int_0^{h^{1/4}} \frac{h}{h^2 + x^2} dx \quad (0 \leq \xi \leq h^{1/4})$

$= f(\xi) \arctan \frac{x}{h} \Big|_0^{h^{1/4}} = f(\xi) \arctan \frac{1}{h^{3/4}} \to f(0)\dfrac{\pi}{2} \quad (h \to 0^+)$

$|I_2| = \left| \int_{h^{1/4}}^1 \frac{h}{h^2 + x^2} f(x) dx \right| \leq M \int_{h^{1/4}}^1 \frac{h}{h^2 + x^2} dx(\quad |f(x)|\leq M\quad)$

$= M \left( \arctan \frac{1}{h} - \arctan \frac{1}{h^{3/4}} \right) \to 0 \quad (h \to 0^+)$

因此$h\to 0^+$时$I_1+I_2\to f(0)\dfrac{\pi}{2}$

Qed.
</input_content>

</output_content>
[Sentence 1] 假设 $f(x)$ 在 $[0,1]$ 上连续
[Sentence 2] 证明: $\lim_{h \to 0^+} \int_0^1 \frac{h}{h^2 + x^2} f(x) dx = \frac{\pi}{2} f(0)$
[Sentence 3] $\int_0^1 \frac{h}{h^2 + x^2} f(x) dx = \int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx + \int_{h^{1/4}}^1 \frac{hf(x)}{h^2 + x^2} dx$
[Sentence 4] 令$I_1 = \int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx$, $I_2 = \int_{h^{1/4}}^1 \frac{hf(x)}{h^2 + x^2} dx$
[Sentence 5] 其中 $I_1 = \int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx = f(\xi) \int_0^{h^{1/4}} \frac{h}{h^2 + x^2} dx \quad (0 \leq \xi \leq h^{1/4})$
[Sentence 6] $= f(\xi) \arctan \frac{x}{h} \Big|_0^{h^{1/4}} = f(\xi) \arctan \frac{1}{h^{3/4}} \to f(0)\dfrac{\pi}{2} \quad (h \to 0^+)$
[Sentence 7] $|I_2| = \left| \int_{h^{1/4}}^1 \frac{h}{h^2 + x^2} f(x) dx \right| \leq M \int_{h^{1/4}}^1 \frac{h}{h^2 + x^2} dx(\quad |f(x)|\leq M\quad)$
[Sentence 8] $= M \left( \arctan \frac{1}{h} - \arctan \frac{1}{h^{3/4}} \right) \to 0 \quad (h \to 0^+)$
[Sentence 9] 因此$h\to 0^+$时$I_1+I_2\to f(0)\dfrac{\pi}{2}$
</output_content>

（再次强调，你不许对原文做任何修改（即便原文可能是错误的）！！！只做切分！！！）
（你的输出不用包含标签<output_content>和</output_content>）