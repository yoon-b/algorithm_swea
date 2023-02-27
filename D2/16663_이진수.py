def htob(n):
    hDict = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    if n in hDict.keys():
        n = hDict[n]
    else:
        n = int(n)

    binary = ''
    for i in range(4):
        binary = str(n % 2) + binary
        n = n//2

    return binary


T = int(input())

for tc in range(1, T+1):
    n, hexa = input().split()
    rlt = ''
    for h in hexa:
        rlt += htob(h)

    print(f'#{tc}', rlt)