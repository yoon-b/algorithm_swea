def isRun(arr: list):
    for x in range(8):
        if arr[x] and arr[x+1] and arr[x+2]:
            return True
    return False


for tc in range(int(input())):
    cards = list(map(int, input().split()))
    cardFor1 = [0] * 10
    cardFor2 = [0] * 10
    winner = 0
    for i in range(0, 12, 2):
        cardFor1[cards[i]] += 1
        cardFor2[cards[i + 1]] += 1
        if i > 2:
            if 3 in cardFor1 or isRun(cardFor1):
                winner = 1
                break
            if 3 in cardFor2 or isRun(cardFor2):
                winner = 2
                break

    print(f'#{tc+1}', winner)