T = int(input())
 
for tc in range(1, T+1):
    N = int(input()) # 2<= N <= 10,000,000
    prime = [2, 3, 5, 7, 11]
    counts = [0] * 5
 
    #prime[i]로 나누어 떨어지면 counts[i]에 + 1
    for i in range(5):
        while N > 1:
            if N % prime[i] == 0:
                counts[i] += 1
                N //= prime[i]
            else:
                break
 
    counts = ' '.join(map(str, counts))
 
    print(f'#{tc} {counts}')