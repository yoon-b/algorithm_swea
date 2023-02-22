def subtree(edge: list, node: int):
    subs = edge[node]
    numSubs = len(subs)
    if subs:
        for s in subs:
            numSubs += subtree(edge, s)
    return numSubs


T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    edges = list(map(int, input().split()))
    edgeInfo = [[] for _ in range(E+2)]
    for i in range(E):
        edgeInfo[edges[2*i]].append(edges[2 * i + 1])

    ans = subtree(edgeInfo, N) + 1  # 루트의 수 더하기
    print(f'#{tc}', ans)