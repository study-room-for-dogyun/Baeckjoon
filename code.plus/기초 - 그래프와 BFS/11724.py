# https://www.acmicpc.net/problem/11724
import sys

sys.setrecursionlimit(10000)
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


visited = [False] * (n+1)
def dfs(v):
    visited[v] = True

    for i in graph[v]:
        if visited[i] == False:
            dfs(i)


result = 0
for i in range(1, n+1):
    if visited[i] is False:
        dfs(i)
        result += 1

print(result)