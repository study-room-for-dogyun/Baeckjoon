# https://www.acmicpc.net/problem/10866

from collections import deque

N = int(input())
command = []
for _ in range(N):
    command.append(input().split(' '))

q = deque()
for c in command:
    if c[0] == 'push_front':
        q.appendleft(c[1])
    elif c[0] == 'push_back':
        q.append(c[1])
    elif c[0] == 'pop_front':
        print(q.popleft() if q else -1)
    elif c[0] == 'pop_back':
        print(q.pop() if q else -1)
    elif c[0] == 'size':
        print(len(q))
    elif c[0] == 'empty':
        print(0 if q else 1)
    elif c[0] == 'front':
        print(q[0] if q else -1)
    elif c[0] == 'back':
        print(q[-1] if q else -1)