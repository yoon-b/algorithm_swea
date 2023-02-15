def infixToPostfix(expression):
    stack = []
    rlt = ''

    for character in expression:
        if character != '+':  # only '+' will be given through inputs 
                              # (restricted by the problem)
                              # ∴ not '+' == digit
            rlt += character
        else:  # stack the operators
            stack.append(character)

    while stack:  # while there's at least one operator on the stack
        rlt += stack.pop()

    return rlt


def evaluatePostfix(expression):
    stack = []

    for character in expression:
        if character != '+':
            stack.append(character)
        else:
            a, b = int(stack.pop(-2)), int(stack.pop(-1))
            stack.append(a+b)

    return stack.pop()


for tc in range(1, 11):
    N = int(input())
    exp = input()
    print(f'#{tc}', evaluatePostfix(infixToPostfix(exp)))