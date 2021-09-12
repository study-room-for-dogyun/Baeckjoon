# https://www.acmicpc.net/problem/14502
from collections import deque


# INPUT
n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]


# Solution

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def count_safe_area(graph):
    count = 0

    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == 0:
                count += 1

    return count

def virus_position(graph):
    l = []
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == 2:
                l.append([i, j])
    return l

def bfs(graph):
    visited = [[False] * m for _ in range(n)]
    q = deque()
    for virus in virus_position(graph):
        q.append(virus)
        visited[virus[0]][virus[1]] = True

    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if not(0 <= nx < n and 0 <= ny < m):
                continue
            if visited[nx][ny]:
                continue
            if graph[nx][ny] == 1:
                continue

            graph[nx][ny] = 2
            visited[nx][ny] = True
            q.append([nx, ny])
        
        
    return count_safe_area(graph)

# 좌표 3개 조합으로 뽑기

# 1. 벽 세울 수 있는 좌표 저장
geo = []
for x in range(n):
    for y in range(m):
        if maps[x][y] == 0:
            geo.append([x, y])


# 2. 좌표 중 3개씩 조합
answer = 0
for i in range(len(geo)):
    for j in range(i+1, len(geo)):
        for k in range(j+1, len(geo)):
            # 좌표에 벽 세우기
            maps[geo[i][0]][geo[i][1]] = 1
            maps[geo[j][0]][geo[j][1]] = 1
            maps[geo[k][0]][geo[k][1]] = 1

            g = []
            for l in maps:
                g.append(l[:])

            # 바이러스 퍼뜨리기
            answer = max(bfs(g), answer)

            # 다시 되돌리기
            maps[geo[i][0]][geo[i][1]] = 0
            maps[geo[j][0]][geo[j][1]] = 0
            maps[geo[k][0]][geo[k][1]] = 0


# OUTPUT
print(answer)