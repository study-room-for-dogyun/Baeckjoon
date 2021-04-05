# https://www.acmicpc.net/problem/3055

from collections import deque

r, c = map(int, input().split())
graph = [list(map(str, input())) for _ in range(r)]


def s_water(graph):
    water = []
    for i in range(r):
        for j in range(c):
            if graph[i][j] == '*':
                water.append([i, j])
            
    return water

def ds(graph):
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 'S':
                sx, sy = i, j
            if graph[i][j] == 'D':
                dx, dy = i, j
    
    return sx, sy, dx, dy

def bfs(str_x, str_y, dst_x, dst_y):
    #    U  D   L  R
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    graph[str_x][str_y] = 0

    water = deque()
    queue = deque()
    queue.append([str_x, str_y])
    for i in s_water(graph):
        water.append(i)


    while queue:

        for _ in range(len(water)):     # 현재 물 다 쓰기
            wx, wy = water.popleft()

            for i in range(4):
                nx = wx + dx[i]
                ny = wy + dy[i]
                if 0 <= nx < r and 0 <= ny < c:
                    if graph[nx][ny] != 'X' and graph[nx][ny] != 'D':
                        graph[nx][ny] = '*'
                        water.append([nx, ny])   # 다음 물 위치 임시저장
        
        for _ in range(len(queue)):     # 고슴도치 이동
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < r and 0 <= ny < c:
                    if graph[nx][ny] == 'D':
                        return graph[x][y] + 1

                    if graph[nx][ny] == '.':
                        graph[nx][ny] = graph[x][y] + 1
                        queue.append([nx, ny])
        
    
    return False


sx, sy, dx, dy = ds(graph)
result = bfs(sx, sy, dx, dy)

if not result:
    print("KAKTUS")
else:
    print(result)