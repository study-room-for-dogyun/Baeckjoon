from collections import deque

C = int(input())
answer = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(graph):
    distance = [[10e9] * N for _ in range(N)]
    distance[0][0] = 0
    q = deque([[0, 0]])

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not (0 <= nx < N and 0 <= ny < N):
                continue

            if distance[nx][ny] > graph[nx][ny] + distance[x][y]:
                distance[nx][ny] = graph[nx][ny] + distance[x][y]
                q.append([nx, ny])

    return distance[N - 1][N - 1]


for _ in range(C):
    N = int(input())
    graph = [list(map(int, input())) for _ in range(N)]
    answer.append(bfs(graph))

for idx, i in enumerate(answer):
    print(f'#{idx + 1} {i}')
