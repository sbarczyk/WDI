from math import sqrt
def czy_pierwsza(x):
    if x == 2 or x == 3:
        return True
    if x <= 1 or x % 2 == 0 or x % 3 == 0:
        return False
    for i in range (6, int(sqrt(x))+1, 6):
        if x % (i-1) == 0 or x % (i+1) == 0:
            return False
    return True

def create_sum(t1, t2, mask):
    suma = 0
    counter = 0

    for i in range(len(t1)):
        if mask % 3 == 0:
            suma += t1[i]
        elif mask % 3 == 1:
            suma += t2[i]
        elif mask % 3 == 2:
            suma += t1[i] + t2[i]
        mask //= 3
    return suma

def maska(t1,t2):
    counter = 0
    for mask in range (3**len(t1)):
        if czy_pierwsza(create_sum(t1,t2,mask)):
            counter += 1
    return counter

t1 = [1,3,2,4]
t2 = [9,7,4,8]
print(maska(t1,t2))

