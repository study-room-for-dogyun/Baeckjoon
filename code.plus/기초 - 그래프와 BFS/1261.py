# https://www.acmicpc.net/problem/1261

from collections import deque

m, n = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
dist = [[-1] * m for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

q = deque([[0, 0]])
dist[0][0] = 0

while q:
    
    x, y = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not(0 <= nx < n and 0 <= ny < m):    # 범위 초과하면 패스
            continue

        if dist[nx][ny] != -1:                  # 방문했으면 패스
            continue

        if graph[nx][ny]:   # 벽이면
            dist[nx][ny] = dist[x][y] + 1       # 부수고 카운터 증가
            q.append([nx, ny])

        else:               # 길이면
            dist[nx][ny] = dist[x][y]
            q.appendleft([nx, ny])              # 길 우선적으로 탐색하게 맨 앞에 넣기
        
print(dist[n-1][m-1])