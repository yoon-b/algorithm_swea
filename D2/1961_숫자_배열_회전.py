T = int(input())
 
for tc in range(1, T+1):
    N = int(input()) # 3<=N<=7
    target = [list(map(int, input().split())) for _ in range(N)]
    rlt90= [[0] * N for _ in range(N)]
    rlt180 = [[0] * N for _ in range(N)]
    rlt270 = [[0] * N for _ in range(N)]
 
    for i in range(N):
        for j in range(N):
            rlt90[i][j] = target[N-1-j][i]
    for i in range(N):
        for j in range(N):
            rlt180[i][j] = rlt90[N-1-j][i]
    for i in range(N):
        for j in range(N):
            rlt270[i][j] = rlt180[N-1-j][i]
 
    print(f'#{tc}')
    for i in range(N):
        print(''.join(map(str, rlt90[i])), end=' ')
        print(''.join(map(str, rlt180[i])), end=' ')
        print(''.join(map(str, rlt270[i])), end=' ')
        print()