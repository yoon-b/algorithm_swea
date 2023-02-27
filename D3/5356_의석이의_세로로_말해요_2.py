T = int(input())

for tc in range(1, T+1):
    blank = [['#'] * 15 for _ in range(5)]
    for i in range(5):
        letter = input()
        for j in range(len(letter)):
            blank[i][j] = letter[j]
    blankT = list(zip(*blank))
    rlt = ''
    for b in blankT:
        rlt += ''.join(b)
    ans = rlt.replace('#', '')
    print(f'#{tc}', ans)