# https://www.acmicpc.net/problem/13549
from collections import deque

n, k = map(int, input().split())
MAX = 100001
visited = [-1] * MAX

q = deque([n])
visited[n] = 0

while q:
    cur = q.popleft()
    if 2*cur < MAX and visited[2*cur] == -1:
        q.appendleft(2*cur)
        visited[2*cur] = visited[cur]
        
    if 0 <= cur - 1 and visited[cur-1] == -1:
        q.append(cur-1)
        visited[cur-1] = visited[cur] + 1

    if cur + 1 < MAX and visited[cur+1] == -1:
        q.append(cur+1)
        visited[cur+1] = visited[cur] + 1

print(visited[k])