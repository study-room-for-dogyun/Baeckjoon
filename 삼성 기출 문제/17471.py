# https://www.acmicpc.net/problem/17471
from collections import deque
from itertools import combinations

N = int(input())
populations = [-1] + list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    info = list(map(int, input().split()))
    graph[i] = info[1:]

split_table = [-1] + [0] * N


def bfs(m, split_table):
    visited = [True] + [False] * N
    # 두 구역으로 나뉘었는지 확인
    for p in range(2):
        q = deque()

        for i in range(1, N + 1):
            if not visited[i] and split_table[i] == p:
                q.append(i)
                visited[i] = True
                break

        while q:
            cur = q.popleft()
            for next_node in m[cur]:
                if not visited[next_node] and split_table[next_node] == p:
                    q.append(next_node)
                    visited[next_node] = True

    # 두 개로 안 나눠졌으면.
    if False in visited:
        return False

    # 두 개로 나눠졌다면 각 구역의 인구수 합의 차를 리턴
    a, b = 0, 0
    for i in range(1, N + 1):
        if split_table[i] == 0:
            a += populations[i]
        elif split_table[i] == 1:
            b += populations[i]

    return abs(a - b)


ans = 10e9

for k in range(1, N):
    for i in combinations(range(1, N + 1), k):
        l = [-1] + [0] * N
        for a in i:
            l[a] = 1
        result = bfs(graph, l)
        if result is False:
            continue
        ans = min(ans, result)

print(ans if ans != 10e9 else -1)
