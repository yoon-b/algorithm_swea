def dfs(n, cost):
    global minCost
    if cost > minCost:
        return

    if n > 12:
        minCost = min(cost, minCost)
        return
    dfs(n+1, cost + day*plan[n])
    dfs(n+1, cost + mon)
    dfs(n+3, cost + quart)
    dfs(n+12, cost + year)


T = int(input())
for tc in range(1, T+1):
    day, mon, quart, year = map(int, input().split())
    plan = [0] + list(map(int, input().split()))
    minCost = day * 365
    dfs(1, 0)
    print(f'#{tc}', minCost)