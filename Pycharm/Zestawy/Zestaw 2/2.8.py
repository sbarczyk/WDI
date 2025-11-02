def is_in_fibo(n):
    a1, a2, b1, b2 = 1, 1, 1, 1
    sum = 0
    while sum < n:
        sum += a1
        a1, a2 = a2, a1 + a2

    while sum > n:
        sum -= b1
        b1, b2 = b2, b1 + b2

    return(sum == n)

def next_not_in(n):
    n += 1
    while True:
        if is_in_fibo(n):
            n += 1
        else:
            return n

n = int(input())
print(next_not_in(n))
