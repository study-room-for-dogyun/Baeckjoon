n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):                                  # 탐색 시작지점 좌표

    if x <= -1 or x >= n or y <= -1 or y >= m:  # 더이상 나아갈 수 없으면 False
        return False

    if graph[x][y] == 0:            # 만약 좌표가 방문하지 않은 노드라면
        graph[x][y] = 1             # 방문표시를 하고                    

        dfs(x, y + 1)               # 인접노드에 대해 탐색
        dfs(x, y - 1)               # 인접노드에 대해 탐색
        dfs(x + 1, y)               # 인접노드에 대해 탐색
        dfs(x - 1, y)               # 인접노드에 대해 탐색
        return True                 # 모든 인접노드가 다 탐색됐으면 True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)