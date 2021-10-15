# https://www.acmicpc.net/problem/16234

from collections import deque

N, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(sx, sy):
    q = deque([[sx, sy]])

    total = graph[sx][sy]
    check = [[sx, sy]]
    visited[sx][sy] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if not(0 <= nx < N and 0 <= ny < N) or visited[nx][ny]:
                continue

            if L <= abs(graph[nx][ny] - graph[x][y]) <= R:
                q.append([nx, ny])
                check.append([nx, ny])
                total += graph[nx][ny]
                visited[nx][ny] = True

    for x, y in check:
        graph[x][y] = total // len(check)

    if len(check) <= 1:
        return 1
    return 0


ans = 0
while True:
    until = 0
    visited = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                until += bfs(i, j)

    if until == N**2:
        break

    ans += 1

print(ans)
