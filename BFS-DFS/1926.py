# https://www.acmicpc.net/problem/1926
from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
area = 0
num = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    cnt = 1
    graph[x][y] = 0
    q = deque([[x, y]])
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if not (0 <= nx < N and 0 <= ny < M) or graph[nx][ny] == 0:
                continue
            cnt += 1
            graph[nx][ny] = 0
            q.append([nx, ny])

    return cnt


for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            num += 1
            area = max(area, bfs(i, j))

print(num, area, sep='\n')
