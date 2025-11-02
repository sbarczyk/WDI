def sito(N):
    numbers = [True for _ in range(N)]
    length = len(numbers)
    for i in range (length):
        if i <= 1:
            numbers[i] = False
        else:
            if numbers[i]:
                print(i)
                for k in range (i, N+1, i):
                    numbers[k] = False

    exit(0)

print(sito(19))