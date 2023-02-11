n = 100
 
 
for _ in range(1, 11):
    tc = int(input())
 
    lst = [list(map(int, input().split())) for _ in range(n)]
 
    maxValue = 0
    for i in range(n):
        sum_rows = 0
        for j in range(n):
            sum_rows += lst[i][j]
            if maxValue < sum_rows:
                maxValue = sum_rows
 
    for i in range(n):
        sum_columns = 0
        for j in range(n):
            sum_columns += lst[j][i]
            if maxValue < sum_columns:
                maxValue = sum_columns
 
    sum_dia = 0
    for i in range(n):
        sum_dia += lst[i][i]
        if maxValue < sum_dia:
            maxValue = sum_dia
 
    sum_diag = 0
    for i in range(n):
        sum_diag += lst[-i][-i]
        if maxValue < sum_diag:
            maxValue = sum_diag
 
    print(f'#{tc} {maxValue}')