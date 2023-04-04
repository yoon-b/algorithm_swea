from collections import deque


def bfs(si, sj):
    global usedEnergy
    queue = deque()
    queue.append((si, sj))
    usedEnergy[si][sj] = 0
    while queue:
        ci, cj = queue.popleft()
        for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            ni, nj = ci + di, cj + dj
            heightDiff = 0
            if 0 <= ni < N and 0 <= nj < N:
                if heights[ci][cj] < heights[ni][nj]:
                    heightDiff = heights[ni][nj] - heights[ci][cj]
                if usedEnergy[ni][nj] > usedEnergy[ci][cj] + heightDiff + 1:
                    usedEnergy[ni][nj] = usedEnergy[ci][cj] + heightDiff + 1
                    queue.append((ni, nj))


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    heights = [list(map(int, input().split())) for _ in range(N)]
    usedEnergy = [[1000000] * N for _ in range(N)]
    bfs(0, 0)
    answer = usedEnergy[N-1][N-1]
    print(f'#{tc}', answer)
