你需要你帮我提取数学自然语言的结构，用json格式输出。

## 数学结构的定义

### 结构介绍

数学自然语言的结构是带有类型的节点序列。节点共有八种类型：

[Show: "P"] - 下面证明命题P (P可以是列表)
    常见的可以识别为Show的自然语言表达：
        "下面证明集合S不为空"；
        "我们来证明集合S⊆T"
[Assume: "P"] - 假设命题P成立 (P可以是列表)
    常见的可以识别为Assume的自然语言表达：
        "假设a+b>1"
        "假设a+b>1不成立"
[Have: "P" by "Q"] - 根据一列“定理/已得到的命题/自然语言提示”Q，得出命题P成立 (P,Q可以是列表)
    常见的可以识别为Have的自然语言表达：
        "根据逆的唯一性，我们有A=B"
        "我们有x^2>0"
        "因此f(x)=g(x)"
[Fix: {var_list} such that "P"] - 取定变量列表var_list，这些变量满足命题P (P可以是列表)
    常见的可以识别为Fix的自然语言表达：
        "给定任意X ∈ A"
        "取 x ∈ R"
[SufficeToProve: "P" by "Q"] - 提出要证明当前目标，只需证明命题P，理由为Q (P,Q可以是列表)
    常见的可以识别为SufficeToProve的自然语言表达：
        "只需证..."
        "根据...，所以只需证..."
[ToHave: "P"] - 要使得...成立，与OnlyNeeds连着使用（P可以是列表）
[OnlyNeeds: "P" by "Q"] - 只需...成立，跟在OnlyNeeds后方 (P,Q可以是列表)
    常见的可以识别为ToHave, OnlyNeeds的自然语言表达：
        "要使得...成立， 只需..."
        "要使得...成立， 只需...，即...，那么只需..."
[Find: {var_list} such that "P"] - 求解满足命题P的变量列表 (P可以是列表)
    常见的可以识别为Find的自然语言表达：
        "求满足x^2+2x+1=0的x"；
        "我们要找出满足x>y的f(x)的取值范围"；
        "求$\int x^2 dx$"（此时P为空）
[Define: "A" as "B"] - 定义一个“符号/概念”A，其含义是B (A,B不能是列表)
    常见的可以识别为Define的自然语言表达：
        "我们用符号a ⊆ b来表示∀x, (x∈a) -> (x∈b)"
        "令f(x):=x^2"
[Hint: "string"] - 一个自然语言注释
    常见的可以识别为Hint的自然语言表达：
        "我们按照...的思路来证明"
        "于是我们可以得到答案了"
        "让我们看看接下来会发生什么"

### JSON定义

以下是数学结构的json定义：

```
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "ProofStructure": {
            "type": "array",
            "items": {
                "anyOf": [
                    {"$ref": "#/$defs/Show"},
                    {"$ref": "#/$defs/Assume"},
                    {"$ref": "#/$defs/Have"},
                    {"$ref": "#/$defs/Fix"},
                    {"$ref": "#/$defs/SufficeToProve"},
                    {"$ref": "#/$defs/ToHave"},
                    {"$ref": "#/$defs/OnlyNeeds"},
                    {"$ref": "#/$defs/Find"},
                    {"$ref": "#/$defs/Define"},
                    {"$ref": "#/$defs/Hint"}
                ]
            }
        }
    },
    "required": ["ProofStructure"],
    "additionalProperties": False,
    "$defs": {
        "Show": {
            "type": "object",
            "properties": OrderedDict([
                ("type", {"type": "string", "const": "Show"}),
                ("proposition", {
                    "type": "array",
                    "items": {"type": "string"},
                    "default": []
                })
            ]),
            "required": ["type", "proposition"],
            "additionalProperties": False
        },
        "Assume": {
            "type": "object",
            "properties": OrderedDict([
                ("type", {"type": "string", "const": "Assume"}),
                ("assumption", {
                    "type": "array",
                    "items": {"type": "string"},
                    "default": []
                })
            ]),
            "required": ["type", "assumption"],
            "additionalProperties": False
        },
        "Have": {
            "type": "object",
            "properties": OrderedDict([
                ("type", {"type": "string", "const": "Have"}),
                ("proposition", {
                    "type": "array",
                    "items": {"type": "string"},
                    "default": []
                }),
                ("reasons", {
                    "type": "array",
                    "items": {"type": "string"},
                    "default": []
                })
            ]),
            "required": ["type", "proposition", "reasons"],
            "additionalProperties": False
        },
        "Fix": {
            "type": "object",
            "properties": OrderedDict([
                ("type", {"type": "string", "const": "Fix"}),
                ("var_list", {"type": "array", "items": {"type": "string"}}),
                ("condition", {
                    "type": "array",
                    "items": {"type": "string"},
                    "default": []
                })
            ]),
            "required": ["type", "var_list", "condition"],
            "additionalProperties": False
        },
        "SufficeToProve": {
            "type": "object",
            "properties": OrderedDict([
                ("type", {"type": "string", "const": "SufficeToProve"}),
                ("proposition", {
                    "type": "array",
                    "items": {"type": "string"},
                    "default": []
                }),
                ("reasons", {
                    "type": "array",
                    "items": {"type": "string"},
                    "default": []
                })
            ]),
            "required": ["type", "proposition", "reasons"],
            "additionalProperties": False
        },
        "ToHave": {
            "type": "object",
            "properties": OrderedDict([
                ("type", {"type": "string", "const": "ToHave"}),
                ("proposition", {
                    "type": "array",
                    "items": {"type": "string"},
                    "default": []
                }),
            ]),
            "required": ["type", "proposition"],
            "additionalProperties": False
        },
        "OnlyNeeds": {
            "type": "object",
            "properties": OrderedDict([
                ("type", {"type": "string", "const": "OnlyNeeds"}),
                ("proposition", {
                    "type": "array",
                    "items": {"type": "string"},
                    "default": []
                }),
                ("reasons", {
                    "type": "array",
                    "items": {"type": "string"},
                    "default": []
                })
            ]),
            "required": ["type", "proposition", "reasons"],
            "additionalProperties": False
        },
        "Find": {
            "type": "object",
            "properties": OrderedDict([
                ("type", {"type": "string", "const": "Find"}),
                ("var_list", {"type": "array", "items": {"type": "string"}}),
                ("condition", {
                    "type": "array",
                    "items": {"type": "string"},
                    "default": []
                })
            ]),
            "required": ["type", "var_list", "condition"],
            "additionalProperties": False
        },
        "Define": {
            "type": "object",
            "properties": OrderedDict([
                ("type", {"type": "string", "const": "Define"}),
                ("symbol", {"type": "string"}),
                ("meaning", {
                    "type": "array",
                    "items": {"type": "string"},
                    "default": []
                })
            ]),
            "required": ["type", "symbol", "meaning"],
            "additionalProperties": False
        },
        "Hint": {
            "type": "object",
            "properties": OrderedDict([
                ("type", {"type": "string", "const": "Hint"}),
                ("comment", {"type": "string"})
            ]),
            "required": ["type", "comment"],
            "additionalProperties": False
        }
    }
}
```

## 结构提取要求

1. 按照自然语言的顺序逐句转化，不要擅自增加或删减自然语言表达
2. 当引入一个新的变量名时，需用Fix或Define结构
3. 在特定情况下，需补充必要的命题内容或逻辑关系，具体见下面的样例

## 样例

在样例中，我不完整写出json作为示例，而是写一个简洁的图示。在一些样例中，我包含了“解释”部分的内容，这部分内容是我为了向你说明如何提取结构以及要注意的事项，不是你要输出的内容！！！

### 样例 1

输入：

If $A \subseteq B$, then $\mathcal{P}(A) \subseteq \mathcal{P}(B)$:

Let $X \in \mathcal{P}(A)$. By definition of power set, $X \subseteq A$. Since $A \subseteq B$, it follows that $X \subseteq B$. Therefore, $X \in \mathcal{P}(B)$. Hence, every element of $\mathcal{P}(A)$ is also in $\mathcal{P}(B)$, so $\mathcal{P}(A) \subseteq \mathcal{P}(B)$.

解释：

下面我们向你示范如何提取该证明的结构。

首先，引入了变量A,B以及一个假设$A \subseteq B$。所以这一小句被识别为Fix类型的节点：[Fix: {A,B} such that "$A \subseteq B$"]，表示固定变量A,B，这两个变量满足条件$A \subseteq B$。

在这一假设下，我们要证明$\mathcal{P}(A) \subseteq \mathcal{P}(B)$，所以这一小句被识别为Show类型节点：[Show: "$\mathcal{P}(A) \subseteq \mathcal{P}(B)$"]

Let $X \in \mathcal{P}(A)$，引入了一个新变量X，满足$X \in \mathcal{P}(A)$。所以这是一个Fix类型的节点：[Fix: {X} such that "$X \in \mathcal{P}(A)$"]

By definition of power set, $X \subseteq A$. 这是一个断言，因此是Have类型节点。其中，断言内容是$X \subseteq A$，其依据是By definition of power set。所以结构为：[Have: "$X \subseteq A$" by "definition of power set"]

Since $A \subseteq B$, it follows that $X \subseteq B$。这是一个断言，因此是Have类型节点。其中，断言内容是$X \subseteq B$，其依据是$A \subseteq B$。所以结构为：[Have: "$X \subseteq B$" by "$A \subseteq B$"]

Therefore, $X \in \mathcal{P}(B)$. 这是一个断言，推理依据为空。所以结构为：[Have: "$X \in \mathcal{P}(B)$"]

Hence, every element of $\mathcal{P}(A)$ is also in $\mathcal{P}(B)$. 这是一个断言，推理依据为空。所以结构为：[Have: "every element of $\mathcal{P}(A)$ is also in $\mathcal{P}(B)$"]

$\mathcal{P}(A) \subseteq \mathcal{P}(B)$. 这是一个断言，推理依据为空。所以结构为：[Have: "$\mathcal{P}(A) \subseteq \mathcal{P}(B)$"]

结构：

[Fix: {A,B} such that "$A \subseteq B$"]
[Show: "$\mathcal{P}(A) \subseteq \mathcal{P}(B)$"]
[Fix: {X} such that "$X \in \mathcal{P}(A)$"]
[Have: "$X \subseteq A$" by "definition of power set"]
[Have: "$X \subseteq B$" by "$A \subseteq B$"]
[Have: "$X \in \mathcal{P}(B)$"]
[Have: "every element of $\mathcal{P}(A)$ is also in $\mathcal{P}(B)$"]
[Have: "$\mathcal{P}(A) \subseteq \mathcal{P}(B)$"]

### 样例 2

输入：

下面我们对$x^3-4x^2+2x+1$做因式分解。观察到$x=1$是$\text{原式}=0$的一个解，所以可以令$x^3-4x^2+2x+1=(x-1)(x^2+ax+b)$。有$(x-1)(x^2+ax+b)=x^3+(a-1)x^2+(b-a)x-b$。对比系数可得$a-1=-4,b-a=2,-b=1$。解得$a=-3,b=-1$。于是完成因式分解：$x^3-4x^2+2x+1=(x-1)(x^2-3x-1)$。

解释：

在这个样例的结构提取中要注意以下几点：

“下面我们对$x^3-4x^2+2x+1$做因式分解”应该被识别为一个Hint节点。

“观察到$x=1$是$\text{原式}=0$的一个解”是一个断言，所以是Have类型节点。注意，在结构提取的时候，你需要把“原式”给补充出来。也即，你不要写[Have: "$x=1$是$\text{原式}=0$的一个解"]，而是写[Have: "$x=1$是$x^3-4x^2+2x+1=0$的一个解"]

“所以可以令$x^3-4x^2+2x+1=(x-1)(x^2+ax+b)$”中，虽然没有显示说明，但其实引入了两个新的变量a,b。引入变量必须用Fix或Define。在这里，因为a,b并不是被“定义”的，而是“待定系数法”的系数，所以我们将其识别为Fix类型节点。写[Fix: {a,b} such that "$x^3-4x^2+2x+1=(x-1)(x^2+ax+b)$"]

“于是完成因式分解”不是断言，它是自然语言中的“注解”或“解释说明”。对于这样的内容，我们将其识别为Hint节点。写[Hint: "于是完成因式分解"]

结构：

[Hint: "下面我们对$x^3-4x^2+2x+1$做因式分解"]
[Have: "$x=1$是$x^3-4x^2+2x+1=0$的一个解"]
[Fix: {a,b} such that "$x^3-4x^2+2x+1=(x-1)(x^2+ax+b)$"]
[Have: "$(x-1)(x^2+ax+b)=x^3+(a-1)x^2+(b-a)x-b$"]
[Have: "$a-1=-4,b-a=2,-b=1$" by "对比系数"]
[Have: "$a=-3,b=-1$" by "解得"]
[Hint: "于是完成因式分解"]
[Have: "$x^3-4x^2+2x+1=(x-1)(x^2-3x-1)$"]

### 样例 3

输入：

$1 + 2 + \cdots  + n = \frac{n\left( {n + 1}\right) }{2}$ .

证：
我们用数学归纳法证明
当 $n = 1$ 时，等式成立.
假设$n=k$时等式成立
则$n=k+1$时有
$1 + 2 + \cdots  + k + \left( {k + 1}\right)  = \frac{k\left( {k + 1}\right) }{2} + k + 1 = \frac{\left( {k + 1}\right) \left\lbrack  {\left( {k + 1}\right)  + 1}\right\rbrack  }{2}$
所以$n = k+ 1$ 时等式也成立.
于是,对于任何正整数 $n$ ,有 $1 + 2 + \cdots  + n = \frac{n\left( {n + 1}\right) }{2}$ .

注意事项：

“我们用数学归纳法证明”只是为接下来要用的证明方法做出提示、注解，所以应该被识别为Hint节点：[Hint: "我们用数学归纳法证明"]

“当 $n = 1$ 时，等式成立”中，我们希望把“等式”是什么给补充出来。不要写[Have: "当 $n = 1$ 时，等式成立"]，而是写[Have: "当$n=1$时$1 + 2 + \cdots + n = \frac{n(n+1)}{2}$成立"]。

长的连等式要放进同一个Have节点中，不要做拆分。

结构：

[Show: "$1 + 2 + \cdots + n = \frac{n(n+1)}{2}$"]
[Hint: "我们用数学归纳法证明"]
[Have: "当$n=1$时$1 + 2 + \cdots + n = \frac{n(n+1)}{2}$成立"]
[Assume: "$n=k$时$1 + 2 + \cdots + n = \frac{n(n+1)}{2}$成立"]
[Have: "$1 + 2 + \cdots  + k + \left( {k + 1}\right)  = \frac{k\left( {k + 1}\right) }{2} + k + 1 = \frac{\left( {k + 1}\right) \left\lbrack  {\left( {k + 1}\right)  + 1}\right\rbrack  }{2}$"]
[Have: "$n=k+1$时$1 + 2 + \cdots + n = \frac{n(n+1)}{2}$成立"]
[Have: "对于任何正整数$n$,有$1 + 2 + \cdots + n = \frac{n(n+1)}{2}$"]

### 样例 4

输入：

$\mathop{\lim }\limits_{{n \rightarrow  \infty }}\sqrt[n]{a} = 1\;\left( {a > 0}\right)$ .

提示 分别就 $a = 1,a > 1$ 及 $0 < a < 1$ 三种情形加以证明.

证 (1) 当 $a = 1$ 时,等式显然成立;

(2)当 $a > 1$ 时,因为 ${\left( 1 + \varepsilon \right) }^{n} > 1 + {n\varepsilon }\left( {n > 1,\varepsilon  > 0}\right)$ ,则当 $n$ 充分大后,可使 $1 + {n\varepsilon } > a$ ,即 ${\left( 1 + \varepsilon \right) }^{n} > a$ . 事实上,只要取 $N = \left\lceil  \frac{a - 1}{\varepsilon }\right\rceil$ ,当 $n > N$ 时,就可保证这点. 所以, $1 < \sqrt[n]{a} < 1 + \varepsilon$ ,于是,当 $n > N$ 时, $\left| {\sqrt[n]{a} - 1}\right|  < \varepsilon$ ,此即 $\mathop{\lim }\limits_{{n \rightarrow  \infty }}\sqrt[n]{a} = 1$ ;

(3) 当 $0 < a < 1$ 时,则令 $a = \frac{1}{{a}^{\prime }}$ ,其中 ${a}^{\prime } > 1$ . 于是,当 $n \rightarrow  \infty$ 时, $\sqrt[n]{a} = \frac{1}{\sqrt[n]{{a}^{\prime }}} \rightarrow  1$ . 总之,当 $a > 0$ 时, $\mathop{\lim }\limits_{{n \rightarrow  \infty }}\sqrt[n]{a} = 1$.

注意事项：

变量a贯穿整个证明，所以在最开头用Fix节点引入a
对于分类讨论的每一种情况，用一个Assume作为当前类别的假设。
“当$n$充分大后”虽然不是一个严谨的数学表达，但我们还是将其当作有含义的假设，写[Assume: "$n$ 充分大后"]，我们这么做是因为我们知道像这样不严谨的数学语言其实指向一种更严谨的数学表达。千万不能将这样的表达识别为“Hint节点”，Hint节点是那些辅助性、引导性的、不表达任何新的信息的表达。
“取$N = \left\lceil  \frac{a - 1}{\varepsilon }\right\rceil$”可以识别为Define，也可以识别为Fix。因为这里既可以认为是基于给定的a,ɛ取一个任意满足条件$N = \left\lceil  \frac{a - 1}{\varepsilon }\right\rceil$的N，也可以认为将N定义为$N = \left\lceil  \frac{a - 1}{\varepsilon }\right\rceil$。后者更直观一些，所以这里选择Define。

结构：

[Fix: {a} such that "a > 0"]
[Show: "$\mathop{\lim }\limits_{{n \rightarrow  \infty }}\sqrt[n]{a} = 1$"]
[Hint: "分别就$a=1,a>1$及$0<a<1$三种情形加以证明"]
[Assume: "$a=1$"]
[Have: "$\mathop{\lim }\limits_{{n \rightarrow  \infty }}\sqrt[n]{a} = 1$"]
[Assume: "$a>1$"]
[Fix: {n, ɛ} such that "$n>1$"; "$\varepsilon>0$"]
[Have: "{\left( 1 + \varepsilon \right) }^{n} > 1 + {n\varepsilon }"]
[Assume: "$n$ 充分大后"]
[Have: "$1 + {n\varepsilon } > a$"]
[Have: "${\left( 1 + \varepsilon \right) }^{n} > a$"]
[Define: {N} as "$N = \left\lceil  \frac{a - 1}{\varepsilon }\right\rceil$"]
[Have: "当$n > N$时${\left( 1 + \varepsilon \right) }^{n} > a$"]
[Have: "$1 < \sqrt[n]{a} < 1 + \varepsilon$"]
[Have: "当$n > N$时$\left| {\sqrt[n]{a} - 1}\right|  < \varepsilon$"]
[Have: "$\mathop{\lim }\limits_{{n \rightarrow  \infty }}\sqrt[n]{a} = 1$"]
[Assume: "$0 < a < 1$"]
[Define: {a'} such that "$a = \frac{1}{{a}^{\prime }} ; "a'>1"]
[Have: "当$n \rightarrow  \infty$时$\sqrt[n]{a} = \frac{1}{\sqrt[n]{{a}^{\prime }}} \rightarrow  1$"]
[Have: "当$a > 0$时$\mathop{\lim }\limits_{{n \rightarrow  \infty }}\sqrt[n]{a} = 1$"]

### 样例 5

输入：

假设 $f(x)$ 在 $[0,1]$ 上连续，证明: $\lim_{h \to 0^+} \int_0^1 \frac{h}{h^2 + x^2} f(x) dx = \frac{\pi}{2} f(0)$

Pf:

$\int_0^1 \frac{h}{h^2 + x^2} f(x) dx = \int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx + \int_{h^{1/4}}^1 \frac{hf(x)}{h^2 + x^2} dx$

令$I_1 = \int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx$, $I_2 = \int_{h^{1/4}}^1 \frac{hf(x)}{h^2 + x^2} dx$

其中

$I_1 = \int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx = f(\xi) \int_0^{h^{1/4}} \frac{h}{h^2 + x^2} dx \quad (0 \leq \xi \leq h^{1/4})$

$= f(\xi) \arctan \frac{x}{h} \Big|_0^{h^{1/4}} = f(\xi) \arctan \frac{1}{h^{3/4}} \to f(0)\dfrac{\pi}{2} \quad (h \to 0^+)$

$|I_2| = \left| \int_{h^{1/4}}^1 \frac{h}{h^2 + x^2} f(x) dx \right| \leq M \int_{h^{1/4}}^1 \frac{h}{h^2 + x^2} dx(\quad \forall x\in [0,1], |f(x)|\leq M\quad)$

$= M \left( \arctan \frac{1}{h} - \arctan \frac{1}{h^{3/4}} \right) \to 0 \quad (h \to 0^+)$

因此$h\to 0^+$时$I_1+I_2\to f(0)\dfrac{\pi}{2}$

Qed.

注意事项：
不要把长的连等式拆分开，而是应当写到同一个Have当中

结构：

[Fix: {f} such that "$f(x)$ 在 $[0,1]$ 上连续"]
[Show: "$\lim_{h \to 0^+} \int_0^1 \frac{h}{h^2 + x^2} f(x) dx = \frac{\pi}{2} f(0)$"]
[Have: "$\int_0^1 \frac{h}{h^2 + x^2} f(x) dx = \int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx + \int_{h^{1/4}}^1 \frac{hf(x)}{h^2 + x^2} dx$"]
[Define: {I1} as "$I_1 = \int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx$"]
[Define: {I2} as "$I_2 = \int_{h^{1/4}}^1 \frac{hf(x)}{h^2 + x^2} dx$"]
[Have: "$I_1 = \int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx = f(\xi) \int_0^{h^{1/4}} \frac{h}{h^2 + x^2} dx \quad (0 \leq \xi \leq h^{1/4})= f(\xi) \arctan \frac{x}{h} \Big|_0^{h^{1/4}} = f(\xi) \arctan \frac{1}{h^{3/4}} \to f(0)\dfrac{\pi}{2} \quad (h \to 0^+)$"]
[Have: "$|I_2| = \left| \int_{h^{1/4}}^1 \frac{h}{h^2 + x^2} f(x) dx \right| \leq M \int_{h^{1/4}}^1 \frac{h}{h^2 + x^2} dx(\quad \forall x\in [0,1], |f(x)|\leq M\quad)= M \left( \arctan \frac{1}{h} - \arctan \frac{1}{h^{3/4}} \right) \to 0 \quad (h \to 0^+)$"]
[Have: "$h\to 0^+$时$I_1+I_2\to f(0)\dfrac{\pi}{2}$"]

### 样例 6

设 $|q| < 1$，证明等比数列  $x_n=q^{n-1}$ 的极限是 0。
证  
$\forall \varepsilon > 0$（设 $\varepsilon < 1$），因为  $|x_n - 0| = |q^{n-1} - 0| = |q|^{n-1},$ 
要使 $|x_n - 0| < \varepsilon$，只要  $|q|^{n-1} < \varepsilon.$
取自然对数，得  $(n-1) \ln |q| < \ln \varepsilon.$
因 $|q| < 1$，$\ln |q| < 0$，故  $n > 1 + \frac{\ln \varepsilon}{\ln |q|}.$
取  $N = \left\lceil 1 + \frac{\ln \varepsilon}{\ln |q|} \right\rceil,$
则当 $n > N$ 时，就有  $|q^{n-1} - 0| < \varepsilon,$
即  $\lim_{n \to \infty} q^{n-1} = 0.$

注意事项：
注意本例中ToHave, OnlyNeeds的使用。第一个OnlyNeeds的识别是容易的，因为自然语言用的词就是“只要”。但是，我们要识别出来第二个和第三个也是“取自然对数，得  $(n-1) \ln |q| < \ln \varepsilon.$”和“因 $|q| < 1$，$\ln |q| < 0$，故  $n > 1 + \frac{\ln \varepsilon}{\ln |q|}.$”也还是在做反向推导，也要用OnlyNeeds，其中推导的理由用by写出。

结构：

[Fix: {q} such that "$|q| < 1$"]
[Show: "等比数列$\lim_{n \to \infty} q^{n-1} = 0$"]
[Fix: {ε} such that "$0 < ε < 1$"]
[Have: "$|x_n - 0| = |q^{n-1} - 0| = |q|^{n-1}$"]
[ToHave: "$|x_n - 0| < ε$"]
[OnlyNeeds: "$|q|^{n-1} < ε$"]
[OnlyNeeds: "$(n-1) \ln |q| < \ln ε$" by "取自然对数"]
[OnlyNeeds: "$n > 1 + \frac{\ln ε}{\ln |q|}$" by {"$|q| < 1$"; "$\ln |q| < 0$"}]
[Define: {N} as "$N = \left\lceil 1 + \frac{\ln ε}{\ln |q|} \right\rceil$"]
[Have: "当$n > N$时，$|q^{n-1} - 0| < ε$"]
[Have: "$\lim_{n \to \infty} q^{n-1} = 0$"]

### 样例 7

输入：

【819】求对于所有实数 $x$ 和 $y$ 都满足方程组:

$$
f\left( {x + y}\right)  = f\left( x\right) f\left( y\right)  - g\left( x\right) g\left( y\right) ,
$$

$$
g\left( {x + y}\right)  = f\left( x\right) g\left( y\right)  + f\left( y\right) g\left( x\right) ,
$$

以及规范条件

$$
f\left( 0\right)  = 1\text{ 和 }g\left( 0\right)  = 0
$$

的所有的有界连续函数 $f\left( x\right)$ 和 $g\left( x\right) \left( {-\infty  < x <  + \infty }\right)$ .

提示 考虑函数 $F\left( x\right)  = {f}^{2}\left( x\right)  + {g}^{2}\left( x\right)$ .

解 考虑函数 $F\left( x\right)  = {f}^{2}\left( x\right)  + {g}^{2}\left( x\right)$ ,则

$$
F\left( {x + y}\right)  = {f}^{2}\left( {x + y}\right)  + {g}^{2}\left( {x + y}\right)
$$

$$
= {\left\lbrack  f\left( x\right) f\left( y\right)  - g\left( x\right) g\left( y\right) \right\rbrack  }^{2} + {\left\lbrack  f\left( x\right) g\left( y\right)  + f\left( y\right) g\left( x\right) \right\rbrack  }^{2} = F\left( x\right) F\left( y\right) ,
$$

由于 $F\left( 0\right)  = 1$ 及 $F\left( x\right)  ≢ 0$ ,故

$$
F\left( x\right)  = {a}^{x}\;\left( {-\infty  < x <  + \infty }\right) ,
$$

式中 $a = F\left( 1\right)$ 为正的常数 ${}^{*)}$ .

由于 $f\left( x\right)$ 及 $g\left( x\right)$ 有界,故只能有 $a = 1$ . 因此,对于所有的实数 $x$ ,有 ${f}^{2}\left( x\right)  + {g}^{2}\left( x\right)  = 1$ . 因为

$$
0 = g\left( 0\right)  = g\left( {x - x}\right)  = f\left( x\right) g\left( {-x}\right)  + f\left( {-x}\right) g\left( x\right)
$$

及

$$
1 = f\left( 0\right)  = f\left( {x - x}\right)  = f\left( x\right) f\left( {-x}\right)  - g\left( {-x}\right) g\left( x\right) .
$$

上面二式分别乘以 $g\left( {-x}\right)$ 及 $f\left( {-x}\right)$ ,然后相加,得

$$
f\left( {-x}\right)  = f\left( x\right) \left\lbrack  {{f}^{2}\left( {-x}\right)  + {g}^{2}\left( {-x}\right) }\right\rbrack   = f\left( x\right) ;
$$

如果上面二式分别乘以 $f\left( {-x}\right)$ 及 $g\left( {-x}\right)$ ,然后相减,得

$$
g\left( {-x}\right)  =  - g\left( x\right) \left\lbrack  {{g}^{2}\left( {-x}\right)  + {f}^{2}\left( {-x}\right) }\right\rbrack   =  - g\left( x\right) .
$$

从而可得

$$
f\left( {x + y}\right)  + f\left( {x - y}\right)  = f\left( x\right) f\left( y\right)  - g\left( x\right) g\left( y\right)  + f\left( x\right) f\left( {-y}\right)  - g\left( x\right) g\left( {-y}\right)  = {2f}\left( x\right) f\left( y\right) .
$$

于是,考虑到 $f\left( x\right)$ 的有界性,可得

$$
f\left( x\right)  = \cos a{x}^{* * )},
$$

再由 ${f}^{2}\left( x\right)  + {g}^{2}\left( x\right)  = 1$ 可得

$$
g\left( x\right)  =  \pm  \sin {ax}.
$$

注意事项：
注意本例不是一个证明，而是一个问题求解过程。问题是要求满足一些复杂条件的函数f,g，所以开头用Find。

结构：

[Find: {f,g} such that  {"对于所有实数 $x$ 和 $y$ 都满足方程组 $f(x + y) = f(x) f(y) - g(x) g(y)$, $g(x + y) = f(x) g(y) + f(y) g(x)$"; "规范条件$f(0) = 1$, $g(0) = 0$"; "$f(x), g(x)$ 连续且有界"}]
[Hint: "考虑 $F(x) = f^2(x) + g^2(x)$"]
[Define: "F" as "$F(x) = f^2(x) + g^2(x)$"]
[Have: "$F(x+y) = f^2(x+y) + g^2(x+y) ={\left\lbrack  f\left( x\right) f\left( y\right)  - g\left( x\right) g\left( y\right) \right\rbrack  }^{2} + {\left\lbrack  f\left( x\right) g\left( y\right)  + f\left( y\right) g\left( x\right) \right\rbrack  }^{2} = F\left( x\right) F\left( y\right)$"]
[Fix: {a} such that "a = F(1) > 0"]
[Have: "$F(x) = a^x$" by ["$F(0)=1$" ; "$F(x) \not\equiv 0$"]]
[Have: "a = 1" by "$f(x)$ 和 $g(x)$ 有界"]
[Have: "$f^2(x) + g^2(x) = 1$ 对所有实数 $x$ 成立"]
[Have: "$0=g(0)=g(x-x) = f(x)g(-x) + f(-x)g(x)$"]
[Have: "$1=f(0)=f(x-x) = f(x)f(-x) - g(-x)g(x)$"]
[Have: "$f(-x) = f(x)[f^2(-x) + g^2(-x)] = f(x)$" by "上面两式分别乘以$g(-x)$和$f(-x)$，然后相加"]
[Have: "$g(-x) = -g(x)[g^2(-x) + f^2(-x)] = -g(x)$" by "上面两式分别乘以$f(-x)$和$g(-x)$，然后相减"]
[Have: "$f(x+y)+f(x-y)=f(x)f(y) - g(x)g(y) + f(x)f(-y) - g(x)g(-y) = 2f(x)f(y)$"]
[Have: "$f(x) = \cos a x$" by "$f(x)$的有界性"]
[Have: "$g(x) = \pm \sin a x$" by "$f^2(x) + g^2(x) = 1$"]

### 样例 8

输入：

设 $\{x_n\}$ 是实数上的数列，满足 $\forall n \geq 1, x_n = n^{(-1)^n}$。请证明：$\{x_n\}$ 无界，且$\lim\limits_{n \to \infty} x_n=\infty$不成立。

Pf:

首先，我们有对于任意正整数 $k$，$x_{2k} = 2k$, $x_{2k-1}=\frac{1}{2k-1}$

(1) 下面证明 $\{x_n\}$ 无界：

考虑$\{x_n\}$的子列 $y_k=x_{2k}$。下面证明$\{y_n\}$无界。对于任意给定的 $M > 0$，存在 $k_0 = \lceil M/2 \rceil$，使得当 $k \geq k_0$ 时，$y_k=x_{2k} = 2k \geq 2k_0 \geq M$。因此，$\{y_n\}$ 无界。

因为$\{y_n\}$无界，因此 $\{x_n\}$ 无界。

(2) 证明 $\lim\limits_{n \to \infty} x_n=\infty$ 不成立：

考虑两个子列$y_k=x_{2k}$与$z_k=x_{2k-1}$，我们有 $\lim\limits_{k \to \infty} y_k = \lim\limits_{k \to \infty} x_{2k}=\lim\limits_{k \to \infty} 2k=+\infty$；又有 $\lim\limits_{k \to \infty} z_k=\lim\limits_{k \to \infty}x_{2k-1} =\lim\limits_{k \to \infty} \frac{1}{2k-1}= 0$。所以$\lim\limits_{n \to \infty} x_n=\infty$ 不成立。

Qed.

注意事项：
开头定义数列x时，用Define或Fix都可以。
本例中，有两个证明目标，这需要在最初的Show节点中用列表写出，然后分别证明子目标。
用Define节点定义子列y：[Define: "y" as "$\{x_n\}$的子列$y_k=x_{2k}$"]

结构：

[Define: {x} as {"$\{x_n\}$ 是实数上的数列"; "$\forall n \geq 1, x_n = n^{(-1)^n}$"}]
[Show: {"$\{x_n\}$ 无界"; "$\lim\limits_{n \to \infty} x_n=\infty$ 不成立"}]
[Have: "对于任意正整数 $k$，$x_{2k} = 2k$, $x_{2k-1}=\frac{1}{2k-1}$"]
[Show: "$\{x_n\}$ 无界"]
[Define: "y" as "$\{x_n\}$的子列$y_k=x_{2k}$"]
[Show: "$\{y_n\}$无界"]
[Fix: {M} such that $M>0$]
[Have: "存在 $k_0 = \lceil M/2 \rceil$，使得当 $k \geq k_0$ 时，$y_k=x_{2k} = 2k \geq 2k_0 \geq M$"]
[Have: "$\{y_n\}$ 无界"]
[Have: "$\{x_n\}$ 无界" by "$\{y_n\}$无界"]
[Show: "$\lim\limits_{n \to \infty} x_n=\infty$ 不成立"]
[Define: "y,z" as "$x$的两个子列$y_k=x_{2k}$与$z_k=x_{2k-1}$"]
[Have: "$\lim\limits_{k \to \infty} y_k = \lim\limits_{k \to \infty} x_{2k}=\lim\limits_{k \to \infty} 2k=+\infty$"]
[Have: "$\lim\limits_{k \to \infty} z_k=\lim\limits_{k \to \infty}x_{2k-1} =\lim\limits_{k \to \infty} \frac{1}{2k-1}= 0$"]
[Have: "$\lim\limits_{n \to \infty} x_n=\infty$ 不成立"]

### 样例 9

输入：

**Theorem 4** (Schröder-Bernstein's Theorem). If $f: A \to B$ and $g: B \to A$ are both injections, then there is a bijection from $A$ into $B$.

**Proof.**

Suppose $f: A \to B, g: B \to A$ are injections. Let’s construct the bijection $h$ from $A$ into $B$.

$$
C_0 = \{ a \in A \mid \forall b \in B. \, g(b) \neq a \}
$$

$$
D_0 = \{ f(a) \mid a \in C_0 \}
$$

$$
C_1 = \{ a \in A \setminus C_0 \mid \forall b \in B \setminus D_0. \, g(b) \neq a \}. \, \text{We can prove that} \, C_1 = \{ g(b) \mid b \in D_0 \} \, \text{also}.
$$

$$
D_1 = \{ f(a) \mid a \in C_1 \}
$$

So that we can define

$$
C_{n+1} = \{ a \in A \setminus \bigcup_{i=0}^{n} C_i \mid \forall b \in B \setminus \bigcup_{i=0}^{n} D_i. \, g(b) \neq a \}
$$

$$
D_{n+1} = \{ f(a) \mid a \in C_{n+1} \}
$$

And similarly, we can prove that $C_{n+1} = \{ g(b) \mid b \in D_n \}$.

In the end, we can define

$$
h(a) := \begin{cases} 
f(a), & \text{if} \, a \in \bigcup_{i=0}^{\infty} C_i \\
b, \, \text{such that} \, g(b) = a, & \text{if} \, a \in A \setminus \bigcup_{i=0}^{\infty} C_i 
\end{cases}
$$

Obviously, the $f$ part is a bijection from $C_n$ into $D_n$.

So we just need to prove that the $g$ part is a bijection from $D := B \setminus \bigcup_{i=0}^{\infty} D_i$ into $C := A \setminus \bigcup_{i=0}^{\infty} C_i$.

Thus, it is suffice to prove: (1) $\forall d \in D. \, \exists c \in C. \, g(d) = c$ and (2) $\forall c \in C. \, \exists d \in D. \, g(d) = c$.

- $\forall d \in D. \exists c \in C. g(d) = c$.

  As $g$ is an injection from $B$ into $A$, $\exists c \in A, g(d) = c$.

  Let prove $c \notin C_n$.

  Suppose $c \in C_n$.

  - $n = 0$, Obviously contradiction.
  - $n = m + 1$, $c \in C_{m+1} \Rightarrow d \in D_m$, contradiction.

  Therefore, $c \in C$.

- $\forall c \in C. \exists d \in D. g(d) = c$.

  $\exists d \in B. g(d) = c$. Otherwise, $c \in C_0$, contradiction.

  Let’s prove $d \notin D_n$.

  Suppose $d \in D_n$, so that $c \in C_{n+1}$, contradiction.

  Therefore, $d \in D$.

Qed.

注意事项：
尽管证明目标中做了$f,g$是单射的假设，但是证明开头自然语言又说了一遍。对于这样的情况，我们按照字面翻译，不要省略。
Let’s construct...是一个Hint
注意本例中SufficeToProve的使用

结构：

[Fix: {f,g} such that {"$f: A \to B$ injection"; "$g: B \to A$ injection"}]
[Show: "There exists a bijection from $A$ to $B$"]
[Fix: {f,g} such that {"$f: A \to B$ injection"; "$g: B \to A$ injection"}]
[Hint: "Let’s construct the bijection $h$ from $A$ into $B$."]
[Define: "$C_0$" as "C_0 = \{ a \in A \mid \forall b \in B.\, g(b) \neq a \}$"]
[Define: "$D_0$" as "$D_0 = \{ f(a) \mid a \in C_0 \}$"]
[Define: "$C_1$" as "$C_1 = \{ a \in A \setminus C_0 \mid \forall b \in B \setminus D_0.\, g(b) \neq a \}$"]
[Have: "$C_1 = \{ g(b) \mid b \in D_0 \}$" by "We can prove"]
[Define: "$D_1$" as "$D_1 = \{ f(a) \mid a \in C_1 \}$"]
[Define: "$C_{n+1}$" as "$C_{n+1} = \{ a \in A \setminus \bigcup_{i=0}^{n} C_i \mid \forall b \in B \setminus \bigcup_{i=0}^{n} D_i.\, g(b) \neq a \}$"]
[Define: "$D_{n+1}$" as "$D_{n+1} = \{ f(a) \mid a \in C_{n+1} \}$"]
[Have: "$C_{n+1} = \{g(b) \mid b \in D_n \}$" by "Similarly, we can prove that"]
[Define: "$h(a)$" as "$h(a) := \begin{cases} f(a), & \text{if} \, a \in \bigcup_{i=0}^{\infty} C_i \\ b, \, \text{such that}\, g(b) = a, & \text{if} \, a \in A \setminus \bigcup_{i=0}^{\infty} C_i \end{cases}$"]
[Have: "The $f$ part is a bijection from $C_n$ into $D_n$."]
[SufficeToProve: "the $g$ part is a bijection from $D := B \setminus \bigcup_{i=0}^{\infty} D_i$ into $C := A \setminus \bigcup_{i=0}^{\infty} C_i$."]
[SufficeToProve: {"$\forall d \in D.\, \exists c \in C.\, g(d) = c$; $\forall c \in C.\, \exists d \in D.\, g(d) = c$."}]
[Show: "$\forall d \in D.\, \exists c \in C.\, g(d) = c$"]
[Have: "$\exists c \in A, g(d) = c$" by "$g$ is an injection from $B$ into $A$"]
[Show: "$c \notin C_n$"]
[Assume: "$c \in C_n$"]
[Assume: "$n = 0$"]
[Have: "contradiction"]
[Assume: "$n = m+1$"]
[Have: "$c \in C_{m+1} \Rightarrow d \in D_m$"]
[Have: "contradiction"]
[Have: "$c \in C$"]
[Show: "$\forall c \in C.\, \exists d \in D.\, g(d) = c$"]
[Have: "$\exists d \in B. g(d) = c$" by "Otherwise, $c \in C_0$, contradiction."]
[Show: "$d \notin D_n$"]
[Assume: "$d \notin D_n$"]
[Have: "$c \in C_{n+1}$"]
[Have: "contradiction"]
[Have: "$d \in D$"]

### 样例 10

输入：

求$\displaystyle\int \frac{4x^3 - 13x^2 + 3x + 8}{(x+1)(x-2)(x-1)^2} \, dx$

先将被积函数分解成简单分式之和。设：
$\displaystyle\frac{4x^3 - 13x^2 + 3x + 8}{(x+1)(x-2)(x-1)^2} = \frac{A}{x+1} + \frac{B}{x-2} + \frac{C}{x-1} + \frac{D}{(x-1)^2}.$

将右边通分后，两边的分子应该相等，所以：
$4x^3 - 13x^2 + 3x + 8 = A(x-2)(x-1)^2 + B(x+1)(x-1)^2 +$
$C(x+1)(x-2)(x-1) + D(x+1)(x-2).$
令 $x = -1$，得到 $A = 1$；
令 $x = 2$，得到 $B = -2$；
令 $x = 1$，得到 $D = -1$；
两边求导后再令 $x = 1$，得到 $C = 5$，
于是：
$\displaystyle\int \frac{4x^3 - 13x^2 + 3x + 8}{(x+1)(x-2)(x-1)^2} \, dx = \int \left[ \frac{1}{x+1} - \frac{2}{x-2} + \frac{5}{x-1} - \frac{1}{(x-1)^2} \right] \, dx$
计算得：
$$
= \ln |(x+1)(x-1)^5| - \ln |(x-2)^2| + \frac{1}{x-1} + C.
$$

注意事项：
本例涉及待定系数法，你需要把引入的系数A,B,C,D用Fix节点提取出来。

结构：

[Find: "\displaystyle\int \frac{4x^3 - 13x^2 + 3x + 8}{(x+1)(x-2)(x-1)^2} \, dx"]
[Hint: "先将被积函数分解成简单分式之和"]
[Fix: {A,B,C,D} such that "$\frac{4x^3 - 13x^2 + 3x + 8}{(x+1)(x-2)(x-1)^2} = \frac{A}{x+1} + \frac{B}{x-2} + \frac{C}{x-1} + \frac{D}{(x-1)^2}$"]
[Have: "$4x^3 - 13x^2 + 3x + 8 = A(x-2)(x-1)^2 + B(x+1)(x-1)^2 + C(x+1)(x-2)(x-1) + D(x+1)(x-2)$" by "将右边通分后，两边的分子应该相等"]
[Have: "$A = 1$" by "令$x=-1$"]
[Have: "$B = -2$" by "令$x=2$"]
[Have: "$D = -1$" by "令$x=1$"]
[Have: "$C = 5$" by "两边求导后再令$x=1$"]
[Have: "$\displaystyle\int \frac{4x^3 - 13x^2 + 3x + 8}{(x+1)(x-2)(x-1)^2} \, dx = \int \left[ \frac{1}{x+1} - \frac{2}{x-2} + \frac{5}{x-1} - \frac{1}{(x-1)^2} \right] \, dx$"]
[Have: "$\displaystyle\int \frac{4x^3 - 13x^2 + 3x + 8}{(x+1)(x-2)(x-1)^2} \, dx = = \ln |(x+1)(x-1)^5| - \ln |(x-2)^2| + \frac{1}{x-1} + C$"]

### 样例 11

输入：

求 $\int x \ln x \, dx$.

解：

设 $u = \ln x$, $dv = x \, dx$, 则 $\int x \ln x \, dx = \int \ln x \, d \frac{x^2}{2} = \frac{x^2}{2} \ln x - \int \frac{x^2}{2} d(\ln x)$
$= \frac{x^2}{2} \ln x - \frac{1}{2} \int x \, dx = \frac{x^2}{2} \ln x - \frac{x^2}{4} + C$

结构：

[Find: "$\int x \ln x \, dx$" such that []]
[Define: "u" as "u = \ln x"]
[Define: "v" as "dv = x \, dx"]
[Have: "\int x \ln x \, dx = \int \ln x \, d \frac{x^2}{2} = \frac{x^2}{2} \ln x - \int \frac{x^2}{2} d(\ln x)= \frac{x^2}{2} \ln x - \frac{1}{2} \int x \, dx = \frac{x^2}{2} \ln x - \frac{x^2}{4} + C"]

### 样例 12

输入：

**例2** 计算反常积分 $\int_0^{+\infty} te^{-pt} dt$，其中 $p$ 是常数，且 $p > 0$。

**解**

$\int_0^{+\infty} te^{-pt} dt = \left[ \int te^{-pt} dt \right]_0^{+\infty} = \left[ -\frac{1}{p} \int t d(e^{-pt}) \right]_0^{+\infty}$

$= \left[ -\frac{t}{p} e^{-pt} + \frac{1}{p} \int e^{-pt} dt \right]_0^{+\infty}$

$= \left[ -\frac{t}{p} e^{-pt} \right]_0^{+\infty} - \left[ \frac{1}{p^2} e^{-pt} \right]_0^{+\infty}$

$= -\frac{1}{p} \lim_{t \to +\infty} te^{-pt} - 0 - \frac{1}{p^2} (0 - 1) = \frac{1}{p^2}$

注意，上式中的极限 $\lim_{t \to +\infty} te^{-pt}$ 是未定式，可用洛必达法则确定。

结构：

[Fix: {p} such that "$p > 0$"]
[Find: "反常积分$\int_0^{+\infty} te^{-pt} dt$"]
[Have: "$\int_0^{+\infty} te^{-pt} dt = \left[ \int te^{-pt} dt \right]_0^{+\infty} = \left[ -\frac{1}{p} \int t d(e^{-pt}) \right]_0^{+\infty}$= \left[ -\frac{t}{p} e^{-pt} + \frac{1}{p} \int e^{-pt} dt \right]_0^{+\infty}= \left[ -\frac{t}{p} e^{-pt} \right]_0^{+\infty} - \left[ \frac{1}{p^2} e^{-pt} \right]_0^{+\infty}= -\frac{1}{p} \lim_{t \to +\infty} te^{-pt} - 0 - \frac{1}{p^2} (0 - 1) = \frac{1}{p^2}"]
[Hint: "注意，上式中的极限 $\lim_{t \to +\infty} te^{-pt}$ 是未定式，可用洛必达法则确定。"]

### 样例 13

输入：

**例1** 求微分方程$\frac{dy}{dx} = 2xy$的通解。

**解** 方程是可分离变量的，分离变量后得$\frac{dy}{y} = 2x dx,$

两端积分$\int \frac{dy}{y} = \int 2x dx,$

得$\ln |y| = x^2 + C_1,$

从而$y = \pm e^{x^2 + C_1} = \pm e^{C_1} e^{x^2}.$

因 $\pm e^{C_1}$ 是任意非零常数，又 $y=0$ 也是方程的解，故得通解$y = C e^{x^2}.$

结构：

[Find: "y" such that "y是微分方程$\frac{dy}{dx} = 2xy$的通解"]
[Hint: "方程是可分离变量的"]
[Have: "$\frac{dy}{y} = 2x dx$" by "分离变量"]
[Have: "\int \frac{dy}{y} = \int 2x dx" by "两端积分"]
[Have: "$\ln |y| = x^2 + C_1$"]
[Have: "$y = \pm e^{x^2 + C_1} = \pm e^{C_1} e^{x^2}.$"]
[Have: "$\pm e^{C_1}$ 是任意非零常数"]
[Have: "$y=0$ 也是原方程的解"]
[Have: "通解$y = C e^{x^2}$" by "$\pm e^{C_1} 是任意非零常数"; "$y=0$ 也是原方程的解"]

### 样例 14

输入：

对于正实数数列$\{x_n\}$和任意正整数$n$，请证明：

$$
\prod\limits_{i=1}^{n}\left( {1 + {x}_{i}}\right)\geq  1 + \sum\limits_{i=1}^{n}{x}_{i},
$$

Pf:

我们使用数学归纳法证明。

归纳基础：当 $n = 1$ 时，$1+x_1=1+x_1$，成立.

归纳步骤：设对于任意的正整数$k$，成立$\prod\limits_{i=1}^{k}\left( {1 + {x}_{i}}\right)\geq  1 + \sum\limits_{i=1}^{k}{x}_{i}$。下面证明$\prod\limits_{i=1}^{k+1}\left( {1 + {x}_{i}}\right)\geq  1 + \sum\limits_{i=1}^{k+1}{x}_{i}$。由于 $\forall 1\leq i \leq n,{x}_{i}>0$,所以, $1 + {x}_{i} > 0$。 因而,有

$$
\prod\limits_{i=1}^{k+1}\left( {1 + {x}_{i}}\right)\geq   (1 + \sum\limits_{i=1}^{k}{x}_{i})(1+x_{k+1})
$$

$$
=(1 + \sum\limits_{i=1}^{k+1}{x}_{i})+\sum\limits_{i=1}^{k}(x_i x_{k+1})
$$

由于 $\forall 1\leq i,j \leq n,{x}_{i}{x}_{j} \geq  0$。所以,

$$
\prod\limits_{i=1}^{k+1}\left( {1 + {x}_{i}}\right)\geq 1 + \sum\limits_{i=1}^{k+1}{x}_{i}
$$

归纳证明结束。

于是,对于任何正整数 $n$ ,有

所以

$$
\prod\limits_{i=1}^{n}\left( {1 + {x}_{i}}\right)\geq  1 + \sum\limits_{i=1}^{n}{x}_{i},
$$

Qed.

结构：

[Fix：{x,n} such that "x是正实数数列"; "n是正整数"]
[Show: "$\prod\limits_{i=1}^{n}\left( {1 + {x}_{i}}\right)\geq  1 + \sum\limits_{i=1}^{n}{x}_{i}$"]
[Hint: "我们使用数学归纳法证明。"]
[Hint: "归纳基础"]
[Have: "当 $n = 1$ 时，$1+x_1=1+x_1$，成立."]
[Hint: "归纳步骤"]
[Fix: {k} such that {"k是正整数"; "$\prod\limits_{i=1}^{k}\left( {1 + {x}_{i}}\right)\geq  1 + \sum\limits_{i=1}^{k}{x}_{i}$"}]
[Show: "$\prod\limits_{i=1}^{k+1}\left( {1 + {x}_{i}}\right)\geq  1 + \sum\limits_{i=1}^{k+1}{x}_{i}$"]
[Have: "$\forall 1\leq i \leq n,1 + {x}_{i} > 0$" by "$\forall 1\leq i \leq n,{x}_{i}>0$"]
[Have: "$\prod\limits_{i=1}^{k+1}\left( {1 + {x}_{i}}\right)\geq   (1 + \sum\limits_{i=1}^{k}{x}_{i})(1+x_{k+1})=(1 + \sum\limits_{i=1}^{k+1}{x}_{i})+\sum\limits_{i=1}^{k}(x_i x_{k+1})$"]
[Have: "$\prod\limits_{i=1}^{k+1}\left( {1 + {x}_{i}}\right)\geq 1 + \sum\limits_{i=1}^{k+1}{x}_{i}$" by "$\forall 1\leq i,j \leq n,{x}_{i}{x}_{j} \geq  0$"]
[Hint: "归纳证明结束。"]
[Have: "对于任何正整数 $n$ ,有 $\prod\limits_{i=1}^{n}\left( {1 + {x}_{i}}\right)\geq  1 + \sum\limits_{i=1}^{n}{x}_{i}$"]

### 样例 15

输入：

设 $\{x_n\}$是实数上的数列，满足$\forall n\geq 1,{x}_{n} = \frac{n}{n + 1}$。请证明：$\mathop{\lim }\limits_{{n \rightarrow  \infty }}{x}_{n} = 1$。

Pf: 

我们有 $\forall n\geq 1, \left| {{x}_{n} - 1}\right|  = \frac{1}{n + 1}$.

对于任意的 $\varepsilon  > 0$ , 我们可以取$N  = \left\lbrack  \frac{1}{\varepsilon }\right\rbrack$。我们证明$\forall n>N,|x_n-1|<\varepsilon$。只需证$\frac{1}{n + 1} < \varepsilon$。只需证 $n > \frac{1}{\varepsilon } - 1$。我们有$n>\left\lbrack  \frac{1}{\varepsilon }\right\rbrack$，得证。

所以, $\mathop{\lim }\limits_{{n \rightarrow  \infty }}{x}_{n} = 1$ .

Qed.

结构：

[Define: {x} as {"$\{x_n\}$是实数上的数列"; "满足$\forall n\geq 1,{x}_{n} = \frac{n}{n + 1}$"}]
[Show: "$\mathop{\lim }\limits_{{n \rightarrow  \infty }}{x}_{n} = 1$"]
[Have: "$\forall n\geq 1, \left| {{x}_{n} - 1}\right|  = \frac{1}{n + 1}$"]
[Fix: {ɛ} such that "$\varepsilon  > 0$"]
[Define: {N} as "$N  = \left\lbrack  \frac{1}{\varepsilon }\right\rbrack$"]
[Show: "$\forall n>N,|x_n-1|<\varepsilon$"]
[SufficeToProve: "$\frac{1}{n + 1} < \varepsilon$"]
[SufficeToProve: "$n > \frac{1}{\varepsilon } - 1$"]
[Have: "$n>\left\lbrack  \frac{1}{\varepsilon }\right\rbrack$"]
[Hint: "得证"]
[Have: "$\mathop{\lim }\limits_{{n \rightarrow  \infty }}{x}_{n} = 1$"]

### 样例 16

输入：

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

结构：

[Fix: {f} such that "$f(x)$ 在 $[0,1]$ 上连续"]
[Show: "$\lim_{h \to 0^+} \int_0^1 \frac{h}{h^2 + x^2} f(x) dx = \frac{\pi}{2} f(0)$"]
[Hint: "拟合法"]
[Have: "$\frac{\pi}{2} f(0) = \lim_{h \to 0} \int_0^1 \frac{h}{h^2 + x^2} f(0) dx$" by "$\lim_{h \to 0} \int_0^1 \frac{h}{h^2 + x^2} dx = \frac{\pi}{2}$"]
[Have: "$\lim_{h \to 0} \int_0^1 \frac{h}{h^2 + x^2} [f(x) - f(0)] dx = 0 \implies \lim_{h \to 0^+} \int_0^1 \frac{h}{h^2 + x^2} f(x) dx = \frac{\pi}{2} f(0)$"]
[Show: "$\lim_{h \to 0} \int_0^1 \frac{h}{h^2 + x^2} [f(x) - f(0)] dx = 0$"]
[Have: "$\int_0^1 \frac{h}{h^2 + x^2} [f(x) - f(0)] dx = \left( \int_0^\delta + \int_\delta^1 \right) \frac{h}{h^2 + x^2} [f(x) - f(0)] dx$"]
[Have: "$\forall \varepsilon > 0$, 当 $\delta > 0$ 充分小时，在 $[0, \delta]$ 上，$|f(x) - f(0)| < \frac{\varepsilon}{\pi}$" by ""$f(x)$ 在 $x=0$ 处连续""]
[Have: "$\left| \int_0^\delta \frac{h}{h^2 + x^2} [f(x) - f(0)] dx \right| \\ \leq \int_0^\delta \frac{h|f(x)-f(0)|}{h^2 + x^2} \cdot dx \leq \frac{\varepsilon}{\pi} \cdot \int_{0}^{\delta}\frac{h}{h^2+x^2}dx \\ = \frac{\varepsilon}{\pi} \arctan \frac{\delta}{h} \leq \frac{\varepsilon}{\pi} \cdot \frac{\pi}{2} = \frac{\varepsilon}{2}.$"]
[Hint: "再将 $\delta$ 固定"]
[Have: "$\left| \int_\delta^1 \frac{h}{h^2 + x^2} [f(x) - f(0)] dx \right| \leq h \int_\delta^1 \frac{1}{x^2} |f(x) - f(0)| dx \equiv h \cdot M_0$"]
[Have: "当 $0 < h < \frac{\epsilon}{2M_0}$ 时，$\left| \int_0^1 \frac{h}{h^2 + x^2} [f(x) - f(0)] dx \right| < \epsilon$"]

### 样例 17

输入：

【41】设 ${x}_{n} = \frac{n}{n + 1}\left( {n = 1,2,\cdots }\right)$ . 证明: $\mathop{\lim }\limits_{{n \rightarrow  \infty }}{x}_{n} = 1$

证 $\left| {{x}_{n} - 1}\right|  = \frac{1}{n + 1}$ . 任给 $\varepsilon  > 0$ ,要 $\left| {{x}_{n} - 1}\right|  < \varepsilon$ ,只要 $\frac{1}{n + 1} < \varepsilon$ . 即只要 $n > \frac{1}{\varepsilon } - 1$ .

可取 $N = N\left( \varepsilon \right)  = \left\lbrack  \frac{1}{\varepsilon }\right\rbrack$ ,则当 $n > N$ 时, $\left| {{x}_{n} - 1}\right|  < \varepsilon$ ,所以, $\mathop{\lim }\limits_{{n \rightarrow  \infty }}{x}_{n} = 1$ .

结构：

[Define: {x} as "{x}_{n} = \frac{n}{n + 1}\left( {n = 1,2,\cdots }\right)"]
[Show: "$\mathop{\lim }\limits_{{n \rightarrow  \infty }}{x}_{n} = 1$"]
[Have: "$|x_n - 1| = \frac{1}{n + 1}$"]
[Fix: {\varepsilon} such that "$\varepsilon  > 0$"]
[Have: "$\frac{1}{n+1} < \varepsilon \implies |x_n - 1| < \varepsilon$"]
[Have: "$n > \frac{1}{\varepsilon} - 1 \implies \frac{1}{n+1} < \varepsilon$"]
[Define: {N} as "$N = N(\varepsilon) = \left\lbrack  \frac{1}{\varepsilon }\right\rbrack$"]
[Have: "当$n > N$时，$|x_n - 1| < \varepsilon$"]
[Have: "$\lim_{n\to \infty} x_n = 1$"]

### 样例 18

输入：

【90】证明: 若单调数列的某一子数列收敛, 则此单调数列本身是收敛的.

证 不失一般性,假设数列 $\left\{  {x}_{n}\right\}$ 单调增加,其一子数列 $\left\{  {x}_{{p}_{n}}\right\}$ 收敛于 $a$ . 则对于任给的 $\varepsilon  > 0$ ,存在正整数 $N$ ,使当 $k > N$ 时, $\left| {{x}_{{p}_{k}} - a}\right|  < \varepsilon$ ,令 ${N}^{\prime } = {p}_{N + 1}$ . 设 $n > {N}^{\prime }$ ,由于 ${p}_{1} < {p}_{2} < {p}_{3} < \cdots  \rightarrow   + \infty$ ,故必有 ${p}_{k}\left( {k > N}\right)$ 使 ${p}_{k} \leq  n < {p}_{k + 1}$ . 由上知

$$
\left| {{x}_{{p}_{k}} - a}\right|  < \varepsilon ,\;\left| {{x}_{{p}_{k + 1}} - a}\right|  < \varepsilon .
$$

而 ${x}_{{p}_{k}} \leq  {x}_{n} \leq  {x}_{{p}_{k + 1}}$ (因 ${x}_{n}$ 递增),故必 $\left| {{x}_{n} - a}\right|  < \varepsilon$ . 由此可知 $\mathop{\lim }\limits_{{n \rightarrow  \infty }}{x}_{n} = a$ ,即 $\left\{  {x}_{n}\right\}$ 是收敛的.

结构：

[Show: "若单调数列的某一子数列收敛, 则此单调数列本身是收敛的"]  
[Fix: {x,a} such that "数列 $\left\{  {x}_{n}\right\}$ 单调增加,其一子数列 $\left\{  {x}_{{p}_{n}}\right\}$ 收敛于 $a$"]
[Fix: {ɛ} such that "$\varepsilon > 0$"]
[Have: "存在正整数 $N$, 使当 $k > N$ 时, $\left| x_{p_k} - a \right| < \varepsilon$"]
[Define: {N'} as "$N' = p_{N+1}$"]
[Fix: {n} such that "$n > N'$"]
[Have: "有 $p_k (k > N)$ 使 $p_k \leq n < p_{k+1}$" by "$p_1 < p_2 < p_3 < \cdots \rightarrow +\infty$"]
[Have: {"$\left| x_{p_k} - a \right| < \varepsilon$"; "$\left| x_{p_{k+1}} - a \right| < \varepsilon$"} by "由上知"]
[Have: "$x_{p_k} \leq x_n \leq x_{p_{k+1}}$" by "$x_n$ 递增"]
[Have: "$\left| x_n - a \right| < \varepsilon$"]
[Have: {"$\lim_{n \to \infty} x_n = a$"; "$\left\{x_n\right\}$ 是收敛的"}]


### 样例 19

输入：

下面我们证明，如果$H\preceq G,K\preceq G$，那么$HK\preceq G\iff HK=KH$。左推右，因为$HK$是子群，根据等价定义得到$(HK)^{-1}=HK$，而$(HK)^{-1}=K^{-1}H^{-1}$，而$H,K$都是子群，因此等于$KH$；右推左，$(HK)^{-1}=K^{-1}H^{-1}=KH=HK$，同时$(HK)(HK)=H(KH)K$$=H(HK)K=(HH)(KK)=HK$，因此$HK\preceq G$。

注意事项：

在提取该段证明的结构时，需要你把[Show: "左推右"]具体展开为[Show: "$HK\preceq G\implies HK=KH$"]

输出：

[Assume: {"$H\preceq G$"; "$K\preceq G$"}]
[Show: "$HK\preceq G\iff HK=KH$"]
[Show: "$HK\preceq G\implies HK=KH$"]
[Show: "$HK\preceq G$"]
[Have: "$(HK)^{-1}=HK$" by {"等价定义"; "$HK$是子群"}]
[Have: "$(HK)^{-1}=K^{-1}H^{-1}$"]
[Have: "$H,K$都是子群"]
[Have: "$(HK)^{-1}=K^{-1}H^{-1}=KH$"]
[Have: "$HK=KH$"]
[Show: "$HK=KH \implies HK\preceq G$"]
[Have: "$(HK)^{-1}=K^{-1}H^{-1}=KH=HK$"]
[Have: "$(HK)(HK)=H(KH)K$$=H(HK)K=(HH)(KK)=HK$"]
[Have: "$HK\preceq G$"]

### 样例 19

输入：

证明: 对于所有实数 $x$ 和 $y$ 都满足方程

$$
f\left( {x + y}\right)  = f\left( x\right)  + f\left( y\right)  \tag{1}
$$

的唯一的连续函数 $f\left( x\right) \left( {-\infty  < x <  + \infty }\right)$ 是线性齐次函数:

$$
f\left( x\right)  = {ax},
$$

式中 $a = f\left( 1\right)$ 是任意的常数.

证 先证: 若 $f\left( x\right)$ 满足 (1),则对任何有理数 $c$ ,必有

$$
f\left( {cx}\right)  = {cf}\left( x\right) \;\left( {-\infty  < x <  + \infty }\right) .
$$

事实上,当 $m$ 与 $n$ 为正整数时,有

$$
f\left( {mx}\right)  = f\left( {x + \left( {m - 1}\right) x}\right)  = f\left( x\right)  + f\left( {\left( {m - 1}\right) x}\right)  = f\left( x\right)  + f\left( x\right)  + f\left( {\left( {m - 2}\right) x}\right)  = \cdots
$$

$$
= f\left( x\right)  + f\left( x\right)  + \cdots  + f\left( x\right)  = {mf}\left( x\right) \text{;}
$$

$$
f\left( x\right)  = f\left( {n \cdot  \frac{x}{n}}\right)  = {nf}\left( \frac{x}{n}\right) ,\;\text{ 故 }f\left( \frac{x}{n}\right)  = \frac{1}{n}f\left( x\right) .
$$

于是,

$$
f\left( {\frac{m}{n}x}\right)  = {mf}\left( \frac{x}{n}\right)  = \frac{m}{n}f\left( x\right) .
$$

又在 (1) 中令 $y = 0$ ,得 $f\left( x\right)  = f\left( x\right)  + f\left( 0\right)$ ,故 $f\left( 0\right)  = 0$ ; 又在 (1) 中令 $y =  - x$ ,并注意到已证的结果 $f\left( 0\right)  = 0$ , 得 $f\left( {-x}\right)  =  - f\left( x\right)$ . 于是,

$$
f\left( {-\frac{m}{n}x}\right)  =  - f\left( {\frac{m}{n}x}\right)  =  - \frac{m}{n}f\left( x\right) .
$$

故对任何有理数 $c$ ,有 $f\left( {cx}\right)  = {cf}\left( x\right) \left( {-\infty  < x <  + \infty }\right)$ . 下面,我们利用 $f\left( x\right)$ 的连续性证明对任何无理数 $c$ , 此式也成立. 事实上,设 $c$ 为无理数. 取一串有理数 ${c}_{n}$ ,使 ${c}_{n} \rightarrow  c\left( {n \rightarrow  \infty }\right)$ . 于是,

$$
f\left( {{c}_{n}x}\right)  = {c}_{n}f\left( x\right) \;\left( {n = 1,2,\cdots }\right) ,
$$

在此式两端令 $n \rightarrow  \infty$ 取极限,并注意到函数 $f$ 在点 ${cx}$ 连续,即得 $f\left( {cx}\right)  = {cf}\left( x\right)$ . 于是,对任何实数 $x$ 和 $c$ , 有 $f\left( {cx}\right)  = {cf}\left( x\right)$ . 由此可知,对任何实数 $x$ ,有

$$
f\left( x\right)  = f\left( {x \cdot  1}\right)  = {xf}\left( 1\right)  = {ax},
$$

其中 $a = f\left( 1\right)$ . 证毕.

结构：

[Fix: {a,f} such that "$a \in \R$"; "f是连续函数"; "对于所有实数 $x$ 和 $y$ 都满足方程$f\left( {x + y}\right)  = f\left( x\right)  + f\left( y\right)  \tag{1}$"; "a=f(1)"]
[Show: {"f唯一"; "f是线性齐次函数f(x)=ax"}]
[Show: "若 $f(x)$ 满足 $f\left( {x + y}\right)  = f\left( x\right)  + f\left( y\right)$,则对任何有理数 $c$ ,必有 $f(cx) = cf(x) \;(-\infty < x < +\infty)$"]
[Fix: {n,m} such that "$m$ 与 $n$ 为正整数"]
[Have: "$f\left( {mx}\right)  = f\left( {x + \left( {m - 1}\right) x}\right)  = f\left( x\right)  + f\left( {\left( {m - 1}\right) x}\right)  = f\left( x\right)  + f\left( x\right)  + f\left( {\left( {m - 2}\right) x}\right)  = \cdots = = f\left( x\right)  + f\left( x\right)  + \cdots  + f\left( x\right)  = {mf}\left( x\right) \text{;}f\left( x\right)  = f\left( {n \cdot  \frac{x}{n}}\right)  = {nf}\left( \frac{x}{n}\right)$"]
[Have: "$f(\frac{x}{n}) = \frac{1}{n} f(x)$"]
[Have: "$f(\frac{m}{n}x) = mf(\frac{x}{n}) = \frac{m}{n} f(x)$"]
[Have: "$f(x) = f(x) + f(0)$" by "在 (1) 中令 $y = 0$"]
[Have: "$f(0) = 0$"]
[Have: "$f(-x) = -f(x)$" by "$f(0)=0$"; "在 (1) 中令 $y = -x$"]
[Have: "$f(-\frac{m}{n}x) = -f(\frac{m}{n}x) = -\frac{m}{n} f(x)$"]
[Have: "对任何有理数 $c$ ,有 $f(cx) = cf(x)$"]
[Show: "对任何无理数 $c$ ,必有 $f(cx) = cf(x) \;(-\infty < x < +\infty)$"]
[Hint: "我们利用 $f(x)$ 的连续性"]
[Fix: {c} such that "$c$ 为无理数"]
[Fix: {c_n} such that "${c}_{n} \rightarrow  c\left( {n \rightarrow  \infty }\right)$"]
[Have: "$f(c_n x) = c_n f(x)\;(n=1,2,\cdots)$"]
[Have: "$f(cx) = c f(x)$" by "在此式两端令 $n \to \infty$ 取极限"; "$f$ 在点 $cx$ 连续"]
[Have: "对任何实数 $x$ 和 $c$, 有 $f(cx) = c f(x)$"]
[Have: "对任何实数 $x$, 有 $f(x) = f(x \cdot 1) = x f(1) = ax$, 其中 $a = f(1)$"]

### 样例 20

输入：

## Goal

Let $\{x_n\}$ and $\{y_n\}$ be numerical sequences. Prove that if $\lim_{n \to \infty} x_n = A$ and $\lim_{n \to \infty} y_n = B$, then $\lim_{n \to \infty} (x_n + y_n) = A + B$.

## Proof

Denote $|A - x_n| = \Delta(x_n)$, $|B - y_n| = \Delta(y_n)$. Then we have

$$
|(A + B) - (x_n + y_n)| \leq \Delta(x_n) + \Delta(y_n).
$$

Suppose $\varepsilon > 0$ is given. Since $\lim_{n \to \infty} x_n = A$, there exists $N'$ such that $\Delta(x_n) < \varepsilon / 2$ for all $n > N'$. Similarly, since $\lim_{n \to \infty} y_n = B$, there exists $N''$ such that $\Delta(y_n) < \varepsilon / 2$ for all $n > N''$. Then for $n > \max\{N', N''\}$ we shall have

$$
|(A + B) - (x_n + y_n)| < \varepsilon,
$$

which, by definition of limit, gives us $\lim_{n \to \infty} (x_n + y_n) = A + B$.

$Qed.$

注意事项：
注意，并不是Goal标题下的都要识别为Show。这里，Let $\{x_n\}$ and $\{y_n\}$ be numerical sequences这句话就应该被识别为Fix，if $\lim_{n \to \infty} x_n = A$ and $\lim_{n \to \infty} y_n = B$也应该被识别为fix，then $\lim_{n \to \infty} (x_n + y_n) = A + B$才应该被识别为Show。

结构：

[Fix: {x,y} such that "$\{x_n\}$ and $\{y_n\}$ be numerical sequences"; ]
[Fix: {A,B} such that "$\lim_{n \to \infty} x_n = A$ and $\lim_{n \to \infty} y_n = B$"]
[Show: "$\lim_{n \to \infty} (x_n + y_n) = A + B$"]
[Define: "\Delta(x_n)" as " $|A - x_n| = \Delta(x_n)$"]
[Define: "\Delta(y_n)" as " $|B - y_n| = \Delta(y_n)$"]
[Have: "$|(A + B) - (x_n + y_n)| \leq \Delta(x_n) + \Delta(y_n)$"]
[Fix: {ɛ} such that "$\varepsilon > 0$"]
[Have: "there exists $N'$ such that $\Delta(x_n) < \varepsilon / 2$ for all $n > N'$" by "$\lim_{n \to \infty} x_n = A$"]
[Have: "there exists $N''$ such that $\Delta(y_n) < \varepsilon / 2$ for all $n > N''$" by "Similarly, $\lim_{n \to \infty} y_n = B$"]
[Have: "Then for $n > \max\{N', N''\}$, $|(A + B) - (x_n + y_n)| < \varepsilon$"]
[Have: "$\lim_{n \to \infty} (x_n + y_n) = A + B$" by "by definition of limit"]

### 样例 21

输入：

$\int {x}^{2}\sqrt{{a}^{2} + {x}^{2}}\mathrm{\;d}x$ .

解 $\int {x}^{2}\sqrt{{a}^{2} + {x}^{2}}\mathrm{\;d}x = \frac{1}{2}\int x{\left( {a}^{2} + {x}^{2}\right) }^{\frac{1}{2}}\mathrm{\;d}\left( {{a}^{2} + {x}^{2}}\right)  = \frac{1}{3}\int x\mathrm{\;d}\left\lbrack  {\left( {a}^{2} + {x}^{2}\right) }^{\frac{3}{2}}\right\rbrack$

$$
= \frac{1}{3}x{\left( {a}^{2} + {x}^{2}\right) }^{\frac{3}{2}} - \frac{1}{3}\int {\left( {a}^{2} + {x}^{2}\right) }^{\frac{3}{2}}\mathrm{\;d}x
$$

$$
= \frac{1}{3}x\left( {{a}^{2} + {x}^{2}}\right) \sqrt{{a}^{2} + {x}^{2}} - \frac{{a}^{2}}{3}\int \sqrt{{a}^{2} + {x}^{2}}\mathrm{\;d}x - \frac{1}{3}\int {x}^{2}\sqrt{{a}^{2} + {x}^{2}}\mathrm{\;d}x.
$$

于是,得 $\int {x}^{2}\sqrt{{a}^{2} + {x}^{2}}\mathrm{\;d}x = \frac{3}{4}\left\lbrack  {\frac{1}{3}x\left( {{a}^{2} + {x}^{2}}\right) \sqrt{{a}^{2} + {x}^{2}} - \frac{{a}^{2}}{3}\int \sqrt{{a}^{2} + {x}^{2}}\mathrm{\;d}x}\right\rbrack$

$$
= \frac{1}{4}x\left( {{a}^{2} + {x}^{2}}\right) \sqrt{{a}^{2} + {x}^{2}} - \frac{{a}^{2}}{4}{\left\lbrack  \frac{x}{2}\sqrt{{a}^{2} + {x}^{2}} + \frac{{a}^{2}}{2}\ln \left( x + \sqrt{{a}^{2} + {x}^{2}}\right) \right\rbrack  } + C
$$

$$
= \frac{x\left( {2{x}^{2} + {a}^{2}}\right) }{8}\sqrt{{a}^{2} + {x}^{2}} - \frac{{a}^{4}}{8}\ln \left( {x + \sqrt{{x}^{2} + {a}^{2}}}\right)  + C.
$$

结构：

[Find: "$\int x^2 \sqrt{a^2 + x^2}\;dx$" such that []]
[Have: "$\int {x}^{2}\sqrt{{a}^{2} + {x}^{2}}\mathrm{\;d}x = \frac{1}{2}\int x{\left( {a}^{2} + {x}^{2}\right) }^{\frac{1}{2}}\mathrm{\;d}\left( {{a}^{2} + {x}^{2}}\right)  = \frac{1}{3}\int x\mathrm{\;d}\left\lbrack  {\left( {a}^{2} + {x}^{2}\right) }^{\frac{3}{2}}\right\rbrack= \frac{1}{3}x{\left( {a}^{2} + {x}^{2}\right) }^{\frac{3}{2}} - \frac{1}{3}\int {\left( {a}^{2} + {x}^{2}\right) }^{\frac{3}{2}}\mathrm{\;d}x= \frac{1}{3}x\left( {{a}^{2} + {x}^{2}}\right) \sqrt{{a}^{2} + {x}^{2}} - \frac{{a}^{2}}{3}\int \sqrt{{a}^{2} + {x}^{2}}\mathrm{\;d}x - \frac{1}{3}\int {x}^{2}\sqrt{{a}^{2} + {x}^{2}}\mathrm{\;d}x.$"]
[Have: "$\int {x}^{2}\sqrt{{a}^{2} + {x}^{2}}\mathrm{\;d}x = \frac{3}{4}\left\lbrack  {\frac{1}{3}x\left( {{a}^{2} + {x}^{2}}\right) \sqrt{{a}^{2} + {x}^{2}} - \frac{{a}^{2}}{3}\int \sqrt{{a}^{2} + {x}^{2}}\mathrm{\;d}x}\right\rbrack= \frac{1}{4}x\left( {{a}^{2} + {x}^{2}}\right) \sqrt{{a}^{2} + {x}^{2}} - \frac{{a}^{2}}{4}{\left\lbrack  \frac{x}{2}\sqrt{{a}^{2} + {x}^{2}} + \frac{{a}^{2}}{2}\ln \left( x + \sqrt{{a}^{2} + {x}^{2}}\right) \right\rbrack  } + C= \frac{x\left( {2{x}^{2} + {a}^{2}}\right) }{8}\sqrt{{a}^{2} + {x}^{2}} - \frac{{a}^{4}}{8}\ln \left( {x + \sqrt{{x}^{2} + {a}^{2}}}\right)  + C.$"]

## 证明开始部分的节点类型识别技巧

证明开头时的节点类型的识别是一个难点。下面我为你做这方面的特训：

### 样例 1

自然语言：`A sequence $\{x_n\}$ is called a Cauchy sequence if for any $\epsilon > 0$ there exists an index $N \in \mathbb{N}$ such that $|x_m - x_n| < \epsilon$ whenever $n > N$ and $m > N$. Prove that a numerical sequence converges if and only if it is a Cauchy sequence.`

处理这段语言时，典型的错误是把`A sequence $\{x_n\}$ is called a **fundamental** or **Cauchy sequence** if for any $\epsilon > 0$ there exists an index $N \in \mathbb{N}$ such that $|x_m - x_n| < \epsilon$ whenever $n > N$ and $m > N$`看成“Show”。但是，这其实是在定义什么是Cauchy sequence。真正的证明目标在后面：`Prove that a numerical sequence converges if and only if it is a Cauchy sequence.`。所以正确的节点识别为：

[Define: "Cauchy sequence" as "A sequence $\{x_n\}$ is called a fundamental or Cauchy sequence if for any $\epsilon > 0$ there exists an index $N \in \mathbb{N}$ such that $|x_m - x_n| < \epsilon$ whenever $n > N$ and $m > N$"]
[Show: "A numerical sequence converges if and only if it is a Cauchy sequence"]

### 样例 2

自然语言：`\lim_{n \to \infty} \sqrt[n]{a} = 1 \text{ for any } a > 0.`



## 特别提醒

注意观察上述样例，你会发现提取结构时，从不补充自然语言没有的表达，不自行补充reasons，不自行补充hint。结构提取必须完全以原文为准！（如果文本是英文的，你也用英文；文本是中文的，你也用中文）

注意，hint是指那些没有提出具体断言、假设、定义等等的自然语言句子。例如“我们考虑使用某某方法”，或“于是我们可以得到答案了”这样的表达。对于有具体数学内容的句子，一般不识别为hint！

请你注意区分，证明的开头有的是前提，要用Assume或Fix；有的是证明目标，要用Show。请仔细区分。

一般而言，你的工作方法是：逐句切分自然语言（不要遗漏任何一句），然后对切分后的每一句识别type

