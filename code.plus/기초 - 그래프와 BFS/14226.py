# https://www.acmicpc.net/problem/14226
from collections import deque

s = int(input())

def bfs():
    check = [0] * 1001

    queue = deque()
    queue.append(2)

    while queue:
        cur = queue.popleft()
        check[cur] = 2

        if check[s] != 0:
            return check[s]

        if 0 <= 2 * cur <= 1001:
            check[2*cur] = check[cur] + 2 
            queue.append(2*cur)

        if 0 <= cur - 1 <= 1001:
            check[cur-1] = check[cur] + 1
            queue.append(cur-1)

print(bfs())