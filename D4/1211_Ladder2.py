for _ in range(1, 11):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    cnts = []
    cntIdx = []
 
    for i in range(100):
        x = 0
        y = 0
        cnt = 0
        if ladder[x][i] == 1:
            y = i
 
        while _ in range(99):
            if x == 99:
                break
            # left
            if 0 <= y - 1 <= 99 and ladder[x][y - 1]:
                while 1 <= y <= 99 and ladder[x][y - 1] != 0:
                    y -= 1
                    cnt += 1
                    if ladder[x][y] == 0:
                        break
            # right
            elif 0 <= y + 1 <= 99 and ladder[x][y + 1]:
                while 0 <= y <= 98 and ladder[x][y + 1] != 0:
                    y += 1
                    cnt += 1
                    if ladder[x][y] == 0:
                        break
            x += 1
            cnt += 1
        cnts.append(cnt)
        cntIdx.append(i)
    ans = cntIdx[cnts.index(min(cnts))]
 
    print(f'#{tc} {ans}')