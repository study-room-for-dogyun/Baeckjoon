# https://www.acmicpc.net/problem/7562
from collections import deque

def bfs(sx, sy):
    q = deque()
    q.append([sx, sy])
    dx = [-2, -1, 1, 2, -2, -1, 1, 2]
    dy = [-1, -2, -2, -1, 1, 2, 2, 1]

    while q:
        x, y = q.popleft()

        if [x, y] == goal:
            return graph[x][y]

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < l and 0 <= ny < l and graph[nx][ny] == 0:
                graph[nx][ny] += graph[x][y] + 1
                q.append([nx, ny])

t = int(input())

for _ in range(t):
    l = int(input())
    x, y = map(int, input().split())
    goal = list(map(int, input().split()))
    graph = [[0] * l for _ in range(l)]

    print(bfs(x, y))