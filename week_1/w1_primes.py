def prime(n):
    if n in (0, 1):
        return False
    if n in (2, 3):
        return True

    result, i = True, 2
    while result and (i <= n ** (1 / 2)):
        if n % i == 0:
            result = False
        i += 1
    return result
