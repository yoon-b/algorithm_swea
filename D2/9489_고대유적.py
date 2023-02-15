T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())  # size of rows and columns 
                                      # (note that these two can be different)
    photo = [list(map(int, input().split())) for _ in range(N)]
    photoT = list(zip(*photo))  # transposed matrix
    maxL = 2  # maximum length (minimum of 2 was given by the problem)

    for i in range(N):  # find the maximum value travers rows
        cnt = 0  # var. for counting the length of a pictured heritage
        for j in range(M):
            if photo[i][j] == 1:
                cnt += 1
                if cnt > maxL:  # update the maximum value
                    maxL = cnt
            else:
                cnt = 0

    for i in range(M):  # find the maximum value travers columns 
                        # (= traversing rows of the transposed matrix)
        cnt = 0
        for j in range(N):
            if photoT[i][j] == 1:
                cnt += 1
                if cnt > maxL:
                    maxL = cnt
            else:
                cnt = 0

    print(f'#{tc}', maxL)
