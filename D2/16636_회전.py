T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))
    print(f'#{tc}', queue[M % N])