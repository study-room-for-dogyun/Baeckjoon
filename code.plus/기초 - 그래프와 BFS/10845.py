# https://www.acmicpc.net/problem/10845

from collections import deque

N = int(input())
q = deque()
command = []

for _ in range(N):
    command.append(input().split(' '))

for c in command:
    if c[0] == 'push':
        q.append(c[1])
    elif c[0] == 'pop':
        print(q.popleft() if q else -1)
    elif c[0] == 'size':
        print(len(q))
    elif c[0] == 'empty':
        print(0 if q else 1)
    elif c[0] == 'front':
        print(q[0] if q else -1)
    elif c[0] == 'back':
        print(q[-1] if q else -1)