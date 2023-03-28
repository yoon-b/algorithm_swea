def bruteForce(trial, change):
    global answer, n
    if trial == change:
        answer = max(answer, int(''.join(numbers)))
        return

    for i in range(n):
        for j in range(i+1, n):
            a, b = stack[-1]
            if (i >= a and j >= b) or i > a:
                numbers[i], numbers[j] = numbers[j], numbers[i]
                stack.append((i,j))
                bruteForce(trial+1, change)
                numbers[i], numbers[j] = numbers[j], numbers[i]
                stack.pop()


for tc in range(int(input())):
    numbers, change = input().split()
    numbers = list(numbers)
    change = int(change)
    n = len(numbers)
    answer = 0
    stack = [(-1, -1)]
    bruteForce(0, change)
    print(f'#{tc+1}', answer)