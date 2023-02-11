T = int(input())
 
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    confetti = []
    di = [0, 0, 1, 0, -1] # 중앙, 우, 하, 좌, 상
    dj = [0, 1, 0, -1, 0]
 
    for i in range(N):
        for j in range(M):
            conf = 0
            for k in range(5):
                ni, nj = i + di[k], j + dj[k]
                if 0 <= ni < N and 0 <= nj < M:
                    conf += lst[ni][nj]
 
            confetti.append(conf)
    result = max(confetti)
 
    print(f'#{tc} {result}')