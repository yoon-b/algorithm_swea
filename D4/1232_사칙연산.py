op = {'+': lambda x, y: x + y,
      '-': lambda x, y: x - y,
      '*': lambda x, y: x * y,
      '/': lambda x, y: x / y}

for tc in range(1, 11):
    N = int(input())
    heap = [[] for _ in range(N+1)]

    for i in range(N):
        idx, *info = input().split()
        heap[int(idx)].extend(info)
    for p in range(N, 0, -1):
        if len(heap[p]) == 1:
            heap[p] = int(heap[p][0])
        elif len(heap[p]) == 3:
            left = int(heap[p][1])
            right = int(heap[p][2])
            heap[p] = op[heap[p][0]](heap[left], heap[right])
    ans = round(heap[1])
    print(f'#{tc}', ans)
