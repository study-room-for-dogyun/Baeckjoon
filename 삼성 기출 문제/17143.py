# https://www.acmicpc.net/problem/17143
R, C, M = map(int, input().split())
graph = [[[] for _ in range(C)] for _ in range(R)]
for _ in range(M):
    _r, _c, _s, _d, _z = map(int, input().split())
    graph[_r - 1][_c - 1].append([_z, _d - 1, _s])

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def move_shark():
    temp = []
    for x in range(R):
        for y in range(C):

            if graph[x][y]:
                z, d, s = graph[x][y].pop()
                cx, cy = x, y
                for _ in range(s):
                    nx, ny = cx + dx[d], cy + dy[d]
                    if not (0 <= nx < R and 0 <= ny < C):
                        d = d + 1 if d % 2 == 0 else d - 1
                        nx, ny = cx + dx[d], cy + dy[d]

                    cx, cy = nx, ny

                temp.append([cx, cy, z, d, s])

    for x, y, z, d, s in temp:
        if not graph[x][y] or max(graph[x][y])[0] < z:
            graph[x][y] = [[z, d, s]]


def catch_shark(king_position):
    for x in range(R):
        if graph[x][king_position]:
            size = graph[x][king_position][0][0]
            graph[x][king_position] = []
            return size
    return 0


ans = 0
for king_position in range(C):
    ans += catch_shark(king_position)
    move_shark()

print(ans)
