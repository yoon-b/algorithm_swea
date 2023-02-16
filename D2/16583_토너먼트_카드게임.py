def rsp(a, b):  # 가위바위보
    if card[a] - card[b] == -1 or card[a] - card[b] == 2:  # b가 이김
        return b
    else:  # 비기거나 a가 이기는 경우
        return a


def tournament(start, end):  # 토너먼트 조 짜기
    if start == end:  # 한 명 남으면 우승
        return start
    left = tournament(start, (start+end)//2)
    right = tournament((start+end)//2+1, end)

    return rsp(left, right)  # 게임


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    card = list(map(int, input().split()))
    print(f'#{tc}', tournament(0, N-1)+1)  # 번호가 1부터 시작이니 +1
