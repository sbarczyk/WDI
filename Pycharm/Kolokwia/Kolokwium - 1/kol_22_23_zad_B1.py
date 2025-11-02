def spr(T):
    l = len(T)
    max_beg = -float('inf')
    min_end = float('inf')
    cur_seq = 1

    for i in range(1, l):
        if T[i - 1] < T[i]:
            cur_seq += 1
        elif cur_seq > 2:
            if T[i - 1] < min_end:
                min_end = T[i - 1]
            if T[i - cur_seq] > max_beg:
                max_beg = T[i - cur_seq]
            cur_seq = 1
        else:
            cur_seq = 1

    if cur_seq > 2:
        if T[l - 1] < min_end:
            min_end = T[l - 1]
        if T[l - cur_seq] > max_beg:
            max_beg = T[l - cur_seq]
        cur_seq = 1

    return max_beg > min_end


# Przykłady użycia:
T1 = [2, 15, 17, 13, 17, 19, 23, 2, 6, 4, 8, 3, 5, 7, 1, 3, 2]
T2 = [2, 15, 17, 13, 17, 19, 23, 2, 6, 4, 8, 3, 5, 7, 14, 3, 2]

print(spr(T1))  # Powinno zwrócić True
print(spr(T2))  # Powinno zwrócić False
