# https://www.acmicpc.net/problem/19237

N, M, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
shark_init_d = list(map(int, input().split()))
shark_info = [[list(map(int, input().split())) for _ in range(4)] for _ in range(4)]

# 방향
dx = [None, -1, 1, 0, 0]
dy = [None, 0, 0, -1, 1]


