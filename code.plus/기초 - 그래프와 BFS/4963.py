# https://www.acmicpc.net/problem/4963
import sys

sys.setrecursionlimit(5000)
graphs = []
sizes = []

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    sizes.append([w, h])

    graph = []
    for i in range(h):
        graph.append(list(map(int, input().split())))

    graphs.append(graph)


def dfs(graph, x, y, w, h):

    if x <= -1 or x >= h or y <= -1 or y >= w:
        return False
    
    if graph[x][y] == 1:
        graph[x][y] = 0

        dfs(graph, x+1, y, w, h)
        dfs(graph, x-1, y, w, h)
        dfs(graph, x, y+1, w, h)
        dfs(graph, x, y-1, w, h)
        dfs(graph, x+1, y+1, w, h)
        dfs(graph, x+1, y-1, w, h)
        dfs(graph, x-1, y+1, w, h)
        dfs(graph, x-1, y-1, w, h)
        return True     # 위의 재귀함수들이 다 True이면
    
    return False



for i in range(len(sizes)):
    result = 0

    for j in range(sizes[i][1]):
        for k in range(sizes[i][0]):
            if dfs(graphs[i], j, k, sizes[i][0], sizes[i][1]) == True:
                result += 1

    print(result)
    
