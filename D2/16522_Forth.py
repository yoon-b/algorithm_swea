def evaluatePostfix(expression):
    stack = []  # initialize an empty stack

    for character in expression:
        if character == '.':  # end of an expression (given by the problem)
            if len(stack) == 1:  # when evaluation ends, there should be only one element 
                                 # in the stack, which is the answer
                return stack.pop()  # output the answer
            else:
                return 'error'  # expression is not valid
        elif character not in operations:  # when character is a digit
            stack.append(character)
        else:  # when character is an operator
            if len(stack) >= 2:  # when there are at least 2 operands in the stack
                a, b = int(stack.pop(-2)), int(stack.pop(-1))  # later one goes to the right side of an operator
                stack.append(operations[character](a, b))
            else:  # less than 2 operands means the expression given is not valid
                return 'error'

# dictionary for converting a string to an operator
operations = {'+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x // y}  # remainder is always zero (given by the problem)
                                       # '//' for fitting the result into the format required (integer, not float)
                                       # got no problem with operations
T = int(input())

for tc in range(1, T+1):
    exp = input().split()
    print(f'#{tc}', evaluatePostfix(exp))



# using eval() method
def evaluatePostfix2(expression):
    stack = []

    for character in expression:
        if character == '.':
            if len(stack) == 1:
                return stack.pop()
            else:
                return 'error'
        elif character not in operation:
            stack.append(character)
        else:
            if len(stack) >= 2:
                a, b = int(stack.pop(-2)), int(stack.pop(-1))
                stack.append(eval(str(a)+character+str(b)))
            else:
                return 'error'


operation = ['+', '-', '*', '/']
T = int(input())

for tc in range(1, T+1):
    exp = input().split()
    print(f'#{tc}', evaluatePostfix2(exp))