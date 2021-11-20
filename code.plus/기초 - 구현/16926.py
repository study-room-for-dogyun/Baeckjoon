# https://www.acmicpc.net/problem/16926

N, M, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]


def rotate_layer(r1, c1, r2, c2):
    temp = A[r2][c1]
    # 왼쪽
    for i in range(r2, r1, -1):
        A[i][c1] = A[i - 1][c1]
    # 위
    for i in range(c1, c2):
        A[r1][i] = A[r1][i + 1]
    # 오른쪽
    for i in range(r1, r2):
        A[i][c2] = A[i + 1][c2]
    # 아래
    for i in range(c2, c1, -1):
        A[r2][i] = A[r2][i - 1]

    A[r2][c1 + 1] = temp


def rotate():
    r1, r2, c1, c2 = 0, N - 1, 0, M - 1
    while r1 < r2 and c1 < c2:
        rotate_layer(r1, c1, r2, c2)
        r1 += 1
        r2 -= 1
        c1 += 1
        c2 -= 1


for _ in range(R):
    rotate()

for i in A:
    print(" ".join(map(str, i)))
