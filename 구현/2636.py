# https://www.acmicpc.net/problem/2636

from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]


def print_graph():
    for i in graph:
        print(i)
    print()


def melting():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque([[0, 0]])
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not(0 <= nx < n and 0 <= ny < m) or visited[nx][ny]:
                continue

            if graph[nx][ny] == 0:
                visited[nx][ny] = True
                q.append([nx, ny])
            elif graph[nx][ny] == 1:
                visited[nx][ny] = True
                graph[nx][ny] = 0


def counting():
    cnt = 0
    for i in graph:
        cnt += i.count(1)
    return cnt


hour = 0
while True:
    before_cnt = counting()
    melting()
    hour += 1
    if counting() == 0:
        print(hour)
        print(before_cnt)
        break
