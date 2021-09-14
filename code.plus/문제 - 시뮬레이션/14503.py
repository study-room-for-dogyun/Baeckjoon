from collections import deque

n, m = map(int, input().split())
x, y, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 0  1  2  3 
# 북 동 남 서
# <-- 반시계방향 회전
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def bfs():
    global d
    result = 0
    q = deque([[x, y]])
    graph[x][y] = 2

    while q:

        cx, cy = q.popleft()

        # 네 방향 모두 청소나 벽이면 (벽 1, 청소 2)
        cnt = 0
        for i in range(4):
            tx = cx + dx[i]
            ty = cy + dy[i]
            if not(0 <= tx < n and 0 <= ty < m):
                cnt += 1
                continue

            if graph[tx][ty] == 1 or graph[tx][ty] == 2:
                cnt += 1
        
        if cnt == 4:
            l = d + 2
            if l > 3:
                l %= 2
            if graph[cx + dx[l]][cy + dy[l]] == 1:
                return result
            q.append([cx + dx[l], cy + dy[l]])
            continue

        # 왼쪽으로 회전
        d -= 1
        if d < 0:
            d = 3

        nx = cx + dx[d]
        ny = cy + dy[d]

        # 범위 벗어나면
        if not(0 <= nx < n and 0 <= ny < m):
            continue

        # 왼쪽에 청소할 게 있으면
        if graph[nx][ny] == 0:
            graph[nx][ny] = 2
            result += 1
            q.append([nx, ny])
            continue

    
    return result

print(bfs())