def dfs(idx, sumP):
    global answer
    if K < sumP:
        return

    if idx == N:
        if sumP == K:
            answer += 1
        return

    dfs(idx + 1, sumP + numList[idx])
    dfs(idx + 1, sumP)


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    numList = list(map(int, input().split()))
    answer = 0
    dfs(0, 0)
    print(f'#{tc}', answer)
