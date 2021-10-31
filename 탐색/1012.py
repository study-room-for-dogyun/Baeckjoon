# https://www.acmicpc.net/problem/1012

from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(sx, sy):

    q = deque([[sx, sy]])
    graph[sx][sy] = 0
    while q:
        cx, cy = q.popleft()

        for i in range(4):

            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append([nx, ny])


for _ in range(t):

    # INPUT
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        y, x = map(int, input().split())
        graph[x][y] = 1


    # OUTPUT
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)

    


