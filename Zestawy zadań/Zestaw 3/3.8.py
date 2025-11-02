def check(tab):
    mask = [False] * len(tab)
    mask[0] = True
    for i, element in enumerate(tab):
        if mask[i]:
            div = 2
            while element != 1:
                while element % div == 0:
                    if i + div < len(tab):
                        mask[i + div] = True
                    element //= div
                div += 1
    return mask[-1]


tab = [6,1,5,2,4,3,9,6,1,2,4]
print(check(tab))


