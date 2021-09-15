# https://www.acmicpc.net/problem/10971

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

mini = 10987654321

def dfs(visited, init, cur, depth, value):
    global mini

    if depth == n and graph[cur][init]:
        mini = min(mini, value+graph[cur][init])
        return

    for next in range(n):
        if not visited[next] and graph[cur][next] and next != init:
            visited[next] = True
            dfs(visited, init, next, depth+1, value+graph[cur][next])
            visited[next] = False

for start in range(n):
    visited = [False] * n
    dfs(visited, start, start, 1, 0)

print(mini)