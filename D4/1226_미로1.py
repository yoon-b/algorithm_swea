for _ in range(10):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    escape = False
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                queue = [(i, j)]
                break

    while queue:
        ci, cj = queue.pop(0)
        maze[ci][cj] = 1
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = ci + di, cj + dj
            if maze[ni][nj] == 3:
                escape = True
                break
            if maze[ni][nj] == 0:
                queue.append((ni, nj))

    print(f'#{tc}', 1 if escape else 0)