T = int(input())
 
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    flies = []
 
    for i in range(N):
        for j in range(N):
            fly = 0
            for k in range(M):
                for l in range(M):
                    ni = i + k
                    nj = j + l
                    if 0 <= ni < N and 0 <= nj < N:
                        fly += lst[ni][nj]
 
            flies.append(fly)
    result = max(flies)
 
    print(f'#{tc} {result}')