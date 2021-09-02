# https://www.acmicpc.net/problem/3197
from collections import deque

x, y = map(int, input().split())
graph = [list(map(str, input())) for _ in range(x)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def find_L():
    for i in range(x):
        for j in range(y):
            if graph[x][y] == 'L':
                return [i, j]

def bfs(sx, sy, visited):
    melt_list = []
    q = deque([[sx, sy]])

    while q:
        cx, cy = q.popleft()

        # if graph[cx][cy] == 'X':
        #     continue

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if not(0 <= nx < x and 0 <= ny < y):
                continue

            if graph[nx][ny] == 'L':
                continue

            if graph[nx][ny] == 'X':
                # graph[nx][ny] = '.'
                melt_list.append([nx, ny])
                visited[nx][ny] = True
                continue
            
            q.append([nx, ny])
            visited[nx][ny] = True
    
    return melt_list, visited

def melt():
    global x, y

    l = []
    visited = [[False] * y for _ in range(x)]
    
    for i in range(x):
        for j in range(y):
            if graph[i][j] == '.':
                temp, visited = bfs(i, j, visited)
                l += temp
    
    for x, y in l:
        graph[x][y] = '.'

    for i in visited:
        print(i)


melt()
for i in graph:
    print(" ".join(i))


print()


melt()
for i in graph:
    print(" ".join(i))