# https://www.acmicpc.net/problem/15683

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [
    [],
    [[-1], [0], [1], [0]],
    [[0, 0], [-1, 1]],
    [[-1, 0], [0, 1], [1, 0], [0, -1]],
    [[-1, 0, 0], [0, -1, 1], [1, 0, 0], [0, 1, -1]],
    [[-1, 0, 1, 0]]
]
dy = [
    [],
    [[0], [1], [0], [-1]],
    [[-1, 1], [0, 0]],
    [[0, 1], [1, 0], [0, -1], [-1, 0]],
    [[0, -1, 1], [1, 0, 0], [0, 1, -1], [-1, 0, 0]],
    [[0, 1, 0, -1]]
]

ans = 10e9


def dfs(m, cnt):
    global ans

    if cnt == len(cctv):
        temp = 0
        for i in m:
            temp += i.count(0)
        ans = min(ans, temp)
        return

    sx, sy, t = cctv[cnt]

    for d in range(len(dx[t])):  # CCTV에 대한 방향 개수

        check = []
        for i in range(len(dx[t][d])):  # 해당 화살표 개수
            x, y = sx, sy
            while True:
                nx, ny = x + dx[t][d][i], y + dy[t][d][i]
                if not (0 <= nx < N and 0 <= ny < M) or m[nx][ny] == 6:
                    break
                if m[nx][ny] == 0:
                    m[nx][ny] = '#'
                    check.append([nx, ny])
                x, y = nx, ny

        dfs(m, cnt + 1)

        # 이전에 했던 감시구역 색칠해제
        for i, j in check:
            m[i][j] = 0


cctv = []
for i in range(N):
    for j in range(M):
        if 0 < graph[i][j] < 6:
            cctv.append([i, j, graph[i][j]])

dfs(graph, 0)

print(ans)
