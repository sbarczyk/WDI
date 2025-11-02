from math import sqrt
def sum_of_div(num):
    sum = 1
    for i in range (2, int(sqrt(num))+1):
        if num % i == 0:
            if num == i ** i:
                sum += i
            else:
                sum += (i+(num//i))
    return sum

def zad():
    for num in range(2, 1000000):
        if sum_of_div(num) == num:
            print(num)
    exit(0)

zad()
