def dfs(n, ci, cj, temp):
    if n == 7:
        result.add(temp)
        return

    for di, dj in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
        ni, nj = ci + di, cj + dj
        if 0 <= ni < 4 and 0 <= nj < 4:
            dfs(n+1, ni, nj, temp+board[ni][nj])


T = int(input())
for tc in range(1, T + 1):
    board = [input().split() for _ in range(4)]
    result = set()

    for i in range(4):
        for j in range(4):
            dfs(1, i, j, board[i][j])

    ans = len(result)
    print(f'#{tc}', ans)
