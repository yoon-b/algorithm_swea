T = int(input())
 
for tc in range(1, T+1):
    str1 = input()
    N = len(str1)
    str2 = input()
    M = len(str2)
    cnts = {}
 
    for i in str1:
        if i in cnts.keys():
            continue
        for j in str2:
            if i == j:
                try:
                    cnts[i] += 1
                except:
                    cnts[i] = 1
 
    print(f'#{tc} {max(cnts.values())}')