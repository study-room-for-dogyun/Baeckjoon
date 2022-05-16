# https://www.acmicpc.net/problem/5430
from collections import deque

T = int(input())

for _ in range(T):
    p = input()
    n = int(input())
    arr = input()
    if len(arr) == 2:
        arr = []
    else:
        arr = deque(list(map(int, arr[1:-1].split(","))))

    check = False
    cur = True
    for idx, i in enumerate(p):
        if i == 'R':
            cur = not cur
        elif i == 'D':
            try:
                if cur:
                    arr.popleft()
                else:
                    arr.pop()
            except:
                print("error")
                check = True
                break

    if check:
        continue
    if cur:
        print(str(list(arr)).replace(' ', ''))
    else:
        print(str(list(reversed(arr))).replace(' ', ''))
