# Live Coding Problem 1
"""
A positive integer `m` is a prime product if it can be written as `p* q`, where `p` and `q` are both primes. .

Write a Python function prime_product(m) that takes an integer `m` as input and returns `True` if `m` is a prime product and `False` otherwise. (If `m` is not positive, function should return `False`.)

Sample Input
6

Output
True
"""


def prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    res, i = True, 2
    while res and (i <= n**0.5):
        if n % i == 0:
            res = False
        i += 1
    return res


def prime_product(m):
    found = False
    for i in range(1, m // 2 + 1):
        if prime(i):
            for j in range(m // 2, 1, -1):
                if prime(j) and i * j == m:
                    found = True
                if found:
                    break
        if found:
            break
    return found


if __name__ == "__main__":
    # Suffix Code
    n = int(input())
    print(prime_product(n))
