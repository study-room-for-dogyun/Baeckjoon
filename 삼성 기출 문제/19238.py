# https://www.acmicpc.net/problem/19238
from collections import deque

N, M, fuel = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
tx, ty = map(int, input().split())
tx -= 1
ty -= 1
passenger = []
for _ in range(M):
    a, b, c, d = map(int, input().split())
    passenger.append([a - 1, b - 1, c - 1, d - 1])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def find_shortest_passenger(m):
    q = deque([[tx, ty]])
    m[tx][ty] = 1
    shortest = 10e9
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if not (0 <= nx < N and 0 <= ny < N) or m[nx][ny] != 0:
                continue

            m[nx][ny] = m[cx][cy] + 1
            q.append([nx, ny])

    shortest_list = []
    for idx, p in enumerate(passenger):
        i, j = p[0], p[1]
        gx, gy = p[2], p[3]
        if 0 < m[i][j] < shortest:
            shortest = m[i][j]
            shortest_list = [[i, j, gx, gy, m[i][j] - 1, idx]]
        elif shortest == m[i][j]:
            shortest_list.append([i, j, gx, gy, m[i][j] - 1, idx])
    shortest_list.sort()

    if shortest_list:
        return shortest_list[0]
    return False


def move_to(m, gx, gy):
    q = deque([[tx, ty]])
    m[tx][ty] = 1
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if not (0 <= nx < N and 0 <= ny < N) or m[nx][ny] != 0:
                continue

            m[nx][ny] = m[cx][cy] + 1
            q.append([nx, ny])

    return m[gx][gy] - 1


while passenger:
    # tx, ty, des_x, des_y, used1, idx)
    temp = [i[:] for i in graph]
    path_info = find_shortest_passenger(temp)

    if not path_info:
        if passenger:
            fuel = -1
        break
    tx, ty, des_x, des_y, used1, idx = path_info

    del passenger[idx]

    # 손님까지 갈 때 연료 ㅇㅋ?
    fuel -= used1
    if fuel < 0:
        fuel = -1
        break

    temp = [i[:] for i in graph]
    used2 = move_to(temp, des_x, des_y)

    if used2 == -1:
        fuel = -1
        break

    # 목적지까지 갈 때 연료 ㅇㅋ?
    fuel -= used2
    if fuel < 0:
        fuel = -1
        break
    fuel += 2 * used2

    tx, ty = des_x, des_y

print(fuel)
