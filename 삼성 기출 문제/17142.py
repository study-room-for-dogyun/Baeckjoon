# https://www.acmicpc.net/problem/17142

from itertools import combinations
from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
ans = 10e9

virus = []
for x in range(N):
    for y in range(N):
        if graph[x][y] == 2:
            virus.append([x, y])
            graph[x][y] = 'v'
        if graph[x][y] == 1:
            graph[x][y] = '#'


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(m, start):
    global ans

    q = deque()
    for i in start:
        m[virus[i][0]][virus[i][1]] = 0
        q.append(virus[i])

    time = 0
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if not(0 <= nx < N and 0 <= ny < N) or m[nx][ny] != 0:
                continue

            if m[nx][ny] == 'v':
                m[nx][ny] = m[x][y]
            else:
                m[nx][ny] = m[x][y]+1
            time = max(time, m[nx][ny])

            q.append([nx, ny])

    ans = min(ans, time)

for seleted_idx in combinations(list(range(len(virus))), M):
    temp = [item[:] for item in graph]
    bfs(temp, seleted_idx)


print(ans)