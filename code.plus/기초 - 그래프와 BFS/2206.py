# https://www.acmicpc.net/problem/2206

from collections import deque

# INPUT
n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[[-1] * m for _ in range(n)] for _ in range(2)]


# Solution
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# [벽][x][y]
visited[0][0][0] = 1
q = deque([[0, 0, 0]])

while q:

    crush, x, y = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not(0 <= nx < n and 0 <= ny < m):    # 범위 벗어나면
            continue
        
        if visited[crush][nx][ny] != -1:         # 방문했다면
            continue

        if graph[nx][ny]:       # 벽일 때
            if not crush and visited[1][nx][ny] == -1:           # 벽을 부수지 않았을 때
                visited[1][nx][ny] = visited[0][x][y] + 1    # 벽을 부순 세상은 벽을 부수지 않은 세상 + 1이 된다.
                q.append([1, nx, ny])

        else:                   # 길일 때
            if visited[crush][nx][ny] == -1:     # 방문 안 했으면
                visited[crush][nx][ny] = visited[crush][x][y] + 1
                q.append([crush, nx, ny])


# OUTPUT
not_broken, broken = visited[0][n-1][m-1], visited[1][n-1][m-1]

if not_broken != -1 and broken == -1:
    print(not_broken)
elif not_broken == -1 and broken != -1:
    print(broken)
else:
    print(min(not_broken, broken))