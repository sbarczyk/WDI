
def steps(A):
    counter = 0
    while A != 1:
        counter += 1
        A = (A % 2) * (3 * A + 1) + (1 - A % 2) * A / 2
    return counter

def zad16():
    max_steps = 0
    max_start = None
    for i in range (2, 10000+1):
        if steps(i) > max_steps:
            max_steps = steps(i)
            max_start = i
    print("Liczba krokow: " + str(max_steps))
    print("Wyraz początkowy: " + str(max_start))

zad16()