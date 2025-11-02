T = [1, 7, 3, 5, 11, 2]


def zad6(T):
    n = len(T)

    def rek(i, sum_of_el, sum_of_ind):
        if sum_of_el == sum_of_ind and sum_of_el != 0:
            return sum_of_el
        elif i == n:
            return None

        return rek(i + 1, sum_of_el, sum_of_ind) or rek(i + 1, sum_of_el + T[i], sum_of_ind + i)

    return rek(0, 0, 0)


print(zad6(T))
