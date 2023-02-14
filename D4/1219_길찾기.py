def dfs(graph, start, goal):
    visited[start] = 1

    for next in range(1, 101):
        if next in graph[start] and not visited[next]:
            dfs(graph, next, goal)

        if visited[goal]:
            return 1
    return 0

for _ in range(10):
    tc, r = map(int, input().split())
    edge = [[] for _ in range(100)]
    route = list(map(int, input().split()))
    visited = [0] * 100

    for i in range(r):
        f = route[2*i]  # from
        t = route[2*i+1]  # to
        edge[f].append(t)

    print(f'#{tc}', dfs(edge, 0, 99))

