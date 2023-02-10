T = int(input())
 
for tc in range(1, T+1):
    N = int(input())
    carrot = list(map(int, input().split()))
    got_bigger = [0] * N
 
    for i in range(1, N):
        if carrot[i] > carrot[i-1]:
            got_bigger[i] = 1
 
    for i in range(1, N):
        if got_bigger[i] == 1:
            got_bigger[i] += got_bigger[i-1]
 
    print(f'#{tc} {max(got_bigger) + 1}')