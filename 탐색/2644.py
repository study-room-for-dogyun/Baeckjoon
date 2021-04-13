# https://www.acmicpc.net/problem/2644
from collections import deque

n = int(input())
x, y = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start, goal, visited):
    q = deque([start])
    visited[start] = 1

    while q:
        cur = q.popleft()

        for i in graph[cur]:
            if i == goal:
                return visited[cur]

            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[cur] + 1

    return -1

# bfs에서 깊이 측정할 때는 방문기록을 이전노드 + 1로 해주기
visited = [0] * (n+1)
print(bfs(y, x, visited))