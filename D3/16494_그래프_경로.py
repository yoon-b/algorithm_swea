def dfs(graph, start, goal):
    visited[start] = 1

    for next in range(1, V+1):
        if next in graph[start] and not visited[next]:
            dfs(graph, next, goal)

        if visited[goal]:
            return 1
    return 0


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    adjL = [[] for _ in range(V+1)]  # 1번부터 V개의 노드
    visited = [0] * (V+1)
    stack = list()

    for _ in range(E):
        a, b = map(int, input().split())
        adjL[a].append(b)
    S, G = map(int, input().split())

    print(f'#{tc}', dfs(adjL, S, G))
