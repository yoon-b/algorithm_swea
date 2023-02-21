T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    adjLst = [[] for _ in range(V+1)]
    for _ in range(E):
        f, t = map(int, input().split())  # from, to
        adjLst[f].append(t)
        adjLst[t].append(f)
    S, G = map(int, input().split())

    visited = [0 for _ in range(V+1)]
    queue = [S]

    while queue:
        C = queue.pop(0)  # C: current

        if C == G:
            break

        for neighbor in adjLst[C]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = visited[C] + 1

    print(f'#{tc}', visited[G])
