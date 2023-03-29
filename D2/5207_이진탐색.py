def binarySearch(arr, s, e, key):
    side = "c"  # center
    while s <= e:
        m = (s + e) // 2
        if arr[m] == key:
            return 1
        elif arr[m] > key:
            if side == "r":  # right side
                break
            e = m - 1
            side = "r"
        else:
            if side == "l":  # left side
                break
            s = m + 1
            side = "l"
    return 0


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    numA = sorted(list(map(int, input().split())))
    numB = list(map(int, input().split()))
    cnt = 0
    for b in numB:
        cnt += binarySearch(numA, 0, N-1, b)
    print(f'#{tc}', cnt)