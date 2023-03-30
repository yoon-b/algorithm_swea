def calculatePossibility(table: list, n: int):
    col = set()
    possibility = 1

    def backtrack(r):
        global maxPossibility
        nonlocal possibility
        if r == n:
            if possibility > maxPossibility:
                maxPossibility = possibility
            return
        if possibility <= maxPossibility:
            return

        for c in range(n):
            if c in col or table[r][c] == 0:
                continue
            col.add(c)
            possibility *= (table[r][c]/100)
            backtrack(r + 1)
            col.remove(c)
            possibility /= (table[r][c]/100)

    backtrack(0)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    taskTable = [list(map(int, input().split())) for _ in range(N)]
    maxPossibility = 0
    calculatePossibility(taskTable, N)
    answer = "{:.6f}".format(maxPossibility * 100)
    print(f'#{tc}', answer)
