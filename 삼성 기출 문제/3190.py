# https://www.acmicpc.net/problem/3190

from collections import deque

N = int(input())
K = int(input())
graph = [[0] * N for _ in range(N)]
for _ in range(K):
    i, j = map(int, input().split())
    graph[i - 1][j - 1] = 4

L = int(input())
commands = [list(map(str, input().split())) for _ in range(L)]

# 북쪽부터 시계방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

d = 1

time = 0
cnt = 0
graph[0][0] = 1
q = deque([[0, 0]])

while True:
    time += 1

    x, y = q[-1]
    nx, ny = x + dx[d], y + dy[d]

    if not (0 <= nx < N and 0 <= ny < N) or graph[nx][ny] == 1:
        break

    if graph[nx][ny] != 4:
        tx, ty = q.popleft()
        graph[tx][ty] = 0

    graph[nx][ny] = 1
    q.append([nx, ny])

    if time == int(commands[cnt][0]):
        if commands[cnt][1] == 'L':
            d = (d - 1) % 4
        else:
            d = (d + 1) % 4
        cnt = (cnt + 1) % len(commands)

print(time)
