你是一个数学专家。下面我会给你一段数学文本，你需要按照我提供的格式将其切分为一个一个的句子，并依次给这些句子按顺序编号。

## 格式

对于每个语句，格式如下：

[Sentence N] {content}

## 要求

这个任务关键的难点在于判断“什么是一个句子”。

一般而言，如果你能够识别出一个句子是一个意思明确的数学命题，直接把这个命题切分出来即可。

而有的时候，在哪里做切分并不那么明显，需要你仔细思考。

比如，单单两个字“证明：”不能算作一个句子，这是自然语言的语言习惯问题。这时候，你需要把“证明：”移动到证明目标的前面（见样例1）。

尽管“假设...”并不是一个意义完整的数学命题，但是自然语言中通常会做出一个假设，然后推导这个假设的必要条件。这就使得切分的时候，我们通常需要把“假设...”作为单独的一个句子切分（见样例1）。

一个动作通常不是一个句子。比如，“令$y=0$”这不是一个句子而是一个动作，一个完整的数学命题应该是“令$y=1$我们可以得到...”（见样例2）。但是一些特定的动作是一个句子，比如上面提到的“假设...”通常需要被看作一个句子；再比如，“定义I_1=...”或“令I_1=...”，这样的动作会引入一个新的变量，这样的动作需要被看作一个句子。（见样例1）

自然语言中会出现长的连等式，比如“A = B = C = D”或“A = B (理由说明) = C (理由说明) = D”或“A iff B (理由说明) iff C (理由说明) iff D”等连等式。这时候，你需要把它们拆分开，每个等式单独表达（理由说明的形式保持不变）。（见样例1）

从上面的要求可以看出，切分时在特定的情形下，你可能需要对原始文本做一些小的改动，而不仅是做“插入换行符”的工作。但是，这些小的改动都是为“切分”服务的。对禁止修改原文内容！比如，你不允许把“$x\to 1$时$f(x)\to 0$”修改为“$\lim\limits_{x\to 1}f(x)=1$”，而是完全保持自然语言的原始表达。

## 样例

### 样例 1

<input_content>
假设 $f(x)$ 在 $[0,1]$ 上连续，那么$\lim_{h \to 0^+} \int_0^1 \frac{h}{h^2 + x^2} f(x) dx = \frac{\pi}{2} f(0)$

证明:

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

在这个样例中，有以下几点需要注意：
“假设...”单独作为一个句子
“证明:”需要被移到证明目标的前面
连等式需要做拆分，但不修改原始表达，只是以切分为目的做补全
“令I_1=...”的动作单独作为一个句子。并且自然语言把两次“令”的动作合并写成了一行，这是一种自然语言的简写，你需要分行写。

<output_content>
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
[Sentence 13] $M \int_{h^{1/4}}^1 \frac{h}{h^2 + x^2} dx= M \left( \arctan \frac{1}{h} - \arctan \frac{1}{h^{3/4}} \right)$
[Sentence 14] $M \left( \arctan \frac{1}{h} - \arctan \frac{1}{h^{3/4}} \right) \to 0 \quad (h \to 0^+)$
[Sentence 15] 因此$h\to 0^+$时$I_1+I_2\to f(0)\dfrac{\pi}{2}$
[Sentence 16] Qed.
</output_content>

### 样例 2

<input_content>
我们需要找到所有满足以下条件的函数 $ f: \mathbb{R} \rightarrow \mathbb{R} $：$\forall x,y, f(x+y) - f(x-y) = f(x)f(y) $

**解**

首先，将原式中的 $ x $ 和 $ y $ 互换得到：$ f(y+x) - f(y-x) = f(y)f(x) $. 因此，我们有：$ f(y+x) - f(y-x) = f(x+y) - f(x-y) $。这意味着：$ f(y-x) = f(x-y) $。令 $ y = 0 $，可得：$ f(x) = f(-x) $。这表明 $ f $ 是偶函数。在原式中令 $ y = -y $，我们有：$ f(x)f(-y) = f(-y+x) - f(-y-x) = f(-(y-x)) - f(-(x+y)) $$ = f(y-x) - f(x+y) $$ = -[f(x+y) - f(y-x)] $$ = -f(y)f(x) $。因此，得到：$ f(x)f(y) = -f(x)f(y) $。这意味着：$ 2f(x)f(y) = 0 $。所以对于所有 $ x, y $，我们有 $ f(x)f(y) = 0 $。特别地，令 $ y = x $，得到：$ 2f^2(x) = 0 $。因此，$ f(x) = 0 $ 对于所有 $ x $。综上所述，满足条件的函数为：$\boxed{f(x) = 0}$
</input_content>

这个例子不是一个“证明”，而是一个问题求解。切分时需注意：
由于第一句话已经强调了“我们需要找到...”，这已经表明了待求解的问题是什么，以及接下来求解过程就要开始，所以“解：”字可以省略，不放进任何一个句子里。
“令 y=0”不是单独的一个句子，而是和其后的句子作为一个整体，因为“令y=0”在这里是得出$ f(x) = f(-x) $的一种方法上的解释，其本身不是一个有含义的数学命题。
连等式需要做拆分。

<output_content>
[Sentence 1] 我们需要找到所有满足以下条件的函数 $ f: \mathbb{R} \rightarrow \mathbb{R} $：$\forall x,y, f(x+y) - f(x-y) = f(x)f(y) $
[Sentence 2] 首先，将原式中的 $ x $ 和 $ y $ 互换得到：$ f(y+x) - f(y-x) = f(y)f(x) $.
[Sentence 3] 因此，我们有：$ f(y+x) - f(y-x) = f(x+y) - f(x-y) $。
[Sentence 4] 这意味着：$ f(y-x) = f(x-y) $。
[Sentence 5] 令 $ y = 0 $，可得：$ f(x) = f(-x) $。
[Sentence 6] 这表明 $ f $ 是偶函数。
[Sentence 7] 在原式中令 $ y = -y $，我们有：$ f(x)f(-y) = f(-y+x) - f(-y-x)$。
[Sentence 8] $f(-y+x) - f(-y-x) = f(-(y-x)) - f(-(x+y))$。
[Sentence 9] $f(-(y-x)) - f(-(x+y)) = f(y-x) - f(x+y)$。
[Sentence 10] $f(y-x) - f(x+y)  = -[f(x+y) - f(y-x)]$
[Sentence 11] $-[f(x+y) - f(y-x)]  = -f(y)f(x) $
[Sentence 12] 因此，得到：$ f(x)f(y) = -f(x)f(y) $。
[Sentence 13] 这意味着：$ 2f(x)f(y) = 0 $。
[Sentence 14] 所以对于所有 $ x, y $，我们有 $ f(x)f(y) = 0 $。
[Sentence 15] 特别地，令 $ y = x $，得到：$ 2f^2(x) = 0 $。
[Sentence 16] 因此，$ f(x) = 0 $ 对于所有 $ x $。
[Sentence 17] 综上所述，满足条件的函数为：$\boxed{f(x) = 0}$
</output_content>

（再次强调，你不许对原文做任何修改（即便原文可能是错误的）！！！只做切分！！！）
（你的输出不用包含标签<output_content>和</output_content>）