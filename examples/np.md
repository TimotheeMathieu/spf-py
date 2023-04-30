# A proof of Neyman-Pearson Lemma

$\renewcommand{\P}{\mathbb{P}}$
$\newcommand{\E}{\mathbb{E}}$
$\newcommand{\R}{\mathbb{R}}$
$\newcommand{\1}{\textbf{1}}$
$\newcommand{\d}{\textrm{d}}$
$\newcommand{\Med}{\mathrm{Med}}$
$\newcommand{\N}{\mathbb{N}}$

**Theorem**

Let $P_0$ and $P_1$ be probability distributions with densities $p_0$ and $p_1$ respectively with respect to a common measure $\mu$.

* (i). For testing $H_0:p_0$ versus $H_1: p_1$ there exists a (randomized) test $\phi$ and a constant $k>0$ such that $\E_{p_0}[\phi(X)]=\alpha$, and
$$\phi(x)=\begin{cases}
0 & \text{if } p_1(x) < kp_0(x)\\
1 & \text{if } p_1(x) > kp_0(x).
\end{cases}$$
* (ii). For any test $\psi$ and $k>0$, it holds that 
$$k\E_{p_0}[\psi(X)]+ \E_{p_1}[1-\psi(X)]\ge \int_\R \min(kp_0(x), p_1(x)) \d \mu(x),$$p
Moreover, equality holds for a likelihood ratio test, e.g. $\psi = \phi$ whatever its value when $p_1(x) = kp_0(x)$.

> *Remarks*: 
> * Result (i) says that for any type I error $\alpha \in (0,1)$, there exists a likelihood ratio test with exactly level $\alpha$·
> * A consequence of (ii) is that for a (randomized) test $\psi$, if the type I error $\E_{p_0}[\psi(X)]$ is fixed equal to some $\alpha \in (0,1)$, then the test that achieve the minimal type II error $\E_{p_1}[1-\psi(X)]$ is the likelihood ratio test of level $\alpha$. Hence, the liklihood ratio test is the most powerful test for testing simple hypotheses.
> * One may notice that in the case $k=1$ and if $\mu(\{x: p_1(x)=p_0(x)\})=0$ , $\int_\R \min(p_0(x), p_1(x)) \d\mu(x) = 1-TV(P_0, P_1)$. Similarly, the quantity $\int_\R \min(kp_0(x), p_1(x)) \d \mu(x)$ can be interpreted as a weighted similarity measure between $P_0$ and $P_1$.

*Proof of the theorem*  
## Proof of (i) follows from the fact that $c \mapsto \P_{p_0}(p_1(X)> cp_0(x))$ is non-increasing and by tuning appropriately the value of $\phi$ when $p_1(x)=k p_0(x)$ if there is a jump of $c \mapsto \P_{p_0}(p_1(X)> cp_0(x))$  at this point.

### For some $c>0$, let $\alpha(c) = \P_{p_0}(p_1(X)> cp_0(x))$. We have,
$$\alpha(c) = \P_{p_0}\left( \frac{p_1(X)}{p_0(X)}\ge c \right).$$

#### The probability is taken under $p_0$, hence it only needs to be considered when $p_0(x)>0$.

### Hence, $1-\alpha(c)$ is a c.d.f. and in particular, $\alpha(c)$ is non-increasing and continuous on the right.\slabel{step:continuity_alpha}

### Let $\alpha(k-0)=\lim_{c \to k, c < k} \alpha(c)$ be the limit by the left of $\alpha(c)$ in $c=k$ and let $k$ be such that $\alpha(k)\le \alpha \le \alpha(k-0) $. Define \slabel{step:def_phi}
$$\phi(x)=\begin{cases}
0 & \text{if } p_1(x) > kp_0(x)\\
\frac{\alpha-\alpha(k-0)}{ \alpha(k-0)-\alpha(k)} & \text{if }p_1(x)=kp_0(x)\\
1 & \text{if } p_1(x) < kp_0(x).
\end{cases}$$
With this definition of $\phi$, we have $\E_{p_0}[\phi(X)]=\alpha$.
#### Existence of $k$: we have $\alpha(0)=\P_{p_0}(p_1(X)\ge 0)=1$ and $\alpha(\infty)=\P_{p_0}(p_1(X)\ge \infty)=0$. 
Then, because $\alpha$ is right-continuous and non-increasing (See Step \sref{step:continuity_alpha}), by intermediate value theorem, there exists $k$ such that $\alpha(k)\le \alpha \le \alpha(k-0)$.
#### $\E_{p_0}[\phi(X)]=\alpha$: we have, 
$$\E_{p_0}[\phi(X)]=\P_{p_0}\left( \frac{p_1(x)}{p_0(x)}>k \right)+\frac{\alpha-\alpha(k-0)}{ \alpha(k-0)-\alpha(k)}\P_{p_0}\left( \frac{p_1(x)}{p_0(x)}=k \right)$$
by continuity on the right, $\P_{p_0}\left( \frac{p_1(x)}{p_0(x)}=k \right)=\alpha(k-0)-\alpha(k)$ and moreover, by definition of $k$,  $\P_{p_0}\left( \frac{p_1(x)}{p_0(x)}>k \right) = \alpha(k-0)$. Hence $\E_{p_0}[\phi(X)]=\alpha$.

## Proof of (ii) follows by first showing that the value of $\psi$ when $kp_0(x)=p_1(x)$ has no incidence on the value of  $k\E_{p_0}[\psi(X)]+ \E_{p_1}[1-\psi(X)]$. Then, we show equality in the inequality of (ii) for $\psi=\phi $ and then finally we proove that for any $\psi$,
$$k\E_{p_0}[\psi(X)]+ \E_{p_1}[1-\psi(X)] \ge k\E_{p_0}[\phi(X)]+ \E_{p_1}[1-\phi(X)],$$
which concludes the argument.

### $k\E_{p_0}[\psi(X)]+ \E_{p_1}[1-\psi(X)]$ has the same value if we change the value given to $\psi$ when $kp_0(x)=p_1(x)$, because \slabel{step:equality}
$$
\begin{align*}
k\E_{p_0}[\psi(X)]+ \E_{p_1}[1-\psi(X)]&= 1+\int (kp_0(x)-p_1(x))\psi(x) \d \mu(x)\\
&=1+\int (kp_0(x)-p_1(x)) \1\{kp_0(x) \neq p_1(x)\}\psi(x) \d \mu(x).
\end{align*}$$

### In the case of $\psi=\phi$, from Step \sref{step:equality}, we have 
$$
\begin{align*}
k\E_{p_0}[\phi(X)]+ \E_{p_1}[1-\phi(X)]&=1+\int (kp_0(x)-p_1(x)) \1\{kp_0(x) \neq p_1(x)\}\phi(X) \d \mu(x))\\
&=1+\int (kp_0(x)-p_1(x)) \1\{\phi(X)=1\} \d \mu(x))\\
&=1+k\P_{p_0}(\phi(X)=1)-\P_{p_1}(\phi(X)=1)\\
&= k\P_{p_0}(\phi(X)=1)+ \P_{p_1}(\phi(X)=0)+ \P_{p_1}(\phi(X) \in (0,1)),
\end{align*}
$$
Then, use that $\P_{p_1}(\phi(X) \in (0,1))=\int_{\R}\min(kp_0(x), p_1(x)) \1\{kp_0(x) =   p_1(x)\} \d \mu(x)$ and 
$$\begin{align}
k&\P_{p_0}(\phi(X)=1)+ \P_{p_1}(\phi(X)=0) \\
=& k\int_{\R}p_0(x)\1\{\phi(x)=1\} \d \mu(x) + \int_{\R}p_1(x)\1\{\phi(x)=0\} \d \mu(x)\\
=& k\int_{\R}p_0(x)\1\{p_1(x) > kp_0(x)\} \d \mu(x) + \int_{\R}p_1(x)\1\{p_1(x) < kp_0(x)\} \d \mu(x)\\
=& \int_{\R}\min(kp_0(x), p_1(x)) \1\{kp_0(x) \neq  p_1(x)\} \d \mu(x). 
\end{align}
$$
Together, these prove the equality in the inequality of (ii).
### Optimality of $\phi$: from Step \sref{step:equality}, we have
$$
\begin{align*}
k\E_{p_0}[\psi(X)]+ \E_{p_1}[1-\psi(X)]&= 1+\int (kp_0(x)-p_1(x)) \1\{kp_0(x) \neq p_1(x)\}\psi(x) \d \mu(x)\\
&= 1+\int (kp_0(x)-p_1(x)) \psi(x)\1\{\phi(x)=1\} \d \mu(x)+\int (kp_0(x)-p_1(x))\psi(X)\1\{\phi(x)=0\} \d \mu(x)\\
&=1-\int |kp_0(x)-p_1(x)| \psi(x)\1\{\phi(x)=1\} \d \mu(x)+\int |kp_0(x)-p_1(x)|\psi(X)\1\{\phi(x)=0\} \d \mu(x)\\
&=1+\int |kp_0(x)-p_1(x)| \psi(x)(\1\{\phi(x)=0\}-\1\{\phi(x)=1\}) \d \mu(x)
\end{align*}
$$
The above is minimized by $\psi = \phi$.
#### Proof that $\psi=\phi$ is minimizer: we have because $\psi \ge 0$ 
$$\int |kp_0(x)-p_1(x)| \psi(x)(\1\{\phi(x)=0\}-\1\{\phi(x)=1\}) \d \mu(x) \ge -\int |kp_0(x)-p_1(x)| \psi(x)\1\{\phi(x)=1\} \d \mu(x)$$
and having that $\psi(x)\le 1$, we get
$$\int |kp_0(x)-p_1(x)| \psi(x)(\1\{\phi(x)=0\}-\1\{\phi(x)=1\}) \d \mu(x) \ge -\int |kp_0(x)-p_1(x)| \1\{\phi(x)=1\} \d \mu(x)$$
and this last value is exaclty equal to $\int |kp_0(x)-p_1(x)| \psi(x)(\1\{\phi(x)=0\}-\1\{\phi(x)=1\}) \d \mu(x)$ for $\psi=\phi$.
