def binarySearch(a, N, key):
    start = 1
    end = N-1
    cnt = 0
    while start <= end:
        middle = (start + end) // 2
        cnt += 1
        if a[middle] == key: #value found
            return cnt
        elif a[middle] > key: #search left
            end = middle
        else: #search right
            start = middle
    return 'try again'
 
T = int(input())
 
for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    book = range(P)
    cnt_a = binarySearch(book, P+1, Pa)
    cnt_b = binarySearch(book, P+1, Pb)
    if cnt_a > cnt_b:
        winner = 'B'
    elif cnt_a < cnt_b:
        winner = 'A'
    else:
        winner = 0
    print(f'#{tc} {winner}')