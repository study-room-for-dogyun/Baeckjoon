# https://www.acmicpc.net/problem/17142

from itertools import combinations
from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
active_virus = [[0] * N for _ in range(N)]
ans = 10e9

virus = []
for x in range(N):
    for y in range(N):
        if graph[x][y] == 2:
            virus.append([x, y])
            graph[x][y] = 0
            active_virus[x][y] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(m, start, active):
    global ans

    q = deque()
    print(start)
    for i, j in start:
        m[i][j] = 1
        active[i][j] = 2
        q.append([i, j])

    time = 0
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not (0 <= nx < N and 0 <= ny < N):
                continue

            if m[nx][ny] == 0:
                if active[nx][ny] == 1:
                    m[nx][ny] = m[x][y]
                    active[nx][ny] = 2
                elif active[nx][ny] == 0:
                    m[nx][ny] = m[x][y] + 1
                q.append([nx, ny])

    for i in m:
        if 0 in i:
            return -1
        time = max(time, max(i)-1)
        print(i)
    print(time)
    print()

    return time


for selected_idx in combinations(virus, M):
    temp = [i[:] for i in graph]
    ans = min(ans, bfs(temp, selected_idx, active_virus))

print(ans)
