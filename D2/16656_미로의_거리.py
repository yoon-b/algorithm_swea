di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    maze = [[1] * (N+2)] + [[1] + list(map(int, input())) + [1] for _ in range(N)] + [[1] * (N+2)]
    visited = [[0] * (N+2) for _ in range(N+2)]
    si = sj = gi = gj = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if maze[i][j] == 2:
                queue = [(i, j)]
                visited[i][j] = 1
            elif maze[i][j] == 3:
                gi, gj = i, j

    while queue:
        ci, cj = queue.pop(0)

        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]
            if maze[ni][nj] != 1 and visited[ni][nj] == 0:
                queue.append((ni, nj))
                visited[ni][nj] = visited[ci][cj] + 1
                if maze[ni][nj] == 3:
                    break

    ans = visited[gi][gj]
    if ans > 0:
        ans -= 2
    print(f'#{tc}', ans)