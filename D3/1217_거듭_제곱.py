exp_cache = dict()


def expo(a, b):  # exponentiation
    global exp_cache
    if b == 0:
        return 1

    if b in exp_cache:
        return exp_cache[b]
    else:
        result = expo(a, b-1) * a
        exp_cache[b] = result
        return result


for _ in range(10):
    tc = int(input())
    a, b = map(int, input().split())
    ans = expo(a, b)
    exp_cache = dict()
    print(f'#{tc} {ans}')