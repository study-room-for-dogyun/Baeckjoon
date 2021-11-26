# https://www.acmicpc.net/problem/16967

H, W, X, Y = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(H + X)]

for i in range(X + H):
    for j in range(Y + W):
        if X <= i < X + H and Y <= j < Y + W:
            B[i][j] -= B[i - X][j - Y]

for i in range(H):
    for j in range(W):
        print(B[i][j], end=' ')
    print()
