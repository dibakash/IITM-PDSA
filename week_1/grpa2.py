"""Goldbach's conjecture is one of the oldest and best-known unsolved problems in number theory.
It states that every even number greater than 2 is the sum of two prime numbers.

For Example:
12 = 5 + 7
26 = 3 + 23 or 7 + 19 or 13 + 13

Write a function Goldbach(n) where n is a positive even number ( n > 2) that return a list of tuples.
In each tuple (a, b) where a <= b, a and b should be prime numbers and the sum of  a and b should be equal to n

Sample input 1: 12
Sample output : [(5,7)]
Sample input 2: 26
Sample output : [(3,23),(7,19),(13,13)]
"""
def prime(n):
    if n < 2:
        return False
    if n in (2,3):
        return True

    result, i = True, 2

    while result and (i <= n**(1/2)):
        if n%i == 0:
            result = False
        i += 1

    return result


def Goldbach(n):
    res = []
    for i in range(2,n//2 + 1):
        if prime(i) and prime(n-i):
            res.append((i, n-i))
    return res



if __name__ == "__main__":
    n=int(input())
    print(sorted(Goldbach(n)))
