from math import sqrt
def dzielniki(num):
    if num == 0:
        return "Wszystkie liczby poza 0"
    for i in range (1, int(sqrt(num))+1):
        if num%i == 0:
            if num == i*i:
                print (i)
            else:
                print(i, num//i)
    exit(0)
print(podzielniki(4556))
