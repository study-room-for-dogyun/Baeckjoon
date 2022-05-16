# https://www.acmicpc.net/problem/15662

from collections import deque

T = int(input())
gear = [list(map(int, input())) for _ in range(T)]
K = int(input())


def rotate(num, direction):
    global gear

    if direction == 1:
        gear[num] = [gear[num][-1]] + gear[num][:-1]

    elif direction == -1:
        gear[num] = gear[num][1:] + [gear[num][0]]


for _ in range(K):
    n, d = map(int, input().split())
    visited = [False] * T
    visited[n - 1] = True

    q = deque([[n - 1, d]])
    while q:
        cur, cur_d = q.popleft()

        if cur < T - 1 and gear[cur][2] != gear[cur + 1][6] and not visited[cur + 1]:
            q.append([cur + 1, -cur_d])
            visited[cur + 1] = True

        if 0 < cur and gear[cur][6] != gear[cur - 1][2] and not visited[cur - 1]:
            q.append([cur - 1, -cur_d])
            visited[cur - 1] = True

        rotate(cur, cur_d)

answer = 0
for i in gear:
    if i[0] == 1:
        answer += 1

print(answer)
