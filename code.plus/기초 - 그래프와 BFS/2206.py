# https://www.acmicpc.net/problem/2206

from collections import deque

x, y = map(int, input().split())
graph = [list(map(str, input())) for _ in range(x)]
# visited = [[False] * y for _ in range(x)]
# cnt = [[0] * y for _ in range(x)]

def bfs(sx, sy):
    graph[sx][sy] = 0
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    q = deque([[sx, sy, 0]])

    while q:
        cx, cy, cb = q.popleft()
        nb = cb

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if not(0 <= nx < x and 0 <= ny < y):
                continue
        
            if type(graph[nx][ny]) == int:
                continue

            if graph[nx][ny] == '1':
                if cb == 0:
                    graph[nx][ny] = int(graph[cx][cy]) + 1
                    nb = 1
                else:
                    nb = 1
            else:
                nb = cb
                graph[nx][ny] = int(graph[cx][cy]) + 1

            q.append([nx, ny, nb])

    if graph[x-1][y-1] == '0':
        return -1
    else:
        return graph[x-1][y-1] + 1

print(bfs(0, 0))

for i in graph:
    print(i)
print()