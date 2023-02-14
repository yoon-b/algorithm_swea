T = int(input())

paper = [0, 1, 3] + [0] * 28

for tc in range(1, T+1):
    N = int(input()) // 10
    for i in range(3, N+1):
        paper[i] = paper[i-1] + 2 * paper[i-2]
    
    print(f'#{tc} {paper[N]}')