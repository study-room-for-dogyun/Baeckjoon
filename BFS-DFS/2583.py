# https://www.acmicpc.net/problem/2583

M, N, K = map(int, input().split())
graph = [[0] * N for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1


def bfs(sx, sy):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    s = [[sx, sy]]
    total = 1
    while s:
        x, y = s.pop()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not (0 <= nx < M and 0 <= ny < N) or graph[nx][ny] == 1:
                continue

            graph[nx][ny] = 1
            total += 1
            s.append([nx, ny])
    return total


cnt = 0
area = []
for i in range(M):
    for j in range(N):
        if graph[i][j] == 1:
            continue
        graph[i][j] = 1
        area.append(bfs(i, j))
        cnt += 1

print(cnt)
print(" ".join(list(map(str, sorted(area)))))
