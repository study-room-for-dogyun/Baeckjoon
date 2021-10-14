# https://www.acmicpc.net/problem/14891
from collections import deque

circle = [list(map(int, input())) for _ in range(4)]
K = int(input())
method = []
for i in range(K):
    num, d = map(int, input().split())
    method.append([num-1, d])


def rotate(l, d):
    if d == 1:
        temp = l[-1]
        for i in range(len(l)-1, 0, -1):
            l[i] = l[i-1]
        l[0] = temp
    else:
        temp = l[0]
        for i in range(len(l) - 1):
            l[i] = l[i+1]
        l[-1] = temp


for i in method:
    visited = [False] * 4
    q = deque([i])
    while q:
        num, d = q.popleft()
        visited[num] = True

        if num < 3 and not visited[num+1]:
            if circle[num][2] != circle[num+1][6]:
                q.append([num+1, -d])

        if 0 < num and not visited[num-1]:
            if circle[num][6] != circle[num-1][2]:
                q.append([num-1, -d])

        rotate(circle[num], d)

ans = 0
for i in range(4):
    ans += circle[i][0] * (2**i)
print(ans)
for i in circle:
    print(i)