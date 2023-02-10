T = int(input())
 
for tc in range(1, T+1):
    N = int(input())
    H = list(map(int, input().split()))
    fall_down = [0] * N
 
    for i in range(N):
        fall = 0
        for j in range(i + 1, N):
            if H[i] > H[j]:
                fall += 1
        fall_down[i] = fall
 
    max_fall = 0
 
    for a in fall_down:
        if a > max_fall:
            max_fall = a
 
    print(f'#{tc} {max_fall}')