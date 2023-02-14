T = int(input())

for tc in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))

    revenue = 0
    maxP = price[-1]

    for i in range(N-2, -1, -1):
        if maxP < price[i]:
            maxP = price[i]
        else:
            revenue += maxP - price[i]

    print(f'#{tc}', revenue)