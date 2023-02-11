def rev(a):
    r = ''
    for letter in a:
        r = letter + r
    return r
 
T = int(input())
 
for tc in range(1, T+1):
    word = input()
    if word == rev(word):
        rlt = 1
    else:
        rlt = 0
 
    print(f'#{tc} {rlt}')