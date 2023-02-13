T = int(input())

for tc in range(1, T+1):
    a = input()
    metal = a.replace('()', '!')
    stack = []
    piece = 0
    for i in metal:
        if i == '(':
            stack.append(i)
            piece += 1
        elif i == '!':
            piece += len(stack)
        else:
            if stack and stack[-1] == '(':
                stack.pop()

    print(f'#{tc} {piece}')