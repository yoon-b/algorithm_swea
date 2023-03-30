def calculateCosts(table: list, n: int):
    col = set()
    cost = 0

    def backtrack(r):
        global minCost
        nonlocal cost
        if r == n:
            if cost < minCost:
                minCost = cost
            return
        if cost >= minCost:
            return

        for c in range(n):
            if c in col:
                continue
            col.add(c)
            cost += table[r][c]
            backtrack(r + 1)
            col.remove(c)
            cost -= table[r][c]

    backtrack(0)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    costTable = [list(map(int, input().split())) for _ in range(N)]
    minCost = 99 * N
    calculateCosts(costTable, N)
    print(f'#{tc}', minCost)
