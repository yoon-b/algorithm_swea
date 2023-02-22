"""
1. 방에 적힌 숫자가 중복되지 않고, 현재 방보다 1만큼 큰 방으로만 이동할 수 있음
2. 방의 숫자를 인덱스로 활용하여, 현재 원소에서 다음 인덱스로 이동 가능한 지 여부를 확인
3. 이동할 경우 카운트를 증가시키고, 이동이 불가능하면 카운트를 초기화
4. 카운트가 최대값보다 크면 그 값과 이동이 시작한 지점을 답으로 갱신
"""

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    room = [0] * (N**2+1)  # 주어진 정수가 취할 수 있는 최대값이 N^2
    for i in range(N):
        row = list(map(int, input().split()))
        for j in range(N):
            room[row[j]] = (i, j)  # 주어진 방의 숫자를 인덱스로 하고, 그 자리에 좌표 값을 삽입

    maxL = ans = 1  # 갱신 될 답
    cnt = start = 1  # 현재 측정 중인 이동 거리와 그 시작점
    for n in range(1, len(room)):
        y, x = room[n]
        for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if room[n -1] == (y + dy, x + dx):  # 다음 칸으로 이동 가능한 경우
                cnt += 1  # 거리 1 추가
                if maxL < cnt:  # 지금까지의 이동 거리가 기존의 최댓값보다 클 경우
                    maxL, ans = cnt, start  # 답 갱신
                break
        else:  # 이동할 수 없는 경우 이동 거리와 시작점을 초기화
            cnt, start = 1, n

    print(f'#{tc}', ans, maxL)