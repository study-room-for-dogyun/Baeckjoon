# https://www.acmicpc.net/problem/2606

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

ans = 0
def dfs(v):
    global ans
    visited[v] = True
    
    for i in graph[v]:
        if visited[i] == False:
            ans += 1
            dfs(i)

dfs(1)
print(ans)