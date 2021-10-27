# https://www.acmicpc.net/problem/20061

N = int(input())
graph = [[0] * 10 for _ in range(10)]


for _ in range(N):
    t, x, y = map(int, input().split())
