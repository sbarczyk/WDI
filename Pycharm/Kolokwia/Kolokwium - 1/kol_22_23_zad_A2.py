def check(a, b, c):
    return c == a + b - 1


def in_seq(a, b):
    while a > 1:
        z = b - a + 1
        b, a = a, z
    return a == 1 and b == 2


def find(T):
    l = len(T)
    x = l - 3
    y = 0
    while x > 0:
        counter = 0
        for i in range(l - x - 2):
            if check(T[i + x][y + i], T[i + x + 1][y + i + 1], T[i + x + 2][y + i + 2]):
                counter = 3 if counter == 0 else counter + 1
            else:
                if counter > 0 and in_seq(T[i + x - counter + 3][y + i - counter + 3],
                                          T[i + x - counter + 4][y + i - counter + 4]):
                    return counter
                counter = 0
        if counter > 0 and in_seq(T[i + x - counter + 3][y + i - counter + 3],
                                  T[i + x - counter + 4][y + i - counter + 4]):
            return counter
        counter = 0
        x -= 1

    while y <= l - 3:
        counter = 0
        for i in range(l - y - 2):
            if check(T[i + x][y + i], T[i + x + 1][y + i + 1], T[i + x + 2][y + i + 2]):
                counter = 3 if counter == 0 else counter + 1
            else:
                if counter > 0 and in_seq(T[i + x - counter + 3][y + i - counter + 3],
                                          T[i + x - counter + 4][y + i - counter + 4]):
                    return counter
                counter = 0
        if counter > 0 and in_seq(T[i + x - counter + 3][y + i - counter + 3],
                                  T[i + x - counter + 4][y + i - counter + 4]):
            return counter
        counter = 0
        y += 1

    return 0


T = [[0, 0, 0, 0, 2, 2, 0, 0],
     [0, 0, 0, 0, 0, 2, 2, 0],
     [0, 0, 0, 4, 0, 0, 3, 3],
     [0, 6, 0, 0, 4, 0, 0, 0],
     [0, 0, 9, 0, 0, 7, 0, 0],
     [0, 0, 0, 14, 0, 0, 10, 0],
     [0, 0, 0, 0, 22, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     ]

print(find(T))
