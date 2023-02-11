def func_max(arr):
    maxV = arr[0]
    for i in range(1, len(arr)):
        if maxV < arr[i]:
            maxV = arr[i]
    return maxV
 
def func_min(arr):
    minV = arr[0]
    for i in range(1, len(arr)):
        if minV > arr[i]:
            minV = arr[i]
    return minV
 
T = int(input())
 
for tc in range(1, T+1):
    N = int(input())
    targetLst = list(map(int, input().split()))
    specialLst = [0] * 10
 
    for j in range(10):
        if j % 2:
            specialLst[j] = func_min(targetLst)
            targetLst.remove(func_min(targetLst))
 
        else:
            specialLst[j] = func_max(targetLst)
            targetLst.remove(func_max(targetLst))
 
    answer = ' '.join(map(str, specialLst))
    print(f'#{tc} {answer}')