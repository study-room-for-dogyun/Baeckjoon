n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

maxi = 0
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(value, depth, x, y):
    global maxi, visited

    if depth == 4:
        maxi = max(maxi, value)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not(0 <= nx < n and 0 <= ny < m) or visited[nx][ny]:
            continue
        
        visited[nx][ny] = True
        dfs(value+graph[nx][ny], depth+1, nx, ny)
        visited[nx][ny] = False

def fuck(x, y):
    global maxi

    # ㅗ
    if 1 <= x < n-1 and 1 <= y < m:
        maxi = max(maxi, graph[x-1][y]+graph[x][y]+graph[x+1][y]+graph[x][y-1])
    # ㅓ
    if 1 <= x < n and 1 <= y < m-1:
        maxi = max(maxi, graph[x-1][y]+graph[x][y]+graph[x][y-1]+graph[x][y+1])
    # ㅏ
    if 0 <= x < n-1 and 1 <= y < m-1:
        maxi = max(maxi, graph[x][y]+graph[x][y-1]+graph[x][y+1]+graph[x+1][y])
    # ㅜ
    if 1 <= x < n-1 and 0 <= y < m-1:
        maxi = max(maxi, graph[x][y]+graph[x-1][y]+graph[x+1][y]+graph[x][y+1])

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(graph[i][j], 1, i, j)
        visited[i][j] = False

        fuck(i, j)

print(maxi)