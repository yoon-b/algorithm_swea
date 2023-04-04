def dijkstra(s, V):
    U = [0] * (V+1)
    U[s] = 1
    for i in range(V+1):
        D[i] = adjM[s][i]

    for _ in range(V):
        minV = inf
        w = 0
        for i in range(V+1):
            if not U[i] and minV > D[i]:
                w = i
                minV = D[i]
        U[w] = 1
        for v in range(V+1):
            if 0 < adjM[w][v] < inf:
                D[v] = min(D[v], D[w]+adjM[w][v])


T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    inf = 10 * N * N
    adjM = [[inf] * (N+1) for _ in range(N+1)]
    for i in range(N+1):
        adjM[i][i] = 0

    for _ in range(E):
        u, v, w = map(int, input().split())
        adjM[u][v] = w

    D = [0] * (N+1)
    dijkstra(0, N)
    print(f'#{tc}', D[N])


