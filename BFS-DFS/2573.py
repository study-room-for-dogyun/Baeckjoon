# https://www.acmicpc.net/problem/2573
from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, visited):
    q = deque([[x, y]])
    visited[x][y] = True

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if not (0 <= nx < N and 0 <= ny < M) or visited[nx][ny] or graph[nx][ny] == 0:
                continue

            q.append([nx, ny])
            visited[nx][ny] = True


def check():
    visited = [[False] * M for _ in range(N)]
    cnt = 0
    for x in range(N):
        for y in range(M):
            if graph[x][y] != 0 and not visited[x][y]:
                cnt += 1
                dfs(x, y, visited)

    return cnt


def melting():
    melt_list = []
    for x in range(N):
        for y in range(M):
            if graph[x][y] != 0:
                cnt = 0
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if not (0 <= nx < N and 0 <= ny < M) or graph[nx][ny] != 0:
                        continue
                    cnt += 1
                melt_list.append([x, y, cnt])

    for x, y, cnt in melt_list:
        graph[x][y] -= cnt
        if graph[x][y] < 0:
            graph[x][y] = 0


ans = 0
while check() == 1 and check() != 0:
    melting()
    ans += 1

if check() == 0:
    print(0)
else:
    print(ans)
