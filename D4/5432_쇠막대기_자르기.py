T = int(input())
 
for tc in range(1, T + 1):
    stick = input()
    nStick = stick.replace('()', '#')
 
    stack, piece = 0, 0
 
    for i in nStick:
        if i == '(':
            stack += 1
            piece += 1
        elif i == '#':
            piece += stack
        else:
            stack -= 1
 
    print(f'#{tc} {piece}')