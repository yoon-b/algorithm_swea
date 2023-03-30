def solveNQueens(n: int):
    col = set()
    posDiag = set()
    negDiag = set()

    def backtrack(r):
        global cnt
        if r == n:
            cnt += 1
            return

        for c in range(n):
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue
            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            backtrack(r + 1)
            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
    backtrack(0)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = 0
    solveNQueens(N)
    print(f'#{tc}', cnt)