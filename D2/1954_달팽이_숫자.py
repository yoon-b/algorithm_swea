di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
 
T = int(input())
 
for tc in range(1, T+1):
    N = int(input())
    snail = [[0] * N for _ in range(N)]
    dIdx = 0
    i = 0
    j = 0
    for num in range(1, N*N+1):
        snail[i][j] = num
        ni, nj = i + di[dIdx], j + dj[dIdx]
        if 0<=ni<N and 0<=nj<N and snail[ni][nj] == 0:
            i = ni
            j = nj
        else:
            dIdx = (dIdx + 1) % 4
            i, j = i + di[dIdx], j + dj[dIdx]
 
    print(f'#{tc}')
 
    for a in range(N):
        for b in range(N):
            print(snail[a][b], end=' ')
        print()