T = int(input())
openingB = ['(', '{']
closingB = [')', '}']

for tc in range(1, T+1):
    text = input()
    stack = []
    rlt = 1
    for i in text:
        if i in openingB:
            stack.append(i)

        if i in closingB:
            if not stack:
                rlt = 0
                break

            if i == ')':
                if stack.pop() != '(':
                    rlt = 0
                    break
            if i == '}':
                if stack.pop() != '{':
                    rlt = 0
                    break

    if rlt and not stack:
        rlt = 1
    else:
        rlt = 0

    print(f'#{tc} {rlt}')
