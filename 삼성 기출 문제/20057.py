# https://www.acmicpc.net/problem/20057

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
answer = 0


def sand(i, j, d):

    

    pass


# 1. 토네이도의 경로
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

x, y, d, t = N // 2, N // 2, 0, 1
check = True
while check:
    for _ in range(t):
        x += dx[d%4]
        y += dy[d%4]

        if x == 0 and y == 0:
            check = False
            break
        
        # function


    d += 1
    t = t+1 if d%2 == 0 else t
    