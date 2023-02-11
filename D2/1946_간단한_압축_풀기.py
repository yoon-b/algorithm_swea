T =int(input())
 
for tc in range(1, T+1):
    N = int(input())
    text = ''
 
    for _ in range(N):
        c, k = input().split()
        text += c * int(k)
 
    print(f'#{tc}')
    n = 0
    while n < len(text):
        print(text[0+n:10+n])
        n += 10