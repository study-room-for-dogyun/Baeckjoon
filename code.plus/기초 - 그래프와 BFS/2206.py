# https://www.acmicpc.net/problem/2206

from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()

x, y = map(int, input().split())
graph = [list(map(str, input())) for _ in range(x)]
# visited = [[False] * y for _ in range(x)]
# cnt = [[0] * y for _ in range(x)]

def bfs(sx, sy):
    graph[sx][sy] = 0
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    q = deque([[sx, sy, 0]])

    while q:
        cx, cy, cb = q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if not(0 <= nx < x and 0 <= ny < y):
                continue
        
            if type(graph[nx][ny]) == int:
                continue

            if graph[nx][ny] == '0':
                if cb == 0:
                    graph[nx][ny] = int(graph[cx][cy]) + 1
                    q.append([nx, ny, 1])

            else:
                graph[nx][ny] = int(graph[cx][cy]) + 1
                q.append([nx, ny, cb])
        
        for i in graph:
            for j in i:
                if j == '1':
                    print('*', end=" ")
                elif j == '0':
                    print(0, end=" ")
                else:
                    print(j, end=" ")
            print()
        
        print('\n\n\n')

            

    if graph[x-1][y-1] == '0':
        return -1
    else:
        return graph[x-1][y-1] + 1

print(bfs(0, 0))

# for i in graph:
#     for j in i:
#         if j == '1':
#             print('*', end=" ")
#         elif j == '0':
#             print(0, end=" ")
#         else:
#             print(j, end=" ")
#     print()