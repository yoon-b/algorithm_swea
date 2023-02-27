T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]
    maxFly = 0
    di1 = [0, 1, 0, -1]
    dj1 = [1, 0, -1, 0]
    di2 = [-1, 1, 1, -1]
    dj2 = [1, 1, -1, -1]

    for i in range(N):
        for j in range(N):
            fly1 = flies[i][j]
            fly2 = flies[i][j]
            for x in range(4):
                for m in range(1, M):
                    a = i + di1[x] * m
                    b = j + dj1[x] * m
                    c = i + di2[x] * m
                    d = j + dj2[x] * m

                    if 0 <= a < N and 0 <= b < N:
                        fly1 += flies[a][b]
                    if 0 <= c < N and 0 <= d < N:
                        fly2 += flies[c][d]
            if maxFly < max(fly1, fly2):
                maxFly = max(fly1, fly2)
    print(f'#{tc}', maxFly)