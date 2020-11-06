
# 스택 사용!!!!!!!!!

def dfs(graph, v, visited):
    visited[v] = True               # 현재 노드 방문처리하고
    print(v, end=' ')               # 현재 노드 출력 (탐색 순서가 됨)

    for i in graph[v]:              # 현재 노드에서 인접한 노드들
        if not visited[i]:          # 만약 방문하지 않았다면
            dfs(graph, i, visited)  # 그 노드를 기준으로 다시 재귀

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]    
]

visited = [False] * 9

dfs(graph, 1, visited)