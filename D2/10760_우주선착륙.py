di = [0, 1, 1, 1, 0, -1, -1, -1]
dj = [1, 1, 0, -1, -1, -1, 0, 1]


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    district = [list(map(int, input().split())) for _ in range(N)]
    candidate = 0
    for i in range(N):
        for j in range(M):
            cnt = 0
            for d in range(8):
                ni, nj = i + di[d], j + dj[d]
                if 0 <= ni < N and 0 <= nj < M and district[ni][nj] < district[i][j]:
                    cnt += 1
                    if cnt >= 4:
                        candidate += 1
                        break
    print(f'#{tc}', candidate)

