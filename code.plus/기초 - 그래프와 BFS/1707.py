# https://www.acmicpc.net/problem/1707
from collections import deque
import sys

input = lambda: sys.stdin.readline().rstrip()

k = int(input())

def bfs(graph, check):
    queue = deque()
    for node in range(1, len(graph)):
        
        if check[node] != None:
            continue

        queue.append(node)
        
        while queue:
            cur = queue.popleft()
            if check[cur] == None:
                check[cur] = True

            for i in graph[cur]:
                if check[i] == check[cur]:
                    return "NO"

                if check[i] == None:
                    check[i] = not check[cur]
                    queue.append(i)   

    return "YES"
    

for i in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    check = [None] * (v+1)

    for _ in range(e):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    print(bfs(graph, check))
