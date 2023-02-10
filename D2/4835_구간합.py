T = int(input())
 
for t in range(1, T+1):
    N, M = map(int, input().split())
    num = list(map(int, input().split()))
    rlt = [0] * (N - M + 1)
 
    for i in range(N - M + 1):
        num_sum = 0
        for j in range(i, i+M):
            num_sum += num[j]
        rlt[i] = num_sum
 
    for a in range(len(rlt), 0, -1):
        for b in range(0, len(rlt)-1):
            if rlt[b] > rlt[b+1]:
                rlt[b], rlt[b+1] = rlt[b+1], rlt[b]
 
    print(f'#{t} {rlt[-1] - rlt[0]}')