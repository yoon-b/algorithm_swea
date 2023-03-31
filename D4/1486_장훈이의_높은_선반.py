def dfs(n, sumHeight):
    global minDifference
    if minDifference <= sumHeight - shelfHeight:
        return

    if minDifference == 0:
        return

    if n == numStaff:
        if sumHeight >= shelfHeight:
            minDifference = min(minDifference, sumHeight-shelfHeight)
        return
    dfs(n+1, sumHeight + staffHeight[n])
    dfs(n+1, sumHeight)


T = int(input())
for tc in range(1, T+1):
    numStaff, shelfHeight = map(int, input().split())
    staffHeight = list(map(int, input().split()))
    minDifference = 10000 * numStaff
    dfs(0, 0)
    print(f'#{tc}', minDifference)