def bfs(lst: list):
    queue = []
    queue.extend(lst)
    while queue:
        student = queue.pop(0)
        if pairList[student]:
            for s in pairList[student]:
                if not paired[s]:
                    queue.append(s)
                    paired[s] = 1


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    pair = list(map(int, input().split()))
    pairList = [[] for _ in range(N+1)]
    paired = [0] * (N+1)
    cnt = 0
    for i in range(M):
        pairList[pair[2*i]].append(pair[2*i+1])
        pairList[pair[2*i+1]].append(pair[2*i])
    for i in range(N):
        if paired[i] or not pairList[i]:
            continue
        bfs(pairList[i])
        cnt += 1
    solo = paired.count(0) - 1  # 0번은 결번이니 제외 (-1)
    answer = solo + cnt
    print(f'#{tc}', answer)