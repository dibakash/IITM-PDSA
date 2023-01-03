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

![fx_bigO_of_gx](image/lecture_2/fx_bigO_of_gx.png)

![bigo](image/lecture_2/bigo.png)
