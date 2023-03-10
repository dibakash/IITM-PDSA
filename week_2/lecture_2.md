# Comparing Orders of Magnitude

<!-- Notes maintained by: Dibakash Baruah -->

How do we compare functions concerning orders of magnitude?

To compare one function against another function we have a notion called the upper bound.

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
  <figcaption>fig 1. upper bound of a graph</figcaption>
</figure>

<br>

Here are some graphs that we discussed before. both $\log n$ and $\sqrt n$ doesn't grow very fast. Here we can say $\sqrt n$ is an upper bound for $\log n$

<figure>
  <img src = "image/lecture_2/bigo.png" alt="comparing two graphs"></img>
  <figcaption>fig 2. BigO comparison</figcaption>
</figure>

For a small value of $n$, $n\log n$ looks like it is closer to $n^2$ like the above image however we can observe that it is much closer to $O(n)$ than it is to $O(n^2)$ as n approaches some large value as shown in the fig. 3 below.

<figure>
  <img src = "image/lecture_2/bigo_large_n.png" alt="BigO comparison with large n"></img>
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
  > So, we found $c=105$ and $n_o = 5$ for which $100n+5 \le 105n \le c \cdot g(n)$, i.e. $f(n) \le c \cdot g(n)$ holds true.
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

- So, what matters is the highest term

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

The lower bound of an algorithm is the minimum number of steps that an algorithm must take to solve a problem of a certain size.

It is not something that is determined for an individual algorithm, but rather it is a property of the problem itself. In other words, it is the minimum amount of work that must be done to solve the problem, regardless of the specific algorithm being used. In other words, it represents the inherent difficulty of the problem, and no matter which algorithm is used, it will always take at least this many steps to solve the problem.

- For example, suppose we have a problem that requires us to compare every element in an array with every other element to find a certain pattern. In this case, the lower bound of the problem would be $n^2$, because no matter which algorithm we use, we will always have to do at least $n^2$ comparisons to solve the problem. Even if we use a more efficient algorithm that can solve the problem in fewer than $n^2$ steps, the lower bound will still be $\Omega (n^2)$ because that is the minimum number of steps required to solve the problem.

- Similarly, searching for an element in an unsorted array that is not present in the array will have a lower bound of the size of the array as regardless of the algorithm used we have to look into every element for the array

- If we sort a list by comparing elements and swapping them (i.e. comparing and rearranging), we require $\Omega (n\log n)$ comparisons

- This is independent of the algorithm we use for sorting

> Note:
>
> In general, both $Big O$ and $Omega$ notation are used to describe the upper and lower bounds of an algorithm's time complexity, respectively.
>
> $Big O$ notation is usually used to describe the worst-case time complexity of an algorithm, which represents an upper bound on the amount of time the algorithm will take to solve a problem as the size of its inputs grows. It's commonly used to describe the scalability of an algorithm, so it's often considered to be a property of the algorithm's implementation.
>
> Omega $(\Omega)$ notation, on the other hand, is used to describe the best-case time complexity of an algorithm, which represents a lower bound on the amount of time the algorithm will take to solve a problem. It's used to describe the minimum amount of time an algorithm will take, so it's often considered to be a property of the problem, not the implementation.
>
> In either case, the notation provides a way to describe and compare the time complexity of algorithms, which is useful for selecting the most appropriate algorithm for a given problem and understanding how the running time of an algorithm will grow as the size of its inputs grows.

---

## Tight Bounds

---

$f(x)$ is said to be $\Theta(g(x))$ if it is both $O(g(x))$ and $\Omega(g(x))$

> find constants $c_1, c_2, x_o$ such that $c_1 \cdot g(x) \le f(x) \le c_2 \cdot g(x), \ \ \ \space \forall \ x >x_o$

Example: Show that $n(n-1) \over 2$ is $\Theta(n^2)$

- Upper bound:

  > ${n(n-1)\over 2} ={n^2 \over 2}-{n \over 2} \le {1\over 2}n^2, \ \ \forall n \ge 0$

- Lower bound:
  > ${n(n-1)\over 2} ={n^2 \over 2}-{n \over 2} \ge {n^2\over 2}-({n \over 2} \times {n \over 2}) \ge {n^2 \over 4}, \ \ \forall n \ge 2$
- Choose $n_o = 2, c_1 = {1 \over 4}, c_2= {1 \over 2}$

- So, ${1 \over 4} n^2 \le {n(n-1)\over 2} \le {1 \over 2} n^2$

Note:

> Tight bounds refer to bounds on an algorithm's performance that are as close as possible to the actual performance of the algorithm. For example, if an algorithm has a time complexity of $O(n^2)$, and its performance closely matches this bound for a wide range of input sizes, we say that the bound is tight. On the other hand, if an algorithm has a time complexity of $O(n^2)$ but its actual performance is much worse than this bound for a given input size, we say that the bound is not tight.
>
> Tight bounds are important because they give us a better understanding of an algorithm's actual performance characteristics. If the bounds on an algorithm's performance are not tight, it can be difficult to predict how well the algorithm will perform on different inputs, making it harder to choose the best algorithm for a given problem. On the other hand, if the bounds are tight, we can have more confidence in our predictions about the algorithm's performance, and we can more accurately compare the relative performance of different algorithms for a given problem.

## Summary

- $f(n)$ is $O(g(n))$ means $g(n)$ is an upper bound for $f(n)$

  - Useful to describe asymptotic worst-case running time

- $f(n)$ is $\Omega (g(n))$ means $g(n)$ is a lower bound for $f(n)$
  - Typically used for a problem as a whole, rather than an individual algorithm
- $f(n)$ is $\Theta (g(n))$ : matching upper and lower bounds
  - We have found an optimal algorithm for a problem.
