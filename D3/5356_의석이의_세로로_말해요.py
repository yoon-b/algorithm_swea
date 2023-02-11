T = int(input())
 
for tc in range(1, T+1):
    letters = [[0] for _ in range(5)]
    for i in range(5):
        chars = input()
        for char in chars:
            letters[i].append(char)
 
    rlt = ''
    for i in range(1, 16):
        for j in range(5):
            try: rlt += letters[j][i]
            except: continue
 
    print(f'#{tc} {rlt}')