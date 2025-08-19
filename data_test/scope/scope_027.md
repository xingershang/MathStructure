[Hint: "Let k≥2 be an integer."]
[Fix: {k} st {"k is an integer"; "k \ge 2"}]
{
    [Show: "The smallest integer n\ge k+1 with the property that “there exists a set of n distinct real numbers such that each element of the set can be written as a sum of k other distinct elements of the set” is n = k+4"]
    {
        [Hint: "First we prove the lower bound n \ge k+4."]
        [Assume: {"There exists a set \{a_1,a_2,\dots ,a_n\} of n distinct real numbers satisfying the required property"; "They are ordered a_1<a_2<\cdots <a_n"}]
        {
            [Have: "a_1 \ge a_2+\cdots +a_{k+1}" by "a_1 must be expressed as a sum of k other distinct elements"]
            [Have: "a_{n-k}+\cdots +a_{n-1} \ge a_n" by "a_n must be expressed as a sum of k other distinct elements"]
            [Have: "n \ge k+1"]
            [Hint: "Case n = k+1 leads to a contradiction."]
            [Assume: "n = k+1"]
            {
                [Have: "a_1 \ge a_2+\cdots +a_{k+1} > a_1+\cdots +a_k \ge a_{k+1}"]
                [Have: "Contradiction"]
            }
            [Hint: "Case n = k+2 leads to a contradiction."]
            [Assume: "n = k+2"]
            {
                [Have: "a_1 \ge a_2+\cdots +a_{k+1} \ge a_{k+2}"]
                [Have: "Contradiction"]
            }
            [Hint: "Case n = k+3 also gives a contradiction."]
            [Assume: "n = k+3"]
            {
                [Have: "a_1 \ge a_2+\cdots +a_{k+1}"]
                [Have: "a_3+\cdots +a_{k+2} \ge a_{k+3}"]
                [Have: "Adding the two inequalities gives a_1+a_{k+2} \ge a_2+a_{k+3}"]
                [Have: "Contradiction"]
            }
            [Have: "Therefore n \ge k+4" by "All smaller possibilities contradicted"]
        }
        [Hint: "Now we construct a set with k+4 elements that satisfies the property."]
        [Hint: "Even k = 2l case"]
        [Assume: {"k = 2l"; "l \ge 1"}]
        {
            [Define: "A_i" as ""For 1\le i\le l+2, A_i = \{-i,i\}""]
            [Define: "S" as ""S = A_1 \cup A_2 \cup \cdots \cup A_{l+2}""]
            [Have: "S has exactly k+4 = 2l+4 elements"]
            [Hint: "Showing every element of S is a sum of k other distinct elements (even k)."]
            [Have: {"If i can be represented, so can -i by negating"; "Consider only 1\le i\le l+2"}]
            [Have: "For i<l+2 we use the numbers from any l-1 sets A_j (j\ne1,i+1) together with i+1 and -1 to obtain i"]
            [Have: "For i = l+2 we use the numbers from any l-1 sets A_j (j\ne 1,l+1) together with l+1 and 1 to obtain l+2"]
            [Have: "Thus every element of S can be written as a sum of k distinct others"]
        }
        [Hint: "Odd k = 2l+1 case"]
        [Assume: {"k = 2l+1"; "l \ge 1"}]
        {
            [Define: "S'" as ""Take the previous even–k set S and add 0""]
            [Have: "S' has (k+4) elements"]
            [Have: "Adding 0 preserves all earlier representations"]
            [Have: "0 can be represented as 1+2+(-3) plus the elements of the remaining l-1 sets A_4,\dots ,A_{l+2}, giving a sum of k distinct elements"]
            [Have: "Hence every element of S' is a sum of k other distinct elements"]
        }
        [Have: "There exists a set of k+4 distinct real numbers satisfying the property" by "Both even and odd k constructions provided"]
        [Have: "Combining the lower bound n \ge k+4 with the construction for n = k+4, the smallest such n is k+4"]
    }
}