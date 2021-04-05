# https://www.acmicpc.net/problem/13023

n, m = map(int, input().split())
<<<<<<< HEAD
graph = [list(map(int, input().split())) for _ in range(m)]

=======
graph = [[] for _ in range(n)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
       

def dfs(v, depth):
    global anw

    if depth == 4:
        anw = True
        return 

    visited[v] = True

    for n in graph[v]:
        if not visited[n]:
            dfs(n, depth+1)
            visited[n] = False


anw = False
visited = [False] * n

for i in range(len(graph)):
    dfs(i, 0)
    visited[i] = False

print(1 if anw else 0)
>>>>>>> d337d43d7e93782a7bbc74817729575c743e49fe
