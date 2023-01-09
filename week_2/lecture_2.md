# Comparing Orders of Magnitude

<!-- Notes maintained by: Dibakash Baruah -->

How do we compare functions with respect to orders of magnitude

In order to compare one function against another function we have a notion called upper bound.

---

## Upper Bound (Big O of a function)

---

- $f(x)$ is said to $O(g(x))$ if we can find constants $c$ and $x_0$ such that $c \cdot g(x)$ is an upper bound for $f(x)$ beyond $x_o$

  > $f(x)$ is said to $O(g(x))$ ( Big O of g(x) ) if in some sense the function $g(x)$ sits above $f(x)$. Now, as we are ignoring constants, (and order of magnitude is what matters to us ) we are allowed to make $g(x)$ sit above $f(x)$ by multiplying g(x) by some suitable constants.
  >
  > This might not happen for small values of $n$ as in the case of $n^3 >, =, < 5000.n^2$.
  >
  > So, basically we need to find out two values $x_o$ and $c$ such that if we go beyond $x_o$ then $f(x)$ is below $c \cdot g(x)$

- Mathematically it can be represented as,
  > $f(x)\le c.g(x), \space \forall  \space x \ge x_o$

<figure>
  <img src = "image/lecture_2/fx_bigO_of_gx.png" alt="comparing two graphs"></img>
  <figcaption>fig 1. upper bound of a graphs</figcaption>
</figure>

<br>

Here are some graphs that we discussed before. both $\log n$ and $\sqrt n$ doesn't grow very fast. Here we can say $\sqrt n$ is an upper bound for $\log n$

<figure>
  <img src = "image/lecture_2/bigo.png" alt="comparing two graphs"></img>
  <figcaption>fig 2. BigO comparison</figcaption>
</figure>

For small value of $n$, $n\log n$ looks like it is closer to $n^2$ like the above image however we can observe that it is actually much closer to $O(n)$ than it is to $O(n^2)$ as n approaches some large value as shown in the fig. 3 below.

<figure>
  <img src = "image/lecture_2/bigo_large_n.png" alt="bigo comparison with large n"></img>
  <figcaption>fig. 3: BigO comparison with large n</figcaption>
</figure>

As discussed before (fig. 1), to show that something is BigO of a function say $f(x)$ formally, we have to find out $c$ and $x_o$ and demonstrate $f(x)\le c.g(x), \space \forall  \space x \ge x_o$

---

### Examples

---

- Finding $BigO$ of $100n + 5$

  > - $100n + 5 \le 100n + n,\ \ \ \ \forall \space n \ge 5$
  >
  > - $\Rightarrow 100n + 5 \le 101n,\ \ \ \ \forall \space n \ge 5$
  >
  > now,
  >
  > - $101n \le 101n^2, \ \ \ \ \forall \ n \in \set{ +ve \space integers }$ ...(in this example it holds true even for negative integers). Note that $n$ is always $+ve$ as input size is non negative.
  >
  > - let, $f(n) = 100n + 5$ and $g(n) = n^2$
  >
  > - $101n^2$ is of the form $c \cdot g(x)$
  >
  > So, we found $c$ as $101$ and for the lower bound of $n$ for which $100n+5 \le 101n \le c \cdot g(n)$, i.e. $f(n) \le c \cdot g(n)$ holds true is 5. So, $x_o$ is $5$.
  >
  > $\therefore 100n + 5$ is $BigO(n^2)$

  > Alternatively,
  >
  > - $100n + 5 \le 100n + 5n = 105n, \ \ \ \ \forall \ n \ge 1$
  >
  > - now, $105n \le 105n^2$
  >
  > - $105n^2$ is of the form $c \cdot g(x)$
  >
  > - choose $n_o = 1$, $c=105$
  >
  > So, we found $c=105$ and $n_o = 5 $ for which $100n+5 \le 105n \le c \cdot g(n)$, i.e. $f(n) \le c \cdot g(n)$ holds true.
  >
  > Therefore, $100n + 5$ is $BigO(n^2)$
  >
  > - Choice of $c$ and $n_o$ is not unique

<br>

- Finding $BigO$ of $100n^2 + 20n+ 5$

  > let, $f(n) = 100n^2 + 20n+ 5$
  >
  > - $100n^2 + 20n+ 5 \le 100n^2 + 20n^2+ 5n^2, \ \ \ \ \forall \ n \ge 1$
  >
  > - $100n^2 + 20n+ 5 \le 125n^2$
  >
  > - let, $g(n) = n^2$
  >
  > - Choose $n_o = 1$ and $c=125$
  >
  > - So, $f(n) \le g(n), \ \ \ \ \forall \ n \ge n_o$
  >
  > - Hence, $100n^2 + 20n+ 5$ is $O(n^2)$

- So, what really matters is the highest term

  - $20n + 5$ is dominated by $100n^2$

- $\underline{n^3 \text{ is not } O(n^2)}$
  - No matter what $c$ we choose, $cn^2$ will be dominated by $n^3$ for $n \ge c$

---

### Useful Properties

---

- if $f_1(n)$ is $O(g_1(n))$ and $f_2(n)$ is $O(g_2(n))$, then $f_1(n) + f_2(n)$ is $O(max(g_1(n),g_2(n)))$
  > Proof
  >
  > $f_1(n) \le c_1 \cdot g_1(n), \ \ \ \forall n \ge n_1$
  >
  > $f_2(n) \le c_2 \cdot g_2(n), \ \ \ \forall n \ge n_2$
  >
  > Let, $c = max(c_1, c_2)$, $n_3 = max(n_1, n_2)$
  >
  > So, for $n \ge n_3$,
  >
  > $f_1(n) + f_2(n) \le c_1 \cdot g_1(n) + c_2 \cdot g_2(n)$
  >
  > $\Rightarrow f_1(n) + f_2(n) \le c_3 \cdot g_1(n) + c_3 \cdot g_2(n)$
  >
  > $\Rightarrow f_1(n) + f_2(n) \le c_3 ( g_1(n) + g_2(n))$
  >
  > $\Rightarrow f_1(n) + f_2(n) \le 2c_3 \cdot  max( g_1(n), g_2(n))$
  >
  > $\therefore f_1(n) + f_2(n)$ is $O(max(g_1(n),g_2(n)))$

In other words, if a problem has two phases e.g. the Aadhar Card example,

- Phase A (e.g. Sorting Aadhar cards) takes time $O(g_A(n))$

- Phase B (e.g. searching) takes time $O(g_B(n))$

- The algorithm as a whole takes time: $max(O(g_A(n)), O(g_B(n)))$

- i.e. the least efficient phase will dominate the running time and is the bottleneck and $\text {upper bound}$ for the whole algorithm.

---

## Lower Bound (Omega of a function)

---

$f(x)$ is said to be $\Omega (g(x))$, if we find constants $c$ and $x_o$ such that $c \cdot g(x)$ is a lower bound for $f(x)$ for $x$ beyond $x_o$

> $f(x)\ge c.g(x), \space \forall  \space x \ge x_o$

e.g. $n^3$ is $\Omega (n^2)$ as $n^3 \ge n^2$ for all $n$. So, $n_0 = 1, c = 1$

### Typically we establish lower bounds for a problem rather than an individual algorithm

Lower bound of an algorithm is the minimum number of steps that an algorithm must take in order to solve a problem of a certain size.

It is not something that is determined for an individual algorithm, but rather it is a property of the problem itself. In other words, it is the minimum amount of work that must be done in order to solve the problem, regardless of the specific algorithm being used. In other words, it represents the inherent difficulty of the problem, and no matter which algorithm is used, it will always take at least this many steps to solve the problem.

- For example, suppose we have a problem that requires us to compare every element in an array with every other element in order to find a certain pattern. In this case, the lower bound of the problem would be $n^2$, because no matter which algorithm we use, we will always have to do at least $n^2$ comparisons in order to solve the problem. Even if we use a more efficient algorithm that is able to solve the problem in fewer than $n^2$ steps, the lower bound will still be $\Omega (n^2)$ because that is the minimum number of steps required to solve the problem.

- Similarly, searching for an element in an unsorted array that is not present in the array will have a lower bound of size of the array as regardless of algorithm used we have to look into every element for the array

- If we sort a list by comparing elements and swapping them (i.e. comparing and rearranging), we require $\Omega (n\log n)$ comparisons

- This is independent of the algorithm we use for sorting

> Note:
>
> The upper bound of an algorithm, also known as its worst-case time complexity, is a measure of the maximum amount of time that the algorithm will take to solve a problem of a given size. Like the lower bound, it is a property of the problem rather than the specific algorithm being used. However, it is possible for different algorithms to have different upper bounds for the same problem, depending on how efficiently they are able to solve it. For example, one algorithm might have an upper bound of O(n^2) for a particular problem, while another algorithm might have an upper bound of O(n log n) for the same problem. The upper bound is important because it helps to determine the feasibility of an algorithm for solving a given problem, as well as its potential performance characteristics.
