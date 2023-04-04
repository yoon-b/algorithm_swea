def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x


def union(x, y):
    rep[find_set(y)] = find_set(x)


T = int(input())
for tc in range(1, 2):
    V, E = map(int, input().split())
    rep = [i for i in range(V + 1)]  # 자기 자신을 대표원소로 함
    graph = []
    for _ in range(E):
        edge = list(map(int, input().split()))
        graph.append(edge)
    graph.sort(key=lambda x: x[2])  # 가중치 기준 오름차순 정렬

    N = V + 1
    sumWeight = 0
    cnt = 0

    for u, v, w in graph:
        if find_set(u) != find_set(v):  # non-cyclical
            cnt += 1
            sumWeight += w
            union(u, v)
            if cnt == N-1:
                break
    print(f'#{tc}', sumWeight)


