# https://www.acmicpc.net/problem/9205
from collections import deque

t = int(input())


def distance(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])


def bfs():
    q = deque([home])
    while q:
        cur = q.popleft()
        if distance(cur, festival) <= 1000:
            print("happy")
            return

        for i in range(n):
            if not visited[i]:
                if distance(shops[i], cur) <= 1000:
                    q.append(shops[i])
                    visited[i] = True
    print("sad")
    return


for _ in range(t):
    n = int(input())
    home = list(map(int, input().split()))
    shops = []
    for _ in range(n):
        temp = list(map(int, input().split()))
        shops.append(temp)
    festival = list(map(int, input().split()))

    visited = [False] * n
    bfs()
