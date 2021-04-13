# https://www.acmicpc.net/problem/7569
from collections import deque

m, n, h = map(int, input().split())
graph = []

for _ in range(h):
    layer = [list(map(int, input().split())) for _ in range(n)]
    graph.append(layer)
    

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
dz = [-1, 1]

def bfs():
    q = deque()
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k] == 1:
                    q.append([k, j, i])

    result = 0
    while q:
        x, y, z = q.popleft()

        for i in range(2):
            nz = z + dz[i]
            if 0 <= nz < h and graph[nz][y][x] == 0:
                graph[nz][y][x] = graph[z][y][x] + 1
                q.append([x, y, nz])

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and graph[z][ny][nx] == 0:
                graph[z][ny][nx] = graph[z][y][x] + 1
                q.append([nx, ny, z])
        
        result = graph[z][y][x]
    
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k] == 0:
                    return -1
    
    return result-1

           
print(bfs())