# https://www.acmicpc.net/problem/17070

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
answer = 0

def dfs(x, y, m):
    global answer

    if [x, y] == [N-1, N-1]:
        answer += 1
        return

    # 0: 가로, 1: 세로, 2: 대각
    if m == 0 or m == 2:
        if y+1 < N and graph[x][y+1] != 1:
            dfs(x, y+1, 0)
            
    if m == 1 or m == 2:
        if x+1 < N and graph[x+1][y] != 1:
            dfs(x+1, y, 1)

    if x+1 < N and y+1 < N:
        if graph[x+1][y] != 1 and graph[x][y+1] != 1 and graph[x+1][y+1] != 1:
            dfs(x+1, y+1, 2)


dfs(0, 1, 0)
print(answer)
