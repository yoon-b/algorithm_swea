code = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
 
T = int(input())
 
for tc in range(1, T+1):
    N = int(input()[3:])
    num = input().split()
    rlt = [0] * N
    ans = [0] * N
 
    for i in range(N):
        rlt[i] = code.index(num[i])
 
    rlt = sorted(rlt)
 
    for i in range(N):
        ans[i] = code[rlt[i]]
 
    print(f'#{tc}')
    print(' '.join(ans))