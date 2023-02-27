T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cnt = 0
    digit = set()
    while len(digit) != 10:
        cnt += 1
        num = str(N * cnt)
        for n in num:
            digit.add(n)

    print(f'#{tc}', num)
