T = int(input())
 
 
for tc in range(1, T+1):
    N = int(input())
    n = str(input())
    C = [0] * 10
 
    for i in n:
        C[int(i)] += 1
 
    max_C = C[9]
    most = 9
    for j in range(8, -1, -1):
        if max_C < C[j]:
            max_C = C[j]
            most = j
 
    print(f'#{tc} {most} {max_C}')