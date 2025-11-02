t = [2,9,3,1,7,11,9,6,7,7,1,3,9,12,15]
def zad(t):
    n = len(t)
    max_length = 0
    for left in range (n-1):
        if n - left + 1< max_length:
            break
        for right in range (n-1, -1, -1):
            if right - left + 1 < max_length:
                break
            if t[left] == t[right]:
                cnt = 1
                left += 1
                right -= 1
                while right >= left:
                    if t[right] == t[left]:
                        cnt += 1
                        left += 1
                        right -= 1
                    else:
                        break
                max_length = max(cnt, max_length)
    return max_length

print(zad(t))