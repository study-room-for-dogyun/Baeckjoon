# https://www.acmicpc.net/problem/2667

import sys
sys.setrecursionlimit(5000)

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

cnt = 0
def dfs(x, y):
    global cnt
    if x >= n or x < 0 or y >= n or y < 0:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0
        cnt += 1
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True
    
    return False

result = 0
count = []
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            result += 1
            count.append(cnt)
            cnt = 0


print(result)
for i in sorted(count):
    print(i)