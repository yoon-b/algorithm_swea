def levelOrder(lst: list, s: int):
    queue = [s]
    rlt = []
    visited = [0] * 101

    while queue:
        level = []
        l = len(queue)
        for i in range(l):
            current = queue.pop(0)
            if not visited[current]:
                visited[current] = 1
            else:
                continue

            if lst[current]:
                for c in lst[current]:
                    if not visited[c]:
                        level.append(c)
                        queue.append(c)
        rlt.append(level)
    return rlt


for tc in range(1, 11):
    N, S = map(int, input().split())
    data = list(map(int, input().split()))
    adjLst = [[] for _ in range(101)]
    for i in range(N//2):
        adjLst[data[2*i]].append(data[2*i+1])

    print(f'#{tc}', max(levelOrder(adjLst, S)[-2]))

