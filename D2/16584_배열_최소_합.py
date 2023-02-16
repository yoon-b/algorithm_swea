# modified from N-Queen

def findMin(n):
    col = set()

    def backtrack(r):
        global sumV, minV

        if sumV > minV:
            return
        if r == n:
            if minV > sumV:
                minV = sumV
            return

        for c in range(n):
            if c in col:
                continue

            col.add(c)
            sumV += nums[r][c]

            backtrack(r + 1)

            col.remove(c)
            sumV -= nums[r][c]

    backtrack(0)
    return minV


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = [list(map(int, input().split())) for _ in range(N)]
    minV = 10 * N
    sumV = 0
    print(f'#{tc}', findMin(N))