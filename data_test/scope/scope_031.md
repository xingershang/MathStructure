[Hint: "Let $a_1, a_2, \dots , a_{100}$ be non-negative real numbers with $\sum_{k=1}^{100}a_k^{2}=1$"]
[Fix: {a_1, a_2, a_3, a_4, a_5, a_6, a_7, a_8, a_9, a_{10}, a_{11}, a_{12}, a_{13}, a_{14}, a_{15}, a_{16}, a_{17}, a_{18}, a_{19}, a_{20}, a_{21}, a_{22}, a_{23}, a_{24}, a_{25}, a_{26}, a_{27}, a_{28}, a_{29}, a_{30}, a_{31}, a_{32}, a_{33}, a_{34}, a_{35}, a_{36}, a_{37}, a_{38}, a_{39}, a_{40}, a_{41}, a_{42}, a_{43}, a_{44}, a_{45}, a_{46}, a_{47}, a_{48}, a_{49}, a_{50}, a_{51}, a_{52}, a_{53}, a_{54}, a_{55}, a_{56}, a_{57}, a_{58}, a_{59}, a_{60}, a_{61}, a_{62}, a_{63}, a_{64}, a_{65}, a_{66}, a_{67}, a_{68}, a_{69}, a_{70}, a_{71}, a_{72}, a_{73}, a_{74}, a_{75}, a_{76}, a_{77}, a_{78}, a_{79}, a_{80}, a_{81}, a_{82}, a_{83}, a_{84}, a_{85}, a_{86}, a_{87}, a_{88}, a_{89}, a_{90}, a_{91}, a_{92}, a_{93}, a_{94}, a_{95}, a_{96}, a_{97}, a_{98}, a_{99}, a_{100}} st {"a_1,\dots ,a_{100}\ge 0"; "$a_1^{2}+\dots +a_{100}^{2}=1$"}]
{
    [Show: "$a_1^{2}a_2+a_2^{2}a_3+\dots +a_{100}^{2}a_1<\dfrac{12}{25}$"]
    {
        [Define: "S" as ""$S=\sum_{k=1}^{100}a_k^{2}a_{k+1}$ (indices modulo $100$)""]
        [Hint: "Apply Cauchy–Schwarz and then AM–GM"]
        [Have: "$(3S)^{2}\le\left(\sum_{k=1}^{100}a_{k+1}^{2}\right)\left(\sum_{k=1}^{100}(a_k^{2}+2a_ka_{k+1}a_{k+2})^{2}\right)$" by "Cauchy–Schwarz on sequences $(a_{k+1})$ and $(a_k^{2}+2a_ka_{k+1}a_{k+2})$"]
        [Have: "$(3S)^{2}\le\sum_{k=1}^{100}\bigl(a_k^{4}+4a_k^{2}a_{k+1}a_ka_{k+2}+4a_k^{2}a_{k+1}^{2}\bigr)$" by "$\sum_{k=1}^{100}a_{k+1}^{2}=1$"]
        [Have: "$(3S)^{2}\le\sum_{k=1}^{100}\bigl(a_k^{4}+6a_k^{2}a_{k+1}^{2}+2a_k^{2}a_{k+2}^{2}\bigr)$" by "AM–GM: $4a_k^{2}a_{k+1}a_ka_{k+2}\le 2a_k^{2}(a_k^{2}+a_{k+2}^{2})$"]
        [Hint: "Use two trivial estimates to bound the sum"]
        [Have: "$\displaystyle\sum_{k=1}^{100}\bigl(a_k^{4}+2a_k^{2}a_{k+1}^{2}+2a_k^{2}a_{k+2}^{2}\bigr)\le\left(\sum_{k=1}^{100}a_k^{2}\right)^{2}=1$" by "Cauchy–Schwarz / rearrangement"]
        [Have: "$\displaystyle\sum_{k=1}^{100}a_{2k-1}^{2}a_{2k}^{2}\le\left(\sum_{k=1}^{50}a_{2k-1}^{2}\right)\left(\sum_{k=1}^{50}a_{2k}^{2}\right)$" by "Cauchy–Schwarz"]
        [Have: "$(3S)^{2}\le 1+4\left(\sum_{k=1}^{50}a_{2k-1}^{2}\right)\left(\sum_{k=1}^{50}a_{2k}^{2}\right)\le1+\left(\sum_{k=1}^{100}a_k^{2}\right)^{2}=2$" by {"Previous two bounds"; "$x+y\le(x+y)^{2}$ when $x+y=1$"}]
        [Have: "$S\le\dfrac{\sqrt2}{3}<\dfrac{12}{25}$" by "$(3S)^{2}\le2\implies S\le\sqrt2/3$"]
        [Have: "$a_1^{2}a_2+a_2^{2}a_3+\dots +a_{100}^{2}a_1<\dfrac{12}{25}$" by "$S<12/25$"]
    }
}