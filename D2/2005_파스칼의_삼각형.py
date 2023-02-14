T = int(input())

for tc in range(1, T+1):
    N = int(input())
    pascal = [[] for _ in range(N)]  # intialize an empty matrix
    for i in range(N):
        for j in range(i+1):
            if j == 0 or j == i:  # both ends of a row should be 1
                pascal[i].append(1)
            else:
                pascal[i].append(pascal[i-1][j-1] + pascal[i-1][j])

    print(f'#{tc}')
    for i in range(N):
        print(*pascal[i], sep=' ')