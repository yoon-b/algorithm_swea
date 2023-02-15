'''
maze info.
0: passage
1: obstacle
2: start
3: exit
'''

dx = [0, 1, 0, -1]  # Right, Down, Left, Up
dy = [1, 0, -1, 0]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    maze = [[i for i in str(input())] for _ in range(N)]
    ans = 0
    stack = []
    for i in range(N):  # finding the starting point
        for j in range(N):
            if maze[i][j] == '2':
                stack.append((i, j))

    while stack:  # while there is a point to go back (for backtracking)
        x, y = stack.pop()  # updating the starting point to the most recent possible passage
        maze[x][y] = 1  # visited point marked as an obstacle to prevent re-visiting

        for d in range(4):  # checking all four directions from the point
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < N:  # if in the boundaries of the maze
                if maze[nx][ny] == '3':  # exit found
                    ans = 1  # escape
                    break
                elif maze[nx][ny] == '0':  # possible passage
                    stack.append((nx, ny))

    print(f'#{tc}', ans)
