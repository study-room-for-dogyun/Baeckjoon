# https://www.acmicpc.net/problem/14226
from collections import deque

s = int(input())

def bfs():
    check = [0] * 1001

    queue = deque()
    queue.append(1)

    while queue:
        cur = queue.popleft()

        if cur == s:
            return check[cur]

        if 1 < 2 * cur <= 1001:     # 붙여넣기
            check[2*cur] = check[cur] + 1
            queue.append(2*cur)

        if 1 < cur - 1 <= 1001:     # 1개 지우기
            check[cur-1] = check[cur] + 1
            queue.append(cur-1)


print(bfs())