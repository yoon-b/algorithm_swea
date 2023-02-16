operator = ['+', '*']

def infixToPostfix(expression):
    stack = []
    rlt = ''

    for character in expression:
        if character not in operator:
            rlt += character
        else:
            while stack and operator.index(character) <= operator.index(stack[-1]):
                rlt += stack.pop()
            stack.append(character)

    while stack:
        rlt += stack.pop()

    return rlt


def evaluatePostfix(expression):
    stack = []

    for character in expression:
        if character not in operator:
            stack.append(int(character))
        elif character == '+':
            a, b = int(stack.pop(-2)), int(stack.pop(-1))
            stack.append(a+b)
        else:
            a, b = int(stack.pop(-2)), int(stack.pop(-1))
            stack.append(a*b)

    return stack.pop()


for tc in range(1, 11):
    N = int(input())
    exp = input()
    print(f'#{tc}', evaluatePostfix(infixToPostfix(exp)))