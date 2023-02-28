T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    flag = [list(input()) for _ in range(N)]
    color = [] * N  # 해당 색깔로 바꾸기 위한 색칠 횟수 저장
    minC = N * M  # minimum change (to be updated)
    for f in flag:
        W, B, R = M - f.count('W'), M - f.count('B'), M - f.count('R')
        color.append((W, B, R))
    colorU = color[1:-1]  # color undefined. 색이 확정되지 않은 부분

    # 첫번째와 마지막 행을 제외한 범위에서 가능한 줄의 개수 (n-2개를 3개의 색으로 나눌 수 있는 조합)
    for w in range(0, N-2):  # 흰 색은 0부터 n-3개 (파란색 1개가 필수이므로)
        for b in range(1, N-1-w):  # 파란색은 1부터 n-2개 - 흰 색
            r = N - 2 - w - b   # 빨간색은 전체 행에서 위 두 색과 고정된 첫번째와 마지막을 제외한 나머지

            # 각 줄의 수를 정한 후 바꿔야 하는 색의 수 더하기
            cnt = 0
            for i in range(w):  # w-1까지
                cnt += colorU[i][0]
            for j in range(w, w+b):  # 흰 색 다음 줄이므로 +1 해서 시작
                cnt += colorU[j][1]
            for k in range(w+b, w+b+r):
                cnt += colorU[k][2]

            if cnt < minC:
                minC = cnt

    ans = minC + color[0][0] + color[-1][2]
    print(f'#{tc}', ans)
