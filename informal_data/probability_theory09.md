# Natural Language

**Theorem 9.8.** Let $\{X_n, \mathcal{F}_n, n=0,1,2,\}$ be a submartingale and let $T$ be a stopping time. Then $\{X_{n \wedge T}, \mathcal{F}_n, n=0,1,2,\ldots\}$ is a submartingale, as is $\{X_{n \wedge T}, \mathcal{F}_{n \wedge T}, n=0,1,2,\ldots\}$.

**Proof.** The properties of stopping times and their associated $\sigma$-fields were established in §7.4. We will use them freely.

Note that $X_{n \wedge T}$ is measurable with respect to $\mathcal{F}_{n \wedge T} \subset \mathcal{F}_T$, so $X_{n \wedge T}$ is adapted to both filtrations $(\mathcal{F}_n)$ and $(\mathcal{F}_{n \wedge T})$. Let $\Lambda \in \mathcal{F}_n$.

\[
\int_{\Lambda} X_{(n+1) \wedge T} dP = \int_{\Lambda \cap \{T > n\}} X_{n+1} dP + \int_{\Lambda \cap \{T \leq n\}} X_{n \wedge T} dP,
\]

for $X_{(n+1) \wedge T} = X_{n+1}$ if $T > n$. Now $\Lambda \cap \{T > n\} \in \mathcal{F}_n$ so, as $(X_n)$ is a submartingale,

\[
\int_{\Lambda \cap \{T > n\}} X_{n+1} dP \geq \int_{\Lambda \cap \{T > n\}} X_n dP = \int_{\Lambda \cap \{T > n\}} X_{n \wedge T} dP,
\]

and the above is

\[
\geq \int_{\Lambda \cap \{T > n\}} X_{n \wedge T} dP + \int_{\Lambda \cap \{T \leq n\}} X_{n \wedge T} dP = \int_{\Lambda} X_{n \wedge T} dP,
\]

showing that $(X_{n \wedge T})$ is a submartingale relative to the filtration $(\mathcal{F}_n)$. Since $\mathcal{F}_{n \wedge T} \subset \mathcal{F}_n$, this also shows it is a submartingale with respect to the filtration $(\mathcal{F}_{n \wedge T})$.  □
