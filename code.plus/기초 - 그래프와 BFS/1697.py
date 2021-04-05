# https://www.acmicpc.net/problem/1697

from collections import deque

n, k = map(int, input().split())

def bfs():

    # 좌 우 순간이동 좌 순간이동 우
    queue = deque()
    queue.append(n)
    visited = [0] * 100000
    visited[n] = 1

    while queue:

        cur = queue.popleft()

        if cur == k:
            return (visited[cur] - 1)
        
        if 0 <= cur-1 <= 100000 and visited[cur-1] == 0:
            visited[cur-1] = visited[cur] + 1
            queue.append(cur-1)
        if 0 <= cur+1 <= 100000 and visited[cur+1] == 0:
            visited[cur+1] = visited[cur] + 1
            queue.append(cur+1)
        if 0 <= 2*cur <= 100000 and visited[2*cur] == 0:
            visited[2*cur] = visited[cur] + 1
            queue.append(2*cur)

    return False

print(bfs())