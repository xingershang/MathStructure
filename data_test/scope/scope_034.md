[Show: "a + b + c + d < \frac{b}{a} + \frac{c}{b} + \frac{d}{c} + \frac{a}{d}"]
{
    [Assume: "a + b + c + d > \frac{a}{b} + \frac{b}{c} + \frac{c}{d} + \frac{d}{a}"]
    {
        [Fix: {a, b, c, d} st {"a,b,c,d>0"; "abcd = 1"}]
        {
            [Hint: "We show that the sum a+b+c+d is bounded above by a weighted mean of two cyclic ratios."]
            [Hint: "Apply the AM-GM inequality to \tfrac{a}{b},\tfrac{b}{c},\tfrac{c}{d},\tfrac{d}{a}."]
            [Have: {"a \le \tfrac14\left(\tfrac{a}{b}+\tfrac{b}{c}+\tfrac{c}{d}+\tfrac{d}{a}\right)"; "b \le \tfrac14\left(\tfrac{b}{c}+\tfrac{c}{d}+\tfrac{d}{a}+\tfrac{a}{b}\right)"; "c \le \tfrac14\left(\tfrac{c}{d}+\tfrac{d}{a}+\tfrac{a}{b}+\tfrac{b}{c}\right)"; "d \le \tfrac14\left(\tfrac{d}{a}+\tfrac{a}{b}+\tfrac{b}{c}+\tfrac{c}{d}\right)"} by "AM-GM"]
            [Have: "a + b + c + d \le \tfrac34\left(\tfrac{a}{b}+\tfrac{b}{c}+\tfrac{c}{d}+\tfrac{d}{a}\right)+\tfrac14\left(\tfrac{b}{a}+\tfrac{c}{b}+\tfrac{d}{c}+\tfrac{a}{d}\right)" by "Summing previous inequalities"]
            [Have: "a + b + c + d < \tfrac{b}{a}+\tfrac{c}{b}+\tfrac{d}{c}+\tfrac{a}{d}" by {"Assumption a+b+c+d > a/b + b/c + c/d + d/a"; "Weighted-mean inequality obtained above"}]
        }
    }
}