# 5188. 최소합
# DFS

def dfs(i, j):
    global tempSum, minSum
    if tempSum > minSum:
        return

    if i == N-1 and j == N-1:
        minSum = tempSum
        return

    for di, dj in [(0, 1), (1, 0)]:
        ni, nj = i+di, j+dj
        if 0<=ni<N and 0<=nj<N and (ni, nj) not in visited:
            visited.append((ni,nj))
            tempSum += numbers[ni][nj]
            dfs(ni,nj)
            visited.pop()
            tempSum -= numbers[ni][nj]


for tc in range(int(input())):
    N = int(input())
    numbers = [list(map(int, input().split())) for _ in range(N)]
    minSum = 10*N
    tempSum = numbers[0][0]  # 시작 값
    visited = []
    dfs(0,0)
    print(f'#{tc+1}', minSum)

