# https://www.acmicpc.net/problem/2638

from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def get_inner():
    q = deque([[0, 0]])
    inner = [[True] * m for _ in range(n)]
    inner[0][0] = False
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not (0 <= nx < n and 0 <= ny < m) or not inner[nx][ny]:
                continue
            if graph[nx][ny] == 0:
                q.append([nx, ny])
                inner[nx][ny] = False

    return inner


def is_melting(x, y, inner):
    cnt = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if not (0 <= nx < n and 0 <= ny < m):
            continue
        if graph[nx][ny] == 0 and not inner[nx][ny]:
            cnt += 1

    if cnt >= 2:
        return True
    return False


def melting():
    q = deque([[0, 0]])
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    will_melt = []

    inner = get_inner()
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not (0 <= nx < n and 0 <= ny < m) or visited[nx][ny]:
                continue

            if graph[nx][ny] == 0:
                visited[nx][ny] = True
                q.append([nx, ny])

            elif graph[nx][ny] == 1:
                visited[nx][ny] = True

                if is_melting(nx, ny, inner):
                    will_melt.append([nx, ny])

    for i, j in will_melt:
        graph[i][j] = 0


def counting():
    cnt = 0
    for i in graph:
        cnt += i.count(1)
    return cnt


hour = 0
while counting() > 0:
    melting()
    hour += 1

print(hour)
