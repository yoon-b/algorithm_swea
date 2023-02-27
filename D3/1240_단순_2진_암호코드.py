def validPw(p):
    sumE = 0
    sumO = 0
    for i in range(8):
        if i % 2:
            sumO += int(p[i])
        else:
            sumE += int(p[i])

    if ((sumE * 3) + sumO) % 10:
        return 0
    else:
        return sumE + sumO


decode = {'0001101': '0', '0011001': '1', '0010011': '2',
          '0111101': '3', '0100011': '4', '0110001': '5',
          '0101111': '6', '0111011': '7', '0110111': '8',
          '0001011': '9'}

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    pw = [input() for _ in range(N)]
    for p in pw:
        p = p.rstrip('0')
        rlt = ''
        if len(p):
            for _ in range(8):
                c = p[-7:]
                p = p[0:-7]
                rlt = decode[c] + rlt
            break
    ans = validPw(rlt)
    print(f'#{tc}', ans)