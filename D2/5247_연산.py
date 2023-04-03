from collections import deque


def bfs(n: int) -> int:
    numQ = deque()
    numQ.append((n, 0))
    # visited = set()
    while numQ:
        curNum, numOp = numQ.popleft()
        for nextNum in (curNum + 1, curNum - 1, curNum * 2, curNum - 10):
            # if nextNum <= 1000000 and nextNum not in visited:
            if nextNum <= 1000000 and not visited[nextNum]:
                numQ.append((nextNum, numOp+1))
                visited[nextNum] = 1
                # visited.add(nextNum)
                if nextNum == goal:
                    return numOp + 1


T = int(input())
for tc in range(1, T+1):
    N, goal = map(int, input().split())
    visited = [0] * 1000001
    answer = bfs(N)
    print(f'#{tc}', answer)