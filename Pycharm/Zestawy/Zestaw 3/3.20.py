MAX_NUMBER_VALUE = 1000
T = [2,23,33,35,7,4,6,7,5,11,13,22]

def najdluzszy_fragment(T):
    n = len(T)
    factors = [0] * 1001

    left, right = 0, 0
    max_len = 0
    while right < n:
        if max(factors) <= 1:
            copy_num = T[right]
            d = 2
            while copy_num != 1:
                while copy_num % d == 0:
                    factors[d] += 1
                    copy_num //= d
                d += 1
            right += 1

        else:
            copy_num = T[left]
            d = 2
            while copy_num != 1:
                while copy_num % d == 0:
                    factors[d] -= 1
                    copy_num //= d
                d += 1
            left += 1

        if max(factors) <= 1:
             max_len = right - left

    return max_len

print(najdluzszy_fragment(T))




