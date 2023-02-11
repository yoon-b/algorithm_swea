T = int(input())
 
for tc in range(1, T + 1):
    N = int(input())
 
    lst = [[0 for _ in range(10)] for _ in range(10)]
    count = 0
    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for j in range(r1, r2 + 1):
            for k in range(c1, c2 + 1):
                lst[j][k] += color
        # print(lst)
    for i in range(10):
        for j in range(10):
            if lst[i][j] == 3:
                count += 1
 
    print(f'#{tc} {count}')