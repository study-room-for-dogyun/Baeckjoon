# https://www.acmicpc.net/problem/20057

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
ans = 0


dx0 = [0, 0, 1, -1, 1, -1, 2, -2, 1, -1]
dy0 = [-1, -2, -1, -1, 0, 0, 0, 0, 1, 1]

dx1 = [1, 2, 1, 1, 0, 0, 0, 0, -1, -1]
dy1 = [0, 0, 1, -1, 1, -1, 2, -2, 1, -1]

dx2 = [0, 0, -1, 1, -1, 1, -2, 2, -1, 1]
dy2 = [1, 2, 1, 1, 0, 0, 0, 0, -1, -1]

dx3 = [-1, -2, -1, -1, 0, 0, 0, 0, 1, 1]
dy3 = [0, 0, 1, -1, 1, -1, 2, -2, 1, -1]

per = [0, 0.05, 0.1, 0.1, 0.07, 0.07, 0.02, 0.02, 0.01, 0.01]


def sand(d, x, y):
    global ans
    m = graph[x][y]
    graph[x][y] = 0

    temp = 0
    for i in range(1, 10):

        if d == 0:
            nx, ny = x+dx0[i], y+dy0[i]
        elif d == 1:
            nx, ny = x+dx1[i], y+dy1[i]
        elif d == 2:
            nx, ny = x+dx2[i], y+dy2[i]
        else:
            nx, ny = x+dx3[i], y+dy3[i]

        p = per[i]

        if not(0 <= nx < N and 0 <= ny < N):
            ans += int(m*p)
        else:
            graph[nx][ny] += int(m*p)
        temp += int(m*p)

    if d == 0:
        nx, ny = x+dx0[0], y+dy0[0]
    elif d == 1:
        nx, ny = x+dx1[0], y+dy1[0]
    elif d == 2:
        nx, ny = x+dx2[0], y+dy2[0]
    else:
        nx, ny = x+dx3[0], y+dy3[0]

    if not(0 <= nx < N and 0 <= ny < N):
        ans += m - temp
    else:
        graph[nx][ny] += m - temp


dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

X, Y = N//2, N//2
d, t = 0, 1

check = True
while check:

    for _ in range(t):
        X += dx[d % 4]
        Y += dy[d % 4]

        sand(d % 4, X, Y)

        if X == 0 and Y == 0:
            check = False
            break

    d += 1
    t = t+1 if d % 2 == 0 else t

print(ans)
