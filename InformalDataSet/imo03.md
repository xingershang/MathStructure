# Natural Language

## Goal

A number is called Norwegian if it has three distinct positive divisors whose sum is equal to $2022$. Show that the smallest Norwegian number is $1344$.
(Note: The total number of positive divisors of a Norwegian number is allowed to be larger than 3.)

## Proof

Observe that $1344$ is a Norwegian number as $6$, $672$ and $1344$ are three distinct divisors of $1344$ and $6+672+1344=2022$. It remains to show that this is the smallest such number.

Assume for contradiction that $N<1344$ is Norwegian and let $N/a,N/b$ and $N/c$ be the three distinct divisors of $N$, with $a<b<c.$ Then

$$
2022=N\left(\frac1a+\frac1b+\frac1c\right)<1344\left(\frac1a+\frac1b+\frac1c\right)
$$

and so

$$
\left(\frac1a+\frac1b+\frac1c\right)>\frac{2022}{1344}=\frac{337}{224}=\frac32+\frac1{224}
$$

If $a>1$ then

$$
\begin{aligned}\frac{1}{a}+\frac{1}{b}+\frac{1}{c}\leqslant\frac{1}{2}+\frac{1}{3}+\frac{1}{4}=\frac{13}{12}<\frac{3}{2},\end{aligned}
$$

so it must be the case that $a=1.$ Similarly, it must hold that $b<4$ since otherwise

$$
1+\dfrac{1}{b}+\dfrac{1}{c}\leqslant1+\dfrac{1}{4}+\dfrac{1}{5}<\dfrac{3}{2}
$$

This leaves two cases to check, $b=2$ and $b=3$.

$\textbf{Case }b= 3.$ Then

$$
\begin{aligned}\frac1c>\frac32+\frac1{224}-1-\frac13>\frac16,\end{aligned}
$$

so $c=4$ or $c=5.$ If $c=4$ then

$$
2022=N\left(1+\dfrac{1}{3}+\dfrac{1}{4}\right)=\dfrac{19}{12}N
$$

but this is impossible as $19\not\mid 2022$. If $c=5$ then

$$
2022=N\left(1+\frac13+\frac15\right)=\frac{23}{15}N
$$

which again is impossible, as 23 $\nmid2022.$

Case $b=2.$ Note that $c<224$ since

$$
\frac1c>\frac32+\frac1{224}-1-\frac12=\frac1{224}
$$

It holds that

$$
2022=N\left(1+\frac12+\frac1c\right)=\frac{3c+2}{2c}N\Rightarrow(3c+2)N=4044c
$$

Since $(c,3c-2)=(c,2)\in\{1,2\}$, then $3c+2\mid8088=2^3\cdot3\cdot337$ which implies that $3c+2\mid2^3\cdot337.$ But since $3c+2\geqslant3\cdot3+2>8=2^3$ and $3c+2\neq337$, then it must hold that $3c+2\geqslant2\cdot337$, contradicting $c<224.$

$Qed.$













