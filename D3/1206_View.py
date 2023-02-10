for tc in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))
    view = 0 #조망권이 확보된 세대의 수
 
    for i in range(2, N-2):
        left = buildings[i-2:i] #왼쪽 건물
        right = buildings[i+1:i+3] #오른쪽 건물
        neighbor = left + right #조망권에 영향을 주는 이웃
 
        maxN = 0 #이웃 중 가장 큰 빌딩의 높이
        for j in neighbor:
            if j > maxN:
                maxN = j
 
        if buildings[i] > maxN:
            view += buildings[i] - maxN
 
    print(f'#{tc} {view}')