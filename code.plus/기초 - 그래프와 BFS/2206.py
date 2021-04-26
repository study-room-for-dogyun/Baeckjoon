# https://www.acmicpc.net/problem/2206

from collections import deque
import sys

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            graph[i][j] = 'X'

def bfs(graph):

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    queue = deque()
    queue.append([0, 0])
    graph[0][0] = 1

    broke = True        # 부수는 기회 단 1번
    while queue:
        x, y = queue.popleft()
        if [x, y] == [n-1, m-1]:
            return graph[x][y]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 'X' and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])

        

        if not queue and broke == True:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 'X':
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append([nx, ny])
            
            broke = False

    return False

result = bfs(graph)
print(result if result else -1)