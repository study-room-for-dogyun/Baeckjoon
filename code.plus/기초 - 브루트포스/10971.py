# https://www.acmicpc.net/problem/10971

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

result = 10 ** 9

def dfs(x, visited):
    global total

    visited[x] = True

    for i in range(n):
        if graph[x][i] != 0 and not visited[i]:
            total += graph[x][i]
            dfs(i, visited)


for i in range(n):
    total = 0
    check = [False] * n
    dfs(i, check)

    print(total)