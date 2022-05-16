from collections import deque

# 큐 사용!!!!

def bfs(graph, start, visited):     # 필요 : 전체 그래프, BFS-DFS 시작 노드번호, 방문표시 리스트
    
    queue = deque([start])          # 큐를 생성하고 시작노드를 넣는다.
    visited[start] = True           # 시작노드는 탐색을 했으므로 방문표시 한다.

    while queue:                    # 큐가 빌 때 까지 반복한다
        v = queue.popleft()         # 큐에서 하나 pop해서 
        print(v, end=' ')           # 출력하고(탐색했음)

        for i in graph[v]:          # 큐에서 가져온 노드의 인접노드들 반복
            if not visited[i]:      # 만약 인접노드 중 방문하지 않은 노드가 있으면
                queue.append(i)     # 큐에 집어넣고
                visited[i] = True   # 방문표시를 한다.

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

bfs(graph, 1, visited)