T = int(input())
 
for tc in range(1, T + 1):
    stick = input()
    nStick = stick.replace('()', '#') # make lasers easier to identify
 
    stack, piece = 0, 0
 
    for i in nStick:
        if i == '(': # adding a new metal stick to the stack
            stack += 1
            piece += 1
        elif i == '#':
            piece += stack # a laser will add the stack number of pieces
        else: # removing a metal stick from the stack
            stack -= 1
 
    print(f'#{tc} {piece}')