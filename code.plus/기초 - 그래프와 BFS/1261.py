# https://www.acmicpc.net/problem/1261

from collections import deque

y, x = map(int, input().split())
graph = [list(map(int, input())) for _ in range(x)]
visited = [[False] * y for _ in range(x)]
cnt = [[0] * y for _ in range(x)]


def bfs(sx, sy):

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    q = deque([[sx, sy]])

    while q:
        cx, cy = q.popleft()
        visited[cx][cy] = True

        now = cnt[cx][cy]

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if not(0 <= nx < x and 0 <= ny < y):
                continue

            if visited[nx][ny]:
                continue

            if graph[nx][ny] == 1:
                cnt[nx][ny] = now + 1
            else:
                cnt[nx][ny] = cnt[cx][cy]

            q.append([nx, ny])



print(bfs(0, 0))

for i in graph:
    print(i)
print(cnt[x-1][y-1])
for i in cnt:
    print(i)
