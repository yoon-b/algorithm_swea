T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    heap = [0] * (N+1)
    for _ in range(M):
        idx, num = map(int, input().split())
        heap[idx] = num
    for i in range(N, 1, -1):
        heap[i//2] += heap[i]
    ans = heap[L]

    print(f'#{tc}', ans)