# https://www.acmicpc.net/problem/16236
from collections import deque

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
ans = 0

# Init shark info
shark_size = 2
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            shark_x, shark_y = i, j
            graph[i][j] = 0
            break

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def move_to(gx, gy):
    global shark_x, shark_y, ans

    m = [[0] * N for _ in range(N)]
    m[shark_x][shark_y] = 1

    q = deque([[shark_x, shark_y]])
    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if not (0 <= nx < N and 0 <= ny < N) or graph[nx][ny] > shark_size or m[nx][ny] != 0:
                continue

            if [nx, ny] == [gx, gy]:
                shark_x, shark_y = gx, gy
                graph[nx][ny] = 0
                ans += m[cx][cy]
                return

            m[nx][ny] = m[cx][cy] + 1
            q.append([nx, ny])


def find_shortest_fish():
    shortest = 10e9
    m = [[0] * N for _ in range(N)]
    m[shark_x][shark_y] = 1
    q = deque([[shark_x, shark_y]])

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if not (0 <= nx < N and 0 <= ny < N) or graph[nx][ny] > shark_size or m[nx][ny] != 0:
                continue

            m[nx][ny] = m[cx][cy] + 1
            q.append([nx, ny])

    check = []
    for x, y in can_eat:
        if 0 < m[x][y] < shortest:
            shortest = m[x][y]
            check = [[x, y]]
        elif 0 < m[x][y] == shortest:
            shortest = m[x][y]
            check.append([x, y])

    check.sort()
    if not check:
        return False
    return check[0]


eat_cnt = 0
while True:
    can_eat = []
    for i in range(N):
        for j in range(N):
            if 0 < graph[i][j] < shark_size:
                can_eat.append([i, j])

    if not can_eat:
        break
    else:
        position = find_shortest_fish()
        if not position:
            break
        x, y = position
        move_to(x, y)
        eat_cnt += 1

    if eat_cnt == shark_size:
        shark_size += 1
        eat_cnt = 0

print(ans)