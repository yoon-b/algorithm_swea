T = int(input())

for tc in range(1, T+1):
    N = int(input())
    start, end = 1, N
    ans = -1

    while start <= end:
        middle = (start + end) // 2
        if N == middle**3:
            ans = middle
            break
        elif N < middle**3:
            end = middle - 1
        else:
            start = middle + 1

    print(f'#{tc}', ans)