# https://www.acmicpc.net/problem/2812

N, K = map(int, input().split())
num = input()
maxi = 0

def dfs(depth, value):
    global maxi

    if depth == K:
        maxi = max(maxi, int(value))
        return

    for i in range(len(value)):
        dfs(depth+1, value[:i] + value[i+1:])

dfs(0, num)
print(maxi)