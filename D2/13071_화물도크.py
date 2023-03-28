for tc in range(int(input())):
    N = int(input())

    truck = [0] * N

    for i in range(N):
        truck[i] = list(map(int, input().split()))
    truck.sort(key=lambda x: x[1])
    greedyTrucks = [truck[0]]
    for j in range(1, N):
        if truck[j][0] >= greedyTrucks[-1][1]:
            greedyTrucks.append(truck[j])

    print(f'#{tc+1}', len(greedyTrucks))
