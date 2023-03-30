def dfs(arr, current, end):
    global minChange, changeTimes
    if current >= end:
        if changeTimes < minChange:
            minChange = changeTimes
            return
    if changeTimes >= minChange:
        return

    for i in range(1, arr[current]+1):
        changeTimes += 1
        dfs(arr, current+i, end)
        changeTimes -= 1


T = int(input())
for tc in range(1, T+1):
    stopInfo = list(map(int, input().split()))
    N = minChange = len(stopInfo)
    changeTimes = -1
    dfs(stopInfo, 1, N)
    print(f'#{tc}', minChange)
