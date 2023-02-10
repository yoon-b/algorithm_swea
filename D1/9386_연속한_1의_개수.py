T = int(input())
 
for tc in range(1, T+1):
    N = int(input())
    num = input()
    counts = [0] * N
 
    for i in range(N):
        if num[i] == '1':
            counts[i] = 1
 
    for i in range(1, N):
        if counts[i]:
            counts[i] += counts[i-1]
 
    print(f'#{tc} {max(counts)}')