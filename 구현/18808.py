# https://www.acmicpc.net/problem/18808

N, M, K = map(int, input().split())
base = [[False] * M for _ in range(N)]
stickers = []
for _ in range(K):
    R, C = map(int, input().split())
    temp = [list(map(int, input().split())) for _ in range(R)]
    stickers.append(temp)


def check(arr):
    for i in range(N - len(arr) + 1):
        for j in range(M - len(arr[0]) + 1):
            return


for s in stickers:

    check(s)
