for tc in range(1, 11):
    N, text = input().split()
    N = int(N)
    password = []
    for i in text:
        if password and i == password[-1]:
            password.pop()
        else:
            password.append(i)

    print(f'#{tc}', ' ', *password, sep='')