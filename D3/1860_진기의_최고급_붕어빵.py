T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    customer = [0] + sorted(list(map(int, input().split())))
    isPossible = True
    for i in range(1, N+1):
        if (customer[i]//M) * K < i:
            isPossible = False
            break
    ans = "Possible" if isPossible else "Impossible"
    print(f'#{tc}', ans)
