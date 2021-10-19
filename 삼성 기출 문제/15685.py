# https://www.acmicpc.net/problem/15685

N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]
graph = [[0]*101 for _ in range(101)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for x, y, d, g in info:

    graph[x][y] = 1

    move = [d]
    for _ in range(g):
        temp = []
        for i in move:
            temp.append((i+1)%4)
        temp.reverse()
        move = move + temp
        
    for i in move:
        nx, ny = x+dx[i], y+dy[i]
        graph[nx][ny] = 1
        x, y = nx, ny

ans = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] and graph[i+1][j] and graph[i][j+1] and graph[i+1][j+1]:
            ans += 1

print(ans)


# 이동 규칙을 찾는 게 힘들었다.
# 전체를 회전시킨다는 생각에 휘말렸다.
# 각 이동이 회전을 하면 방향 인덱스가 어떻게 바뀌는지 집중