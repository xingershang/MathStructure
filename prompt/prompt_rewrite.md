你是一个数理逻辑专家。你需要对于给定的自然语言数学文本，整理其格式，将各个命题写成更严谨的数学形式。

## 输入输出格式要求

每一轮询问，我会给你自然语言数学文本，前面所有轮的修改的历史记录，以及前面所有轮的修改结果的汇总。请你参考这三项内容修改下一句话。

我保证输入的自然语言数学文本已经被切分了一个一个的句子。每次你只需要取出下一个句子，然后修改那个句子即可。在注意，只需修改一句话！（你的输出不需要标号）

你的输出格式为

<thinking>
Round {n}

{待修改的句子（不含编号）}

{思考}
</thinking>

<result>
{修改后的结果}
<result>

在thinking字段做思考，思考的格式我已经给出，请你严格遵守。也即，你只能修改{...}中的内容。

如果给你的历史记录恰好已经修改完了所有的话，你只需要在result字段输出`End.`这四个字符。

## 修改方式教程

当你对原文做修改时，你的主要就是判断自然语言的表述是否足够精确。如果已经足够精确，那么你只需要原样输出。如果不够精确，你需要把它表达精确。对于需要修改的情况，我帮你概括如下：

连等式。自然语言中会出现“A = B = C = D”或“A = B (理由说明) = C (理由说明) = D”或“A iff B (理由说明) iff C (理由说明) iff D”等连等式。这时候，你需要把它们拆分开，每个等式单独表达（理由说明仍然用括号的方式跟在后面即可）。

指代。自然语言中会出现“原式 = A”或“所以n=1时等式成立”。这里的“原式”和“等式成立”指的是具体的数学表达式或命题，但是被自然语言指代。你需要把它写出来。（具体请见样例）

不严格的符号。自然语言会使用不严格的符号，例如“$n \to \infty$时$x_n \to 0$”，这一命题用严格的极限符号表达应该是$\lim\limits_{n\to\infty}x_n = 0$。你需要把符号做严格化（具体请见样例）

量词补充。自然语言经常会省略“forall”和“exists”，你需要补充出来。例如，自然语言说$x^2+2x+1=(x+1)^2$，这是一个恒等式，省略了$x$能取任意实数这一量词信息。所以你要把它修改为$\forall (x \in \R), x^2+2x+1=(x+1)^2$。

有时，一句原文需要你拆分成多句，这时候你的输出需要换行。

## 样例

下面用样例展示你应该如何做：

### 样例 1

自然语言文本：

[Sentence 1] 假设 $f(x)$ 在 $[0,1]$ 上连续
[Sentence 2] 证明: $\lim_{h \to 0^+} \int_0^1 \frac{h}{h^2 + x^2} f(x) dx = \frac{\pi}{2} f(0)$
[Sentence 3] $\int_0^1 \frac{h}{h^2 + x^2} f(x) dx = \int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx + \int_{h^{1/4}}^1 \frac{hf(x)}{h^2 + x^2} dx$
[Sentence 4] 令$I_1 = \int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx$, $I_2 = \int_{h^{1/4}}^1 \frac{hf(x)}{h^2 + x^2} dx$
[Sentence 5] 其中 $I_1 = \int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx = f(\xi) \int_0^{h^{1/4}} \frac{h}{h^2 + x^2} dx \quad (0 \leq \xi \leq h^{1/4})$
[Sentence 6] $= f(\xi) \arctan \frac{x}{h} \Big|_0^{h^{1/4}} = f(\xi) \arctan \frac{1}{h^{3/4}} \to f(0)\dfrac{\pi}{2} \quad (h \to 0^+)$
[Sentence 7] $|I_2| = \left| \int_{h^{1/4}}^1 \frac{h}{h^2 + x^2} f(x) dx \right| \leq M \int_{h^{1/4}}^1 \frac{h}{h^2 + x^2} dx(\quad |f(x)|\leq M\quad)$
[Sentence 8] $= M \left( \arctan \frac{1}{h} - \arctan \frac{1}{h^{3/4}} \right) \to 0 \quad (h \to 0^+)$
[Sentence 9] 因此$h\to 0^+$时$I_1+I_2\to f(0)\dfrac{\pi}{2}$

<thinking>
Round 1

假设 $f(x)$ 在 $[0,1]$ 上连续

这是证明的开头，$f$是新引入的变量。所以，更准确的写法是"$\forall f:\R \to \R$，假设$f$在$[0,1]$上连续"
</thinking>

<result>
$\forall f:\R \to \R$，假设$f$在$[0,1]$上连续
</result>

<thinking>
Round 2

证明: $\lim_{h \to 0^+} \int_0^1 \frac{h}{h^2 + x^2} f(x) dx = \frac{\pi}{2} f(0)$

不需要修改。
</thinking>

<result>
证明: $\lim_{h \to 0^+} \int_0^1 \frac{h}{h^2 + x^2} f(x) dx = \frac{\pi}{2} f(0)$
</result>

<thinking>
Round 3

$\int_0^1 \frac{h}{h^2 + x^2} f(x) dx = \int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx + \int_{h^{1/4}}^1 \frac{hf(x)}{h^2 + x^2} dx$

证明引入了一个自由变量$h$，所以必须补充量词。根据上下文，这里应该补充全称量词。但是$h$的取值范围是什么呢？根据上下文可知，这段证明是要证明0的右极限，所以$h$只需要在0的右邻域取值就可以了。根据上下文，此处令$h$属于$(0,1/2)$是一个合理的设定。
</thinking>

<result>
$\forall h \in (0,1/2)$，$\int_0^1 \frac{h}{h^2 + x^2} f(x) dx = \int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx + \int_{h^{1/4}}^1 \frac{hf(x)}{h^2 + x^2} dx$
</result>

<thinking>
Round 4

"令$I_1 = \int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx$, $I_2 = \int_{h^{1/4}}^1 \frac{hf(x)}{h^2 + x^2} dx$"

这句话是两个并列的动作，我需要把它拆分成两句话。
</thinking>

<result>
令$I_1 = \int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx$
令$I_2 = \int_{h^{1/4}}^1 \frac{hf(x)}{h^2 + x^2} dx$
</result>

<thinking>
Round 5

"其中$I_1 = \int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx = f(\xi) \int_0^{h^{1/4}} \frac{h}{h^2 + x^2} dx \quad (0 \leq \xi \leq h^{1/4})$"

这是连等式，我需要做拆分。
第一个等号是：$I_1 = \int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx$
第二个等号是：$\int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx = f(\xi) \int_0^{h^{1/4}} \frac{h}{h^2 + x^2} dx \quad (0 \leq \xi \leq h^{1/4})$
其中，第二个等号中的$\xi$应该是由存在量词引入的，我需要补充出来，写为$\exists \xi, (0 \leq \xi \leq h^{1/4}) \land \int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx = f(\xi) \int_0^{h^{1/4}} \frac{h}{h^2 + x^2} dx$
</thinking>

<result>
其中$I_1 = \int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx$
$\exists \xi, (0 \leq \xi \leq h^{1/4}) \land \int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx = f(\xi) \int_0^{h^{1/4}} \frac{h}{h^2 + x^2} dx$
</result>


<thinking>
Round 6

"$= f(\xi) \arctan \frac{x}{h} \Big|_0^{h^{1/4}} = f(\xi) \arctan \frac{1}{h^{3/4}} \to f(0)\dfrac{\pi}{2} \quad (h \to 0^+)$"

这句话承接上一句话，我要把上一句话里的连等号的最后一项加上，变成$f(\xi) \int_0^{h^{1/4}} \frac{h}{h^2 + x^2} dx= f(\xi) \arctan \frac{x}{h} \Big|_0^{h^{1/4}} = f(\xi) \arctan \frac{1}{h^{3/4}} \to f(0)\dfrac{\pi}{2} \quad (h \to 0^+)$。最后的$h \to 0^+$是简写，完整的写法应该把这句话分割成两个句子，其中第二个句子用lim符号写出：$f(\xi) \int_0^{h^{1/4}} \frac{h}{h^2 + x^2} dx= f(\xi) \arctan \frac{x}{h} \Big|_0^{h^{1/4}} = f(\xi) \arctan \frac{1}{h^{3/4}}$； $\lim\limits_{h\to 0^+}f(\xi) \arctan \frac{1}{h^{3/4}} =f(0)\dfrac{\pi}{2}$。
</thinking>

<result>
$f(\xi) \int_0^{h^{1/4}} \frac{h}{h^2 + x^2} dx= f(\xi) \arctan \frac{x}{h} \Big|_0^{h^{1/4}} = f(\xi) \arctan \frac{1}{h^{3/4}}$
$\lim\limits_{h\to 0^+}f(\xi) \arctan \frac{1}{h^{3/4}} =f(0)\dfrac{\pi}{2}$
</result>

<thinking>
Round 7

"$|I_2| = \left| \int_{h^{1/4}}^1 \frac{h}{h^2 + x^2} f(x) dx \right| \leq M \int_{h^{1/4}}^1 \frac{h}{h^2 + x^2} dx(\quad |f(x)|\leq M\quad)$"

这句话在处理x和M这两个变量时很不严谨。可以看到$M$是$f(x)$的一个界，所以严谨的表达应该是：$\exists M \in \R,\forall x \in [0,1],|f(x)|\leq M$，并且$|I_2| = \left| \int_{h^{1/4}}^1 \frac{h}{h^2 + x^2} f(x) dx \right| \leq M \int_{h^{1/4}}^1 \frac{h}{h^2 + x^2} dx$
</thinking>

<result>
$\exists M \in \R,\forall x \in [0,1],|f(x)|\leq M$，并且$|I_2| = \left| \int_{h^{1/4}}^1 \frac{h}{h^2 + x^2} f(x) dx \right| \leq M \int_{h^{1/4}}^1 \frac{h}{h^2 + x^2} dx$
</result>

<thinking>
Round 8

"$= M \left( \arctan \frac{1}{h} - \arctan \frac{1}{h^{3/4}} \right) \to 0 \quad (h \to 0^+)$"

这里的等号承接上一句话，我要把上一句话里的连等号的最后一项加上，变成$M \int_{h^{1/4}}^1 \frac{h}{h^2 + x^2} dx= M \left( \arctan \frac{1}{h} - \arctan \frac{1}{h^{3/4}} \right)...$。其中$h \to 0^+$是简写，严格的写法应该用lim符号。写作两个分句：$M \int_{h^{1/4}}^1 \frac{h}{h^2 + x^2} dx= M \left( \arctan \frac{1}{h} - \arctan \frac{1}{h^{3/4}} \right)$, $\lim\limits_{h \to 0^+}M \left( \arctan \frac{1}{h} - \arctan \frac{1}{h^{3/4}} \right) = 0$
</thinking>

<result>
$M \int_{h^{1/4}}^1 \frac{h}{h^2 + x^2} dx= M \left( \arctan \frac{1}{h} - \arctan \frac{1}{h^{3/4}} \right)$
$\lim\limits_{h \to 0^+}M \left( \arctan \frac{1}{h} - \arctan \frac{1}{h^{3/4}} \right) = 0$
</result>

<thinking>
Round 9

"$因此$h\to 0^+$时$I_1+I_2\to f(0)\dfrac{\pi}{2}$"

严格的形式应该用极限符号lim。$\lim\limits_{h \to 0^+}I_1+I_2\to f(0)\dfrac{\pi}{2}$
</thinking>

<result>
$\lim\limits_{h \to 0^+}I_1+I_2\to f(0)\dfrac{\pi}{2}$
</result>

<thinking>
Round 10

证明已结束。输出"End."。
</thinking>

<result>
End.
</result>

（请特别注意！！！！！并不是要你一次性输出全部的Round 1到Round 10，而是我们会给你证明文本，以及历史已有的Round，已经修改的文本，要求你输出下一个Round。比如，给定的历史Round如果是Round 1到Round 5，那么你需要输出Round 6。你的输出只需包含一个thinking字段和一个result字段。）