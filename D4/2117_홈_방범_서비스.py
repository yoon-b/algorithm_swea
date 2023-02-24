T = int(input())

cost = [c*c+(c-1)*(c-1) for c in range(22)]

for tc in range(1, T+1):
    N, M = map(int, input().split())
    town = [list(map(int, input().split())) for _ in range(N)]
    houses = []
    for i in range(N):
        for j in range(N):
            if town[i][j] == 1:
                houses.append((i, j))
    maxRev = len(houses) * M
    maxH = 0
    for k in range(N+1, 0, -1):
        if maxRev < cost[k]:
            continue
        for i in range(N):
            for j in range(N):
                cnt = 0
                for hi, hj in houses:
                    if abs(i-hi) + abs(j-hj) < k:
                        cnt += 1
                if maxH < cnt and cost[k] <= cnt * M:
                    maxH = cnt
        if maxH:
            break
    print(f'#{tc}', maxH)