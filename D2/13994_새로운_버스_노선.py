T = int(input())
 
for tc in range(1, T+1):
 
    bus_stops = [0] * 1001
 
    N = int(input())
    for i in range(N):
        bus, start, end = map(int, input().split())
        if bus == 1:
            for j in range(start, end+1):
                bus_stops[j] += 1
        elif bus == 2:
            for j in range(start, end+1):
                if start % 2: #odd
                    if j % 2:
                        bus_stops[j] += 1
                else: #even
                    if not j % 2:
                        bus_stops[j] += 1
        else:
            for j in range(start, end+1):
                if start % 2: #odd
                    if (not j % 3) and (j % 10):
                        bus_stops[j] += 1
                else:#even
                    if not j % 4:
                        bus_stops[j] += 1
 
    print(f'#{tc} {max(bus_stops)}')