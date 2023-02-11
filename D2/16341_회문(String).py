def rev(x):
    rlt = ''
    for i in x:
        rlt = i + rlt
 
    return rlt
 
T = int(input())
 
for tc in range(1, T+1):
    N, M = map(int, input().split())
    letters = [[i for i in input()] for _ in range(N)]
 
    for i in range(N):
        for j in range(0, N-M+1):
            word = ''
            for k in range(M):
                word += letters[i][j+k]
        if word == rev(word):
            found = word
 
    for j in range(N):
        for i in range(0, N-M+1):
            word = ''
            for k in range(M):
                word += letters[i+k][j]
        if word == rev(word):
            found = word
 
    print(f'#{tc} {found}')