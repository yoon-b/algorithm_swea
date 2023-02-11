for _ in range(10):
    tc = int(input())
    p = input()
    t = input()
    M = len(p)
    N = len(t)
 
    cnt = 0
    for i in range(N-M+1):
        for j in range(M):
            if t[i+j] != p[j]:
                break
        else:
            cnt += 1
 
    print(f'#{tc} {cnt}')