def quickSort(arr, left, right):
    if left < right:
        p = partition(arr, left, right)
        quickSort(arr, left, p - 1)
        quickSort(arr, p + 1, right)


def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]

    return i


for tc in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    print(A)
    quickSort(A, 0, N-1)
    print(f'#{tc+1}', A[N//2])
