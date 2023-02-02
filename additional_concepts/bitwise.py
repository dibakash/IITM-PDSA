from Performance import Performance
from statistics import mean

p = Performance()


def main():

    monte_carlo = 100
    modulo = []
    for _ in range(monte_carlo):
        p.start()
        for i in range(10000, 1000000):
            is_even_bitwise(i)
        p.stop()
        res = p.performance
        modulo.append(res)

    print("using bitwise", f"{mean(modulo):.4f}")

    for _ in range(monte_carlo):
        p.start()
        for i in range(10000, 1000000):
            is_even(i)
        p.stop()
        res = p.performance
        modulo.append(res)

    print("using modulo", f"{mean(modulo):.4f}")


def is_even_bitwise(n: int) -> bool:
    """check if a number is even or odd

    bitwise AND(~) operation used to determine if a number is even

    Args:
        n (int): integer

    Returns:
        bool: returns True if n is even else False
    """
    return n & 1 == 0


def is_even(n):
    """check if a number is even or odd using modulo

    Args:
        n (int): integer

    Returns:
        bool: returns True if n is even else False
    """

    return n % 2 == 0


if __name__ == "__main__":
    main()
