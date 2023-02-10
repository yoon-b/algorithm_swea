T = int(input())
 
for t in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))
    for i in range(N-1, 0, -1):
        for j in range(0, N-1):
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]
    print(f'#{t} {num[N-1] - num[0]}')