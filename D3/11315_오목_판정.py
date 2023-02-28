def check(arr: list, N: int):
    isValid = False
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                for di, dj in [(0, 1), (1, 1), (1, 0), (1, -1)]:  # 우, 우하, 하, 좌하
                    cnt = 1
                    for t in range(1, 5):
                        ni, nj = i + di * t, j + dj * t
                        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'o':
                            cnt += 1
                        if cnt == 5:
                            isValid = True
                            return isValid
    return isValid


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    board = [list(input()) for _ in range(N)]
    ans = 'YES' if check(board, N) else 'NO'
    print(f'#{tc}', ans)
