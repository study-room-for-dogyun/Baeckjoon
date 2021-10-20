# https://www.acmicpc.net/problem/17142

from itertools import combinations
from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
virus_map = [[False] * N for _ in range(N)]

viruses = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            viruses.append([i, j])
            graph[i][j] = 0
            virus_map[i][j] = True

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(m, virus):
    visited = [[False] * N for _ in range(N)]
    for i, j in virus:
        visited[i][j] = True
    q = deque(virus)

    while q:
        cx, cy = q.popleft()
        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            if not (0 <= nx < N and 0 <= ny < N) or visited[nx][ny]:
                continue

            if graph[nx][ny] != 0:
                continue

            if virus_map[cx][cy]:
                if virus_map[nx][ny]:
                    m[cx][cy] += 1
                    m[nx][ny] = m[cx][cy] + 1
                else:
                    m[nx][ny] = m[cx][cy] + 1
            else:
                if virus_map[nx][ny]:
                    m[nx][ny] = m[cx][cy] + 1
                else:
                    m[nx][ny] = m[cx][cy] + 1
            q.append([nx, ny])
            visited[nx][ny] = True

    # 완벽 확산이 안 될 때
    zero_cnt = 0
    for i in m:
        zero_cnt += i.count(0)
    if zero_cnt > len(virus):
        return -1

    time = 0
    for i in m:
        time = max(time, max(i))
    print(time)
    for i in m:
        print(i)
    print()

    return time


shortest_time = 10e9
for selected_viruses in combinations(viruses, M):
    temp = [i[:] for i in graph]
    shortest_time = min(shortest_time, bfs(temp, selected_viruses))

print(shortest_time)