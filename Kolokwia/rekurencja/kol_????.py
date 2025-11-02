def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def left_rock(T, x, y):
    n = len(T)

    if x == n - 1 and y == n - 1:
        return 0

    best_path = float('inf')

    for new_x in range(x + 1, len(T)):
        if nwd(T[y][x], T[y][new_x]) == 1:
            best_path = min(best_path, left_rock(T, new_x, y) + 1)

    for new_y in range(y + 1, len(T)):
        if nwd(T[y][x], T[new_y][x]) == 1:
            best_path = min(best_path, left_rock(T, x, new_y) + 1)

    return best_path


def right_rock(T, x, y):
    n = len(T)

    if x == 0 and y == n - 1:
        return 0

    best_path = float('inf')

    for new_x in range(x):
        if nwd(T[y][x], T[y][new_x]) == 1:
            best_path = min(best_path, left_rock(T, new_x, y) + 1)

    for new_y in range(y):
        if nwd(T[y][x], T[new_y][x]) == 1:
            best_path = min(best_path, left_rock(T, x, new_y) + 1)

    return best_path


def race(T):
    left_path = left_rock(T, 0, 0)
    right_path = right_rock(T, len(T)-1, 0)
    if left_path > right_path:
        return 1
    elif left_path < right_path:
        return 2
    else:
        return 0
