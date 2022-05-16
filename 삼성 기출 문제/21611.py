# https://www.acmicpc.net/problem/21611

from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
root = []
result = [1, 0, 0, 0]


def p():
    for i in graph:
        print(i)
    print()


def set_root():
    sx, sy = N // 2, N // 2
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    d = -1
    for i in range(2 * N):
        for _ in range((i % 2 + i) // 2):
            root.append([sx, sy])
            sx, sy = sx + dx[d], sy + dy[d]
        d = (d + 1) % 4


def blizzard():
    sx, sy = N // 2, N // 2
    dx = [0, -1, 1, 0, 0]
    dy = [0, 0, 0, -1, 1]
    for _ in range(S):
        sx, sy = sx + dx[D], sy + dy[D]
        graph[sx][sy] = 0

    s = deque([0])
    for x, y in root:
        if graph[x][y] != 0:
            s.append(graph[x][y])

    re_arrange()


def re_arrange():
    s = deque([0])
    for x, y in root:
        if graph[x][y] != 0:
            s.append(graph[x][y])
    for x, y in root:
        if s:
            graph[x][y] = s.popleft()
        else:
            graph[x][y] = 0


def boom():
    is_boom = False
    temp = []
    for i in range(len(root) - 1):
        x, y = root[i]
        nx, ny = root[i + 1]

        if graph[x][y] == graph[nx][ny]:
            temp.append([x, y])
        else:
            if len(temp) >= 3:
                temp.append([x, y])
                # print(temp)
                is_boom = True
                for p, q in temp:
                    result[graph[p][q]] += 1
                    graph[p][q] = 0
            temp = []

    return is_boom


def change():
    origin = deque()
    for x, y in root[1:]:
        if graph[x][y] == 0:
            break
        origin.append(graph[x][y])

    new = deque([0])
    cnt = 1
    while origin:
        group = origin.popleft()

        if not origin:
            new.append(1)
            new.append(group)
            break

        if origin[0] == group:
            cnt += 1
        else:
            new.append(cnt)
            new.append(group)
            cnt = 1

    for x, y in root:
        if new:
            graph[x][y] = new.popleft()
        else:
            graph[x][y] = 0


def answer():
    return result[1] + result[2] * 2 + result[3] * 3


set_root()
for _ in range(M):
    D, S = map(int, input().split())
    # p()
    blizzard()
    # p()
    while boom():
        re_arrange()
    # p()
    change()
    # p()

print(answer())
