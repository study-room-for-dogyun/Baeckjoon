# https://www.acmicpc.net/problem/5014
from collections import deque

F, S, G, U, D = map(int, input().split())

floor = [F] * (F + 1)
floor[S] = 0

q = deque([S])

while q:
    cur = q.popleft()

    for i in [U, -D]:
        next_floor = cur + i

        if not (1 <= next_floor <= F):
            continue

        if floor[next_floor] > floor[cur] + 1:
            floor[next_floor] = floor[cur] + 1
            q.append(next_floor)

if floor[G] != F:
    print(floor[G])
else:
    print('use the stairs')
