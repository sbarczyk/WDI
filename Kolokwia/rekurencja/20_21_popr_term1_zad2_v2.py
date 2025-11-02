def czy_samogloska(ch):
    return ch in ['a', 'e', 'o', 'u', 'i', 'y']


def cutting(s):
    n = len(s)

    def rek(i, cnt):
        if i == n:
            if cnt == 1:
                return 1
            else:
                return 0

        if czy_samogloska(s[i]):
            cnt += 1

        if cnt == 2:
            return 0

        if cnt == 1:
            return rek(i + 1, 0) + rek(i + 1, 1)

        return rek(i+1, 0)

    return rek(0, 0)


print(cutting('student'))
print(cutting('sesja'))
print(cutting('informatyka'))
