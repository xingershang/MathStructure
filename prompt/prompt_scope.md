你需要根据已有的数学自然语言的节点结构，补充“scope”信息（后文会解释），用json格式输出。

## 数学结构的定义

### 结构介绍

数学自然语言的结构是带有类型的节点序列。节点共有八种类型：

[Show: "P"] - 下面证明命题P (P可以是列表)
    常见的可以识别为Show的自然语言表达：
        "下面证明集合S不为空"；
        "我们来证明集合S⊆T"
    Show P的scope包含对命题P的完整证明；

[Assume: "P"] - 假设命题P成立 (P可以是列表)
    常见的可以识别为Assume的自然语言表达：
        "假设a+b>1"
        "假设a+b>1不成立"
    Assume P的scope包含隐含假设P的证明段落；

[Have: "P" by "Q"] - 根据一列“定理/已得到的命题/自然语言提示”Q，得出命题P成立 (P,Q可以是列表)
    常见的可以识别为Have的自然语言表达：
        "根据逆的唯一性，我们有A=B"
        "我们有x^2>0"
        "因此f(x)=g(x)"
    Have没有scope

[Fix: {var_list} such that "P"] - 取定变量列表var_list，这些变量满足命题P (P可以是列表)
    常见的可以识别为Fix的自然语言表达：
        "给定任意X ∈ A"
        "取 x ∈ R"
    Fix的scope与Assume同理，包含会使用到被Fix引入的变量的证明段落；

[SufficeToProve: "P" by "Q"] - 提出要证明当前目标，只需证明命题P，理由为Q (P,Q可以是列表)
    常见的可以识别为SufficeToProve的自然语言表达：
        "只需证..."
        "根据...，所以只需证..."
    SufficeToProve没有scope

[ToHave: "P"] - 要使得...成立，与OnlyNeeds连着使用（P可以是列表）
    ToHave的scope包含其后的所有反向推导(OnlyNeeds)；

[OnlyNeeds: "P" by "Q"] - 只需...成立，跟在OnlyNeeds后方 (P,Q可以是列表)
    常见的可以识别为ToHave, OnlyNeeds的自然语言表达：
        "要使得...成立， 只需..."
        "要使得...成立， 只需...，即...，那么只需..."
    OnlyNeeds没有scope

[Find: {var_list} such that "P"] - 求解满足命题P的变量列表 (P可以是列表)
    常见的可以识别为Find的自然语言表达：
        "求满足x^2+2x+1=0的x"；
        "我们要找出满足x>y的f(x)的取值范围"；
        "求$\int x^2 dx$"（此时P为空）
    Find的scope是整个求解过程；

[Define: "A" as "B"] - 定义一个“符号/概念”A，其含义是B (A,B不能是列表)
    常见的可以识别为Define的自然语言表达：
        "我们用符号a ⊆ b来表示∀x, (x∈a) -> (x∈b)"
        "令f(x):=x^2"
    Define没有scope

[Hint: "string"] - 一个自然语言注释
    常见的可以识别为Hint的自然语言表达：
        "我们按照...的思路来证明"
        "于是我们可以得到答案了"
        "让我们看看接下来会发生什么"
    Hint没有scope

### JSON定义

以下是带有scope的数学结构的json定义：

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
                }),
                ("scope", {
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
                    },
                    "default": []
                })
            ]),
            "required": ["type", "proposition", "scope"],
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
                }),
                ("scope", {
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
                    },
                    "default": []
                })
            ]),
            "required": ["type", "assumption", "scope"],
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
                }),
                ("scope", {
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
                    },
                    "default": []
                })
            ]),
            "required": ["type", "var_list", "condition", "scope"],
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
                ("scope", {
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
                    },
                    "default": []
                })
            ]),
            "required": ["type", "proposition", "scope"],
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
                }),
                ("scope", {
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
                    },
                    "default": []
                })
            ]),
            "required": ["type", "var_list", "condition", "scope"],
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

## scope补充要求

你不允许修改输入的节点内部的信息，只允许补充scope信息！

## 样例

在样例中，我不完整写出json作为示例，而是写一个简洁的图示。在一些样例中，我包含了“解释”部分的内容，这部分内容是我为了向你说明如何提取结构以及要注意的事项，不是你要输出的内容！！！

### 样例 1

输入：

[Fix: {A,B} such that "$A \subseteq B$"]
[Show: "$\mathcal{P}(A) \subseteq \mathcal{P}(B)$"]
[Fix: {X} such that "$X \in \mathcal{P}(A)$"]
[Have: "$X \subseteq A$" by "definition of power set"]
[Have: "$X \subseteq B$" by "$A \subseteq B$"]
[Have: "$X \in \mathcal{P}(B)$"]
[Have: "every element of $\mathcal{P}(A)$ is also in $\mathcal{P}(B)$"]
[Have: "$\mathcal{P}(A) \subseteq \mathcal{P}(B)$"]

解释：

[Fix: {A,B} such that "$A \subseteq B$"]的scope是整个证明，因此其后的节点都位于这个节点的scope中；
[Show: "$\mathcal{P}(A) \subseteq \mathcal{P}(B)$"]的scope是其之后的所有节点；
[Fix: {X} such that "$X \in \mathcal{P}(A)$"]引入的变量X出现在其后的三个节点内，因此其scope就是它之后的三个节点

结构：

[Fix: {A,B} such that "$A \subseteq B$"]
{
    [Show: "$\mathcal{P}(A) \subseteq \mathcal{P}(B)$"]
    {
        [Fix: {X} such that "$X \in \mathcal{P}(A)$"]
        {
            [Have: "$X \subseteq A$" by "definition of power set"]
            [Have: "$X \subseteq B$" by "$A \subseteq B$"]
            [Have: "$X \in \mathcal{P}(B)$"]
        }
        [Have: "every element of $\mathcal{P}(A)$ is also in $\mathcal{P}(B)$"]
        [Have: "$\mathcal{P}(A) \subseteq \mathcal{P}(B)$"]
    }
}


### 样例 2

输入：

[Hint: "下面我们对$x^3-4x^2+2x+1$做因式分解"]
[Have: "$x=1$是$x^3-4x^2+2x+1=0$的一个解"]
[Fix: {a,b} such that "$x^3-4x^2+2x+1=(x-1)(x^2+ax+b)$"]
[Have: "$(x-1)(x^2+ax+b)=x^3+(a-1)x^2+(b-a)x-b$"]
[Have: "$a-1=-4,b-a=2,-b=1$" by "对比系数"]
[Have: "$a=-3,b=-1$" by "解得"]
[Hint: "于是完成因式分解"]
[Have: "$x^3-4x^2+2x+1=(x-1)(x^2-3x-1)$"]

解释：

[Fix: {a,b} such that "$x^3-4x^2+2x+1=(x-1)(x^2+ax+b)$"]引入的a,b出现在其后的三个节点，因此把之后三个节点放进该节点的scope当中。

结构：

[Hint: "下面我们对$x^3-4x^2+2x+1$做因式分解"]
[Have: "$x=1$是$x^3-4x^2+2x+1=0$的一个解"]
[Fix: {a,b} such that "$x^3-4x^2+2x+1=(x-1)(x^2+ax+b)$"]
{
    [Have: "$(x-1)(x^2+ax+b)=x^3+(a-1)x^2+(b-a)x-b$"]
    [Have: "$a-1=-4,b-a=2,-b=1$" by "对比系数"]
    [Have: "$a=-3,b=-1$" by "解得"]
}
[Hint: "于是完成因式分解"]
[Have: "$x^3-4x^2+2x+1=(x-1)(x^2-3x-1)$"]

### 样例 3

输入：

[Show: "$1 + 2 + \cdots + n = \frac{n(n+1)}{2}$"]
[Hint: "我们用数学归纳法证明"]
[Have: "当$n=1$时$1 + 2 + \cdots + n = \frac{n(n+1)}{2}$成立"]
[Assume: "$n=k$时$1 + 2 + \cdots + n = \frac{n(n+1)}{2}$成立"]
[Have: "$1 + 2 + \cdots  + k + \left( {k + 1}\right)  = \frac{k\left( {k + 1}\right) }{2} + k + 1 = \frac{\left( {k + 1}\right) \left\lbrack  {\left( {k + 1}\right)  + 1}\right\rbrack  }{2}$"]
[Have: "$n=k+1$时$1 + 2 + \cdots + n = \frac{n(n+1)}{2}$成立"]
[Have: "对于任何正整数$n$,有$1 + 2 + \cdots + n = \frac{n(n+1)}{2}$"]

结构：

[Show: "$1 + 2 + \cdots + n = \frac{n(n+1)}{2}$"]
{
    [Hint: "我们用数学归纳法证明"]
    [Have: "当$n=1$时$1 + 2 + \cdots + n = \frac{n(n+1)}{2}$成立"]
    [Assume: "$n=k$时$1 + 2 + \cdots + n = \frac{n(n+1)}{2}$成立"]
    {
        [Have: "$1 + 2 + \cdots  + k + \left( {k + 1}\right)  = \frac{k\left( {k + 1}\right) }{2} + k + 1 = \frac{\left( {k + 1}\right) \left\lbrack  {\left( {k + 1}\right)  + 1}\right\rbrack  }{2}$"]
        [Have: "$n=k+1$时$1 + 2 + \cdots + n = \frac{n(n+1)}{2}$成立"]
    }
    [Have: "对于任何正整数$n$,有$1 + 2 + \cdots + n = \frac{n(n+1)}{2}$"]
}

### 样例 4

输入：

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

结构：

[Fix: {a} such that "a > 0"]
{
    [Show: "$\mathop{\lim }\limits_{{n \rightarrow  \infty }}\sqrt[n]{a} = 1$"]
    {
        [Hint: "分别就$a=1,a>1$及$0<a<1$三种情形加以证明"]
        [Assume: "$a=1$"]
        {
            [Have: "$\mathop{\lim }\limits_{{n \rightarrow  \infty }}\sqrt[n]{a} = 1$"]
        }
        [Assume: "$a>1$"]
        {
            [Fix: {n, ɛ} such that "$n>1$"; "$\varepsilon>0$"]
            {
                [Have: "{\left( 1 + \varepsilon \right) }^{n} > 1 + {n\varepsilon }"]
                [Assume: "$n$ 充分大后"]
                {
                    [Have: "$1 + {n\varepsilon } > a$"]
                    [Have: "${\left( 1 + \varepsilon \right) }^{n} > a$"]
                }
                [Define: {N} as "$N = \left\lceil  \frac{a - 1}{\varepsilon }\right\rceil$"]
                [Have: "当$n > N$时${\left( 1 + \varepsilon \right) }^{n} > a$"]
                [Have: "$1 < \sqrt[n]{a} < 1 + \varepsilon$"]
                [Have: "当$n > N$时$\left| {\sqrt[n]{a} - 1}\right|  < \varepsilon$"]
            }
            [Have: "$\mathop{\lim }\limits_{{n \rightarrow  \infty }}\sqrt[n]{a} = 1$"]
        }
        [Assume: "$0 < a < 1$"]
        {
            [Define: {a'} such that "$a = \frac{1}{{a}^{\prime }} ; "a'>1"]
            [Have: "当$n \rightarrow  \infty$时$\sqrt[n]{a} = \frac{1}{\sqrt[n]{{a}^{\prime }}} \rightarrow  1$"]
            [Have: "当$a > 0$时$\mathop{\lim }\limits_{{n \rightarrow  \infty }}\sqrt[n]{a} = 1$"]
        }
    }
}

### 样例 5

输入：

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

结构：

[Fix: {q} such that "$|q| < 1$"]
{
    [Show: "等比数列$\lim_{n \to \infty} q^{n-1} = 0$"]
    {
        [Fix: {ε} such that "$0 < ε < 1$"]
        {
            [Have: "$|x_n - 0| = |q^{n-1} - 0| = |q|^{n-1}$"]
            [ToHave: "$|x_n - 0| < ε$"]
            {
                [OnlyNeeds: "$|q|^{n-1} < ε$"]
                [OnlyNeeds: "$(n-1) \ln |q| < \ln ε$" by "取自然对数"]
                [OnlyNeeds: "$n > 1 + \frac{\ln ε}{\ln |q|}$" by {"$|q| < 1$"; "$\ln |q| < 0$"}]
            }
            [Define: {N} as "$N = \left\lceil 1 + \frac{\ln ε}{\ln |q|} \right\rceil$"]
            [Have: "当$n > N$时，$|q^{n-1} - 0| < ε$"]
            [Have: "$\lim_{n \to \infty} q^{n-1} = 0$"]
        }
    }
}

### 样例 7

输入：

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

结构：

[Find: {f,g} such that  {"对于所有实数 $x$ 和 $y$ 都满足方程组 $f(x + y) = f(x) f(y) - g(x) g(y)$, $g(x + y) = f(x) g(y) + f(y) g(x)$"; "规范条件$f(0) = 1$, $g(0) = 0$"; "$f(x), g(x)$ 连续且有界"}]
{
    [Hint: "考虑 $F(x) = f^2(x) + g^2(x)$"]
    [Define: "F" as "$F(x) = f^2(x) + g^2(x)$"]
    [Have: "$F(x+y) = f^2(x+y) + g^2(x+y) ={\left\lbrack  f\left( x\right) f\left( y\right)  - g\left( x\right) g\left( y\right) \right\rbrack  }^{2} + {\left\lbrack  f\left( x\right) g\left( y\right)  + f\left( y\right) g\left( x\right) \right\rbrack  }^{2} = F\left( x\right) F\left( y\right)$"]
    [Fix: {a} such that "a = F(1) > 0"]
    {
        [Have: "$F(x) = a^x$" by ["$F(0)=1$" ; "$F(x) \not\equiv 0$"]]
        [Have: "a = 1" by "$f(x)$ 和 $g(x)$ 有界"]
    }
    [Have: "$f^2(x) + g^2(x) = 1$ 对所有实数 $x$ 成立"]
    [Have: "$0=g(0)=g(x-x) = f(x)g(-x) + f(-x)g(x)$"]
    [Have: "$1=f(0)=f(x-x) = f(x)f(-x) - g(-x)g(x)$"]
    [Have: "$f(-x) = f(x)[f^2(-x) + g^2(-x)] = f(x)$" by "上面两式分别乘以$g(-x)$和$f(-x)$，然后相加"]
    [Have: "$g(-x) = -g(x)[g^2(-x) + f^2(-x)] = -g(x)$" by "上面两式分别乘以$f(-x)$和$g(-x)$，然后相减"]
    [Have: "$f(x+y)+f(x-y)=f(x)f(y) - g(x)g(y) + f(x)f(-y) - g(x)g(-y) = 2f(x)f(y)$"]
    [Have: "$f(x) = \cos a x$" by "$f(x)$的有界性"]
    [Have: "$g(x) = \pm \sin a x$" by "$f^2(x) + g^2(x) = 1$"]
}

### 样例 8

输入：

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

结构：

[Fix: {f,g} such that {"$f: A \to B$ injection"; "$g: B \to A$ injection"}]
{
    [Show: "There exists a bijection from $A$ to $B$"]
    {
        [Fix: {f,g} such that {"$f: A \to B$ injection"; "$g: B \to A$ injection"}]
        {
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
            {
                [Have: "$\forall d \in D. \exists c \in C. g(d) = c$"]
                [Have: "$\exists c \in A, g(d) = c$" by "$g$ is an injection from $B$ into $A$"]
                [Show: "$c \notin C_n$"]
                {
                    [Assume: "$c \in C_n$"]
                    {
                        [Assume: "$n = 0$"]
                        {
                            [Have: "contradiction"]
                        }
                        [Assume: "$n = m+1$"]
                        {
                            [Have: "$c \in C_{m+1} \Rightarrow d \in D_m$"]
                            [Have: "contradiction"]
                        }
                    }
                }
                [Have: "$c \in C$"]
            }
            [Show: "$\forall c \in C.\, \exists d \in D.\, g(d) = c$"]
            {
                [Have: "$\forall c \in C. \exists d \in D. g(d) = c$"]
                [Have: "$\exists d \in B. g(d) = c$" by "Otherwise, $c \in C_0$, contradiction."]
                [Show: "$d \notin D_n$"]
                {
                    [Assume: "$d \notin D_n$"]
                    {
                        [Have: "$c \in C_{n+1}$"]
                        [Have: "contradiction"]
                    }
                        
                }
                [Have: "$d \in D$"]
            }
        }
    }
}

## 特别提醒

注意观察上述样例，你会发现补充scope时，完全不修改输入的节点信息和节点顺序，只是“补充大括号”的工作。

