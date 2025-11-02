from math import isqrt


def is_prime(x):
    if x == 2 or x == 3:
        return True
    if x <= 1 or x % 2 == 0 or x % 3 == 0:
        return False
    for i in range(6, isqrt(x) + 1, 6):
        if x % (i - 1) == 0 or x % (i + 1) == 0:
            return False
    return True


def zad(x):
    def rek(x, res, flag, pos):
        results = []

        if x == 0:
            if res > 9 and is_prime(res) and flag:
                results.append(res)

        else:
            results.extend(rek(x // 10, res + ((x % 10) * 10 ** pos), flag, pos + 1))
            results.extend(rek(x // 10, res, True, pos))

        return results

    return rek(x, 0, False, 0)


result = zad(2137)
print(result)
