for tc in range(1, 11):
    dump = int(input())
    height = list(map(int, input().split()))
 
    for i in range(dump):
 
        max_h = max(height)
        min_h = min(height)
        max_idx = height.index(max_h)
        min_idx = height.index(min_h)
 
        height[max_idx] -= 1
        height[min_idx] += 1
 
        if max(height) - min(height) <= 1:
            break
 
    difference = max(height) - min(height)
    print(f'#{tc} {difference}')