def mergeSort(arr):
    global cnt
    if len(arr) > 1:
        m = len(arr)//2
        L = mergeSort(arr[:m])
        R = mergeSort(arr[m:])

        l = r = k = 0
        while l < len(L) and r < len(R):
            if L[l] <= R[r]:
                arr[k] = L[l]
                l += 1
            else:
                arr[k] = R[r]
                r += 1
            k += 1

        if l == len(L):
            while r < len(R):
                arr[k] = R[r]
                r += 1
                k += 1
        else:
            while l < len(L):
                arr[k] = L[l]
                l += 1
                k += 1
            cnt += 1
    return arr


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    mergeSort(arr)
    print(f'#{tc}', arr[N//2], cnt)