T = int(input())

for tc in range(1, T+1):
    audience = input()
    cnt = 0
    part = 0  # part-time
    for i in range(len(audience)):
        if audience[i] == '0':
            continue

        if cnt < i:
            part += i - cnt
            cnt += i - cnt
        cnt += int(audience[i])
    print(f'#{tc}', part)