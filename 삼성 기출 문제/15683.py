# https://www.acmicpc.net/problem/15683

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

cctv = []
for i in range(N):
    for j in range(M):
        if 0 < graph[i][j] < 6:
            cctv.append([i, j, graph[i][j]])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
directions = [
    [],
    [[0], [1], [2], [3]],
    [[0, 1], [2, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 2, 3], [0, 1, 3], [1, 2, 3], [0, 1, 2]],
    [[0, 1, 2, 3]]
]

ans = 10987654321

def dfs(depth, m):
    global ans

    if depth == len(cctv):
        cnt = 0
        for i in graph:
            for j in i:
                if j == 0:
                    cnt += 1
        ans = min(ans, cnt)
        return

    
    x, y, ctype = cctv[depth]
    for direction in directions[ctype]:
        for d in direction:
            for i in d:
                cx, cy = x, y
                while True:
                    nx, ny = x+dx[i], y+dy[i]
                    if not(0 <= nx < N and 0 <= ny < M) or m[nx][ny] == 6:
                        break
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = '#'
                    cx, cy = nx, ny


    


print(ans)