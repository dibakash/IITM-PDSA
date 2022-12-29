# Analysis of Algorithms

<!-- Notes maintained by: Dibakash Baruah -->

## What are we interested in when we are computing the performance of an Algorithm?

---

### Two main resources of Interest:

- Running time - how much time the Algorithm takes
- Space - memory requirements

### Time depends of Processing Power -

- Impossible to change for a given hardware
- Based on the present computing power of the CPUs ( last 10 / 15 years [this is 2022] ), Python can do around $10^7$ operations/ second.
- Enhancing hardware has only a limited impact at a practical level
- Meaning, even if we upgrade to a machine which is 10 times faster would not have any significant impact on something which is inherently long to compute.

### Storage is limited by Available Memory

- Easier to configure, augment

Because of this reason, when we talk about performance the focus is more on time rather than space aspect of performance

<br>

### Input Size

---

- Running time depends on input size. For example, a larger array takes more time to sort than a smaller array. We can think of time efficiency as a function of input size $n$ as running time $t(n)$
- Of course, different inputs of same input size $n$ may take different amounts of time. For example, two arrays of same size may take different amount of time to sort if one of them is already sorted and the other one is not.

---

## Why running time is important?

---

### Week 1 example:

---

Let's have a look at the following problem (sim card mapped to Aadhar card)

- Suppose there is need to verify Aadhar number associated with a mobile number so that a person can be verified.
- Assuming everyone have an Aadhar card in India (population of 100 Cr), there are around $10^9$ Aadhar cards. Similarly, assuming person having phones have multiple sim cards, there are around $10^9$ sim cards as well
- So, if we do a nested loop to check whether the Aadhar card provided is valid or not against the sim card provided we'll have to do $10^9 \times 10^9 = 10^{18}$
- with python, it will take:

  > $= 10^{18} / 10^7 = 10^{11}$ seconds!
  > <br> $\Rightarrow 10^{11} \div 60 \approx 1.67 \times 10^9$ mins
  > <br> $\Rightarrow 1.67 \times 10^9 \div 60 \approx 2.78 \times 10^7$ hours
  > <br> $\Rightarrow 2.78 \times 10^7 \div 24 \approx 1158333$ days
  > <br> $\approx 3200$ Years! ⌛🛸 🤣

So, we'll need 3200 years to verify whether correct Aadhar details is mapped to the sim card or not!

### What can be done so that the problem is manageable?

A common strategy is to use the divide and conquer approach (logarithmic) by dividing the problem statement in half in every step until a solution is obtained

- let's say we need to verify the Aadhar card associated with a given sim card.
- The best way is to do a binary search (divide and conquer) by halving the Aadhar data in each go (assuming the Aadhar numbers are in sorted order, which is a prerequisite for this to work).
- When we divide a data in half 10 times we reduce its size roughly by 1000 times (as $2^{10} = 1024$ ).
  > after halving 10 times, $10^9$ becomes $10^6$<br>
  > after halving 10 more times, $10^6$ becomes $10^3$<br>
  > after halving 10 more times, $10^3$ becomes $1$

$\therefore$ We'll require $10^9 \times 30$ computations with this approach which in terms of python will need $( 10^9 \times 30) / 10^7 = 3000 \space seconds = 50\space mins$. This is a huge improvement (obviously as compared to 3200 years) and is just a work of around 1 hour to carry out the needed verification amongst a population of 1 billion.

This is basically tells us about importance of running time of an algorithm.

> - The halving of the operations in terms of mathematics can be thought of as $\log _2n = k \Rightarrow  2^k = n$. The $\log _2n$ is nothing but number of time we need to divide $n$ by $2$ to reach $1$ or number of times we need to multiply $2$ to reach $n$.<br>
> - In terms of programming while representing time complexities, in general we write $\log _2n$ as $\log n$ (omitting the base 2).<br>
> - Specifically, we reduced the the running time of the above operation from $n^2$ (naive algorithm) to $n\log n$ and we can already see how $n\log n$ is way better than $n^2$.

---

### Example 2: Video Game

---

Let's imagine a hypothetical video game where there are several objects on the screen that can attack the each other based on the closest distance.

So, the task is to find the closest pairs of objects. One can think of a naive algorithm (brute force approach) that has running time of $n^2$. More precisely, we need to compare $n$ objects to $(n-1)$ objects and divide it by 2 as we don't need distance from both directions. So, number of comparisons needed:

$$\frac{n(n-1)}{2} = \frac{n^2 -n }{2}\sim n^2$$

<div style="text-align:center;">(asymptotically equivalent to <code>n<sup>2</sup></code> )</div>

Let's say there exist a clever algorithm that takes time $n\log n$

What would be the impact of the naive algorithm and the clever algorithm on running time for this problem?

> A High resolution gaming console may have $4000 \times 2000$ pixels, which in other words $8 \times 10^6 = 8$ million points.
>
> - Suppose we have $100,000 = 10^5$ objects
> - Naive Algorithm takes $n^2$ i.e. $10^{10}$ steps
> - In python this means $1000$ seconds or $16.7$ minutes.
> - Even a ten time faster programming language it will take $1.67$ mins which is unacceptable response time and which is why an $n^2$ algorithm will be useless in this scenario.

What happens with $n \log n$ algorithm?

> Some intuition building maths:
>
> - $\log _2 100,000$ is under $20$
> - as, $2^{10} = 1024 \approx 10^3 \Rightarrow 2^{20} \approx 10^6$
> - $\Rightarrow 2^{19} \approx 5.something \times 10^5$
> - $\log _2 100000$ is certainly less than $20$
>
> Another way we can think is:
>
> - $\log _2 100,000 = \log 10^5 = 5 \cdot\log10 \approx 5 \times 3.something << 20$
>
> So, total operations this program will need to perform is:
>
> - $20 \times 10^5 = 2\times 10^6$
> - So, even in python this will need $0.2$ seconds to run and with some faster programming language like <code>C++</code> we can further reduce the time to numbers like $0.02$ seconds which is much faster than human reaction time which is typically 0.2 seconds.

This was another example of why designing an algorithm that goes from $n^2$ to $n\log n$ can make a huge impact on how useful that algorithm is in practice.

---

## Getting into Technical Aspects - Orders of Magnitude

### How do we actually evaluate and compare different algorithms formally? We need a way to compute these and compare these

---

The first thing is we'll always be interested in comparing the functions $t(n)$ but while doing so we will be interested in $t(n)$ up to some magnitude. In other words, we will-

> Ignore the constant factors

For instance, we know that $n^3 > n^2$ is always $\forall \space n \in \set{ +ve \space integers }$ . But what happens when we stick a constant, say 5000 in front of $n^2$ i.e $5000 n^2$
