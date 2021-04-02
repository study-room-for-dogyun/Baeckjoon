# https://www.acmicpc.net/problem/1260
from collections import deque

n, m, v = map(int, input().split())

graph = []
for _ in range(n+1):
    graph.append([])

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def dfs(v, visit):

    visit[v] = True
    print(v, end=' ')
    
    for i in sorted(graph[v]):
        if not visit[i]:
            dfs(i, visit)

def bfs(v, visit):
    
    queue = deque([v])
    visit[v] = True

    while queue:
        cur = queue.popleft()
        print(cur, end=' ')
        
        for i in sorted(graph[cur]):
            if not visit[i]: 
                visit[i] = True
                queue.append(i)


visit = [False] * (n+1)
dfs(v, visit)
print()
visit = [False] * (n+1)
bfs(v, visit)