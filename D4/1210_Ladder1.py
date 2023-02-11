for _ in range(10):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    x = 99
    y = 0
 
    for i in range(100):
        if ladder[x][i] == 2:
            y = i
 
    while _ in range(99):
        if x == 0:
            break
 
        if 0 <= y-1 <= 99 and ladder[x][y-1]:
            while 0 <= y-1 <= 99 and ladder[x][y-1] != 0:
                y -= 1
                if ladder[x][y] == 0:
                    break
 
        elif 0 <= y+1 <= 99 and ladder[x][y+1]:
            while 0 <= y+1 <= 99 and ladder[x][y+1] != 0:
                y += 1
                if ladder[x][y] == 0:
                    break
        x -= 1
 
    print(f'#{tc} {y}')