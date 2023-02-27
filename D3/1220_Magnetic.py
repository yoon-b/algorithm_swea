for tc in range(1, 11):
    N = int(input())
    mag = [list(map(str, input().split())) for _ in range(100)]
    magT = list(map(list, zip(*mag)))
    cnt = 0
    for m in magT:
        m = ''.join(m)
        m = m.replace('0', '')
        cnt += m.count('12')
    print(f'#{tc}', cnt)
