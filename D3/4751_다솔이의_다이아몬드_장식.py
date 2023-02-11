T = int(input())
 
for tc in range(1, T+1):
    text = input()
    a = ['.', '.', '#', '.', '.']
    b = ['.', '#', '.', '#', '.']
    c = ['#', '.', 0, '.', '#']
    decor = [i for i in (a, b, c, b, a)]
    rlt = [[] for _ in range(5)]
 
    for t in range(len(text)):
        decor[2][2] = text[t]
        if t != len(text) - 1:
            for i in range(5):
                rlt[i] += decor[i][:-1]
 
        else:
            for i in range(5):
                rlt[i] += decor[i]
 
 
    for i in range(5):
        print(*rlt[i], sep='')