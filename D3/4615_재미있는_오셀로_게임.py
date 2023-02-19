di = [0, 0, 1, -1, 1, 1, -1, -1]
dj = [1, -1, 0, 0, 1, -1, 1, -1]

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [[0] * (N+2) for _ in range(N+2)]  # 인덱스 에러 방지용 벽 세우기
    board[N//2][N//2] = board[N//2+1][N//2+1] = 2
    board[N//2][N//2+1] = board[N//2+1][N//2] = 1
    for _ in range(M):
        i, j, c = map(int, input().split())  # c: color
        board[i][j] = c
        for d in range(8):  # d: delta
            temp = []
            for m in range(1, N):  # m: multiply, 1칸부터 보드 끝까지 이동
                ni, nj = i + di[d]*m, j + dj[d]*m
                if board[ni][nj] == 0:  # 빈 칸이면 다음 방향 확인
                    break
                elif board[ni][nj] != c:  # 다른 색이면 후보 리스트에 저장
                    temp.append((nj, nj))
                else:  # 같은 색이면 사이에 있는 돌(리스트에 저장된 돌) 색 바꾸기
                    while temp:  # 돌 좌표 하나씩 꺼내어 바꾸기
                        ti, tj = temp.pop()  # target i & j
                        board[ti][tj] = c
                    break  # 다 바꾸면 반복문 종료 후 다음 방향 확인

    cntB = cntW = 0
    for row in board:
        cntB += row.count(1)
        cntW += row.count(2)

    print(f'#{tc}', cntB, cntW)