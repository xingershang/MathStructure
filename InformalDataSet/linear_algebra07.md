# Natural Language

3.70 *dimension shows whether vector spaces are isomorphic*

Two finite-dimensional vector spaces over $\mathbf{F}$ are isomorphic if and only if they have the same dimension.

**Proof** First suppose $V$ and $W$ are isomorphic finite-dimensional vector spaces. Thus there exists an isomorphism $T$ from $V$ onto $W$. Because $T$ is invertible, we have null $T = \{0\}$ and range $T = W$. Thus

$$\dim \operatorname{null} T = 0 \quad \text{and} \quad \dim \operatorname{range} T = \dim W.$$

The formula

$$\dim V = \dim \operatorname{null} T + \dim \operatorname{range} T$$

(the fundamental theorem of linear maps, which is 3.21) thus becomes the equation $\dim V = \dim W$, completing the proof in one direction.

To prove the other direction, suppose $V$ and $W$ are finite-dimensional vector spaces of the same dimension. Let $v_1, ..., v_n$ be a basis of $V$ and $w_1, ..., w_n$ be a basis of $W$. Let $T \in \mathcal{L}(V,W)$ be defined by

$$T(c_1 v_1 + \cdots + c_n v_n) = c_1 w_1 + \cdots + c_n w_n.$$

Then $T$ is a well-defined linear map because $v_1, ..., v_n$ is a basis of $V$. Also, $T$ is surjective because $w_1, ..., w_n$ spans $W$. Furthermore, null $T = \{0\}$ because $w_1, ..., w_n$ is linearly independent. Thus $T$ is injective. Because $T$ is injective and surjective, it is an isomorphism (see 3.63). Hence $V$ and $W$ are isomorphic.

