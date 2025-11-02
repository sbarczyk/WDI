from random import randint

def print_tab(tab):
    for line in tab:
        print(line)
    print('---------')

def wypelnij(T,N):
    for i in range(N):
        for j in range(N):
            T[i][j]=randint(10,99)
    return T

def sum_of_sides(T, a, b):
    n = len(T)
    sides = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    total_sum = 0
    for k in sides:
        if 0 <= a + k[0] < n and 0 <= b + k[1] < n:
                total_sum += T[a + k[0]][b + k[1]]
    return total_sum

def zad(T):
    n = len(T)
    biggest_sum = 0
    big_a = 0
    big_b = 0

    for a in range(n):
        for b in range(n):
            current_sum = sum_of_sides(T, a, b)
            if current_sum > biggest_sum:
                biggest_sum = current_sum
                big_a = a
                big_b = b
    return biggest_sum, (big_a, big_b)


N=int(input("N: "))
Tab=[[0 for _ in range(N)] for _ in range(N)]
wypelnij(Tab,N)
print_tab(Tab)
print(zad(Tab))

