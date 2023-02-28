T = int(input())

for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int, list(input())))for _ in range(N)]
    c = N//2  # center
    harvest = 0
    for i in range(N):
        for j in range(N):
            if abs(i-c) + abs(j-c) <= c:
                harvest += farm[i][j]
    print(f'#{tc}', harvest)