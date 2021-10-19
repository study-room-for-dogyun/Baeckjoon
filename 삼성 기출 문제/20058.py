# https://www.acmicpc.net/problem/20058
from collections import deque

N, Q = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(2 ** N)]
L = list(map(int, input().split()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def rotate(level):
    s = 2 ** level
    for i in range(2 ** N // s):
        for j in range(2 ** N // s):
            temp = []
            for k in range(j * s, (j + 1) * s):
                temp.append(graph[k][i * s:(i + 1) * s])
            temp = list(zip(*temp[::-1]))
            cnt = 0
            for k in range(j * s, (j + 1) * s):
                graph[k][i * s:(i + 1) * s] = temp[cnt]
                cnt += 1


def melting():
    check = []
    for x in range(2 ** N):
        for y in range(2 ** N):
            cnt = 0
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if not (0 <= nx < 2 ** N and 0 <= ny < 2 ** N) or graph[nx][ny] == 0:
                    continue
                cnt += 1
            if cnt < 3 and graph[x][y] > 0:
                check.append([x, y])

    for x, y in check:
        graph[x][y] -= 1


def counting(x, y):
    cnt = 1
    q = deque([[x, y]])
    graph[x][y] = 0
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if not (0 <= nx < 2 ** N and 0 <= ny < 2 ** N) or graph[nx][ny] == 0:
                continue
            q.append([nx, ny])
            graph[nx][ny] = 0
            cnt += 1
    return cnt


for i in L:
    rotate(i)
    melting()

ices = 0
total_ice = 0
for i in graph:
    total_ice += sum(i)

for i in range(2 ** N):
    for j in range(2 ** N):
        if graph[i][j] != 0:
            ices = max(ices, counting(i, j))

print(total_ice, ices, sep='\n')
