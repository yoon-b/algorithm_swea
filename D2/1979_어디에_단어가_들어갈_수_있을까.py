def checkCross(arr):
    ans = 0
    for row in arr:
        cnt = 0
        for x in row:
            if x == 1:
                cnt += 1
            else:
                if cnt == K:
                    ans += 1
                cnt = 0
    return ans
 
def transpose(arr):
    arr_t = [[0] * (N+1) for _ in range(N+1)]
    for i in range(N+1):
        for j in range(N+1):
            if i < j:
                arr_t[i][j], arr_t[j][i] = arr[j][i], arr[i][j]
            elif i == j:
                arr_t[i][j] = arr[i][j]
    return arr_t
 
T = int(input())
 
for tc in range(1, T+1):
    N, K = map(int, input().split())
    crossword = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N+1)]
    wordcross = transpose(crossword)
 
    space = checkCross(crossword) + checkCross(wordcross)
 
    print(f'#{tc} {space}')