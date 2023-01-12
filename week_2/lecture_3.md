# Calculating Complexity - Examples

<!-- Notes maintained by: Dibakash Baruah -->

Typically there will be two types of code that we look at.

- **Iterative Programs**
- **Recursive Programs**

## Iterative Programs Example

---

Example 1: Find the maximum element in a list:

- The input size is the length of the list
- Single loop scans all elements
- Always takes n steps
- Overall time is $O(n)$

This has worst-case $O(n)$ but in some sense it is in every case $O(n)$

```
def maxElement(L):
    """Finds the maximum element in a list
    Args:
        L (list): list of elements

    Returns:
        int: max element in the list
    """
    maxval = L[0]
    for i in range(len(L)):
        if L[i] > maxval:
            maxval = L[i]
    return maxval
```

<br>

Example 2: Check whether a list contains duplicates:

- The input size is the length of the list
- Nested loops scan all the pairs of elements
- A duplicate may be found in the very first iteration (best scenario)
- Worst case - no duplicates. In other words, both loops run fully
- Time is $(n-1)+(n-2)+...+1 = {n(n-1)\over 2}$
- Overall time is $n^2$.
- (We are looking at the worst-case)

```
def noDuplicates(L):
    """Check whether a list contains duplicates

    Args:
        L (list): list
    """
    for i in range(len(L)-1):
        for j in range(i+1,len(L)):
            if L[i] == L[j]:
                return True
    return False

```

<br>

Example 3: Matrix Multiplication

- Matrix is represented as a list of lists

  - $$
    \begin{bmatrix}
    1&2&3\\
    4&5&6
    \end{bmatrix}
    $$
  - $$[[1,2,3],[4,5,6]]$$

- Input matrices have size $m\times n, n\times p$

- Output matrices have size $m \times p$
- Three nested loops
- Overall time is $O(mnp)$, and $O(n^3)$ if both matrices are $n \times n$
