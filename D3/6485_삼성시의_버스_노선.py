T = int(input())
 
for tc in range(1, T+1):
 
    stops = [0] * 5001
 
    N = int(input()) #number of bus lines
    for i in range(N):
        A, B = map(int, input().split()) # range of bus routes
        for j in range(A, B+1):
            stops[j] += 1
 
    P = int(input())
    rlt = []
    for i in range(P):
        C = int(input()) # the no. of bus stop
        rlt.append(stops[C])
 
    rlt = ' '.join(map(str, rlt))
    print(f'#{tc} {rlt}')