# https://www.acmicpc.net/problem/10026

from collections import deque

n = int(input())
graph = [list(map(str, input())) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(sx, sy):
    global visited

    q = deque([[sx, sy]])
    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if not(0 <= nx < n and 0 <= ny < n):
                continue
            if graph[nx][ny] != graph[cx][cy] or visited[nx][ny]:
                continue

            visited[nx][ny] = True
            q.append([nx, ny])



answer = [0, 0]

# 색맹 아닌 사람
visited = [[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j]:
            continue
        bfs(i, j)
        answer[0] += 1

# 색맹인 사람
visited = [[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

for i in range(n):
    for j in range(n):
        if visited[i][j]:
            continue
        bfs(i, j)
        answer[1] += 1


print(" ".join(map(str, answer)))