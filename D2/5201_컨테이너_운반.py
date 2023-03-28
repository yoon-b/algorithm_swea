for tc in range(int(input())):
    N, M = map(int, input().split())
    weight = sorted(list(map(int, input().split())), reverse=True)
    capacity = sorted(list(map(int, input().split())), reverse=True)
    truckNumber = 0
    sumWeight = 0
    for w in weight:
        if truckNumber == M:
            break
        for c in range(truckNumber, M):
            if w <= capacity[c]:
                sumWeight += w
                truckNumber += 1
                break
    print(f'#{tc+1}', sumWeight)