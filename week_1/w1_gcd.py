import modules
from performance import Performance

a = Performance()


def gcd_a(a, b):
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            mrcf = i

    return mrcf


a.start()
print(gcd_a(1000222, 4212312))
a.stop()
print(a.performance)


def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)


a.start()
print(gcd(1000222, 4212312))
a.stop()
print(a.performance)
