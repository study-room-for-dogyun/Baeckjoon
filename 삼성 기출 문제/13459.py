# https://www.acmicpc.net/problem/13459
from collections import deque

N, M = map(int, input().split())
graph = [list(map(str, input())) for _ in range(N)]
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque()


def init():
    rx, ry, bx, by = 0, 0, 0, 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 'R':
                rx, ry = i, j
            elif graph[i][j] == 'B':
                bx, by = i, j
    q.append([rx, ry, bx, by, 0])
    visited[rx][ry][bx][by] = True


def move(x, y, d):
    c = 0
    while graph[x + dx[d]][y + dy[d]] != '#' and graph[x][y] != 'O':
        x += dx[d]
        y += dy[d]
        c += 1
    return x, y, c


def bfs():
    while q:
        rx, ry, bx, by, cnt = q.popleft()
        if cnt >= 10:
            break

        for i in range(4):
            nrx, nry, rc = move(rx, ry, i)
            nbx, nby, bc = move(bx, by, i)

            if graph[nbx][nby] == 'O':
                continue
            if graph[nrx][nry] == 'O':
                return 1
            if [nrx, nry] == [nbx, nby]:
                if rc > bc:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]
            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = True
                q.append([nrx, nry, nbx, nby, cnt + 1])

    return 0


init()
print(bfs())
