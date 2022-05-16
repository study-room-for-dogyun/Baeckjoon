# https://www.acmicpc.net/problem/9466

T = int(input())


def dfs(start):
    global answer

    visited = [False] * len(std)
    s = [start]
    visited[start] = True

    while s:
        cur = s.pop()
        for n in graph[cur]:
            if visited[n]:
                continue
            if n == start or group[n]:
                answer += 1
                return
            s.append(n)
            visited[n] = True
    return


for _ in range(T):
    n = int(input())
    std = list(map(int, input().split()))
    graph = [[] for _ in range(len(std))]
    for idx, i in enumerate(std):
        graph[i - 1].append(idx)

    answer = 0
    group = [False] * len(std)
    for i in range(len(std)):
        if not group[i]:
            dfs(i)

    print(answer)
