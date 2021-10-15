# https://www.acmicpc.net/problem/17144

R, C, T = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(R)]

# 공기청정기 위치 확인
for i in range(R):
    if graph[i][0] == -1:
        c1, c2 = i, i+1
        break

# 미세먼지 확산
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def spread():
    check = []
    for i in range(R):
        for j in range(C):
            if graph[i][j] > 0:
                check.append([i, j, graph[i][j]])

    for x, y, m in check:
        cnt = 0
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if not(0 <= nx < R and 0 <= ny < C) or graph[nx][ny] == -1:
                continue

            graph[nx][ny] += m//5
            cnt += m//5
        graph[x][y] -= cnt

# 공기청정기 작동
def cleaner_on():

    # 위쪽
    for i in range(c1-1, 0, -1):
        graph[i][0] = graph[i-1][0]
    for i in range(0, C-1):
        graph[0][i] = graph[0][i+1]
    for i in range(0, c1+1):
        graph[i][C-1] = graph[i+1][C-1]
    for i in range(C-1, 1, -1):
        graph[c1][i] = graph[c1][i-1]
    graph[c1][1] = 0

    # 아래쪽
    for i in range(c2+1, R-1):
        graph[i][0] = graph[i+1][0]
    for i in range(0, C-1):
        graph[R-1][i] = graph[R-1][i+1]
    for i in range(R-1, c2, -1):
        graph[i][C-1] = graph[i-1][C-1]
    for i in range(C-1, 1, -1):
        graph[c2][i] = graph[c2][i-1]
    graph[c2][1] = 0


for _ in range(T):
    spread()
    cleaner_on()

ans = 2
for i in graph:
    ans += sum(i)
print(ans)