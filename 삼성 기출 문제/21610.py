# https://www.acmicpc.net/problem/21610

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
command = [list(map(int, input().split())) for _ in range(M)]
clouds = [[N-1, 0], [N-2, 0], [N-1, 1], [N-2, 1]]

dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

for d, s in command:
    
    moved_cloud = []
    visited = [[False]*N for _ in range(N)]
    while clouds:
        x, y = clouds.pop()
        nx, ny = (x+dx[d]*s) % N, (y+dy[d]*s) % N
        graph[nx][ny] += 1
        visited[nx][ny] = True
        moved_cloud.append([nx, ny])

    for x, y in moved_cloud:
        cnt = 0
        for i in range(2, 9, 2):
            nx, ny = x+dx[i], y+dy[i]
            if not(0 <= nx < N and 0 <= ny < N):
                continue
            if graph[nx][ny] != 0:
                cnt += 1

        graph[x][y] += cnt

    for i in range(N):
        for j in range(N):
            if graph[i][j] > 1 and not visited[i][j]:
                graph[i][j] -= 2
                clouds.append([i, j])

ans = 0
for x in graph:
    ans += sum(x)
print(ans)


# 35번째 줄에 not in list -> 이거때문에 시간 초과됨.