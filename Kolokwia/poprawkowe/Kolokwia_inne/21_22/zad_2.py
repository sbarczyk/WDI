def cztero_zgodne(a,b):
    digits = [False] * 4
    while a > 0:
        digits[a % 4] = True
        a //= 4
    
    while b > 0:
        digits[b % 4] = False
        b //= 4
            

    for i in range(len(digits)):
        if digits[i]:
            return False
    return True

print(cztero_zgodne(13,23))



