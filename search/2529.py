# https://www.acmicpc.net/problem/2529

k = int(input())
l = list(map(str, input().split()))


maxi = [0]
mini = [100]

def dfs(depth, route, visited):
    global maxi, mini

    if depth == k:
        value = sum(route)
        if sum(maxi) < value:
            maxi = route
        
        if sum(mini) > value:
            mini = route

        return 

    for i in range(10):
        if visited[i]:
            continue

        if l[depth] == '<':
            if route[-1] < i:
                visited[i] = True
                dfs(depth+1, route+[i], visited)
                visited[i] = False
        else:
            if route[-1] > i:
                visited[i] = True
                dfs(depth+1, route+[i], visited)
                visited[i] = False


visited = [False] * 10
for i in range(10):
    visited[i] = True
    dfs(0, [i], visited)
    visited[i] = False

print(maxi, mini)