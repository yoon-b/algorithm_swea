T = int(input())
 
for tc in range(1, T+1):
    A, B = input().split()
    N = len(A)
    M = len(B)
    idxA = 0
    idxB = 0
    cnt = 0
 
    while idxA < N and idxB < M:
        if A[idxA] == B[idxB]:
            idxA += 1
            idxB += 1
        else:
            idxA = idxA - idxB + 1
            idxB = 0
 
        if idxB == M:
            cnt += 1
            idxB = 0
 
    print(f'#{tc} {N - cnt * (M-1)}')