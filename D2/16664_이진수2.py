def ftob(n):
    rlt = ''
    f = 2 * n
    cnt = 0
    while f != 1:
        cnt += 1
        if f > 1:
            f -= 1
            rlt += str('1')
            f *= 2
        else:
            rlt += str('0')
            f *= 2

        if cnt >= 12:
            return 'overflow'

    if f == 1:
        rlt += str('1')
        return rlt


T = int(input())

for tc in range(1, T+1):
    flo = float(input())
    ans = ftob(flo)
    print(f'#{tc}', ans)
