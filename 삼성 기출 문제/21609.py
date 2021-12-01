# https://www.acmicpc.net/problem/21609

from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def group_size(x, y, visited):
    visited[x][y] = True
    group_head = graph[x][y]
    size = 1
    rainbow = []

    q = deque([[x, y]])
    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if not (0 <= nx < N and 0 <= ny < N) or visited[nx][ny]:
                continue

            if graph[nx][ny] != group_head:
                if graph[nx][ny] == 0:
                    rainbow.append([nx, ny])
                else:
                    continue

            size += 1
            q.append([nx, ny])
            visited[nx][ny] = True

    for i, j in rainbow:
        visited[i][j] = False

    return [size, len(rainbow)]


def remove_group(x, y):
    global graph

    head = graph[x][y]
    graph[x][y] = -2
    q = deque([[x, y]])
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if not (0 <= nx < N and 0 <= ny < N) or graph[nx][ny] < 0:
                continue

            if graph[nx][ny] == 0 or graph[nx][ny] == head:
                graph[nx][ny] = -2
                q.append([nx, ny])


def find_biggest_block_group():
    biggest_pos = [0, 0]
    biggest_size = [0, 0]
    visited = [[False] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if visited[i][j] or graph[i][j] <= 0:
                continue
            result = group_size(i, j, visited)

            if result[0] > biggest_size[0]:
                biggest_size = result
                biggest_pos = [i, j]
            elif result[0] == biggest_size[0]:
                if result[1] >= biggest_size[1]:
                    biggest_size = result
                    biggest_pos = [i, j]

    remove_group(biggest_pos[0], biggest_pos[1])

    return biggest_size[0]


def gravity():
    global graph

    for i in range(N - 2, -1, -1):
        for j in range(N):
            if graph[i][j] > -1:
                r = i
                while True:
                    if r + 1 < N and graph[r + 1][j] == -2:
                        graph[r + 1][j] = graph[r][j]
                        graph[r][j] = -2
                        r += 1
                    else:
                        break


def rotate():
    global graph
    graph = list(map(list, zip(*graph)))[::-1]


if __name__ == "__main__":
    score = 0
    while True:
        biggest_group_size = find_biggest_block_group()
        if biggest_group_size < 2:
            break

        score += biggest_group_size ** 2
        gravity()
        rotate()
        gravity()

    print(score)
