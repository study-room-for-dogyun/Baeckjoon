# https://www.acmicpc.net/problem/14501

n = int(input())
tp = [list(map(int, input().split())) for _ in range(n)]
result = 0


check = [False] * n

def dfs(x, visited, total):
    visited[x] = True

    

for i in range(n):
    result = max(result, dfs(i, check, 0))



print(result)