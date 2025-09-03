你是一个数理逻辑专家。你需要你帮我提取数学自然语言的语言结构，结构的定义如下。

# 数学结构

## 数学结构的定义

数学自然语言的结构是带有类型的节点序列。节点共有八种类型。下面依次给出其格式的定义：

[Show: {P}] - 下面证明命题P (P可以是列表，[Show: {P1}; {P2}; ... ; {Pn}])
    常见的可以识别为Show的自然语言表达：
        "下面证明集合S不为空" -> [Show: {集合S不为空}]；
        "我们来证明集合S⊆T" -> [Show: {集合S⊆T}]；
[Assume: {P}] - 假设命题P成立 (P可以是列表，[Assume: {P1}; {P2}; ... ; {Pn}])
    常见的可以识别为Assume的自然语言表达：
        "假设a+b>1" -> [Assume: {a+b>1}]；
        "假设a+b>1不成立" -> [Assume: {a+b>1不成立}]；
[Have: {P} by {Q}] - 根据一列“定理/已得到的命题/自然语言提示”Q，得出命题P成立 (P,Q可以是列表)
    常见的可以识别为Have的自然语言表达：
        "根据逆的唯一性，我们有A=B"
        "我们有x^2>0"
        "因此f(x)=g(x)"
[Fix: {var_list} such that {P}] - 取定变量列表var_list，这些变量满足命题P (P可以是列表)
    常见的可以识别为Fix的自然语言表达：
        "给定任意X ∈ A"
        "取 x ∈ R"
[SufficeToProve: {P} by {Q}] - 提出要证明当前目标，只需证明命题P，理由为Q (P,Q可以是列表)
    常见的可以识别为SufficeToProve的自然语言表达：
        "只需证..."
        "根据...，所以只需证..."
[ToHave: {P}] - 要使得...成立，与OnlyNeeds连着使用（P可以是列表）
[OnlyNeeds: {P} by {Q}] - 只需...成立，跟在OnlyNeeds后方 (P,Q可以是列表)
    常见的可以识别为ToHave, OnlyNeeds的自然语言表达：
        "要使得...成立， 只需..."
        "要使得...成立， 只需...，即...，那么只需..."
[Find: {var_list} such that {P}] - 求解满足命题P的变量列表 (P可以是列表)
    常见的可以识别为Find的自然语言表达：
        "求满足x^2+2x+1=0的x"；
        "我们要找出满足x>y的f(x)的取值范围"；
        "求$\int x^2 dx$"（此时P为空）
[Define: {A} as {B}] - 定义一个“符号/概念”A，其含义是B (A,B不能是列表)
    常见的可以识别为Define的自然语言表达：
        "我们用符号a ⊆ b来表示∀x, (x∈a) -> (x∈b)"
        "令f(x):=x^2"
[Hint: {string}] - 一个自然语言注释
    常见的可以识别为Hint的自然语言表达：
        "我们按照...的思路来证明"
        "于是我们可以得到答案了"
        "让我们看看接下来会发生什么"

## 自然语言文本与最终结构的识别结果的对比示例

我保证输入的自然语言文本已经按句编号，你只需要对每个句子识别节点类型即可。

### 示例1

自然语言文本：

[Sentence 1] If $A \subseteq B$
[Sentence 2] then $\mathcal{P}(A) \subseteq \mathcal{P}(B)$
[Sentence 3] Let $X \in \mathcal{P}(A)$.
[Sentence 4] By definition of power set, $X \subseteq A$.
[Sentence 5] Since $A \subseteq B$, it follows that $X \subseteq B$. 
[Sentence 6] Therefore, $X \in \mathcal{P}(B)$. 
[Sentence 7] Hence, every element of $\mathcal{P}(A)$ is also in $\mathcal{P}(B)$
[Sentence 8] so $\mathcal{P}(A) \subseteq \mathcal{P}(B)$.

结构：

[Fix: {A,B} such that {$A \subseteq B$}]
[Show: {$\mathcal{P}(A) \subseteq \mathcal{P}(B)$}]
[Fix: {X} such that {$X \in \mathcal{P}(A)$}]
[Have: {$X \subseteq A$} by {definition of power set}]
[Have: {$X \subseteq B$} by {$A \subseteq B$}]
[Have: {$X \in \mathcal{P}(B)$}]
[Have: {every element of $\mathcal{P}(A)$ is also in $\mathcal{P}(B)$}]
[Have: {$\mathcal{P}(A) \subseteq \mathcal{P}(B)$}]

# 输入输出格式要求

每一轮询问，我会给你待识别的自然语言语句，前面所有轮的识别的思考过程的历史记录，以及前面所有轮的识别结果的汇总。请你参考这三项内容识别下一个语句。

我保证输入的自然语言数学文本已经被切分了一个一个的句子。每次你只需要取出下一个句子，然后识别那个句子即可。在注意，只需识别一句话！（你的输出不需要标号）

你的输出格式为

<thinking>
{待识别的句子（含编号）}
{思考}
</thinking>

<result>
{识别结果（按定义中的标准格式输出，不含编号）}
<result>

在thinking字段做思考，思考的格式我已经给出，请你严格遵守。也即，你只能修改{...}中的内容。

如果给你的历史记录恰好已经修改完了所有的话，你只需要在result字段输出`End.`这四个字符。

## 样例

### 样例 1

输入：

[Sentence 1] If $A \subseteq B$
[Sentence 2] then $\mathcal{P}(A) \subseteq \mathcal{P}(B)$
[Sentence 3] Let $X \in \mathcal{P}(A)$.
[Sentence 4] By definition of power set, $X \subseteq A$.
[Sentence 5] Since $A \subseteq B$, it follows that $X \subseteq B$. 
[Sentence 6] Therefore, $X \in \mathcal{P}(B)$. 
[Sentence 7] Hence, every element of $\mathcal{P}(A)$ is also in $\mathcal{P}(B)$
[Sentence 8] so $\mathcal{P}(A) \subseteq \mathcal{P}(B)$.

<thinking>
[Sentence 1] If $A \subseteq B$
这是证明目标的一部分。其中，A,B是新引入的变量，所以用Fix节点。
</thinking>

<result>
[Fix: {A,B} such that {$A \subseteq B$}]
</result>

<thinking>
[Sentence 2] then $\mathcal{P}(A) \subseteq \mathcal{P}(B)$
这是证明目标，所以用Show节点。
</thinking>

<result>
[Show: {$\mathcal{P}(A) \subseteq \mathcal{P}(B)$}]
</result>

<thinking>
[Sentence 3] Let $X \in \mathcal{P}(A)$.
引入了一个新的变量X，满足条件$X \in \mathcal{P}(A)$，所以用Fix节点。
</thinking>

<result>
[Fix: {X} such that {$X \in \mathcal{P}(A)$}]
</result>

<thinking>
[Sentence 4] By definition of power set, $X \subseteq A$.
得到了一个断言$X \subseteq A$，理由是By definition of power set，所以是带有一个依据的Have节点。
</thinking>

<result>
[Have: {$X \subseteq A$" by "definition of power set}]
</result>

<thinking>
[Sentence 5] Since $A \subseteq B$, it follows that $X \subseteq B$. 
得到了一个断言$X \subseteq B$，理由是$A \subseteq B$，所以是带有一个依据的Have节点。
</thinking>

<result>
[Have: {$X \subseteq B$" by "$A \subseteq B$}]
</result>


<thinking>
[Sentence 6] Therefore, $X \in \mathcal{P}(B)$. 
得到了一个断言$X \in \mathcal{P}(B)$，没有说明理由。所以是不带有依据的Have节点。
</thinking>

<result>
[Have: {$X \in \mathcal{P}(B)$}]
</result>

<thinking>
[Sentence 7] Hence, every element of $\mathcal{P}(A)$ is also in $\mathcal{P}(B)$
得到了一个断言every element of $\mathcal{P}(A)$ is also in $\mathcal{P}(B)$，没有说明理由。所以是不带有依据的Have节点。
</thinking>

<result>
[Have: {every element of $\mathcal{P}(A)$ is also in $\mathcal{P}(B)$}]
</result>

<thinking>
[Sentence 8] so $\mathcal{P}(A) \subseteq \mathcal{P}(B)$.
得到了一个断言$\mathcal{P}(A) \subseteq \mathcal{P}(B)$，没有说明理由。所以是不带有依据的Have节点。
</thinking>

<result>
[Have: {$\mathcal{P}(A) \subseteq \mathcal{P}(B)$}]
</result>

<thinking>
证明已结束。输出"End."。
</thinking>

<result>
End.
</result>

（请特别注意！！！！！并不是要你一次性输出全部的Round，而是我们会给你原始自然语言文本，历史已有的Round，以及已经识别的节点，要求你输出下一个Round。比如，给定的历史Round如果是Round 1到Round 5，那么你需要输出Round 6。你的输出只需包含一个thinking字段和一个result字段。）

