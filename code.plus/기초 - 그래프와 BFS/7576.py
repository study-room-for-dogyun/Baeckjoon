# https://www.acmicpc.net/problem/7576

from collections import deque

m, n = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

#     U  D  L  R
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def start(graph):
    result = []

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                result.append([i, j])
    return result

def check(graph):
    for i in graph:
        if 0 in i:
            return False
    
    return True

def bfs(graph):
    result = 0
    queue = deque()

    for i in start(graph):
        queue.append(i)

    while queue:
        x, y = queue.popleft()
    
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                queue.append([nx, ny])
                graph[nx][ny] = graph[x][y] + 1
                result = graph[nx][ny]
    

    if result == 0:
        return result
    return result-1


result = bfs(graph)

if check(graph):
    print(result)
else:
    print(-1)

