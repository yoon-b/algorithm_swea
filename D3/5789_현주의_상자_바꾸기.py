T = int(input())

for tc in range(1, T+1):
    N, Q = map(int, input().split())
    box = [0] * N
    for i in range(1, Q+1):
        s, e = map(int, input().split())
        for b in range(s-1, e):
            box[b] = i
    print(f'#{tc}', *box)