# https://www.acmicpc.net/problem/13460
from collections import deque

N, M = map(int, input().split())
graph = [list(map(str, input())) for _ in range(N)]
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque()


def init():
    rx, ry, bx, by = [0] * 4
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 'R':
                rx, ry = i, j
            elif graph[i][j] == 'B':
                bx, by = i, j
    q.append([rx, ry, bx, by, 0])
    visited[rx][ry][bx][by] = True


def move(x, y, dx, dy, c):
    # c : 이동한 횟수
    while graph[x + dx][y + dy] != '#' and graph[x][y] != 'O':
        x += dx
        y += dy
        c += 1
    return x, y, c


def bfs():
    while q:
        rx, ry, bx, by, d = q.popleft()
        if d >= 10:
            break
        for i in range(4):
            nrx, nry, rc = move(rx, ry, dx[i], dy[i], 0)
            nbx, nby, bc = move(bx, by, dx[i], dy[i], 0)
            if graph[nbx][nby] == 'O':
                continue
            if graph[nrx][nry] == 'O':
                print(d + 1)
                return
            if nrx == nbx and nry == nby:
                if rc > bc:
                    nrx, nry = nrx - dx[i], nry - dy[i]
                else:
                    nbx, nby = nbx - dx[i], nby - dy[i]
            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = True
                q.append([nrx, nry, nbx, nby, d + 1])
    print(-1)


init()
bfs()

# 기울이는 방향의 조합에 따른 백트래킹 문제로 생각할 수 있지만 실상은 그게 아니었다.
# BFS에 의한 최단거리인데 그 때 하나가 아닌 두 개로 조작하는 것임.

