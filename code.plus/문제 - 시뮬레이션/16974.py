# https://www.acmicpc.net/problem/16974

N, X = map(int, input().split())
burger = [0] * (N + 1)

# 버거 장수, 패티 수
burger[0] = [1, 1]

for i in range(1, N + 1):
    burger[i] = [2 * burger[i - 1][0] + 3, 2 * burger[i - 1][1] + 1]


def dfs(p):

    if
