from math import isqrt

def is_prime(x):
    
    if x == 2 or x == 3:
        return True
    if x <= 1 or x % 2 == 0 or x % 3 == 0:
        return False
    for i in range(6, isqrt(x) + 1, 6):
        if x % (i-1) == 0 or x % (i+1) == 0:
            return False
    return True



def komnaty(T):
    
    def rek(i, sztabki):
        if i == len(T) - 1:
            if T[i] + sztabki <= 100 and is_prime(T[i] + sztabki):
                return True
            return False
        
        # x - ilość sztabek, które ZOSTAWIAMY w i-tej komnacie
        for x in range(sztabki - 6, sztabki +1):
            if T[i] + x <= 100 and is_prime(T[i] + x):
                if rek(i+1, sztabki - x):
                    return True
        return False
    
    return rek(0, 0)

T = [10, 20, 30]
print(komnaty(T))