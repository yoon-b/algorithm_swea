def enq(n):
    global last
    last += 1
    heap[last] = n
    c = last  # child
    p = c//2  # parent
    while p > 0 and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c//2
    return


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    heap = [0] * (N+1)
    num = list(map(int, input().split()))
    last = 0
    for n in num:
        enq(n)


    # 조상 노드들의 합
    ancestor = N//2
    sumA = 0
    while ancestor > 0:
        sumA += heap[ancestor]
        ancestor //= 2
    print(f'#{tc}', sumA)
