di = [0, 1, 0, -1] # 우, 하, 좌, 상
dj = [1, 0, -1, 0]
 
 
for tc in range(1, 11):
    N = int(input())
    lst = [list(map(int, input().split())) for i in range(N)]
 
    total = 0
    for i in range(N):
        for j in range(N):
            sum_sub = 0
            for k in range(4):
                ni, nj = i + di[k], j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    sub = lst[ni][nj] - lst[i][j]
                    abs_sub = sub if sub >= 0 else -sub
                    sum_sub += abs_sub
            total += sum_sub
    print(f'#{tc} {total}')