# https://www.acmicpc.net/problem/17142

from collections import deque
from itertools import combinations

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
virus = []
virus_map = [[False] * N for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def init():
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                graph[i][j] = '#'
            if graph[i][j] == 2:
                virus_map[i][j] = True
                virus.append([i, j])


def bfs(graph, v):
    global ans
    visited = [[False] * N for _ in range(N)]
    for i, j in v:
        visited[i][j] = True
        graph[i][j] = 0
    q = deque(v)

    result = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not (0 <= nx < N and 0 <= ny < N) or graph[nx][ny] == '#':
                continue

            if not visited[nx][ny]:
                graph[nx][ny] = graph[x][y] + 1
                q.append([nx, ny])
                visited[nx][ny] = True
            else:
                if graph[nx][ny] > graph[x][y] + 1:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append([nx, ny])
                    visited[nx][ny] = True

            if not virus_map[nx][ny]:
                result = max(result, graph[nx][ny])

            if result > ans:
                return

    if check(graph):
        ans = min(ans, result)


def check(graph):
    zero_cnt = 0
    for i in graph:
        zero_cnt += i.count(0)
        if zero_cnt > M:
            return False
    return True


init()

ans = 10e9
for i in combinations(virus, M):
    temp = [i[:] for i in graph]
    bfs(temp, i)

print(ans if ans != 10e9 else -1)
