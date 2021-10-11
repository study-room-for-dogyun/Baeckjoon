# https://www.acmicpc.net/problem/20056
from collections import deque

N, M, K = map(int, input().split())
graph = [[deque() for _ in range(N)] for _ in range(N)]
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    graph[r-1][c-1].append([m, s, d])

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def move(x, y, cnt):
    for _ in range(cnt):
        m, s, d = graph[x][y].popleft()
        nx = (x + dx[d]*s) % N
        ny = (y + dy[d]*s) % N
        graph[nx][ny].append([m, s, d])

def combine(x, y):
    new_m, new_s, check_eo = 0, 0, 0
    ball_cnt = len(graph[x][y])
    while graph[x][y]:
        m, s, d = graph[x][y].popleft()
        new_m += m
        new_s += s
        check_eo = check_eo + 1 if d % 2 == 0 else check_eo - 1

    if new_m // 5 == 0:
        return

    if abs(check_eo) == ball_cnt:
        for i in range(0, 7, 2):
            graph[x][y].append([new_m//5, new_s//ball_cnt, i])
    else:
        for i in range(1, 8, 2):
            graph[x][y].append([new_m//5, new_s//ball_cnt, i])

for _ in range(K):

    check = []
    for i in range(N):
        for j in range(N):
            if len(graph[i][j]) > 0:
                check.append([i, j, len(graph[i][j])])

    for i in check:
        move(i[0], i[1], i[2])

    for i in range(N):
        for j in range(N):
            if len(graph[i][j]) > 1:
                combine(i, j)

answer = 0
for i in range(N):
    for j in range(N):
        while graph[i][j]:
            answer += graph[i][j].popleft()[0]

print(answer)