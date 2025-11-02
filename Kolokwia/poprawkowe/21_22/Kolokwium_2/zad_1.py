""" Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę zaimplementować funkcję
trojki(T), która zlicza wszystkie trójki liczb, które spełniają następujące warunki:
(1) Największym wspólnym dzielnikiem trzech liczb jest liczba 1,
(2) W każdej trójce dwie dowolne liczby leżą w róznych wierszach i różnych kolumnach.
Funkcja powinna zwrócić liczbę znalezionych trójek. """

def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
    

def trojki(T):
    n = len(T)
    wykorzystane_kolumny = [False] * 8
    wykorzystane_wiersze = [False] * 8
    cnt = 0
    for x1 in range(n):
        wykorzystane_kolumny[x1] = True
        for y1 in range(n):
            wykorzystane_wiersze[y1] = True
            for x2 in range(n):
                if wykorzystane_kolumny[x2]:
                    continue
                wykorzystane_kolumny[x2] = True
                for y2 in range(n):
                    if wykorzystane_wiersze[y2]:
                        continue
                    wykorzystane_wiersze[y2] = True
                    for x3 in range(n):
                        if wykorzystane_kolumny[x3]:
                            continue
                        for y3 in range(n):
                            if wykorzystane_wiersze[y3]:
                                continue
                            if nwd(nwd(T[x1][y1], T[x2][y2]), T[x3][y3]) == 1:
                                cnt += 1
                    wykorzystane_wiersze[y2] = False

                wykorzystane_kolumny[x2] = False

            wykorzystane_wiersze[y1] = False

        wykorzystane_kolumny[x1] = False
    return cnt // 6


example_array = [
    [1, 2, 3, 4, 5, 6, 7, 8],
    [9, 10, 11, 12, 13, 14, 15, 16],
    [17, 18, 19, 20, 21, 22, 23, 24],
    [25, 26, 27, 28, 29, 30, 31, 32],
    [33, 34, 35, 36, 37, 38, 39, 40],
    [41, 42, 43, 44, 45, 46, 47, 48],
    [49, 50, 51, 52, 53, 54, 55, 56],
    [57, 58, 59, 60, 61, 62, 63, 64]
]

print(trojki(example_array))

