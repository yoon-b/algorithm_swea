def perm(i: int, k: int):
    global p, minU, N
    if i == k:
        modifiedP = [1] + p + [1]
        sumU = 0
        for j in range(N):
            sumU += batteryUsage[modifiedP[j]-1][modifiedP[j+1]-1]
        if sumU < minU:
            minU = sumU
    else:
        for j in range(i, k):
            p[i], p[j] = p[j], p[i]
            perm(i+1, k)
            p[i], p[j] = p[j], p[i]


for tc in range(int(input())):
    N = int(input())
    batteryUsage = [list(map(int, input().split())) for _ in range(N)]
    minU = 100*N
    p = [0] * (N-1)
    for i in range(N-1):
        p[i] = i+2
    perm(0,N-1)
    print(f'#{tc+1}', minU)

