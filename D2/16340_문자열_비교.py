T = int(input())
 
for tc in range(1, T+1):
    N = input()
    M = input()
    n, m = len(N), len(M)
 
    i = 0
    j = 0
 
    while i < n and j < m:
        if M[j] != N[i]:
            j = j - i
            i = -1
        j = j + 1
        i = i + 1
 
    if i == n:
        result = 1
    else:
        result = 0
 
    print(f'#{tc} {result}')