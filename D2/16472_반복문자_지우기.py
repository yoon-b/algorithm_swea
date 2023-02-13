T = int(input())

for tc in range(1, T+1):
    text = input()
    stack = []
    for i in text:
        if not stack or i != stack[-1]:
            stack.append(i)
        else:
            stack.pop()
    print(f'#{tc} {len(stack)}')