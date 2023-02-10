T = int(input())
 
for tc in range(1, T+1):
    K, N, M = map(int, input().split()) #최대 이동 거리, 종점 번호, 정류장 수
    charge_stop = list(map(int, input().split()))
 
    charging = now_where = 0
 
    while now_where + K < N:
        for i in range(K, 0, -1):
            if (now_where + i) in charge_stop:
                now_where += i
                charging += 1
                break
 
        else:
            charging = 0
            break
 
    print(f'#{tc} {charging}')