# https://www.acmicpc.net/problem/16947

import sys
from collections import deque
sys.setrecursionlimit(10**9)

N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def is_rotate(start, x, depth):
    global visited, rotate

    for n in graph[x]:
        if n == start and depth > 1:
            rotate.add(n)
            return
        if not visited[n]:
            visited[n] = True
            is_rotate(start, n, depth + 1)
            visited[n] = False


def distance(start):
    global rotate

    visited = [False] * (N + 1)
    visited[start] = True
    q = deque([[start, 0]])
    while q:
        cur, d = q.popleft()
        if cur in rotate:
            return d

        for nxt in graph[cur]:
            if visited[nxt]:
                continue
            q.append([nxt, d + 1])
            visited[nxt] = True


# 순환선 찾기
rotate = set()
visited = [False] * (N + 1)
for i in range(1, N + 1):
    visited[i] = True
    is_rotate(i, i, 0)
    visited[i] = False

# 거리 체크
for i in range(1, N + 1):
    print(distance(i), end=' ')
