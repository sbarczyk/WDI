def check(n):
    counter = 0
    i = 2
    while n > 1:
        if n % i == 0:
            counter += 1
            if counter > 2:
                return False
            else:
                while n % i == 0:
                    n //= i
        i += 1
    if counter == 2:
        return True
    return False


def square(T):
    n = len(T)
    for a in range(2, n):
        for i in range(n-a+1):
            for j in range(n-a+1):
                if check(T[i][j]*T[i+a-1][j]*T[i][j+a-1]*T[i+a-1][j+a-1]):
                    return a
    return 0