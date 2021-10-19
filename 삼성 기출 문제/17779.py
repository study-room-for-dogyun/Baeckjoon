# https://www.acmicpc.net/problem/17779

from itertools import product

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
ans = 10e9


def split_area(x, y, d1, d2):
    for i in range(d1 + 1):
        area[x + i][y - i] = 5
        area[x + d2 + i][y + d2 - i] = 5
    for i in range(d2 + 1):
        area[x + i][y + i] = 5
        area[x + d1 + i][y - d1 + i] = 5

    for r, row in enumerate(area):
        if 5 not in row:
            continue
        s, e = row.index(5), N - list(reversed(row)).index(5)
        for c in range(s, e):
            area[r][c] = 5

    for r in range(x + d1):
        for c in range(y + 1):
            if area[r][c] != 5:
                area[r][c] = 1

    for r in range(x + d2 + 1):
        for c in range(y + 1, N):
            if area[r][c] != 5:
                area[r][c] = 2

    for r in range(x + d1, N):
        for c in range(y - d1 + d2):
            if area[r][c] != 5:
                area[r][c] = 3

    for r in range(x + d2 + 1, N):
        for c in range(y - d1 + d2, N):
            if area[r][c] != 5:
                area[r][c] = 4


def counting():
    global ans

    people = [0] * 5
    for x in range(N):
        for y in range(N):
            people[area[x][y] - 1] += graph[x][y]

    ans = min(ans, max(people) - min(people))


for i, j in product(range(1, N + 1), range(1, N + 1)):
    for d1, d2 in product(range(1, N + 1), range(1, N + 1)):
        if 0 < i < i + d1 + d2 <= N and 0 < j - d1 < j < j + d2 <= N:
            area = [[0] * N for _ in range(N)]
            split_area(i - 1, j - 1, d1, d2)
            counting()

print(ans)
