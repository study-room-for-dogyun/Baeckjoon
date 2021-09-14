# https://www.acmicpc.net/problem/2251
from collections import deque

a, b, c = map(int, input().split())
check = [False] * (c+1)

def bfs():

    q = deque([[0, 0, c]])
    check[c] = True

    while q:

        x, y, z = q.popleft()

        if check[z]:
            continue        

        if x == 0:
            check[z] = True
    