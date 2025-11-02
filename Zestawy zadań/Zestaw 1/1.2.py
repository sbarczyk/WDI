def zad2(target):
    resA = 0
    resB = 0
    best_sum = target
    for a in range(1, int(target+2)):
        for b in range(1, int(target+2)):
            prev = a
            curr = b
            while prev + curr < target + 2:
                next_term = prev + curr
                if prev + curr == target:
                    if a + b < best_sum:
                        best_sum = a + b
                        resA = a
                        resB = b
                prev, curr = curr, next_term
    return resA, resB

print(zad2(2023))
