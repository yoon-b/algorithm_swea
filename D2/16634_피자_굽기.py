T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))
    nPizza = list(map(list, zip(range(1, M+1), pizza)))
    oven = nPizza[:N]
    notOven = N  # 대기 중인 피자의 시작 인덱스 번호

    while len(oven) > 1:  # 화덕에 피자가 1개 이상 있는 동안
        check = oven.pop(0)  # 앞 자리 피자 확인
        check[1] = check[1]//2
        if check[1] != 0:
            oven.append(check)  # 다 구워지지 않았으면 화덕 맨 뒤로
        else:
            if notOven <= M-1:  # 대기중인 피자가 있으면
                oven.append(nPizza[notOven])
                notOven += 1
    print(f'#{tc}', oven[0][0])