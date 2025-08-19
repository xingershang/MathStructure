[Hint: "为方便阅读，首先引入题设条件中的变量"]
[Fix: {a, b, c} st {"a,b,c>0"; "1/a+1/b+1/c=a+b+c"}]
{
    [Show: "1/(2a+b+c)^2+1/(2b+c+a)^2+1/(2c+a+b)^2\le3/16"]
    {
        [Hint: "接下来证明一个对一般正数 x,y,z 成立的不等式，以备后用"]
        [Fix: {x, y, z} st "x,y,z>0"]
        {
            [Have: "1/(2x+y+z)^2\le1/[4(x+y)(x+z)]" by "AM-GM: 2x+y+z=(x+y)+(x+z)\ge2\sqrt{(x+y)(x+z)}"]
        }
        [Hint: "将上式分别代入 a,b,c 可得"]
        [Have: "1/(2a+b+c)^2+1/(2b+c+a)^2+1/(2c+a+b)^2\le1/[4(a+b)(a+c)]+1/[4(b+c)(b+a)]+1/[4(c+a)(c+b)]"]
        [Have: "1/[4(a+b)(a+c)]+1/[4(b+c)(b+a)]+1/[4(c+a)(c+b)]=[a+b+c]/[2(a+b)(b+c)(c+a)]"]
        [Hint: "下面建立几个关于 a,b,c 的辅助不等式"]
        [Have: "a^2b+a^2c+b^2a+b^2c+c^2a+c^2b\ge6abc" by "AM-GM"]
        [Have: "9(a+b)(b+c)(c+a)\ge8(a+b+c)(ab+bc+ca)" by "与上一式等价"]
        [Have: "ab+bc+ca=abc(a+b+c)" by "由 1/a+1/b+1/c=a+b+c 变形"]
        [Have: "(ab+bc+ca)^2\ge3abc(a+b+c)" by "三次应用 AM-GM: a^2b^2+a^2c^2\ge2a^2bc 等"]
        [Hint: "将(1)(2)(3)(4)综合可得目标不等式"]
        [Have: "[a+b+c]/[2(a+b)(b+c)(c+a)]=[(a+b+c)(ab+bc+ca)]/[2(a+b)(b+c)(c+a)]·[ab+bc+ca]/[abc(a+b+c)]=abc(a+b+c)/(ab+bc+ca)^2\le9/2·1/8·1/3=3/16" by "利用之前得到的(2)(3)(4)"]
        [Hint: "证毕"]
    }
}