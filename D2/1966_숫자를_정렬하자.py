T = int(input())
 
for tc in range(1, T + 1):
    N = int(input())  # N = len(lst)
    lst = list(map(int, input().split()))
 
    # counting sort
    sorted_lst = [0] * N
    counts = [0] * 51
 
    for i in range(N):
        counts[lst[i]] += 1
 
    for i in range(1, 51):
        counts[i] += counts[i - 1]
 
    for i in range(N - 1, -1, -1):
        counts[lst[i]] -= 1
        sorted_lst[counts[lst[i]]] = lst[i]
 
    result = ' '.join(list(map(str, sorted_lst)))
    print(f'#{tc} {result}')