# https://www.acmicpc.net/problem/13549
from collections import deque

n, k = map(int, input().split())

def bfs(x):
    visit = [None] * 100001
    q = deque([x])
    visit[x] = 0

    while q:
        cur = q.popleft()

        if cur == k:
            print(visit[:20])
            return visit[cur]

        if 0 < 2 * cur < 100001 and visit[2*cur] == None:
            visit[2*cur] = visit[cur]
            q.append(2*cur)
        
        if 0 <= cur + 1 < 100001 and visit[cur+1] == None:
            visit[cur+1] = visit[cur]+1
            q.append(cur+1)
        
        if 0 <= cur - 1 < 100001 and visit[cur-1] == None:
            visit[cur-1] = visit[cur]+1
            q.append(cur-1)




print(bfs(n))