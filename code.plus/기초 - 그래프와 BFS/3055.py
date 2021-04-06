# https://www.acmicpc.net/problem/3055

from collections import deque
r, c = map(int, input().split())
graph = [list(map(str, input())) for _ in range(r)]


def bfs(graph):
    #    U  D   L  R
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    water = deque()
    queue = deque()


    for i in range(r):          # 물과 고슴도치 시작 위치 저장
        for j in range(c):
            if graph[i][j] == '*':
                water.append([i, j])

            if graph[i][j] == 'S':
                graph[i][j] = 0
                queue.append([i, j])

    ban = 0
    while queue:
        
        for _ in range(len(water)):     # 현재 물 다 쓰기
            x, y = water.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < r and 0 <= ny < c:
                    if graph[nx][ny] != 'X' and graph[nx][ny] != 'D' and graph[nx][ny] != '*' and graph[nx][ny] != ban:     # 세번째 조건을 안 넣으면 메모리초과 뜸
                        graph[nx][ny] = '*'
                        water.append([nx, ny])

        
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
                        ban = graph[x][y] + 1
                        queue.append([nx, ny])
     
    return False



result = bfs(graph)

print(result if result else "KAKTUS")